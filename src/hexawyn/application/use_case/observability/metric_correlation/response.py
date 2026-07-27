from dataclasses import dataclass, field


@dataclass
class MetricCorrelationResponse:
    correlations: list[dict[str, object]] = field(default_factory=list)
    status: str = ""
    primary_service: str = ""
    lag_index: str = ""
    hypothesis: str = ""
    data_point_count: int = 0
    correlated_service: str = ""
    coefficient: str = ""
    error: str | None = None
