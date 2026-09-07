from __future__ import annotations

from datetime import UTC, datetime
from unittest.mock import MagicMock

from hexawyn.domain.models.schedule import CheckResult, CronCheck

_SELECT_CHECKS_COLUMNS = (
    "SELECT name, schedule, use_case, params, enabled, notify_policy, "
    "destinations, timeout_seconds"
)
_SELECT_RESULTS_COLUMNS = (
    "SELECT check_name, phase, started_at, finished_at, duration_ms, summary, "
    "payload_digest, changed, error_message, notified"
)
_INSERT_CHECK_SQL = (
    "INSERT OR REPLACE INTO schedule_checks (name, schedule, use_case, params, "
    "enabled, notify_policy, destinations, timeout_seconds) "
    "VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
)
_INSERT_RESULT_SQL = (
    "INSERT INTO schedule_results (check_name, phase, started_at, finished_at, "
    "duration_ms, summary, payload_digest, changed, error_message, notified) "
    "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
)


def _store(connection: MagicMock) -> MagicMock:
    from hexawyn.domain.services.schedule.duckdb_schedule_store import (
        DuckDBScheduleStore,
    )

    store = DuckDBScheduleStore(connection=connection)
    connection.reset_mock()
    return store


def _check_row(  # noqa: PLR0913
    name: str = "certs",
    schedule: str = "0 */6 * * *",
    use_case: str = "certs_list",
    params: str = '{"env": "prod"}',
    enabled: object = True,
    notify_policy: str = "on_change",
    destinations: str = '["slack", "teams"]',
    timeout_seconds: object = 300,
) -> tuple[object, ...]:
    return (
        name,
        schedule,
        use_case,
        params,
        enabled,
        notify_policy,
        destinations,
        timeout_seconds,
    )


def _result_row(  # noqa: PLR0913
    check_name: str = "certs",
    phase: str = "success",
    started_at: str = "2026-01-02T03:04:05+00:00",
    finished_at: str | None = "2026-01-02T04:00:00+00:00",
    duration_ms: object = 1200,
    summary: str = "ok",
    payload_digest: str = "abc123",
    changed: object = False,
    error_message: str | None = None,
    notified: object = False,
) -> tuple[object, ...]:
    return (
        check_name,
        phase,
        started_at,
        finished_at,
        duration_ms,
        summary,
        payload_digest,
        changed,
        error_message,
        notified,
    )


class TestEnsureSchema:
    def test_creates_both_tables_on_init(self) -> None:
        from hexawyn.domain.services.schedule.duckdb_schedule_store import (
            DuckDBScheduleStore,
        )

        connection = MagicMock()
        DuckDBScheduleStore(connection=connection)

        sql_calls = [call.args[0] for call in connection.execute.call_args_list]
        assert any("CREATE TABLE IF NOT EXISTS schedule_checks" in sql for sql in sql_calls)
        assert any("CREATE TABLE IF NOT EXISTS schedule_results" in sql for sql in sql_calls)


class TestListChecks:
    def test_returns_mapped_checks(self) -> None:
        connection = MagicMock()
        connection.execute.return_value.fetchall.return_value = [
            _check_row(name="certs"),
            _check_row(name="certs2", use_case="rbac", params="{}"),
        ]
        store = _store(connection)

        result = store.list_checks()

        assert len(result) == 2  # noqa: PLR2004
        assert result[0].name == "certs"
        assert result[0].use_case == "certs_list"
        assert result[1].name == "certs2"
        assert connection.execute.call_args.args[0] == (
            f"{_SELECT_CHECKS_COLUMNS} FROM schedule_checks"
        )

    def test_empty_table_returns_empty_list(self) -> None:
        connection = MagicMock()
        connection.execute.return_value.fetchall.return_value = []
        store = _store(connection)

        assert store.list_checks() == []


class TestGetCheck:
    def test_returns_check_when_row_present(self) -> None:
        connection = MagicMock()
        connection.execute.return_value.fetchone.return_value = _check_row()
        store = _store(connection)

        result = store.get_check("certs")

        assert result == CronCheck(
            name="certs",
            schedule="0 */6 * * *",
            use_case="certs_list",
            params={"env": "prod"},
            enabled=True,
            notify_policy="on_change",
            destinations=["slack", "teams"],
            timeout_seconds=300,
        )
        assert connection.execute.call_args.args[0] == (
            f"{_SELECT_CHECKS_COLUMNS} FROM schedule_checks WHERE name = ?"
        )
        assert connection.execute.call_args.args[1] == ["certs"]

    def test_returns_none_when_absent(self) -> None:
        connection = MagicMock()
        connection.execute.return_value.fetchone.return_value = None
        store = _store(connection)

        assert store.get_check("missing") is None

    def test_row_with_defaults_when_nullable_cells(self) -> None:
        connection = MagicMock()
        connection.execute.return_value.fetchone.return_value = _check_row(
            params=None,
            enabled=None,
            notify_policy=None,
            destinations=None,
            timeout_seconds=None,
        )
        store = _store(connection)

        result = store.get_check("certs")

        assert result.params == {}
        assert result.enabled is False
        assert result.notify_policy == "on_change"
        assert result.destinations == ["slack"]
        assert result.timeout_seconds == 300  # noqa: PLR2004


class TestSaveCheck:
    def test_inserts_serialized_check(self) -> None:
        connection = MagicMock()
        store = _store(connection)
        check = CronCheck(
            name="certs",
            schedule="0 */6 * * *",
            use_case="certs_list",
            params={"env": "prod"},
            enabled=False,
            notify_policy="always",
            destinations=["slack"],
            timeout_seconds=120,
        )

        store.save_check(check)

        sql = connection.execute.call_args.args[0]
        params = connection.execute.call_args.args[1]
        assert sql == _INSERT_CHECK_SQL
        assert params == [
            "certs",
            "0 */6 * * *",
            "certs_list",
            '{"env": "prod"}',
            False,
            "always",
            '["slack"]',
            120,
        ]


class TestDeleteCheck:
    def test_deletes_by_name(self) -> None:
        connection = MagicMock()
        store = _store(connection)

        store.delete_check("certs")

        assert connection.execute.call_args.args[0] == (
            "DELETE FROM schedule_checks WHERE name = ?"
        )
        assert connection.execute.call_args.args[1] == ["certs"]


class TestSaveResult:
    def test_inserts_full_result(self) -> None:
        connection = MagicMock()
        store = _store(connection)
        result = CheckResult(
            check_name="certs",
            phase="success",
            started_at=datetime(2026, 1, 2, 3, 4, 5, tzinfo=UTC),
            finished_at=datetime(2026, 1, 2, 4, 0, 0, tzinfo=UTC),
            duration_ms=1200,
            summary="ok",
            payload_digest="abc123",
            changed=True,
            error_message="boom",
            notified=True,
        )

        store.save_result(result)

        sql = connection.execute.call_args.args[0]
        params = connection.execute.call_args.args[1]
        assert sql == _INSERT_RESULT_SQL
        assert params == [
            "certs",
            "success",
            "2026-01-02T03:04:05+00:00",
            "2026-01-02T04:00:00+00:00",
            1200,
            "ok",
            "abc123",
            True,
            "boom",
            True,
        ]

    def test_inserts_result_without_finished(self) -> None:
        connection = MagicMock()
        store = _store(connection)
        result = CheckResult(
            check_name="certs",
            phase="running",
            started_at=datetime(2026, 1, 2, 3, 4, 5, tzinfo=UTC),
            payload_digest="abc123",
        )

        store.save_result(result)

        params = connection.execute.call_args.args[1]
        assert params[3] is None  # finished_at
        assert params[4] is None  # duration_ms
        assert params[6] == "abc123"
        assert params[8] is None  # error_message


class TestLastResult:
    def test_returns_mapped_result_when_present(self) -> None:
        connection = MagicMock()
        connection.execute.return_value.fetchone.return_value = _result_row()
        store = _store(connection)

        result = store.last_result("certs")

        assert result == CheckResult(
            check_name="certs",
            phase="success",
            started_at=datetime(2026, 1, 2, 3, 4, 5, tzinfo=UTC),
            finished_at=datetime(2026, 1, 2, 4, 0, 0, tzinfo=UTC),
            duration_ms=1200,
            summary="ok",
            payload_digest="abc123",
            changed=False,
            error_message=None,
            notified=False,
        )
        assert connection.execute.call_args.args[0] == (
            f"{_SELECT_RESULTS_COLUMNS} FROM schedule_results "
            "WHERE check_name = ? ORDER BY id DESC LIMIT 1"
        )
        assert connection.execute.call_args.args[1] == ["certs"]

    def test_returns_none_when_absent(self) -> None:
        connection = MagicMock()
        connection.execute.return_value.fetchone.return_value = None
        store = _store(connection)

        assert store.last_result("missing") is None

    def test_result_defaults_when_nullable_cells(self) -> None:
        connection = MagicMock()
        connection.execute.return_value.fetchone.return_value = _result_row(
            started_at=None,
            finished_at=None,
            duration_ms=None,
            summary=None,
            error_message=None,
        )
        store = _store(connection)

        result = store.last_result("certs")

        assert result.started_at is not None  # falls back to now
        assert result.finished_at is None
        assert result.duration_ms is None
        assert result.summary == ""
        assert result.error_message is None


class TestHistory:
    def test_returns_most_recent_first(self) -> None:
        connection = MagicMock()
        connection.execute.return_value.fetchall.return_value = [
            _result_row(check_name="certs", started_at="2026-01-02T03:04:05+00:00"),
            _result_row(check_name="certs", started_at="2026-01-01T03:04:05+00:00"),
        ]
        store = _store(connection)

        result = store.history("certs", limit=5)

        assert len(result) == 2  # noqa: PLR2004
        assert result[0].started_at == datetime(2026, 1, 2, 3, 4, 5, tzinfo=UTC)
        assert result[1].started_at == datetime(2026, 1, 1, 3, 4, 5, tzinfo=UTC)
        assert connection.execute.call_args.args[0] == (
            f"{_SELECT_RESULTS_COLUMNS} FROM schedule_results "
            "WHERE check_name = ? ORDER BY id DESC LIMIT ?"
        )
        assert connection.execute.call_args.args[1] == ["certs", 5]

    def test_empty_history_returns_empty_list(self) -> None:
        connection = MagicMock()
        connection.execute.return_value.fetchall.return_value = []
        store = _store(connection)

        assert store.history("certs") == []

    def test_default_limit_is_ten(self) -> None:
        connection = MagicMock()
        connection.execute.return_value.fetchall.return_value = []
        store = _store(connection)

        store.history("certs")

        assert connection.execute.call_args.args[1] == ["certs", 10]  # noqa: PLR2004


class TestRowToCheck:
    def test_maps_every_field(self) -> None:
        from hexawyn.domain.services.schedule.duckdb_schedule_store import _row_to_check

        result = _row_to_check(_check_row())

        assert result == CronCheck(
            name="certs",
            schedule="0 */6 * * *",
            use_case="certs_list",
            params={"env": "prod"},
            enabled=True,
            notify_policy="on_change",
            destinations=["slack", "teams"],
            timeout_seconds=300,
        )

    def test_defaults_for_nullable_cells(self) -> None:
        from hexawyn.domain.services.schedule.duckdb_schedule_store import _row_to_check

        result = _row_to_check(
            _check_row(
                params=None, enabled=0, notify_policy=None, destinations=None, timeout_seconds=0
            )
        )

        assert result.params == {}
        assert result.enabled is False
        assert result.notify_policy == "on_change"
        assert result.destinations == ["slack"]
        assert result.timeout_seconds == 300  # noqa: PLR2004

    def test_params_guard_uses_params_column_not_enabled(self) -> None:
        from hexawyn.domain.services.schedule.duckdb_schedule_store import _row_to_check

        # params falsy + enabled truthy: mutant (if row[4]) would parse enabled as JSON
        result = _row_to_check(
            _check_row(
                params="",
                enabled=1,
                notify_policy="on_change",
                destinations='["s"]',
                timeout_seconds=300,
            )
        )

        assert result.params == {}

    def test_enabled_guard_uses_enabled_column_not_notify_policy(self) -> None:
        from hexawyn.domain.services.schedule.duckdb_schedule_store import _row_to_check

        # enabled falsy + notify_policy truthy: mutant (bool(row[5])) -> "on_change" truthy
        result = _row_to_check(
            _check_row(
                params="{}",
                enabled=0,
                notify_policy="always",
                destinations='["s"]',
                timeout_seconds=300,
            )
        )

        assert result.enabled is False

    def test_notify_policy_guard_uses_own_column(self) -> None:
        from hexawyn.domain.services.schedule.duckdb_schedule_store import _row_to_check

        # notify_policy falsy + destinations truthy: mutant (if row[6]) -> str("") = ""
        result = _row_to_check(
            _check_row(
                params="{}", enabled=1, notify_policy="", destinations='["s"]', timeout_seconds=300
            )
        )

        assert result.notify_policy == "on_change"

    def test_destinations_guard_uses_own_column(self) -> None:
        from hexawyn.domain.services.schedule.duckdb_schedule_store import _row_to_check

        # destinations falsy + timeout truthy: mutant (if row[7]) would json-parse timeout
        result = _row_to_check(
            _check_row(
                params="{}",
                enabled=1,
                notify_policy="on_change",
                destinations="",
                timeout_seconds=300,
            )
        )

        assert result.destinations == ["slack"]


class TestRowToResult:
    def test_maps_every_field(self) -> None:
        from hexawyn.domain.services.schedule.duckdb_schedule_store import _row_to_result

        result = _row_to_result(_result_row())

        assert result == CheckResult(
            check_name="certs",
            phase="success",
            started_at=datetime(2026, 1, 2, 3, 4, 5, tzinfo=UTC),
            finished_at=datetime(2026, 1, 2, 4, 0, 0, tzinfo=UTC),
            duration_ms=1200,
            summary="ok",
            payload_digest="abc123",
            changed=False,
            error_message=None,
            notified=False,
        )

    def test_defaults_for_nullable_cells(self) -> None:
        from hexawyn.domain.services.schedule.duckdb_schedule_store import _row_to_result

        result = _row_to_result(
            _result_row(
                started_at=None,
                finished_at=None,
                duration_ms=None,
                summary=None,
                changed=0,
                error_message=None,
                notified=0,
            )
        )

        assert result.started_at is not None
        assert result.finished_at is None
        assert result.duration_ms is None
        assert result.summary == ""
        assert result.changed is False
        assert result.error_message is None
        assert result.notified is False

    def test_fallback_started_at_is_utc_aware(self) -> None:
        from hexawyn.domain.services.schedule.duckdb_schedule_store import _row_to_result

        result = _row_to_result(_result_row(started_at=None))

        assert result.started_at.tzinfo is UTC

    def test_started_guard_uses_started_column_not_finished(self) -> None:
        from hexawyn.domain.services.schedule.duckdb_schedule_store import _row_to_result

        # started_at falsy + finished_at truthy: mutant (if row[3]) -> fromisoformat("") crash
        result = _row_to_result(
            _result_row(started_at=None, finished_at="2026-01-02T04:00:00+00:00")
        )

        assert result.started_at is not None
        assert result.finished_at == datetime(2026, 1, 2, 4, 0, 0, tzinfo=UTC)

    def test_finished_guard_uses_finished_column_not_duration(self) -> None:
        from hexawyn.domain.services.schedule.duckdb_schedule_store import _row_to_result

        # finished_at falsy + duration truthy: mutant guard row[3] -> row[4] crashes
        result = _row_to_result(_result_row(finished_at=None, duration_ms=1200))

        assert result.finished_at is None
        assert result.duration_ms == 1200  # noqa: PLR2004

    def test_duration_guard_uses_duration_column_not_summary(self) -> None:
        from hexawyn.domain.services.schedule.duckdb_schedule_store import _row_to_result

        # duration_ms falsy + summary truthy: mutant (if row[5] is not None) -> int("ok") crash
        result = _row_to_result(_result_row(duration_ms=None, summary="ok", payload_digest="d"))

        assert result.duration_ms is None
        assert result.summary == "ok"

    def test_changed_column_truthy(self) -> None:
        from hexawyn.domain.services.schedule.duckdb_schedule_store import _row_to_result

        result = _row_to_result(_result_row(changed=1, error_message="boom", notified=1))

        assert result.changed is True
        assert result.error_message == "boom"
        assert result.notified is True

    def test_error_message_guard_uses_error_column_not_notified(self) -> None:
        from hexawyn.domain.services.schedule.duckdb_schedule_store import _row_to_result

        # error falsy + notified truthy: mutant (if row[9]) -> str(row[8])="None"
        result = _row_to_result(_result_row(error_message=None, notified=1))

        assert result.error_message is None
        assert result.notified is True

    def test_changed_column_not_confused_with_error_message(self) -> None:
        from hexawyn.domain.services.schedule.duckdb_schedule_store import _row_to_result

        # changed falsy + error truthy: mutant (bool(row[8])) -> True
        result = _row_to_result(_result_row(changed=0, error_message="boom"))

        assert result.changed is False
        assert result.error_message == "boom"

    def test_notified_column_not_confused_with_error_message(self) -> None:
        from hexawyn.domain.services.schedule.duckdb_schedule_store import _row_to_result

        # error_message index 8, notified index 9 — error truthy must map exactly
        result = _row_to_result(_result_row(error_message="boom", notified=0, changed=1))

        assert result.error_message == "boom"
        assert result.notified is False
        assert result.changed is True
