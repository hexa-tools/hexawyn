from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class CheckPhase(str, Enum):
    SCHEDULED = "scheduled"
    RUNNING = "running"
    SUCCESS = "success"
    ALERTING = "alerting"
    FAILED = "failed"
    DISABLED = "disabled"
    UNKNOWN = "unknown"


class NotifyPolicy(str, Enum):
    ALWAYS = "always"
    ON_CHANGE = "on_change"
    ON_FAILURE = "on_failure"


@dataclass
class CronCheck:
    name: str
    schedule: str
    use_case: str
    params: dict[str, str] = field(default_factory=dict)
    enabled: bool = True
    notify_policy: str = "on_change"
    destinations: list[str] = field(default_factory=lambda: ["slack"])
    timeout_seconds: int = 300


@dataclass
class CheckResult:
    check_name: str
    phase: str
    started_at: datetime
    payload_digest: str
    finished_at: datetime | None = None
    duration_ms: int | None = None
    summary: str = ""
    changed: bool = False
    error_message: str | None = None
    notified: bool = False


@dataclass
class ScheduleStatus:
    total_checks: int = 0
    enabled_checks: int = 0
    failed_checks: int = 0
    next_run_at: datetime | None = None
    last_run_at: datetime | None = None
    checks: list[CronCheck] = field(default_factory=list)
