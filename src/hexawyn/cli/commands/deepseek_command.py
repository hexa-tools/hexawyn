"""hexa deepseek — configure DeepSeek Harness to consume the Hexawyn MCP server."""

from __future__ import annotations

from hexawyn.cli.commands.mcp_client_group import build_mcp_client_group

deepseek = build_mcp_client_group(client="deepseek", display_name="DeepSeek Harness")
