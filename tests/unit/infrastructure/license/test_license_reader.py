import base64
import json
from datetime import UTC, datetime, timedelta
from pathlib import Path
from unittest.mock import patch


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
        assert state.days_remaining >= 58
        assert state.expiry_date != ""
