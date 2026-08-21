"""Shared base for CLI-driven MCP client integrations.

Clients such as Claude Code and Codex configure MCP servers through their own
CLI (`<client> mcp add / get|list / remove`). This base implements the
idempotent install / safe uninstall / status lifecycle, leaving each client to
provide its binary, display name, state probe and add/remove commands.
"""

from __future__ import annotations

import shutil
from abc import abstractmethod
from dataclasses import dataclass

from hexawyn.cli.integrations.mcp.base import (
    MCP_TRANSPORT,
    CommandResult,
    CommandRunner,
    IntegrationResult,
    IntegrationStatus,
    MCPClientIntegration,
    SubprocessRunner,
)


@dataclass(frozen=True)
class CliIntegrationStatus:
    configured: bool
    error: str = ""
    transport: str = MCP_TRANSPORT
    endpoint: str = ""
    command: str = ""


class CliMcpIntegration(MCPClientIntegration):
    """Base for coding agents configured through their own MCP CLI."""

    binary: str = ""
    display_name: str = ""

    def __init__(self, runner: CommandRunner | None = None) -> None:
        self._runner = runner if runner is not None else SubprocessRunner()

    def is_available(self) -> bool:
        return shutil.which(self.binary) is not None

    def is_installed(self) -> bool:
        return self._read_status().configured

    def install(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if status.configured:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        result = self._runner.run(self._add_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp add", result)
            )
        verified = self._read_status()
        if verified.error or not verified.configured:
            detail = verified.error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def uninstall(self) -> IntegrationResult:
        status = self._read_status()
        if status.error:
            return IntegrationResult(success=False, message=status.error)
        if not status.configured:
            return IntegrationResult(success=True, message="not configured")
        result = self._runner.run(self._remove_command())
        if result.returncode != 0:
            return IntegrationResult(
                success=False, message=_failure(f"{self.binary} mcp remove", result)
            )
        remaining = self._read_status()
        if remaining.configured:
            return IntegrationResult(success=False, message="hexawyn still present after removal")
        return IntegrationResult(success=True, message="removed")

    def status(self) -> IntegrationStatus:
        status = self._read_status()
        return IntegrationStatus(
            configured=status.configured,
            transport=status.transport,
            endpoint=status.endpoint,
            command=status.command,
            error=status.error or None,
        )

    @abstractmethod
    def _read_status(self) -> CliIntegrationStatus:
        """Return the client's MCP state for the hexawyn server."""

    @abstractmethod
    def _add_command(self) -> list[str]:
        """Return the CLI command that registers the hexawyn MCP server."""

    @abstractmethod
    def _remove_command(self) -> list[str]:
        """Return the CLI command that removes the hexawyn MCP server."""


def _failure(operation: str, result: CommandResult) -> str:
    return f"{operation} failed: {_error_text(result)}"


def _error_text(result: CommandResult) -> str:
    return result.stderr.strip() or result.stdout.strip() or "unknown error"
