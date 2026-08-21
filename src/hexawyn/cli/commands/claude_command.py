"""hexa claude — configure Claude Code to consume the Hexawyn MCP server.

Thin CLI adapter: delegates to the shared MCP client group builder. No Claude
subprocess, config parsing or endpoint logic lives here.
"""

from __future__ import annotations

from hexawyn.cli.commands.mcp_client_group import build_mcp_client_group

claude = build_mcp_client_group(client="claude", display_name="Claude Code")
