#!/usr/bin/env python3
from __future__ import annotations
"""
Agent-executed graph builder for this offline demo.

Reimplements the Pass-1 (deterministic EXTRACTED) layer of the repo's
tools/build_graph.py so the demo runs with zero LLM / zero extra deps.
Pass-2 (semantic INFERRED inference) is done by the agent, not a script.

Meta files are excluded to match the repo convention (tools/_utils.py
_META_EXCLUDE + health-report.md).
"""
import re
import json
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
WIKI_DIR = REPO_ROOT / "wiki"
GRAPH_DIR = REPO_ROOT / "graph"

TYPE_COLORS = {"source": "#4CAF50", "entity": "#2196F3",
               "concept": "#FF9800", "synthesis": "#9C27B0", "unknown": "#9E9E9E"}

_META_EXCLUDE = {"index.md", "log.md", "lint-report.md", "health-report.md"}


def type_of(content: str) -> str:
    m = re.search(r"^type:\s*(\S+)", content, re.MULTILINE)
    return m.group(1).strip("\"'") if m else "unknown"


def title_of(content: str, fallback: str) -> str:
    m = re.search(r'^title:\s*"?([^"\n]+)"?', content, re.MULTILINE)
    return m.group(1).strip() if m else fallback


pages = [p for p in WIKI_DIR.rglob("*.md") if p.name not in _META_EXCLUDE]

nodes, stem_map = [], {}
for p in pages:
    c = p.read_text(encoding="utf-8")
    pid = p.relative_to(WIKI_DIR).as_posix().replace(".md", "")
    stem_map[p.stem.lower()] = pid
    nodes.append({"id": pid, "label": title_of(c, p.stem),
                  "type": type_of(c), "color": TYPE_COLORS.get(type_of(c), "#9E9E9E")})

edges, seen, broken = [], set(), {}
for p in pages:
    src = p.relative_to(WIKI_DIR).as_posix().replace(".md", "")
    for link in re.findall(r"\[\[([^\]]+)\]\]", p.read_text(encoding="utf-8")):
        tgt = stem_map.get(link.lower())
        if tgt and tgt != src and (src, tgt) not in seen:
            seen.add((src, tgt))
            edges.append({"from": src, "to": tgt, "type": "EXTRACTED"})
        elif not tgt:
            broken[link] = broken.get(link, 0) + 1

GRAPH_DIR.mkdir(parents=True, exist_ok=True)
graph = {"nodes": nodes, "edges": edges, "built": "2026-09-03"}
(GRAPH_DIR / "graph.json").write_text(
    json.dumps(graph, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"nodes: {len(nodes)}  extracted_edges: {len(edges)}")
print("broken_links:")
for k, v in sorted(broken.items(), key=lambda x: -x[1]):
    print(f"  [[{k}]] x{v}")
