from dataclasses import dataclass


@dataclass(frozen=True)
class PrometheusQueryCommand:
    promql: str = ""
