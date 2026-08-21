"""hexa gemini — configure Gemini CLI to consume the Hexawyn MCP server."""

from __future__ import annotations

from hexawyn.cli.commands.mcp_client_group import build_mcp_client_group

gemini = build_mcp_client_group(client="gemini", display_name="Gemini CLI")
