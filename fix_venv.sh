#!/bin/bash
# 修复虚拟环境激活问题的脚本

cd "$(dirname "$0")"

echo "=== 当前状态 ==="
echo "Python3 路径: $(which python3 2>/dev/null || echo '未找到')"
echo "VIRTUAL_ENV: ${VIRTUAL_ENV:-未设置}"
echo "CONDA_DEFAULT_ENV: ${CONDA_DEFAULT_ENV:-未设置}"
echo ""

# 检查并修复 activate 脚本中的硬编码路径问题
ACTIVATE_SCRIPT="venv/bin/activate"
if [ -f "$ACTIVATE_SCRIPT" ]; then
    # 检查是否有硬编码的错误路径
    if grep -q "/home/zweng7/self-evolving-agents/dgm/venv" "$ACTIVATE_SCRIPT" 2>/dev/null; then
        echo "⚠️  检测到 activate 脚本中有硬编码路径，已自动修复..."
        # 修复路径检测逻辑
        sed -i 's|export VIRTUAL_ENV=$(cygpath /home/zweng7/self-evolving-agents/dgm/venv)|_VENV_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"\n    _VENV_DIR="$(dirname "$_VENV_DIR")"\n    export VIRTUAL_ENV=$(cygpath "$_VENV_DIR")|' "$ACTIVATE_SCRIPT" 2>/dev/null || true
        sed -i 's|export VIRTUAL_ENV=/home/zweng7/self-evolving-agents/dgm/venv|_VENV_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"\n_VENV_DIR="$(dirname "$_VENV_DIR")"\nexport VIRTUAL_ENV="$_VENV_DIR"|' "$ACTIVATE_SCRIPT" 2>/dev/null || true
        # 修复 PATH 设置
        sed -i 's|PATH="$VIRTUAL_ENV/"bin":$PATH"|PATH="$VIRTUAL_ENV/bin:$PATH"|' "$ACTIVATE_SCRIPT" 2>/dev/null || true
        echo "✅ activate 脚本已修复"
    fi
fi

# 检查是否有 conda 环境
if [ -n "$CONDA_DEFAULT_ENV" ] || command -v conda &> /dev/null; then
    echo "检测到 conda 环境，先退出..."
    conda deactivate 2>/dev/null || true
fi

# 退出任何已激活的虚拟环境
if [ -n "$VIRTUAL_ENV" ]; then
    echo "退出之前的虚拟环境..."
    deactivate 2>/dev/null || true
    unset VIRTUAL_ENV
fi

# 重新激活虚拟环境
echo "正在激活虚拟环境..."
source venv/bin/activate

echo ""
echo "=== 激活后状态 ==="
PYTHON_PATH=$(which python3 2>/dev/null || echo "未找到")
echo "Python3 路径: $PYTHON_PATH"
echo "VIRTUAL_ENV: ${VIRTUAL_ENV:-未设置}"
if command -v python3 &> /dev/null; then
    echo "Python 版本: $(python3 --version)"
fi

# 验证是否成功
VENV_EXPECTED="/home/zweng7/bedrock-opensource-group-evolving-agents/dgm/venv"
if [[ "$VIRTUAL_ENV" == "$VENV_EXPECTED" ]] && [[ "$PYTHON_PATH" == "$VENV_EXPECTED/bin/python3" ]]; then
    echo ""
    echo "✅ 虚拟环境已成功激活！"
    echo ""
    echo "现在可以使用:"
    echo "  - python3 (指向虚拟环境的 Python)"
    echo "  - pip3 (指向虚拟环境的 pip)"
else
    echo ""
    echo "⚠️  虚拟环境可能未完全激活，请检查:"
    echo "  1. VIRTUAL_ENV 应该指向: $VENV_EXPECTED"
    echo "  2. which python3 应该显示: $VENV_EXPECTED/bin/python3"
fi

