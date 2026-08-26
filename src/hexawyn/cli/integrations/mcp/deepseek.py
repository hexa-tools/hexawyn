"""DeepSeek Harness MCP integration — writes a Cordis composition overlay.

DeepSeek Harness (dsh) enables MCP servers via Cordis patch overlays
(``*.cordis.yml``) provided by ``@deepseek-ai/dsh-mcp-client``; no server is
enabled by default. This integration writes a standalone overlay that registers
the Hexawyn MCP server over stdio.
"""

from __future__ import annotations

from pathlib import Path

import yaml
from hexawyn.cli.integrations.mcp.base import (
    MCP_SERVER_NAME,
    MCP_TRANSPORT,
    IntegrationResult,
    IntegrationStatus,
    MCPClientIntegration,
)
from hexawyn.cli.integrations.mcp.command import mcp_stdio_command

DEEPSEEK_BINARY = "dsh"
DEEPSEEK_DISPLAY_NAME = "DeepSeek Harness"
_MCP_CLIENT_PLUGIN = "@deepseek-ai/dsh-mcp-client"


class DeepSeekHarnessIntegration(MCPClientIntegration):
    """Configure DeepSeek Harness to consume the Hexawyn MCP server."""

    client_name = "deepseek"
    binary = DEEPSEEK_BINARY
    display_name = DEEPSEEK_DISPLAY_NAME
    default_config_path = (
        Path.home() / ".config" / "deepseek-harness" / f"{MCP_SERVER_NAME}.cordis.yml"
    )

    def __init__(self, config_path: Path | None = None) -> None:
        self._config_path = config_path or self.default_config_path

    def is_available(self) -> bool:
        # This integration only writes a Cordis overlay — it never needs the
        # dsh binary on PATH to be useful, so it is always available.
        return True

    def is_installed(self) -> bool:
        return self._config_path.exists()

    def install(self) -> IntegrationResult:
        if not self.is_available():
            return IntegrationResult(
                success=False, message=f"{self.display_name} not found on PATH"
            )
        if self.is_installed():
            return IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        self._write_overlay()
        if self.is_installed():
            return IntegrationResult(success=True, message="configured")
        return IntegrationResult(success=False, message="configuration could not be verified")

    def uninstall(self) -> IntegrationResult:
        if not self._config_path.exists():
            return IntegrationResult(success=True, message="not configured")
        self._config_path.unlink()
        return IntegrationResult(success=True, message="removed")

    def status(self) -> IntegrationStatus:
        command = " ".join(mcp_stdio_command())
        if not self.is_available():
            return IntegrationStatus(
                configured=False,
                command=command,
                error=f"{self.display_name} not found on PATH",
            )
        if not self.is_installed():
            return IntegrationStatus(configured=False, command=command)
        return IntegrationStatus(configured=True, transport=MCP_TRANSPORT, command=command)

    def _write_overlay(self) -> None:
        self._config_path.parent.mkdir(parents=True, exist_ok=True)
        self._config_path.write_text(self._build_overlay(), encoding="utf-8")

    def _build_overlay(self) -> str:
        command_args = mcp_stdio_command()
        overlay = [
            {
                "insert": [
                    {
                        "id": MCP_SERVER_NAME,
                        "name": _MCP_CLIENT_PLUGIN,
                        "config": {
                            "serverName": MCP_SERVER_NAME,
                            "transport": MCP_TRANSPORT,
                            "command": command_args[0],
                            "args": command_args[1:],
                        },
                    }
                ]
            }
        ]
        return yaml.safe_dump(overlay, sort_keys=False)
