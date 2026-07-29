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

    def test_accepts_arbitrary_tier_string(self) -> None:
        key = LicenseKey(tier="custom_plan", expires_at=None, licensee="test")
        assert key.tier == "custom_plan"

    def test_not_expired_at_exact_expiry_moment(self) -> None:
        now = datetime.now(UTC)
        key = LicenseKey(tier=LicenseTier.TEAM, expires_at=now, licensee="test")
        assert key.is_expired is True

    def test_empty_licensee_accepted(self) -> None:
        key = LicenseKey(tier=LicenseTier.STARTER, expires_at=None, licensee="")
        assert key.licensee == ""

    def test_equality(self) -> None:
        a = LicenseKey(tier=LicenseTier.TEAM, expires_at=None, licensee="a@b.com")
        b = LicenseKey(tier=LicenseTier.TEAM, expires_at=None, licensee="a@b.com")
        c = LicenseKey(tier=LicenseTier.STARTER, expires_at=None, licensee="a@b.com")
        assert a == b
        assert a != c


class TestLicenseClaims:
    def test_free_returns_starter_plan(self) -> None:
        from hexawyn.domain.models.license import LicenseClaims

        claims = LicenseClaims.free()
        assert claims.plan == "starter"

    def test_free_has_correct_defaults(self) -> None:
        from hexawyn.domain.models.license import LicenseClaims

        claims = LicenseClaims.free()
        assert claims.sub == "anonymous"
        assert claims.clusters_max == 1
        assert claims.users_max == 1
        assert claims.investigations_monthly == 50  # noqa: PLR2004
        assert claims.history_days == 7  # noqa: PLR2004
        assert claims.providers == ["vanilla"]
        assert claims.exp == 9999999999  # noqa: PLR2004
        assert claims.iat == 0

    def test_constructs_with_custom_values(self) -> None:
        from hexawyn.domain.models.license import LicenseClaims

        claims = LicenseClaims(
            sub="user-123",
            plan="team",
            clusters_max=3,
            users_max=5,
            investigations_monthly=500,
            history_days=90,
            providers=["vanilla", "aws", "gcp"],
            exp=9999999999,
            iat=1700000000,
        )
        assert claims.sub == "user-123"
        assert claims.plan == "team"
        assert claims.clusters_max == 3  # noqa: PLR2004
        assert claims.users_max == 5  # noqa: PLR2004
        assert claims.investigations_monthly == 500  # noqa: PLR2004
        assert claims.history_days == 90  # noqa: PLR2004
        assert claims.providers == ["vanilla", "aws", "gcp"]

    def test_equality(self) -> None:
        from hexawyn.domain.models.license import LicenseClaims

        a = LicenseClaims.free()
        b = LicenseClaims.free()
        c = LicenseClaims(
            sub="x",
            plan="team",
            clusters_max=3,
            users_max=5,
            investigations_monthly=500,
            history_days=90,
            providers=["vanilla"],
            exp=9999999999,
            iat=0,
        )
        assert a == b
        assert a != c
