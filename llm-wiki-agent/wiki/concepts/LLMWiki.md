---
title: "LLM Wiki"
type: concept
tags: [模式, 知识管理]
sources: [karpathy-llm-wiki访谈, 为什么放弃LLM知识库]
last_updated: 2026-09-03
---

# LLM Wiki

一种由 LLM 维护的"编译式"个人知识库模式，由 [[Karpathy]] 倡导（见
[[karpathy-llm-wiki访谈]]）。

## 结构
- `raw/` — 不可变源文件（论文/笔记/网页），ground truth，永不修改
- `wiki/` — LLM 从 raw 编译出的互链 markdown：概念页、实体页、活综合页（overview），
  每个页面用 wikilink 双链语法（形如双中括号 + 页名）指回相关页，并可指回 raw 源

## 核心机制
- **编译一次、持续更新**：新材料 ingest 后，概念页被改写、[[CrossReference]]
  补齐、[[KnowledgeRot]]（过时结论）被当场标记
- **[[HealthCheck]]（健康检查）**：定期全库扫描矛盾/缺口/过时，让库"被主动维护"
- **无需向量库**：靠目录 + 索引页 + 互链导航，[[Karpathy]] 报告 100 篇/40 万词仍流畅

## 价值论断（**有争议**）
- 正方：复利型，质量随时间上升（[[karpathy-llm-wiki访谈]]）
- 反方：同一套机制是**隐性维护成本 + 漂移**——"高 ingest、低查询"使复利很少兑现；
  自动改写 10 次后分不清原话与模型脑补（[[为什么放弃LLM知识库]]）
- **本 wiki 已记录的实质矛盾**：两源对同一机制（自动改写 / 补链 / 健康检查）
  给出相反价值判断（复利 vs 负债）。反方**不否定**结构本身，只反对"长期当基础设施养"。

## 对照
- [[DoubleLinking]]（手工）：能双链但无自动综合与过期清理
- [[RAG]]：能检索但无积累，每次重新推导
