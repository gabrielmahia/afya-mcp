# afya-mcp

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