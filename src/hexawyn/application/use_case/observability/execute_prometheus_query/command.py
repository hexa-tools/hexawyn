from dataclasses import dataclass


@dataclass(frozen=True)
class ExecutePrometheusQueryCommand:
    promql: str = ""
    query_type: str = "instant"
    start: str | None = None
    end: str | None = None
    step: str = "15s"
    timeout_seconds: int = 30
    unit_hint: str | None = None
