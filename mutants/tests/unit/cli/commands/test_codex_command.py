from __future__ import annotations

from unittest.mock import MagicMock, patch

from click.testing import CliRunner
from hexawyn.cli.commands.codex_command import codex
from hexawyn.cli.integrations.mcp.base import IntegrationStatus


class TestCodexCommand:
    def test_group_exposes_commands(self) -> None:
        names = [cmd.name for cmd in codex.commands.values()]
        assert set(names) == {"install", "uninstall", "status"}

    def test_status_hint_uses_codex_client(self) -> None:
        integration = MagicMock()
        integration.is_available.return_value = True
        integration.status.return_value = IntegrationStatus(configured=False)
        with patch(
            "hexawyn.cli.commands.mcp_client_group.get_integration",
            return_value=integration,
        ):
            result = CliRunner().invoke(codex, ["status"])

        assert result.exit_code == 0
        assert "hexa codex install" in result.output

    def test_registered_in_main_app(self) -> None:
        from hexawyn.cli.main import app

        assert "codex" in app.commands
