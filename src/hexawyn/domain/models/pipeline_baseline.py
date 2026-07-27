from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class StageStats:
    avg: float = 0.0
    p50: float = 0.0
    p95: float = 0.0
    max: float = 0.0
    unit: str = "seconds"


@dataclass
class PipelineBaselineResult:
    pipeline: str = ""
    runs_analyzed: int = 0
    requested_limit: int = 30
    stages: dict[str, StageStats] = field(default_factory=dict)
    total_duration: StageStats | None = None
    outliers: list[str] = field(default_factory=list)
    excluded_running: int = 0
    excluded_failed: int = 0
    trend: str = "insufficient_data"
    note: str = ""
