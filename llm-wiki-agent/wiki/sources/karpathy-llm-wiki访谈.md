---
title: "Karpathy 谈 LLM Wiki：让知识自己长出来"
type: source
tags: [llm-wiki, 访谈, 播客]
date: 2026-04-12
source_file: raw/karpathy-llm-wiki访谈.md
---

## Summary
Andrej Karpathy 在播客访谈中描述其实验：把论文、笔记、网页丢进 `raw/` 文件夹，
让 LLM 提炼成互链的 `wiki/` markdown 页面。约 100 篇文章、40 万词的规模下无需
向量数据库即可流畅查询。他强调 LLM Wiki 是"编译一次、持续更新"的复利型系统，
区别于每次重新检索的 RAG，并认为这套模式对个人研究者与独立开发者是性价比最高的
知识管理方式。

## Key Claims
- 100 篇/40 万词规模的 wiki 不需要 RAG 和向量库，模型顺着目录、索引页、互链即可查询
- LLM Wiki 是复利型的：新材料进来会改写概念页、补交叉引用、当场标记矛盾
- 定期"健康检查"（lint）让知识库从仓库变成被主动维护的活系统
- 明确立场：这套东西值得长期投入，质量随时间上升而不是腐烂

## Key Quotes
> "RAG 每次提问都要重新检索、重新推导一遍答案，本质上没有积累。而 LLM Wiki 是'编译一次，持续更新'。" — 对比 RAG 的核心论断

> "它不像 RAG pipeline 那样一旦语料变多就开始发皱，它是复利型的——你投的每一篇材料都在抬高整个库的天花板。" — 对长期价值的判断

## Connections
- [[Karpathy]] — 提出并实践该模式的人
- [[LLMWiki]] — 本文核心模式
- [[RAG]] — 被作为对照的对象
- [[HealthCheck]] — Karpathy 称"最被低估"的环节
- [[CrossReference]] — 互链带来的查询能力

## Contradictions
- （当前无。这是 wiki 的第一篇 source。）
