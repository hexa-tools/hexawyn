from dataclasses import dataclass


@dataclass(frozen=True)
class MetricCorrelationCommand:
    service_name: str = ""
    primary_service: str = ""
    correlated_service: str = ""
    time_window_minutes: int = 60
