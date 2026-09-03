---
title: "笔记：Obsidian 双链工作流实录（自用）"
type: source
tags: [obsidian, 双链, 实践记录]
date: 2026-08-15
source_file: raw/obsidian双链工作流实录.md
---

## Summary
作者 2026-03 至 2026-08 三个月在 Obsidian 中用手工 [[DoubleLinking]]（双链）管理
个人笔记的实录。优点是概念关联显式、graph view 有发现感、纯本地文本零迁移成本。
缺点是双链需手动补（三个月只覆盖不到一半应建链接）、缺全局综合页、知识腐烂
（[[KnowledgeRot]]）不显眼。结论：纯手工双链适合灵感收集，不适合当知识库——
缺自动交叉引用与主动过期清理两样东西。

## Key Claims
- 手工 [[DoubleLinking]] 三个月只覆盖不到一半"该有的链接"，维护累
- 没有全局综合页（overview），每次回答都要自己翻多个文件再拼
- 旧笔记的过时观点不会被标出，查到的可能是三个月前的错误结论
- 结论：知识库需要"自动交叉引用 + 主动过期清理"，手工双链都给不了

## Key Quotes
> "真正的知识库需要两样东西：自动的交叉引用，和主动的过期清理。这两样，手工双链都给不了。" — 全文最核心的一句

> "查到的可能是三个月前的错误结论，而你不会知道它是过时的。" — 描述知识腐烂问题

## Connections
- [[Obsidian]] — 本实践所用工具
- [[DoubleLinking]] — 核心机制，与 [[LLMWiki]] 的自动交叉引用形成对照
- [[CrossReference]] — 作者明确指出的缺失能力
- [[KnowledgeRot]] — 作者观察到的核心失败模式
- [[LLMWiki]] — 被该源作为"可能的解法"间接提出

## Contradictions
- 与 [[karpathy-llm-wiki访谈]] 无直接矛盾，但构成**互补证据**：Karpathy 说 LLM Wiki
  的优势（自动交叉引用、健康检查）正是本源痛点的对解。（非矛盾，是"问题—解法"对应）
