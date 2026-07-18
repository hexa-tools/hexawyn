from datetime import UTC, datetime, timedelta

from hexawyn.domain.models.license import LicenseClaims


def _claims(exp_days_from_now: int = 30) -> LicenseClaims:
    exp = int((datetime.now(UTC) + timedelta(days=exp_days_from_now)).timestamp())
    return LicenseClaims(
        sub="test-user",
        plan="starter",
        clusters_max=1,
        users_max=1,
        investigations_monthly=50,
        history_days=7,
        providers=["vanilla"],
        exp=exp,
        iat=int(datetime.now(UTC).timestamp()),
    )


class TestComputeLicenseState:
    def test_active_when_more_than_7_days(self) -> None:
        from hexawyn.domain.services.license_state import compute_license_state

        state = compute_license_state(_claims(30))
        assert state.state == "active"
        assert state.days_remaining >= 28
        assert state.plan == "starter"

    def test_warning_when_7_days_or_less(self) -> None:
        from hexawyn.domain.services.license_state import compute_license_state

        state = compute_license_state(_claims(3))
        assert state.state == "warning"
        assert 1 <= state.days_remaining <= 7

    def test_expired_when_past(self) -> None:
        from hexawyn.domain.services.license_state import compute_license_state

        state = compute_license_state(_claims(-1))
        assert state.state == "expired"
        assert state.days_remaining < 0

    def test_expiry_date_formatted(self) -> None:
        from hexawyn.domain.services.license_state import compute_license_state

        claims = _claims(30)
        state = compute_license_state(claims)

        expected = datetime.fromtimestamp(claims.exp, tz=UTC).strftime("%d %b %Y")
        assert state.expiry_date == expected
