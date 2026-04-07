import argparse
import datetime
import json
import math
import os
import random
import sys
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed, TimeoutError

from prompts.self_improvement_prompt import find_selfimprove_eval_logs
from self_improve_step import self_improve
from utils.common_utils import load_json_file
from utils.docker_utils import setup_logger
from utils.evo_utils import load_dgm_metadata, is_compiled_self_improve
from utils.docker_utils import safe_log

def initialize_run(output_dir, prevrun_dir=None, polyglot=False):
    # Initialize archive
    start_gen_num = 0
    if not prevrun_dir:
        archive = ['initial']
    else:
        # Load previous run's archive
        metadata_path = os.path.join(prevrun_dir, "dgm_metadata.jsonl")
        metadata = load_dgm_metadata(metadata_path, last_only=True)
        archive = metadata['archive']
        start_gen_num = metadata['generation'] + 1

    # Copy cached initial version into experiment dir
    initial_folder_name = 'initial' if not polyglot else 'initial_polyglot'
    if not prevrun_dir and not os.path.exists(f"{output_dir}/{initial_folder_name}"):
        if os.path.exists(initial_folder_name):
            os.system(f"cp -r {initial_folder_name}/ {output_dir}/initial")
        else:
            raise RuntimeError("Error: Need to properly configure evaluation results for the initial version.")
    
    return archive, start_gen_num

def any_exceeding_context_length(output_dir, commit_id, instance_ids):
    """
    Check if any of the issues have exceeded the context length.
    """
    for instance_id in instance_ids:
        md_logs, _, _, _ = find_selfimprove_eval_logs(instance_id, output_dir, commit_id, filter=False)
        # Skip if no logs found for this instance
        if not md_logs:
            continue
        md_log = md_logs[0]
        error_str = "Error in get_response_withtools: Error code: 400 - {'message': 'Input is too long for requested model.'}"
        # Repeated error_str means no attempt to fix it
        if f'{error_str}\n{error_str}' in md_log:
            return True
    return False


def select_parents_by_performance_novelty(candidates, output_dir, K, M=4, epsilon=1e-8, polyglot=False):
    """
    Select top-K parent agents by combined performance--novelty score.

    For each agent i with task-success vector z_i and performance alpha_i:
    - Cosine distance to j: d(i,j) = 1 - (z_i·z_j) / (||z_i|| ||z_j|| + epsilon)
    - Novelty: nov(i) = (1/M) * sum of d(i,j) over M nearest (most similar) neighbors j
    - Combined score: score(i) = alpha_i * sqrt(nov(i))
    Returns the top-K agents by score(i).
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    subset_dir = 'polyglot' if polyglot else 'swe_bench'
    task_list_path = os.path.join(script_dir, subset_dir, 'subsets', 'task.json')
    commits = list(candidates.keys())
    if not os.path.exists(task_list_path):
        return commits[-K:] if len(commits) >= K else commits

    task_list = load_json_file(task_list_path)
    D = len(task_list)

    # Build list of (commit, alpha, z) for agents that have task_success_vector
    agents = []
    for commit in candidates:
        meta_path = os.path.join(output_dir, commit, 'metadata.json')
        if not os.path.exists(meta_path):
            continue
        try:
            meta = load_json_file(meta_path)
        except Exception:
            continue
        z = meta.get('task_success_vector')
        if z is None or len(z) != D:
            continue
        alpha = candidates[commit]['accuracy_score']
        agents.append((commit, alpha, z))

    if len(agents) < K:
        commits = list(candidates.keys())
        return commits[-K:] if len(commits) >= K else commits

    n = len(agents)
    
    sys.stdout.flush()

    M_actual = min(M, n - 1)
    if M_actual <= 0:
        # Only one agent or M=0: return last K from candidates
        commits = [a[0] for a in agents]
        return commits[-K:] if len(commits) >= K else commits

    # For each i, compute novelty = mean of d(i,j) over M nearest neighbors j
    nov = [0.0] * n
    eps = epsilon
    for i in range(n):
        _, _, z_i = agents[i]
        norm_i = math.sqrt(sum(x * x for x in z_i))
        dists = []
        for j in range(n):
            if j == i:
                continue
            _, _, z_j = agents[j]
            dot = sum(a * b for a, b in zip(z_i, z_j))
            norm_j = math.sqrt(sum(x * x for x in z_j))
            # d(i,j) = 1 - (z_i·z_j) / (||z_i|| ||z_j|| + epsilon)
            denom = norm_i * norm_j + eps
            sim = dot / denom if denom > 0 else 0.0
            d_ij = 1.0 - sim
            dists.append((d_ij, j))
        dists.sort(key=lambda x: x[0])
        nov[i] = sum(dists[k][0] for k in range(M_actual)) / M_actual

    # score(i) = alpha_i * sqrt(nov(i)); rank by score descending
    scored = []
    for i in range(n):
        commit, alpha, _ = agents[i]
        sqrt_nov = math.sqrt(nov[i])
        score_i = alpha * sqrt_nov
        scored.append((score_i, commit, alpha, sqrt_nov))
    scored.sort(key=lambda x: x[0], reverse=True)

    
    sys.stdout.flush()

    return [commit for _, commit, _, _ in scored[:K]]


def choose_selfimproves(output_dir, archive, selfimprove_size, method='random', run_baseline=None, polyglot=False):
    """
    Choose self-improve attempts for the current generation.
    """
    selfimprove_entries = []

    # Get parent candidates
    candidates = {}
    for commit in archive:
        try:
            metadata_path = os.path.join(output_dir, commit, "metadata.json")
            metadata = load_json_file(metadata_path)
            candidates[commit] = {
                'accuracy_score': metadata['overall_performance']['accuracy_score'],
                'total_unresolved_ids': metadata['overall_performance']['total_unresolved_ids'],
                'total_emptypatch_ids': metadata['overall_performance']['total_emptypatch_ids'],
                'total_resolved_ids': metadata['overall_performance']['total_resolved_ids'],
                'children_count': 0,
            }
            # update children count, parent should already be in the archive
            if commit != 'initial':
                parent_commit = metadata['parent_commit']
                candidates[parent_commit]['children_count'] += 1
        except Exception as e:
            # probably because swe-eval failed, generated code did not compile, etc.
            print(f"{commit} not eligible for being a parent: {e}")
            continue

    # Choose parents based on method and baseline
    if run_baseline == 'no_darwin':
        # Always take the last commit
        commits = list(candidates.keys())
        parent_commits = commits[-1:]
    elif method == 'performance_novelty':
        # Rank by performance--novelty score; select top selfimprove_size
        parent_commits = select_parents_by_performance_novelty(candidates, output_dir, selfimprove_size, polyglot=polyglot)
        if len(parent_commits) < selfimprove_size:
            parent_commits.extend(random.choices(parent_commits, k=selfimprove_size - len(parent_commits)))
    elif method == 'score_prop':
        # Choose parents based on score
        commits = list(candidates.keys())
        scores = [candidates[commit]['accuracy_score'] for commit in commits]
        scores = [1 / (1 + math.exp(-10*(score-0.5))) for score in scores]
        probabilities = [score / sum(scores) for score in scores]
        parent_commits = random.choices(commits, probabilities, k=selfimprove_size)
    elif method == 'score_child_prop':
        # Choose parents based on score and the number of children
        commits = list(candidates.keys())
        scores = [candidates[commit]['accuracy_score'] for commit in commits]
        scores = [1 / (1 + math.exp(-10*(score-0.5))) for score in scores]
        children_counts = [candidates[commit]['children_count'] for commit in commits]
        children_counts = [1 / (1 + count) for count in children_counts]
        probabilities = [score * count for score, count in zip(scores, children_counts)]
        probabilities = [prob / sum(probabilities) for prob in probabilities]
        parent_commits = random.choices(commits, probabilities, k=selfimprove_size)
    elif method == 'best':
        # Choose parents with the best score
        sorted_commits = sorted(
            candidates,
            key=lambda x: candidates[x]['accuracy_score'],
            reverse=True,
        )
        parent_commits = sorted_commits[:min(selfimprove_size, len(sorted_commits))]
        if len(parent_commits) < selfimprove_size:
            parent_commits.extend(random.choices(parent_commits, k=selfimprove_size - len(parent_commits)))
    else:
        # Choose parents randomly
        parent_commits = random.choices(list(candidates.keys()), k=selfimprove_size)

    # Choose entries for each parent
    for parent_commit in parent_commits:
        empty_ids = candidates[parent_commit]['total_emptypatch_ids']
        resolved_ids = candidates[parent_commit]['total_resolved_ids']
        unresolved_ids = candidates[parent_commit]['total_unresolved_ids']
        
        if polyglot:
            entry_ids = empty_ids + unresolved_ids
            if not entry_ids:
                entry_ids = resolved_ids + empty_ids + unresolved_ids
        else:
            num_total_ids = len(empty_ids) + len(resolved_ids) + len(unresolved_ids)

            # Solve empty patches
            if len(empty_ids) >= 0.1 * num_total_ids and random.random() < 0.25:
                entry = 'solve_empty_patches'
                selfimprove_entries.append((parent_commit, entry))
                continue

            # Solve stochasticity
            if random.random() < 0.25:
                entry = 'solve_stochasticity'
                selfimprove_entries.append((parent_commit, entry))
                continue

            # Solve context length
            if any_exceeding_context_length(output_dir, parent_commit, empty_ids + unresolved_ids) and \
                random.random() < 0.25:
                entry = 'solve_contextlength'
                selfimprove_entries.append((parent_commit, entry))
                continue

            # Choose a random unresolved entry
            if len(unresolved_ids) == 0:
                weighted_entries = []
                if len(empty_ids) >= 0.1 * num_total_ids:
                    weighted_entries.append(('solve_empty_patches', 0.4))
                weighted_entries.append(('solve_stochasticity', 0.3))
                if any_exceeding_context_length(output_dir, parent_commit, empty_ids + unresolved_ids):
                    weighted_entries.append(('solve_contextlength', 0.3))

                if not weighted_entries:
                    continue

                total_weight = sum(weight for _, weight in weighted_entries)
                rand_val = random.random() * total_weight
                cumulative = 0.0
                entry = weighted_entries[-1][0]  # default to last entry
                for candidate, weight in weighted_entries:
                    cumulative += weight
                    if rand_val <= cumulative:
                        entry = candidate
                        break
                selfimprove_entries.append((parent_commit, entry))
                continue
            entry_ids = unresolved_ids
        entry = random.choice(entry_ids)
        selfimprove_entries.append((parent_commit, entry))

    return selfimprove_entries


def choose_group_improves(output_dir, archive, groupimprove_size, method='random', run_baseline=None, polyglot=False):
    """
    Choose self-improve attempts for the current generation.
    """
    selfimprove_entries = []

    # Get parent candidates
    candidates = {}
    for commit in archive:
        try:
            metadata_path = os.path.join(output_dir, commit, "metadata.json")
            metadata = load_json_file(metadata_path)
            candidates[commit] = {
                'accuracy_score': metadata['overall_performance']['accuracy_score'],
                'total_unresolved_ids': metadata['overall_performance']['total_unresolved_ids'],
                'total_emptypatch_ids': metadata['overall_performance']['total_emptypatch_ids'],
                'total_resolved_ids': metadata['overall_performance']['total_resolved_ids'],
                'children_count': 0,
            }
            # update children count, parent should already be in the archive
            if commit != 'initial':
                parent_commit = metadata['parent_commit']
                candidates[parent_commit]['children_count'] += 1
        except Exception as e:
            # probably because swe-eval failed, generated code did not compile, etc.
            continue

    # Choose parents based on method and baseline
    if run_baseline == 'no_darwin':
        # Always take the last commit
        commits = list(candidates.keys())
        parent_commits = commits[-1:]
    elif method == 'performance_novelty':
        # Rank by performance--novelty score; select top groupimprove_size
        parent_commits = select_parents_by_performance_novelty(candidates, output_dir, groupimprove_size, polyglot=polyglot)
        if len(parent_commits) < groupimprove_size:
            parent_commits.extend(random.choices(parent_commits, k=groupimprove_size - len(parent_commits)))
    elif method == 'score_prop':
        # Choose parents based on score
        commits = list(candidates.keys())
        scores = [candidates[commit]['accuracy_score'] for commit in commits]
        scores = [1 / (1 + math.exp(-10*(score-0.5))) for score in scores]
        probabilities = [score / sum(scores) for score in scores]
        parent_commits = random.choices(commits, probabilities, k=groupimprove_size)
    elif method == 'score_child_prop':
        # Choose parents based on score and the number of children
        commits = list(candidates.keys())
        scores = [candidates[commit]['accuracy_score'] for commit in commits]
        scores = [1 / (1 + math.exp(-10*(score-0.5))) for score in scores]
        children_counts = [candidates[commit]['children_count'] for commit in commits]
        children_counts = [1 / (1 + count) for count in children_counts]
        probabilities = [score * count for score, count in zip(scores, children_counts)]
        probabilities = [prob / sum(probabilities) for prob in probabilities]
        parent_commits = random.choices(commits, probabilities, k=groupimprove_size)
    elif method == 'best':
        # Choose parents with the best score
        sorted_commits = sorted(
            candidates,
            key=lambda x: candidates[x]['accuracy_score'],
            reverse=True,
        )
         
        parent_commits = sorted_commits[:min(groupimprove_size, len(sorted_commits))]
        if len(parent_commits) < groupimprove_size:
            parent_commits.extend(random.choices(parent_commits, k=groupimprove_size - len(parent_commits)))
    else:
        # Choose parents randomly
        parent_commits = random.choices(list(candidates.keys()), k=groupimprove_size)

    # Choose entries for each parent
    for parent_commit in parent_commits:
        empty_ids = candidates[parent_commit]['total_emptypatch_ids']
        resolved_ids = candidates[parent_commit]['total_resolved_ids']
        unresolved_ids = candidates[parent_commit]['total_unresolved_ids']
        
        if polyglot:
            entry_ids = empty_ids + unresolved_ids
            if not entry_ids:
                entry_ids = resolved_ids + empty_ids + unresolved_ids
        else:
            num_total_ids = len(empty_ids) + len(resolved_ids) + len(unresolved_ids)

            # Solve empty patches
            if len(empty_ids) >= 0.1 * num_total_ids and random.random() < 0.25:
                entry = 'solve_empty_patches'
                selfimprove_entries.append((parent_commit, entry))
                continue

            # Solve stochasticity
            if random.random() < 0.25:
                entry = 'solve_stochasticity'
                selfimprove_entries.append((parent_commit, entry))
                continue

            # Solve context length
            if any_exceeding_context_length(output_dir, parent_commit, empty_ids + unresolved_ids) and \
                random.random() < 0.25:
                entry = 'solve_contextlength'
                selfimprove_entries.append((parent_commit, entry))
                continue

            # Choose a random unresolved entry
            if len(unresolved_ids) == 0:
                weighted_entries = []
                if len(empty_ids) >= 0.1 * num_total_ids:
                    weighted_entries.append(('solve_empty_patches', 0.4))
                weighted_entries.append(('solve_stochasticity', 0.3))
                if any_exceeding_context_length(output_dir, parent_commit, empty_ids + unresolved_ids):
                    weighted_entries.append(('solve_contextlength', 0.3))

                if not weighted_entries:
                    continue

                total_weight = sum(weight for _, weight in weighted_entries)
                rand_val = random.random() * total_weight
                cumulative = 0.0
                entry = weighted_entries[-1][0]  # default to last entry
                for candidate, weight in weighted_entries:
                    cumulative += weight
                    if rand_val <= cumulative:
                        entry = candidate
                        break
                selfimprove_entries.append((parent_commit, entry))
                continue
            entry_ids = unresolved_ids
        entry = random.choice(entry_ids)
        selfimprove_entries.append((parent_commit, entry))
    
    if len(selfimprove_entries) >= 2:
        # combined_entry1: (p1+p2, e1+e2) -> 在 self_improve_step 里 codebase 为 P1（split 后第一个）
        combined_entry1 = (
            selfimprove_entries[0][0] + "+" + selfimprove_entries[1][0],
            selfimprove_entries[0][1] + "+" + selfimprove_entries[1][1],
        )
        # combined_entry2: (p2+p1, e2+e1) -> 在 self_improve_step 里 codebase 为 P2（split 后第一个）
        combined_entry2 = (
            selfimprove_entries[1][0] + "+" + selfimprove_entries[0][0],
            selfimprove_entries[1][1] + "+" + selfimprove_entries[0][1],
        )
        selfimprove_entries[0] = combined_entry1
        selfimprove_entries[-1] = combined_entry2
    # selfimprove_entries.append((selfimprove_entries[0][0]+"+"+selfimprove_entries[1][0], selfimprove_entries[0][1]+"+"+selfimprove_entries[1][1]))
    # selfimprove_entries1 = [(selfimprove_entries[0][0]+"+"+selfimprove_entries[1][0], selfimprove_entries[0][1]+"+"+selfimprove_entries[1][1])]
    safe_log(f"这里是DGM_outer.py的choose_group_improves函数256行，groupimprove_entries: {selfimprove_entries}")
    # safe_log(f"这里是DGM_outer.py的choose_group_improves函数257行，混合父代group_improve_entries1: {selfimprove_entries1}")
    
    
    # 再加上一个group-evolving项，以上和之前的逻辑一致选择了p1,p2作为parent，下面再加上(p1,p2)的group evolving项

    return selfimprove_entries



def _select_task_for_parent(parent_data, output_dir, parent_commit, polyglot=False):
    """
    Select a specific task for a parent agent based on their performance.
    This mimics the logic from choose_selfimproves for task selection.
    """
    empty_ids = parent_data.get('total_emptypatch_ids', [])
    resolved_ids = parent_data.get('total_resolved_ids', [])
    unresolved_ids = parent_data.get('total_unresolved_ids', [])
    
    if polyglot:
        entry_ids = empty_ids + unresolved_ids
        if not entry_ids:
            entry_ids = resolved_ids + empty_ids + unresolved_ids
    else:
        num_total_ids = len(empty_ids) + len(resolved_ids) + len(unresolved_ids)

        # Solve empty patches
        if len(empty_ids) >= 0.1 * num_total_ids and random.random() < 0.25:
            return 'solve_empty_patches'

        # Solve stochasticity
        if random.random() < 0.25:
            return 'solve_stochasticity'

        # Solve context length
        if any_exceeding_context_length(output_dir, parent_commit, empty_ids + unresolved_ids) and \
            random.random() < 0.25:
            return 'solve_contextlength'

        # Choose a random unresolved entry
        if not unresolved_ids:
            entry_ids = resolved_ids + empty_ids + unresolved_ids
        else:
            entry_ids = unresolved_ids
    
    return random.choice(entry_ids) if entry_ids else 'solve_empty_patches'

def filter_compiled(run_ids, output_dir, num_swe_issues=[], logger=None):
    """
    Filter out runs that did not compile or have all empty patches.
    """
    run_ids_compiled = []

    logger.info(f"num_swe_issues: {num_swe_issues}")
    for run_id in run_ids:
        metadata_path = os.path.join(output_dir, run_id, "metadata.json")
        metadata = load_json_file(metadata_path)
        logger.info(f"{run_id} metadata: {metadata}")
        if is_compiled_self_improve(metadata, num_swe_issues=num_swe_issues, logger=logger):
            run_ids_compiled.append(run_id)
    return run_ids_compiled

def get_original_score(output_dir):
    """
    Get the original score from the initial version.
    """
    metadata = load_json_file(os.path.join(output_dir, "initial", "metadata.json"))
    return metadata["overall_performance"]["accuracy_score"]

def update_archive(output_dir, archive, new_ids, method='keep_all', noise_leeway=0.1):
    """
    Update the archive with the new self-improve runs.
    """
    if method == 'keep_better':
        # keep only better ones
        original_score = get_original_score(output_dir) - noise_leeway
        for run_id in new_ids:
            metadata = load_json_file(os.path.join(output_dir, run_id, "metadata.json"))
            score = metadata["overall_performance"]["accuracy_score"]
            if score >= original_score:
                archive.append(run_id)
    else:
        # keep  everything
        archive += new_ids

    return archive

def get_full_eval_threshold(output_dir, archive):
    """
    Get the threshold for full evaluation.
    """
    archive_scores = []
    num_full_eval = sum(len(load_json_file(f"./swe_bench/subsets/{size}.json"))
                       for size in ['small', 'medium', 'big'])

    # Get original score
    original_score = get_original_score(output_dir)
    archive_scores.append(original_score)

    # Get scores from the archive
    for run_id in archive:
        metadata = load_json_file(os.path.join(output_dir, run_id, "metadata.json"))
        total_submitted_instances = metadata["overall_performance"]["total_submitted_instances"]
        # Skip if node did not have full evaluation
        if total_submitted_instances < num_full_eval * 0.9:
            continue
        score = metadata["overall_performance"]["accuracy_score"]
        archive_scores.append(score)

    # Get threshold, second highest score
    threshold = sorted(archive_scores, reverse=True)[1] if len(archive_scores) > 1 else archive_scores[0]
    # Ensure threshold is at least 0.4
    threshold = max(threshold, 0.4)

    return threshold

def main():
    # When stdout is redirected (e.g. nohup ... > log), use line buffering so print() appears immediately in the log
    if not sys.stdout.isatty() and hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(line_buffering=True)
    if not sys.stderr.isatty() and hasattr(sys.stderr, 'reconfigure'):
        sys.stderr.reconfigure(line_buffering=True)

    parser = argparse.ArgumentParser(description="Darwin Godel Machine!")
    parser.add_argument("--max_generation", type=int, default=80, help="Maximum number of evolution iterations.")
    parser.add_argument("--selfimprove_size", type=int, default=2, help="Number of self-improvements attempts per DGM generation.")
    parser.add_argument("--selfimprove_workers", type=int, default=2, help="Number of parallel workers for self-improvement attempts.")
    parser.add_argument("--groupimprove_size", type=int, default=None, help="Number of parent agents for group improvement (By default to be 2)")
    parser.add_argument(
        "--choose_selfimproves_method", type=str, default='score_child_prop',
        choices=['random', 'score_prop', 'score_child_prop', 'best', 'performance_novelty'],
        help="Method to choose self-improve attempts.",
    )
    parser.add_argument("--continue_from", type=str, default=None, help="Directory to continue the run from.")
    parser.add_argument("--update_archive", type=str, default='keep_all', choices=['keep_better', 'keep_all'], help="Method to update the archive.")
    # self-improve arguments
    parser.add_argument("--num_swe_evals", type=int, default=1, help="Number of repeated SWE evaluations to run for each self-improve attempt.")
    parser.add_argument('--post_improve_diagnose', default=False, action='store_true', help='Diagnose the self-improvement after evaluation')
    parser.add_argument("--shallow_eval", default=False, action='store_true', help="Run single shallow evaluation for self-improvement on swe.")
    parser.add_argument("--polyglot", default=False, action='store_true', help="Run evolution and evaluation on polyglot benchmark; task-success vector uses polyglot/subsets/task.json.")
    parser.add_argument("--eval_noise", type=float, default=0.1, help="Noise leeway for evaluation.")
    parser.add_argument("--no_full_eval", default=False, action='store_true', help="Do not run full evaluation on swe if a node is the top N highest performing.")
    # baselines
    parser.add_argument("--run_baseline", type=str, default=None, choices=['no_selfimprove', 'no_darwin'], help="Baseline to run.")
    parser.add_argument(
        "--coding_agent",
        type=str,
        default=None,
        choices=['claude_haiku_4.5', 'claude_sonnet_4.5', 'claude_sonnet_3.5'],
        help="Coding agent model (same for self-improvement and evaluation). Use 'claude_haiku_4.5', 'claude_sonnet_4.5', or 'claude_sonnet_3.5'. Default is Opus 4.5."
    )
    parser.add_argument(
        "--diagnose_model",
        type=str,
        default=None,
        choices=['claude_haiku_4.5', 'claude_sonnet_4.5', 'claude_sonnet_3.5'],
        help="Model to use for diagnose (problem diagnosis and improvement diagnosis). Default is 'o1-2024-12-17' (OpenAI). Use 'claude_haiku_4.5', 'claude_sonnet_4.5', or 'claude_sonnet_3.5' to use Claude models instead."
    )
    args = parser.parse_args()
    
    # Set coding agent model based on argument (used for both self-improvement and evaluation)
    if args.coding_agent:
        os.environ['CODING_AGENT_CLAUDE_MODEL'] = args.coding_agent
        print(f"Using coding agent: {args.coding_agent}")
    else:
        print("Using default coding agent: Opus 4.5")

    # Validate groupimprove_size parameter
    if args.groupimprove_size is not None:
        if args.groupimprove_size != 2:
            raise ValueError("groupimprove_size must be 2 when specified")
    else:
        print(f"Standard self-improvement mode: will generate {args.selfimprove_size} children per generation")

    # Variables for this DGM run
    if not args.continue_from:
        run_id = datetime.datetime.now().strftime("%Y%m%d%H%M%S_%f")
    else:
        run_id = os.path.basename(args.continue_from)
        
    output_dir = os.path.join("./output_dgm", run_id)
    os.makedirs(output_dir, exist_ok=True)

    # Initialize
    archive, start_gen_num = initialize_run(output_dir, prevrun_dir=args.continue_from, polyglot=args.polyglot)

    # SWE issues to consider
    if not args.polyglot:
        swe_issues_sm = load_json_file("./swe_bench/subsets/small.json")
        swe_issues_med = load_json_file("./swe_bench/subsets/medium.json")
    else:
        swe_issues_sm = load_json_file("./polyglot/subsets/small.json")
        swe_issues_med = load_json_file("./polyglot/subsets/medium.json")

    # Set up logger
    logger = setup_logger(os.path.join(output_dir, "dgm_outer.log"))
    logger.info(f"Starting DGM run {run_id} with arguments: {vars(args)}")
    logger.info(f"Archive: {archive}")
    test_more_threshold = 0.1  # 设置为 0.1，只有在 small test 上解决 >= 10% 任务时才在 medium subset（60个任务）上评估
    # Run the DGM
    for gen_num in range(start_gen_num, args.max_generation):
        # Choose improvement attempts based on mode
        if args.groupimprove_size is not None and gen_num > 0:
            # Group improvement mode (skip generation 0, use standard mode for initial generation)
            selfimprove_entries = choose_group_improves(
                output_dir, archive, args.groupimprove_size,
                method=args.choose_selfimproves_method,
                run_baseline=args.run_baseline,
                polyglot=args.polyglot,
            )
            logger.info(f"DGM_outer.py的main函数526行，Group-improve entries for generation {gen_num}: {selfimprove_entries}")
        else:
            # Standard self-improvement mode (generation 0 or when groupimprove_size is None)
            selfimprove_entries = choose_selfimproves(
                output_dir, archive, args.selfimprove_size,
                method=args.choose_selfimproves_method,
                run_baseline=args.run_baseline,
                polyglot=args.polyglot,
            )
            logger.info(f"Self-improve entries for generation {gen_num}: {selfimprove_entries}")

        # Run self-improvement processes
        selfimprove_ids = []
        with ThreadPoolExecutor(max_workers=args.selfimprove_workers) as executor:
            futures = [
                executor.submit(
                    self_improve,
                    parent_commit=parent_commit,
                    output_dir=output_dir,
                    force_rebuild=False,
                    num_evals=args.num_swe_evals,
                    post_improve_diagnose=args.post_improve_diagnose,
                    entry=entry,
                    test_task_list=swe_issues_sm,
                    test_more_threshold=None if args.shallow_eval else test_more_threshold,
                    test_task_list_more=None if args.shallow_eval else swe_issues_med,
                    polyglot=args.polyglot,
                    full_eval_threshold=None if args.no_full_eval else get_full_eval_threshold(output_dir, archive),
                    run_baseline=args.run_baseline,
                    coding_agent=args.coding_agent,
                    diagnose_model=args.diagnose_model,
                )
                for parent_commit, entry in selfimprove_entries
            ]

            for future in as_completed(futures):
                try:
                    # Added timeout to avoid hanging indefinitely (1.5 h here)
                    metadata = future.result(timeout=1.5*60*60)
                    selfimprove_ids.append(metadata['run_id'])
                except TimeoutError:
                    logger.error("Self-improvement attempt timed out.")
                    future.cancel()  # Optionally cancel the future if it's still running
                except Exception as e:
                    import traceback
                    logger.error(f"Self-improvement step failed: {e}")
                    logger.error(f"Traceback:\n{traceback.format_exc()}")

        # Update archive
        logger.info(f"Updating archive for generation {gen_num}")
        selfimprove_ids_compiled = filter_compiled(
            selfimprove_ids,
            output_dir,
            num_swe_issues=[len(swe_issues_sm)] if args.shallow_eval else [len(swe_issues_sm), len(swe_issues_med)], logger=logger
        )
        archive = update_archive(output_dir, archive, selfimprove_ids_compiled, method=args.update_archive, noise_leeway=args.eval_noise)

        # Save DGM state
        with open(os.path.join(output_dir, "dgm_metadata.jsonl"), "a") as f:
            f.write(json.dumps({
                "generation": gen_num,
                "selfimprove_entries": selfimprove_entries,
                "children": selfimprove_ids,
                "children_compiled": selfimprove_ids_compiled,
                "archive": archive,
            }, indent=2) + "\n")

if __name__ == "__main__":
    main()

