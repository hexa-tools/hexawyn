from dataclasses import dataclass, field


@dataclass
class TraceLogCorrelationResponse:
    correlations: list[dict[str, object]] = field(default_factory=list)
    trace_id: str = ""
    summary: str = ""
    operation: str = ""
    error_spans: str = ""
    error_span_count: int = 0
    correlated_logs: str = ""
    correlated_log_count: int = 0
    error: str | None = None
