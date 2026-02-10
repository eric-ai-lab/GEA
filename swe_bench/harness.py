import argparse
import datetime
import json
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import docker
from datasets import load_dataset

from prompts.testrepo_prompt import get_test_description
from swebench.harness.test_spec import make_test_spec
from swebench.harness.docker_build import build_env_images, build_container, cleanup_container

from swe_bench.utils import (
    copy_to_container,
    copy_from_container,
    log_container_output,
    remove_existing_container,
    safe_log,
    setup_logger,
)
from utils.common_utils import load_json_file

def process_entry(entry, out_dname, model_name_or_path, model_patch_paths):
    """
    Process a single dataset entry. This function encapsulates the main processing logic
    for each entry to make it suitable for parallel execution.
    """
    instance_id = entry['instance_id']
    problem_statement = entry['problem_statement']
    base_commit = entry['base_commit']
    chat_history_file = out_dname / (instance_id + ".md")
    out_fname = out_dname / (instance_id + ".json")
    eval_file = out_dname / f"{instance_id}_eval.sh"

    # Skip if output result already exists
    if out_fname.exists():
        print(f"Skipping existing entry {instance_id}")
        return {"success": True, "instance_id": instance_id}

    try:
        # Create and start the Docker container
        client = docker.from_env()
        run_id = datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f')
        # Set up thread-specific logger
        logger = setup_logger(str(out_dname / f"{instance_id}_docker.log"))
        nocache = True
        test_spec = make_test_spec(entry)
        # Remove any existing container with the same name
        container_name = test_spec.get_instance_container_name(run_id)
        remove_existing_container(client, container_name)
        # Now create and start the container
        container = build_container(test_spec, client, run_id, logger, nocache, force_rebuild=False)
        container.start()

        # Check that we are in dgm directory
        tmp_currdir = os.path.abspath(os.getcwd())
        logger.info(f"Current directory: {tmp_currdir}")
        # If not in dgm directory, try to change to it
        if not tmp_currdir.endswith('/dgm'):
            try:
                os.chdir('dgm')
                tmp_currdir = os.path.abspath(os.getcwd())
                logger.info(f"Changed directory to: {tmp_currdir}")
            except Exception as e:
                pass
        # If still not in dgm directory, go up until we find it
        while not tmp_currdir.endswith('/dgm'):
            os.chdir('..')
            tmp_currdir = os.path.abspath(os.getcwd())
            logger.info(f"Changed directory to: {tmp_currdir}")

        # Copy the necessary files and requirements to the container
        copy_to_container(container, 'coding_agent.py', '/dgm/coding_agent.py')
        copy_to_container(container, 'requirements.txt', '/dgm/requirements.txt')
        copy_to_container(container, 'pytest.ini', '/dgm/pytest.ini')
        copy_to_container(container, 'tools/', '/dgm/tools/')
        copy_to_container(container, 'utils/', '/dgm/utils/')
        copy_to_container(container, 'tests/', '/dgm/tests/')
        copy_to_container(container, 'prompts/', '/dgm/prompts/')
        copy_to_container(container, 'llm.py', '/dgm/llm.py')
        copy_to_container(container, 'llm_withtools.py', '/dgm/llm_withtools.py')
        chat_history_file_container = f'/dgm/{chat_history_file.name}'

        # Install issue requirements
        logger.info("Setting up environment")
        eval_script = test_spec.eval_script
        eval_file.write_text(eval_script)
        copy_to_container(container, eval_file, '/eval.sh')
        exec_result = container.exec_run("/bin/bash /eval.sh", workdir='/')  # setup environment
        log_container_output(exec_result)
        exec_result = container.exec_run("rm /eval.sh", workdir='/')  # remove eval script
        log_container_output(exec_result)

        # Get test description
        test_description = get_test_description(eval_script=eval_script, swerepo=True)

        # Apply model patch
        if model_patch_paths:
            safe_log("Applying model patches")
            for model_patch_path in model_patch_paths:
                copy_to_container(container, model_patch_path, '/dgm/parent_patch.txt')
                exec_result = container.exec_run("/bin/sh -c 'patch -p1 < /dgm/parent_patch.txt'", workdir='/dgm')
                log_container_output(exec_result)
                exec_result = container.exec_run("rm /dgm/parent_patch.txt", workdir='/dgm')
                log_container_output(exec_result)

        # Install this repo requirements
        safe_log("Installing more requirements")
        exec_result = container.exec_run("python -m pip install -r /dgm/requirements.txt", workdir='/')
        log_container_output(exec_result)

        # Run the agent
        coding_agent_claude_model = os.getenv('CODING_AGENT_CLAUDE_MODEL')
        env_vars = {
            "ANTHROPIC_API_KEY": os.getenv('ANTHROPIC_API_KEY'),
            "OPENAI_API_KEY": os.getenv('OPENAI_API_KEY'),
            "ZAI_API_KEY": os.getenv('ZAI_API_KEY'),
            "AWS_REGION": os.getenv('AWS_REGION'),
            "AWS_REGION_NAME": os.getenv('AWS_REGION_NAME'),
            "AWS_ACCESS_KEY_ID": os.getenv('AWS_ACCESS_KEY_ID'),
            "AWS_SECRET_ACCESS_KEY": os.getenv('AWS_SECRET_ACCESS_KEY'),
            "CODING_AGENT_CLAUDE_MODEL": coding_agent_claude_model,  # Pass Claude model selection to container
        }
        # Log which Claude model is being used
        if coding_agent_claude_model:
            safe_log(f"Using Claude model for coding agent: {coding_agent_claude_model}")
        else:
            safe_log("Using default Claude model for coding agent: Opus 4.5")
        safe_log("Running the agent")
        cmd = [
            "timeout", "10800",  # 3h timeout per instance
            "python", "/dgm/coding_agent.py",
            "--problem_statement", problem_statement,
            "--git_dir", "/testbed/",
            "--chat_history_file", chat_history_file_container,
            "--base_commit", base_commit,
            "--outdir", "/dgm/",
            "--test_description", test_description,
            "--instance_id", instance_id,
        ]
        exec_result = container.exec_run(cmd, environment=env_vars, workdir='/')
        log_container_output(exec_result, raise_error=False)

        # Check if the agent execution timed out or failed
        agent_failed = False
        failure_reason = None
        if exec_result.exit_code == 124:
            agent_failed = True
            failure_reason = "timeout"
            logger.warning(f"Agent execution timed out for {instance_id}")
        elif exec_result.exit_code and exec_result.exit_code != 0:
            agent_failed = True
            failure_reason = f"exit_code_{exec_result.exit_code}"
            logger.warning(f"Agent execution failed with exit code {exec_result.exit_code} for {instance_id}")

        # Copy output files back to host (try even if failed)
        logger.info("Copying output files back to host")
        try:
            copy_from_container(container, chat_history_file_container, chat_history_file)
            # Additional chat history files
            exec_result = container.exec_run(f"find /dgm/ -name '{instance_id}_*.md'", workdir='/')
            chat_history_files_container = exec_result.output.decode().split()
            for chat_history_file_container in chat_history_files_container:
                chat_history_file = out_dname / Path(chat_history_file_container).name
                copy_from_container(container, chat_history_file_container, chat_history_file)
        except Exception as e:
            logger.warning(f"Failed to copy chat history files: {e}")

        # Get model_patch (try even if failed)
        model_patch = ""
        proposed_model_patches = []
        try:
            logger.info("Getting model_patch")
            exec_result = container.exec_run("cat /dgm/model_patch.diff")
            log_container_output(exec_result, raise_error=False)
            if exec_result.exit_code == 0:
                model_patch = exec_result.output.decode()
            # Additional proposed model patches
            exec_result = container.exec_run("find /dgm/ -name 'model_patch_*.diff'", workdir='/')
            if exec_result.exit_code == 0:
                model_patch_files_container = exec_result.output.decode().split()
                for model_patch_file_container in model_patch_files_container:
                    exec_result = container.exec_run(f"cat {model_patch_file_container}")
                    log_container_output(exec_result, raise_error=False)
                    if exec_result.exit_code == 0:
                        proposed_model_patch = exec_result.output.decode()
                        proposed_model_patches.append(proposed_model_patch)
        except Exception as e:
            logger.warning(f"Failed to get model_patch: {e}")

        # Write result to file (always generate JSON, even for failures)
        result = {
            "instance_id": instance_id,
            "model_name_or_path": model_name_or_path,
            "model_patch": model_patch,
            'proposed_model_patches': proposed_model_patches,
        }
        
        # Add failure information if the agent failed
        if agent_failed:
            result["success"] = False
            result["failure_reason"] = failure_reason
            result["exit_code"] = exec_result.exit_code
        else:
            result["success"] = True
        
        out_fname.write_text(json.dumps(result, indent=4))
        logger.info(f"Generated JSON file for {instance_id} (success: {not agent_failed})")

        return {"success": not agent_failed, "instance_id": instance_id}

    except Exception as e:
        print(f"Error processing entry {instance_id}: {str(e)}")
        if 'logger' in locals():
            logger.error(f"Exception processing entry {instance_id}: {str(e)}")
        
        # Generate a JSON file even for exceptions to ensure all tasks are counted
        try:
            result = {
                "instance_id": instance_id,
                "model_name_or_path": model_name_or_path,
                "model_patch": "",
                "proposed_model_patches": [],
                "success": False,
                "failure_reason": "exception",
                "error": str(e),
            }
            out_fname.write_text(json.dumps(result, indent=4))
            if 'logger' in locals():
                logger.info(f"Generated JSON file for failed entry {instance_id}")
        except Exception as json_error:
            if 'logger' in locals():
                logger.error(f"Failed to generate JSON file for {instance_id}: {json_error}")
        
        return {"success": False, "instance_id": instance_id, "error": str(e)}

    finally:
        # Clean up docker container
        try:
            if 'container' in locals() and 'client' in locals():
                cleanup_logger = logger if 'logger' in locals() else None
                cleanup_container(client, container, cleanup_logger)
        except Exception as e:
            print(f"Error cleaning up Docker container for {instance_id}: {e}")

def harness(
        test_task_list=None,
        num_samples=-1,
        max_workers=4,
        model_name_or_path=None,
        model_patch_paths=None,
        num_evals=1,
        num_evals_parallel=1,
        pred_dname='./swe_bench/predictions',
    ):
    """
    Parallel processing harness using ThreadPoolExecutor.
    
    Args:
        test_task_list: List of task IDs to process (None for all)
        num_samples: Number of samples to process (-1 for all)
        max_workers: Maximum number of concurrent threads
        model_name_or_path: Model name or path
        model_patch_paths: Paths to the model patches for dgm
        num_evals: Repeated number of swe evaluations
    """
    # Load dataset
    dataset = load_dataset("princeton-nlp/SWE-bench_Verified")
    dataset = dataset['test']
    
    # Ensure that necessary directories exist
    if model_name_or_path is None:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        model_name_or_path = f"{timestamp}--claude-3-5-haiku-20241022"  # ✅ Haiku 3.5 - 快速且高性价比
    pred_dname = Path(pred_dname)
    pred_dname.mkdir(exist_ok=True)
    out_dnames = []
    
    # Prepare the dataset entries
    entries = list(dataset)
    if test_task_list:
        entries = [entry for entry in entries if entry['instance_id'] in test_task_list]
    if num_samples > 0:
        entries = entries[:num_samples]

    # Build the environment images
    client = docker.from_env()
    build_env_images(client, dataset=entries, force_rebuild=False, max_workers=max_workers)
    
    # Define a function to handle a single evaluation for all specified issues
    def process_evaluation(eval_idx):
        model_name_or_path_inst = f"{model_name_or_path}_{eval_idx}"
        out_dname = pred_dname / model_name_or_path_inst
        out_dname.mkdir(exist_ok=True)
        
        print(f"Starting evaluation {eval_idx} for model {model_name_or_path}")
        
        # Process entries in parallel
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit all tasks
            future_to_entry = {
                executor.submit(process_entry, entry, out_dname, model_name_or_path_inst, model_patch_paths): entry
                for entry in entries
            }
            
            # Process completed tasks as they finish
            for future in as_completed(future_to_entry):
                result = future.result()
                if result["success"]:
                    print(f"Successfully processed entry {result['instance_id']} for eval {eval_idx}")
                else:
                    print(f"Failed to process entry {result['instance_id']} for eval {eval_idx}: {result.get('error', 'Unknown error')}")
        return out_dname

    # Process all evaluations in parallel
    with ThreadPoolExecutor(max_workers=num_evals_parallel) as eval_executor:
        out_dnames = list(eval_executor.map(process_evaluation, range(num_evals)))

    print(f"All evaluations completed for model {model_name_or_path}")
    return out_dnames

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--num_samples", type=int, default=-1, help="Number of samples to process")
    parser.add_argument("--max_workers", type=int, default=4, help="Maximum number of concurrent threads")
    parser.add_argument("--model_name_or_path", type=str, default=None, help="Model name or path")
    parser.add_argument("--model_patch_paths", type=str, default=None, help="Paths to the model patches")
    parser.add_argument("--num_evals", type=int, default=1, help="Repeated number of swe evaluations")
    parser.add_argument("--num_evals_parallel", type=int, default=1, help="Number of parallel repeated evaluations")
    parser.add_argument("--pred_dname", type=str, default="./swe_bench/predictions", help="Output directory for predictions")
    parser.add_argument("--test_task_list", type=str, default=None, help="Subset of swe issues to process")
    args = parser.parse_args()
    
    # Load the test task list
    if args.test_task_list == 'small':
        test_task_list = load_json_file("./swe_bench/subsets/small.json")
    elif args.test_task_list == 'medium':
        test_task_list = load_json_file("./swe_bench/subsets/medium.json")
    else:
        # Default to None, means all of them
        test_task_list = None

    # Run the parallel harness
    harness(
        test_task_list=test_task_list,
        num_samples=args.num_samples,
        max_workers=args.max_workers,
        model_name_or_path=args.model_name_or_path,
        model_patch_paths=args.model_patch_paths,
        num_evals=args.num_evals,
        num_evals_parallel=args.num_evals_parallel,
        pred_dname=args.pred_dname,
    )

if __name__ == "__main__":
    main()
