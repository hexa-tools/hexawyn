from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TraceLogCorrelationResponse:
    trace_id: str | None = None
    operation: str = ""
    error_span_count: int = 0
    correlated_log_count: int = 0
    summary: str = ""
    error_spans: list[dict[str, object]] = field(default_factory=list)
    correlated_logs: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
