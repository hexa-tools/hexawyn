from dataclasses import dataclass


@dataclass
class P99LatencyResponse:
    time_window_minutes: str = ""
    slo_threshold_ms: str = ""
    slo_status: str = ""
    slo_delta_ms: str = ""
    sample_count: int = 0
    p99_ms: str = ""
    p95_ms: str = ""
    p50_ms: str = ""
    endpoint: str = ""
    error: str | None = None
