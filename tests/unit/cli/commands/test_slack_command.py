from __future__ import annotations

from unittest.mock import MagicMock, patch

from click.testing import CliRunner
from hexawyn.cli.commands.slack_command import slack


class TestSlackStatus:
    @staticmethod
    def _make_quota_mock(count: int = 0, limit: int = 50, is_unlimited: bool = False) -> MagicMock:
        mock_quota = MagicMock()
        mock_quota.count = count
        mock_quota.limit = limit
        mock_quota.is_unlimited = is_unlimited
        mock_quota.remaining = limit - count
        return mock_quota

    def test_status_shows_configuration_with_no_tokens(self) -> None:
        runner = CliRunner()
        mock_quota = self._make_quota_mock()
        with (
            patch.dict("os.environ", {}, clear=True),
            patch(
                "hexawyn.cli.commands.slack_command._get_current_slack_quota",
                return_value=mock_quota,
            ),
        ):
            result = runner.invoke(slack, ["status"])

        assert result.exit_code == 0
        assert "not set" in result.output

    def test_status_shows_all_tokens_configured(self) -> None:
        runner = CliRunner()
        mock_quota = self._make_quota_mock()
        env_vars = {
            "HEXAWYN_SLACK_WEBHOOK_URL": "https://hooks.slack.com/test",
            "SLACK_BOT_TOKEN": "xoxb-test",
            "SLACK_APP_TOKEN": "xapp-test",
        }
        with (
            patch.dict("os.environ", env_vars, clear=True),
            patch(
                "hexawyn.cli.commands.slack_command._get_current_slack_quota",
                return_value=mock_quota,
            ),
        ):
            result = runner.invoke(slack, ["status"])

        assert result.exit_code == 0
        assert "configured" in result.output

    def test_status_shows_socket_mode_when_app_token_set(self) -> None:
        runner = CliRunner()
        mock_quota = self._make_quota_mock()
        env_vars = {"SLACK_APP_TOKEN": "xapp-test"}
        with (
            patch.dict("os.environ", env_vars, clear=True),
            patch(
                "hexawyn.cli.commands.slack_command._get_current_slack_quota",
                return_value=mock_quota,
            ),
        ):
            result = runner.invoke(slack, ["status"])

        assert result.exit_code == 0
        assert "Socket Mode" in result.output

    def test_status_quota_unlimited(self) -> None:
        runner = CliRunner()
        mock_quota = self._make_quota_mock(is_unlimited=True)
        env_vars = {}
        with (
            patch.dict("os.environ", env_vars, clear=True),
            patch(
                "hexawyn.cli.commands.slack_command._get_current_slack_quota",
                return_value=mock_quota,
            ),
        ):
            result = runner.invoke(slack, ["status"])

        assert result.exit_code == 0
        assert "unlimited" in result.output


class TestSlackTest:
    def test_test_command_without_webhook_fails(self) -> None:
        runner = CliRunner()
        with patch.dict("os.environ", {}, clear=True):
            result = runner.invoke(slack, ["test"])

        assert result.exit_code == 0
        assert "HEXAWYN_SLACK_WEBHOOK_URL not set" in result.output

    def test_test_command_sends_and_receives_success(self) -> None:
        runner = CliRunner()
        env_vars = {
            "HEXAWYN_SLACK_WEBHOOK_URL": "https://hooks.slack.com/valid",
        }
        mock_adapter = MagicMock()
        mock_adapter.send_test_ping.return_value = True

        with (
            patch.dict("os.environ", env_vars, clear=True),
            patch(
                "hexawyn.cli.commands.slack_command.SlackAlertAdapter",
                return_value=mock_adapter,
            ),
        ):
            result = runner.invoke(slack, ["test"])

        assert result.exit_code == 0
        assert "Test alert sent" in result.output

    def test_test_command_sends_and_receives_failure(self) -> None:
        runner = CliRunner()
        env_vars = {
            "HEXAWYN_SLACK_WEBHOOK_URL": "https://hooks.slack.com/invalid",
        }
        mock_adapter = MagicMock()
        mock_adapter.send_test_ping.return_value = False

        with (
            patch.dict("os.environ", env_vars, clear=True),
            patch(
                "hexawyn.cli.commands.slack_command.SlackAlertAdapter",
                return_value=mock_adapter,
            ),
        ):
            result = runner.invoke(slack, ["test"])

        assert result.exit_code == 0
        assert "Failed to send" in result.output


class TestRequireEnvToken:
    def test_require_env_token_returns_token_when_set(self) -> None:
        from hexawyn.cli.commands.slack_command import _require_env_token

        with patch.dict("os.environ", {"MY_TOKEN": "abc123"}, clear=True):
            result = _require_env_token("MY_TOKEN", "test-display")
            assert result == "abc123"

    def test_require_env_token_returns_none_when_missing(self) -> None:
        from hexawyn.cli.commands.slack_command import _require_env_token

        with patch.dict("os.environ", {}, clear=True):
            result = _require_env_token("MISSING_VAR", "Missing message")
            assert result is None


class TestSlackListen:
    def test_listen_http_missing_bot_token_returns_early(self) -> None:
        runner = CliRunner()
        with patch.dict("os.environ", {}, clear=True):
            result = runner.invoke(slack, ["listen", "--http"])

        assert result.exit_code == 0

    def test_listen_socket_missing_both_tokens_returns_early(self) -> None:
        runner = CliRunner()
        with patch.dict("os.environ", {}, clear=True):
            result = runner.invoke(slack, ["listen"])

        assert result.exit_code == 0

    def test_listen_socket_missing_bot_token_returns_early(self) -> None:
        runner = CliRunner()
        env_vars = {"SLACK_APP_TOKEN": "xapp-test"}
        with patch.dict("os.environ", env_vars, clear=True):
            result = runner.invoke(slack, ["listen"])

        assert result.exit_code == 0
