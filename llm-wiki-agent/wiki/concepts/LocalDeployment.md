---
title: "LocalDeployment"
type: concept
tags: [主题, 本地推理]
sources: [qwen38本地部署实录, llm-wiki调研与选型]
last_updated: 2026-09-03
---

# LocalDeployment（本地部署）

"omp → Ollama → 本地 GPU" 这条推理链路的构成、预算与限制。

## 链路
```
omp (models.yml: provider ollama-local, baseUrl 127.0.0.1:11434/v1)
  → Ollama (0.33.2, OpenAI 兼容协议, 无 key)
    → qwen3.8-q5-262k (100% GPU, resident 29GB)
```

## 预算公式（本部署实测）
显存占用 ≈ 模型权重（19GB）+ 262k 上下文 KV cache（~10GB）≈ 29GB，
对 32GB 卡 = 贴地。**num_ctx 是最敏感的调节旋钮**（默认 4096 → 烤到
262144 的代价就是全部 KV cache）。

## 本机 6 个坑（摘要）
1. GitHub 443 偶发超时（clone 21s 失败，同 host push 2.7s 成功）→ 重试 / 走 raw / 配 proxy
2. 262k 吃满显存，并发不了第二 27B 模型
3. thinking 吃 max_tokens，正文可能为空
4. vision 模型没配 modelRoles.vision = 白下
5. 应用层网络 ≠ git 层网络，排查要分清
6. pi 的 bash 层里 PowerShell 语法要写 .ps1 再执行（`$_` 被 bash 吞）

## 对上层项目的影响
本地模型质量决定了 [[LLMWikiAgent]] 的**语义 layer** 天花板；
确定性 layer（health.py、Pass-1 图谱）与模型质量无关、完全可靠。
