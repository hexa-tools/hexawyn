from __future__ import annotations

from unittest.mock import MagicMock, patch

from click.testing import CliRunner
from hexawyn.cli.commands.gemini_command import gemini
from hexawyn.cli.integrations.mcp.base import IntegrationStatus


class TestGeminiCommand:
    def test_group_exposes_commands(self) -> None:
        names = [cmd.name for cmd in gemini.commands.values()]
        assert set(names) == {"install", "uninstall", "status"}

    def test_status_hint_uses_gemini_client(self) -> None:
        integration = MagicMock()
        integration.is_available.return_value = True
        integration.status.return_value = IntegrationStatus(configured=False)
        with patch(
            "hexawyn.cli.commands.mcp_client_group.get_integration",
            return_value=integration,
        ):
            result = CliRunner().invoke(gemini, ["status"])

        assert result.exit_code == 0
        assert "hexa gemini install" in result.output

    def test_registered_in_main_app(self) -> None:
        from hexawyn.cli.main import app

        assert "gemini" in app.commands
