#!/bin/bash
# wit-wiki 一键安装脚本
# 自动检测本机 AI Agent 平台，安装 skill + 知识库

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
INSTALLED=0

echo "=== wit-wiki 知识库安装 ==="
echo ""

# 安装函数：创建目标目录，复制 SKILL.md，软链 wiki 内容
install_to() {
    local TARGET="$1"
    local PLATFORM="$2"
    mkdir -p "$TARGET"
    cp "$SCRIPT_DIR/SKILL.md" "$TARGET/SKILL.md"
    # 软链 wiki 内容目录
    for dir in cases methodology hua-yu-hua industries clients synthesis competitors visual-cases assets; do
        [ -d "$SCRIPT_DIR/$dir" ] && ln -sfn "$SCRIPT_DIR/$dir" "$TARGET/$dir"
    done
    # 软链关键文件
    for f in index.md AGENTS.md SCHEMA.md; do
        [ -f "$SCRIPT_DIR/$f" ] && ln -sfn "$SCRIPT_DIR/$f" "$TARGET/$f"
    done
    echo "  ✅ $PLATFORM → $TARGET"
    INSTALLED=$((INSTALLED + 1))
}

# Claude Code
[ -d "$HOME/.claude/skills" ] && install_to "$HOME/.claude/skills/wit-wiki" "Claude Code"

# OpenClaw
[ -d "$HOME/.openclaw/skills" ] && install_to "$HOME/.openclaw/skills/wit-wiki" "OpenClaw"

# WorkBuddy
if [ -d "$HOME/.workbuddy" ]; then
    install_to "$HOME/.workbuddy/wit-wiki" "WorkBuddy"
    echo "     💡 WorkBuddy 需在对话中引用 ~/.workbuddy/wit-wiki/SKILL.md"
fi

echo ""
if [ $INSTALLED -eq 0 ]; then
    echo "  ❌ 未检测到已安装的 AI Agent 平台"
    echo "     支持：Claude Code / OpenClaw / WorkBuddy"
    exit 1
fi

echo "=== 安装完成 ($INSTALLED 个平台) ==="
echo ""
echo "使用：在对应平台中提问品牌/营销/案例相关问题"
echo "更新：cd $SCRIPT_DIR && git pull"
