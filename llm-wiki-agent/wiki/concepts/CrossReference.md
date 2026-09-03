---
title: "CrossReference"
type: concept
tags: [机制, 知识管理]
sources: [karpathy-llm-wiki访谈, obsidian双链工作流实录]
last_updated: 2026-09-03
---

# CrossReference（交叉引用 / 互链）

把相关页面用 wikilink 双链语法（形如双中括号 + 页名）串起来，是"编译式"与"检索式"知识库的关键分野。

- **自动交叉引用**：LLM 在 ingest 时识别"这篇新资料和库里哪些概念页有关"，
  并补上链接——这是 [[LLMWiki]] 的核心卖点之一，也是 [[karpathy-llm-wiki访谈]]
  称"查询为什么不用向量库也成立"的原因。
- **手工交叉引用**：[[obsidian双链工作流实录]] 作者明确指出的痛点——三个月只补了
  不到一半应建链接，累且不可持续。

## 为什么重要
互链密度决定了"导航成本"。密度够高，模型顺着链走就能找到（[[Karpathy]] 称"像
人查资料"）；密度太低，[[LLMWiki]] 就退化成一堆孤立文档。
