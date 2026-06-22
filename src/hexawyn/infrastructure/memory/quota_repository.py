from pathlib import Path

import duckdb

from hexawyn.domain.models.quota import (
    FREE_MONTHLY_LIMIT,
    FREE_SLACK_LIMIT,
    SlackQuota,
    UsageQuota,
)

SQL_DIR = Path(__file__).parent / "sql"


def _load_sql(filename: str) -> str:
    """Load SQL from file. All SQL lives in sql/ — never inline."""
    return (SQL_DIR / filename).read_text(encoding="utf-8")


class QuotaRepository:
    """
    Repository for usage quota persistence in DuckDB.
    Single responsibility: read/write usage_quota table.

    Two quota types:
    - Investigation quota: 50/month Free, unlimited Pro
    - Slack quota: 5/month Free, unlimited Pro
    """

    def __init__(self, conn: duckdb.DuckDBPyConnection) -> None:
        self._conn = conn

    def get_investigation_quota(self, month: str) -> UsageQuota:
        row = self._conn.execute(
            _load_sql("get_quota.sql"), [month]
        ).fetchone()

        if row is None:
            return UsageQuota(month=month, count=0, limit=FREE_MONTHLY_LIMIT)

        return UsageQuota(
            month=str(row[1]),
            count=int(row[2]),
            limit=int(row[3]),
        )

    def get_slack_quota(self, month: str) -> SlackQuota:
        row = self._conn.execute(
            _load_sql("get_quota.sql"), [month]
        ).fetchone()

        if row is None:
            return SlackQuota(month=month, count=0, limit=FREE_SLACK_LIMIT)

        return SlackQuota(
            month=str(row[1]),
            count=int(row[4]),
            limit=int(row[5]),
        )

    def increment_investigation(self, month: str, limit: int = FREE_MONTHLY_LIMIT) -> None:
        self._conn.execute(
            _load_sql("upsert_investigation_quota.sql"), [month, limit]
        )

    def increment_slack(self, month: str, limit: int = FREE_SLACK_LIMIT) -> None:
        self._conn.execute(
            _load_sql("upsert_slack_quota.sql"), [month, limit]
        )

    def reset(self, month: str) -> None:
        self._conn.execute(_load_sql("reset_quota.sql"), [month])
