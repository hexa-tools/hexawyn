from dataclasses import dataclass, field


@dataclass
class PrometheusQueryResponse:
    query: str = ""
    query_type: str = "instant"
    results: list[dict[str, object]] = field(default_factory=list)
    result_count: int = 0
    truncated: bool = False
    no_data: bool = False
    summary: str = ""
    error: str | None = None
