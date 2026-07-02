from __future__ import annotations

from collections import Counter
from dataclasses import dataclass


@dataclass(frozen=True)
class TraceSpan:
    trace_id: str
    span_name: str
    duration_ms: float


@dataclass(frozen=True)
class SpanBreakdown:
    span_name: str
    occurrence_count: int
    avg_duration_ms: float


@dataclass(frozen=True)
class LatencyDiagnosticRequest:
    service_name: str
    time_window_minutes: int = 15
    threshold_ms: float = 500.0


@dataclass(frozen=True)
class LatencyDiagnosticResult:
    service_name: str
    time_window_minutes: int
    threshold_ms: float
    slow_trace_count: int
    total_traces: int
    bottlenecks: list[SpanBreakdown]
    slowest_span: TraceSpan | None

    @staticmethod
    def compute(
        request: LatencyDiagnosticRequest,
        slow_spans: list[list[TraceSpan]],
        total_traces: int,
    ) -> LatencyDiagnosticResult:
        flat: list[TraceSpan] = []
        for trace_spans in slow_spans:
            flat.extend(trace_spans)

        if not flat:
            return LatencyDiagnosticResult(
                service_name=request.service_name,
                time_window_minutes=request.time_window_minutes,
                threshold_ms=request.threshold_ms,
                slow_trace_count=0,
                total_traces=total_traces,
                bottlenecks=[],
                slowest_span=None,
            )

        counter: Counter[str] = Counter()
        aggregator: dict[str, float] = {}
        for span in flat:
            counter[span.span_name] += 1
            if span.span_name not in aggregator:
                aggregator[span.span_name] = 0.0
            aggregator[span.span_name] += span.duration_ms

        breakdowns = sorted(
            [
                SpanBreakdown(
                    span_name=name,
                    occurrence_count=counter[name],
                    avg_duration_ms=round(aggregator[name] / counter[name], 2),
                )
                for name in counter
            ],
            key=lambda b: b.avg_duration_ms,
            reverse=True,
        )

        slowest = max(flat, key=lambda s: s.duration_ms)

        return LatencyDiagnosticResult(
            service_name=request.service_name,
            time_window_minutes=request.time_window_minutes,
            threshold_ms=request.threshold_ms,
            slow_trace_count=len(slow_spans),
            total_traces=total_traces,
            bottlenecks=breakdowns,
            slowest_span=slowest,
        )
