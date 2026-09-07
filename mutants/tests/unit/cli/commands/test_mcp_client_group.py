from __future__ import annotations

import sys
from unittest.mock import MagicMock, patch

from click.testing import CliRunner
from hexawyn.cli.commands.mcp_client_group import build_mcp_client_group
from hexawyn.cli.integrations.mcp.base import (
    IntegrationResult,
    IntegrationStatus,
)

_COMMAND_TEXT = f"Command: {sys.executable} -m hexawyn.mcp.stdio"


def _mock_integration(
    *,
    available: bool = True,
    install_result: IntegrationResult | None = None,
    uninstall_result: IntegrationResult | None = None,
    status: IntegrationStatus | None = None,
) -> MagicMock:
    integration = MagicMock()
    integration.is_available.return_value = available
    integration.install.return_value = install_result or IntegrationResult(
        success=True, message="configured"
    )
    integration.uninstall.return_value = uninstall_result or IntegrationResult(
        success=True, message="removed"
    )
    integration.status.return_value = status or IntegrationStatus(configured=False)
    return integration


class TestBuildMcpClientGroup:
    def test_group_has_install_uninstall_status(self) -> None:
        group = build_mcp_client_group(client="codex", display_name="Codex")
        names = [cmd.name for cmd in group.commands.values()]
        assert "install" in names
        assert "uninstall" in names
        assert "status" in names

    def test_group_help_mentions_client(self) -> None:
        group = build_mcp_client_group(client="codex", display_name="Codex")
        runner = CliRunner()
        result = runner.invoke(group, ["--help"])
        assert "Codex" in result.output

    def test_install_success(self) -> None:
        group = build_mcp_client_group(client="codex", display_name="Codex")
        integration = _mock_integration(
            install_result=IntegrationResult(success=True, message="configured")
        )
        with patch(
            "hexawyn.cli.commands.mcp_client_group.get_integration",
            return_value=integration,
        ):
            result = CliRunner().invoke(group, ["install"])

        assert result.exit_code == 0
        assert "Codex detected" in result.output
        assert "Hexawyn MCP configured" in result.output
        assert "Configuration verified" in result.output
        assert _COMMAND_TEXT in result.output

    def test_install_already_configured(self) -> None:
        group = build_mcp_client_group(client="codex", display_name="Codex")
        integration = _mock_integration(
            install_result=IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        )
        with patch(
            "hexawyn.cli.commands.mcp_client_group.get_integration",
            return_value=integration,
        ):
            result = CliRunner().invoke(group, ["install"])

        assert result.exit_code == 0
        assert "already configured" in result.output

    def test_install_client_not_detected(self) -> None:
        group = build_mcp_client_group(client="codex", display_name="Codex")
        integration = _mock_integration(available=False)
        with patch(
            "hexawyn.cli.commands.mcp_client_group.get_integration",
            return_value=integration,
        ):
            result = CliRunner().invoke(group, ["install"])

        assert result.exit_code == 1
        assert "Codex not detected" in result.output

    def test_install_failure(self) -> None:
        group = build_mcp_client_group(client="codex", display_name="Codex")
        integration = _mock_integration(
            install_result=IntegrationResult(success=False, message="boom")
        )
        with patch(
            "hexawyn.cli.commands.mcp_client_group.get_integration",
            return_value=integration,
        ):
            result = CliRunner().invoke(group, ["install"])

        assert result.exit_code == 1
        assert "boom" in result.output

    def test_uninstall_success(self) -> None:
        group = build_mcp_client_group(client="codex", display_name="Codex")
        integration = _mock_integration(
            uninstall_result=IntegrationResult(success=True, message="removed")
        )
        with patch(
            "hexawyn.cli.commands.mcp_client_group.get_integration",
            return_value=integration,
        ):
            result = CliRunner().invoke(group, ["uninstall"])

        assert result.exit_code == 0
        assert "removed from Codex" in result.output

    def test_uninstall_not_configured(self) -> None:
        group = build_mcp_client_group(client="codex", display_name="Codex")
        integration = _mock_integration(
            uninstall_result=IntegrationResult(success=True, message="not configured")
        )
        with patch(
            "hexawyn.cli.commands.mcp_client_group.get_integration",
            return_value=integration,
        ):
            result = CliRunner().invoke(group, ["uninstall"])

        assert result.exit_code == 0
        assert "nothing to remove" in result.output

    def test_uninstall_failure(self) -> None:
        group = build_mcp_client_group(client="codex", display_name="Codex")
        integration = _mock_integration(
            uninstall_result=IntegrationResult(success=False, message="boom")
        )
        with patch(
            "hexawyn.cli.commands.mcp_client_group.get_integration",
            return_value=integration,
        ):
            result = CliRunner().invoke(group, ["uninstall"])

        assert result.exit_code == 1
        assert "boom" in result.output

    def test_status_configured(self) -> None:
        group = build_mcp_client_group(client="codex", display_name="Codex")
        integration = _mock_integration(
            status=IntegrationStatus(
                configured=True,
                command=f"{sys.executable} -m hexawyn.mcp.stdio",
            )
        )
        with patch(
            "hexawyn.cli.commands.mcp_client_group.get_integration",
            return_value=integration,
        ):
            result = CliRunner().invoke(group, ["status"])

        assert result.exit_code == 0
        assert "Status: ✓ Configured" in result.output
        assert "hexa codex install" not in result.output

    def test_status_not_configured(self) -> None:
        group = build_mcp_client_group(client="codex", display_name="Codex")
        integration = _mock_integration(status=IntegrationStatus(configured=False))
        with patch(
            "hexawyn.cli.commands.mcp_client_group.get_integration",
            return_value=integration,
        ):
            result = CliRunner().invoke(group, ["status"])

        assert result.exit_code == 0
        assert "Status: ✗ Not configured" in result.output
        assert "hexa codex install" in result.output

    def test_status_configured_with_endpoint(self) -> None:
        group = build_mcp_client_group(client="codex", display_name="Codex")
        integration = _mock_integration(
            status=IntegrationStatus(
                configured=True,
                transport="http",
                endpoint="http://localhost:8000/mcp",
                command=f"{sys.executable} -m hexawyn.mcp.stdio",
            )
        )
        with patch(
            "hexawyn.cli.commands.mcp_client_group.get_integration",
            return_value=integration,
        ):
            result = CliRunner().invoke(group, ["status"])

        assert result.exit_code == 0
        assert "Status: ✓ Configured" in result.output
        assert "Endpoint: http://localhost:8000/mcp" in result.output

    def test_status_error(self) -> None:
        group = build_mcp_client_group(client="codex", display_name="Codex")
        integration = _mock_integration(
            status=IntegrationStatus(configured=False, error="codex mcp list failed")
        )
        with patch(
            "hexawyn.cli.commands.mcp_client_group.get_integration",
            return_value=integration,
        ):
            result = CliRunner().invoke(group, ["status"])

        assert result.exit_code == 1
        assert "codex mcp list failed" in result.output
