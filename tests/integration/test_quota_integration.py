from pathlib import Path

import duckdb
import pytest
from hexawyn.domain.errors import QuotaExceededError
from hexawyn.domain.models.quota import (
    UNLIMITED,
    LicenseTier,
    get_history_days,
    get_investigation_limit,
    get_slack_limit,
)
from hexawyn.infrastructure.config.quota_manager import (
    _get_current_month,
    check_quota,
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


def _fill_investigations(repo: QuotaRepository, month: str, tier: LicenseTier, count: int) -> None:
    limit = get_investigation_limit(tier)
    for _ in range(count):
        repo.increment_investigation(month=month, tier=tier, limit=limit)


class TestQuotaRepositoryIntegration:
    @pytest.mark.integration
    def test_get_quota_returns_default_when_no_row(self, repo: QuotaRepository) -> None:
        quota = repo.get_investigation_quota(month="2026-06")
        assert quota.month == "2026-06"
        assert quota.count == 0
        assert quota.limit == get_investigation_limit(LicenseTier.FREE)

    @pytest.mark.integration
    def test_increment_creates_row_on_first_call(self, repo: QuotaRepository) -> None:
        repo.increment_investigation(
            month="2026-06",
            tier=LicenseTier.FREE,
            limit=get_investigation_limit(LicenseTier.FREE),
        )
        quota = repo.get_investigation_quota(month="2026-06")
        assert quota.count == 1

    @pytest.mark.integration
    def test_multiple_increments_accumulate(self, repo: QuotaRepository) -> None:
        tier = LicenseTier.FREE
        limit = get_investigation_limit(tier)
        for _ in range(5):
            repo.increment_investigation(month="2026-06", tier=tier, limit=limit)
        quota = repo.get_investigation_quota(month="2026-06")
        assert quota.count == 5

    @pytest.mark.integration
    def test_different_months_are_independent(self, repo: QuotaRepository) -> None:
        tier = LicenseTier.FREE
        limit = get_investigation_limit(tier)
        repo.increment_investigation(month="2026-06", tier=tier, limit=limit)
        repo.increment_investigation(month="2026-06", tier=tier, limit=limit)
        repo.increment_investigation(month="2026-07", tier=tier, limit=limit)

        june = repo.get_investigation_quota(month="2026-06")
        july = repo.get_investigation_quota(month="2026-07")
        assert june.count == 2
        assert july.count == 1

    @pytest.mark.integration
    def test_reset_sets_count_to_zero(self, repo: QuotaRepository) -> None:
        tier = LicenseTier.FREE
        limit = get_investigation_limit(tier)
        for _ in range(10):
            repo.increment_investigation(month="2026-06", tier=tier, limit=limit)
        repo.reset(month="2026-06")
        quota = repo.get_investigation_quota(month="2026-06")
        assert quota.count == 0

    @pytest.mark.integration
    def test_slack_quota_independent_from_investigation(self, repo: QuotaRepository) -> None:
        repo.increment_investigation(
            month="2026-06",
            tier=LicenseTier.FREE,
            limit=get_investigation_limit(LicenseTier.FREE),
        )
        repo.increment_investigation(
            month="2026-06",
            tier=LicenseTier.FREE,
            limit=get_investigation_limit(LicenseTier.FREE),
        )
        repo.increment_slack(
            month="2026-06",
            tier=LicenseTier.FREE,
            limit=get_slack_limit(LicenseTier.FREE),
        )

        inv = repo.get_investigation_quota(month="2026-06")
        slack = repo.get_slack_quota(month="2026-06")
        assert inv.count == 2
        assert slack.count == 1

    @pytest.mark.integration
    def test_quota_exceeded_at_limit(self, repo: QuotaRepository) -> None:
        limit = get_investigation_limit(LicenseTier.FREE)
        _fill_investigations(repo, "2026-06", LicenseTier.FREE, limit)
        quota = repo.get_investigation_quota(month="2026-06")
        assert quota.is_exceeded is True
        assert quota.remaining == 0

    @pytest.mark.integration
    def test_slack_quota_exceeded_at_limit(self, repo: QuotaRepository) -> None:
        tier = LicenseTier.FREE
        limit = get_slack_limit(tier)
        for _ in range(limit):
            repo.increment_slack(month="2026-06", tier=tier, limit=limit)
        slack = repo.get_slack_quota(month="2026-06")
        assert slack.is_exceeded is True
        assert slack.remaining == 0


class TestTierSpecificIntegration:
    @pytest.mark.integration
    def test_free_tier_quota_full_cycle(self, repo: QuotaRepository) -> None:
        """Real DuckDB — 50 increments → is_exceeded."""
        limit = get_investigation_limit(LicenseTier.FREE)
        _fill_investigations(repo, "2026-06", LicenseTier.FREE, limit)
        quota = repo.get_investigation_quota(month="2026-06")
        assert quota.is_exceeded is True
        assert quota.limit == 50

    @pytest.mark.integration
    def test_dev_tier_quota_full_cycle(self, repo: QuotaRepository) -> None:
        """Real DuckDB — 200 increments → is_exceeded."""
        limit = get_investigation_limit(LicenseTier.DEV)
        _fill_investigations(repo, "2026-06", LicenseTier.DEV, limit)
        quota = repo.get_investigation_quota(month="2026-06")
        assert quota.is_exceeded is True
        assert quota.limit == 200

    @pytest.mark.integration
    def test_different_tiers_different_limits(self, repo: QuotaRepository) -> None:
        """Free=50, Dev=200, Startup=500 all enforced correctly."""
        repo.increment_investigation(
            month="2026-06",
            tier=LicenseTier.DEV,
            limit=get_investigation_limit(LicenseTier.DEV),
        )
        repo.increment_investigation(
            month="2026-07",
            tier=LicenseTier.STARTUP,
            limit=get_investigation_limit(LicenseTier.STARTUP),
        )

        q_dev = repo.get_investigation_quota(month="2026-06")
        q_startup = repo.get_investigation_quota(month="2026-07")

        assert q_dev.limit == 200
        assert q_startup.limit == 500

    @pytest.mark.integration
    def test_slack_quota_independent_from_investigation(self, repo: QuotaRepository) -> None:
        repo.increment_investigation(
            month="2026-06",
            tier=LicenseTier.DEV,
            limit=get_investigation_limit(LicenseTier.DEV),
        )
        repo.increment_slack(
            month="2026-06",
            tier=LicenseTier.DEV,
            limit=get_slack_limit(LicenseTier.DEV),
        )

        inv = repo.get_investigation_quota(month="2026-06")
        slack = repo.get_slack_quota(month="2026-06")

        assert inv.count == 1
        assert slack.count == 1
        assert inv.limit != slack.limit

    @pytest.mark.integration
    def test_history_days_by_tier(self) -> None:
        """Free=7, Dev=30, Startup=90, Scale-up=unlimited."""
        assert get_history_days(LicenseTier.FREE) == 7
        assert get_history_days(LicenseTier.DEV) == 30
        assert get_history_days(LicenseTier.STARTUP) == 90
        assert get_history_days(LicenseTier.SCALE_UP) == UNLIMITED


class TestQuotaManagerIntegration:
    @pytest.mark.integration
    def test_check_quota_passes_with_real_duckdb(
        self, test_conn: duckdb.DuckDBPyConnection, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr(
            "hexawyn.infrastructure.config.quota_manager.get_connection",
            lambda: test_conn,
        )
        check_quota()

    @pytest.mark.integration
    def test_increment_then_check_quota_with_real_duckdb(
        self, test_conn: duckdb.DuckDBPyConnection, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr(
            "hexawyn.infrastructure.config.quota_manager.get_connection",
            lambda: test_conn,
        )
        repo = QuotaRepository(conn=test_conn)
        month = _get_current_month()
        limit = get_investigation_limit(LicenseTier.FREE)

        for _ in range(limit):
            repo.increment_investigation(
                month=month,
                tier=LicenseTier.FREE,
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
            "hexawyn.infrastructure.config.quota_manager.get_connection",
            lambda: test_conn,
        )
        repo = QuotaRepository(conn=test_conn)
        month = _get_current_month()
        limit = get_investigation_limit(LicenseTier.FREE)

        for _ in range(10):
            repo.increment_investigation(
                month=month,
                tier=LicenseTier.FREE,
                limit=limit,
            )

        display = get_quota_display()
        assert "10" in display
        assert "50" in display
        assert "40" in display
