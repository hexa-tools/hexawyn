from pathlib import Path

import duckdb

from hexawyn.application.ports.driven.quota_port import QuotaStorePort
from hexawyn.domain.models.quota import (
    LicenseTier,
    SlackQuota,
    UsageQuota,
    get_investigation_limit,
    get_slack_limit,
)

SQL_DIR = Path(__file__).parent / "sql"


def _load_sql(filename: str) -> str:
    return (SQL_DIR / filename).read_text(encoding="utf-8")


class QuotaRepository(QuotaStorePort):
    """
    Repository for usage quota in DuckDB.
    Handles both investigation quota and Slack alert quota.
    Tier-aware: limits come from LicenseTier constants.
    """

    def __init__(self, conn: duckdb.DuckDBPyConnection) -> None:
        self._conn = conn

    def get_investigation_quota(self, month: str) -> UsageQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return UsageQuota(
                month=month,
                count=0,
                limit=get_investigation_limit(LicenseTier.FREE),
            )

        return UsageQuota(
            month=str(row[1]),
            count=int(row[3]),
            limit=int(row[4]),
        )

    def get_slack_quota(self, month: str) -> SlackQuota:
        row = self._conn.execute(_load_sql("get_quota.sql"), [month]).fetchone()

        if row is None:
            return SlackQuota(
                month=month,
                count=0,
                limit=get_slack_limit(LicenseTier.FREE),
            )

        return SlackQuota(
            month=str(row[1]),
            count=int(row[5]),
            limit=int(row[6]),
        )

    def increment_investigation(
        self,
        month: str,
        tier: LicenseTier,
        limit: int,
    ) -> None:
        self._conn.execute(
            _load_sql("upsert_investigation_quota.sql"),
            [month, tier.value, limit],
        )

    def increment_slack(
        self,
        month: str,
        tier: LicenseTier,
        limit: int,
    ) -> None:
        self._conn.execute(
            _load_sql("upsert_slack_quota.sql"),
            [month, tier.value, limit],
        )

    def reset(self, month: str) -> None:
        self._conn.execute(_load_sql("reset_quota.sql"), [month])
