#!/bin/bash

# 永久设置API密钥脚本
echo "=== DGM API密钥永久设置 ==="
echo ""

# 检查是否已经设置过
if grep -q "OPENAI_API_KEY" ~/.bashrc 2>/dev/null; then
    echo "⚠️  检测到 ~/.bashrc 中已有 OPENAI_API_KEY 设置"
    echo "   现有设置："
    grep "OPENAI_API_KEY" ~/.bashrc
    echo ""
    read -p "是否要覆盖现有设置？(y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "取消设置"
        exit 1
    fi
fi

if grep -q "ANTHROPIC_API_KEY" ~/.bashrc 2>/dev/null; then
    echo "⚠️  检测到 ~/.bashrc 中已有 ANTHROPIC_API_KEY 设置"
    echo "   现有设置："
    grep "ANTHROPIC_API_KEY" ~/.bashrc
    echo ""
    read -p "是否要覆盖现有设置？(y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "取消设置"
        exit 1
    fi
fi

echo "请按以下步骤设置API密钥："
echo ""
echo "1. 获取您的API密钥："
echo "   - OpenAI: https://platform.openai.com/api-keys"
echo "   - Anthropic: https://console.anthropic.com/keys"
echo ""
echo "2. 运行以下命令（替换为您的实际密钥）："
echo ""
echo "   # 设置OpenAI API密钥"
echo "   echo 'export OPENAI_API_KEY=\"sk-your-actual-openai-key-here\"' >> ~/.bashrc"
echo ""
echo "   # 设置Anthropic API密钥"
echo "   echo 'export ANTHROPIC_API_KEY=\"sk-ant-your-actual-anthropic-key-here\"' >> ~/.bashrc"
echo ""
echo "3. 重新加载配置："
echo "   source ~/.bashrc"
echo ""
echo "4. 验证设置："
echo "   cd /home/zweng7/self-evolving-agents/dgm"
echo "   source venv/bin/activate"
echo "   python test_api_keys.py"
echo ""
echo "5. 运行DGM："
echo "   ./run_dgm.sh"
echo ""
echo "注意："
echo "- 设置后，每次登录服务器都会自动加载这些环境变量"
echo "- 如果使用SSH连接，请确保使用 -t 参数或配置SSH转发"
echo "- 密钥格式："
echo "  * OpenAI: 以 'sk-' 开头"
echo "  * Anthropic: 以 'sk-ant-' 开头"

