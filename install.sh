#!/bin/bash
# wit-wiki 一键安装脚本
# 自动检测本机 AI Agent 平台，选择安装

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "=== wit-wiki 知识库安装 ==="
echo ""

# 检测可用平台
PLATFORMS=()
[ -d "$HOME/.claude/skills" ] && PLATFORMS+=("Claude Code:$HOME/.claude/skills/wit-wiki")
[ -d "$HOME/.openclaw/skills" ] && PLATFORMS+=("OpenClaw:$HOME/.openclaw/skills/wit-wiki")
[ -d "$HOME/.workbuddy" ] && PLATFORMS+=("WorkBuddy:$HOME/.workbuddy/wit-wiki")

if [ ${#PLATFORMS[@]} -eq 0 ]; then
    echo "  ❌ 未检测到已安装的 AI Agent 平台"
    exit 1
fi

# 让用户选择
echo "检测到以下平台："
for i in "${!PLATFORMS[@]}"; do
    NAME="${PLATFORMS[$i]%%:*}"
    echo "  $((i+1))) $NAME"
done
echo "  a) 全部安装"
echo ""
read -p "选择安装到哪个平台 [1/${#PLATFORMS[@]}/a]: " CHOICE

# 安装函数
install_to() {
    local TARGET="$1"
    local PLATFORM="$2"
    mkdir -p "$TARGET"
    cp "$SCRIPT_DIR/SKILL.md" "$TARGET/SKILL.md"
    for dir in cases methodology hua-yu-hua industries clients synthesis competitors visual-cases assets; do
        [ -d "$SCRIPT_DIR/$dir" ] && ln -sfn "$SCRIPT_DIR/$dir" "$TARGET/$dir"
    done
    for f in index.md AGENTS.md SCHEMA.md; do
        [ -f "$SCRIPT_DIR/$f" ] && ln -sfn "$SCRIPT_DIR/$f" "$TARGET/$f"
    done
    echo "  ✅ $PLATFORM → $TARGET"
}

# 执行安装
if [ "$CHOICE" = "a" ] || [ "$CHOICE" = "A" ]; then
    for item in "${PLATFORMS[@]}"; do
        NAME="${item%%:*}"
        TARGET="${item#*:}"
        install_to "$TARGET" "$NAME"
    done
elif [[ "$CHOICE" =~ ^[0-9]+$ ]] && [ "$CHOICE" -ge 1 ] && [ "$CHOICE" -le ${#PLATFORMS[@]} ]; then
    ITEM="${PLATFORMS[$((CHOICE-1))]}"
    install_to "${ITEM#*:}" "${ITEM%%:*}"
else
    echo "  ❌ 无效选择"
    exit 1
fi

echo ""
echo "=== 安装完成 ==="
echo ""
echo "使用：在对应平台中提问品牌/营销/案例相关问题"
echo "更新：cd $SCRIPT_DIR && git pull"
