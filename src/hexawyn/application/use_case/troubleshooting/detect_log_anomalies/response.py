from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypedDict


class LogAnomalyDict(TypedDict):
    log_line: str
    zscore: float
    log_level: str
    timestamp: str


@dataclass
class DetectLogAnomaliesResponse:
    pod_name: str = ""
    namespace: str = ""
    time_window_minutes: int = 0
    total_lines: int = 0
    anomaly_count: int = 0
    anomalies: list[LogAnomalyDict] = field(default_factory=list)
    formats_analyzed_separately: bool = False
    baseline_mean_lines_per_minute: float = 0.0
    baseline_std_dev: float = 0.0
    summary: str = ""
    insufficient_data: bool = False
