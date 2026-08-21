"""Codex MCP integration — uses the official `codex mcp` CLI.

Configures Codex to consume the existing Hexawyn MCP server over the stdio
transport through the documented `codex mcp add / list / remove` mechanism.
"""

from __future__ import annotations

from hexawyn.cli.integrations.mcp.base import MCP_SERVER_NAME
from hexawyn.cli.integrations.mcp.cli_mcp import (
    CliIntegrationStatus,
    CliMcpIntegration,
    _error_text,
)
from hexawyn.cli.integrations.mcp.command import mcp_stdio_command

CODEX_BINARY = "codex"
CODEX_DISPLAY_NAME = "Codex"


class CodexIntegration(CliMcpIntegration):
    client_name = "codex"
    binary = CODEX_BINARY
    display_name = CODEX_DISPLAY_NAME

    def _read_status(self) -> CliIntegrationStatus:
        if not self.is_available():
            return CliIntegrationStatus(
                configured=False, error=f"{self.display_name} not found on PATH"
            )
        result = self._runner.run([self.binary, "mcp", "list"])
        if result.returncode != 0:
            return CliIntegrationStatus(configured=False, error=_error_text(result))
        configured = MCP_SERVER_NAME in result.stdout.lower()
        return CliIntegrationStatus(
            configured=configured,
            command=" ".join(mcp_stdio_command()) if configured else "",
        )

    def _add_command(self) -> list[str]:
        return [self.binary, "mcp", "add", MCP_SERVER_NAME, "--", *mcp_stdio_command()]

    def _remove_command(self) -> list[str]:
        return [self.binary, "mcp", "remove", MCP_SERVER_NAME]
