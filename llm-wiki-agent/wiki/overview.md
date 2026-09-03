---
title: "Wiki Overview"
type: synthesis
tags: [overview]
sources: [karpathy-llm-wiki访谈, obsidian双链工作流实录, 为什么放弃LLM知识库, qwen38本地部署实录, llm-wiki调研与选型]
last_updated: 2026-09-03
---

# Overview

（本页面为"活综合"——每次 ingest 后由 agent 修订，反映全 wiki 的当前结论。）

## 当前主线
两条线交织：
1. **LLM Wiki 到底值不值得长期投入**（3 源：正方 / 痛点实证 / 反方）
2. **本机如何把 LLM 知识库跑起来**（2 源：本地部署实录 + 调研选型）

## 第 1 线：LLM Wiki 价值之争
- 正方 [[karpathy-llm-wiki访谈]]：复利型、无需向量库、值得长期养
- 痛点实证 [[obsidian双链工作流实录]]：手工 [[DoubleLinking]] 累、无综合、
  [[KnowledgeRot]] 不显眼 —— LLM Wiki 要解决的问题真实存在
- 反方 [[为什么放弃LLM知识库]]：同一机制是隐性成本 + 漂移，"高 ingest 低查询"
  使复利不兑现
- **已记录的实质矛盾**：[[LLMWiki]]"复利 vs 负债"，裁决变量 = 查询/ingest 比（缺量化材料）

## 第 2 线：本机落地（2026-09-03 完成）
- 部署基线（[[qwen38本地部署实录]]）：Ollama 0.33.2 + [[Qwen38]]（27.3B
  Q5_K_M，262k ctx）跑在 RTX 5090 D，100% GPU、resident 29GB、显存贴地
- 选型（[[llm-wiki调研与选型]]）：**[[LLMWikiAgent]]**（MIT、零 API key、
  schema 即 agent 指令）；放弃 open-knowledge（GPL v3 + 重运行时）与
  [[ObsidianLLMWikiLocal]]（转维护模式）
- 分层结论：**确定性 layer**（schema + [[healthCheck]] 脚本 + Pass-1 图谱）
  与模型质量无关、完全可靠；**语义 layer**（ingest 判断、query 综合、语义 lint）
  天花板取决于本地模型能力
- **本 wiki 自身即为该部署的第一个工作实例**（13→20 页，含图谱）

## 两线交汇
反方"别当基础设施养"的论点在本机语境被软化：本地免费推理使 ingest 的
token 成本≈电费，反方的主要成本论点（"为每次操作付费"）在本地部署下不成立；
其"查询稀少"论点仍然有效 —— [[LocalDeployment]] + 本 wiki 的存续将由
真实查询频率裁决。

## 未决问题
- 查询/ingest 比的量化裁决（缺材料）
- 半自动折中（只建链不改写正文）是否存在（缺材料）
- [[Quantization]] 低档位下 thinking 质量退化幅度（缺实测）

## 已保存的综合
- [[llm-wiki-值得长期投入吗]] — 第 1 线 query 答案
