# Wiki Index

## Overview
- [Overview](overview.md) — living synthesis across all sources

## Sources
- [Karpathy 谈 LLM Wiki：让知识自己长出来](sources/karpathy-llm-wiki访谈.md) — 正方：LLM Wiki 复利型、值得长期养
- [笔记：Obsidian 双链工作流实录（自用）](sources/obsidian双链工作流实录.md) — 痛点实证：手工双链累、无综合、会腐烂
- [我为什么放弃了那个 LLM 知识库（一篇劝退文）](sources/为什么放弃LLM知识库.md) — 反方：同一机制是隐性成本 + 漂移
- [Qwen3.8 本地部署实录（这台机器）](sources/qwen38本地部署实录.md) — Ollama + Q5_K_M + 262k 的部署基线与 6 个坑
- [llm-wiki 调研与选型](sources/llm-wiki调研与选型.md) — 生态对比、选型理由、本机实跑分层结论

## Entities
- [Karpathy](entities/Karpathy.md) — LLM Wiki 模式的主要倡导者
- [Qwen3.8](entities/Qwen38.md) — 本 wiki 驱动模型（27.3B / Q5_K_M / 262k）
- [Ollama](entities/Ollama.md) — 本地 LLM 运行时，omp 与模型之间的 OpenAI 兼容层
- [RAG](entities/RAG.md) — 检索增强生成，LLM Wiki 的主要对照组
- [LLM Wiki Agent](entities/LLMWikiAgent.md) — 选定的开源项目（SamurAIGPT，MIT，agent-skill 形态）
- [obsidian-llm-wiki-local](entities/ObsidianLLMWikiLocal.md) — 被放弃的备选（本地 Ollama + Obsidian，已转维护模式）
- [Obsidian](entities/Obsidian.md) — 双链笔记软件，手工双链实践的载体

## Concepts
- [LLMWiki](concepts/LLMWiki.md) — 编译式知识库模式（核心价值论断有争议）
- [CrossReference](concepts/CrossReference.md) — 交叉引用 / 互链，自动 vs 手工
- [KnowledgeRot](concepts/KnowledgeRot.md) — 知识腐烂：旧结论失效但不被标记
- [HealthCheck](concepts/HealthCheck.md) — 健康检查：定期全库扫描矛盾/缺口/过时
- [DoubleLinking](concepts/DoubleLinking.md) — wikilink 双链，LLM Wiki 的技术底座
- [LocalDeployment](concepts/LocalDeployment.md) — omp→Ollama→GPU 链路的预算与 6 个坑
- [Quantization](concepts/Quantization.md) — 量化档位 vs 显存预算 vs 精度的三方挤压

## Syntheses
- [LLM Wiki 值得长期投入吗？](syntheses/llm-wiki-值得长期投入吗.md) — 裁决需要"查询/ingest 比"这个缺变量
