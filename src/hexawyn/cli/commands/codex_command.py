"""hexa codex — configure Codex to consume the Hexawyn MCP server."""

from __future__ import annotations

from hexawyn.cli.commands.mcp_client_group import build_mcp_client_group

codex = build_mcp_client_group(client="codex", display_name="Codex")
