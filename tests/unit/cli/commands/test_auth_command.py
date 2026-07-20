"""Tests for hexa auth CLI commands."""

from unittest.mock import AsyncMock, MagicMock, patch

from click.testing import CliRunner
from hexawyn.cli.main import app


class TestAuthSetToken:
    def setup_method(self) -> None:
        self.runner = CliRunner()

    def test_set_token_stores_license_and_shows_plan(self) -> None:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "token": "eyJhbGciOiJSUzI1NiJ9.eyJwbGFuIjoic3RhcnRlciJ9.signature",
            "plan": "starter",
            "expires_at": "2026-08-17T00:00:00Z",
        }

        fake_client = MagicMock()
        fake_client.__aenter__ = AsyncMock(return_value=fake_client)
        fake_client.__aexit__ = AsyncMock(return_value=None)
        fake_client.post = AsyncMock(return_value=mock_response)

        with (
            patch("httpx.AsyncClient", return_value=fake_client),
            patch("hexawyn.cli.commands.auth_command.save_config") as mock_save,
            patch("pathlib.Path.mkdir"),
            patch("pathlib.Path.write_text") as mock_write,
        ):
            result = self.runner.invoke(app, ["auth", "set-token", "hxw_test_abc123"])
        assert result.exit_code == 0
        assert "starter" in result.output
        mock_save.assert_called_once()
        mock_write.assert_called_once()

    def test_set_token_prints_error_on_401(self) -> None:
        mock_response = MagicMock()
        mock_response.status_code = 401
        mock_response.json.return_value = {"detail": "Invalid API key"}

        fake_client = MagicMock()
        fake_client.__aenter__ = AsyncMock(return_value=fake_client)
        fake_client.__aexit__ = AsyncMock(return_value=None)
        fake_client.post = AsyncMock(return_value=mock_response)

        with patch("httpx.AsyncClient", return_value=fake_client):
            result = self.runner.invoke(app, ["auth", "set-token", "hxw_bad_key"])
        assert result.exit_code == 1
        assert "Invalid" in result.output

    def test_set_token_prints_error_on_connection_failure(self) -> None:
        import httpx

        fake_client = MagicMock()
        fake_client.__aenter__ = AsyncMock(return_value=fake_client)
        fake_client.__aexit__ = AsyncMock(return_value=None)
        fake_client.post = AsyncMock(side_effect=httpx.ConnectError("connection refused"))

        with patch("httpx.AsyncClient", return_value=fake_client):
            result = self.runner.invoke(app, ["auth", "set-token", "hxw_test_abc"])
        assert result.exit_code == 1

    def test_set_token_requires_token_argument(self) -> None:
        result = self.runner.invoke(app, ["auth", "set-token"])
        assert result.exit_code != 0


class TestAuthStatus:
    def setup_method(self) -> None:
        self.runner = CliRunner()

    def test_status_shows_not_configured_when_no_license(self) -> None:
        from hexawyn.domain.services.license_state import LicenseState

        with patch(
            "hexawyn.cli.commands.auth_command.read_license_state",
            return_value=LicenseState(
                state="missing", plan="unknown", days_remaining=0, expiry_date=""
            ),
        ):
            result = self.runner.invoke(app, ["auth", "status"])
        assert result.exit_code == 0
        assert "not configured" in result.output.lower()

    def test_status_shows_plan_when_license_exists(self) -> None:
        from hexawyn.domain.services.license_state import LicenseState

        with patch(
            "hexawyn.cli.commands.auth_command.read_license_state",
            return_value=LicenseState(
                state="active", plan="starter", days_remaining=30, expiry_date="19 Aug 2026"
            ),
        ):
            result = self.runner.invoke(app, ["auth", "status"])
        assert result.exit_code == 0
        assert "starter" in result.output.lower()

    def test_status_shows_expiry_when_license_exists(self) -> None:
        from hexawyn.domain.services.license_state import LicenseState

        with patch(
            "hexawyn.cli.commands.auth_command.read_license_state",
            return_value=LicenseState(
                state="active", plan="team", days_remaining=60, expiry_date="18 Sep 2026"
            ),
        ):
            result = self.runner.invoke(app, ["auth", "status"])
        assert result.exit_code == 0
        assert "Team" in result.output
        assert "Expires" in result.output

    def test_status_shows_expired_when_license_expired(self) -> None:
        from hexawyn.domain.services.license_state import LicenseState

        with patch(
            "hexawyn.cli.commands.auth_command.read_license_state",
            return_value=LicenseState(
                state="expired", plan="starter", days_remaining=-1, expiry_date="19 Jul 2026"
            ),
        ):
            result = self.runner.invoke(app, ["auth", "status"])
        assert result.exit_code == 0
        assert "expired" in result.output.lower()

    def test_status_shows_error_on_invalid_license(self) -> None:
        from hexawyn.domain.services.license_state import LicenseState

        with patch(
            "hexawyn.cli.commands.auth_command.read_license_state",
            return_value=LicenseState(
                state="invalid", plan="unknown", days_remaining=0, expiry_date=""
            ),
        ):
            result = self.runner.invoke(app, ["auth", "status"])
        assert result.exit_code == 0
        assert "not read" in result.output.lower() or "could not" in result.output.lower()


class TestFormatExpiry:
    def test_valid_iso_date(self) -> None:
        from hexawyn.cli.commands.auth_command import _format_expiry

        result = _format_expiry("2026-08-17T00:00:00Z")
        assert "Aug 2026" in result
        assert "days" in result

    def test_empty_string_returns_unknown(self) -> None:
        from hexawyn.cli.commands.auth_command import _format_expiry

        assert _format_expiry("") == "unknown"

    def test_invalid_date_returns_input(self) -> None:
        from hexawyn.cli.commands.auth_command import _format_expiry

        assert _format_expiry("not-a-date") == "not-a-date"


class TestActivateLicense:
    def test_calls_api_with_token(self) -> None:
        from hexawyn.cli.commands.auth_command import _activate_license

        mock_response = MagicMock()
        mock_response.status_code = 200

        fake_client = MagicMock()
        fake_client.__aenter__ = AsyncMock(return_value=fake_client)
        fake_client.__aexit__ = AsyncMock(return_value=None)
        fake_client.post = AsyncMock(return_value=mock_response)

        with patch("hexawyn.cli.commands.auth_command.httpx.AsyncClient", return_value=fake_client):
            result = _activate_license("https://test.local", "hxw_test")

        assert result.status_code == 200

    def test_connection_error_propagates(self) -> None:
        import httpx

        fake_client = MagicMock()
        fake_client.__aenter__ = AsyncMock(return_value=fake_client)
        fake_client.__aexit__ = AsyncMock(return_value=None)
        fake_client.post = AsyncMock(side_effect=httpx.ConnectError("refused"))

        from hexawyn.cli.commands.auth_command import _activate_license

        with patch("hexawyn.cli.commands.auth_command.httpx.AsyncClient", return_value=fake_client):
            import pytest

            with pytest.raises(httpx.ConnectError):
                _activate_license("https://test.local", "hxw_test")


class TestSetTokenErrorHandling:
    def test_set_token_handles_corrupted_response_json(self) -> None:
        from click.testing import CliRunner
        from hexawyn.cli.main import app

        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.json.side_effect = ValueError("corrupt json")
        fake_client = MagicMock()
        fake_client.__aenter__ = AsyncMock(return_value=fake_client)
        fake_client.__aexit__ = AsyncMock(return_value=None)
        fake_client.post = AsyncMock(return_value=mock_response)

        with patch("httpx.AsyncClient", return_value=fake_client):
            runner = CliRunner()
            result = runner.invoke(app, ["auth", "set-token", "hxw_test"])
        assert result.exit_code == 1


class TestAuthAccount:
    def setup_method(self) -> None:
        self.runner = CliRunner()

    def test_account_requires_token(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.config_manager.load_config",
            return_value={},
        ):
            result = self.runner.invoke(app, ["auth", "account"])
        assert result.exit_code == 1
        assert "No license configured" in result.output

    def test_account_opens_portal_on_success(self) -> None:
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"url": "https://polar.sh/portal/123"}

        with (
            patch(
                "hexawyn.infrastructure.config.config_manager.load_config",
                return_value={"hexawyn_token": "hxw_live_test"},
            ),
            patch("httpx.post", return_value=mock_resp),
            patch("webbrowser.open") as mock_browser,
        ):
            result = self.runner.invoke(app, ["auth", "account"])
        assert result.exit_code == 0
        assert "Opening subscription portal" in result.output
        mock_browser.assert_called_once_with("https://polar.sh/portal/123")

    def test_account_shows_404_message(self) -> None:
        mock_resp = MagicMock()
        mock_resp.status_code = 404

        with (
            patch(
                "hexawyn.infrastructure.config.config_manager.load_config",
                return_value={"hexawyn_token": "hxw_live_test"},
            ),
            patch("httpx.post", return_value=mock_resp),
        ):
            result = self.runner.invoke(app, ["auth", "account"])
        assert result.exit_code == 1
        assert "polar.sh/purchases" in result.output

    def test_account_handles_connection_error(self) -> None:
        import httpx

        with (
            patch(
                "hexawyn.infrastructure.config.config_manager.load_config",
                return_value={"hexawyn_token": "hxw_live_test"},
            ),
            patch("httpx.post", side_effect=httpx.ConnectError("refused")),
        ):
            result = self.runner.invoke(app, ["auth", "account"])
        assert result.exit_code == 1
        assert "Cannot reach hexa-cloud" in result.output

    def test_account_handles_other_http_error(self) -> None:
        mock_resp = MagicMock()
        mock_resp.status_code = 500
        mock_resp.json.return_value = {"detail": "Server error"}

        with (
            patch(
                "hexawyn.infrastructure.config.config_manager.load_config",
                return_value={"hexawyn_token": "hxw_live_test"},
            ),
            patch("httpx.post", return_value=mock_resp),
        ):
            result = self.runner.invoke(app, ["auth", "account"])
        assert result.exit_code == 1
        assert "Server error" in result.output

    def test_account_handles_error_with_corrupt_json(self) -> None:
        mock_resp = MagicMock()
        mock_resp.status_code = 500
        mock_resp.json.side_effect = ValueError("bad json")

        with (
            patch(
                "hexawyn.infrastructure.config.config_manager.load_config",
                return_value={"hexawyn_token": "hxw_live_test"},
            ),
            patch("httpx.post", return_value=mock_resp),
        ):
            result = self.runner.invoke(app, ["auth", "account"])
        assert result.exit_code == 1
        assert "Unknown error" in result.output

    def test_account_handles_missing_url_in_response(self) -> None:
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {}

        with (
            patch(
                "hexawyn.infrastructure.config.config_manager.load_config",
                return_value={"hexawyn_token": "hxw_live_test"},
            ),
            patch("httpx.post", return_value=mock_resp),
        ):
            result = self.runner.invoke(app, ["auth", "account"])
        assert result.exit_code == 1
        assert "No portal URL returned" in result.output
