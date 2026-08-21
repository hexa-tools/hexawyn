"""OpenCode MCP integration — configures the opencode.json `mcp` section.

OpenCode does not expose an `mcp add` CLI for local servers; local MCP servers
are declared in the config file under the `mcp` key. This integration edits
only the hexawyn entry and preserves every other server.
"""

from __future__ import annotations

from pathlib import Path

from hexawyn.cli.integrations.mcp.command import mcp_stdio_command
from hexawyn.cli.integrations.mcp.file import McpConfigFileIntegration

OPENCODE_BINARY = "opencode"
OPENCODE_DISPLAY_NAME = "OpenCode"


class OpenCodeIntegration(McpConfigFileIntegration):
    client_name = "opencode"
    binary = OPENCODE_BINARY
    display_name = OPENCODE_DISPLAY_NAME
    default_config_path = Path.home() / ".config" / "opencode" / "opencode.json"

    def __init__(self, config_path: Path | None = None) -> None:
        super().__init__(config_path or self.default_config_path)

    def _config_root_key(self) -> str:
        return "mcp"

    def _build_entry(self) -> dict[str, object]:
        return {"type": "local", "command": mcp_stdio_command()}
