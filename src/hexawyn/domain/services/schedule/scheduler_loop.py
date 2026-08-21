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


class SchedulerLoop:
    """Runs due checks on each tick using an injectable clock."""

    def __init__(
        self,
        runner: CheckRunnerUseCase,
        now: Now = lambda: datetime.now(UTC),
    ) -> None:
        self._runner = runner
        self._now = now
        self._last_run: dict[str, datetime] = {}

    def prime(self, checks: list[CronCheck]) -> None:
        """Mark every check as just started so nothing runs on the first tick."""
        now = self._now()
        self._last_run = {check.name: now for check in checks}

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


def _elapsed_minutes(now: datetime, previous: datetime) -> float:
    return (now - previous).total_seconds() / 60
