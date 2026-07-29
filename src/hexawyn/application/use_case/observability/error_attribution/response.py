from dataclasses import dataclass


@dataclass
class ErrorAttributionResponse:
    total_errors: int = 0
    pareto_culprit: str = ""
    gateway: str = ""
    attribution: str = ""
    error: str | None = None
