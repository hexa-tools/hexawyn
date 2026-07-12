from __future__ import annotations

import json
from collections.abc import Sequence
from datetime import UTC, datetime
from typing import TYPE_CHECKING

from hexawyn.application.ports.driven.schedule_store_port import ScheduleStorePort
from hexawyn.domain.models.schedule import CheckResult, CronCheck

if TYPE_CHECKING:
    from duckdb import DuckDBPyConnection


class DuckDBScheduleStore(ScheduleStorePort):
    """Persiste définitions + historique dans DuckDB."""

    def __init__(self, connection: DuckDBPyConnection) -> None:
        self._conn = connection
        self._ensure_schema()

    def _ensure_schema(self) -> None:
        self._conn.execute("""
            CREATE TABLE IF NOT EXISTS schedule_checks (
                name TEXT PRIMARY KEY,
                schedule TEXT NOT NULL,
                use_case TEXT NOT NULL,
                params TEXT DEFAULT '{}',
                enabled BOOLEAN DEFAULT TRUE,
                notify_policy TEXT DEFAULT 'on_change',
                destinations TEXT DEFAULT '["slack"]',
                timeout_seconds INTEGER DEFAULT 300
            )
        """)
        self._conn.execute("""
            CREATE TABLE IF NOT EXISTS schedule_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                check_name TEXT NOT NULL,
                phase TEXT NOT NULL,
                started_at TEXT NOT NULL,
                finished_at TEXT,
                duration_ms INTEGER,
                summary TEXT DEFAULT '',
                payload_digest TEXT NOT NULL,
                changed BOOLEAN DEFAULT FALSE,
                error_message TEXT,
                notified BOOLEAN DEFAULT FALSE
            )
        """)

    def list_checks(self) -> list[CronCheck]:
        rows = self._conn.execute(
            "SELECT name, schedule, use_case, params, enabled, notify_policy, destinations, timeout_seconds "
            "FROM schedule_checks"
        ).fetchall()
        return [_row_to_check(row) for row in rows]

    def get_check(self, name: str) -> CronCheck | None:
        row = self._conn.execute(
            "SELECT name, schedule, use_case, params, enabled, notify_policy, destinations, timeout_seconds "
            "FROM schedule_checks WHERE name = ?",
            [name],
        ).fetchone()
        return _row_to_check(row) if row else None

    def save_check(self, check: CronCheck) -> None:
        self._conn.execute(
            "INSERT OR REPLACE INTO schedule_checks (name, schedule, use_case, params, enabled, notify_policy, destinations, timeout_seconds) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            [
                check.name,
                check.schedule,
                check.use_case,
                json.dumps(check.params),
                check.enabled,
                check.notify_policy,
                json.dumps(check.destinations),
                check.timeout_seconds,
            ],
        )

    def delete_check(self, name: str) -> None:
        self._conn.execute("DELETE FROM schedule_checks WHERE name = ?", [name])

    def save_result(self, result: CheckResult) -> None:
        self._conn.execute(
            "INSERT INTO schedule_results (check_name, phase, started_at, finished_at, duration_ms, summary, payload_digest, changed, error_message, notified) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                result.check_name,
                result.phase,
                result.started_at.isoformat(),
                result.finished_at.isoformat() if result.finished_at else None,
                result.duration_ms,
                result.summary,
                result.payload_digest,
                result.changed,
                result.error_message,
                result.notified,
            ],
        )

    def last_result(self, name: str) -> CheckResult | None:
        row = self._conn.execute(
            "SELECT check_name, phase, started_at, finished_at, duration_ms, summary, payload_digest, changed, error_message, notified "
            "FROM schedule_results WHERE check_name = ? ORDER BY id DESC LIMIT 1",
            [name],
        ).fetchone()
        return _row_to_result(row) if row else None

    def history(self, name: str, limit: int = 10) -> list[CheckResult]:
        rows = self._conn.execute(
            "SELECT check_name, phase, started_at, finished_at, duration_ms, summary, payload_digest, changed, error_message, notified "
            "FROM schedule_results WHERE check_name = ? ORDER BY id DESC LIMIT ?",
            [name, limit],
        ).fetchall()
        return [_row_to_result(row) for row in rows]


def _row_to_check(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def _row_to_result(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(str(row[3])) if row[3] else None
    return CheckResult(
        check_name=str(row[0]),
        phase=str(row[1]),
        started_at=started,
        finished_at=finished,
        duration_ms=int(str(row[4])) if row[4] is not None else None,
        summary=str(row[5]) if row[5] else "",
        payload_digest=str(row[6]),
        changed=bool(row[7]),
        error_message=str(row[8]) if row[8] else None,
        notified=bool(row[9]),
    )
