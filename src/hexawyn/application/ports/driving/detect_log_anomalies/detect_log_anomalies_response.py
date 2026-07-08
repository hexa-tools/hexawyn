from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypedDict


class LogAnomalyDict(TypedDict):
    timestamp: str
    log_line: str
    anomaly_score: float
    type: str
    low_confidence: bool


@dataclass
class DetectLogAnomaliesResponse:
    pod_name: str = ""
    namespace: str = ""
    time_window_minutes: int = 240
    total_lines: int = 0
    baseline_mean_lines_per_minute: float = 0.0
    baseline_std_dev: float = 0.0
    summary: str = ""
    insufficient_data: bool = False
    formats_analyzed_separately: int = 1
    anomalies: list[LogAnomalyDict] = field(default_factory=list)
    error: str | None = None
