from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.domain.services.license_state import compute_license_state


class TestComputeLicenseState:
    def test_active_state(self) -> None:
        claims = MagicMock()
        claims.exp = 3100000000
        claims.plan = "team"
        result = compute_license_state(claims)
        assert result.state == "active"
        assert result.plan == "team"

    def test_expired_state(self) -> None:
        claims = MagicMock()
        claims.exp = 0
        claims.plan = "starter"
        result = compute_license_state(claims)
        assert result.state == "expired"

    def test_str_exp_type(self) -> None:
        claims = MagicMock()
        claims.exp = "3100000000"
        claims.plan = "team"
        result = compute_license_state(claims)
        assert result.state == "active"

    def test_not_expired_when_under_a_day_remains(self) -> None:
        import time

        claims = MagicMock()
        claims.exp = int(time.time()) + 21 * 3600  # ~21h in the future
        claims.plan = "team"
        result = compute_license_state(claims)
        assert result.state != "expired"
        assert result.days_remaining >= 1
