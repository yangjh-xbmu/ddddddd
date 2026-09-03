---
title: "llm-wiki 调研与选型"
type: source
tags: [调研, 选型, llm-wiki, 开源]
date: 2026-09-03
source_file: raw/llm-wiki调研与选型.md
---

## Summary
对 LLM Wiki 生态（2026-09）的调研与选型记录：概念源于 Karpathy 2026-04 的
idea file；候选包括 inkeep/open-knowledge（~3.9k⭐, GPL v3）、
SamurAIGPT/llm-wiki-agent（~3.5k⭐, MIT）、kytmanov/obsidian-llm-wiki-local
（~820⭐, MIT, 已转维护模式）等。选型结论：本机先跑 **llm-wiki-agent**
（零 API key、schema 即文档、MIT、health.py 确定性可离线）。并记录本机
实跑结论：确定性 layer（schema + health.py）可靠；语义 layer（ingest 判断、
query 综合、语义 lint）受本地 Q5 模型质量限制；离线环境下
build_graph.py 只能跑 Pass-1、lint.py 只能跑确定性部分。

## Key Claims
- 选型四理由：零外部依赖 / schema 即文档 / MIT / health.py 确定性
- 放弃 open-knowledge（GPL v3 + Node24 运行时，试用太重）与 OLW（转维护模式 + 依赖多）
- 调研时点各项目星数：open-knowledge ~3.9k、llm-wiki-agent ~3.5k、OLW ~820
- 本地可靠 layer = schema + health.py；模型依赖 layer = ingest/query/语义 lint
- 离线跑该项目的 4 个已知坑：git 偶发 443 / lint-语义要 API / graph Pass-2 要 API / 正文里双中括号 wikilink 字面量会触发假断链
- 落地路径：先用 llm-wiki-agent + 本地模型跑日常，质量不够处等强模型再上 OLW/open-knowledge 补强

## Key Quotes
> "agent 读 schema 自己维护 wiki，零 API key、零服务 —— 这是唯一'读 README 就能跑'的。" — 选型核心理由

> "确定性 layer 可靠；语义 layer 受本地模型质量限制。" — 本机实跑的分层结论

## Connections
- [[LLMWikiAgent]] — 选定的项目
- [[LLMWiki]] — 被调研的模式（与 [[karpathy-llm-wiki访谈]] 的主题衔接）
- [[Karpathy]] — 概念提出者
- [[qwen38本地部署实录]] — 本机实跑结论所依赖的部署前提
- [[ObsidianLLMWikiLocal]] — 被放弃但特性值得借鉴的备选

## Contradictions
- 与 [[为什么放弃LLM知识库]] 的方向性张力：本源决定"继续跑 llm-wiki-agent"，
  反方源主张"别当基础设施养"。本源的处理：定位为"试用 + 确定性 layer 落地"，
  不承诺"长期养"，从而与反方论点不直接冲突（见 LLMWiki 页的裁决变量）。
