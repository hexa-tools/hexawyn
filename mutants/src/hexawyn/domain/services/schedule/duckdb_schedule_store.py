from __future__ import annotations

import json
from collections.abc import Sequence
from datetime import UTC, datetime
from typing import TYPE_CHECKING

from hexawyn.application.ports.driven.schedule_store_port import ScheduleStorePort
from hexawyn.domain.models.schedule import CheckResult, CronCheck

if TYPE_CHECKING:
    from duckdb import DuckDBPyConnection


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁDuckDBScheduleStoreǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuckDBScheduleStoreǁ_ensure_schema__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuckDBScheduleStoreǁlist_checks__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuckDBScheduleStoreǁget_check__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuckDBScheduleStoreǁsave_check__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuckDBScheduleStoreǁdelete_check__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuckDBScheduleStoreǁsave_result__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuckDBScheduleStoreǁlast_result__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDuckDBScheduleStoreǁhistory__mutmut: MutantDict = {}  # type: ignore


class DuckDBScheduleStore(ScheduleStorePort):
    """Persiste définitions + historique dans DuckDB."""

    @_mutmut_mutated(mutants_xǁDuckDBScheduleStoreǁ__init____mutmut)
    def __init__(self, connection: DuckDBPyConnection) -> None:
        self._conn = connection
        self._ensure_schema()

    def xǁDuckDBScheduleStoreǁ__init____mutmut_orig(self, connection: DuckDBPyConnection) -> None:
        self._conn = connection
        self._ensure_schema()

    def xǁDuckDBScheduleStoreǁ__init____mutmut_1(self, connection: DuckDBPyConnection) -> None:
        self._conn = None
        self._ensure_schema()

    @_mutmut_mutated(mutants_xǁDuckDBScheduleStoreǁ_ensure_schema__mutmut)
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

    def xǁDuckDBScheduleStoreǁ_ensure_schema__mutmut_orig(self) -> None:
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

    def xǁDuckDBScheduleStoreǁ_ensure_schema__mutmut_1(self) -> None:
        self._conn.execute(None)
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

    def xǁDuckDBScheduleStoreǁ_ensure_schema__mutmut_2(self) -> None:
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
        self._conn.execute(None)

    @_mutmut_mutated(mutants_xǁDuckDBScheduleStoreǁlist_checks__mutmut)
    def list_checks(self) -> list[CronCheck]:
        rows = self._conn.execute(
            "SELECT name, schedule, use_case, params, enabled, notify_policy, destinations, timeout_seconds "  # noqa: E501
            "FROM schedule_checks"
        ).fetchall()
        return [_row_to_check(row) for row in rows]

    def xǁDuckDBScheduleStoreǁlist_checks__mutmut_orig(self) -> list[CronCheck]:
        rows = self._conn.execute(
            "SELECT name, schedule, use_case, params, enabled, notify_policy, destinations, timeout_seconds "  # noqa: E501
            "FROM schedule_checks"
        ).fetchall()
        return [_row_to_check(row) for row in rows]

    def xǁDuckDBScheduleStoreǁlist_checks__mutmut_1(self) -> list[CronCheck]:
        rows = None
        return [_row_to_check(row) for row in rows]

    def xǁDuckDBScheduleStoreǁlist_checks__mutmut_2(self) -> list[CronCheck]:
        rows = self._conn.execute(
            None
        ).fetchall()
        return [_row_to_check(row) for row in rows]

    def xǁDuckDBScheduleStoreǁlist_checks__mutmut_3(self) -> list[CronCheck]:
        rows = self._conn.execute(
            "XXSELECT name, schedule, use_case, params, enabled, notify_policy, destinations, timeout_seconds XX"  # noqa: E501
            "FROM schedule_checks"
        ).fetchall()
        return [_row_to_check(row) for row in rows]

    def xǁDuckDBScheduleStoreǁlist_checks__mutmut_4(self) -> list[CronCheck]:
        rows = self._conn.execute(
            "select name, schedule, use_case, params, enabled, notify_policy, destinations, timeout_seconds "  # noqa: E501
            "FROM schedule_checks"
        ).fetchall()
        return [_row_to_check(row) for row in rows]

    def xǁDuckDBScheduleStoreǁlist_checks__mutmut_5(self) -> list[CronCheck]:
        rows = self._conn.execute(
            "SELECT NAME, SCHEDULE, USE_CASE, PARAMS, ENABLED, NOTIFY_POLICY, DESTINATIONS, TIMEOUT_SECONDS "  # noqa: E501
            "FROM schedule_checks"
        ).fetchall()
        return [_row_to_check(row) for row in rows]

    def xǁDuckDBScheduleStoreǁlist_checks__mutmut_6(self) -> list[CronCheck]:
        rows = self._conn.execute(
            "SELECT name, schedule, use_case, params, enabled, notify_policy, destinations, timeout_seconds "  # noqa: E501
            "XXFROM schedule_checksXX"
        ).fetchall()
        return [_row_to_check(row) for row in rows]

    def xǁDuckDBScheduleStoreǁlist_checks__mutmut_7(self) -> list[CronCheck]:
        rows = self._conn.execute(
            "SELECT name, schedule, use_case, params, enabled, notify_policy, destinations, timeout_seconds "  # noqa: E501
            "from schedule_checks"
        ).fetchall()
        return [_row_to_check(row) for row in rows]

    def xǁDuckDBScheduleStoreǁlist_checks__mutmut_8(self) -> list[CronCheck]:
        rows = self._conn.execute(
            "SELECT name, schedule, use_case, params, enabled, notify_policy, destinations, timeout_seconds "  # noqa: E501
            "FROM SCHEDULE_CHECKS"
        ).fetchall()
        return [_row_to_check(row) for row in rows]

    def xǁDuckDBScheduleStoreǁlist_checks__mutmut_9(self) -> list[CronCheck]:
        rows = self._conn.execute(
            "SELECT name, schedule, use_case, params, enabled, notify_policy, destinations, timeout_seconds "  # noqa: E501
            "FROM schedule_checks"
        ).fetchall()
        return [_row_to_check(None) for row in rows]

    @_mutmut_mutated(mutants_xǁDuckDBScheduleStoreǁget_check__mutmut)
    def get_check(self, name: str) -> CronCheck | None:
        row = self._conn.execute(
            "SELECT name, schedule, use_case, params, enabled, notify_policy, destinations, timeout_seconds "  # noqa: E501
            "FROM schedule_checks WHERE name = ?",
            [name],
        ).fetchone()
        return _row_to_check(row) if row else None

    def xǁDuckDBScheduleStoreǁget_check__mutmut_orig(self, name: str) -> CronCheck | None:
        row = self._conn.execute(
            "SELECT name, schedule, use_case, params, enabled, notify_policy, destinations, timeout_seconds "  # noqa: E501
            "FROM schedule_checks WHERE name = ?",
            [name],
        ).fetchone()
        return _row_to_check(row) if row else None

    def xǁDuckDBScheduleStoreǁget_check__mutmut_1(self, name: str) -> CronCheck | None:
        row = None
        return _row_to_check(row) if row else None

    def xǁDuckDBScheduleStoreǁget_check__mutmut_2(self, name: str) -> CronCheck | None:
        row = self._conn.execute(
            None,
            [name],
        ).fetchone()
        return _row_to_check(row) if row else None

    def xǁDuckDBScheduleStoreǁget_check__mutmut_3(self, name: str) -> CronCheck | None:
        row = self._conn.execute(
            "SELECT name, schedule, use_case, params, enabled, notify_policy, destinations, timeout_seconds "  # noqa: E501
            "FROM schedule_checks WHERE name = ?",
            None,
        ).fetchone()
        return _row_to_check(row) if row else None

    def xǁDuckDBScheduleStoreǁget_check__mutmut_4(self, name: str) -> CronCheck | None:
        row = self._conn.execute(
            [name],
        ).fetchone()
        return _row_to_check(row) if row else None

    def xǁDuckDBScheduleStoreǁget_check__mutmut_5(self, name: str) -> CronCheck | None:
        row = self._conn.execute(
            "SELECT name, schedule, use_case, params, enabled, notify_policy, destinations, timeout_seconds "  # noqa: E501
            "FROM schedule_checks WHERE name = ?",
            ).fetchone()
        return _row_to_check(row) if row else None

    def xǁDuckDBScheduleStoreǁget_check__mutmut_6(self, name: str) -> CronCheck | None:
        row = self._conn.execute(
            "XXSELECT name, schedule, use_case, params, enabled, notify_policy, destinations, timeout_seconds XX"  # noqa: E501
            "FROM schedule_checks WHERE name = ?",
            [name],
        ).fetchone()
        return _row_to_check(row) if row else None

    def xǁDuckDBScheduleStoreǁget_check__mutmut_7(self, name: str) -> CronCheck | None:
        row = self._conn.execute(
            "select name, schedule, use_case, params, enabled, notify_policy, destinations, timeout_seconds "  # noqa: E501
            "FROM schedule_checks WHERE name = ?",
            [name],
        ).fetchone()
        return _row_to_check(row) if row else None

    def xǁDuckDBScheduleStoreǁget_check__mutmut_8(self, name: str) -> CronCheck | None:
        row = self._conn.execute(
            "SELECT NAME, SCHEDULE, USE_CASE, PARAMS, ENABLED, NOTIFY_POLICY, DESTINATIONS, TIMEOUT_SECONDS "  # noqa: E501
            "FROM schedule_checks WHERE name = ?",
            [name],
        ).fetchone()
        return _row_to_check(row) if row else None

    def xǁDuckDBScheduleStoreǁget_check__mutmut_9(self, name: str) -> CronCheck | None:
        row = self._conn.execute(
            "SELECT name, schedule, use_case, params, enabled, notify_policy, destinations, timeout_seconds "  # noqa: E501
            "XXFROM schedule_checks WHERE name = ?XX",
            [name],
        ).fetchone()
        return _row_to_check(row) if row else None

    def xǁDuckDBScheduleStoreǁget_check__mutmut_10(self, name: str) -> CronCheck | None:
        row = self._conn.execute(
            "SELECT name, schedule, use_case, params, enabled, notify_policy, destinations, timeout_seconds "  # noqa: E501
            "from schedule_checks where name = ?",
            [name],
        ).fetchone()
        return _row_to_check(row) if row else None

    def xǁDuckDBScheduleStoreǁget_check__mutmut_11(self, name: str) -> CronCheck | None:
        row = self._conn.execute(
            "SELECT name, schedule, use_case, params, enabled, notify_policy, destinations, timeout_seconds "  # noqa: E501
            "FROM SCHEDULE_CHECKS WHERE NAME = ?",
            [name],
        ).fetchone()
        return _row_to_check(row) if row else None

    def xǁDuckDBScheduleStoreǁget_check__mutmut_12(self, name: str) -> CronCheck | None:
        row = self._conn.execute(
            "SELECT name, schedule, use_case, params, enabled, notify_policy, destinations, timeout_seconds "  # noqa: E501
            "FROM schedule_checks WHERE name = ?",
            [name],
        ).fetchone()
        return _row_to_check(None) if row else None

    @_mutmut_mutated(mutants_xǁDuckDBScheduleStoreǁsave_check__mutmut)
    def save_check(self, check: CronCheck) -> None:
        self._conn.execute(
            "INSERT OR REPLACE INTO schedule_checks (name, schedule, use_case, params, enabled, notify_policy, destinations, timeout_seconds) "  # noqa: E501
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

    def xǁDuckDBScheduleStoreǁsave_check__mutmut_orig(self, check: CronCheck) -> None:
        self._conn.execute(
            "INSERT OR REPLACE INTO schedule_checks (name, schedule, use_case, params, enabled, notify_policy, destinations, timeout_seconds) "  # noqa: E501
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

    def xǁDuckDBScheduleStoreǁsave_check__mutmut_1(self, check: CronCheck) -> None:
        self._conn.execute(
            None,
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

    def xǁDuckDBScheduleStoreǁsave_check__mutmut_2(self, check: CronCheck) -> None:
        self._conn.execute(
            "INSERT OR REPLACE INTO schedule_checks (name, schedule, use_case, params, enabled, notify_policy, destinations, timeout_seconds) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            None,
        )

    def xǁDuckDBScheduleStoreǁsave_check__mutmut_3(self, check: CronCheck) -> None:
        self._conn.execute(
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

    def xǁDuckDBScheduleStoreǁsave_check__mutmut_4(self, check: CronCheck) -> None:
        self._conn.execute(
            "INSERT OR REPLACE INTO schedule_checks (name, schedule, use_case, params, enabled, notify_policy, destinations, timeout_seconds) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            )

    def xǁDuckDBScheduleStoreǁsave_check__mutmut_5(self, check: CronCheck) -> None:
        self._conn.execute(
            "XXINSERT OR REPLACE INTO schedule_checks (name, schedule, use_case, params, enabled, notify_policy, destinations, timeout_seconds) XX"  # noqa: E501
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

    def xǁDuckDBScheduleStoreǁsave_check__mutmut_6(self, check: CronCheck) -> None:
        self._conn.execute(
            "insert or replace into schedule_checks (name, schedule, use_case, params, enabled, notify_policy, destinations, timeout_seconds) "  # noqa: E501
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

    def xǁDuckDBScheduleStoreǁsave_check__mutmut_7(self, check: CronCheck) -> None:
        self._conn.execute(
            "INSERT OR REPLACE INTO SCHEDULE_CHECKS (NAME, SCHEDULE, USE_CASE, PARAMS, ENABLED, NOTIFY_POLICY, DESTINATIONS, TIMEOUT_SECONDS) "  # noqa: E501
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

    def xǁDuckDBScheduleStoreǁsave_check__mutmut_8(self, check: CronCheck) -> None:
        self._conn.execute(
            "INSERT OR REPLACE INTO schedule_checks (name, schedule, use_case, params, enabled, notify_policy, destinations, timeout_seconds) "  # noqa: E501
            "XXVALUES (?, ?, ?, ?, ?, ?, ?, ?)XX",
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

    def xǁDuckDBScheduleStoreǁsave_check__mutmut_9(self, check: CronCheck) -> None:
        self._conn.execute(
            "INSERT OR REPLACE INTO schedule_checks (name, schedule, use_case, params, enabled, notify_policy, destinations, timeout_seconds) "  # noqa: E501
            "values (?, ?, ?, ?, ?, ?, ?, ?)",
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

    def xǁDuckDBScheduleStoreǁsave_check__mutmut_10(self, check: CronCheck) -> None:
        self._conn.execute(
            "INSERT OR REPLACE INTO schedule_checks (name, schedule, use_case, params, enabled, notify_policy, destinations, timeout_seconds) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            [
                check.name,
                check.schedule,
                check.use_case,
                json.dumps(None),
                check.enabled,
                check.notify_policy,
                json.dumps(check.destinations),
                check.timeout_seconds,
            ],
        )

    def xǁDuckDBScheduleStoreǁsave_check__mutmut_11(self, check: CronCheck) -> None:
        self._conn.execute(
            "INSERT OR REPLACE INTO schedule_checks (name, schedule, use_case, params, enabled, notify_policy, destinations, timeout_seconds) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            [
                check.name,
                check.schedule,
                check.use_case,
                json.dumps(check.params),
                check.enabled,
                check.notify_policy,
                json.dumps(None),
                check.timeout_seconds,
            ],
        )

    @_mutmut_mutated(mutants_xǁDuckDBScheduleStoreǁdelete_check__mutmut)
    def delete_check(self, name: str) -> None:
        self._conn.execute("DELETE FROM schedule_checks WHERE name = ?", [name])

    def xǁDuckDBScheduleStoreǁdelete_check__mutmut_orig(self, name: str) -> None:
        self._conn.execute("DELETE FROM schedule_checks WHERE name = ?", [name])

    def xǁDuckDBScheduleStoreǁdelete_check__mutmut_1(self, name: str) -> None:
        self._conn.execute(None, [name])

    def xǁDuckDBScheduleStoreǁdelete_check__mutmut_2(self, name: str) -> None:
        self._conn.execute("DELETE FROM schedule_checks WHERE name = ?", None)

    def xǁDuckDBScheduleStoreǁdelete_check__mutmut_3(self, name: str) -> None:
        self._conn.execute([name])

    def xǁDuckDBScheduleStoreǁdelete_check__mutmut_4(self, name: str) -> None:
        self._conn.execute("DELETE FROM schedule_checks WHERE name = ?", )

    def xǁDuckDBScheduleStoreǁdelete_check__mutmut_5(self, name: str) -> None:
        self._conn.execute("XXDELETE FROM schedule_checks WHERE name = ?XX", [name])

    def xǁDuckDBScheduleStoreǁdelete_check__mutmut_6(self, name: str) -> None:
        self._conn.execute("delete from schedule_checks where name = ?", [name])

    def xǁDuckDBScheduleStoreǁdelete_check__mutmut_7(self, name: str) -> None:
        self._conn.execute("DELETE FROM SCHEDULE_CHECKS WHERE NAME = ?", [name])

    @_mutmut_mutated(mutants_xǁDuckDBScheduleStoreǁsave_result__mutmut)
    def save_result(self, result: CheckResult) -> None:
        self._conn.execute(
            "INSERT INTO schedule_results (check_name, phase, started_at, finished_at, duration_ms, summary, payload_digest, changed, error_message, notified) "  # noqa: E501
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

    def xǁDuckDBScheduleStoreǁsave_result__mutmut_orig(self, result: CheckResult) -> None:
        self._conn.execute(
            "INSERT INTO schedule_results (check_name, phase, started_at, finished_at, duration_ms, summary, payload_digest, changed, error_message, notified) "  # noqa: E501
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

    def xǁDuckDBScheduleStoreǁsave_result__mutmut_1(self, result: CheckResult) -> None:
        self._conn.execute(
            None,
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

    def xǁDuckDBScheduleStoreǁsave_result__mutmut_2(self, result: CheckResult) -> None:
        self._conn.execute(
            "INSERT INTO schedule_results (check_name, phase, started_at, finished_at, duration_ms, summary, payload_digest, changed, error_message, notified) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            None,
        )

    def xǁDuckDBScheduleStoreǁsave_result__mutmut_3(self, result: CheckResult) -> None:
        self._conn.execute(
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

    def xǁDuckDBScheduleStoreǁsave_result__mutmut_4(self, result: CheckResult) -> None:
        self._conn.execute(
            "INSERT INTO schedule_results (check_name, phase, started_at, finished_at, duration_ms, summary, payload_digest, changed, error_message, notified) "  # noqa: E501
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            )

    def xǁDuckDBScheduleStoreǁsave_result__mutmut_5(self, result: CheckResult) -> None:
        self._conn.execute(
            "XXINSERT INTO schedule_results (check_name, phase, started_at, finished_at, duration_ms, summary, payload_digest, changed, error_message, notified) XX"  # noqa: E501
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

    def xǁDuckDBScheduleStoreǁsave_result__mutmut_6(self, result: CheckResult) -> None:
        self._conn.execute(
            "insert into schedule_results (check_name, phase, started_at, finished_at, duration_ms, summary, payload_digest, changed, error_message, notified) "  # noqa: E501
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

    def xǁDuckDBScheduleStoreǁsave_result__mutmut_7(self, result: CheckResult) -> None:
        self._conn.execute(
            "INSERT INTO SCHEDULE_RESULTS (CHECK_NAME, PHASE, STARTED_AT, FINISHED_AT, DURATION_MS, SUMMARY, PAYLOAD_DIGEST, CHANGED, ERROR_MESSAGE, NOTIFIED) "  # noqa: E501
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

    def xǁDuckDBScheduleStoreǁsave_result__mutmut_8(self, result: CheckResult) -> None:
        self._conn.execute(
            "INSERT INTO schedule_results (check_name, phase, started_at, finished_at, duration_ms, summary, payload_digest, changed, error_message, notified) "  # noqa: E501
            "XXVALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)XX",
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

    def xǁDuckDBScheduleStoreǁsave_result__mutmut_9(self, result: CheckResult) -> None:
        self._conn.execute(
            "INSERT INTO schedule_results (check_name, phase, started_at, finished_at, duration_ms, summary, payload_digest, changed, error_message, notified) "  # noqa: E501
            "values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
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

    @_mutmut_mutated(mutants_xǁDuckDBScheduleStoreǁlast_result__mutmut)
    def last_result(self, name: str) -> CheckResult | None:
        row = self._conn.execute(
            "SELECT check_name, phase, started_at, finished_at, duration_ms, summary, payload_digest, changed, error_message, notified "  # noqa: E501
            "FROM schedule_results WHERE check_name = ? ORDER BY id DESC LIMIT 1",
            [name],
        ).fetchone()
        return _row_to_result(row) if row else None

    def xǁDuckDBScheduleStoreǁlast_result__mutmut_orig(self, name: str) -> CheckResult | None:
        row = self._conn.execute(
            "SELECT check_name, phase, started_at, finished_at, duration_ms, summary, payload_digest, changed, error_message, notified "  # noqa: E501
            "FROM schedule_results WHERE check_name = ? ORDER BY id DESC LIMIT 1",
            [name],
        ).fetchone()
        return _row_to_result(row) if row else None

    def xǁDuckDBScheduleStoreǁlast_result__mutmut_1(self, name: str) -> CheckResult | None:
        row = None
        return _row_to_result(row) if row else None

    def xǁDuckDBScheduleStoreǁlast_result__mutmut_2(self, name: str) -> CheckResult | None:
        row = self._conn.execute(
            None,
            [name],
        ).fetchone()
        return _row_to_result(row) if row else None

    def xǁDuckDBScheduleStoreǁlast_result__mutmut_3(self, name: str) -> CheckResult | None:
        row = self._conn.execute(
            "SELECT check_name, phase, started_at, finished_at, duration_ms, summary, payload_digest, changed, error_message, notified "  # noqa: E501
            "FROM schedule_results WHERE check_name = ? ORDER BY id DESC LIMIT 1",
            None,
        ).fetchone()
        return _row_to_result(row) if row else None

    def xǁDuckDBScheduleStoreǁlast_result__mutmut_4(self, name: str) -> CheckResult | None:
        row = self._conn.execute(
            [name],
        ).fetchone()
        return _row_to_result(row) if row else None

    def xǁDuckDBScheduleStoreǁlast_result__mutmut_5(self, name: str) -> CheckResult | None:
        row = self._conn.execute(
            "SELECT check_name, phase, started_at, finished_at, duration_ms, summary, payload_digest, changed, error_message, notified "  # noqa: E501
            "FROM schedule_results WHERE check_name = ? ORDER BY id DESC LIMIT 1",
            ).fetchone()
        return _row_to_result(row) if row else None

    def xǁDuckDBScheduleStoreǁlast_result__mutmut_6(self, name: str) -> CheckResult | None:
        row = self._conn.execute(
            "XXSELECT check_name, phase, started_at, finished_at, duration_ms, summary, payload_digest, changed, error_message, notified XX"  # noqa: E501
            "FROM schedule_results WHERE check_name = ? ORDER BY id DESC LIMIT 1",
            [name],
        ).fetchone()
        return _row_to_result(row) if row else None

    def xǁDuckDBScheduleStoreǁlast_result__mutmut_7(self, name: str) -> CheckResult | None:
        row = self._conn.execute(
            "select check_name, phase, started_at, finished_at, duration_ms, summary, payload_digest, changed, error_message, notified "  # noqa: E501
            "FROM schedule_results WHERE check_name = ? ORDER BY id DESC LIMIT 1",
            [name],
        ).fetchone()
        return _row_to_result(row) if row else None

    def xǁDuckDBScheduleStoreǁlast_result__mutmut_8(self, name: str) -> CheckResult | None:
        row = self._conn.execute(
            "SELECT CHECK_NAME, PHASE, STARTED_AT, FINISHED_AT, DURATION_MS, SUMMARY, PAYLOAD_DIGEST, CHANGED, ERROR_MESSAGE, NOTIFIED "  # noqa: E501
            "FROM schedule_results WHERE check_name = ? ORDER BY id DESC LIMIT 1",
            [name],
        ).fetchone()
        return _row_to_result(row) if row else None

    def xǁDuckDBScheduleStoreǁlast_result__mutmut_9(self, name: str) -> CheckResult | None:
        row = self._conn.execute(
            "SELECT check_name, phase, started_at, finished_at, duration_ms, summary, payload_digest, changed, error_message, notified "  # noqa: E501
            "XXFROM schedule_results WHERE check_name = ? ORDER BY id DESC LIMIT 1XX",
            [name],
        ).fetchone()
        return _row_to_result(row) if row else None

    def xǁDuckDBScheduleStoreǁlast_result__mutmut_10(self, name: str) -> CheckResult | None:
        row = self._conn.execute(
            "SELECT check_name, phase, started_at, finished_at, duration_ms, summary, payload_digest, changed, error_message, notified "  # noqa: E501
            "from schedule_results where check_name = ? order by id desc limit 1",
            [name],
        ).fetchone()
        return _row_to_result(row) if row else None

    def xǁDuckDBScheduleStoreǁlast_result__mutmut_11(self, name: str) -> CheckResult | None:
        row = self._conn.execute(
            "SELECT check_name, phase, started_at, finished_at, duration_ms, summary, payload_digest, changed, error_message, notified "  # noqa: E501
            "FROM SCHEDULE_RESULTS WHERE CHECK_NAME = ? ORDER BY ID DESC LIMIT 1",
            [name],
        ).fetchone()
        return _row_to_result(row) if row else None

    def xǁDuckDBScheduleStoreǁlast_result__mutmut_12(self, name: str) -> CheckResult | None:
        row = self._conn.execute(
            "SELECT check_name, phase, started_at, finished_at, duration_ms, summary, payload_digest, changed, error_message, notified "  # noqa: E501
            "FROM schedule_results WHERE check_name = ? ORDER BY id DESC LIMIT 1",
            [name],
        ).fetchone()
        return _row_to_result(None) if row else None

    @_mutmut_mutated(mutants_xǁDuckDBScheduleStoreǁhistory__mutmut)
    def history(self, name: str, limit: int = 10) -> list[CheckResult]:
        rows = self._conn.execute(
            "SELECT check_name, phase, started_at, finished_at, duration_ms, summary, payload_digest, changed, error_message, notified "  # noqa: E501
            "FROM schedule_results WHERE check_name = ? ORDER BY id DESC LIMIT ?",
            [name, limit],
        ).fetchall()
        return [_row_to_result(row) for row in rows]

    def xǁDuckDBScheduleStoreǁhistory__mutmut_orig(self, name: str, limit: int = 10) -> list[CheckResult]:
        rows = self._conn.execute(
            "SELECT check_name, phase, started_at, finished_at, duration_ms, summary, payload_digest, changed, error_message, notified "  # noqa: E501
            "FROM schedule_results WHERE check_name = ? ORDER BY id DESC LIMIT ?",
            [name, limit],
        ).fetchall()
        return [_row_to_result(row) for row in rows]

    def xǁDuckDBScheduleStoreǁhistory__mutmut_1(self, name: str, limit: int = 11) -> list[CheckResult]:
        rows = self._conn.execute(
            "SELECT check_name, phase, started_at, finished_at, duration_ms, summary, payload_digest, changed, error_message, notified "  # noqa: E501
            "FROM schedule_results WHERE check_name = ? ORDER BY id DESC LIMIT ?",
            [name, limit],
        ).fetchall()
        return [_row_to_result(row) for row in rows]

    def xǁDuckDBScheduleStoreǁhistory__mutmut_2(self, name: str, limit: int = 10) -> list[CheckResult]:
        rows = None
        return [_row_to_result(row) for row in rows]

    def xǁDuckDBScheduleStoreǁhistory__mutmut_3(self, name: str, limit: int = 10) -> list[CheckResult]:
        rows = self._conn.execute(
            None,
            [name, limit],
        ).fetchall()
        return [_row_to_result(row) for row in rows]

    def xǁDuckDBScheduleStoreǁhistory__mutmut_4(self, name: str, limit: int = 10) -> list[CheckResult]:
        rows = self._conn.execute(
            "SELECT check_name, phase, started_at, finished_at, duration_ms, summary, payload_digest, changed, error_message, notified "  # noqa: E501
            "FROM schedule_results WHERE check_name = ? ORDER BY id DESC LIMIT ?",
            None,
        ).fetchall()
        return [_row_to_result(row) for row in rows]

    def xǁDuckDBScheduleStoreǁhistory__mutmut_5(self, name: str, limit: int = 10) -> list[CheckResult]:
        rows = self._conn.execute(
            [name, limit],
        ).fetchall()
        return [_row_to_result(row) for row in rows]

    def xǁDuckDBScheduleStoreǁhistory__mutmut_6(self, name: str, limit: int = 10) -> list[CheckResult]:
        rows = self._conn.execute(
            "SELECT check_name, phase, started_at, finished_at, duration_ms, summary, payload_digest, changed, error_message, notified "  # noqa: E501
            "FROM schedule_results WHERE check_name = ? ORDER BY id DESC LIMIT ?",
            ).fetchall()
        return [_row_to_result(row) for row in rows]

    def xǁDuckDBScheduleStoreǁhistory__mutmut_7(self, name: str, limit: int = 10) -> list[CheckResult]:
        rows = self._conn.execute(
            "XXSELECT check_name, phase, started_at, finished_at, duration_ms, summary, payload_digest, changed, error_message, notified XX"  # noqa: E501
            "FROM schedule_results WHERE check_name = ? ORDER BY id DESC LIMIT ?",
            [name, limit],
        ).fetchall()
        return [_row_to_result(row) for row in rows]

    def xǁDuckDBScheduleStoreǁhistory__mutmut_8(self, name: str, limit: int = 10) -> list[CheckResult]:
        rows = self._conn.execute(
            "select check_name, phase, started_at, finished_at, duration_ms, summary, payload_digest, changed, error_message, notified "  # noqa: E501
            "FROM schedule_results WHERE check_name = ? ORDER BY id DESC LIMIT ?",
            [name, limit],
        ).fetchall()
        return [_row_to_result(row) for row in rows]

    def xǁDuckDBScheduleStoreǁhistory__mutmut_9(self, name: str, limit: int = 10) -> list[CheckResult]:
        rows = self._conn.execute(
            "SELECT CHECK_NAME, PHASE, STARTED_AT, FINISHED_AT, DURATION_MS, SUMMARY, PAYLOAD_DIGEST, CHANGED, ERROR_MESSAGE, NOTIFIED "  # noqa: E501
            "FROM schedule_results WHERE check_name = ? ORDER BY id DESC LIMIT ?",
            [name, limit],
        ).fetchall()
        return [_row_to_result(row) for row in rows]

    def xǁDuckDBScheduleStoreǁhistory__mutmut_10(self, name: str, limit: int = 10) -> list[CheckResult]:
        rows = self._conn.execute(
            "SELECT check_name, phase, started_at, finished_at, duration_ms, summary, payload_digest, changed, error_message, notified "  # noqa: E501
            "XXFROM schedule_results WHERE check_name = ? ORDER BY id DESC LIMIT ?XX",
            [name, limit],
        ).fetchall()
        return [_row_to_result(row) for row in rows]

    def xǁDuckDBScheduleStoreǁhistory__mutmut_11(self, name: str, limit: int = 10) -> list[CheckResult]:
        rows = self._conn.execute(
            "SELECT check_name, phase, started_at, finished_at, duration_ms, summary, payload_digest, changed, error_message, notified "  # noqa: E501
            "from schedule_results where check_name = ? order by id desc limit ?",
            [name, limit],
        ).fetchall()
        return [_row_to_result(row) for row in rows]

    def xǁDuckDBScheduleStoreǁhistory__mutmut_12(self, name: str, limit: int = 10) -> list[CheckResult]:
        rows = self._conn.execute(
            "SELECT check_name, phase, started_at, finished_at, duration_ms, summary, payload_digest, changed, error_message, notified "  # noqa: E501
            "FROM SCHEDULE_RESULTS WHERE CHECK_NAME = ? ORDER BY ID DESC LIMIT ?",
            [name, limit],
        ).fetchall()
        return [_row_to_result(row) for row in rows]

    def xǁDuckDBScheduleStoreǁhistory__mutmut_13(self, name: str, limit: int = 10) -> list[CheckResult]:
        rows = self._conn.execute(
            "SELECT check_name, phase, started_at, finished_at, duration_ms, summary, payload_digest, changed, error_message, notified "  # noqa: E501
            "FROM schedule_results WHERE check_name = ? ORDER BY id DESC LIMIT ?",
            [name, limit],
        ).fetchall()
        return [_row_to_result(None) for row in rows]

mutants_xǁDuckDBScheduleStoreǁ__init____mutmut['_mutmut_orig'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁ__init____mutmut['xǁDuckDBScheduleStoreǁ__init____mutmut_1'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁDuckDBScheduleStoreǁ_ensure_schema__mutmut['_mutmut_orig'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁ_ensure_schema__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁ_ensure_schema__mutmut['xǁDuckDBScheduleStoreǁ_ensure_schema__mutmut_1'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁ_ensure_schema__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁ_ensure_schema__mutmut['xǁDuckDBScheduleStoreǁ_ensure_schema__mutmut_2'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁ_ensure_schema__mutmut_2 # type: ignore # mutmut generated

mutants_xǁDuckDBScheduleStoreǁlist_checks__mutmut['_mutmut_orig'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁlist_checks__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁlist_checks__mutmut['xǁDuckDBScheduleStoreǁlist_checks__mutmut_1'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁlist_checks__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁlist_checks__mutmut['xǁDuckDBScheduleStoreǁlist_checks__mutmut_2'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁlist_checks__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁlist_checks__mutmut['xǁDuckDBScheduleStoreǁlist_checks__mutmut_3'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁlist_checks__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁlist_checks__mutmut['xǁDuckDBScheduleStoreǁlist_checks__mutmut_4'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁlist_checks__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁlist_checks__mutmut['xǁDuckDBScheduleStoreǁlist_checks__mutmut_5'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁlist_checks__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁlist_checks__mutmut['xǁDuckDBScheduleStoreǁlist_checks__mutmut_6'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁlist_checks__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁlist_checks__mutmut['xǁDuckDBScheduleStoreǁlist_checks__mutmut_7'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁlist_checks__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁlist_checks__mutmut['xǁDuckDBScheduleStoreǁlist_checks__mutmut_8'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁlist_checks__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁlist_checks__mutmut['xǁDuckDBScheduleStoreǁlist_checks__mutmut_9'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁlist_checks__mutmut_9 # type: ignore # mutmut generated

mutants_xǁDuckDBScheduleStoreǁget_check__mutmut['_mutmut_orig'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁget_check__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁget_check__mutmut['xǁDuckDBScheduleStoreǁget_check__mutmut_1'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁget_check__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁget_check__mutmut['xǁDuckDBScheduleStoreǁget_check__mutmut_2'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁget_check__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁget_check__mutmut['xǁDuckDBScheduleStoreǁget_check__mutmut_3'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁget_check__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁget_check__mutmut['xǁDuckDBScheduleStoreǁget_check__mutmut_4'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁget_check__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁget_check__mutmut['xǁDuckDBScheduleStoreǁget_check__mutmut_5'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁget_check__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁget_check__mutmut['xǁDuckDBScheduleStoreǁget_check__mutmut_6'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁget_check__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁget_check__mutmut['xǁDuckDBScheduleStoreǁget_check__mutmut_7'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁget_check__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁget_check__mutmut['xǁDuckDBScheduleStoreǁget_check__mutmut_8'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁget_check__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁget_check__mutmut['xǁDuckDBScheduleStoreǁget_check__mutmut_9'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁget_check__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁget_check__mutmut['xǁDuckDBScheduleStoreǁget_check__mutmut_10'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁget_check__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁget_check__mutmut['xǁDuckDBScheduleStoreǁget_check__mutmut_11'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁget_check__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁget_check__mutmut['xǁDuckDBScheduleStoreǁget_check__mutmut_12'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁget_check__mutmut_12 # type: ignore # mutmut generated

mutants_xǁDuckDBScheduleStoreǁsave_check__mutmut['_mutmut_orig'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁsave_check__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁsave_check__mutmut['xǁDuckDBScheduleStoreǁsave_check__mutmut_1'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁsave_check__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁsave_check__mutmut['xǁDuckDBScheduleStoreǁsave_check__mutmut_2'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁsave_check__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁsave_check__mutmut['xǁDuckDBScheduleStoreǁsave_check__mutmut_3'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁsave_check__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁsave_check__mutmut['xǁDuckDBScheduleStoreǁsave_check__mutmut_4'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁsave_check__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁsave_check__mutmut['xǁDuckDBScheduleStoreǁsave_check__mutmut_5'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁsave_check__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁsave_check__mutmut['xǁDuckDBScheduleStoreǁsave_check__mutmut_6'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁsave_check__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁsave_check__mutmut['xǁDuckDBScheduleStoreǁsave_check__mutmut_7'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁsave_check__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁsave_check__mutmut['xǁDuckDBScheduleStoreǁsave_check__mutmut_8'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁsave_check__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁsave_check__mutmut['xǁDuckDBScheduleStoreǁsave_check__mutmut_9'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁsave_check__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁsave_check__mutmut['xǁDuckDBScheduleStoreǁsave_check__mutmut_10'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁsave_check__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁsave_check__mutmut['xǁDuckDBScheduleStoreǁsave_check__mutmut_11'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁsave_check__mutmut_11 # type: ignore # mutmut generated

mutants_xǁDuckDBScheduleStoreǁdelete_check__mutmut['_mutmut_orig'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁdelete_check__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁdelete_check__mutmut['xǁDuckDBScheduleStoreǁdelete_check__mutmut_1'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁdelete_check__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁdelete_check__mutmut['xǁDuckDBScheduleStoreǁdelete_check__mutmut_2'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁdelete_check__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁdelete_check__mutmut['xǁDuckDBScheduleStoreǁdelete_check__mutmut_3'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁdelete_check__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁdelete_check__mutmut['xǁDuckDBScheduleStoreǁdelete_check__mutmut_4'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁdelete_check__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁdelete_check__mutmut['xǁDuckDBScheduleStoreǁdelete_check__mutmut_5'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁdelete_check__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁdelete_check__mutmut['xǁDuckDBScheduleStoreǁdelete_check__mutmut_6'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁdelete_check__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁdelete_check__mutmut['xǁDuckDBScheduleStoreǁdelete_check__mutmut_7'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁdelete_check__mutmut_7 # type: ignore # mutmut generated

mutants_xǁDuckDBScheduleStoreǁsave_result__mutmut['_mutmut_orig'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁsave_result__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁsave_result__mutmut['xǁDuckDBScheduleStoreǁsave_result__mutmut_1'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁsave_result__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁsave_result__mutmut['xǁDuckDBScheduleStoreǁsave_result__mutmut_2'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁsave_result__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁsave_result__mutmut['xǁDuckDBScheduleStoreǁsave_result__mutmut_3'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁsave_result__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁsave_result__mutmut['xǁDuckDBScheduleStoreǁsave_result__mutmut_4'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁsave_result__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁsave_result__mutmut['xǁDuckDBScheduleStoreǁsave_result__mutmut_5'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁsave_result__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁsave_result__mutmut['xǁDuckDBScheduleStoreǁsave_result__mutmut_6'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁsave_result__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁsave_result__mutmut['xǁDuckDBScheduleStoreǁsave_result__mutmut_7'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁsave_result__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁsave_result__mutmut['xǁDuckDBScheduleStoreǁsave_result__mutmut_8'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁsave_result__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁsave_result__mutmut['xǁDuckDBScheduleStoreǁsave_result__mutmut_9'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁsave_result__mutmut_9 # type: ignore # mutmut generated

mutants_xǁDuckDBScheduleStoreǁlast_result__mutmut['_mutmut_orig'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁlast_result__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁlast_result__mutmut['xǁDuckDBScheduleStoreǁlast_result__mutmut_1'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁlast_result__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁlast_result__mutmut['xǁDuckDBScheduleStoreǁlast_result__mutmut_2'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁlast_result__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁlast_result__mutmut['xǁDuckDBScheduleStoreǁlast_result__mutmut_3'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁlast_result__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁlast_result__mutmut['xǁDuckDBScheduleStoreǁlast_result__mutmut_4'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁlast_result__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁlast_result__mutmut['xǁDuckDBScheduleStoreǁlast_result__mutmut_5'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁlast_result__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁlast_result__mutmut['xǁDuckDBScheduleStoreǁlast_result__mutmut_6'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁlast_result__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁlast_result__mutmut['xǁDuckDBScheduleStoreǁlast_result__mutmut_7'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁlast_result__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁlast_result__mutmut['xǁDuckDBScheduleStoreǁlast_result__mutmut_8'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁlast_result__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁlast_result__mutmut['xǁDuckDBScheduleStoreǁlast_result__mutmut_9'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁlast_result__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁlast_result__mutmut['xǁDuckDBScheduleStoreǁlast_result__mutmut_10'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁlast_result__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁlast_result__mutmut['xǁDuckDBScheduleStoreǁlast_result__mutmut_11'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁlast_result__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁlast_result__mutmut['xǁDuckDBScheduleStoreǁlast_result__mutmut_12'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁlast_result__mutmut_12 # type: ignore # mutmut generated

mutants_xǁDuckDBScheduleStoreǁhistory__mutmut['_mutmut_orig'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁhistory__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁhistory__mutmut['xǁDuckDBScheduleStoreǁhistory__mutmut_1'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁhistory__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁhistory__mutmut['xǁDuckDBScheduleStoreǁhistory__mutmut_2'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁhistory__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁhistory__mutmut['xǁDuckDBScheduleStoreǁhistory__mutmut_3'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁhistory__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁhistory__mutmut['xǁDuckDBScheduleStoreǁhistory__mutmut_4'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁhistory__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁhistory__mutmut['xǁDuckDBScheduleStoreǁhistory__mutmut_5'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁhistory__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁhistory__mutmut['xǁDuckDBScheduleStoreǁhistory__mutmut_6'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁhistory__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁhistory__mutmut['xǁDuckDBScheduleStoreǁhistory__mutmut_7'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁhistory__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁhistory__mutmut['xǁDuckDBScheduleStoreǁhistory__mutmut_8'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁhistory__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁhistory__mutmut['xǁDuckDBScheduleStoreǁhistory__mutmut_9'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁhistory__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁhistory__mutmut['xǁDuckDBScheduleStoreǁhistory__mutmut_10'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁhistory__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁhistory__mutmut['xǁDuckDBScheduleStoreǁhistory__mutmut_11'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁhistory__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁhistory__mutmut['xǁDuckDBScheduleStoreǁhistory__mutmut_12'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁhistory__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDuckDBScheduleStoreǁhistory__mutmut['xǁDuckDBScheduleStoreǁhistory__mutmut_13'] = DuckDBScheduleStore.xǁDuckDBScheduleStoreǁhistory__mutmut_13 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__row_to_check__mutmut)
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


def x__row_to_check__mutmut_orig(row: Sequence[object]) -> CronCheck:
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


def x__row_to_check__mutmut_1(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=None,
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_2(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=None,
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_3(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=None,
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_4(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=None,
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_5(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=None,
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_6(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=None,
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_7(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=None,
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_8(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=None,
    )


def x__row_to_check__mutmut_9(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_10(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_11(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_12(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_13(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_14(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_15(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_16(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        )


def x__row_to_check__mutmut_17(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(None),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_18(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[1]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_19(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(None),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_20(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[2]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_21(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(None),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_22(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[3]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_23(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(None) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_24(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(None)) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_25(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(row[4])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_26(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[4] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_27(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(None),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_28(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[5]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_29(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(None) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_30(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[6]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_31(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[6] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_32(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "XXon_changeXX",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_33(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "ON_CHANGE",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_34(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(None) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_35(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(None)) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_36(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[7])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_37(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[7] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_38(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["XXslackXX"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_39(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["SLACK"],
        timeout_seconds=int(str(row[7])) if row[7] else 300,
    )


def x__row_to_check__mutmut_40(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(None) if row[7] else 300,
    )


def x__row_to_check__mutmut_41(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(None)) if row[7] else 300,
    )


def x__row_to_check__mutmut_42(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[8])) if row[7] else 300,
    )


def x__row_to_check__mutmut_43(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[8] else 300,
    )


def x__row_to_check__mutmut_44(row: Sequence[object]) -> CronCheck:
    return CronCheck(
        name=str(row[0]),
        schedule=str(row[1]),
        use_case=str(row[2]),
        params=json.loads(str(row[3])) if row[3] else {},
        enabled=bool(row[4]),
        notify_policy=str(row[5]) if row[5] else "on_change",
        destinations=json.loads(str(row[6])) if row[6] else ["slack"],
        timeout_seconds=int(str(row[7])) if row[7] else 301,
    )

mutants_x__row_to_check__mutmut['_mutmut_orig'] = x__row_to_check__mutmut_orig # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_1'] = x__row_to_check__mutmut_1 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_2'] = x__row_to_check__mutmut_2 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_3'] = x__row_to_check__mutmut_3 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_4'] = x__row_to_check__mutmut_4 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_5'] = x__row_to_check__mutmut_5 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_6'] = x__row_to_check__mutmut_6 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_7'] = x__row_to_check__mutmut_7 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_8'] = x__row_to_check__mutmut_8 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_9'] = x__row_to_check__mutmut_9 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_10'] = x__row_to_check__mutmut_10 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_11'] = x__row_to_check__mutmut_11 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_12'] = x__row_to_check__mutmut_12 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_13'] = x__row_to_check__mutmut_13 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_14'] = x__row_to_check__mutmut_14 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_15'] = x__row_to_check__mutmut_15 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_16'] = x__row_to_check__mutmut_16 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_17'] = x__row_to_check__mutmut_17 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_18'] = x__row_to_check__mutmut_18 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_19'] = x__row_to_check__mutmut_19 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_20'] = x__row_to_check__mutmut_20 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_21'] = x__row_to_check__mutmut_21 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_22'] = x__row_to_check__mutmut_22 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_23'] = x__row_to_check__mutmut_23 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_24'] = x__row_to_check__mutmut_24 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_25'] = x__row_to_check__mutmut_25 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_26'] = x__row_to_check__mutmut_26 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_27'] = x__row_to_check__mutmut_27 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_28'] = x__row_to_check__mutmut_28 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_29'] = x__row_to_check__mutmut_29 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_30'] = x__row_to_check__mutmut_30 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_31'] = x__row_to_check__mutmut_31 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_32'] = x__row_to_check__mutmut_32 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_33'] = x__row_to_check__mutmut_33 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_34'] = x__row_to_check__mutmut_34 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_35'] = x__row_to_check__mutmut_35 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_36'] = x__row_to_check__mutmut_36 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_37'] = x__row_to_check__mutmut_37 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_38'] = x__row_to_check__mutmut_38 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_39'] = x__row_to_check__mutmut_39 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_40'] = x__row_to_check__mutmut_40 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_41'] = x__row_to_check__mutmut_41 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_42'] = x__row_to_check__mutmut_42 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_43'] = x__row_to_check__mutmut_43 # type: ignore # mutmut generated
mutants_x__row_to_check__mutmut['x__row_to_check__mutmut_44'] = x__row_to_check__mutmut_44 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__row_to_result__mutmut)
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


def x__row_to_result__mutmut_orig(row: Sequence[object]) -> CheckResult:
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


def x__row_to_result__mutmut_1(row: Sequence[object]) -> CheckResult:
    started = None
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


def x__row_to_result__mutmut_2(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(None) if row[2] else datetime.now(UTC)
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


def x__row_to_result__mutmut_3(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(None)) if row[2] else datetime.now(UTC)
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


def x__row_to_result__mutmut_4(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[3])) if row[2] else datetime.now(UTC)
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


def x__row_to_result__mutmut_5(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[3] else datetime.now(UTC)
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


def x__row_to_result__mutmut_6(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(None)
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


def x__row_to_result__mutmut_7(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = None
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


def x__row_to_result__mutmut_8(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(None) if row[3] else None
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


def x__row_to_result__mutmut_9(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(str(None)) if row[3] else None
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


def x__row_to_result__mutmut_10(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(str(row[4])) if row[3] else None
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


def x__row_to_result__mutmut_11(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(str(row[3])) if row[4] else None
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


def x__row_to_result__mutmut_12(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(str(row[3])) if row[3] else None
    return CheckResult(
        check_name=None,
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


def x__row_to_result__mutmut_13(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(str(row[3])) if row[3] else None
    return CheckResult(
        check_name=str(row[0]),
        phase=None,
        started_at=started,
        finished_at=finished,
        duration_ms=int(str(row[4])) if row[4] is not None else None,
        summary=str(row[5]) if row[5] else "",
        payload_digest=str(row[6]),
        changed=bool(row[7]),
        error_message=str(row[8]) if row[8] else None,
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_14(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(str(row[3])) if row[3] else None
    return CheckResult(
        check_name=str(row[0]),
        phase=str(row[1]),
        started_at=None,
        finished_at=finished,
        duration_ms=int(str(row[4])) if row[4] is not None else None,
        summary=str(row[5]) if row[5] else "",
        payload_digest=str(row[6]),
        changed=bool(row[7]),
        error_message=str(row[8]) if row[8] else None,
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_15(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(str(row[3])) if row[3] else None
    return CheckResult(
        check_name=str(row[0]),
        phase=str(row[1]),
        started_at=started,
        finished_at=None,
        duration_ms=int(str(row[4])) if row[4] is not None else None,
        summary=str(row[5]) if row[5] else "",
        payload_digest=str(row[6]),
        changed=bool(row[7]),
        error_message=str(row[8]) if row[8] else None,
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_16(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(str(row[3])) if row[3] else None
    return CheckResult(
        check_name=str(row[0]),
        phase=str(row[1]),
        started_at=started,
        finished_at=finished,
        duration_ms=None,
        summary=str(row[5]) if row[5] else "",
        payload_digest=str(row[6]),
        changed=bool(row[7]),
        error_message=str(row[8]) if row[8] else None,
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_17(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(str(row[3])) if row[3] else None
    return CheckResult(
        check_name=str(row[0]),
        phase=str(row[1]),
        started_at=started,
        finished_at=finished,
        duration_ms=int(str(row[4])) if row[4] is not None else None,
        summary=None,
        payload_digest=str(row[6]),
        changed=bool(row[7]),
        error_message=str(row[8]) if row[8] else None,
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_18(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(str(row[3])) if row[3] else None
    return CheckResult(
        check_name=str(row[0]),
        phase=str(row[1]),
        started_at=started,
        finished_at=finished,
        duration_ms=int(str(row[4])) if row[4] is not None else None,
        summary=str(row[5]) if row[5] else "",
        payload_digest=None,
        changed=bool(row[7]),
        error_message=str(row[8]) if row[8] else None,
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_19(row: Sequence[object]) -> CheckResult:
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
        changed=None,
        error_message=str(row[8]) if row[8] else None,
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_20(row: Sequence[object]) -> CheckResult:
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
        error_message=None,
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_21(row: Sequence[object]) -> CheckResult:
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
        notified=None,
    )


def x__row_to_result__mutmut_22(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(str(row[3])) if row[3] else None
    return CheckResult(
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


def x__row_to_result__mutmut_23(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(str(row[3])) if row[3] else None
    return CheckResult(
        check_name=str(row[0]),
        started_at=started,
        finished_at=finished,
        duration_ms=int(str(row[4])) if row[4] is not None else None,
        summary=str(row[5]) if row[5] else "",
        payload_digest=str(row[6]),
        changed=bool(row[7]),
        error_message=str(row[8]) if row[8] else None,
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_24(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(str(row[3])) if row[3] else None
    return CheckResult(
        check_name=str(row[0]),
        phase=str(row[1]),
        finished_at=finished,
        duration_ms=int(str(row[4])) if row[4] is not None else None,
        summary=str(row[5]) if row[5] else "",
        payload_digest=str(row[6]),
        changed=bool(row[7]),
        error_message=str(row[8]) if row[8] else None,
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_25(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(str(row[3])) if row[3] else None
    return CheckResult(
        check_name=str(row[0]),
        phase=str(row[1]),
        started_at=started,
        duration_ms=int(str(row[4])) if row[4] is not None else None,
        summary=str(row[5]) if row[5] else "",
        payload_digest=str(row[6]),
        changed=bool(row[7]),
        error_message=str(row[8]) if row[8] else None,
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_26(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(str(row[3])) if row[3] else None
    return CheckResult(
        check_name=str(row[0]),
        phase=str(row[1]),
        started_at=started,
        finished_at=finished,
        summary=str(row[5]) if row[5] else "",
        payload_digest=str(row[6]),
        changed=bool(row[7]),
        error_message=str(row[8]) if row[8] else None,
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_27(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(str(row[3])) if row[3] else None
    return CheckResult(
        check_name=str(row[0]),
        phase=str(row[1]),
        started_at=started,
        finished_at=finished,
        duration_ms=int(str(row[4])) if row[4] is not None else None,
        payload_digest=str(row[6]),
        changed=bool(row[7]),
        error_message=str(row[8]) if row[8] else None,
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_28(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(str(row[3])) if row[3] else None
    return CheckResult(
        check_name=str(row[0]),
        phase=str(row[1]),
        started_at=started,
        finished_at=finished,
        duration_ms=int(str(row[4])) if row[4] is not None else None,
        summary=str(row[5]) if row[5] else "",
        changed=bool(row[7]),
        error_message=str(row[8]) if row[8] else None,
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_29(row: Sequence[object]) -> CheckResult:
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
        error_message=str(row[8]) if row[8] else None,
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_30(row: Sequence[object]) -> CheckResult:
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
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_31(row: Sequence[object]) -> CheckResult:
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
        )


def x__row_to_result__mutmut_32(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(str(row[3])) if row[3] else None
    return CheckResult(
        check_name=str(None),
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


def x__row_to_result__mutmut_33(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(str(row[3])) if row[3] else None
    return CheckResult(
        check_name=str(row[1]),
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


def x__row_to_result__mutmut_34(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(str(row[3])) if row[3] else None
    return CheckResult(
        check_name=str(row[0]),
        phase=str(None),
        started_at=started,
        finished_at=finished,
        duration_ms=int(str(row[4])) if row[4] is not None else None,
        summary=str(row[5]) if row[5] else "",
        payload_digest=str(row[6]),
        changed=bool(row[7]),
        error_message=str(row[8]) if row[8] else None,
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_35(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(str(row[3])) if row[3] else None
    return CheckResult(
        check_name=str(row[0]),
        phase=str(row[2]),
        started_at=started,
        finished_at=finished,
        duration_ms=int(str(row[4])) if row[4] is not None else None,
        summary=str(row[5]) if row[5] else "",
        payload_digest=str(row[6]),
        changed=bool(row[7]),
        error_message=str(row[8]) if row[8] else None,
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_36(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(str(row[3])) if row[3] else None
    return CheckResult(
        check_name=str(row[0]),
        phase=str(row[1]),
        started_at=started,
        finished_at=finished,
        duration_ms=int(None) if row[4] is not None else None,
        summary=str(row[5]) if row[5] else "",
        payload_digest=str(row[6]),
        changed=bool(row[7]),
        error_message=str(row[8]) if row[8] else None,
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_37(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(str(row[3])) if row[3] else None
    return CheckResult(
        check_name=str(row[0]),
        phase=str(row[1]),
        started_at=started,
        finished_at=finished,
        duration_ms=int(str(None)) if row[4] is not None else None,
        summary=str(row[5]) if row[5] else "",
        payload_digest=str(row[6]),
        changed=bool(row[7]),
        error_message=str(row[8]) if row[8] else None,
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_38(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(str(row[3])) if row[3] else None
    return CheckResult(
        check_name=str(row[0]),
        phase=str(row[1]),
        started_at=started,
        finished_at=finished,
        duration_ms=int(str(row[5])) if row[4] is not None else None,
        summary=str(row[5]) if row[5] else "",
        payload_digest=str(row[6]),
        changed=bool(row[7]),
        error_message=str(row[8]) if row[8] else None,
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_39(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(str(row[3])) if row[3] else None
    return CheckResult(
        check_name=str(row[0]),
        phase=str(row[1]),
        started_at=started,
        finished_at=finished,
        duration_ms=int(str(row[4])) if row[5] is not None else None,
        summary=str(row[5]) if row[5] else "",
        payload_digest=str(row[6]),
        changed=bool(row[7]),
        error_message=str(row[8]) if row[8] else None,
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_40(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(str(row[3])) if row[3] else None
    return CheckResult(
        check_name=str(row[0]),
        phase=str(row[1]),
        started_at=started,
        finished_at=finished,
        duration_ms=int(str(row[4])) if row[4] is None else None,
        summary=str(row[5]) if row[5] else "",
        payload_digest=str(row[6]),
        changed=bool(row[7]),
        error_message=str(row[8]) if row[8] else None,
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_41(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(str(row[3])) if row[3] else None
    return CheckResult(
        check_name=str(row[0]),
        phase=str(row[1]),
        started_at=started,
        finished_at=finished,
        duration_ms=int(str(row[4])) if row[4] is not None else None,
        summary=str(None) if row[5] else "",
        payload_digest=str(row[6]),
        changed=bool(row[7]),
        error_message=str(row[8]) if row[8] else None,
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_42(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(str(row[3])) if row[3] else None
    return CheckResult(
        check_name=str(row[0]),
        phase=str(row[1]),
        started_at=started,
        finished_at=finished,
        duration_ms=int(str(row[4])) if row[4] is not None else None,
        summary=str(row[6]) if row[5] else "",
        payload_digest=str(row[6]),
        changed=bool(row[7]),
        error_message=str(row[8]) if row[8] else None,
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_43(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(str(row[3])) if row[3] else None
    return CheckResult(
        check_name=str(row[0]),
        phase=str(row[1]),
        started_at=started,
        finished_at=finished,
        duration_ms=int(str(row[4])) if row[4] is not None else None,
        summary=str(row[5]) if row[6] else "",
        payload_digest=str(row[6]),
        changed=bool(row[7]),
        error_message=str(row[8]) if row[8] else None,
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_44(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(str(row[3])) if row[3] else None
    return CheckResult(
        check_name=str(row[0]),
        phase=str(row[1]),
        started_at=started,
        finished_at=finished,
        duration_ms=int(str(row[4])) if row[4] is not None else None,
        summary=str(row[5]) if row[5] else "XXXX",
        payload_digest=str(row[6]),
        changed=bool(row[7]),
        error_message=str(row[8]) if row[8] else None,
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_45(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(str(row[3])) if row[3] else None
    return CheckResult(
        check_name=str(row[0]),
        phase=str(row[1]),
        started_at=started,
        finished_at=finished,
        duration_ms=int(str(row[4])) if row[4] is not None else None,
        summary=str(row[5]) if row[5] else "",
        payload_digest=str(None),
        changed=bool(row[7]),
        error_message=str(row[8]) if row[8] else None,
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_46(row: Sequence[object]) -> CheckResult:
    started = datetime.fromisoformat(str(row[2])) if row[2] else datetime.now(UTC)
    finished = datetime.fromisoformat(str(row[3])) if row[3] else None
    return CheckResult(
        check_name=str(row[0]),
        phase=str(row[1]),
        started_at=started,
        finished_at=finished,
        duration_ms=int(str(row[4])) if row[4] is not None else None,
        summary=str(row[5]) if row[5] else "",
        payload_digest=str(row[7]),
        changed=bool(row[7]),
        error_message=str(row[8]) if row[8] else None,
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_47(row: Sequence[object]) -> CheckResult:
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
        changed=bool(None),
        error_message=str(row[8]) if row[8] else None,
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_48(row: Sequence[object]) -> CheckResult:
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
        changed=bool(row[8]),
        error_message=str(row[8]) if row[8] else None,
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_49(row: Sequence[object]) -> CheckResult:
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
        error_message=str(None) if row[8] else None,
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_50(row: Sequence[object]) -> CheckResult:
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
        error_message=str(row[9]) if row[8] else None,
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_51(row: Sequence[object]) -> CheckResult:
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
        error_message=str(row[8]) if row[9] else None,
        notified=bool(row[9]),
    )


def x__row_to_result__mutmut_52(row: Sequence[object]) -> CheckResult:
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
        notified=bool(None),
    )


def x__row_to_result__mutmut_53(row: Sequence[object]) -> CheckResult:
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
        notified=bool(row[10]),
    )

mutants_x__row_to_result__mutmut['_mutmut_orig'] = x__row_to_result__mutmut_orig # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_1'] = x__row_to_result__mutmut_1 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_2'] = x__row_to_result__mutmut_2 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_3'] = x__row_to_result__mutmut_3 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_4'] = x__row_to_result__mutmut_4 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_5'] = x__row_to_result__mutmut_5 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_6'] = x__row_to_result__mutmut_6 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_7'] = x__row_to_result__mutmut_7 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_8'] = x__row_to_result__mutmut_8 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_9'] = x__row_to_result__mutmut_9 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_10'] = x__row_to_result__mutmut_10 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_11'] = x__row_to_result__mutmut_11 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_12'] = x__row_to_result__mutmut_12 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_13'] = x__row_to_result__mutmut_13 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_14'] = x__row_to_result__mutmut_14 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_15'] = x__row_to_result__mutmut_15 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_16'] = x__row_to_result__mutmut_16 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_17'] = x__row_to_result__mutmut_17 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_18'] = x__row_to_result__mutmut_18 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_19'] = x__row_to_result__mutmut_19 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_20'] = x__row_to_result__mutmut_20 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_21'] = x__row_to_result__mutmut_21 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_22'] = x__row_to_result__mutmut_22 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_23'] = x__row_to_result__mutmut_23 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_24'] = x__row_to_result__mutmut_24 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_25'] = x__row_to_result__mutmut_25 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_26'] = x__row_to_result__mutmut_26 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_27'] = x__row_to_result__mutmut_27 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_28'] = x__row_to_result__mutmut_28 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_29'] = x__row_to_result__mutmut_29 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_30'] = x__row_to_result__mutmut_30 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_31'] = x__row_to_result__mutmut_31 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_32'] = x__row_to_result__mutmut_32 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_33'] = x__row_to_result__mutmut_33 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_34'] = x__row_to_result__mutmut_34 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_35'] = x__row_to_result__mutmut_35 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_36'] = x__row_to_result__mutmut_36 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_37'] = x__row_to_result__mutmut_37 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_38'] = x__row_to_result__mutmut_38 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_39'] = x__row_to_result__mutmut_39 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_40'] = x__row_to_result__mutmut_40 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_41'] = x__row_to_result__mutmut_41 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_42'] = x__row_to_result__mutmut_42 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_43'] = x__row_to_result__mutmut_43 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_44'] = x__row_to_result__mutmut_44 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_45'] = x__row_to_result__mutmut_45 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_46'] = x__row_to_result__mutmut_46 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_47'] = x__row_to_result__mutmut_47 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_48'] = x__row_to_result__mutmut_48 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_49'] = x__row_to_result__mutmut_49 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_50'] = x__row_to_result__mutmut_50 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_51'] = x__row_to_result__mutmut_51 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_52'] = x__row_to_result__mutmut_52 # type: ignore # mutmut generated
mutants_x__row_to_result__mutmut['x__row_to_result__mutmut_53'] = x__row_to_result__mutmut_53 # type: ignore # mutmut generated
