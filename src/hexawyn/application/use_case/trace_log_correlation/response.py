from dataclasses import dataclass, field


@dataclass
class TraceLogCorrelationResponse:
    correlations: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
