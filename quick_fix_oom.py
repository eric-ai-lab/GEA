#!/usr/bin/env python3
"""
快速修复 OOM 问题的脚本
提供几个立即可用的修复方案
"""

import os
import sys

def apply_quick_fix_1():
    """修复方案 1: 在 harness.py 中添加内存限制"""
    print("=" * 80)
    print("修复方案 1: 在容器启动后添加内存限制")
    print("=" * 80)
    
    harness_file = "swe_bench/harness.py"
    if not os.path.exists(harness_file):
        print(f"错误: 找不到文件 {harness_file}")
        return False
    
    with open(harness_file, 'r') as f:
        content = f.read()
    
    # 检查是否已经添加了内存限制
    if "mem_limit" in content or "update(mem_limit" in content:
        print("⚠ 文件可能已经包含内存限制配置")
        return False
    
    # 查找 container.start() 的位置
    old_code = "        container = build_container(test_spec, client, run_id, logger, nocache, force_rebuild=False)\n        container.start()"
    new_code = """        container = build_container(test_spec, client, run_id, logger, nocache, force_rebuild=False)
        # Set memory limit to prevent OOM (4GB)
        try:
            container.update(mem_limit='4g', memswap_limit='4g')
        except Exception as e:
            logger.warning(f"Failed to set memory limit: {e}")
        container.start()"""
    
    if old_code in content:
        content = content.replace(old_code, new_code)
        with open(harness_file, 'w') as f:
            f.write(content)
        print(f"✓ 已修改 {harness_file}")
        print("  添加了 4GB 内存限制")
        return True
    else:
        print("⚠ 未找到预期的代码模式，请手动修改")
        return False

def apply_quick_fix_2():
    """修复方案 2: 减少 evaluate_agent.py 中的并发数"""
    print("\n" + "=" * 80)
    print("修复方案 2: 减少评估并发数")
    print("=" * 80)
    
    eval_file = "analysis/evaluate_agent.py"
    if not os.path.exists(eval_file):
        print(f"错误: 找不到文件 {eval_file}")
        return False
    
    with open(eval_file, 'r') as f:
        content = f.read()
    
    # 检查当前设置
    if "max_workers=min(1," in content:
        print("⚠ 并发数已经是 1，无需修改")
        return False
    
    # 替换 max_workers
    old_code = "max_workers=min(2, len(test_task_list))"
    new_code = "max_workers=min(1, len(test_task_list))  # Reduced to prevent OOM"
    
    if old_code in content:
        content = content.replace(old_code, new_code)
        with open(eval_file, 'w') as f:
            f.write(content)
        print(f"✓ 已修改 {eval_file}")
        print("  将并发数从 2 改为 1")
        return True
    else:
        print("⚠ 未找到预期的代码，当前设置可能是:")
        import re
        matches = re.findall(r"max_workers=min\(\d+", content)
        if matches:
            print(f"  {matches[0]}")
        return False

def apply_quick_fix_3():
    """修复方案 3: 减少 self_improve_step.py 中的并发数"""
    print("\n" + "=" * 80)
    print("修复方案 3: 减少 self-improvement 并发数")
    print("=" * 80)
    
    step_file = "self_improve_step.py"
    if not os.path.exists(step_file):
        print(f"错误: 找不到文件 {step_file}")
        return False
    
    with open(step_file, 'r') as f:
        content = f.read()
    
    # 替换两处 max_workers
    changes = 0
    
    # 第一处：run_harness_swe
    old_code1 = "max_workers=min(5, len(test_task_list))"
    new_code1 = "max_workers=min(2, len(test_task_list))  # Reduced to prevent OOM"
    
    if old_code1 in content:
        content = content.replace(old_code1, new_code1)
        changes += 1
        print(f"  ✓ 第一处: 将 small subset 并发数从 5 改为 2")
    
    # 第二处：run_harness_swe (medium subset)
    old_code2 = "max_workers=min(5, len(test_task_list_more))"
    new_code2 = "max_workers=min(2, len(test_task_list_more))  # Reduced to prevent OOM"
    
    if old_code2 in content:
        content = content.replace(old_code2, new_code2)
        changes += 1
        print(f"  ✓ 第二处: 将 medium subset 并发数从 5 改为 2")
    
    if changes > 0:
        with open(step_file, 'w') as f:
            f.write(content)
        print(f"✓ 已修改 {step_file}，共 {changes} 处")
        return True
    else:
        print("⚠ 未找到需要修改的代码")
        return False

def main():
    print("\n" + "=" * 80)
    print("OOM 问题快速修复工具")
    print("=" * 80)
    print("\n此工具将应用以下修复:")
    print("1. 在容器启动时添加 4GB 内存限制")
    print("2. 将评估并发数从 2 改为 1")
    print("3. 将 self-improvement 并发数从 5 改为 2")
    print("\n注意: 这些修改会降低性能，但可以减少 OOM 问题")
    
    response = input("\n是否继续? (y/n): ")
    if response.lower() != 'y':
        print("已取消")
        return
    
    results = []
    results.append(("方案 1: 添加内存限制", apply_quick_fix_1()))
    results.append(("方案 2: 减少评估并发数", apply_quick_fix_2()))
    results.append(("方案 3: 减少 self-improvement 并发数", apply_quick_fix_3()))
    
    print("\n" + "=" * 80)
    print("修复结果总结")
    print("=" * 80)
    for name, success in results:
        status = "✓ 成功" if success else "✗ 跳过/失败"
        print(f"{name}: {status}")
    
    print("\n" + "=" * 80)
    print("后续步骤")
    print("=" * 80)
    print("1. 测试修改后的代码")
    print("2. 监控内存使用: docker stats")
    print("3. 如果仍有问题，可以:")
    print("   - 进一步减少并发数")
    print("   - 增加内存限制（如果系统有足够内存）")
    print("   - 查看详细解决方案: SOLVE_OOM_PROBLEMS.md")

if __name__ == "__main__":
    main()


















