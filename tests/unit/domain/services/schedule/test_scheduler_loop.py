from __future__ import annotations

from datetime import UTC, datetime, timedelta
from unittest.mock import MagicMock

from hexawyn.domain.models.schedule import CheckPhase, CheckResult, CronCheck
from hexawyn.domain.services.schedule.scheduler_loop import SchedulerLoop


def _enabled_check(name: str, schedule: str = "0 0 * * *") -> CronCheck:
    return CronCheck(name=name, schedule=schedule, use_case="certs_list", enabled=True)


def _disabled_check(name: str) -> CronCheck:
    return CronCheck(name=name, schedule="0 0 * * *", use_case="certs_list", enabled=False)


def _success_result(name: str) -> CheckResult:
    return CheckResult(
        check_name=name,
        phase=CheckPhase.SUCCESS.value,
        started_at=datetime.now(UTC),
        payload_digest="d",
    )


def _changed_result(name: str) -> CheckResult:
    return CheckResult(
        check_name=name,
        phase=CheckPhase.ALERTING.value,
        started_at=datetime.now(UTC),
        payload_digest="d",
        changed=True,
    )


def _runner(return_values: list[CheckResult] | None = None) -> MagicMock:
    runner = MagicMock()
    if return_values:
        runner.execute.side_effect = return_values
    return runner


class TestSchedulerLoop:
    def test_tick_skips_checks_not_yet_due(self) -> None:
        start = datetime(2026, 8, 20, 9, 0, tzinfo=UTC)
        clock = {"now": start}
        loop = SchedulerLoop(runner=_runner(), now=lambda: clock["now"])
        check = _enabled_check("daily")  # 0 0 * * * = 1440 min
        loop.prime([check])

        clock["now"] = start + timedelta(hours=12)  # 720 min < 1440
        results = loop.tick([check])

        assert results == []

    def test_tick_executes_due_check(self) -> None:
        start = datetime(2026, 8, 20, 9, 0, tzinfo=UTC)
        clock = {"now": start}
        runner = _runner(return_values=[_success_result("daily")])
        loop = SchedulerLoop(runner=runner, now=lambda: clock["now"])
        check = _enabled_check("daily")
        loop.prime([check])

        clock["now"] = start + timedelta(hours=24)
        results = loop.tick([check])

        assert len(results) == 1  # noqa: PLR2004
        runner.execute.assert_called_once_with(check)

    def test_tick_executes_once_per_interval(self) -> None:
        start = datetime(2026, 8, 20, 9, 0, tzinfo=UTC)
        clock = {"now": start}
        runner = _runner(return_values=[_success_result("daily"), _success_result("daily")])
        loop = SchedulerLoop(runner=runner, now=lambda: clock["now"])
        check = _enabled_check("daily")
        loop.prime([check])

        clock["now"] = start + timedelta(hours=24)
        loop.tick([check])
        clock["now"] = start + timedelta(hours=47)  # < 48h depuis le premier run
        loop.tick([check])
        clock["now"] = start + timedelta(hours=72)
        loop.tick([check])

        assert runner.execute.call_count == 2  # noqa: PLR2004

    def test_tick_skips_disabled_checks(self) -> None:
        loop = SchedulerLoop(runner=_runner())
        loop.prime([_disabled_check("off")])
        results = loop.tick([_disabled_check("off")])
        assert results == []

    def test_tick_skips_unknown_schedule(self) -> None:
        start = datetime(2026, 8, 20, 9, 0, tzinfo=UTC)
        clock = {"now": start}
        loop = SchedulerLoop(runner=_runner(), now=lambda: clock["now"])
        check = _enabled_check("custom", schedule="30 2 * * *")  # cron_to_minutes == 0
        loop.prime([check])

        clock["now"] = start + timedelta(days=2)
        results = loop.tick([check])

        assert results == []

    def test_tick_without_prime_runs_when_due(self) -> None:
        start = datetime(2026, 8, 20, 9, 0, tzinfo=UTC)
        runner = _runner(return_values=[_success_result("daily")])
        loop = SchedulerLoop(runner=runner, now=lambda: start)
        check = _enabled_check("daily")

        results = loop.tick([check])

        assert len(results) == 1  # noqa: PLR2004
        runner.execute.assert_called_once_with(check)

    def test_tick_returns_executed_results(self) -> None:
        start = datetime(2026, 8, 20, 9, 0, tzinfo=UTC)
        clock = {"now": start}
        runner = _runner(return_values=[_changed_result("daily")])
        loop = SchedulerLoop(runner=runner, now=lambda: clock["now"])
        check = _enabled_check("daily")
        loop.prime([check])

        clock["now"] = start + timedelta(hours=24)
        results = loop.tick([check])

        assert results[0].check_name == "daily"
        assert results[0].changed is True
