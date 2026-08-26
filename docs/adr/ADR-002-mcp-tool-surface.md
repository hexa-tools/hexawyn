# ADR-002 — MCP / FastMCP as the agent surface

**Date** : 2026-08-25 · **Status** : `accepted`

## Context

Users drive hexawyn through *coding agents* (Claude, Codex, Gemini, Cursor,
OpenCode). Historically each agent had its own integration, so every new
agent required dedicated code and capabilities were not reusable across
agents.

## Decision

Expose all of hexawyn's capabilities as one **MCP (Model Context Protocol)
server** via **FastMCP**:

- `mcp/server.py` — composition root: `build_*_adapter()` + `register_tools()`
  (auto-discovery of `mcp/tools/`).
- `mcp/stdio.py` — stdio transport for agents that spawn the server
  (`python -m hexawyn.mcp.stdio`).
- `mcp/tools/` — ~158 tools, one file per use case.
- **Descriptions sourced from `datasets/intent_examples.yaml`**
  (`build_tool_descriptions()`), enriched with 3–5 example queries
  (`build_enriched_tool_descriptions()`) to guide the model's tool selection.
- `mcp-inspector` (Makefile) to browse/test the tools in a browser.

The model receives the `name` + `description` + `inputSchema` trio via
`tools/list`.

## Alternatives considered

- **A Textual CLI only** — rejected: not consumable by a coding agent.
- **A dedicated SDK per agent** — rejected: duplicates the surface,
  maintenance cost per agent.
- **SSE/HTTP only** — rejected: many agents prefer stdio; we keep both
  (`server.py` HTTP + `stdio.py`).

## Consequences

- Any new capability = one file in `mcp/tools/` (exposed to all agents at
  once).
- **Forbidden**: writing an agent-by-agent integration (cf. ADR-001, we
  consume the MCP ports).
- The quality of `description` + `examples` directly affects the LLM's tool
  selection → docs are a first-class citizen.
- Reversible: the MCP transport can evolve without touching the core.
