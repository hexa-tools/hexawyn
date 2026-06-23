from hexawyn.domain.models.quota import (
    FREE_HISTORY_DAYS,
    FREE_MONTHLY_LIMIT,
    FREE_SLACK_LIMIT,
    PRO_HISTORY_DAYS,
    UNLIMITED,
    LicenseTier,
    SlackQuota,
    UsageQuota,
    get_history_days,
    get_investigation_limit,
    get_slack_limit,
)


class TestConstants:
    def test_unlimited_is_minus_one(self):
        assert UNLIMITED == -1


class TestLicenseTier:
    def test_has_five_tiers(self):
        tiers = [
            LicenseTier.FREE,
            LicenseTier.DEV,
            LicenseTier.STARTUP,
            LicenseTier.SCALE_UP,
            LicenseTier.ENTERPRISE,
        ]
        assert len(tiers) == 5


class TestGetInvestigationLimit:
    def test_free_is_50(self):
        assert get_investigation_limit(LicenseTier.FREE) == 50

    def test_dev_is_200(self):
        assert get_investigation_limit(LicenseTier.DEV) == 200

    def test_startup_is_500(self):
        assert get_investigation_limit(LicenseTier.STARTUP) == 500

    def test_scale_up_is_unlimited(self):
        assert get_investigation_limit(LicenseTier.SCALE_UP) == UNLIMITED

    def test_enterprise_is_unlimited(self):
        assert get_investigation_limit(LicenseTier.ENTERPRISE) == UNLIMITED

    def test_backward_compat_free_monthly_limit(self):
        assert FREE_MONTHLY_LIMIT == 50


class TestGetSlackLimit:
    def test_free_is_5(self):
        assert get_slack_limit(LicenseTier.FREE) == 5

    def test_dev_is_50(self):
        assert get_slack_limit(LicenseTier.DEV) == 50

    def test_startup_is_unlimited(self):
        assert get_slack_limit(LicenseTier.STARTUP) == UNLIMITED

    def test_scale_up_is_unlimited(self):
        assert get_slack_limit(LicenseTier.SCALE_UP) == UNLIMITED

    def test_backward_compat_free_slack_limit(self):
        assert FREE_SLACK_LIMIT == 5


class TestGetHistoryDays:
    def test_free_is_7(self):
        assert get_history_days(LicenseTier.FREE) == 7

    def test_dev_is_30(self):
        assert get_history_days(LicenseTier.DEV) == 30

    def test_startup_is_90(self):
        assert get_history_days(LicenseTier.STARTUP) == 90

    def test_scale_up_is_unlimited(self):
        assert get_history_days(LicenseTier.SCALE_UP) == UNLIMITED

    def test_enterprise_is_unlimited(self):
        assert get_history_days(LicenseTier.ENTERPRISE) == UNLIMITED

    def test_backward_compat_free_history_days(self):
        assert FREE_HISTORY_DAYS == 7

    def test_backward_compat_pro_history_days(self):
        assert PRO_HISTORY_DAYS == 90


class TestUsageQuota:
    def test_default_limit_uses_free_tier(self):
        quota = UsageQuota(month="2026-06", count=0)
        assert quota.limit == 50

    def test_remaining_calculation(self):
        quota = UsageQuota(month="2026-06", count=23, limit=50)
        assert quota.remaining == 27

    def test_remaining_never_negative(self):
        quota = UsageQuota(month="2026-06", count=55, limit=50)
        assert quota.remaining == 0

    def test_is_exceeded_when_count_equals_limit(self):
        quota = UsageQuota(month="2026-06", count=50, limit=50)
        assert quota.is_exceeded is True

    def test_is_exceeded_when_count_over_limit(self):
        quota = UsageQuota(month="2026-06", count=51, limit=50)
        assert quota.is_exceeded is True

    def test_is_not_exceeded_when_under_limit(self):
        quota = UsageQuota(month="2026-06", count=49, limit=50)
        assert quota.is_exceeded is False

    def test_unlimited_never_exceeded(self):
        quota = UsageQuota(month="2026-06", count=99999, limit=UNLIMITED)
        assert quota.is_exceeded is False

    def test_remaining_unlimited_when_unlimited(self):
        quota = UsageQuota(month="2026-06", count=99999, limit=UNLIMITED)
        assert quota.remaining == UNLIMITED

    def test_is_unlimited_property(self):
        quota = UsageQuota(month="2026-06", count=0, limit=UNLIMITED)
        assert quota.is_unlimited is True

    def test_is_not_unlimited_for_free(self):
        quota = UsageQuota(month="2026-06", count=0, limit=50)
        assert quota.is_unlimited is False

    def test_month_format(self):
        quota = UsageQuota(month="2026-06", count=0)
        assert len(quota.month) == 7
        assert quota.month[4] == "-"


class TestSlackQuota:
    def test_default_limit_uses_free_tier(self):
        quota = SlackQuota(month="2026-06", count=0)
        assert quota.limit == 5

    def test_is_exceeded_at_limit(self):
        quota = SlackQuota(month="2026-06", count=5, limit=5)
        assert quota.is_exceeded is True

    def test_is_not_exceeded_under_limit(self):
        quota = SlackQuota(month="2026-06", count=4, limit=5)
        assert quota.is_exceeded is False

    def test_startup_unlimited(self):
        quota = SlackQuota(month="2026-06", count=9999, limit=UNLIMITED)
        assert quota.is_exceeded is False
