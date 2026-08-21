"""hexa opencode — configure OpenCode to consume the Hexawyn MCP server."""

from __future__ import annotations

from hexawyn.cli.commands.mcp_client_group import build_mcp_client_group

opencode = build_mcp_client_group(client="opencode", display_name="OpenCode")
