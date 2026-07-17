from datetime import UTC, datetime, timedelta

from hexawyn.domain.models.license import LicenseKey
from hexawyn.domain.models.quota import LicenseTier


class TestLicenseKey:
    def test_valid_when_not_expired(self) -> None:
        future = datetime.now(UTC) + timedelta(days=365)
        key = LicenseKey(
            tier=LicenseTier.TEAM,
            expires_at=future,
            licensee="dev@company.com",
        )
        assert key.is_valid is True
        assert key.is_expired is False

    def test_expired_when_past_date(self) -> None:
        past = datetime.now(UTC) - timedelta(days=1)
        key = LicenseKey(
            tier=LicenseTier.TEAM,
            expires_at=past,
            licensee="expired@company.com",
        )
        assert key.is_expired is True
        assert key.is_valid is False

    def test_perpetual_never_expires(self) -> None:
        key = LicenseKey(
            tier=LicenseTier.SCALE_UP,
            expires_at=None,
            licensee="enterprise@bigcorp.com",
        )
        assert key.is_expired is False
        assert key.is_valid is True

    def test_stores_tier(self) -> None:
        key = LicenseKey(
            tier=LicenseTier.SCALE_UP,
            expires_at=None,
            licensee="scale@company.com",
        )
        assert key.tier == LicenseTier.SCALE_UP

    def test_stores_licensee(self) -> None:
        key = LicenseKey(
            tier=LicenseTier.STARTER,
            expires_at=None,
            licensee="free@opensource.org",
        )
        assert key.licensee == "free@opensource.org"
