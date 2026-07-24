from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class DetectLogAnomaliesResponse:
    pod_name: str = ""
    namespace: str = ""
    time_window_minutes: int = 0
    total_lines: int = 0
    baseline_mean_lines_per_minute: float = 0.0
    baseline_std_dev: float = 0.0
    summary: str = ""
    insufficient_data: bool = False
    formats_analyzed_separately: int = 1
    anomalies: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
