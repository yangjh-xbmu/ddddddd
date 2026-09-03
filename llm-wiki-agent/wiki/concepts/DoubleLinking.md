---
title: "DoubleLinking"
type: concept
tags: [机制, 知识管理]
sources: [obsidian双链工作流实录]
last_updated: 2026-09-03
---

# DoubleLinking（双链 / wikilink）

用 wikilink 双链语法（形如双中括号 + 页名）把笔记/页面互相链接的机制，最早流行于 [[Obsidian]]。

## 在本 wiki 中的角色
- 是 [[LLMWiki]] 的技术底座：LLM Wiki 生成的正是带 wikilink 的 markdown，
  因此能直接在 Obsidian graph view 里浏览
- 单独作为"手工双链笔记"时，[[obsidian双链工作流实录]] 显示其局限：链接靠人手动
  补、缺全局综合、[[KnowledgeRot]] 不显眼

## 与 CrossReference 的区别
[[CrossReference]] 强调"建链这件事由谁做、何时做"（自动 vs 手工）；
[[DoubleLinking]] 只指"链接用 wikilink 表示"这一表示法。LLM Wiki ≈ 自动
CrossReference 生成 DoubleLinking。
