from hexawyn.domain.models.quota import (
    UNLIMITED,
    LicenseTier,
    SlackQuota,
    UsageQuota,
)


class TestConstants:
    def test_unlimited_is_minus_one(self) -> None:
        assert UNLIMITED == -1


class TestLicenseTier:
    def test_has_three_tiers(self) -> None:
        tiers = [
            LicenseTier.STARTER,
            LicenseTier.TEAM,
            LicenseTier.SCALE_UP,
        ]
        assert len(tiers) == 3  # noqa: PLR2004


class TestUsageQuota:
    def test_default_limit_is_neutral_unlimited(self) -> None:
        quota = UsageQuota(month="2026-06", count=0)
        assert quota.limit == UNLIMITED

    def test_remaining_calculation(self) -> None:
        quota = UsageQuota(month="2026-06", count=23, limit=50)
        assert quota.remaining == 27  # noqa: PLR2004

    def test_remaining_never_negative(self) -> None:
        quota = UsageQuota(month="2026-06", count=55, limit=50)
        assert quota.remaining == 0

    def test_is_exceeded_when_count_equals_limit(self) -> None:
        quota = UsageQuota(month="2026-06", count=50, limit=50)
        assert quota.is_exceeded is True

    def test_is_exceeded_when_count_over_limit(self) -> None:
        quota = UsageQuota(month="2026-06", count=51, limit=50)
        assert quota.is_exceeded is True

    def test_is_not_exceeded_when_under_limit(self) -> None:
        quota = UsageQuota(month="2026-06", count=49, limit=50)
        assert quota.is_exceeded is False

    def test_unlimited_never_exceeded(self) -> None:
        quota = UsageQuota(month="2026-06", count=99999, limit=UNLIMITED)
        assert quota.is_exceeded is False

    def test_remaining_unlimited_when_unlimited(self) -> None:
        quota = UsageQuota(month="2026-06", count=99999, limit=UNLIMITED)
        assert quota.remaining == UNLIMITED

    def test_is_unlimited_property(self) -> None:
        quota = UsageQuota(month="2026-06", count=0, limit=UNLIMITED)
        assert quota.is_unlimited is True

    def test_is_not_unlimited_for_limited(self) -> None:
        quota = UsageQuota(month="2026-06", count=0, limit=50)
        assert quota.is_unlimited is False

    def test_month_format(self) -> None:
        quota = UsageQuota(month="2026-06", count=0)
        assert len(quota.month) == 7  # noqa: PLR2004
        assert quota.month[4] == "-"


class TestSlackQuota:
    def test_default_limit_is_neutral_unlimited(self) -> None:
        quota = SlackQuota(month="2026-06", count=0)
        assert quota.limit == UNLIMITED

    def test_is_exceeded_at_limit(self) -> None:
        quota = SlackQuota(month="2026-06", count=50, limit=50)
        assert quota.is_exceeded is True

    def test_is_not_exceeded_under_limit(self) -> None:
        quota = SlackQuota(month="2026-06", count=49, limit=50)
        assert quota.is_exceeded is False

    def test_unlimited_never_exceeded(self) -> None:
        quota = SlackQuota(month="2026-06", count=9999, limit=UNLIMITED)
        assert quota.is_exceeded is False

    def test_remaining_unlimited_when_unlimited(self) -> None:
        quota = SlackQuota(month="2026-06", count=5, limit=UNLIMITED)
        assert quota.remaining == UNLIMITED

    def test_remaining_calculation(self) -> None:
        quota = SlackQuota(month="2026-06", count=23, limit=50)
        assert quota.remaining == 27  # noqa: PLR2004

    def test_is_unlimited_property(self) -> None:
        quota = SlackQuota(month="2026-06", count=5, limit=UNLIMITED)
        assert quota.is_unlimited is True
