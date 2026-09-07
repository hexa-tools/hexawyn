"""Scheduler loop — evaluates and runs due scheduled checks.

Extracts the periodic evaluation out of the CLI daemon into a testable
service: each tick() executes the enabled checks whose interval has elapsed.
The CLI keeps only a thin `while True: tick() + sleep` loop.
"""

from __future__ import annotations

from collections.abc import Callable
from datetime import UTC, datetime

from hexawyn.domain.models.schedule import CheckResult, CronCheck
from hexawyn.domain.services.schedule.check_runner import CheckRunnerUseCase
from hexawyn.domain.services.schedule.cron_shortcut import cron_to_minutes

Now = Callable[[], datetime]


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁSchedulerLoopǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁSchedulerLoopǁprime__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSchedulerLoopǁtick__mutmut: MutantDict = {}  # type: ignore


class SchedulerLoop:
    """Runs due checks on each tick using an injectable clock."""

    @_mutmut_mutated(mutants_xǁSchedulerLoopǁ__init____mutmut)
    def __init__(
        self,
        runner: CheckRunnerUseCase,
        now: Now = lambda: datetime.now(UTC),
    ) -> None:
        self._runner = runner
        self._now = now
        self._last_run: dict[str, datetime] = {}

    def xǁSchedulerLoopǁ__init____mutmut_orig(
        self,
        runner: CheckRunnerUseCase,
        now: Now = lambda: datetime.now(UTC),
    ) -> None:
        self._runner = runner
        self._now = now
        self._last_run: dict[str, datetime] = {}

    def xǁSchedulerLoopǁ__init____mutmut_1(
        self,
        runner: CheckRunnerUseCase,
        now: Now = lambda: datetime.now(UTC),
    ) -> None:
        self._runner = None
        self._now = now
        self._last_run: dict[str, datetime] = {}

    def xǁSchedulerLoopǁ__init____mutmut_2(
        self,
        runner: CheckRunnerUseCase,
        now: Now = lambda: datetime.now(UTC),
    ) -> None:
        self._runner = runner
        self._now = None
        self._last_run: dict[str, datetime] = {}

    def xǁSchedulerLoopǁ__init____mutmut_3(
        self,
        runner: CheckRunnerUseCase,
        now: Now = lambda: datetime.now(UTC),
    ) -> None:
        self._runner = runner
        self._now = now
        self._last_run: dict[str, datetime] = None

    @_mutmut_mutated(mutants_xǁSchedulerLoopǁprime__mutmut)
    def prime(self, checks: list[CronCheck]) -> None:
        """Mark every check as just started so nothing runs on the first tick."""
        now = self._now()
        self._last_run = {check.name: now for check in checks}

    def xǁSchedulerLoopǁprime__mutmut_orig(self, checks: list[CronCheck]) -> None:
        """Mark every check as just started so nothing runs on the first tick."""
        now = self._now()
        self._last_run = {check.name: now for check in checks}

    def xǁSchedulerLoopǁprime__mutmut_1(self, checks: list[CronCheck]) -> None:
        """Mark every check as just started so nothing runs on the first tick."""
        now = None
        self._last_run = {check.name: now for check in checks}

    def xǁSchedulerLoopǁprime__mutmut_2(self, checks: list[CronCheck]) -> None:
        """Mark every check as just started so nothing runs on the first tick."""
        now = self._now()
        self._last_run = None

    @_mutmut_mutated(mutants_xǁSchedulerLoopǁtick__mutmut)
    def tick(self, checks: list[CronCheck]) -> list[CheckResult]:
        """Execute the enabled checks whose interval has elapsed."""
        executed: list[CheckResult] = []
        now = self._now()
        for check in checks:
            if not check.enabled:
                continue
            interval_minutes = cron_to_minutes(check.schedule)
            if interval_minutes <= 0:
                continue
            last = self._last_run.get(check.name)
            if last is not None and _elapsed_minutes(now, last) < interval_minutes:
                continue
            executed.append(self._runner.execute(check))
            self._last_run[check.name] = now
        return executed

    def xǁSchedulerLoopǁtick__mutmut_orig(self, checks: list[CronCheck]) -> list[CheckResult]:
        """Execute the enabled checks whose interval has elapsed."""
        executed: list[CheckResult] = []
        now = self._now()
        for check in checks:
            if not check.enabled:
                continue
            interval_minutes = cron_to_minutes(check.schedule)
            if interval_minutes <= 0:
                continue
            last = self._last_run.get(check.name)
            if last is not None and _elapsed_minutes(now, last) < interval_minutes:
                continue
            executed.append(self._runner.execute(check))
            self._last_run[check.name] = now
        return executed

    def xǁSchedulerLoopǁtick__mutmut_1(self, checks: list[CronCheck]) -> list[CheckResult]:
        """Execute the enabled checks whose interval has elapsed."""
        executed: list[CheckResult] = None
        now = self._now()
        for check in checks:
            if not check.enabled:
                continue
            interval_minutes = cron_to_minutes(check.schedule)
            if interval_minutes <= 0:
                continue
            last = self._last_run.get(check.name)
            if last is not None and _elapsed_minutes(now, last) < interval_minutes:
                continue
            executed.append(self._runner.execute(check))
            self._last_run[check.name] = now
        return executed

    def xǁSchedulerLoopǁtick__mutmut_2(self, checks: list[CronCheck]) -> list[CheckResult]:
        """Execute the enabled checks whose interval has elapsed."""
        executed: list[CheckResult] = []
        now = None
        for check in checks:
            if not check.enabled:
                continue
            interval_minutes = cron_to_minutes(check.schedule)
            if interval_minutes <= 0:
                continue
            last = self._last_run.get(check.name)
            if last is not None and _elapsed_minutes(now, last) < interval_minutes:
                continue
            executed.append(self._runner.execute(check))
            self._last_run[check.name] = now
        return executed

    def xǁSchedulerLoopǁtick__mutmut_3(self, checks: list[CronCheck]) -> list[CheckResult]:
        """Execute the enabled checks whose interval has elapsed."""
        executed: list[CheckResult] = []
        now = self._now()
        for check in checks:
            if check.enabled:
                continue
            interval_minutes = cron_to_minutes(check.schedule)
            if interval_minutes <= 0:
                continue
            last = self._last_run.get(check.name)
            if last is not None and _elapsed_minutes(now, last) < interval_minutes:
                continue
            executed.append(self._runner.execute(check))
            self._last_run[check.name] = now
        return executed

    def xǁSchedulerLoopǁtick__mutmut_4(self, checks: list[CronCheck]) -> list[CheckResult]:
        """Execute the enabled checks whose interval has elapsed."""
        executed: list[CheckResult] = []
        now = self._now()
        for check in checks:
            if not check.enabled:
                break
            interval_minutes = cron_to_minutes(check.schedule)
            if interval_minutes <= 0:
                continue
            last = self._last_run.get(check.name)
            if last is not None and _elapsed_minutes(now, last) < interval_minutes:
                continue
            executed.append(self._runner.execute(check))
            self._last_run[check.name] = now
        return executed

    def xǁSchedulerLoopǁtick__mutmut_5(self, checks: list[CronCheck]) -> list[CheckResult]:
        """Execute the enabled checks whose interval has elapsed."""
        executed: list[CheckResult] = []
        now = self._now()
        for check in checks:
            if not check.enabled:
                continue
            interval_minutes = None
            if interval_minutes <= 0:
                continue
            last = self._last_run.get(check.name)
            if last is not None and _elapsed_minutes(now, last) < interval_minutes:
                continue
            executed.append(self._runner.execute(check))
            self._last_run[check.name] = now
        return executed

    def xǁSchedulerLoopǁtick__mutmut_6(self, checks: list[CronCheck]) -> list[CheckResult]:
        """Execute the enabled checks whose interval has elapsed."""
        executed: list[CheckResult] = []
        now = self._now()
        for check in checks:
            if not check.enabled:
                continue
            interval_minutes = cron_to_minutes(None)
            if interval_minutes <= 0:
                continue
            last = self._last_run.get(check.name)
            if last is not None and _elapsed_minutes(now, last) < interval_minutes:
                continue
            executed.append(self._runner.execute(check))
            self._last_run[check.name] = now
        return executed

    def xǁSchedulerLoopǁtick__mutmut_7(self, checks: list[CronCheck]) -> list[CheckResult]:
        """Execute the enabled checks whose interval has elapsed."""
        executed: list[CheckResult] = []
        now = self._now()
        for check in checks:
            if not check.enabled:
                continue
            interval_minutes = cron_to_minutes(check.schedule)
            if interval_minutes < 0:
                continue
            last = self._last_run.get(check.name)
            if last is not None and _elapsed_minutes(now, last) < interval_minutes:
                continue
            executed.append(self._runner.execute(check))
            self._last_run[check.name] = now
        return executed

    def xǁSchedulerLoopǁtick__mutmut_8(self, checks: list[CronCheck]) -> list[CheckResult]:
        """Execute the enabled checks whose interval has elapsed."""
        executed: list[CheckResult] = []
        now = self._now()
        for check in checks:
            if not check.enabled:
                continue
            interval_minutes = cron_to_minutes(check.schedule)
            if interval_minutes <= 1:
                continue
            last = self._last_run.get(check.name)
            if last is not None and _elapsed_minutes(now, last) < interval_minutes:
                continue
            executed.append(self._runner.execute(check))
            self._last_run[check.name] = now
        return executed

    def xǁSchedulerLoopǁtick__mutmut_9(self, checks: list[CronCheck]) -> list[CheckResult]:
        """Execute the enabled checks whose interval has elapsed."""
        executed: list[CheckResult] = []
        now = self._now()
        for check in checks:
            if not check.enabled:
                continue
            interval_minutes = cron_to_minutes(check.schedule)
            if interval_minutes <= 0:
                break
            last = self._last_run.get(check.name)
            if last is not None and _elapsed_minutes(now, last) < interval_minutes:
                continue
            executed.append(self._runner.execute(check))
            self._last_run[check.name] = now
        return executed

    def xǁSchedulerLoopǁtick__mutmut_10(self, checks: list[CronCheck]) -> list[CheckResult]:
        """Execute the enabled checks whose interval has elapsed."""
        executed: list[CheckResult] = []
        now = self._now()
        for check in checks:
            if not check.enabled:
                continue
            interval_minutes = cron_to_minutes(check.schedule)
            if interval_minutes <= 0:
                continue
            last = None
            if last is not None and _elapsed_minutes(now, last) < interval_minutes:
                continue
            executed.append(self._runner.execute(check))
            self._last_run[check.name] = now
        return executed

    def xǁSchedulerLoopǁtick__mutmut_11(self, checks: list[CronCheck]) -> list[CheckResult]:
        """Execute the enabled checks whose interval has elapsed."""
        executed: list[CheckResult] = []
        now = self._now()
        for check in checks:
            if not check.enabled:
                continue
            interval_minutes = cron_to_minutes(check.schedule)
            if interval_minutes <= 0:
                continue
            last = self._last_run.get(None)
            if last is not None and _elapsed_minutes(now, last) < interval_minutes:
                continue
            executed.append(self._runner.execute(check))
            self._last_run[check.name] = now
        return executed

    def xǁSchedulerLoopǁtick__mutmut_12(self, checks: list[CronCheck]) -> list[CheckResult]:
        """Execute the enabled checks whose interval has elapsed."""
        executed: list[CheckResult] = []
        now = self._now()
        for check in checks:
            if not check.enabled:
                continue
            interval_minutes = cron_to_minutes(check.schedule)
            if interval_minutes <= 0:
                continue
            last = self._last_run.get(check.name)
            if last is not None or _elapsed_minutes(now, last) < interval_minutes:
                continue
            executed.append(self._runner.execute(check))
            self._last_run[check.name] = now
        return executed

    def xǁSchedulerLoopǁtick__mutmut_13(self, checks: list[CronCheck]) -> list[CheckResult]:
        """Execute the enabled checks whose interval has elapsed."""
        executed: list[CheckResult] = []
        now = self._now()
        for check in checks:
            if not check.enabled:
                continue
            interval_minutes = cron_to_minutes(check.schedule)
            if interval_minutes <= 0:
                continue
            last = self._last_run.get(check.name)
            if last is None and _elapsed_minutes(now, last) < interval_minutes:
                continue
            executed.append(self._runner.execute(check))
            self._last_run[check.name] = now
        return executed

    def xǁSchedulerLoopǁtick__mutmut_14(self, checks: list[CronCheck]) -> list[CheckResult]:
        """Execute the enabled checks whose interval has elapsed."""
        executed: list[CheckResult] = []
        now = self._now()
        for check in checks:
            if not check.enabled:
                continue
            interval_minutes = cron_to_minutes(check.schedule)
            if interval_minutes <= 0:
                continue
            last = self._last_run.get(check.name)
            if last is not None and _elapsed_minutes(None, last) < interval_minutes:
                continue
            executed.append(self._runner.execute(check))
            self._last_run[check.name] = now
        return executed

    def xǁSchedulerLoopǁtick__mutmut_15(self, checks: list[CronCheck]) -> list[CheckResult]:
        """Execute the enabled checks whose interval has elapsed."""
        executed: list[CheckResult] = []
        now = self._now()
        for check in checks:
            if not check.enabled:
                continue
            interval_minutes = cron_to_minutes(check.schedule)
            if interval_minutes <= 0:
                continue
            last = self._last_run.get(check.name)
            if last is not None and _elapsed_minutes(now, None) < interval_minutes:
                continue
            executed.append(self._runner.execute(check))
            self._last_run[check.name] = now
        return executed

    def xǁSchedulerLoopǁtick__mutmut_16(self, checks: list[CronCheck]) -> list[CheckResult]:
        """Execute the enabled checks whose interval has elapsed."""
        executed: list[CheckResult] = []
        now = self._now()
        for check in checks:
            if not check.enabled:
                continue
            interval_minutes = cron_to_minutes(check.schedule)
            if interval_minutes <= 0:
                continue
            last = self._last_run.get(check.name)
            if last is not None and _elapsed_minutes(last) < interval_minutes:
                continue
            executed.append(self._runner.execute(check))
            self._last_run[check.name] = now
        return executed

    def xǁSchedulerLoopǁtick__mutmut_17(self, checks: list[CronCheck]) -> list[CheckResult]:
        """Execute the enabled checks whose interval has elapsed."""
        executed: list[CheckResult] = []
        now = self._now()
        for check in checks:
            if not check.enabled:
                continue
            interval_minutes = cron_to_minutes(check.schedule)
            if interval_minutes <= 0:
                continue
            last = self._last_run.get(check.name)
            if last is not None and _elapsed_minutes(now, ) < interval_minutes:
                continue
            executed.append(self._runner.execute(check))
            self._last_run[check.name] = now
        return executed

    def xǁSchedulerLoopǁtick__mutmut_18(self, checks: list[CronCheck]) -> list[CheckResult]:
        """Execute the enabled checks whose interval has elapsed."""
        executed: list[CheckResult] = []
        now = self._now()
        for check in checks:
            if not check.enabled:
                continue
            interval_minutes = cron_to_minutes(check.schedule)
            if interval_minutes <= 0:
                continue
            last = self._last_run.get(check.name)
            if last is not None and _elapsed_minutes(now, last) <= interval_minutes:
                continue
            executed.append(self._runner.execute(check))
            self._last_run[check.name] = now
        return executed

    def xǁSchedulerLoopǁtick__mutmut_19(self, checks: list[CronCheck]) -> list[CheckResult]:
        """Execute the enabled checks whose interval has elapsed."""
        executed: list[CheckResult] = []
        now = self._now()
        for check in checks:
            if not check.enabled:
                continue
            interval_minutes = cron_to_minutes(check.schedule)
            if interval_minutes <= 0:
                continue
            last = self._last_run.get(check.name)
            if last is not None and _elapsed_minutes(now, last) < interval_minutes:
                break
            executed.append(self._runner.execute(check))
            self._last_run[check.name] = now
        return executed

    def xǁSchedulerLoopǁtick__mutmut_20(self, checks: list[CronCheck]) -> list[CheckResult]:
        """Execute the enabled checks whose interval has elapsed."""
        executed: list[CheckResult] = []
        now = self._now()
        for check in checks:
            if not check.enabled:
                continue
            interval_minutes = cron_to_minutes(check.schedule)
            if interval_minutes <= 0:
                continue
            last = self._last_run.get(check.name)
            if last is not None and _elapsed_minutes(now, last) < interval_minutes:
                continue
            executed.append(None)
            self._last_run[check.name] = now
        return executed

    def xǁSchedulerLoopǁtick__mutmut_21(self, checks: list[CronCheck]) -> list[CheckResult]:
        """Execute the enabled checks whose interval has elapsed."""
        executed: list[CheckResult] = []
        now = self._now()
        for check in checks:
            if not check.enabled:
                continue
            interval_minutes = cron_to_minutes(check.schedule)
            if interval_minutes <= 0:
                continue
            last = self._last_run.get(check.name)
            if last is not None and _elapsed_minutes(now, last) < interval_minutes:
                continue
            executed.append(self._runner.execute(None))
            self._last_run[check.name] = now
        return executed

    def xǁSchedulerLoopǁtick__mutmut_22(self, checks: list[CronCheck]) -> list[CheckResult]:
        """Execute the enabled checks whose interval has elapsed."""
        executed: list[CheckResult] = []
        now = self._now()
        for check in checks:
            if not check.enabled:
                continue
            interval_minutes = cron_to_minutes(check.schedule)
            if interval_minutes <= 0:
                continue
            last = self._last_run.get(check.name)
            if last is not None and _elapsed_minutes(now, last) < interval_minutes:
                continue
            executed.append(self._runner.execute(check))
            self._last_run[check.name] = None
        return executed

mutants_xǁSchedulerLoopǁ__init____mutmut['_mutmut_orig'] = SchedulerLoop.xǁSchedulerLoopǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁSchedulerLoopǁ__init____mutmut['xǁSchedulerLoopǁ__init____mutmut_1'] = SchedulerLoop.xǁSchedulerLoopǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁSchedulerLoopǁ__init____mutmut['xǁSchedulerLoopǁ__init____mutmut_2'] = SchedulerLoop.xǁSchedulerLoopǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁSchedulerLoopǁ__init____mutmut['xǁSchedulerLoopǁ__init____mutmut_3'] = SchedulerLoop.xǁSchedulerLoopǁ__init____mutmut_3 # type: ignore # mutmut generated

mutants_xǁSchedulerLoopǁprime__mutmut['_mutmut_orig'] = SchedulerLoop.xǁSchedulerLoopǁprime__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSchedulerLoopǁprime__mutmut['xǁSchedulerLoopǁprime__mutmut_1'] = SchedulerLoop.xǁSchedulerLoopǁprime__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSchedulerLoopǁprime__mutmut['xǁSchedulerLoopǁprime__mutmut_2'] = SchedulerLoop.xǁSchedulerLoopǁprime__mutmut_2 # type: ignore # mutmut generated

mutants_xǁSchedulerLoopǁtick__mutmut['_mutmut_orig'] = SchedulerLoop.xǁSchedulerLoopǁtick__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSchedulerLoopǁtick__mutmut['xǁSchedulerLoopǁtick__mutmut_1'] = SchedulerLoop.xǁSchedulerLoopǁtick__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSchedulerLoopǁtick__mutmut['xǁSchedulerLoopǁtick__mutmut_2'] = SchedulerLoop.xǁSchedulerLoopǁtick__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSchedulerLoopǁtick__mutmut['xǁSchedulerLoopǁtick__mutmut_3'] = SchedulerLoop.xǁSchedulerLoopǁtick__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSchedulerLoopǁtick__mutmut['xǁSchedulerLoopǁtick__mutmut_4'] = SchedulerLoop.xǁSchedulerLoopǁtick__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSchedulerLoopǁtick__mutmut['xǁSchedulerLoopǁtick__mutmut_5'] = SchedulerLoop.xǁSchedulerLoopǁtick__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSchedulerLoopǁtick__mutmut['xǁSchedulerLoopǁtick__mutmut_6'] = SchedulerLoop.xǁSchedulerLoopǁtick__mutmut_6 # type: ignore # mutmut generated
mutants_xǁSchedulerLoopǁtick__mutmut['xǁSchedulerLoopǁtick__mutmut_7'] = SchedulerLoop.xǁSchedulerLoopǁtick__mutmut_7 # type: ignore # mutmut generated
mutants_xǁSchedulerLoopǁtick__mutmut['xǁSchedulerLoopǁtick__mutmut_8'] = SchedulerLoop.xǁSchedulerLoopǁtick__mutmut_8 # type: ignore # mutmut generated
mutants_xǁSchedulerLoopǁtick__mutmut['xǁSchedulerLoopǁtick__mutmut_9'] = SchedulerLoop.xǁSchedulerLoopǁtick__mutmut_9 # type: ignore # mutmut generated
mutants_xǁSchedulerLoopǁtick__mutmut['xǁSchedulerLoopǁtick__mutmut_10'] = SchedulerLoop.xǁSchedulerLoopǁtick__mutmut_10 # type: ignore # mutmut generated
mutants_xǁSchedulerLoopǁtick__mutmut['xǁSchedulerLoopǁtick__mutmut_11'] = SchedulerLoop.xǁSchedulerLoopǁtick__mutmut_11 # type: ignore # mutmut generated
mutants_xǁSchedulerLoopǁtick__mutmut['xǁSchedulerLoopǁtick__mutmut_12'] = SchedulerLoop.xǁSchedulerLoopǁtick__mutmut_12 # type: ignore # mutmut generated
mutants_xǁSchedulerLoopǁtick__mutmut['xǁSchedulerLoopǁtick__mutmut_13'] = SchedulerLoop.xǁSchedulerLoopǁtick__mutmut_13 # type: ignore # mutmut generated
mutants_xǁSchedulerLoopǁtick__mutmut['xǁSchedulerLoopǁtick__mutmut_14'] = SchedulerLoop.xǁSchedulerLoopǁtick__mutmut_14 # type: ignore # mutmut generated
mutants_xǁSchedulerLoopǁtick__mutmut['xǁSchedulerLoopǁtick__mutmut_15'] = SchedulerLoop.xǁSchedulerLoopǁtick__mutmut_15 # type: ignore # mutmut generated
mutants_xǁSchedulerLoopǁtick__mutmut['xǁSchedulerLoopǁtick__mutmut_16'] = SchedulerLoop.xǁSchedulerLoopǁtick__mutmut_16 # type: ignore # mutmut generated
mutants_xǁSchedulerLoopǁtick__mutmut['xǁSchedulerLoopǁtick__mutmut_17'] = SchedulerLoop.xǁSchedulerLoopǁtick__mutmut_17 # type: ignore # mutmut generated
mutants_xǁSchedulerLoopǁtick__mutmut['xǁSchedulerLoopǁtick__mutmut_18'] = SchedulerLoop.xǁSchedulerLoopǁtick__mutmut_18 # type: ignore # mutmut generated
mutants_xǁSchedulerLoopǁtick__mutmut['xǁSchedulerLoopǁtick__mutmut_19'] = SchedulerLoop.xǁSchedulerLoopǁtick__mutmut_19 # type: ignore # mutmut generated
mutants_xǁSchedulerLoopǁtick__mutmut['xǁSchedulerLoopǁtick__mutmut_20'] = SchedulerLoop.xǁSchedulerLoopǁtick__mutmut_20 # type: ignore # mutmut generated
mutants_xǁSchedulerLoopǁtick__mutmut['xǁSchedulerLoopǁtick__mutmut_21'] = SchedulerLoop.xǁSchedulerLoopǁtick__mutmut_21 # type: ignore # mutmut generated
mutants_xǁSchedulerLoopǁtick__mutmut['xǁSchedulerLoopǁtick__mutmut_22'] = SchedulerLoop.xǁSchedulerLoopǁtick__mutmut_22 # type: ignore # mutmut generated
mutants_x__elapsed_minutes__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__elapsed_minutes__mutmut)
def _elapsed_minutes(now: datetime, previous: datetime) -> float:
    return (now - previous).total_seconds() / 60


def x__elapsed_minutes__mutmut_orig(now: datetime, previous: datetime) -> float:
    return (now - previous).total_seconds() / 60


def x__elapsed_minutes__mutmut_1(now: datetime, previous: datetime) -> float:
    return (now - previous).total_seconds() * 60


def x__elapsed_minutes__mutmut_2(now: datetime, previous: datetime) -> float:
    return (now + previous).total_seconds() / 60


def x__elapsed_minutes__mutmut_3(now: datetime, previous: datetime) -> float:
    return (now - previous).total_seconds() / 61

mutants_x__elapsed_minutes__mutmut['_mutmut_orig'] = x__elapsed_minutes__mutmut_orig # type: ignore # mutmut generated
mutants_x__elapsed_minutes__mutmut['x__elapsed_minutes__mutmut_1'] = x__elapsed_minutes__mutmut_1 # type: ignore # mutmut generated
mutants_x__elapsed_minutes__mutmut['x__elapsed_minutes__mutmut_2'] = x__elapsed_minutes__mutmut_2 # type: ignore # mutmut generated
mutants_x__elapsed_minutes__mutmut['x__elapsed_minutes__mutmut_3'] = x__elapsed_minutes__mutmut_3 # type: ignore # mutmut generated
