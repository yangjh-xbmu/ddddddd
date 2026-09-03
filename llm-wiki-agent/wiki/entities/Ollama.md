---
title: "Ollama"
type: entity
tags: [工具, 本地推理, 运行时]
sources: [qwen38本地部署实录]
last_updated: 2026-09-03
---

# Ollama

本地 LLM 运行时（本部署用 v0.33.2，Windows 托盘服务，开机自启）。
对外暴露 **OpenAI 兼容 API**（`http://127.0.0.1:11434/v1`，本机回环无鉴权），
是 omp 接入本地模型的中转层。

## 本部署中的关键行为
- `ollama list` / `ollama ps` —— 模型清单、驻留状态、显存占用、GPU offload 比例
- 空闲 ~5 分钟自动 unload 模型（切换模型有等待窗口）
- **Modelfile 参数会被烤进模型**：本部署 `num_ctx 262144` 是非默认值
  （默认 4096），`ollama show --modelfile` 可查证
- `capabilities: tools, thinking, completion` —— 当前加载的 [[Qwen38]]
  支持工具调用与思考模式

## 相关
- [[Qwen38]] — 本运行时上跑的主模型
- [[LocalDeployment]] — 整条 omp → Ollama → GPU 链路的主题
