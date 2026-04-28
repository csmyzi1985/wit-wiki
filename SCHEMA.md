# 智讯知识库 Wiki Schema

## 知识来源体系

本知识库整合三个来源，统一入口，但通过 `source_origin` 字段和视觉标识严格区分：

| 来源 | source_origin | 颜色 | 标识 | 用途 |
|------|--------------|------|------|------|
| 智讯自有 | `wit` | 🔵 蓝色 | 智讯自有 · 案例/方法论 | 证明能力、复用经验 |
| 华与华外脑 | `hua-yu-hua` | 🔴 红色 | 华与华参考 · 仅供内部学习 | 理论框架、方法论参考 |
| 竞品外脑 | `competitor` | ⚪ 灰色 | 竞品参考 · 公司名 · 仅供内部学习 | 竞争情报、差异化参考 |

**重要规则**：华与华和竞品内容仅供内部学习，不可直接用于客户提案。

## 目录结构

```
wit-wiki/
├── cases/              ← 智讯案例
├── methodology/        ← 智讯方法论
├── industries/         ← 行业洞察
├── hua-yu-hua/         ← 华与华外脑
│   ├── methods/        ← 核心方法论卡片
│   ├── cases/          ← 经典案例
│   └── models/         ← 理论模型
├── competitors/        ← 竞品外脑（按公司分子目录）
├── clients/            ← 客户画像
├── synthesis/          ← 综合分析
├── assets/             ← 可复用素材
└── visual-cases/       ← 视觉案例
```

## Frontmatter 规范

### 公共字段（所有页面必须包含）

```yaml
---
type: case | methodology | industry | reference | index
source_origin: wit | hua-yu-hua | competitor
title: "页面标题"
source: "原始来源标识"
---
```

### 智讯案例页 (cases/)

```yaml
---
type: case
source_origin: wit
title: "项目名称"
date: YYYY
industry: 行业
client: "客户名"
methodology: [用到的方法论]
keywords: [关键词]
decision_logic: "一句话决策逻辑"
source: "原始文章目录名"
---
```

正文开头必须有来源标识块：`> 🔵 **智讯自有** · 案例`

### 智讯方法论页 (methodology/)

```yaml
---
type: methodology
source_origin: wit
title: "方法论名称"
---
```

正文开头必须有来源标识块：`> 🔵 **智讯自有** · 方法论`

### 华与华参考页 (hua-yu-hua/)

```yaml
---
type: reference
source_origin: hua-yu-hua
title: "方法论/案例名称"
methodology: [相关方法论]
keywords: [关键词]
source: "来源"
---
```

正文开头必须有来源标识块：`> 🔴 **华与华参考** · 仅供内部学习，不可直接用于客户提案`

### 竞品参考页 (competitors/)

```yaml
---
type: reference
source_origin: competitor
company: "公司名称"
title: "案例名称"
date: YYYY
industry: 行业
methodology: [相关方法论]
keywords: [关键词]
source: "来源"
---
```

正文开头必须有来源标识块：`> ⚪ **竞品参考** · 公司名 · 仅供内部学习，不可直接用于客户提案`

### 行业页 (industries/)

```yaml
---
type: industry
source_origin: wit
title: "行业名称"
---
```

## 摄入规则

1. 每条断言必须标注来源 `[R: 文件名]`
2. 新页面必须被 `index.md` 引用
3. 每次摄入必须更新 `log.md`
4. 交叉引用用 `[[页面名]]` 格式
5. 图片引用使用相对路径
6. 新页面必须包含 `source_origin` 字段和对应来源标识块

## 质量标准

- 不允许无来源的断言
- 不允许孤儿页面（至少被 index.md 引用）
- 同一概念不允许有两个页面（合并或重定向）
- 案例页必须包含至少一个数据点
- 华与华和竞品页面必须标注"仅供内部学习"

## Obsidian 配置

Vault 根目录：`/Users/csmyz/Documents/maizicheng/`

- CSS 样式：`{vault}/.obsidian/snippets/source-colors.css`（目录颜色区分）
- 模板：`{vault}/05-Templates/` 下三个模板文件（智讯案例、华与华方法论、竞品案例）
- 使用前需在 Obsidian 设置 > 外观 > CSS 代码片段 中启用 `source-colors`
