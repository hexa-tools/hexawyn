from dataclasses import dataclass, field


@dataclass
class SpanBottleneckAnalysisResponse:
    bottlenecks: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
