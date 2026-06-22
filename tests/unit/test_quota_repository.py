from unittest.mock import MagicMock

from hexawyn.domain.models.quota import (
    FREE_MONTHLY_LIMIT,
    FREE_SLACK_LIMIT,
    SlackQuota,
    UsageQuota,
)
from hexawyn.infrastructure.memory.quota_repository import QuotaRepository


class TestQuotaRepository:
    def setup_method(self):
        self.mock_conn = MagicMock()
        self.repo = QuotaRepository(conn=self.mock_conn)

    def test_get_quota_returns_usage_quota_when_row_exists(self):
        self.mock_conn.execute.return_value.fetchone.return_value = (
            "uuid-123",
            "2026-06",
            23,
            50,
            3,
            5,
            "2026-06-01",
            "2026-06-22",
        )
        quota = self.repo.get_investigation_quota(month="2026-06")
        assert quota.month == "2026-06"
        assert quota.count == 23
        assert quota.limit == 50

    def test_get_quota_returns_default_when_no_row(self):
        self.mock_conn.execute.return_value.fetchone.return_value = None
        quota = self.repo.get_investigation_quota(month="2026-06")
        assert quota.month == "2026-06"
        assert quota.count == 0
        assert quota.limit == FREE_MONTHLY_LIMIT

    def test_get_slack_quota_returns_slack_quota(self):
        self.mock_conn.execute.return_value.fetchone.return_value = (
            "uuid-123", "2026-06", 10, 50, 3, 5, "2026-06-01", "2026-06-22",
        )
        quota = self.repo.get_slack_quota(month="2026-06")
        assert isinstance(quota, SlackQuota)
        assert quota.count == 3
        assert quota.limit == 5

    def test_get_slack_quota_returns_default_when_no_row(self):
        self.mock_conn.execute.return_value.fetchone.return_value = None
        quota = self.repo.get_slack_quota(month="2026-06")
        assert quota.count == 0
        assert quota.limit == FREE_SLACK_LIMIT

    def test_increment_investigation_calls_upsert(self):
        self.repo.increment_investigation(month="2026-06", limit=FREE_MONTHLY_LIMIT)
        self.mock_conn.execute.assert_called_once()

    def test_increment_slack_calls_upsert(self):
        self.repo.increment_slack(month="2026-06", limit=FREE_SLACK_LIMIT)
        self.mock_conn.execute.assert_called_once()

    def test_reset_calls_reset_sql(self):
        self.repo.reset(month="2026-06")
        self.mock_conn.execute.assert_called_once()
