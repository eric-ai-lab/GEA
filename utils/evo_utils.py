import json
import os

from utils.common_utils import load_json_file, read_file


def load_dgm_metadata(dgm_metadata_path, last_only=False):
    # Load all archives from given metadata file
    if not os.path.exists(dgm_metadata_path):
        raise FileNotFoundError(f"Metadata file not found at {dgm_metadata_path}")
    # Read all JSON entries from the metadata file
    content = read_file(dgm_metadata_path)
    json_entries = content.split('\n{')
    # Parse all JSON entries
    dgm_metadata = []
    for json_entry in json_entries:
        # Add back the { if it was removed by split
        if not json_entry.startswith('{'):
            json_entry = '{' + json_entry
        # Parse the JSON entry
        metadata = json.loads(json_entry)
        dgm_metadata.append(metadata)

    if last_only:
        return dgm_metadata[-1]
    return dgm_metadata

def get_model_patch_paths(root_dir, dgm_dir, parent_commit):
    prev_commit = parent_commit
    patch_files = []
    print(f"这里是  evo_utils.py 的get_model_patch_paths函数第31行，root_dir: {root_dir}\n")
    print(f"这里是  evo_utils.py 的get_model_patch_paths函数第32行，dgm_dir: {dgm_dir}\n")
    while prev_commit != 'initial':
        print(f"这里是  evo_utils.py 的get_model_patch_paths函数第34行，prev_commit: {prev_commit}\n")
        parent_dir = os.path.join(root_dir, dgm_dir, prev_commit)
        parent_patch_file = os.path.join(parent_dir, "model_patch.diff")
        if os.path.exists(parent_patch_file):
            patch_files.append(parent_patch_file)
        else:
            print(f"Parent patch file not found: {parent_patch_file}")
        # find next parent commit in the metadata
        parent_metadata = load_json_file(os.path.join(parent_dir, "metadata.json"))
        print(f"这里是  evo_utils.py 的get_model_patch_paths函数第40行，parent_metadata: {parent_metadata}\n")
        prev_commit = parent_metadata.get('parent_commit', 'initial')
        print(f"这里是  evo_utils.py 的get_model_patch_paths函数第41行，prev_commit: {prev_commit}\n")
        if "+" in prev_commit:
            print(f"这里是  evo_utils.py 的get_model_patch_paths函数第42行，有+号的，prev_commit: {prev_commit}\n")
            prev_commit = prev_commit.split("+")[0]
    return patch_files[::-1]  # reverse the list to get the correct order

def get_all_performance(run_keyword, results_dir='./swe_bench'):
    """
    Retrieve performance results for all runs based on the provided keyword.

    Args:
        run_keyword (str): A keyword used to identify the target runs' evaluation results.

    Returns:
        list: A list of dictionaries, each containing performance results for a matching run.
    """
    # Find all JSON files in eval_results_dir matching the keyword
    matching_files = [
        f for f in os.listdir(results_dir)
        if f.endswith('.json') and run_keyword in f
    ]
    
    # Return an empty list if no matches are found
    if not matching_files:
        print(f"No evaluation files found matching the keyword '{run_keyword}'.")
        return None, None
    
    # Process each matching file
    performance_results = []
    total_resolved_instances = 0
    total_submitted_instances = 0
    total_unresolved_ids = []
    total_resolved_ids = []
    total_emptypatch_ids = []
    for file_name in matching_files:
        eval_agent_path = os.path.join(results_dir, file_name)
        eval_results = load_json_file(eval_agent_path)
        resolved_instances = eval_results.get('resolved_instances', 0)
        submitted_instances = eval_results.get('submitted_instances', 0)
        total_resolved_instances += resolved_instances
        total_submitted_instances += submitted_instances
        accuracy_score = resolved_instances / submitted_instances if submitted_instances > 0 else 0
        performance_results.append({'file': file_name, 'accuracy_score': accuracy_score, **eval_results})
        total_unresolved_ids.extend(eval_results.get('unresolved_ids', []))
        total_emptypatch_ids.extend(eval_results.get('empty_patch_ids', []))
        total_resolved_ids.extend(eval_results.get('resolved_ids', []))

    # Calculate the overall accuracy score
    overall_performance = {}
    overall_performance['accuracy_score'] = total_resolved_instances / total_submitted_instances if total_submitted_instances > 0 else 0
    overall_performance['total_resolved_instances'] = total_resolved_instances
    overall_performance['total_submitted_instances'] = total_submitted_instances
    overall_performance['files'] = matching_files
    overall_performance['total_unresolved_ids'] = total_unresolved_ids
    overall_performance['total_emptypatch_ids'] = total_emptypatch_ids
    overall_performance['total_resolved_ids'] = total_resolved_ids
    
    return performance_results, overall_performance


def build_task_success_vector(overall_performance, task_list_path):
    """
    Build a binary success vector for an agent: one entry per task in task_list_path.
    For each task, 1 if the agent resolved it (task_id in total_resolved_ids), else 0.

    Args:
        overall_performance: dict with key 'total_resolved_ids' (list of resolved instance_ids).
        task_list_path: path to JSON file containing list of task instance_ids (e.g. swe_bench/subsets/task.json).

    Returns:
        list of int (0 or 1) of length len(task_list), or None if overall_performance is None
        or task_list_path does not exist.
    """
    if not overall_performance or not os.path.exists(task_list_path):
        return None
    task_list = load_json_file(task_list_path)
    resolved_set = set(overall_performance.get('total_resolved_ids', []))
    return [1 if tid in resolved_set else 0 for tid in task_list]


def is_compiled_self_improve(metadata, num_swe_issues=[], logger=None):
    """
    Checks if the run was properly compiled and 'self-improved' by verifying:
      1. The 'overall_performance' dict has the required keys:
         ('accuracy_score', 'total_unresolved_ids', 'total_resolved_ids', 'total_emptypatch_ids').
      2. There is at least one non-empty patch (resolved + unresolved > 0).
      3. If num_swe_issues is provided, the total number of evaluated issues matches num_swe_issues.

    Returns True if all conditions are met, else False.
    """
    overall_perf = metadata.get('overall_performance', {})
    required_keys = ['accuracy_score', 'total_unresolved_ids', 'total_resolved_ids', 'total_emptypatch_ids']

    # 1. Must have the required keys
    if not overall_perf or not all(k in overall_perf for k in required_keys):
        logger.info(f"no required keys")
        return False

    # 2. Must have at least one non-empty patch
    num_resolved = len(overall_perf['total_resolved_ids'])
    num_unresolved = len(overall_perf['total_unresolved_ids'])
    if (num_resolved + num_unresolved) == 0:
        logger.info(f"no non-empty patch")
        return False

    # 3. If specified, total evaluated must match num_swe_issues, else it means that some didn't compile
    total_evaluated = overall_perf['total_submitted_instances']
    if total_evaluated < num_swe_issues[0]:
        logger.info(f"not match num_issues")
        return False

    return True
