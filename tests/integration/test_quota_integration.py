from pathlib import Path

import duckdb
import pytest
from hexawyn.domain.errors import QuotaExceededError
from hexawyn.domain.models.quota import UNLIMITED, LicenseTier
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
def test_conn() -> duckdb.DuckDBPyConnection:
    conn = duckdb.connect(":memory:")
    conn.execute("INSTALL vss;")
    conn.execute("LOAD vss;")
    schema_sql = SCHEMA_PATH.read_text(encoding="utf-8")
    conn.execute(schema_sql)
    yield conn
    conn.close()


@pytest.fixture
def repo(test_conn: duckdb.DuckDBPyConnection) -> QuotaRepository:
    return QuotaRepository(conn=test_conn)


def _fill_investigations(repo: QuotaRepository, month: str, limit: int, count: int) -> None:
    for _ in range(count):
        repo.increment_investigation(month=month, tier=LicenseTier.STARTER, limit=limit)


class TestQuotaRepositoryIntegration:
    @pytest.mark.integration
    def test_get_quota_returns_neutral_default_when_no_row(self, repo: QuotaRepository) -> None:
        quota = repo.get_investigation_quota(month="2026-06")
        assert quota.month == "2026-06"
        assert quota.count == 0
        assert quota.limit == UNLIMITED

    @pytest.mark.integration
    def test_increment_creates_row_on_first_call(self, repo: QuotaRepository) -> None:
        repo.increment_investigation(
            month="2026-06",
            tier=LicenseTier.STARTER,
            limit=50,
        )
        quota = repo.get_investigation_quota(month="2026-06")
        assert quota.count == 1

    @pytest.mark.integration
    def test_multiple_increments_accumulate(self, repo: QuotaRepository) -> None:
        for _ in range(5):
            repo.increment_investigation(month="2026-06", tier=LicenseTier.STARTER, limit=50)
        quota = repo.get_investigation_quota(month="2026-06")
        assert quota.count == 5  # noqa: PLR2004

    @pytest.mark.integration
    def test_different_months_are_independent(self, repo: QuotaRepository) -> None:
        repo.increment_investigation(month="2026-06", tier=LicenseTier.STARTER, limit=50)
        repo.increment_investigation(month="2026-06", tier=LicenseTier.STARTER, limit=50)
        repo.increment_investigation(month="2026-07", tier=LicenseTier.STARTER, limit=50)

        june = repo.get_investigation_quota(month="2026-06")
        july = repo.get_investigation_quota(month="2026-07")
        assert june.count == 2  # noqa: PLR2004
        assert july.count == 1

    @pytest.mark.integration
    def test_reset_sets_count_to_zero(self, repo: QuotaRepository) -> None:
        for _ in range(10):
            repo.increment_investigation(month="2026-06", tier=LicenseTier.STARTER, limit=50)
        repo.reset(month="2026-06")
        quota = repo.get_investigation_quota(month="2026-06")
        assert quota.count == 0

    @pytest.mark.integration
    def test_slack_quota_independent_from_investigation(self, repo: QuotaRepository) -> None:
        repo.increment_investigation(month="2026-06", tier=LicenseTier.STARTER, limit=50)
        repo.increment_investigation(month="2026-06", tier=LicenseTier.STARTER, limit=50)
        repo.increment_slack(month="2026-06", tier=LicenseTier.STARTER, limit=50)

        inv = repo.get_investigation_quota(month="2026-06")
        slack = repo.get_slack_quota(month="2026-06")
        assert inv.count == 2  # noqa: PLR2004
        assert slack.count == 1

    @pytest.mark.integration
    def test_quota_exceeded_at_limit(self, repo: QuotaRepository) -> None:
        limit = 5
        _fill_investigations(repo, "2026-06", limit, limit)
        quota = repo.get_investigation_quota(month="2026-06")
        assert quota.is_exceeded is True
        assert quota.remaining == 0

    @pytest.mark.integration
    def test_slack_quota_exceeded_at_limit(self, repo: QuotaRepository) -> None:
        limit = 5
        for _ in range(limit):
            repo.increment_slack(month="2026-06", tier=LicenseTier.STARTER, limit=limit)
        slack = repo.get_slack_quota(month="2026-06")
        assert slack.is_exceeded is True
        assert slack.remaining == 0


class TestExplicitLimitPersistence:
    @pytest.mark.integration
    def test_full_cycle_reaches_exceeded(self, repo: QuotaRepository) -> None:
        """Real DuckDB — an explicit limit increments to is_exceeded."""
        limit = 5
        _fill_investigations(repo, "2026-06", limit, limit)
        quota = repo.get_investigation_quota(month="2026-06")
        assert quota.is_exceeded is True
        assert quota.limit == limit

    @pytest.mark.integration
    def test_distinct_rows_keep_their_own_limit(self, repo: QuotaRepository) -> None:
        """Each usage row persists its own limit (no shared tier grid)."""
        repo.increment_investigation(month="2026-06", tier=LicenseTier.STARTER, limit=5)
        repo.increment_investigation(month="2026-07", tier=LicenseTier.TEAM, limit=10)

        q_june = repo.get_investigation_quota(month="2026-06")
        q_july = repo.get_investigation_quota(month="2026-07")

        assert q_june.limit == 5  # noqa: PLR2004
        assert q_july.limit == 10  # noqa: PLR2004
        assert q_june.limit != q_july.limit

    @pytest.mark.integration
    def test_slack_quota_independent_from_investigation(self, repo: QuotaRepository) -> None:
        repo.increment_investigation(month="2026-06", tier=LicenseTier.TEAM, limit=50)
        repo.increment_slack(month="2026-06", tier=LicenseTier.TEAM, limit=5)

        inv = repo.get_investigation_quota(month="2026-06")
        slack = repo.get_slack_quota(month="2026-06")

        assert inv.count == 1
        assert slack.count == 1
        assert inv.limit != slack.limit

    @pytest.mark.integration
    def test_history_days_is_neutral_unlimited(self) -> None:
        """No hardcoded tiered retention — neutral keeps the full window."""
        assert get_history_days() == UNLIMITED


class TestQuotaManagerIntegration:
    @pytest.mark.integration
    def test_check_quota_passes_with_real_duckdb(
        self, test_conn: duckdb.DuckDBPyConnection, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr(
            "hexawyn.infrastructure.config.quota_manager._store",
            QuotaRepository(conn=test_conn),
        )
        check_quota()

    @pytest.mark.integration
    def test_increment_then_check_quota_with_real_duckdb(
        self, test_conn: duckdb.DuckDBPyConnection, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr(
            "hexawyn.infrastructure.config.quota_manager._store",
            QuotaRepository(conn=test_conn),
        )
        repo = QuotaRepository(conn=test_conn)
        month = _get_current_month()
        limit = 5

        for _ in range(limit):
            repo.increment_investigation(
                month=month,
                tier=LicenseTier.STARTER,
                limit=limit,
            )

        with pytest.raises(QuotaExceededError) as exc_info:
            check_quota()
        assert exc_info.value.used == limit
        assert exc_info.value.limit == limit

    @pytest.mark.integration
    def test_get_quota_display_with_real_duckdb(
        self, test_conn: duckdb.DuckDBPyConnection, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr(
            "hexawyn.infrastructure.config.quota_manager._store",
            QuotaRepository(conn=test_conn),
        )
        monkeypatch.setattr(
            "hexawyn.infrastructure.config.quota_manager._get_current_tier",
            lambda: LicenseTier.STARTER,
        )
        repo = QuotaRepository(conn=test_conn)
        month = _get_current_month()
        limit = 50

        for _ in range(10):
            repo.increment_investigation(
                month=month,
                tier=LicenseTier.STARTER,
                limit=limit,
            )

        display = get_quota_display()
        assert "10" in display
        assert str(limit) in display
        assert str(limit - 10) in display
