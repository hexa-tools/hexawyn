"""Claude Code MCP integration — uses the official `claude mcp` CLI.

Configures Claude Code to consume the existing Hexawyn MCP server over the
stdio transport through the documented `claude mcp add / get / remove`
mechanism. Claude Code spawns the server per session, so no separate HTTP
server needs to run.
"""

from __future__ import annotations

from hexawyn.cli.integrations.mcp.base import MCP_SERVER_NAME, MCP_TRANSPORT
from hexawyn.cli.integrations.mcp.cli_mcp import (
    CliIntegrationStatus,
    CliMcpIntegration,
    _error_text,
)
from hexawyn.cli.integrations.mcp.command import mcp_stdio_command

CLAUDE_BINARY = "claude"
CLAUDE_DISPLAY_NAME = "Claude Code"
_NOT_CONFIGURED_MARKER = "No MCP server named"


class ClaudeCodeIntegration(CliMcpIntegration):
    client_name = "claude"
    binary = CLAUDE_BINARY
    display_name = CLAUDE_DISPLAY_NAME

    def _read_status(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "get", MCP_SERVER_NAME])
        # `claude mcp get` exits 0 even when the server is missing, so the
        # "not found" marker must be honoured before trusting the exit code —
        # otherwise install() reports a false "already configured".
        combined = f"{result.stdout}\n{result.stderr}"
        if _NOT_CONFIGURED_MARKER in combined:
            return CliIntegrationStatus(configured=False)
        if result.returncode == 0:
            entry = _parse_entry(result.stdout)
            transport = str(entry.get("type", MCP_TRANSPORT)) or MCP_TRANSPORT
            return CliIntegrationStatus(
                configured=True,
                transport=transport,
                endpoint=str(entry.get("url", "") or ""),
                command=_command_string(entry),
            )
        return CliIntegrationStatus(configured=False, error=_error_text(result))

    def _add_command(self) -> list[str]:
        return [self.binary, "mcp", "add", MCP_SERVER_NAME, "--", *mcp_stdio_command()]

    def _remove_command(self) -> list[str]:
        return [self.binary, "mcp", "remove", MCP_SERVER_NAME]


def _parse_entry(text: str) -> dict[str, object]:
    entry: dict[str, object] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("Type:"):
            entry["type"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("URL:"):
            entry["url"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Command:"):
            entry["command"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Args:"):
            entry["args"] = stripped.split(":", 1)[1].strip()
    return entry


def _command_string(entry: dict[str, object]) -> str:
    command = str(entry.get("command", "") or "")
    args = str(entry.get("args", "") or "")
    if command and args:
        return f"{command} {args}"
    return command
