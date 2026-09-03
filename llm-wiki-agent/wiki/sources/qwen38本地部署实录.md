---
title: "Qwen3.8 本地部署实录（这台机器）"
type: source
tags: [部署, ollama, 本地推理, 坑]
date: 2026-09-03
source_file: raw/qwen38本地部署实录.md
---

## Summary
本机（RTX 5090 D 32GB / 64GB / i7-14700F）用 [[Ollama]] 0.33.2 跑
[[Qwen38]]（27.3B，Q5_K_M，num_ctx 烤到 262144），omp 通过 OpenAI 兼容接口
（127.0.0.1:11434/v1，无 key）接入作为默认模型。实测 GPU offload 100%、
常驻 29GB、显存 31.7/32.6GB（贴地）。记录 6 个部署坑：GitHub 443 不通、
262k 上下文吃满显存、thinking 吃 max_tokens、vision 模型缺 role 映射、
应用层与 git 层网络出口不同、bash/PowerShell 混用翻车。

## Key Claims
- 27.3B Q5_K_M 权重约 19GB，262k 上下文的 KV cache 约占 10GB → "刚好够"不是"富余"
- num_ctx 262144 是烤进 Modelfile 的非默认参数（ollama 默认 4096），不改则长上下文归零
- thinking 模式下 max_tokens:10 全部消耗在 reasoning，正文为空 → maxTokens 必须配大
- vision 模型下载就绪 ≠ 可用：config.yml 缺 modelRoles.vision 映射则视觉功能全报错
- 本地 curl 真发请求 1.4s 出 10 tokens（含 thinking，prompt 57 tokens）
- 并发第二 27B 级模型放不下（unload 需 ~5min 空闲）

## Key Quotes
> "num_ctx 是按 262144 烤进 Modelfile 的，不是 ollama 默认值——默认 num_ctx 只有 4096，不改的话长上下文能力直接归零。" — 部署最关键的"非默认参数"

> "这套组合能用但不宽裕：显存贴地、并发不了第二模型、思考模式吃 token。" — 总体判断

## Connections
- [[Ollama]] — 部署运行时（Windows 托盘服务，11434 端口）
- [[Qwen38]] — 被部署的模型（27.3B / Q5_K_M / 262k）
- [[LocalDeployment]] — 本笔记所属主题：本地推理栈的构成与限制
- [[Quantization]] — Q5_K_M vs Q4_K_M 直接决定显存预算档位

## Contradictions
- （当前无）此源与库内现有三源无冲突；与 [[llm-wiki调研与选型]] 互补
  （调研笔记的"本机实跑结论"引用了本源的坑 #1）。
