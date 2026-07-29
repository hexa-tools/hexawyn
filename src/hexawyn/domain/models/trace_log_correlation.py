from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TraceLogSpan:
    span_name: str
    error_message: str
    timestamp: str
    trace_id: str


@dataclass(frozen=True)
class CorrelatedLog:
    timestamp: str
    level: str
    message: str


@dataclass(frozen=True)
class TraceLogCorrelationRequest:
    operation: str
    trace_id: str | None = None


@dataclass(frozen=True)
class TraceLogResult:
    trace_id: str | None
    operation: str
    error_span_count: int
    correlated_log_count: int
    error_spans: list[TraceLogSpan]
    correlated_logs: list[CorrelatedLog]
    summary: str

    @staticmethod
    def compute(
        request: TraceLogCorrelationRequest,
        error_spans: list[TraceLogSpan],
        logs: list[CorrelatedLog],
    ) -> TraceLogResult:
        trace_id = error_spans[0].trace_id if error_spans else None
        if not error_spans:
            return TraceLogResult(
                trace_id=None,
                operation=request.operation,
                error_span_count=0,
                correlated_log_count=0,
                error_spans=[],
                correlated_logs=[],
                summary=f"No error spans found for {request.operation}",
            )
        if not logs:
            return TraceLogResult(
                trace_id=trace_id,
                operation=request.operation,
                error_span_count=len(error_spans),
                correlated_log_count=0,
                error_spans=error_spans,
                correlated_logs=[],
                summary=f"Found {len(error_spans)} error span(s) but no correlated logs",
            )
        return TraceLogResult(
            trace_id=trace_id,
            operation=request.operation,
            error_span_count=len(error_spans),
            correlated_log_count=len(logs),
            error_spans=error_spans,
            correlated_logs=logs,
            summary=f"Found {len(error_spans)} error span(s) with {len(logs)} correlated log(s) for trace {trace_id}",  # noqa: E501
        )
