"""hexa cursor — configure Cursor to consume the Hexawyn MCP server."""

from __future__ import annotations

from hexawyn.cli.commands.mcp_client_group import build_mcp_client_group

cursor = build_mcp_client_group(client="cursor", display_name="Cursor")
