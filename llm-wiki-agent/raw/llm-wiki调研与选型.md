# 调研：LLM Wiki —— 概念、开源项目与选型（2026-09-03）

## 概念来源

"LLM Wiki" 是 Andrej Karpathy 2026-04 提出的 knowledge base 模式
（idea file: karpathy.ai/llmwiki，gist 442a6bf555914893e9891c11519de94f）。
核心论断：**不要把精力花在工程化检索（RAG）上，让 LLM 把知识预先编译成
结构化 wiki，检索就变成走目录和互链的简单事。**

机制：
- `raw/`（不可变源，ground truth）→ `wiki/`（LLM 编译的互链 markdown：
  概念页/实体页/活综合页 overview，页面间 wikilink，可指回 raw 源）
- 定期 health check（lint）：全库扫矛盾、缺口、过时结论 —— Karpathy 称
  为"最被低估的环节"
- query 的答案写回 wiki/syntheses/，库随使用复利增长
- 与 RAG 的分界：RAG 每次 query 重新检索+推导，无积累；LLM Wiki 编译一次、
  增量维护

## 调研到的开源项目（2026-09 时点）

| 项目 | 主语言 | 星数 | 定位 | 许可 |
|---|---|---|---|---|
| inkeep/open-knowledge | TS | ~3.9k | 完整产品：WYSIWYG markdown IDE + wiki，桌面/网页，agent 集成、git 同步 | GPL v3 |
| SamurAIGPT/llm-wiki-agent | Py | ~3.5k | 纯 agent skill：agent 读 schema 自己维护 wiki，零 API key、零服务 | MIT |
| kytmanov/obsidian-llm-wiki-local (OLW) | Py | ~820 | 100% 本地 + Ollama，Obsidian 友好，watcher/undo/git 感知；**已转维护模式**，后继为 kytmanov/synto | MIT |
| alsayadi/karpathy-llm-wiki-plugin | - | ~7 | Claude Code 最小插件（/wiki），可作参考实现 | MIT |
| ThinkInAIXYZ（LLM Wiki 桌面 app） | - | - | 跨平台桌面应用，文档自动组织互链 | - |
| 周边：llm-wiki.net（agent 插件生态）、llmwikis.org（handbook）、Google OKF（跨 agent 可分享 wiki 标准，2026 新） | | | | |

## 选型决策：SamurAIGPT/llm-wiki-agent

选它的理由（针对本机环境）：
1. **零外部依赖**：不需要 API key、不需要起服务——agent（包括本地小模型
   驱动的 omp 会话）直接读 AGENTS.md schema 干活。本机 GitHub 443 不通、
   不想装一堆 python 包，这是唯一"读 README 就能跑"的。
2. **schema 即文档**：AGENTS.md 把 ingest/query/lint/health/graph 工作流、
   页面格式、命名规范全写成可执行的 agent 指令，本身是"agent 维护知识库"
   的范本。
3. **MIT 许可**，可魔改（对比 open-knowledge 的 GPL v3，分发有约束）。
4. **health.py 是确定性脚本**（零 LLM 调用）：即使模型质量一般，结构完整性
   检查（空页/索引同步/log 覆盖）照样可用。

放弃的其他选项：
- open-knowledge：产品最完整，但 GPL v3 + 要装 Node24 运行时，作为"试用"
  太重；适合后续当主力 App 再评估。
- obsidian-llm-wiki-local：最贴"本地 Ollama + 离线"诉求，但已转维护模式、
  要 pip 一堆依赖、默认 7B+ 模型才好用；其设计里"拒绝反馈"和"手改保护"
  两个特性值得借鉴。

## 本机实跑结论（2026-09-03）

在 `llm-wiki-agent/` 目录用 omp 本地模型（qwen3.8-q5-262k）完整跑通
ingest → query → lint → graph 全流程，13 页 wiki + 13 节点 65 边图谱：

- **真正能本地可靠运行的层**：schema + health.py（纯 Python，模型无关）
- **依赖模型质量的层**：ingest 的判断（建哪些页、抓哪条矛盾）、query 综合、
  语义 lint。本地 Q5 量化能跑通流程，但页面质量天花板受模型限制
- **抓到的真实价值**：ingest 时显式标记矛盾（"复利 vs 负债"）、lint 抓出
  孤儿页和 `[[wikilink]]` 字面量假断链——这两点证明了"编译式维护"相对
  "检索式"的结构性优势不是空话
- **本机跑该项目的已知坑**：
  1. git clone 443 不通 → 用 raw.githubusercontent.com 逐文件还原
  2. build_graph.py 的 Pass-2（语义推断）要 litellm + API → 离线环境跳过，
     只用 Pass-1（确定性 wikilink 解析）就够出图
  3. lint.py 的语义部分同样要 API → 离线 lint 只保留确定性部分
     （孤儿/断链/稀疏页/缺实体页）+ agent 自己写语义报告
  4. 正文里出现 `[[wikilink]]` 这种字面示例会被解析器当真断链——写 wiki
     页时示例要避开双中括号字面量
- **建议的落地路径**：先用 llm-wiki-agent 的 schema + 本地模型跑日常 ingest，
  质量不够的地方（语义 lint、复杂综合）等 vision/更强模型就绪后再上
  obsidian-llm-wiki-local 或 open-knowledge 补强
