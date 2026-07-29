from dataclasses import dataclass, field


@dataclass
class SLOBreachPredictionResponse:
    at_risk: list[dict[str, object]] = field(default_factory=list)
    safe_count: int = 0
    error: str | None = None
