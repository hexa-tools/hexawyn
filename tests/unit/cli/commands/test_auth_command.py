from __future__ import annotations

from unittest.mock import MagicMock, patch

from click.testing import CliRunner
from hexawyn.cli.commands.auth_command import auth


class TestAuthStatus:
    def test_status_shows_missing_when_no_license(self) -> None:
        runner = CliRunner()
        with patch(
            "hexawyn.cli.commands.auth_command.read_license_state",
        ) as mock_read:
            mock_read.return_value = MagicMock(
                state="missing", plan="unknown", days_remaining=0, expiry_date=""
            )
            result = runner.invoke(auth, ["status"])

        assert result.exit_code == 0
        assert "License not configured" in result.output

    def test_status_shows_invalid_when_corrupt(self) -> None:
        runner = CliRunner()
        with patch(
            "hexawyn.cli.commands.auth_command.read_license_state",
        ) as mock_read:
            mock_read.return_value = MagicMock(
                state="invalid", plan="unknown", days_remaining=0, expiry_date=""
            )
            result = runner.invoke(auth, ["status"])

        assert result.exit_code == 0
        assert "Could not read license data" in result.output

    def test_status_shows_expired_license(self) -> None:
        runner = CliRunner()
        with patch(
            "hexawyn.cli.commands.auth_command.read_license_state",
        ) as mock_read:
            mock_read.return_value = MagicMock(
                state="expired", plan="starter", days_remaining=-5, expiry_date="01 Jan 2026"
            )
            result = runner.invoke(auth, ["status"])

        assert result.exit_code == 0
        assert "expired" in result.output.lower()

    def test_status_shows_active_license(self) -> None:
        runner = CliRunner()
        with patch(
            "hexawyn.cli.commands.auth_command.read_license_state",
        ) as mock_read:
            mock_read.return_value = MagicMock(
                state="active",
                plan="starter",
                days_remaining=25,
                expiry_date="01 Jan 2027",
            )
            result = runner.invoke(auth, ["status"])

        assert result.exit_code == 0
        assert "active" in result.output.lower()


class TestAuthSetToken:
    def test_set_token_activates_successfully(self) -> None:
        runner = CliRunner()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "token": "jwt-token-value",
            "plan": "starter",
            "expires_at": "2027-01-01T00:00:00Z",
        }

        with (
            patch(
                "hexawyn.cli.commands.auth_command._activate_license",
                return_value=mock_response,
            ),
            patch(
                "hexawyn.cli.commands.auth_command.load_config",
                return_value={},
            ),
            patch(
                "hexawyn.cli.commands.auth_command.save_config",
            ) as mock_save,
            patch(
                "hexawyn.cli.commands.auth_command.LICENSE_KEY_PATH",
            ) as mock_path,
        ):
            mock_path.parent.mkdir.return_value = None
            result = runner.invoke(auth, ["set-token", "valid-token-1234567890"])

        assert result.exit_code == 0
        assert "License activated" in result.output
        mock_save.assert_called_once()

    def test_set_token_handles_connection_error(self) -> None:
        runner = CliRunner()
        import httpx

        with patch(
            "hexawyn.cli.commands.auth_command._activate_license",
            side_effect=httpx.ConnectError("connection refused"),
        ):
            result = runner.invoke(auth, ["set-token", "any-token"])

        assert result.exit_code == 1
        assert "Failed to connect" in result.output

    def test_set_token_handles_non_200_response(self) -> None:
        runner = CliRunner()
        mock_response = MagicMock()
        mock_response.status_code = 401
        mock_response.json.return_value = {"detail": "Invalid API key"}

        with patch(
            "hexawyn.cli.commands.auth_command._activate_license",
            return_value=mock_response,
        ):
            result = runner.invoke(auth, ["set-token", "bad-token"])

        assert result.exit_code == 1
        assert "Invalid API key" in result.output

    def test_set_token_handles_non_json_error_response(self) -> None:
        runner = CliRunner()
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.json.side_effect = ValueError("not json")

        with patch(
            "hexawyn.cli.commands.auth_command._activate_license",
            return_value=mock_response,
        ):
            result = runner.invoke(auth, ["set-token", "some-token"])

        assert result.exit_code == 1
        assert "Unknown error" in result.output


class TestFormatExpiry:
    def test_format_expiry_returns_unknown_for_empty_string(self) -> None:
        from hexawyn.cli.commands.auth_command import _format_expiry

        result = _format_expiry("")
        assert result == "unknown"

    def test_format_expiry_handles_iso_format(self) -> None:
        from hexawyn.cli.commands.auth_command import _format_expiry

        result = _format_expiry("2027-06-15T00:00:00Z")
        assert "Jun" in result
        assert "2027" in result

    def test_format_expiry_handles_unix_timestamp(self) -> None:
        from hexawyn.cli.commands.auth_command import _format_expiry

        result = _format_expiry("1800000000")
        assert "2027" in result

    def test_format_expiry_returns_original_on_parse_error(self) -> None:
        from hexawyn.cli.commands.auth_command import _format_expiry

        result = _format_expiry("not-a-date")
        assert result == "not-a-date"


class TestAuthAccount:
    def test_account_without_token_shows_error(self) -> None:
        runner = CliRunner()
        with patch(
            "hexawyn.infrastructure.config.config_manager.load_config",
            return_value={},
        ):
            result = runner.invoke(auth, ["account"])

        assert result.exit_code == 1
        assert "No license configured" in result.output

    def test_account_handles_connection_error(self) -> None:
        runner = CliRunner()
        import httpx

        with (
            patch(
                "hexawyn.infrastructure.config.config_manager.load_config",
                return_value={"hexawyn_token": "valid-token"},
            ),
            patch(
                "hexawyn.cli.commands.auth_command.httpx.post",
                side_effect=httpx.ConnectError("refused"),
            ),
        ):
            result = runner.invoke(auth, ["account"])

        assert result.exit_code == 1
        assert "polar.sh/purchases" in result.output

    def test_account_handles_404_response(self) -> None:
        runner = CliRunner()
        mock_resp = MagicMock()
        mock_resp.status_code = 404

        with (
            patch(
                "hexawyn.infrastructure.config.config_manager.load_config",
                return_value={"hexawyn_token": "valid-token"},
            ),
            patch(
                "hexawyn.cli.commands.auth_command.httpx.post",
                return_value=mock_resp,
            ),
        ):
            result = runner.invoke(auth, ["account"])

        assert result.exit_code == 1
        assert "polar.sh" in result.output

    def test_account_handles_500_with_detail(self) -> None:
        runner = CliRunner()
        mock_resp = MagicMock()
        mock_resp.status_code = 500
        mock_resp.json.return_value = {"detail": "Internal error"}

        with (
            patch(
                "hexawyn.infrastructure.config.config_manager.load_config",
                return_value={"hexawyn_token": "valid-token"},
            ),
            patch(
                "hexawyn.cli.commands.auth_command.httpx.post",
                return_value=mock_resp,
            ),
        ):
            result = runner.invoke(auth, ["account"])

        assert result.exit_code == 1
        assert "Internal error" in result.output

    def test_account_handles_missing_portal_url(self) -> None:
        runner = CliRunner()
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {}

        with (
            patch(
                "hexawyn.infrastructure.config.config_manager.load_config",
                return_value={"hexawyn_token": "valid-token"},
            ),
            patch(
                "hexawyn.cli.commands.auth_command.httpx.post",
                return_value=mock_resp,
            ),
        ):
            result = runner.invoke(auth, ["account"])

        assert result.exit_code == 1
        assert "No portal URL returned" in result.output

    def test_account_opens_browser_on_success(self) -> None:
        runner = CliRunner()
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"url": "https://polar.sh/portal/xyz"}

        with (
            patch(
                "hexawyn.infrastructure.config.config_manager.load_config",
                return_value={"hexawyn_token": "valid-token"},
            ),
            patch(
                "hexawyn.cli.commands.auth_command.httpx.post",
                return_value=mock_resp,
            ),
            patch(
                "webbrowser.open",
            ) as mock_browser,
        ):
            result = runner.invoke(auth, ["account"])

        assert result.exit_code == 0
        assert "Opening subscription portal" in result.output
        mock_browser.assert_called_once_with("https://polar.sh/portal/xyz")
