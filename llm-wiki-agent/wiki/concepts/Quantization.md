---
title: "Quantization"
type: concept
tags: [主题, 模型压缩]
sources: [qwen38本地部署实录]
last_updated: 2026-09-03
---

# Quantization（量化）

LLM 权重的位压缩，直接决定 32GB 级显存能放下多大的模型。

## 本 wiki 中的实例
[[Qwen38]] 用 **Q5_K_M**（~5.5 bit/weight）：
- 27.3B 权重 ≈ 19GB 磁盘 / ~22GB 显存常驻（叠加 KV cache 后 resident 29GB）
- 比 Q4_K_M 高两档精度，比 Q8 小约 40% 显存
- 对 5090 D（32GB）是"刚好够"的折中：Q8 放不下 262k 上下文，Q4 省显存但有更多压缩损失

## 相关权衡
- 显存预算 vs 精度 vs 上下文长度，三者互相挤压
- 量化档位还影响 thinking 质量（低量化下长推理更容易乱，wiki 内暂无实测数据，
  属于 data gap）
