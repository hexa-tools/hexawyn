from unittest.mock import MagicMock

from hexawyn.domain.models.quota import UNLIMITED, LicenseTier, SlackQuota, UsageQuota
from hexawyn.infrastructure.memory.quota_repository import QuotaRepository


class TestQuotaRepository:
    def setup_method(self) -> None:
        self.mock_conn = MagicMock()
        self.repo = QuotaRepository(conn=self.mock_conn)

    def test_get_investigation_quota_defaults_to_neutral_when_no_row(self) -> None:
        self.mock_conn.execute.return_value.fetchone.return_value = None
        quota = self.repo.get_investigation_quota(month="2026-06")
        assert isinstance(quota, UsageQuota)
        assert quota.month == "2026-06"
        assert quota.count == 0
        assert quota.limit == UNLIMITED

    def test_get_investigation_quota_returns_row_when_exists(self) -> None:
        self.mock_conn.execute.return_value.fetchone.return_value = (
            "uuid-123",
            "2026-06",
            "dev",
            23,
            200,
            3,
            50,
            "2026-06-01",
            "2026-06-22",
        )
        quota = self.repo.get_investigation_quota(month="2026-06")
        assert quota.month == "2026-06"
        assert quota.count == 23  # noqa: PLR2004
        assert quota.limit == 200  # noqa: PLR2004

    def test_get_slack_quota_defaults_to_neutral_when_no_row(self) -> None:
        self.mock_conn.execute.return_value.fetchone.return_value = None
        quota = self.repo.get_slack_quota(month="2026-06")
        assert isinstance(quota, SlackQuota)
        assert quota.count == 0
        assert quota.limit == UNLIMITED

    def test_get_slack_quota_returns_row_when_exists(self) -> None:
        self.mock_conn.execute.return_value.fetchone.return_value = (
            "uuid-123",
            "2026-06",
            "dev",
            10,
            200,
            3,
            50,
            "2026-06-01",
            "2026-06-22",
        )
        quota = self.repo.get_slack_quota(month="2026-06")
        assert isinstance(quota, SlackQuota)
        assert quota.count == 3  # noqa: PLR2004
        assert quota.limit == 50  # noqa: PLR2004

    def test_increment_investigation_calls_upsert(self) -> None:
        self.repo.increment_investigation(
            month="2026-06",
            tier=LicenseTier.TEAM,
            limit=200,
        )
        self.mock_conn.execute.assert_called_once()

    def test_increment_slack_calls_upsert(self) -> None:
        self.repo.increment_slack(
            month="2026-06",
            tier=LicenseTier.STARTER,
            limit=5,
        )
        self.mock_conn.execute.assert_called_once()

    def test_reset_calls_reset_sql(self) -> None:
        self.repo.reset(month="2026-06")
        self.mock_conn.execute.assert_called_once()
