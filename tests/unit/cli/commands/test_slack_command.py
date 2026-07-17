import os
from unittest.mock import AsyncMock, patch

from click.testing import CliRunner
from hexawyn.cli.main import app


class TestSlackCommand:
    def setup_method(self) -> None:
        self.runner = CliRunner()

    def test_slack_test_sends_test_message(self) -> None:
        with patch.dict(
            os.environ,
            {"HEXAWYN_SLACK_WEBHOOK_URL": "https://hooks.slack.com/test"},
        ):
            with patch("hexawyn.cli.commands.slack_command.SlackAlertAdapter") as mock_adapter:
                mock_adapter.return_value.send_test_ping.return_value = True
                result = self.runner.invoke(app, ["slack", "test"])
        assert result.exit_code == 0
        assert "✅" in result.output

    def test_slack_test_shows_error_when_no_webhook(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            result = self.runner.invoke(app, ["slack", "test"])
        assert "HEXAWYN_SLACK_WEBHOOK_URL" in result.output

    def test_slack_test_shows_failure_message_on_send_error(self) -> None:
        with patch.dict(
            os.environ,
            {"HEXAWYN_SLACK_WEBHOOK_URL": "https://hooks.slack.com/test"},
        ):
            with patch("hexawyn.cli.commands.slack_command.SlackAlertAdapter") as mock_adapter:
                mock_adapter.return_value.send_test_ping.return_value = False
                result = self.runner.invoke(app, ["slack", "test"])
        assert result.exit_code == 0
        assert "❌" in result.output

    def test_slack_status_shows_not_configured_without_env(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            with patch("hexawyn.cli.commands.slack_command._get_current_slack_quota") as mock_quota:
                mock_quota.return_value.is_unlimited = False
                mock_quota.return_value.count = 0
                mock_quota.return_value.limit = 5
                mock_quota.return_value.remaining = 5
                result = self.runner.invoke(app, ["slack", "status"])
        assert result.exit_code == 0
        assert "not set" in result.output or "❌" in result.output

    def test_slack_status_shows_configured_with_env(self) -> None:
        with patch.dict(
            os.environ,
            {"HEXAWYN_SLACK_WEBHOOK_URL": "https://hooks.slack.com/test"},
        ):
            with patch("hexawyn.cli.commands.slack_command._get_current_slack_quota") as mock_quota:
                mock_quota.return_value.is_unlimited = False
                mock_quota.return_value.count = 2
                mock_quota.return_value.limit = 5
                mock_quota.return_value.remaining = 3
                result = self.runner.invoke(app, ["slack", "status"])
        assert result.exit_code == 0
        assert "✅" in result.output

    def test_slack_status_shows_unlimited_for_pro(self) -> None:
        with patch.dict(
            os.environ,
            {"HEXAWYN_SLACK_WEBHOOK_URL": "https://hooks.slack.com/x"},
        ):
            with patch("hexawyn.cli.commands.slack_command._get_current_slack_quota") as mock_quota:
                mock_quota.return_value.is_unlimited = True
                result = self.runner.invoke(app, ["slack", "status"])
        assert result.exit_code == 0
        assert "unlimited" in result.output.lower() or "Pro" in result.output


class TestSlackListenCommand:
    def setup_method(self) -> None:
        self.runner = CliRunner()

    def test_listen_requires_slack_app_token(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            result = self.runner.invoke(app, ["slack", "listen"])
        assert result.exit_code == 0
        assert "SLACK_APP_TOKEN" in result.output

    def test_listen_requires_slack_bot_token_when_app_token_set(self) -> None:
        with patch.dict(os.environ, {"SLACK_APP_TOKEN": "xapp-test"}, clear=True):
            result = self.runner.invoke(app, ["slack", "listen"])
        assert result.exit_code == 0
        assert "SLACK_BOT_TOKEN" in result.output

    def test_listen_starts_socket_client_with_both_tokens(self) -> None:
        env_vars = {"SLACK_APP_TOKEN": "xapp-test", "SLACK_BOT_TOKEN": "xoxb-test"}
        with patch.dict(os.environ, env_vars):
            with patch("hexawyn.cli.commands.slack_command.SlackSocketClient") as mock_client_cls:
                mock_client = mock_client_cls.return_value
                mock_client.run = AsyncMock(return_value=None)
                result = self.runner.invoke(app, ["slack", "listen"])
        assert result.exit_code == 0
        assert "Socket Mode" in result.output

    def test_listen_uses_default_port_8080_with_http_flag(self) -> None:
        with patch.dict(os.environ, {"SLACK_BOT_TOKEN": "xoxb-test"}):
            with patch("hexawyn.cli.commands.slack_command.SlackEventServer") as mock_server_cls:
                mock_server_cls.return_value.start.return_value = None
                self.runner.invoke(app, ["slack", "listen", "--http"])
        call_kwargs = mock_server_cls.return_value.start.call_args
        port_used = call_kwargs[1].get("port") if call_kwargs else None
        assert port_used == 8080

    def test_listen_accepts_custom_port_with_http_flag(self) -> None:
        with patch.dict(os.environ, {"SLACK_BOT_TOKEN": "xoxb-test"}):
            with patch("hexawyn.cli.commands.slack_command.SlackEventServer") as mock_server_cls:
                mock_server_cls.return_value.start.return_value = None
                self.runner.invoke(app, ["slack", "listen", "--http", "--port", "3000"])
        call_kwargs = mock_server_cls.return_value.start.call_args
        port_used = call_kwargs[1].get("port") if call_kwargs else None
        assert port_used == 3000

    def test_listen_shows_startup_message(self) -> None:
        env_vars = {"SLACK_APP_TOKEN": "xapp-test", "SLACK_BOT_TOKEN": "xoxb-test"}
        with patch.dict(os.environ, env_vars):
            with patch("hexawyn.cli.commands.slack_command.SlackSocketClient") as mock_client_cls:
                mock_client = mock_client_cls.return_value
                mock_client.run = AsyncMock(return_value=None)
                result = self.runner.invoke(app, ["slack", "listen"])
        assert result.exit_code == 0
        assert "Socket Mode" in result.output or "listening" in result.output.lower()
