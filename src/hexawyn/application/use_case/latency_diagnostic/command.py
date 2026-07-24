from dataclasses import dataclass


@dataclass(frozen=True)
class LatencyDiagnosticCommand:
    service_name: str
    time_window_minutes: int = 15
    threshold_ms: float = 500.0
