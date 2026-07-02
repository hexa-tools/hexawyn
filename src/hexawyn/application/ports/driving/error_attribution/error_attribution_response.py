from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ErrorAttributionResponse:
    gateway: str = ""
    total_errors: int = 0
    attribution: list[dict[str, object]] = field(default_factory=list)
    pareto_culprit: str | None = None
    error: str | None = None
