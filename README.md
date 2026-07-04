# afya-mcp
<!-- mcp-name: io.github.gabrielmahia/afya-mcp -->

[![afya-mcp Glama score](https://glama.ai/mcp/servers/gabrielmahia/afya-mcp/badges/score.svg)](https://glama.ai/mcp/servers/gabrielmahia/afya-mcp)
[![smithery badge](https://smithery.ai/badge/@gabrielmahia/afya-mcp)](https://smithery.ai/server/@gabrielmahia/afya-mcp)


---
**Compatible with `claude-sonnet-5`** (released 2026-06-30) — Anthropic's most agentic
Sonnet yet. Runs multi-step tool chains end-to-end without stopping short.
Install: `pip install afya-mcp` · Use with any MCP client.

---

MCP server for Kenya health system navigation — NHIF coverage, facility finder, maternal health, CHW support, and essential medicines. 6 tools.

## Part of the East Africa Coordination Stack

This MCP server is one of 32 tools in the Kenya coordination infrastructure.
It connects to [`africa-coord-bus`](https://github.com/gabrielmahia/africa-coord-bus) — the coordination
event bus that routes signals between domains automatically.

When this server detects a threshold condition, the bus notifies:
- `bima-mcp` — parametric insurance evaluation
- `kilimo-mcp` — agricultural advisory
- `afya-mcp` — health surveillance activation
- `county-mcp` — county office alert

```python
pip install africa-coord-bus
```

All servers: [pypi.org/user/gmahia](https://pypi.org/user/gmahia/)
## AI Architecture: Health Domain RAG

Medical AI requires grounding — ungrounded responses in health contexts cause real harm.
Use this server as a **RAG entry point**, not a standalone health oracle.

**Research basis:**
- *RAG Best Practices for Medical Domain* (2026): RAG outperforms chain-of-thought
  on complex medical reasoning and is more interpretable — critical in clinical contexts.
- *AfricaNLP 2025/2026*: Only 4 African languages (incl. Swahili) have consistent
  NLP support. Healthcare is identified as the highest-priority domain needing
  accurate, grounded AI — and the one with the most critical data gaps.
- *Multilingual NLP for African Healthcare* (AfricaNLP 2025): Bias and translation
  errors persist specifically in African health AI contexts.

**Appropriate use:**
✅ Health facility navigation, NHIF coverage lookup, community health worker support  
✅ Health information grounded in verified Kenya health system data  
✅ Triage to appropriate care level  
❌ Diagnosis, prescription, or clinical decision-making (human-in-the-loop required)

## IP & Collaboration

MIT licensed. Feedback via GitHub Issues only — pull requests are not accepted. Demo data is labeled DEMO and is not suitable for operational decisions. Full policy: [docs/architecture/IP_POLICY.md](docs/architecture/IP_POLICY.md). Security reports: see [SECURITY.md](SECURITY.md).
