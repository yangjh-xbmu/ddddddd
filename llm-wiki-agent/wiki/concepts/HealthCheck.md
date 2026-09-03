---
title: "HealthCheck"
type: concept
tags: [机制, 质量保障]
sources: [karpathy-llm-wiki访谈]
last_updated: 2026-09-03
---

# HealthCheck（健康检查）

定期让 LLM 把整个 wiki 扫一遍，找出质量问题。是 [[LLMWiki]] 从"只进不出的仓库"
变成"被主动维护的活系统"的关键环节。

## 检查什么
- **矛盾**：不同页面/来源的结论互斥
- **缺口**：wiki 无法回答的重要问题 → 建议补充哪些源
- **过时**：被新证据推翻的旧结论（即 [[KnowledgeRot]]）
- **孤立页**：没有任何入链的页面（可能建错或被孤儿化）

## 在 AGENTS.md 中的实现边界
- `health`（结构、零 LLM 调用、每次会话跑）
- `lint`（语义、调用 LLM、每 10–15 次 ingest 跑一次）

> 注意：本概念与"自动化改写的漂移风险"相关——见待补材料。
