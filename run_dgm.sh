#!/bin/bash

# DGM运行脚本
# 请在使用前设置您的API密钥

echo "=== DGM (Darwin Gödel Machine) 运行脚本 ==="
echo ""

# 检查API密钥是否设置
if [ -z "$OPENAI_API_KEY" ]; then
    echo "❌ 错误: 请设置 OPENAI_API_KEY 环境变量"
    echo "   例如: export OPENAI_API_KEY='your-openai-key-here'"
    exit 1
fi

if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "❌ 错误: 请设置 ANTHROPIC_API_KEY 环境变量"
    echo "   例如: export ANTHROPIC_API_KEY='your-anthropic-key-here'"
    exit 1
fi

echo "✅ API密钥已设置"
echo ""

# 激活虚拟环境
source venv/bin/activate

echo "🚀 开始运行DGM..."
echo "参数:"
echo "  - 最大代数: 2"
echo "  - 自我改进数量: 3"
echo "  - 并行工作进程: 3"
echo "  - SWE评估次数: 1"
echo "  - 浅层评估: 启用"
echo "  - 选择方法: score_child_prop"
echo ""

# 运行DGM
python DGM_outer.py \
    --max_generation 2 \
    --selfimprove_size 3 \
    --selfimprove_workers 3 \
    --num_swe_evals 1 \
    --shallow_eval \
    --choose_selfimproves_method score_child_prop

echo ""
echo "🎉 DGM运行完成！"
echo "结果将保存在 output_dgm/ 目录中"

