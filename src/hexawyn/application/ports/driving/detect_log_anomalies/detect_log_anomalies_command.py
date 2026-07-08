from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DetectLogAnomaliesCommand:
    pod_name: str
    namespace: str
    time_window_minutes: int = 240
    zscore_threshold: float = 3.0
