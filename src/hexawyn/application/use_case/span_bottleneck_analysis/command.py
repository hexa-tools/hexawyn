from dataclasses import dataclass


@dataclass(frozen=True)
class SpanBottleneckAnalysisCommand:
    service_name: str
    lookback_minutes: int = 60
