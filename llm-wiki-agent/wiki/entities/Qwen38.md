---
title: "Qwen3.8"
type: entity
tags: [模型, 本地推理]
sources: [qwen38本地部署实录]
last_updated: 2026-09-03
---

# Qwen3.8（qwen3.8-q5-262k）

本 wiki 的驱动模型：27.3B 参数（架构代号 qwen35），来自社区 GGUF
`smtek/Qwen3.8-27B:Q5_K_M`，Q5_K_M 量化（~5.5 bit/weight，见 [[Quantization]]），
num_ctx 烤到 262144。经 [[Ollama]] 在 RTX 5090 D 上 100% GPU 运行。

## 能力与限制（wiki 内证据）
- 支持 tools / thinking / completion
- **thinking 模式消耗 max_tokens 预算**：实测 max_tokens:10 时正文为空，
  token 全在 reasoning 字段 → 配置 maxTokens 必须远大于预期正文长度
- **无图像输入**（当前加载的是文本模型；另有 `qwen3.8-q5-vision` 20GB
  在 ollama 就绪，但 omp 未配 `modelRoles.vision`，视觉功能不可用）
- 上下文 262k：可一次吞下代码库级文档，代价是 KV cache 约 10GB 显存

## 部署数据
- 权重磁盘 ~19GB，运行时 resident 29GB
- 显存 31.7/32.6GB（贴地），并发第二 27B 级模型放不下
