import pytest

from hexawyn.domain.models.quota import (
    FREE_HISTORY_DAYS,
    FREE_MONTHLY_LIMIT,
    FREE_SLACK_LIMIT,
    PRO_HISTORY_DAYS,
    UNLIMITED,
    SlackQuota,
    UsageQuota,
)


class TestConstants:
    def test_free_monthly_limit_is_50(self):
        assert FREE_MONTHLY_LIMIT == 50

    def test_free_slack_limit_is_5(self):
        assert FREE_SLACK_LIMIT == 5

    def test_free_history_days_is_7(self):
        assert FREE_HISTORY_DAYS == 7

    def test_pro_history_days_is_90(self):
        assert PRO_HISTORY_DAYS == 90

    def test_unlimited_is_minus_one(self):
        assert UNLIMITED == -1


class TestUsageQuota:
    def test_default_limit_is_50(self):
        quota = UsageQuota(month="2026-06", count=0)
        assert quota.limit == FREE_MONTHLY_LIMIT

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

    def test_remaining_is_unlimited_when_pro(self):
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


class TestUsageQuotaSlack:
    def test_slack_quota_default_limit(self):
        quota = SlackQuota(month="2026-06", count=0)
        assert quota.limit == FREE_SLACK_LIMIT

    def test_slack_quota_exceeded(self):
        quota = SlackQuota(month="2026-06", count=5, limit=5)
        assert quota.is_exceeded is True

    def test_slack_quota_not_exceeded(self):
        quota = SlackQuota(month="2026-06", count=4, limit=5)
        assert quota.is_exceeded is False
