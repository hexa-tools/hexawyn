"""MCP client integration abstraction — external coding agent configuration.

Each integration configures an external coding agent (Claude Code, OpenCode,
...) to consume the existing Hexawyn MCP server. This lives outside the
Hexawyn diagnostic core: integrations only translate MCP client configuration
into external CLI calls, keeping the diagnostic engine decoupled from any
coding agent.
"""

from __future__ import annotations

import subprocess
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Protocol

MCP_SERVER_NAME = "hexawyn"
MCP_TRANSPORT = "stdio"


@dataclass(frozen=True)
class CommandResult:
    returncode: int
    stdout: str
    stderr: str = ""


class CommandRunner(Protocol):
    def run(self, command: list[str]) -> CommandResult:
        """Execute a command and return its captured result."""


class SubprocessRunner:
    """CommandRunner implementation backed by subprocess."""

    def run(self, command: list[str]) -> CommandResult:
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=30)
        except FileNotFoundError as exc:
            return CommandResult(returncode=127, stdout="", stderr=str(exc))
        except subprocess.TimeoutExpired as exc:
            return CommandResult(returncode=124, stdout="", stderr=str(exc))
        return CommandResult(returncode=proc.returncode, stdout=proc.stdout, stderr=proc.stderr)


@dataclass(frozen=True)
class IntegrationStatus:
    configured: bool
    transport: str = MCP_TRANSPORT
    endpoint: str = ""
    command: str = ""
    error: str | None = None


@dataclass(frozen=True)
class IntegrationResult:
    success: bool
    message: str
    already_configured: bool = False


class MCPClientIntegration(ABC):
    """Configure an external coding agent to consume the Hexawyn MCP server."""

    client_name: str = ""

    @abstractmethod
    def is_available(self) -> bool:
        """Return whether the client binary is installed."""

    @abstractmethod
    def is_installed(self) -> bool:
        """Return whether the hexawyn MCP server is already configured."""

    @abstractmethod
    def install(self) -> IntegrationResult:
        """Configure the hexawyn MCP server for the client (idempotent)."""

    @abstractmethod
    def uninstall(self) -> IntegrationResult:
        """Remove only the hexawyn MCP server for the client."""

    @abstractmethod
    def status(self) -> IntegrationStatus:
        """Report whether the hexawyn MCP server is configured for the client."""
