from dataclasses import dataclass


@dataclass(frozen=True)
class MetricCorrelationCommand:
    service_name: str
    lookback_minutes: int = 60
