from dataclasses import dataclass


@dataclass(frozen=True)
class PrometheusQueryCommand:
    end: str = ""
    query_type: str = ""
    start: str = ""
    step: str = ""
    timeout_seconds: str = ""
    unit_hint: str = ""
