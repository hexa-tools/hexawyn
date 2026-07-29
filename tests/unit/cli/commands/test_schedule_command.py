from __future__ import annotations

from datetime import UTC, datetime
from unittest.mock import MagicMock, patch

from click.testing import CliRunner
from hexawyn.cli.commands.schedule_command import schedule
from hexawyn.domain.models.schedule import CheckPhase, CheckResult, CronCheck


class TestScheduleList:
    def test_list_shows_empty_when_no_checks(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.schedule_source.YamlScheduleSource"
        ) as mock_source_cls:
            mock_source = MagicMock()
            mock_source.load_checks.return_value = []
            mock_source_cls.return_value = mock_source

            runner = CliRunner()
            result = runner.invoke(schedule, ["list"])

            assert result.exit_code == 0  # noqa: PLR2004
            assert "No scheduled checks" in result.output

    def test_list_shows_checks_when_present(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.schedule_source.YamlScheduleSource"
        ) as mock_source_cls:
            mock_source = MagicMock()
            mock_source.load_checks.return_value = [
                CronCheck(
                    name="test-check",
                    schedule="0 */6 * * *",
                    use_case="health_check",
                    enabled=True,
                    notify_policy="always",
                )
            ]
            mock_source_cls.return_value = mock_source

            runner = CliRunner()
            result = runner.invoke(schedule, ["list"])

            assert result.exit_code == 0  # noqa: PLR2004
            assert "test-check" in result.output
            assert "health_check" in result.output
            assert "0 */6 * * *" in result.output

    def test_list_shows_disabled_status(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.schedule_source.YamlScheduleSource"
        ) as mock_source_cls:
            mock_source = MagicMock()
            mock_source.load_checks.return_value = [
                CronCheck(
                    name="disabled-check",
                    schedule="0 0 * * *",
                    use_case="certs_list",
                    enabled=False,
                )
            ]
            mock_source_cls.return_value = mock_source

            runner = CliRunner()
            result = runner.invoke(schedule, ["list"])

            assert result.exit_code == 0  # noqa: PLR2004
            assert "disabled-check" in result.output


class TestScheduleCreate:
    def test_create_with_every_shortcut(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.schedule_source.YamlScheduleSource"
        ) as mock_source_cls:
            mock_source = MagicMock()
            mock_source.load_checks.return_value = []
            mock_source_cls.return_value = mock_source

            runner = CliRunner()
            result = runner.invoke(
                schedule,
                [
                    "create",
                    "--name",
                    "test-check",
                    "--use-case",
                    "health_check",
                    "--every",
                    "6h",
                ],
            )

            assert result.exit_code == 0  # noqa: PLR2004
            assert "test-check" in result.output

    def test_create_with_cron_expression(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.schedule_source.YamlScheduleSource"
        ) as mock_source_cls:
            mock_source = MagicMock()
            mock_source.load_checks.return_value = []
            mock_source_cls.return_value = mock_source

            runner = CliRunner()
            result = runner.invoke(
                schedule,
                [
                    "create",
                    "--name",
                    "nightly",
                    "--use-case",
                    "certs_list",
                    "--cron",
                    "0 2 * * *",
                ],
            )

            assert result.exit_code == 0  # noqa: PLR2004

    def test_create_with_namespace_filter(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.schedule_source.YamlScheduleSource"
        ) as mock_source_cls:
            mock_source = MagicMock()
            mock_source.load_checks.return_value = []
            mock_source_cls.return_value = mock_source

            runner = CliRunner()
            result = runner.invoke(
                schedule,
                [
                    "create",
                    "--name",
                    "ns-check",
                    "--use-case",
                    "health_check",
                    "--every",
                    "1h",
                    "--namespace",
                    "production",
                ],
            )

            assert result.exit_code == 0  # noqa: PLR2004

    def test_create_overwrites_existing_check(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.schedule_source.YamlScheduleSource"
        ) as mock_source_cls:
            existing = CronCheck(name="dup", schedule="0 * * * *", use_case="old")
            mock_source = MagicMock()
            mock_source.load_checks.return_value = [existing]
            mock_source_cls.return_value = mock_source

            runner = CliRunner()
            result = runner.invoke(
                schedule,
                [
                    "create",
                    "--name",
                    "dup",
                    "--use-case",
                    "new_case",
                    "--every",
                    "12h",
                ],
            )

            assert result.exit_code == 0  # noqa: PLR2004
            saved_checks = mock_source.save_checks.call_args[0][0]
            assert len(saved_checks) == 1  # noqa: PLR2004
            assert saved_checks[0].use_case == "new_case"

    def test_create_deduplicates_by_name(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.schedule_source.YamlScheduleSource"
        ) as mock_source_cls:
            existing_a = CronCheck(name="alpha", schedule="0 * * * *", use_case="a")
            existing_b = CronCheck(name="beta", schedule="0 * * * *", use_case="b")
            mock_source = MagicMock()
            mock_source.load_checks.return_value = [existing_a, existing_b]
            mock_source_cls.return_value = mock_source

            runner = CliRunner()
            result = runner.invoke(
                schedule,
                [
                    "create",
                    "--name",
                    "alpha",
                    "--use-case",
                    "a_v2",
                    "--every",
                    "24h",
                ],
            )

            assert result.exit_code == 0  # noqa: PLR2004
            saved_checks = mock_source.save_checks.call_args[0][0]
            assert len(saved_checks) == 2  # noqa: PLR2004
            assert saved_checks[0].name == "beta"
            assert saved_checks[1].name == "alpha"


class TestScheduleGet:
    def test_get_shows_check_details(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.schedule_source.YamlScheduleSource"
        ) as mock_source_cls:
            mock_source = MagicMock()
            mock_source.load_checks.return_value = [
                CronCheck(
                    name="my-check",
                    schedule="0 */6 * * *",
                    use_case="health_check",
                    enabled=True,
                    notify_policy="on_change",
                    destinations=["slack", "email"],
                )
            ]
            mock_source_cls.return_value = mock_source

            runner = CliRunner()
            result = runner.invoke(schedule, ["get", "my-check"])

            assert result.exit_code == 0  # noqa: PLR2004
            assert "my-check" in result.output
            assert "health_check" in result.output

    def test_get_not_found_shows_error(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.schedule_source.YamlScheduleSource"
        ) as mock_source_cls:
            mock_source = MagicMock()
            mock_source.load_checks.return_value = []
            mock_source_cls.return_value = mock_source

            runner = CliRunner()
            result = runner.invoke(schedule, ["get", "nope"])

            assert result.exit_code == 0  # noqa: PLR2004
            assert "not found" in result.output


class TestScheduleStatus:
    def test_status_shows_total_and_enabled(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.schedule_source.YamlScheduleSource"
        ) as mock_source_cls:
            mock_source = MagicMock()
            mock_source.load_checks.return_value = [
                CronCheck(name="a", schedule="* * * * *", use_case="x", enabled=True),
                CronCheck(name="b", schedule="* * * * *", use_case="y", enabled=False),
                CronCheck(name="c", schedule="* * * * *", use_case="z", enabled=True),
            ]
            mock_source_cls.return_value = mock_source

            runner = CliRunner()
            result = runner.invoke(schedule, ["status"])

            assert result.exit_code == 0  # noqa: PLR2004
            assert "Total checks:" in result.output
            assert "Enabled:" in result.output
            assert "Disabled:" in result.output

    def test_status_with_no_checks(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.schedule_source.YamlScheduleSource"
        ) as mock_source_cls:
            mock_source = MagicMock()
            mock_source.load_checks.return_value = []
            mock_source_cls.return_value = mock_source

            runner = CliRunner()
            result = runner.invoke(schedule, ["status"])

            assert result.exit_code == 0  # noqa: PLR2004
            assert "Total checks:     0" in result.output


class TestScheduleEnable:
    def test_enable_toggles_check(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.schedule_source.YamlScheduleSource"
        ) as mock_source_cls:
            check = CronCheck(name="my-check", schedule="* * * * *", use_case="x", enabled=False)
            mock_source = MagicMock()
            mock_source.load_checks.return_value = [check]
            mock_source_cls.return_value = mock_source

            runner = CliRunner()
            result = runner.invoke(schedule, ["enable", "my-check"])

            assert result.exit_code == 0  # noqa: PLR2004
            assert "enabled" in result.output
            saved_checks = mock_source.save_checks.call_args[0][0]
            assert saved_checks[0].enabled is True

    def test_enable_not_found_shows_error(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.schedule_source.YamlScheduleSource"
        ) as mock_source_cls:
            mock_source = MagicMock()
            mock_source.load_checks.return_value = []
            mock_source_cls.return_value = mock_source

            runner = CliRunner()
            result = runner.invoke(schedule, ["enable", "nope"])

            assert result.exit_code == 0  # noqa: PLR2004
            assert "not found" in result.output


class TestScheduleDisable:
    def test_disable_toggles_check(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.schedule_source.YamlScheduleSource"
        ) as mock_source_cls:
            check = CronCheck(name="my-check", schedule="* * * * *", use_case="x", enabled=True)
            mock_source = MagicMock()
            mock_source.load_checks.return_value = [check]
            mock_source_cls.return_value = mock_source

            runner = CliRunner()
            result = runner.invoke(schedule, ["disable", "my-check"])

            assert result.exit_code == 0  # noqa: PLR2004
            assert "disabled" in result.output
            saved_checks = mock_source.save_checks.call_args[0][0]
            assert saved_checks[0].enabled is False


class TestScheduleDelete:
    def test_delete_removes_check(self) -> None:
        with (
            patch(
                "hexawyn.infrastructure.config.schedule_source.YamlScheduleSource"
            ) as mock_source_cls,
            patch("hexawyn.infrastructure.memory.duckdb_client.get_connection") as mock_get_conn,
            patch(
                "hexawyn.domain.services.schedule.duckdb_schedule_store.DuckDBScheduleStore"
            ) as mock_store_cls,
        ):
            mock_source = MagicMock()
            mock_source.load_checks.return_value = [
                CronCheck(name="keep", schedule="* * * * *", use_case="x"),
                CronCheck(name="delete-me", schedule="* * * * *", use_case="y"),
            ]
            mock_source_cls.return_value = mock_source
            mock_conn = MagicMock()
            mock_get_conn.return_value = mock_conn
            mock_store = MagicMock()
            mock_store_cls.return_value = mock_store

            runner = CliRunner()
            result = runner.invoke(schedule, ["delete", "delete-me"])

            assert result.exit_code == 0  # noqa: PLR2004
            assert "deleted" in result.output
            saved_checks = mock_source.save_checks.call_args[0][0]
            assert len(saved_checks) == 1  # noqa: PLR2004
            assert saved_checks[0].name == "keep"
            mock_store.delete_check.assert_called_once_with("delete-me")


class TestScheduleHistory:
    def test_history_shows_results(self) -> None:
        with (
            patch("hexawyn.infrastructure.memory.duckdb_client.get_connection") as mock_get_conn,
            patch(
                "hexawyn.domain.services.schedule.duckdb_schedule_store.DuckDBScheduleStore"
            ) as mock_store_cls,
        ):
            mock_conn = MagicMock()
            mock_get_conn.return_value = mock_conn
            mock_store = MagicMock()
            mock_store.history.return_value = [
                CheckResult(
                    check_name="my-check",
                    phase=CheckPhase.SUCCESS.value,
                    started_at=datetime(2026, 1, 15, 12, 0, 0, tzinfo=UTC),
                    payload_digest="abc123",
                    summary="All OK",
                    changed=True,
                )
            ]
            mock_store_cls.return_value = mock_store

            runner = CliRunner()
            result = runner.invoke(schedule, ["history", "my-check"])

            assert result.exit_code == 0  # noqa: PLR2004
            assert "All OK" in result.output

    def test_history_empty_shows_message(self) -> None:
        with (
            patch("hexawyn.infrastructure.memory.duckdb_client.get_connection") as mock_get_conn,
            patch(
                "hexawyn.domain.services.schedule.duckdb_schedule_store.DuckDBScheduleStore"
            ) as mock_store_cls,
        ):
            mock_conn = MagicMock()
            mock_get_conn.return_value = mock_conn
            mock_store = MagicMock()
            mock_store.history.return_value = []
            mock_store_cls.return_value = mock_store

            runner = CliRunner()
            result = runner.invoke(schedule, ["history", "empty-check"])

            assert result.exit_code == 0  # noqa: PLR2004
            assert "No history" in result.output


class TestScheduleRun:
    def test_run_not_found_shows_error(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.schedule_source.YamlScheduleSource"
        ) as mock_source_cls:
            mock_source = MagicMock()
            mock_source.load_checks.return_value = []
            mock_source_cls.return_value = mock_source

            runner = CliRunner()
            result = runner.invoke(schedule, ["run", "nope"])

            assert result.exit_code == 0  # noqa: PLR2004
            assert "not found" in result.output

    def test_run_executes_check(self) -> None:
        with (
            patch(
                "hexawyn.infrastructure.config.schedule_source.YamlScheduleSource"
            ) as mock_source_cls,
            patch("hexawyn.infrastructure.memory.duckdb_client.get_connection") as mock_get_conn,
            patch(
                "hexawyn.domain.services.schedule.duckdb_schedule_store.DuckDBScheduleStore"
            ) as mock_store_cls,
            patch(
                "hexawyn.domain.services.schedule.check_runner.CheckRunnerUseCase"
            ) as mock_runner_cls,
            patch("hexawyn.infrastructure.config.schedule_registry.build_registry") as mock_reg,
        ):
            mock_reg.return_value = {}
            check = CronCheck(
                name="urgent",
                schedule="* * * * *",
                use_case="health_check",
                enabled=True,
            )
            mock_source = MagicMock()
            mock_source.load_checks.return_value = [check]
            mock_source_cls.return_value = mock_source
            mock_conn = MagicMock()
            mock_get_conn.return_value = mock_conn
            mock_store = MagicMock()
            mock_store_cls.return_value = mock_store

            mock_result = MagicMock()
            mock_result.changed = False
            mock_result.phase = CheckPhase.SUCCESS.value
            mock_result.summary = "Everything looks great"
            mock_result.error_message = None

            mock_runner = MagicMock()
            mock_runner.execute.return_value = mock_result
            mock_runner_cls.return_value = mock_runner

            runner = CliRunner()
            result = runner.invoke(schedule, ["run", "urgent"])

            assert result.exit_code == 0  # noqa: PLR2004
            assert "Everything looks great" in result.output

    def test_run_shows_error_message_when_present(self) -> None:
        with (
            patch(
                "hexawyn.infrastructure.config.schedule_source.YamlScheduleSource"
            ) as mock_source_cls,
            patch("hexawyn.infrastructure.memory.duckdb_client.get_connection") as mock_get_conn,
            patch(
                "hexawyn.domain.services.schedule.duckdb_schedule_store.DuckDBScheduleStore"
            ) as mock_store_cls,
            patch(
                "hexawyn.domain.services.schedule.check_runner.CheckRunnerUseCase"
            ) as mock_runner_cls,
            patch("hexawyn.infrastructure.config.schedule_registry.build_registry") as mock_reg,
        ):
            mock_reg.return_value = {}
            check = CronCheck(name="failing", schedule="* * * * *", use_case="x", enabled=True)
            mock_source = MagicMock()
            mock_source.load_checks.return_value = [check]
            mock_source_cls.return_value = mock_source
            mock_conn = MagicMock()
            mock_get_conn.return_value = mock_conn
            mock_store = MagicMock()
            mock_store_cls.return_value = mock_store

            mock_result = MagicMock()
            mock_result.changed = False
            mock_result.phase = CheckPhase.FAILED.value
            mock_result.summary = "Check failed"
            mock_result.error_message = "connection timeout"

            mock_runner = MagicMock()
            mock_runner.execute.return_value = mock_result
            mock_runner_cls.return_value = mock_runner

            runner = CliRunner()
            result = runner.invoke(schedule, ["run", "failing"])

            assert result.exit_code == 0  # noqa: PLR2004
            assert "connection timeout" in result.output


class TestScheduleStart:
    def test_start_disabled_env_shows_warning(self) -> None:
        runner = CliRunner()
        result = runner.invoke(schedule, ["start"], env={"HEXAWYN_SCHEDULER_ENABLED": "false"})

        assert result.exit_code == 0  # noqa: PLR2004
        assert "HEXAWYN_SCHEDULER_ENABLED=false" in result.output

    def test_start_dry_run_shows_checks(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.schedule_source.YamlScheduleSource"
        ) as mock_source_cls:
            mock_source = MagicMock()
            mock_source.load_checks.return_value = [
                CronCheck(
                    name="c1",
                    schedule="0 */6 * * *",
                    use_case="certs_list",
                    enabled=True,
                ),
                CronCheck(
                    name="c2",
                    schedule="0 0 * * *",
                    use_case="health_check",
                    enabled=True,
                ),
            ]
            mock_source_cls.return_value = mock_source

            runner = CliRunner()
            result = runner.invoke(
                schedule,
                ["start", "--dry-run"],
                env={"HEXAWYN_SCHEDULER_ENABLED": "true"},
            )

            assert result.exit_code == 0  # noqa: PLR2004
            assert "c1" in result.output
            assert "c2" in result.output

    def test_start_no_enabled_checks(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.schedule_source.YamlScheduleSource"
        ) as mock_source_cls:
            mock_source = MagicMock()
            mock_source.load_checks.return_value = []
            mock_source_cls.return_value = mock_source

            runner = CliRunner()
            result = runner.invoke(schedule, ["start"], env={"HEXAWYN_SCHEDULER_ENABLED": "true"})

            assert result.exit_code == 0  # noqa: PLR2004
            assert "No enabled checks" in result.output

    def test_start_filters_disabled_checks(self) -> None:
        with patch(
            "hexawyn.infrastructure.config.schedule_source.YamlScheduleSource"
        ) as mock_source_cls:
            mock_source = MagicMock()
            mock_source.load_checks.return_value = [
                CronCheck(name="enabled1", schedule="* * * * *", use_case="x", enabled=True),
                CronCheck(name="disabled1", schedule="* * * * *", use_case="y", enabled=False),
            ]
            mock_source_cls.return_value = mock_source

            runner = CliRunner()
            result = runner.invoke(
                schedule, ["start", "--dry-run"], env={"HEXAWYN_SCHEDULER_ENABLED": "true"}
            )

            assert result.exit_code == 0  # noqa: PLR2004
            assert "enabled1" in result.output
            assert "disabled1" not in result.output


class TestScheduleHelp:
    def test_schedule_group_help(self) -> None:
        runner = CliRunner()
        result = runner.invoke(schedule, ["--help"])

        assert result.exit_code == 0  # noqa: PLR2004
        assert "schedule" in result.output.lower()
