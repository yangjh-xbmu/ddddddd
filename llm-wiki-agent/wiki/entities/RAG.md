---
title: "RAG"
type: entity
tags: [技术, 检索]
sources: [karpathy-llm-wiki访谈]
last_updated: 2026-09-03
---

# RAG

Retrieval-Augmented Generation（检索增强生成）。本 wiki 中它作为 [[LLMWiki]]
的对照组反复出现。

## 工作方式
每次查询时，现场从语料中检索 chunks（embedding + 向量库 + 分块 + 重排），再让
LLM 基于检索结果推导答案。

## 被指出的缺陷
来自 [[Karpathy]] 访谈：
- 没有跨查询的积累，"本质上每次都是重新推导"
- 语料增长时，pipeline 复杂度快速上升、开始发皱

## 相关
- [[为什么放弃LLM知识库]] — 反对派视角，对 RAG 的替代价值有另一套论点
