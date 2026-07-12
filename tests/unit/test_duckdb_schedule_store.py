from unittest.mock import MagicMock, patch

from hexawyn.domain.models.schedule import CheckResult, CronCheck


class TestDuckDBScheduleStore:
    def test_save_and_get_check(self) -> None:
        with patch("duckdb.connect") as mock_connect:
            conn = MagicMock()
            mock_connect.return_value = conn
            from hexawyn.domain.services.schedule.duckdb_schedule_store import (
                DuckDBScheduleStore,
            )

            store = DuckDBScheduleStore(connection=conn)
            check = CronCheck(name="certs", schedule="0 */6 * * *", use_case="certs_list")

            store.save_check(check)

            conn.execute.assert_called()

    def test_list_checks_returns_list(self) -> None:
        with patch("duckdb.connect"):
            conn = MagicMock()
            conn.execute.return_value.fetchall.return_value = [
                ("certs", "0 */6 * * *", "certs_list", "{}", True, "on_change", '["slack"]', 300),
            ]
            from hexawyn.domain.services.schedule.duckdb_schedule_store import (
                DuckDBScheduleStore,
            )

            store = DuckDBScheduleStore(connection=conn)
            result = store.list_checks()

            assert len(result) == 1
            assert result[0].name == "certs"

    def test_history_returns_results(self) -> None:
        from datetime import UTC, datetime

        with patch("duckdb.connect"):
            conn = MagicMock()
            conn.execute.return_value.fetchall.return_value = [
                (
                    "certs",
                    "success",
                    datetime.now(UTC).isoformat(),
                    datetime.now(UTC).isoformat(),
                    100,
                    "ok",
                    "abc",
                    False,
                    None,
                    False,
                ),
            ]
            from hexawyn.domain.services.schedule.duckdb_schedule_store import (
                DuckDBScheduleStore,
            )

            store = DuckDBScheduleStore(connection=conn)
            result = store.history("certs", limit=5)

            assert len(result) == 1
            assert result[0].check_name == "certs"

    def test_delete_check(self) -> None:
        with patch("duckdb.connect"):
            conn = MagicMock()
            from hexawyn.domain.services.schedule.duckdb_schedule_store import (
                DuckDBScheduleStore,
            )

            store = DuckDBScheduleStore(connection=conn)
            store.delete_check("certs")

            conn.execute.assert_called()

    def test_last_result_returns_none_when_none(self) -> None:
        with patch("duckdb.connect"):
            conn = MagicMock()
            conn.execute.return_value.fetchone.return_value = None
            from hexawyn.domain.services.schedule.duckdb_schedule_store import (
                DuckDBScheduleStore,
            )

            store = DuckDBScheduleStore(connection=conn)
            result = store.last_result("certs")

            assert result is None

    def test_get_check_returns_none_when_absent(self) -> None:
        with patch("duckdb.connect"):
            conn = MagicMock()
            conn.execute.return_value.fetchone.return_value = None
            from hexawyn.domain.services.schedule.duckdb_schedule_store import (
                DuckDBScheduleStore,
            )

            store = DuckDBScheduleStore(connection=conn)
            result = store.get_check("unknown")

            assert result is None

    def test_save_result_inserts_row(self) -> None:
        from datetime import UTC, datetime

        with patch("duckdb.connect"):
            conn = MagicMock()
            from hexawyn.domain.services.schedule.duckdb_schedule_store import (
                DuckDBScheduleStore,
            )

            store = DuckDBScheduleStore(connection=conn)
            store.save_result(
                CheckResult(
                    check_name="test",
                    phase="success",
                    started_at=datetime.now(UTC),
                    payload_digest="abc",
                )
            )

            conn.execute.assert_called()
