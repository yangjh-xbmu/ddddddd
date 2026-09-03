# 笔记：Qwen3.8 本地部署实录（这台机器 · 2026-09-03）

## 部署形态

本机用 Ollama 跑 Qwen3.8，omp（omp 编码 harness）通过 OpenAI 兼容接口连过去。
整条链路：

```
omp (Windows Terminal)
  └─ models.yml 定义 provider "ollama-local"
       baseUrl: http://127.0.0.1:11434/v1   (OpenAI chat completions 协议)
       auth: none                            (本机回环，无 key)
  └─ config.yml: modelRoles.default: ollama-local/qwen3.8-q5-262k
Ollama 0.33.2 (Windows 托盘服务，开机自启，127.0.0.1:11434)
  └─ 模型 qwen3.8-q5-262k:latest  (27.3B 参数, Q5_K_M 量化, 19 GB 磁盘)
  └─ 推理: 100% GPU (nvidia-smi 确认, 进程级 100% GPU offload)
  └─ 运行时实测 (ollama ps): resident 29 GB, context 262144,
     unload 策略 ~5 分钟空闲后卸载
另有一个 qwen3.8-q5-vision:latest (20 GB) —— 带视觉，但 omp 未配 vision role，
所以本 session 里 inspect_image / 图片输入全部不可用（报错：当前模型不支持
image input）。
```

## 硬件基线（本部署的前提）

| 项 | 实测值 |
|---|---|
| GPU | RTX 5090 D（32 GB VRAM，驱动 591.59） |
| 内存 | 64 GB DDR5 |
| CPU | i7-14700F |
| 部署后显存占用 | 31.7 / 32.6 GB（模型权重 + KV cache，几乎吃满） |

29 GB 常驻 vs 32 GB 显存：Q5_K_M 27.3B 权重约 19 GB，剩下约 10 GB 是
262144 上下文的 KV cache。这台机器是"刚好够"，不是"富余"。

## 模型参数（`ollama show` 原文）

```
architecture   qwen35           (27.3B 参数)
quantization   Q5_K_M           (约 5.5 bit/weight，比 Q4_K_M 高两档)
num_ctx        262144           (≈ 262k 上下文)
temperature 1 / top_p 0.95 / top_k 20
capabilities: tools, thinking, completion   (支持工具调用 + 思考模式)
```

模型本体是社区 GGUF（`smtek/Qwen3.8-27B:Q5_K_M`）拉下来后在 ollama 里
tag 成了 `qwen3.8-q5-262k:latest`。`num_ctx` 是按 262144 烤进 Modelfile 的
（`PARAMETER num_ctx 262144`），不是 ollama 默认值——默认 num_ctx 只有
4096，不改的话长上下文能力直接归零。这是部署时最关键的"非默认参数"。

## 踩的坑（按发生顺序）

1. **GitHub 443 直连不通。** `git clone` 到 github.com 直接
   `Failed to connect ... port 443`，但 web/HTTPS 代理通道是通的。绕过方式：
   走 `raw.githubusercontent.com` 逐文件拉（本次 llm-wiki-agent 就是这
   样还原的）。教训：这台机器 git 要配 proxy 或走 raw/镜像，否则大量
   "clone 依赖"的开源项目第一步就卡死。
2. **262k 上下文显存吃满。** 实测 nvidia-smi 31.7/32.6 GB。并发开第二个
   27B 级模型、或跑带 20GB 的 vision 模型同时驻留都放不下。ollama 的
    unload 是空闲 ~5 分钟才生效，切换模型时有等待窗口。小显存机器要主动
   把 num_ctx 降下来（262k → 32k 能省一大截 KV cache）。
3. **thinking 模式吃掉 max_tokens 预算。** 本地 curl 实测：`max_tokens:10` 时
   输出正文是空的，10 个 token 全花在 `reasoning` 字段里
   （"The user wants me to reply with exactly OK"）。maxTokens 配置必须远大于
   预期正文长度，否则"模型没说话"。文本模型配了 8192 / vision 配了 16384。
4. **vision 模型下载了 ≠ 视觉能力可用。** `qwen3.8-q5-vision` 在 ollama 里
   就绪，但 omp 的 `config.yml` 只有 `modelRoles.default`，没有
   `modelRoles.vision`，于是图片附件 / inspect_image 全部报错。配置
   缺一条 role 映射，20GB 模型等于白下。
5. **工具/浏览器通道和 LLM 通道是分开的网络出口。** headless Chromium 能
   访问 unpkg CDN（vis.js 加载成功），git 却连不上 github.com——排查网络
   不能只看"模型通不通"，要分清是应用层（浏览器/代理）还是 git 层的问题。
6. **shell 是 bash 而非 PowerShell。** pi 的 bash 层里 `Get-xxx` /
   `Format-Table` 直接报"command not found"或 syntax error；复杂 PS 片段
   要先写成 .ps1 文件再 `powershell -File` 执行。内联 `$_` 会被 bash 展开，
   是高频翻车点。

## 验证方法（这次用的三条命令）

```bash
ollama list                 # 模型都在不在、多大
ollama ps                   # 是否驻留、显存多少、多少 GPU offload、ctx
nvidia-smi --query-gpu=memory.used --format=csv
ollama show <model> --modelfile   # 烤进去的参数（num_ctx 是不是改过）
curl http://127.0.0.1:11434/v1/chat/completions  # 真发一次请求测延迟
```

本次真发请求：1.4 s 出 10 tokens（含 thinking，prompt 57 tokens）。

## 结论

这套"Ollama + Q5_K_M + 262k + 5090D"组合**能用但不宽裕**：
- 优点：本地免费、无审核、262k 能一次吞整个代码库级文档、支持工具调用
- 代价：显存贴地、并发不了第二模型、思考模式吃 token、maxTokens 要配大
- 适用：长文档理解、代码库级问答、不需要图片的 agent 工作流
- 不适用：多模型同时驻留、需要 vision 的场景（除非把 vision role 配上）
