"""Cursor MCP integration — configures ~/.cursor/mcp.json `mcpServers`.

Cursor configures MCP servers through the `mcp.json` file (global or project);
there is no `cursor mcp` CLI. This integration edits only the hexawyn entry
and preserves every other server.
"""

from __future__ import annotations

from pathlib import Path

from hexawyn.cli.integrations.mcp.command import mcp_stdio_command
from hexawyn.cli.integrations.mcp.file import McpConfigFileIntegration

CURSOR_BINARY = "cursor"
CURSOR_DISPLAY_NAME = "Cursor"


class CursorIntegration(McpConfigFileIntegration):
    client_name = "cursor"
    binary = CURSOR_BINARY
    display_name = CURSOR_DISPLAY_NAME
    default_config_path = Path.home() / ".cursor" / "mcp.json"

    def __init__(self, config_path: Path | None = None) -> None:
        super().__init__(config_path or self.default_config_path)

    def _config_root_key(self) -> str:
        return "mcpServers"

    def _build_entry(self) -> dict[str, object]:
        return {"command": mcp_stdio_command()[0], "args": mcp_stdio_command()[1:]}
