from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

AnomalyType = Literal["volume", "semantic"]


@dataclass(frozen=True)
class LogAnomaly:
    timestamp: str
    log_line: str
    anomaly_score: float
    type: AnomalyType
    low_confidence: bool = False


@dataclass(frozen=True)
class DetectLogAnomaliesRequest:
    pod_name: str
    namespace: str
    time_window_minutes: int = 240
    zscore_threshold: float = 3.0


@dataclass(frozen=True)
class DetectLogAnomaliesResult:
    pod_name: str
    namespace: str
    time_window_minutes: int
    total_lines: int
    anomalies: list[LogAnomaly] = field(default_factory=list)
    baseline_mean_lines_per_minute: float = 0.0
    baseline_std_dev: float = 0.0
    summary: str = ""
    insufficient_data: bool = False
    formats_analyzed_separately: int = 1
