import argparse
import datetime
import json
import os
import docker

from llm import create_client, get_response_from_llm, extract_json_between_markers
from prompts.self_improvement_prompt import get_diagnose_prompt_polyglot, get_diagnose_prompt_swe, get_problem_description_prompt
from prompts.diagnose_improvement_prompt import get_diagnose_improvement_prompt
from prompts.testrepo_prompt import get_test_description
from swe_bench.harness import harness
from polyglot.harness import harness as polyglot_harness
from swe_bench.report import make_report
from utils.common_utils import load_json_file, ensure_patch_file_newline
from utils.evo_utils import get_model_patch_paths, get_all_performance, is_compiled_self_improve, build_task_success_vector
from utils.docker_utils import (
    build_dgm_container,
    cleanup_container,
    copy_from_container,
    copy_to_container,
    log_container_output,
    remove_existing_container,
    setup_logger,
    safe_log,
)

dataset = None
diagnose_model = 'o1-2024-12-17'

def get_bedrock_model_name(claude_model):
    """Convert short claude model names to full bedrock model names"""
    model_mapping = {
        'claude_haiku_4.5': 'bedrock/global.anthropic.claude-haiku-4-5-20251001-v1:0',
        'claude_sonnet_4.5': 'bedrock/us.anthropic.claude-sonnet-4-5-20250929-v1:0',
    }
    return model_mapping.get(claude_model, claude_model)

def _get_task_logs_for_parent(dgm_output_dir, parent_commit, task_id):
    """
    Get specific task logs for a parent agent.
    This function mimics the logic from find_selfimprove_eval_logs.
    """
    try:
        # Import the function from prompts module
        from prompts.self_improvement_prompt import find_selfimprove_eval_logs, process_selfimprove_eval_logs
        
        # For 'initial' parent, we need to handle it differently
        if parent_commit == 'initial':
            # For initial parent, we don't have specific task logs
            # Return a generic message indicating this is the initial agent
            return f"""
Task ID: {task_id}
Parent Commit: {parent_commit}

Note: This is the initial agent, so no specific task logs are available.
The initial agent represents the baseline DGM codebase before any improvements.
"""
        
        # Construct the output directory path for the parent
        parent_output_dir = os.path.join(dgm_output_dir, parent_commit)
        
        # Get task logs using the same logic as choose_selfimproves
        md_logs, eval_logs, predicted_patches, eval_results = find_selfimprove_eval_logs(
            task_id, parent_output_dir, commit_id=parent_commit
        )
        
        # Process the logs to get the final content
        md_log, eval_log, predicted_patch, eval_result = process_selfimprove_eval_logs(
            md_logs, eval_logs, predicted_patches, eval_results
        )
        
        # Combine all log information
        combined_log = f"""
Task ID: {task_id}
Parent Commit: {parent_commit}

Agent Execution Log:
{md_log}

Test Results:
{eval_log}

Predicted Patch:
{predicted_patch}

Evaluation Result:
{eval_result}
"""
        return combined_log
        
    except Exception as e:
        # Fallback: return basic information if specific task logs are not available
        return f"Task ID: {task_id}\nParent Commit: {parent_commit}\nError retrieving task logs: {str(e)}"

def diagnose_problem(entry, commit, root_dir, out_dir, patch_files=[], max_attempts=3, polyglot=False, group_improve=False, entry1=None, commit1=None, patch_files1=None, claude_model=None, diagnose_model=None):
    # Use diagnose_model parameter if provided, otherwise fallback to claude_model, otherwise use global diagnose_model
    # Store parameter in local variable to avoid shadowing global variable
    diagnose_model_param = diagnose_model
    if diagnose_model_param:
        model_to_use = get_bedrock_model_name(diagnose_model_param)
    elif claude_model:
        model_to_use = get_bedrock_model_name(claude_model)
    else:
        # Access the global variable using globals() to avoid conflict with parameter name
        model_to_use = globals()['diagnose_model']  # This refers to the global variable 'diagnose_model' = 'o1-2024-12-17'
    client = create_client(model_to_use)
    
#     # Handle group improvement entries
#     if entry in ['group_p1', 'group_p2', 'group_p1_p2']:
#         # Parse the commit string to extract parent commits and tasks
#         commit_parts = commit.split('+')
#         safe_log(f"这里是self_improve_step.py的diagnose_problem函数")
#         safe_log(f"entry: {entry}")
#         safe_log(f"commit: {commit}")
#         safe_log(f"commit_parts: {commit_parts}")
#         safe_log(f"root_dir: {root_dir}")
#         safe_log(f"out_dir: {out_dir}")
#         safe_log(f"patch_files: {patch_files}")
#         safe_log(f"max_attempts: {max_attempts}")
#         safe_log(f"polyglot: {polyglot}")
#         safe_log(f"commit_parts: {commit_parts}")
        
#         if entry == 'group_p1_p2' and len(commit_parts) >= 4:
#             # Combined parent (p1+p2) with specific tasks
#             # Format: "p1+p2+task1+task2"
#             p1_commit, p2_commit, p1_task, p2_task = commit_parts[0], commit_parts[1], commit_parts[2], commit_parts[3]
            
#             # Load specific task logs from both parents using find_selfimprove_eval_logs
#             dgm_output_dir = os.path.dirname(root_dir)  # 获取DGM输出目录
            
#             # Get task logs for p1
#             p1_logs = _get_task_logs_for_parent(dgm_output_dir, p1_commit, p1_task)
            
#             # Get task logs for p2  
#             p2_logs = _get_task_logs_for_parent(dgm_output_dir, p2_commit, p2_task)
            
#             # Combine logs
#             combined_log = f"=== Parent 1 ({p1_commit}) Task: {p1_task} ===\n{p1_logs}\n\n"
#             combined_log += f"=== Parent 2 ({p2_commit}) Task: {p2_task} ===\n{p2_logs}\n\n"
            
#             # Create a special prompt for combined analysis
#             diagnose_sys_message = "You are an expert software engineer analyzing combined task logs from two parent agents to identify improvement opportunities."
#             diagnose_prompt = f"""
# Analyze the following combined task logs from two parent agents and identify the most promising improvement opportunities:

# {combined_log}

# Based on the analysis of both parent agents' performance on their respective tasks, identify:
# 1. Common failure patterns across both agents
# 2. Complementary strengths that could be combined
# 3. Specific improvement opportunities
# 4. Recommended changes to the codebase

# Provide your analysis in JSON format with the following structure:
# {{
#     "analysis": "Detailed analysis of the combined task logs",
#     "improvement_opportunities": ["List of specific improvements"],
#     "recommended_changes": "Specific code changes to implement"
# }}
# """
#         elif entry in ['group_p1', 'group_p2'] and len(commit_parts) >= 2:

#             safe_log(f"diagnose_sys_message: {diagnose_sys_message}")
#             safe_log(f"diagnose_prompt: {diagnose_prompt}\n")
#             # Single parent (p1 or p2) with specific task
#             parent_commit, parent_task = commit_parts[0], commit_parts[1]
#             safe_log(f"entry in ['group_p1', 'group_p2'] and len(commit_parts) >= 2")
#             safe_log(f"parent_commit: {parent_commit}")
#             safe_log(f"parent_task: {parent_task}\n")
            
#             # Load specific task log for the parent
#             dgm_output_dir = os.path.dirname(root_dir)  # 获取DGM输出目录
#             parent_logs = _get_task_logs_for_parent(dgm_output_dir, parent_commit, parent_task)
#             diagnose_sys_message, diagnose_prompt = get_diagnose_prompt_swe(
#             parent_task, parent_commit, root_dir, out_dir, dataset,
#             patch_files=patch_files,
#             )
# #             diagnose_sys_message = "You are an expert software engineer analyzing a parent agent's task log to identify improvement opportunities."
# #             diagnose_prompt = f"""
# # Analyze the following parent agent task log and identify improvement opportunities:

# # === Parent ({parent_commit}) Task: {parent_task} ===
# # {parent_logs}

# # Based on this analysis, identify:
# # 1. Failure patterns and their causes
# # 2. Performance bottlenecks
# # 3. Specific improvement opportunities
# # 4. Recommended changes to the codebase

# # Provide your analysis in JSON format with the following structure:
# # {{
# #     "analysis": "Detailed analysis of the parent task log",
# #     "improvement_opportunities": ["List of specific improvements"],
# #     "recommended_changes": "Specific code changes to implement"
# # }}
# # """
#         else:
#             # Fallback to old format (backward compatibility)
#             if '+' in commit:
#                 # This is a combined parent (p1+p2) - old format
#                 p1_commit, p2_commit = commit.split('+')
#                 dgm_output_dir = os.path.dirname(root_dir)
#                 p1_log_path = os.path.join(dgm_output_dir, p1_commit, "self_improve.log")
#                 p2_log_path = os.path.join(dgm_output_dir, p2_commit, "self_improve.log")
                
#                 combined_log = ""
#                 if os.path.exists(p1_log_path):
#                     with open(p1_log_path, 'r') as f:
#                         combined_log += f"=== Parent 1 ({p1_commit}) Log ===\n{f.read()}\n\n"
#                 if os.path.exists(p2_log_path):
#                     with open(p2_log_path, 'r') as f:
#                         combined_log += f"=== Parent 2 ({p2_commit}) Log ===\n{f.read()}\n\n"
                
#                 diagnose_sys_message = "You are an expert software engineer analyzing combined logs from two parent agents to identify improvement opportunities."
#                 diagnose_prompt = f"""
# Analyze the following combined logs from two parent agents and identify the most promising improvement opportunities:

# {combined_log}

# Based on the analysis of both parent agents' performance, identify:
# 1. Common failure patterns across both agents
# 2. Complementary strengths that could be combined
# 3. Specific improvement opportunities
# 4. Recommended changes to the codebase

# Provide your analysis in JSON format with the following structure:
# {{
#     "analysis": "Detailed analysis of the combined logs",
#     "improvement_opportunities": ["List of specific improvements"],
#     "recommended_changes": "Specific code changes to implement"
# }}
# """
#             else:
#                 # Single parent - old format
#                 dgm_output_dir = os.path.dirname(root_dir)
#                 parent_log_path = os.path.join(dgm_output_dir, commit, "self_improve.log")
#                 if os.path.exists(parent_log_path):
#                     with open(parent_log_path, 'r') as f:
#                         parent_log = f.read()
#                 else:
#                     parent_log = "No parent log found"
                
#                 diagnose_sys_message = "You are an expert software engineer analyzing a parent agent's log to identify improvement opportunities."
#                 diagnose_prompt = f"""
# Analyze the following parent agent log and identify improvement opportunities:

# {parent_log}

# Based on this analysis, identify:
# 1. Failure patterns and their causes
# 2. Performance bottlenecks
# 3. Specific improvement opportunities
# 4. Recommended changes to the codebase

# Provide your analysis in JSON format with the following structure:
# {{
#     "analysis": "Detailed analysis of the parent log",
#     "improvement_opportunities": ["List of specific improvements"],
#     "recommended_changes": "Specific code changes to implement"
# # }}
# """
    if group_improve:
        if polyglot: #这个先不修改，还没用上polyglot
            diagnose_sys_message, diagnose_prompt = get_diagnose_prompt_polyglot(
            entry, commit, root_dir, out_dir, dataset,
            patch_files=patch_files,
            commit1=commit1,
        )
        else: #group_improve为True,输入需要处理两个entry和两个commit
            diagnose_sys_message, diagnose_prompt = get_diagnose_prompt_swe(
            entry, commit, root_dir, out_dir, dataset,
            patch_files=patch_files,
            group_improve=True,
            entry1_id=entry1,
            commit1=commit1,
            patch_files1=patch_files1,
        )
    elif polyglot:
        diagnose_sys_message, diagnose_prompt = get_diagnose_prompt_polyglot(
            entry, commit, root_dir, out_dir, dataset,
            patch_files=patch_files,
        )
    else:
        print(f"这里是self_improve_step.py的diagnose_problem函数268行，进入selfimprove流程或者group_improve分支中的p1/p2分支,非polyglot，混合父代是否开启: {group_improve}，查看参数,entry: {entry},commit: {commit},root_dir: {root_dir},out_dir: {out_dir},patch_files: {patch_files},max_attempts: {max_attempts},polyglot: {polyglot},dataset: {dataset}")
        # safe_log(f"entry: {entry}")
        # safe_log(f"commit: {commit}")
        # safe_log(f"root_dir: {root_dir}")
        # safe_log(f"out_dir: {out_dir}")
        # safe_log(f"patch_files: {patch_files}")
        # safe_log(f"max_attempts: {max_attempts}")
        # safe_log(f"polyglot: {polyglot}")
        # safe_log(f"dataset: {dataset}")
        diagnose_sys_message, diagnose_prompt = get_diagnose_prompt_swe(
            entry, commit, root_dir, out_dir, dataset,
            patch_files=patch_files,
        )
    try:
        response, msg_history = get_response_from_llm(
            msg=diagnose_prompt,
            client=client[0],
            model=client[1],
            system_message=diagnose_sys_message,
            print_debug=False,
            msg_history=None,
        )
        safe_log(f"Message history: {msg_history}")
        response_json = extract_json_between_markers(response)
        assert response_json, "empty response json"
        problem_statement = get_problem_description_prompt(response_json, polyglot)
    except Exception as e:
        # Exception most probably due to not having json in the response
        safe_log(f"Error while diagnosing the problem: {e}")
        if max_attempts > 0:
            return diagnose_problem(
                entry, commit, root_dir, out_dir,
                patch_files=patch_files,
                claude_model=claude_model,
                diagnose_model=diagnose_model,
                max_attempts=max_attempts-1,
                polyglot=polyglot,
            )
        else:
            return None
    return problem_statement

def diagnose_improvement(
        entry, parent_commit, root_dir, model_patch_file, out_dir, run_id,
        patch_files=[], max_attempts=3, diagnose_model=None,
    ):
    """
    Diagnose the improvement of the model patch.

    Args:
        entry (str): The task entry to improve.
        parent_commit (str): The commit hash of the parent commit.
        root_dir (str): The root directory of the repository.
        model_patch_file (str): The path to the model patch file.
        out_dir (str): The output directory.
        run_id (str): The run id of the self-improvement attempt.
        patch_files (list): The list of patch files before self-improvement.
        max_attempts (int): The maximum number of attempts to diagnose the improvement.
        diagnose_model (str): Model to use for diagnose. If None, uses the global diagnose_model variable.
    
    Returns:
        dict: The improvement diagnosis.
    """
    # Use diagnose_model parameter if provided, otherwise use global diagnose_model variable
    # Note: 'diagnose_model' is both a parameter name and a global variable name
    # Store parameter value in a local variable to avoid shadowing
    diagnose_model_param = diagnose_model
    if diagnose_model_param:
        model_to_use = get_bedrock_model_name(diagnose_model_param)
    else:
        # Access the global variable using globals() to avoid conflict with parameter name
        model_to_use = globals()['diagnose_model']  # This refers to the global variable 'diagnose_model' = 'o1-2024-12-17'
    client = create_client(model_to_use)
    diagnose_sys_message, diagnose_prompt = get_diagnose_improvement_prompt(
        entry, parent_commit, root_dir, model_patch_file, out_dir, run_id, dataset,
        patch_files=patch_files,
    )
    safe_log(f"Diagnosing the improvement: {diagnose_prompt}")
    try:
        response, msg_history = get_response_from_llm(
            msg=diagnose_prompt,
            client=client[0],
            model=client[1],
            system_message=diagnose_sys_message,
            print_debug=False,
            msg_history=None,
        )
        safe_log(f"Message history: {msg_history}")
        response_json = extract_json_between_markers(response)
        assert response_json, "empty response json"
        improvement_diagnosis = response_json
    except Exception as e:
        # Exception most probably due to not having json in the response
        safe_log(f"Error while diagnosing the improvement: {e}")
        if max_attempts > 0:
            return diagnose_improvement(
                entry, parent_commit, root_dir, model_patch_file, out_dir, run_id,
                patch_files=patch_files, max_attempts=max_attempts-1, diagnose_model=diagnose_model,
            )
        else:
            return None
    return improvement_diagnosis

def save_metadata(metadata, output_dir):
    metadata_file = os.path.join(output_dir, "metadata.json")
    with open(metadata_file, 'w') as f:
        json.dump(metadata, f, indent=4)

def run_harness_swe(entry, model_name_or_path, patch_files, num_evals, output_dir, metadata, run_id, test_more_threshold, test_task_list, test_task_list_more):
    safe_log('Start harness')
    test_task_list = [entry] if test_task_list is None else test_task_list
    dnames = harness(
        test_task_list=test_task_list,
        num_samples=-1,
        max_workers=min(5, len(test_task_list)),
        model_name_or_path=model_name_or_path,
        model_patch_paths=patch_files,
        num_evals=num_evals,
        num_evals_parallel=5,
        pred_dname=os.path.join(output_dir, "predictions"),
    )
    metadata['swe_dnames'] = [str(dn) for dn in dnames]
    safe_log('Start make_report')
    make_report(
        dnames,
        run_ids=[f"{run_id}_{i}" for i in range(len(dnames))],
        dataset_name="princeton-nlp/SWE-bench_Verified",
        output_dir=output_dir,
        dnames_workers=5,
    )
    safe_log('Start get_performance')
    performances, overall_performance = get_all_performance(model_name_or_path, results_dir=output_dir)
    metadata['overall_performance'] = overall_performance
    safe_log("End of evaluation")

    # Check if additional evaluation should be run
    if (overall_performance and \
        test_more_threshold is not None and test_task_list_more is not None and \
            overall_performance.get('total_resolved_instances', 0) >= len(test_task_list) * test_more_threshold):
        safe_log("Start additional evaluation cycle")
        dnames = harness(
            test_task_list=test_task_list_more,
            num_samples=-1,
            max_workers=min(5, len(test_task_list_more)),
            model_name_or_path=model_name_or_path,
            model_patch_paths=patch_files,
            num_evals=num_evals,
            num_evals_parallel=5,
            pred_dname=os.path.join(output_dir, "predictions"),
        )
        safe_log('Start make_report more')
        make_report(
            dnames,
            run_ids=[f"{run_id}_{i}" for i in range(len(dnames))],
            dataset_name="princeton-nlp/SWE-bench_Verified",
            output_dir=output_dir,
            dnames_workers=5,
        )
        safe_log('Start get_performance')
        performances, overall_performance = get_all_performance(model_name_or_path, results_dir=output_dir)
        metadata['overall_performance'] = overall_performance
        safe_log("End of evaluation more")

def run_harness_polyglot(entry, model_name_or_path, patch_files, num_evals, output_dir, metadata, run_id, test_more_threshold, test_task_list, test_task_list_more):
    safe_log('Start harness')
    test_task_list = [entry] if test_task_list is None else test_task_list
    safe_log(f'workers {min(10, len(test_task_list))}')
    dnames = polyglot_harness(
        test_task_list=test_task_list,
        num_samples=-1,
        max_workers=min(10, len(test_task_list)),
        model_name_or_path=model_name_or_path,
        model_patch_paths=patch_files,
        num_evals=num_evals,
        num_evals_parallel=min(5, num_evals),
        pred_dname=os.path.join(output_dir, "predictions"),
        output_dir=output_dir
    )
    metadata['swe_dnames'] = [str(dn) for dn in dnames]
    safe_log('Start get_performance')
    performances, overall_performance = get_all_performance(model_name_or_path, results_dir=output_dir)
    metadata['overall_performance'] = overall_performance
    safe_log("End of evaluation")

    # Check if additional evaluation should be run
    if (overall_performance and \
        test_more_threshold is not None and test_task_list_more is not None and \
            overall_performance.get('total_resolved_instances', 0) >= len(test_task_list) * test_more_threshold):
        safe_log("Start additional evaluation cycle")
        dnames = polyglot_harness(
            test_task_list=test_task_list_more,
            num_samples=-1,
            max_workers=50,
            model_name_or_path=model_name_or_path,
            model_patch_paths=patch_files,
            num_evals=num_evals,
            num_evals_parallel=min(5, num_evals),
            pred_dname=os.path.join(output_dir, "predictions"),
            output_dir=output_dir
        )
        # metadata['swe_dnames'] = [str(dn) for dn in dnames]
        safe_log('Start get_performance')
        performances, overall_performance = get_all_performance(model_name_or_path, results_dir=output_dir)
        metadata['overall_performance_deep'] = overall_performance
        safe_log("End of evaluation more")

def self_improve(
    parent_commit='initial',  # 'initial' if starting from original dgm, else the run_id
    output_dir='output_selfimprove/',
    force_rebuild=False,
    num_evals=1,
    post_improve_diagnose=True,
    entry=None,
    test_task_list=None,  # None means the entry above only
    # Additional evaluation parameters
    test_more_threshold=None,
    test_task_list_more=None,
    full_eval_threshold=None,
    # Run baseline
    run_baseline=None,
    polyglot=False,
    group_improve=False,
    claude_model=None,  # Claude model to use for coding agent
    diagnose_model=None  # Model to use for diagnose (problem diagnosis and improvement diagnosis)
):  

    global dataset
    if polyglot:
        with open("polyglot/polyglot_benchmark_metadata.json") as f:
            dataset = json.loads(f.read())
    else:
        from datasets import load_dataset
        dataset = load_dataset("princeton-nlp/SWE-bench_Verified")
        dataset = dataset['test']

    # Variables for this self-improvement attempt
    metadata = {}
    root_dir = os.path.abspath('./')  # root_dir should be /dgm
    run_id = datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f')
    out_dir_base = output_dir  # out_dir_base should be /dgm/output_selfimprove/ or /dgm/output_dgm/{dgm_run_id}/
    output_dir = os.path.join(root_dir, f"{output_dir}/{run_id}/")
    os.makedirs(output_dir, exist_ok=True)
    metadata['run_id'] = run_id
    metadata['parent_commit'] = parent_commit
    test_task_list_big = load_json_file("./swe_bench/subsets/big.json")

    # Set up logger
    logger = setup_logger(os.path.join(output_dir, "self_improve.log"))

    # Create and start the Docker container
    image_name = "dgm"
    container_name = f"dgm-container-{run_id}"
    client = docker.from_env()
    # Remove any existing container with the same name
    remove_existing_container(client, container_name)
    # Now create and start the container
    container = build_dgm_container(
        client, root_dir, image_name, container_name,
        force_rebuild=force_rebuild,
    )
    container.start()

    if polyglot:
        # remove the swe version of coding_agent.py
        exec_result = container.exec_run("rm /dgm/coding_agent.py", workdir='/')
        log_container_output(exec_result)
        # rename coding_agent_polyglot.py to coding_agent.py
        exec_result = container.exec_run("mv /dgm/coding_agent_polyglot.py /dgm/coding_agent.py", workdir='/')
        log_container_output(exec_result)
        # remove swe-specific files utils/eval_utils.py and utils/swe_log_parsers.py
        exec_result = container.exec_run("rm /dgm/utils/eval_utils.py", workdir='/')
        log_container_output(exec_result)
        exec_result = container.exec_run("rm /dgm/utils/swe_log_parsers.py", workdir='/')
        log_container_output(exec_result)
    else:
        # remove the polyglot version of coding_agent.py
        exec_result = container.exec_run("rm /dgm/coding_agent_polyglot.py", workdir='/')

    # safe_log(f"这里是self_improve_step.py的self_improve函数")
    # safe_log(f"entry: {entry}")
    # Handle group improvement parent_commit parsing
    # if entry in ['group_p1', 'group_p2', 'group_p1_p2']:
    #     # Parse the parent_commit to extract the actual parent commit(s)
    #     if entry == 'group_p1_p2' and '+' in parent_commit:
    #         # For combined parents, use the first parent as the base
    #         parts = parent_commit.split('+')
    #         if len(parts) >= 2:
    #             actual_parent_commit = parts[0]  # Use first parent as base
    #             safe_log(f"Group improvement: using {actual_parent_commit} as base for combined evolution")
    #         else:
    #             actual_parent_commit = parent_commit
    #     elif entry in ['group_p1', 'group_p2'] and '+' in parent_commit:
    #         # For single parent, extract the parent commit
    #         parts = parent_commit.split('+')
    #         if len(parts) >= 2:
    #             actual_parent_commit = parts[0]  # Use the parent commit
    #             safe_log(f"Group improvement: using {actual_parent_commit} as base for {entry}")
    #         else:
    #             actual_parent_commit = parent_commit
    #     else:
    #         actual_parent_commit = parent_commit
    # else:
    #     actual_parent_commit = parent_commit

    if "+" in parent_commit and "+" in entry: #('initial+initial', 'sphinx-doc__sphinx-8548+sphinx-doc__sphinx-9281') 这种情况需要处理
        group_improve = True
        entry_list = entry.split("+")
        parent_commit_list = parent_commit.split("+")
        parent_commit0 = parent_commit_list[0]
        parent_commit1 = parent_commit_list[1]
        entry0 = entry_list[0]
        entry1 = entry_list[1]
        actual_parent_commit = parent_commit0  #确保Find all parent patches and apply them这个模块的代码以第一个parent_commit为准来进行自我提升
   
        patch_files = get_model_patch_paths(root_dir, os.path.join(output_dir, '../'), actual_parent_commit)
        patch_files1 = get_model_patch_paths(root_dir, os.path.join(output_dir, '../'), parent_commit1)
        print(f"这里是self_improve_step.py的self_improve函数570行，进入group_improve分支中的混合父代分支，混合父代机制是否开启:{group_improve},entry0: {entry0}, entry1: {entry1}, parent_commit0: {parent_commit0}, parent_commit1: {parent_commit1},获得patch_files:{patch_files}和patch_files1: {patch_files1}")
        if run_baseline not in ['no_selfimprove']:
            for patch_file in patch_files:
                ensure_patch_file_newline(patch_file)  # double insurance: valid format for patch command
                copy_to_container(container, patch_file, '/dgm/parent_patch.txt')
                exec_result = container.exec_run("/bin/sh -c 'patch -p1 < /dgm/parent_patch.txt'", workdir='/dgm')
                log_container_output(exec_result)
                exec_result = container.exec_run("rm /dgm/parent_patch.txt", workdir='/dgm')
                log_container_output(exec_result)
    
    else: #只要不是group_improve分支中的混合父代分支，都走这个分支,包括self_improve或者group_improve分支中的p1/p2分支，因为都是1v1进化，不用特殊处理
        patch_files = get_model_patch_paths(root_dir, os.path.join(output_dir, '../'), parent_commit)
        print(f"这里是self_improve_step.py的self_improve函数584行，进入self_improve或者group_improve分支中的p1/p2分支了,混合父代机制是否开启: {group_improve},获得patch_files: {patch_files},entry: {entry},parent_commit: {parent_commit}")
        if run_baseline not in ['no_selfimprove']:
            for patch_file in patch_files:
                ensure_patch_file_newline(patch_file)  # double insurance: valid format for patch command
                copy_to_container(container, patch_file, '/dgm/parent_patch.txt')
                exec_result = container.exec_run("/bin/sh -c 'patch -p1 < /dgm/parent_patch.txt'", workdir='/dgm')
                log_container_output(exec_result)
                exec_result = container.exec_run("rm /dgm/parent_patch.txt", workdir='/dgm')
                log_container_output(exec_result)

    # Commit this version of dgm, so that irrelevant changes are not included in the patch
    exec_result = container.exec_run("git add --all", workdir='/dgm/')
    log_container_output(exec_result)
    exec_result = container.exec_run("git -c user.name='user' -c user.email='you@example.com' commit -m 'a nonsense commit message'", workdir='/dgm/')
    log_container_output(exec_result)
    commit_output = exec_result.output.decode('utf-8')
    # Git commit output format: `[master (root-commit) <hash>] a nonsense commit message`
    commit_hash = commit_output.split()[1].strip("[]")  # Extract the hash part

    # Install requirements again in case of any changes
    exec_result = container.exec_run("python -m pip install -r /dgm/requirements.txt", workdir='/')
    log_container_output(exec_result)

    # Get tasks to improve
    if entry:
        print(f"这里是self_improve_step.py的self_improve函数609行，entry: {entry},parent_commit: {parent_commit},root_dir: {root_dir},out_dir_base: {out_dir_base},patch_files: {patch_files},混合父代机制是否开启: {group_improve}")
        safe_log(f"Task to improve: {entry}")
        # safe_log(f"parent_commit: {parent_commit}")
        # safe_log(f"root_dir: {root_dir}")
        # safe_log(f"out_dir_base: {out_dir_base}")
        # safe_log(f"patch_files: {patch_files}")
        # Handle group improvement entries
        if group_improve:
            print(f"Group improvement mode: {entry} with parent_commit: {parent_commit}")
            problem_statement = diagnose_problem(entry0, parent_commit0, root_dir, out_dir_base, patch_files=patch_files, polyglot=polyglot, group_improve=True, entry1=entry1, commit1=parent_commit1,patch_files1=patch_files1, claude_model=claude_model, diagnose_model=diagnose_model)
        else:
            problem_statement = diagnose_problem(entry, parent_commit, root_dir, out_dir_base, patch_files=patch_files, polyglot=polyglot, claude_model=claude_model, diagnose_model=diagnose_model)
        safe_log(f"problem_statement: {problem_statement}")
    else:
        safe_log("No entry provided. Exiting.")
        cleanup_container(container)
        save_metadata(metadata, output_dir)
        return metadata

    metadata['entry'] = entry
    metadata['problem_statement'] = problem_statement
    # If problem statement is not found, exit
    if not problem_statement:
        safe_log("Failed to diagnose the problem statement. Exiting.")
        cleanup_container(container)
        save_metadata(metadata, output_dir)
        return metadata

    # Run self-improvement
    safe_log("Running self-improvement")
    chat_history_file_container = "/dgm/self_evo.md"
    test_description = get_test_description(swerepo=False)
    # Use claude_model parameter if provided, otherwise use environment variable
    coding_agent_claude_model = claude_model if claude_model else os.getenv('CODING_AGENT_CLAUDE_MODEL')
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
        safe_log(f"Using Claude model for coding agent (self-modification): {coding_agent_claude_model}")
    else:
        safe_log("Using default model for coding agent (self-modification): Claude Opus 4.5")
    cmd = [
        "timeout", "2700",  # 45min timeout
        "python", "/dgm/coding_agent.py",
        "--problem_statement", problem_statement,
        "--git_dir", "/dgm/",
        "--chat_history_file", chat_history_file_container,
        "--base_commit", commit_hash,
        "--outdir", "/dgm/",
        "--test_description", test_description,
        "--self_improve",
    ]
    exec_result = container.exec_run(cmd, environment=env_vars, workdir='/')
    log_container_output(exec_result)

    # Copy output files back to host
    chat_history_file = os.path.join(output_dir, "self_evo.md")
    copy_from_container(container, chat_history_file_container, chat_history_file)
    model_patch_file = os.path.join(output_dir, "model_patch.diff")
    copy_from_container(container, "/dgm/model_patch.diff", model_patch_file)

    # Try reading the patch file to validate it
    try:
        # Check if patch file exists and is not empty
        if not os.path.exists(model_patch_file):
            raise Exception("Model patch file is empty or does not exist")
        with open(model_patch_file, 'r') as f:
            patch_content = f.read()
            if not patch_content.strip():
                raise Exception("Model patch file is empty")
    except Exception as e:
        safe_log(f"Failed to read model patch file: {str(e)}")
        save_metadata(metadata, output_dir)
        return metadata

    patch_files.append(model_patch_file)

    # Stop and remove the container
    cleanup_container(container)

    # Evaluate the performance of the self-improvement
    model_patch_exists = os.path.exists(model_patch_file)
    metadata['model_patch_exists'] = model_patch_exists
    model_patch_notempty = os.path.getsize(model_patch_file) > 0
    metadata['model_patch_notempty'] = model_patch_notempty
    model_name_or_path = run_id
    if model_patch_exists and model_patch_notempty:
        try:
            if not polyglot:
                run_harness_swe(entry, model_name_or_path, patch_files, num_evals, output_dir, metadata, run_id, test_more_threshold, test_task_list, test_task_list_more)
            else:
                run_harness_polyglot(entry, model_name_or_path, patch_files, num_evals, output_dir, metadata, run_id, test_more_threshold, test_task_list, test_task_list_more)
        except Exception as e:
            safe_log(f"Error while evaluating the self-improvement: {e}")

    # Build task success vector (same order as swe_bench/subsets/task.json): 1 if resolved, 0 otherwise
    if metadata.get('overall_performance'):
        task_list_path = os.path.join(root_dir, 'swe_bench', 'subsets', 'task.json')
        task_success_vector = build_task_success_vector(metadata['overall_performance'], task_list_path)
        if task_success_vector is not None:
            metadata['task_success_vector'] = task_success_vector

    # Post-self-improvement diagnosis
    if post_improve_diagnose:
        safe_log("Diagnosing the self-improvement")
        metadata['is_compiled'] = is_compiled_self_improve(metadata)
        if metadata['is_compiled']:
            safe_log("The self-improvement succeed to be complied")
            improvement_diagnosis = diagnose_improvement(
                entry, parent_commit, root_dir,
                model_patch_file, out_dir_base, run_id,
                patch_files=patch_files,
                diagnose_model=diagnose_model,
            )
            metadata['improvement_diagnosis'] = improvement_diagnosis
            safe_log(f"Improvement diagnosis: {improvement_diagnosis}")
        else:
            safe_log("The self-improvement fail to be complied")
            metadata['improvement_diagnosis'] = "Fail to complied. Ignore this."

    # Save metadata of this self-improvement attempt
    save_metadata(metadata, output_dir)
    return metadata

def main():
    parser = argparse.ArgumentParser(description="Self-improvement step for the repository.")
    parser.add_argument('--parent_commit', default="initial", type=str, help='Current commit to find the eval results, "initial" if starting from original dgm, else the run_id')
    parser.add_argument('--output_dir', default="./output_selfimprove", type=str, help='Directory to store the output')
    parser.add_argument('--force_rebuild', default=False, action='store_true', help='Force rebuild of the Docker image')
    parser.add_argument('--num_evals', default=1, type=int, help='Repeated number of swe evaluations after self-improvement')
    parser.add_argument('--no_post_improve_diagnose', default=False, action='store_true', help='Skip diagnosing the self-improvement after evaluation')
    parser.add_argument('--entry', default="django__django-10999", type=str, help='Task entry to improve')
    parser.add_argument('--test_task_list', default=None, type=str, help='List of tasks to evaluate the self-improvement')
    args = parser.parse_args()

    # Copy cached initial version into experiment dir
    os.system(f"cp -r initial/ {args.output_dir}")

    metadata = self_improve(
        parent_commit=args.parent_commit,
        output_dir=args.output_dir,
        force_rebuild=args.force_rebuild,
        num_evals=args.num_evals,
        post_improve_diagnose=not args.no_post_improve_diagnose,
        entry=args.entry,
        test_task_list=args.test_task_list,
    )

if __name__ == "__main__":
    main()
