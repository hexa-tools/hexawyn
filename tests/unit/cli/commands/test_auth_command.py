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

        with patch("httpx.AsyncClient", return_value=fake_client):
            result = self.runner.invoke(app, ["auth", "set-token", "hxw_test_abc123"])
        assert result.exit_code == 0
        assert "starter" in result.output

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
        with patch(
            "hexawyn.cli.commands.auth_command._read_license_key",
            return_value=None,
        ):
            result = self.runner.invoke(app, ["auth", "status"])
        assert result.exit_code == 0
        assert "not configured" in result.output.lower()

    def test_status_shows_plan_when_license_exists(self) -> None:
        with patch(
            "hexawyn.cli.commands.auth_command._read_license_key",
            return_value="eyJhbGci.eyJwbGFuIjoic3RhcnRlciJ9.signature",
        ):
            with patch(
                "hexawyn.cli.commands.auth_command._decode_jwt_payload",
                return_value={"plan": "starter", "exp": 1780000000},
            ):
                with patch(
                    "hexawyn.cli.commands.auth_command._is_jwt_expired",
                    return_value=False,
                ):
                    result = self.runner.invoke(app, ["auth", "status"])
        assert result.exit_code == 0
        assert "starter" in result.output

    def test_status_shows_expiry_when_license_exists(self) -> None:
        with patch(
            "hexawyn.cli.commands.auth_command._read_license_key",
            return_value="jwt",
        ):
            with patch(
                "hexawyn.cli.commands.auth_command._decode_jwt_payload",
                return_value={"plan": "team", "exp": 1780000000},
            ):
                with patch(
                    "hexawyn.cli.commands.auth_command._is_jwt_expired",
                    return_value=False,
                ):
                    result = self.runner.invoke(app, ["auth", "status"])
        assert result.exit_code == 0
        assert "team" in result.output
        assert "Expires" in result.output

    def test_status_shows_expired_when_license_expired(self) -> None:
        with patch(
            "hexawyn.cli.commands.auth_command._read_license_key",
            return_value="jwt",
        ):
            with patch(
                "hexawyn.cli.commands.auth_command._decode_jwt_payload",
                return_value={"plan": "starter", "exp": 1000000000},
            ):
                with patch(
                    "hexawyn.cli.commands.auth_command._is_jwt_expired",
                    return_value=True,
                ):
                    result = self.runner.invoke(app, ["auth", "status"])
        assert result.exit_code == 0
        assert "expired" in result.output.lower()

    def test_status_shows_error_on_corrupted_jwt(self) -> None:
        with patch(
            "hexawyn.cli.commands.auth_command._read_license_key",
            return_value="not.valid.jwt",
        ):
            with patch(
                "hexawyn.cli.commands.auth_command._decode_jwt_payload",
                return_value=None,
            ):
                result = self.runner.invoke(app, ["auth", "status"])
        assert result.exit_code == 0
        assert "not read" in result.output.lower() or "error" in result.output.lower()


class TestDecodeJwtPayload:
    def test_decodes_valid_jwt(self) -> None:
        import base64
        import json

        payload = {"plan": "starter", "exp": 1780000000}
        payload_b64 = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode().rstrip("=")
        jwt = f"header.{payload_b64}.signature"

        from hexawyn.cli.commands.auth_command import _decode_jwt_payload

        result = _decode_jwt_payload(jwt)
        assert result is not None
        assert result["plan"] == "starter"

    def test_returns_none_for_short_string(self) -> None:
        from hexawyn.cli.commands.auth_command import _decode_jwt_payload

        assert _decode_jwt_payload("notajwt") is None
        assert _decode_jwt_payload("") is None

    def test_returns_none_for_invalid_base64(self) -> None:
        from hexawyn.cli.commands.auth_command import _decode_jwt_payload

        assert _decode_jwt_payload("a.!!!.c") is None

    def test_returns_none_for_non_dict_json(self) -> None:
        import base64

        payload_b64 = base64.urlsafe_b64encode(b'"just a string"').decode().rstrip("=")
        jwt = f"header.{payload_b64}.signature"

        from hexawyn.cli.commands.auth_command import _decode_jwt_payload

        assert _decode_jwt_payload(jwt) is None


class TestIsJwtExpired:
    def test_expired_in_past(self) -> None:
        from datetime import UTC, datetime

        from hexawyn.cli.commands.auth_command import _is_jwt_expired

        past = int((datetime.now(UTC).timestamp()) - 3600)
        assert _is_jwt_expired(past) is True

    def test_not_expired_in_future(self) -> None:
        from datetime import UTC, datetime

        from hexawyn.cli.commands.auth_command import _is_jwt_expired

        future = int((datetime.now(UTC).timestamp()) + 86400 * 365)
        assert _is_jwt_expired(future) is False

    def test_zero_exp_returns_false(self) -> None:
        from hexawyn.cli.commands.auth_command import _is_jwt_expired

        assert _is_jwt_expired(0) is False


class TestFormatExpiry:
    def test_valid_iso_date(self) -> None:
        from hexawyn.cli.commands.auth_command import _format_expiry

        result = _format_expiry("2026-08-17T00:00:00Z")
        assert "2026-08-17" in result
        assert "days" in result

    def test_empty_string_returns_unknown(self) -> None:
        from hexawyn.cli.commands.auth_command import _format_expiry

        assert _format_expiry("") == "unknown"

    def test_invalid_date_returns_input(self) -> None:
        from hexawyn.cli.commands.auth_command import _format_expiry

        assert _format_expiry("not-a-date") == "not-a-date"


class TestFormatExpiryFromTimestamp:
    def test_valid_timestamp(self) -> None:
        from datetime import UTC, datetime

        from hexawyn.cli.commands.auth_command import _format_expiry_from_timestamp

        future = int((datetime.now(UTC).timestamp()) + 86400 * 30)
        result = _format_expiry_from_timestamp(future)
        assert "days" in result

    def test_zero_timestamp_returns_unknown(self) -> None:
        from hexawyn.cli.commands.auth_command import _format_expiry_from_timestamp

        assert _format_expiry_from_timestamp(0) == "unknown"


class TestReadLicenseKey:
    def test_returns_none_when_file_missing(self) -> None:
        from pathlib import Path

        with patch(
            "hexawyn.cli.commands.auth_command.LICENSE_KEY_PATH",
            Path("/tmp/nonexistent_license.key"),
        ):
            from hexawyn.cli.commands.auth_command import _read_license_key

            assert _read_license_key() is None

    def test_returns_content_when_file_exists(self) -> None:
        import tempfile
        from pathlib import Path

        with tempfile.NamedTemporaryFile(mode="w", suffix=".key", delete=False) as f:
            f.write("test-token\n")
            f.flush()
            try:
                with patch(
                    "hexawyn.cli.commands.auth_command.LICENSE_KEY_PATH",
                    Path(f.name),
                ):
                    from hexawyn.cli.commands.auth_command import _read_license_key

                    assert _read_license_key() == "test-token"
            finally:
                Path(f.name).unlink()


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


class TestIsJwtExpiredEdgeCases:
    def test_overflow_timestamp_returns_false(self) -> None:
        from hexawyn.cli.commands.auth_command import _is_jwt_expired

        assert _is_jwt_expired(99999999999) is False


class TestFormatExpiryFromTimestampEdgeCases:
    def test_overflow_timestamp_returns_string(self) -> None:
        from hexawyn.cli.commands.auth_command import _format_expiry_from_timestamp

        result = _format_expiry_from_timestamp(99999999999)
        assert isinstance(result, str)
