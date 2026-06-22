from pathlib import Path

import duckdb
import pytest
from hexawyn.domain.errors import QuotaExceededError
from hexawyn.domain.models.quota import (
    FREE_HISTORY_DAYS,
    FREE_MONTHLY_LIMIT,
    FREE_SLACK_LIMIT,
)
from hexawyn.infrastructure.config.quota_manager import (
    _get_current_month,
    check_quota,
    get_history_days,
    get_quota_display,
)
from hexawyn.infrastructure.memory.quota_repository import QuotaRepository

SCHEMA_PATH = (
    Path(__file__).parent.parent.parent / "src/hexawyn/infrastructure/memory/sql/schema.sql"
)


@pytest.fixture
def test_conn():
    conn = duckdb.connect(":memory:")
    conn.execute("INSTALL vss;")
    conn.execute("LOAD vss;")
    schema_sql = SCHEMA_PATH.read_text(encoding="utf-8")
    conn.execute(schema_sql)
    yield conn
    conn.close()


@pytest.fixture
def quota_repo(test_conn):
    return QuotaRepository(conn=test_conn)


class TestQuotaRepositoryIntegration:
    @pytest.mark.integration
    def test_get_quota_returns_default_when_no_row(self, quota_repo):
        quota = quota_repo.get_investigation_quota(month="2026-06")
        assert quota.month == "2026-06"
        assert quota.count == 0
        assert quota.limit == FREE_MONTHLY_LIMIT

    @pytest.mark.integration
    def test_increment_creates_row_on_first_call(self, quota_repo):
        quota_repo.increment_investigation(month="2026-06", limit=FREE_MONTHLY_LIMIT)
        quota = quota_repo.get_investigation_quota(month="2026-06")
        assert quota.count == 1

    @pytest.mark.integration
    def test_multiple_increments_accumulate(self, quota_repo):
        for _ in range(5):
            quota_repo.increment_investigation(
                month="2026-06",
                limit=FREE_MONTHLY_LIMIT,
            )
        quota = quota_repo.get_investigation_quota(month="2026-06")
        assert quota.count == 5

    @pytest.mark.integration
    def test_different_months_are_independent(self, quota_repo):
        quota_repo.increment_investigation(month="2026-06", limit=FREE_MONTHLY_LIMIT)
        quota_repo.increment_investigation(month="2026-06", limit=FREE_MONTHLY_LIMIT)
        quota_repo.increment_investigation(month="2026-07", limit=FREE_MONTHLY_LIMIT)

        june = quota_repo.get_investigation_quota(month="2026-06")
        july = quota_repo.get_investigation_quota(month="2026-07")

        assert june.count == 2
        assert july.count == 1

    @pytest.mark.integration
    def test_reset_sets_count_to_zero(self, quota_repo):
        for _ in range(10):
            quota_repo.increment_investigation(
                month="2026-06",
                limit=FREE_MONTHLY_LIMIT,
            )
        quota_repo.reset(month="2026-06")
        quota = quota_repo.get_investigation_quota(month="2026-06")
        assert quota.count == 0

    @pytest.mark.integration
    def test_slack_quota_independent_from_investigation_quota(self, quota_repo):
        quota_repo.increment_investigation(month="2026-06", limit=FREE_MONTHLY_LIMIT)
        quota_repo.increment_investigation(month="2026-06", limit=FREE_MONTHLY_LIMIT)
        quota_repo.increment_slack(month="2026-06", limit=FREE_SLACK_LIMIT)

        inv_quota = quota_repo.get_investigation_quota(month="2026-06")
        slack_quota = quota_repo.get_slack_quota(month="2026-06")

        assert inv_quota.count == 2
        assert slack_quota.count == 1

    @pytest.mark.integration
    def test_quota_exceeded_at_limit(self, quota_repo):
        for _ in range(FREE_MONTHLY_LIMIT):
            quota_repo.increment_investigation(
                month="2026-06",
                limit=FREE_MONTHLY_LIMIT,
            )
        quota = quota_repo.get_investigation_quota(month="2026-06")
        assert quota.is_exceeded is True
        assert quota.remaining == 0

    @pytest.mark.integration
    def test_slack_quota_exceeded_at_limit(self, quota_repo):
        for _ in range(FREE_SLACK_LIMIT):
            quota_repo.increment_slack(
                month="2026-06",
                limit=FREE_SLACK_LIMIT,
            )
        slack_quota = quota_repo.get_slack_quota(month="2026-06")
        assert slack_quota.is_exceeded is True
        assert slack_quota.remaining == 0


class TestQuotaManagerIntegration:
    @pytest.mark.integration
    def test_check_quota_passes_with_real_duckdb(self, test_conn, monkeypatch):
        monkeypatch.setattr(
            "hexawyn.infrastructure.config.quota_manager.get_connection",
            lambda: test_conn,
        )
        check_quota()

    @pytest.mark.integration
    def test_increment_then_check_quota_with_real_duckdb(self, test_conn, monkeypatch):
        monkeypatch.setattr(
            "hexawyn.infrastructure.config.quota_manager.get_connection",
            lambda: test_conn,
        )
        repo = QuotaRepository(conn=test_conn)
        month = _get_current_month()

        for _ in range(FREE_MONTHLY_LIMIT):
            repo.increment_investigation(month=month, limit=FREE_MONTHLY_LIMIT)

        with pytest.raises(QuotaExceededError) as exc_info:
            check_quota()
        assert exc_info.value.used == FREE_MONTHLY_LIMIT
        assert exc_info.value.limit == FREE_MONTHLY_LIMIT

    @pytest.mark.integration
    def test_get_history_days_free_tier(self, monkeypatch):
        monkeypatch.delenv("HEXAWYN_LICENSE_KEY", raising=False)
        assert get_history_days() == FREE_HISTORY_DAYS

    @pytest.mark.integration
    def test_get_quota_display_with_real_duckdb(self, test_conn, monkeypatch):
        monkeypatch.setattr(
            "hexawyn.infrastructure.config.quota_manager.get_connection",
            lambda: test_conn,
        )
        repo = QuotaRepository(conn=test_conn)
        month = _get_current_month()

        for _ in range(10):
            repo.increment_investigation(month=month, limit=FREE_MONTHLY_LIMIT)

        display = get_quota_display()
        assert "10" in display
        assert "50" in display
        assert "40" in display
