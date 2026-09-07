import base64
import json
from datetime import UTC, datetime, timedelta
from pathlib import Path
from unittest.mock import MagicMock, patch


def _jwt(plan: str = "starter", exp_days: int = 30) -> str:
    exp = int((datetime.now(UTC) + timedelta(days=exp_days)).timestamp())
    payload = json.dumps({"plan": plan, "exp": exp, "sub": "test", "iat": 0})
    payload_b64 = base64.urlsafe_b64encode(payload.encode()).decode().rstrip("=")
    return f"header.{payload_b64}.signature"


class TestReadLicenseState:
    def test_active_license(self) -> None:
        from hexawyn.infrastructure.license.license_reader import read_license_state

        with (
            patch.object(Path, "exists", return_value=True),
            patch.object(Path, "read_text", return_value=_jwt("starter", 30)),
        ):
            state = read_license_state()
        assert state.state == "active"
        assert state.plan == "starter"

    def test_warning_license(self) -> None:
        from hexawyn.infrastructure.license.license_reader import read_license_state

        with (
            patch.object(Path, "exists", return_value=True),
            patch.object(Path, "read_text", return_value=_jwt("team", 3)),
        ):
            state = read_license_state()
        assert state.state == "warning"
        assert state.plan == "team"

    def test_expired_license(self) -> None:
        from hexawyn.infrastructure.license.license_reader import read_license_state

        with (
            patch.object(Path, "exists", return_value=True),
            patch.object(Path, "read_text", return_value=_jwt("starter", -1)),
        ):
            state = read_license_state()
        assert state.state == "expired"

    def test_missing_license_file(self) -> None:
        from hexawyn.infrastructure.license.license_reader import read_license_state

        with patch.object(Path, "exists", return_value=False):
            state = read_license_state()
        assert state.state == "missing"

    def test_invalid_jwt(self) -> None:
        from hexawyn.infrastructure.license.license_reader import read_license_state

        with (
            patch.object(Path, "exists", return_value=True),
            patch.object(Path, "read_text", return_value="bad-token"),
        ):
            state = read_license_state()
        assert state.state == "invalid"

    def test_active_state_shows_plan_and_expiry(self) -> None:
        from hexawyn.infrastructure.license.license_reader import read_license_state

        with (
            patch.object(Path, "exists", return_value=True),
            patch.object(Path, "read_text", return_value=_jwt("scale_up", 60)),
        ):
            state = read_license_state()
        assert state.state == "active"
        assert state.plan == "scale_up"
        assert state.days_remaining >= 58  # noqa: PLR2004
        assert state.expiry_date != ""

    def test_reads_from_env_var_when_set(self) -> None:
        from hexawyn.infrastructure.license.license_reader import (
            _read_license_key,
        )

        with patch.dict("os.environ", {"HEXAWYN_LICENSE_KEY": _jwt("starter", 60)}):
            key = _read_license_key()
        assert key is not None
        assert "header" in key

    def test_reads_from_file_when_env_not_set(self, tmp_path: Path) -> None:
        from hexawyn.infrastructure.license.license_reader import _read_license_key

        license_file = tmp_path / "license.key"
        license_file.write_text(_jwt("team", 90))
        with patch.dict("os.environ", {}, clear=True):
            with patch(
                "hexawyn.infrastructure.license.license_reader.LICENSE_KEY_PATH",
                license_file,
            ):
                key = _read_license_key()
        assert key is not None

    def test_returns_none_when_no_env_and_no_file(self) -> None:
        from hexawyn.infrastructure.license.license_reader import _read_license_key

        with patch.dict("os.environ", {}, clear=True):
            with patch.object(Path, "exists", return_value=False):
                assert _read_license_key() is None

    def test_no_expiry_license_stays_active(self) -> None:
        import base64
        import json

        payload = json.dumps({"plan": "enterprise", "sub": "org", "iat": 0})
        payload_b64 = base64.urlsafe_b64encode(payload.encode()).decode().rstrip("=")
        no_exp_jwt = f"header.{payload_b64}.signature"

        from hexawyn.infrastructure.license.license_reader import read_license_state

        with (
            patch.object(Path, "exists", return_value=True),
            patch.object(Path, "read_text", return_value=no_exp_jwt),
        ):
            state = read_license_state()
        assert state.state == "active"

    def test_refresh_license_handles_missing_token(self) -> None:
        from hexawyn.infrastructure.license.license_reader import refresh_license

        with patch(
            "hexawyn.infrastructure.config.config_manager.load_config",
            return_value={},
        ):
            result = refresh_license()
            assert result is False

    def test_refresh_license_handles_http_error(self) -> None:
        from hexawyn.infrastructure.license.license_reader import refresh_license

        with patch(
            "hexawyn.infrastructure.config.config_manager.load_config",
            return_value={"hexawyn_token": "fake-token"},
        ):
            with patch(
                "hexawyn.infrastructure.config.machine_id.get_machine_id",
                return_value="fake-machine-id",
            ):
                with patch("httpx.Client.post", side_effect=Exception("timeout")):
                    result = refresh_license()
                    assert result is False

    def test_license_state_from_env_key(self) -> None:
        with patch.dict("os.environ", {"HEXAWYN_LICENSE_KEY": _jwt("scale_up", 120)}):
            from hexawyn.infrastructure.license.license_reader import (
                read_license_state,
            )

            state = read_license_state()
            assert state.state == "active"
            assert state.plan == "scale_up"

    def test_read_license_state_invalid_on_parse_error(self) -> None:
        from hexawyn.infrastructure.license.license_reader import read_license_state

        with (
            patch.object(Path, "exists", return_value=True),
            patch.object(Path, "read_text", return_value="header.W3sibm90LXZhbGlkLWpzb259XQ==.sig"),
        ):
            state = read_license_state()
            assert state.state == "invalid"

    def test_read_license_key_exception_returns_none(self) -> None:
        from hexawyn.infrastructure.license.license_reader import _read_license_key

        with patch.dict("os.environ", {}, clear=True):
            with patch.object(Path, "exists", return_value=True):
                with patch.object(Path, "read_text", side_effect=OSError("permission denied")):
                    assert _read_license_key() is None

    def test_refresh_license_returns_false_on_non_200(self) -> None:
        from hexawyn.infrastructure.license.license_reader import refresh_license

        with patch(
            "hexawyn.infrastructure.config.config_manager.load_config",
            return_value={"hexawyn_token": "fake-token"},
        ):
            with patch(
                "hexawyn.infrastructure.config.machine_id.get_machine_id",
                return_value="fake-machine-id",
            ):
                mock_response = MagicMock()
                mock_response.status_code = 403
                mock_client = MagicMock()
                mock_client.__enter__ = MagicMock(return_value=mock_client)
                mock_client.__exit__ = MagicMock(return_value=False)
                mock_client.post.return_value = mock_response
                with patch("httpx.Client", return_value=mock_client):
                    result = refresh_license()
                    assert result is False

    def test_refresh_license_returns_false_on_empty_token_in_response(self) -> None:
        from hexawyn.infrastructure.license.license_reader import refresh_license

        with patch(
            "hexawyn.infrastructure.config.config_manager.load_config",
            return_value={"hexawyn_token": "fake-token"},
        ):
            with patch(
                "hexawyn.infrastructure.config.machine_id.get_machine_id",
                return_value="fake-machine-id",
            ):
                mock_response = MagicMock()
                mock_response.status_code = 200
                mock_response.json.return_value = {}
                mock_client = MagicMock()
                mock_client.__enter__ = MagicMock(return_value=mock_client)
                mock_client.__exit__ = MagicMock(return_value=False)
                mock_client.post.return_value = mock_response
                with patch("httpx.Client", return_value=mock_client):
                    result = refresh_license()
                    assert result is False
