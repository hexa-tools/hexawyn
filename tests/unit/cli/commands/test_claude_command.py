from __future__ import annotations

from unittest.mock import MagicMock, patch

from click.testing import CliRunner
from hexawyn.cli.commands.claude_command import claude
from hexawyn.cli.integrations.mcp.base import (
    IntegrationResult,
    IntegrationStatus,
)


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


class TestClaudeCommandRegistration:
    def test_group_exposes_install_uninstall_status(self) -> None:
        names = [cmd.name for cmd in claude.commands.values()]
        assert "install" in names
        assert "uninstall" in names
        assert "status" in names


class TestClaudeInstallCommand:
    def test_install_success(self) -> None:
        runner = CliRunner()
        integration = _mock_integration(
            install_result=IntegrationResult(success=True, message="configured")
        )
        with patch(
            "hexawyn.cli.commands.mcp_client_group.get_integration",
            return_value=integration,
        ):
            result = runner.invoke(claude, ["install"])

        assert result.exit_code == 0
        assert "Claude Code detected" in result.output
        assert "Hexawyn MCP configured" in result.output
        assert "Configuration verified" in result.output
        assert "Server: hexawyn" in result.output
        assert "Transport: stdio" in result.output
        assert "Command: python -m hexawyn.mcp.stdio" in result.output

    def test_install_already_configured(self) -> None:
        runner = CliRunner()
        integration = _mock_integration(
            install_result=IntegrationResult(
                success=True, message="already configured", already_configured=True
            )
        )
        with patch(
            "hexawyn.cli.commands.mcp_client_group.get_integration",
            return_value=integration,
        ):
            result = runner.invoke(claude, ["install"])

        assert result.exit_code == 0
        assert "Hexawyn MCP already configured" in result.output
        assert "Configuration verified" in result.output

    def test_install_client_not_detected(self) -> None:
        runner = CliRunner()
        integration = _mock_integration(available=False)
        with patch(
            "hexawyn.cli.commands.mcp_client_group.get_integration",
            return_value=integration,
        ):
            result = runner.invoke(claude, ["install"])

        assert result.exit_code == 1
        assert "Claude Code not detected" in result.output

    def test_install_failure(self) -> None:
        runner = CliRunner()
        integration = _mock_integration(
            install_result=IntegrationResult(success=False, message="boom")
        )
        with patch(
            "hexawyn.cli.commands.mcp_client_group.get_integration",
            return_value=integration,
        ):
            result = runner.invoke(claude, ["install"])

        assert result.exit_code == 1
        assert "boom" in result.output


class TestClaudeUninstallCommand:
    def test_uninstall_success(self) -> None:
        runner = CliRunner()
        integration = _mock_integration(
            uninstall_result=IntegrationResult(success=True, message="removed")
        )
        with patch(
            "hexawyn.cli.commands.mcp_client_group.get_integration",
            return_value=integration,
        ):
            result = runner.invoke(claude, ["uninstall"])

        assert result.exit_code == 0
        assert "removed from Claude Code" in result.output

    def test_uninstall_not_configured(self) -> None:
        runner = CliRunner()
        integration = _mock_integration(
            uninstall_result=IntegrationResult(success=True, message="not configured")
        )
        with patch(
            "hexawyn.cli.commands.mcp_client_group.get_integration",
            return_value=integration,
        ):
            result = runner.invoke(claude, ["uninstall"])

        assert result.exit_code == 0
        assert "nothing to remove" in result.output

    def test_uninstall_failure(self) -> None:
        runner = CliRunner()
        integration = _mock_integration(
            uninstall_result=IntegrationResult(success=False, message="boom")
        )
        with patch(
            "hexawyn.cli.commands.mcp_client_group.get_integration",
            return_value=integration,
        ):
            result = runner.invoke(claude, ["uninstall"])

        assert result.exit_code == 1
        assert "boom" in result.output

    def test_uninstall_client_not_detected(self) -> None:
        runner = CliRunner()
        integration = _mock_integration(available=False)
        with patch(
            "hexawyn.cli.commands.mcp_client_group.get_integration",
            return_value=integration,
        ):
            result = runner.invoke(claude, ["uninstall"])

        assert result.exit_code == 1
        assert "Claude Code not detected" in result.output


class TestClaudeStatusCommand:
    def test_status_configured(self) -> None:
        runner = CliRunner()
        integration = _mock_integration(
            status=IntegrationStatus(
                configured=True,
                transport="stdio",
                command="python -m hexawyn.mcp.stdio",
            )
        )
        with patch(
            "hexawyn.cli.commands.mcp_client_group.get_integration",
            return_value=integration,
        ):
            result = runner.invoke(claude, ["status"])

        assert result.exit_code == 0
        assert "Status: ✓ Configured" in result.output
        assert "Server: hexawyn" in result.output
        assert "Transport: stdio" in result.output
        assert "Command: python -m hexawyn.mcp.stdio" in result.output

    def test_status_not_configured(self) -> None:
        runner = CliRunner()
        integration = _mock_integration(status=IntegrationStatus(configured=False))
        with patch(
            "hexawyn.cli.commands.mcp_client_group.get_integration",
            return_value=integration,
        ):
            result = runner.invoke(claude, ["status"])

        assert result.exit_code == 0
        assert "Status: ✗ Not configured" in result.output
        assert "hexa claude install" in result.output

    def test_status_error(self) -> None:
        runner = CliRunner()
        integration = _mock_integration(
            status=IntegrationStatus(configured=False, error="claude mcp list failed")
        )
        with patch(
            "hexawyn.cli.commands.mcp_client_group.get_integration",
            return_value=integration,
        ):
            result = runner.invoke(claude, ["status"])

        assert result.exit_code == 1
        assert "claude mcp list failed" in result.output

    def test_status_client_not_detected(self) -> None:
        runner = CliRunner()
        integration = _mock_integration(available=False)
        with patch(
            "hexawyn.cli.commands.mcp_client_group.get_integration",
            return_value=integration,
        ):
            result = runner.invoke(claude, ["status"])

        assert result.exit_code == 0
        assert "Status: ✗ Not configured" in result.output
        assert "hexa claude install" in result.output
