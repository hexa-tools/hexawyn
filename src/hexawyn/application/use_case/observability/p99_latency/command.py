from dataclasses import dataclass


@dataclass(frozen=True)
class P99LatencyCommand:
    endpoint: str = ""
    slo_threshold_ms: str = ""
    time_window_minutes: str = ""
