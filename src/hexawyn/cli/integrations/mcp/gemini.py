"""Gemini CLI MCP integration — configures ~/.gemini/settings.json `mcpServers`.

Gemini CLI configures MCP servers in `~/.gemini/settings.json` under the
`mcpServers` key. This integration edits only the hexawyn entry and preserves
every other server.
"""

from __future__ import annotations

from pathlib import Path

from hexawyn.cli.integrations.mcp.command import mcp_stdio_command
from hexawyn.cli.integrations.mcp.file import McpConfigFileIntegration

GEMINI_BINARY = "gemini"
GEMINI_DISPLAY_NAME = "Gemini CLI"


class GeminiIntegration(McpConfigFileIntegration):
    client_name = "gemini"
    binary = GEMINI_BINARY
    display_name = GEMINI_DISPLAY_NAME
    default_config_path = Path.home() / ".gemini" / "settings.json"

    def __init__(self, config_path: Path | None = None) -> None:
        super().__init__(config_path or self.default_config_path)

    def _config_root_key(self) -> str:
        return "mcpServers"

    def _build_entry(self) -> dict[str, object]:
        return {"command": mcp_stdio_command()[0], "args": mcp_stdio_command()[1:]}
