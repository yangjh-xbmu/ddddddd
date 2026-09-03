---
title: "obsidian-llm-wiki-local"
type: entity
tags: [项目, 开源, 本地推理]
sources: [llm-wiki调研与选型]
last_updated: 2026-09-03
---

# obsidian-llm-wiki-local (OLW)

kytmanov 的项目（MIT，调研时点 ~820⭐）：Obsidian 友好的 [[LLMWiki]]
实现，主打 **100% 本地 + Ollama**，pip 安装，CLI 驱动。

## 调研中值得借鉴的特性
- **拒绝反馈**：reject 一篇 draft 并附理由 → 下次 compile 把反馈带进 prompt
- **手改保护**：agent 检测到人工编辑过即跳过重生成，不覆盖
- **git 感知 + undo**：自动动作带 `[olw]` 前缀提交，`olw undo` 可回滚

## 状态（重要）
**已转维护模式**，后继项目为 `kytmanov/synto`。选型时被放弃的原因：
转维护 + 依赖多 + 默认 7B+ 模型才好用（见 [[llm-wiki调研与选型]]）。
其"拒绝反馈"与"手改保护"是两个 LLM Wiki 通用需求，值得在
[[LLMWikiAgent]] 或其他实现里手动补上。
