from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime


@dataclass
class PipelineRunSummary:
    name: str
    status: str
    start_time: str | None
    duration_seconds: int | None
    failure_reason: str | None
    pipeline_ref: str


@dataclass
class PipelineRunStatusReport:
    namespace: str
    window_hours: int
    total: int
    running: int = 0
    succeeded: int = 0
    failed: int = 0
    cancelled: int = 0
    not_started: int = 0
    most_recent_failed: PipelineRunSummary | None = None
    slowest_run: PipelineRunSummary | None = None
    generated_at: datetime = field(default_factory=lambda: datetime.now(UTC))
