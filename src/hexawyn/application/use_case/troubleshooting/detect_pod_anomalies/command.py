from dataclasses import dataclass


@dataclass(frozen=True)
class DetectPodAnomaliesCommand:
    namespace: str
    baseline_window_days: int = 7
