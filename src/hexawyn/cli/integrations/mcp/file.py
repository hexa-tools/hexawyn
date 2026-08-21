"""Base for config-file-driven MCP client integrations.

Clients such as OpenCode, Cursor and Gemini CLI configure MCP servers through
a JSON configuration file rather than an MCP CLI. These integrations edit only
the hexawyn entry under the client's config root key and preserve every other
server.
"""

from __future__ import annotations

import json
import shutil
from abc import abstractmethod
from pathlib import Path

from hexawyn.cli.integrations.mcp.base import (
    MCP_SERVER_NAME,
    MCP_TRANSPORT,
    IntegrationResult,
    IntegrationStatus,
    MCPClientIntegration,
)
from hexawyn.cli.integrations.mcp.command import mcp_stdio_command


class McpConfigFileIntegration(MCPClientIntegration):
    """Base for coding agents configured through a JSON config file."""

    binary: str = ""
    display_name: str = ""

    def __init__(self, config_path: Path) -> None:
        self._config_path = config_path

    def is_available(self) -> bool:
        return shutil.which(self.binary) is not None or self._config_path.parent.exists()

    def is_installed(self) -> bool:
        status = self.status()
        return status.configured

    def install(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME in servers:
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        servers[MCP_SERVER_NAME] = self._build_entry()
        self._write_config(config)
        verified, verify_error = self._read_config()
        if verified is None or MCP_SERVER_NAME not in self._servers(verified):
            detail = verify_error or "configuration could not be verified after install"
            return IntegrationResult(success=False, message=detail)
        return IntegrationResult(success=True, message="configured")

    def uninstall(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationResult(success=False, message=error)
        servers = self._servers(config)
        if MCP_SERVER_NAME not in servers:
            return IntegrationResult(success=True, message="not configured")
        del servers[MCP_SERVER_NAME]
        self._write_config(config)
        return IntegrationResult(success=True, message="removed")

    def status(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        config, error = self._read_config()
        if config is None:
            return IntegrationStatus(configured=False, command=command, error=error)
        if MCP_SERVER_NAME not in self._servers(config):
            return IntegrationStatus(configured=False, command=command)
        return IntegrationStatus(configured=True, transport=MCP_TRANSPORT, command=command)

    def _read_config(self) -> tuple[dict[str, object] | None, str]:
        if not self._config_path.exists():
            return {}, ""
        try:
            data = json.loads(self._config_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            return None, f"{self.display_name} config is not valid JSON: {exc}"
        except OSError as exc:
            return None, f"cannot read {self._config_path}: {exc}"
        if not isinstance(data, dict):
            return None, f"{self.display_name} config is not a JSON object"
        return data, ""

    def _write_config(self, config: dict[str, object]) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        self._config_path.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")

    def _servers(self, config: dict[str, object]) -> dict[str, object]:
        root = config.get(self._config_root_key())
        if not isinstance(root, dict):
            root = {}
            config[self._config_root_key()] = root
        return root

    @abstractmethod
    def _config_root_key(self) -> str:
        """Return the top-level key holding the MCP servers map."""

    @abstractmethod
    def _build_entry(self) -> dict[str, object]:
        """Return the config entry for the hexawyn MCP server."""
