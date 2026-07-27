from hexawyn.domain.models.quota import (
    PRO_HISTORY_DAYS,
    STARTER_HISTORY_DAYS,
    STARTER_MONTHLY_LIMIT,
    STARTER_SLACK_LIMIT,
    UNLIMITED,
    LicenseTier,
    SlackQuota,
    UsageQuota,
    get_history_days,
    get_investigation_limit,
    get_slack_limit,
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


class TestGetInvestigationLimit:
    def test_starter_is_50(self) -> None:
        assert get_investigation_limit(LicenseTier.STARTER) == 200  # noqa: PLR2004

    def test_team_is_500(self) -> None:
        assert get_investigation_limit(LicenseTier.TEAM) == 500  # noqa: PLR2004

    def test_scale_up_is_unlimited(self) -> None:
        assert get_investigation_limit(LicenseTier.SCALE_UP) == UNLIMITED

    def test_backward_compat_starter_monthly_limit(self) -> None:
        assert STARTER_MONTHLY_LIMIT == 200  # noqa: PLR2004


class TestGetSlackLimit:
    def test_starter_is_5(self) -> None:
        assert get_slack_limit(LicenseTier.STARTER) == 50  # noqa: PLR2004

    def test_team_is_unlimited(self) -> None:
        assert get_slack_limit(LicenseTier.TEAM) == UNLIMITED

    def test_scale_up_is_unlimited(self) -> None:
        assert get_slack_limit(LicenseTier.SCALE_UP) == UNLIMITED

    def test_backward_compat_starter_slack_limit(self) -> None:
        assert STARTER_SLACK_LIMIT == 50  # noqa: PLR2004


class TestGetHistoryDays:
    def test_starter_is_7(self) -> None:
        assert get_history_days(LicenseTier.STARTER) == 30  # noqa: PLR2004

    def test_team_is_90(self) -> None:
        assert get_history_days(LicenseTier.TEAM) == 90  # noqa: PLR2004

    def test_scale_up_is_unlimited(self) -> None:
        assert get_history_days(LicenseTier.SCALE_UP) == UNLIMITED

    def test_backward_compat_starter_history_days(self) -> None:
        assert STARTER_HISTORY_DAYS == 30  # noqa: PLR2004

    def test_backward_compat_pro_history_days(self) -> None:
        assert PRO_HISTORY_DAYS == 90  # noqa: PLR2004


class TestUsageQuota:
    def test_default_limit_uses_starter_tier(self) -> None:
        quota = UsageQuota(month="2026-06", count=0)
        assert quota.limit == 200  # noqa: PLR2004

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

    def test_is_not_unlimited_for_starter(self) -> None:
        quota = UsageQuota(month="2026-06", count=0, limit=50)
        assert quota.is_unlimited is False

    def test_month_format(self) -> None:
        quota = UsageQuota(month="2026-06", count=0)
        assert len(quota.month) == 7  # noqa: PLR2004
        assert quota.month[4] == "-"


class TestSlackQuota:
    def test_default_limit_uses_starter_tier(self) -> None:
        quota = SlackQuota(month="2026-06", count=0)
        assert quota.limit == 50  # noqa: PLR2004

    def test_is_exceeded_at_limit(self) -> None:
        quota = SlackQuota(month="2026-06", count=50, limit=50)
        assert quota.is_exceeded is True

    def test_is_not_exceeded_under_limit(self) -> None:
        quota = SlackQuota(month="2026-06", count=49, limit=50)
        assert quota.is_exceeded is False

    def test_team_unlimited(self) -> None:
        quota = SlackQuota(month="2026-06", count=9999, limit=UNLIMITED)
        assert quota.is_exceeded is False
