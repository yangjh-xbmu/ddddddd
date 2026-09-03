---
title: "LLM Wiki Agent"
type: entity
tags: [项目, 开源, agent-skill]
sources: [llm-wiki调研与选型]
last_updated: 2026-09-03
---

# LLM Wiki Agent

SamurAIGPT/llm-wiki-agent（MIT，调研时点 ~3.5k⭐）。**agent skill 形态**的
[[LLMWiki]] 实现：agent（Claude Code / Codex / OpenCode / 任意读 config 的
agent）读 `AGENTS.md` schema，自己当 wiki 维护者，零 API key、零服务。

## 结构
- `raw/` 源（不可变）· `wiki/`（sources/entities/concepts/syntheses 四层 +
  index/overview/log）· `graph/`（graph.json + graph.html）
- `tools/health.py` —— 确定性结构检查（空页/索引同步/log 覆盖），零 LLM 调用
- `tools/lint.py` / `tools/build_graph.py` —— 语义部分依赖 litellm（离线不可用）

## 在本 wiki 中的角色
- 本 wiki 即按它的 schema 运行（[[llm-wiki调研与选型]] 记录选型理由）
- 本机实跑分层结论：确定性 layer（schema + health.py）可靠；语义 layer
  质量取决于驱动模型（见 [[qwen38本地部署实录]] 关于本地模型能力的说明）

## 离线跑法（已验证）
- lint：只保留确定性部分（孤儿/断链/稀疏页/缺实体页），语义部分由 agent 手写报告
- graph：只跑 Pass-1（wikilink 确定性解析），跳过 Pass-2 语义推断
