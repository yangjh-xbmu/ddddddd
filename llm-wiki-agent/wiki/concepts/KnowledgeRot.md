---
title: "KnowledgeRot"
type: concept
tags: [问题, 知识管理]
sources: [obsidian双链工作流实录]
last_updated: 2026-09-03
---

# KnowledgeRot（知识腐烂）

指知识库中的旧结论/旧事实随时间失效，但**系统不会主动告诉你哪条已经过期**，
于是查询命中的可能是几个月前的错误信息，且使用者无从察觉。

## 证据
- [[obsidian双链工作流实录]]：作者三个月实测，"查到的可能是三个月前的错误结论，
  而你不会知道它是过时的"。

## 对策（wiki 内）
- [[LLMWiki]] / [[HealthCheck]]：定期让 LLM 全库扫描，标记被新证据推翻的旧结论。
  [[Karpathy]] 称健康检查是"最被低估的环节"，正是冲着 KnowledgeRot 去的。

> 待补：反方是否认为"过度标记矛盾"本身会引入噪音？（尚无材料支持此方向）
