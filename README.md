# wit-wiki：智讯品牌营销知识库

WIT 智讯策划咨询的品牌营销知识库。基于 Karpathy LLM Wiki 方法论构建，专为 AI Agent 优化的结构化知识资产。

## 快速开始

```bash
git clone https://github.com/csmyzi1985/wit-wiki.git
cd wit-wiki
```

支持 Claude Code、Codex、Hermes Agent 等任何支持 `AGENTS.md` 的 AI 编程工具 — 进入目录后自动加载知识库上下文。

### 在 Hermes 中使用

```bash
cd ~/Documents/maizicheng/wit-wiki
hermes
```

### 在 Claude Code 中使用

```bash
cd wit-wiki
claude
```

### 在其他 AI Agent 中使用

进入 `wit-wiki` 目录启动你的 Agent 即可。项目根目录的 `AGENTS.md` 定义了知识库操作规范，Agent 会自动加载。

## 使用示例

- 「智讯做过哪些城市品牌案例？」
- 「反碎片方法论的核心逻辑是什么？」
- 「万科的项目有什么共性？」
- 「华与华的超级符号原理是什么？」

## 内容结构

| 目录 | 数量 | 说明 | 来源标识 |
|------|------|------|----------|
| `cases/` | 150 个 | 智讯自有品牌营销案例 | 🔵 |
| `methodology/` | 31 篇 | 智讯方法论体系 | 🔵 |
| `hua-yu-hua/` | 178 篇 | 华与华外脑（仅供内部参考） | 🔴 |
| `industries/` | 1 篇 | 行业洞察（建设中） | 🟡 |
| `synthesis/` | 2 篇 | 综合分析 | 🔵 |

### 来源标识说明

| 标识 | 含义 | 用途限制 |
|------|------|----------|
| 🔵 | 智讯自有内容 | 可用于客户提案 |
| 🔴 | 华与华外脑 | **仅供内部学习，不可直接用于客户提案** |
| 🟢 | 联网搜索结果 | 待核实 |
| 🟡 | 内部编写 | 持续更新中 |

## 更新

```bash
git pull
```

## 许可

内部知识库，仅限智讯团队及授权合作伙伴使用。

## 维护者

麦子程 · WIT 智讯策划咨询
