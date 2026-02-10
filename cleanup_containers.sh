#!/bin/bash
# 清理 Docker 容器和资源的脚本

cd "$(dirname "$0")"

echo "=== 开始清理容器和资源 ==="
echo ""

# 1. 清理所有相关的容器
echo "1. 清理 Docker 容器..."
CONTAINERS=$(docker ps -a --format "{{.Names}}" | grep -E "dgm-container|sweb\.|testbed" || true)
if [ -z "$CONTAINERS" ]; then
    echo "   没有找到相关容器"
else
    echo "   找到以下容器："
    echo "$CONTAINERS" | sed 's/^/     - /'
    echo ""
    echo "$CONTAINERS" | while read -r container; do
        echo "   正在停止并删除容器: $container"
        docker stop "$container" 2>/dev/null || true
        docker rm "$container" 2>/dev/null || true
    done
    echo "   ✅ 容器清理完成"
fi
echo ""

# 2. 清理所有停止的容器（可选）
echo "2. 清理所有停止的容器..."
STOPPED=$(docker ps -a --filter "status=exited" --format "{{.Names}}" | grep -E "dgm|sweb|testbed" || true)
if [ -z "$STOPPED" ]; then
    echo "   没有找到停止的相关容器"
else
    echo "   找到以下停止的容器："
    echo "$STOPPED" | sed 's/^/     - /'
    echo "$STOPPED" | xargs -r docker rm 2>/dev/null || true
    echo "   ✅ 停止的容器清理完成"
fi
echo ""

# 3. 清理悬空镜像（可选）
echo "3. 清理悬空镜像..."
DANGLING=$(docker images -f "dangling=true" -q)
if [ -z "$DANGLING" ]; then
    echo "   没有悬空镜像"
else
    echo "   找到 $(echo "$DANGLING" | wc -l) 个悬空镜像"
    docker rmi $DANGLING 2>/dev/null || true
    echo "   ✅ 悬空镜像清理完成"
fi
echo ""

# 4. 清理 SWE-bench 相关镜像（可选，需要确认）
if [ "$1" == "--all" ] || [ "$1" == "-a" ]; then
    echo "4. 清理 SWE-bench 相关镜像..."
    IMAGES=$(docker images --format "{{.Repository}}:{{.Tag}}" | grep -E "sweb\." || true)
    if [ -z "$IMAGES" ]; then
        echo "   没有找到 SWE-bench 相关镜像"
    else
        echo "   找到以下镜像："
        echo "$IMAGES" | sed 's/^/     - /'
        read -p "   确认删除这些镜像吗？(y/N): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            echo "$IMAGES" | while read -r image; do
                docker rmi "$image" 2>/dev/null || true
            done
            echo "   ✅ 镜像清理完成"
        else
            echo "   跳过镜像清理"
        fi
    fi
    echo ""
fi

# 5. 清理输出目录（可选）
if [ "$1" == "--all" ] || [ "$1" == "-a" ]; then
    echo "5. 清理输出目录..."
    if [ -d "output_dgm" ]; then
        echo "   找到 output_dgm 目录"
        read -p "   确认删除 output_dgm 目录吗？(y/N): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            rm -rf output_dgm
            echo "   ✅ output_dgm 目录已删除"
        else
            echo "   跳过 output_dgm 清理"
        fi
    else
        echo "   没有找到 output_dgm 目录"
    fi
    echo ""
fi

# 6. 清理日志目录（可选）
if [ "$1" == "--all" ] || [ "$1" == "-a" ]; then
    echo "6. 清理日志目录..."
    if [ -d "logs" ]; then
        echo "   找到 logs 目录"
        read -p "   确认清理 logs/build_images 目录吗？(y/N): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            rm -rf logs/build_images/*
            echo "   ✅ logs/build_images 已清理"
        else
            echo "   跳过日志清理"
        fi
    else
        echo "   没有找到 logs 目录"
    fi
    echo ""
fi

echo "=== 清理完成 ==="
echo ""
echo "清理统计："
echo "  - 运行中的容器: $(docker ps --format '{{.Names}}' | grep -E 'dgm|sweb|testbed' | wc -l)"
echo "  - 所有容器: $(docker ps -a --format '{{.Names}}' | grep -E 'dgm|sweb|testbed' | wc -l)"
echo ""
echo "提示："
echo "  - 使用 '$0 --all' 或 '$0 -a' 来清理镜像和输出目录"
echo "  - 使用 'docker system prune' 来清理更多 Docker 资源"





