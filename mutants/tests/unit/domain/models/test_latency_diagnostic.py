from __future__ import annotations

from hexawyn.domain.models.latency_diagnostic import (
    LatencyDiagnosticRequest,
    LatencyDiagnosticResult,
    SpanBreakdown,
    TraceSpan,
)


class TestTraceSpan:
    def test_create(self) -> None:
        span = TraceSpan(
            trace_id="abc123",
            span_name="postgres.query",
            duration_ms=580.0,
        )
        assert span.span_name == "postgres.query"
        assert span.duration_ms == 580.0  # noqa: PLR2004


class TestSpanBreakdown:
    def test_create(self) -> None:
        sb = SpanBreakdown(
            span_name="postgres.query",
            occurrence_count=20,
            avg_duration_ms=580.0,
        )
        assert sb.span_name == "postgres.query"
        assert sb.avg_duration_ms == 580.0  # noqa: PLR2004


class TestLatencyDiagnosticResult:
    def test_db_bottleneck(self) -> None:
        traces = [
            [
                TraceSpan(trace_id="abc", span_name="postgres.query", duration_ms=580.0),
                TraceSpan(trace_id="abc", span_name="redis.get", duration_ms=12.0),
            ],
            [
                TraceSpan(trace_id="def", span_name="postgres.query", duration_ms=520.0),
            ],
        ]
        result = LatencyDiagnosticResult.compute(
            request=LatencyDiagnosticRequest(service_name="payment-api", threshold_ms=500.0),
            slow_spans=traces,
            total_traces=2,
        )
        assert result.slow_trace_count == 2  # noqa: PLR2004
        assert len(result.bottlenecks) >= 1
        assert result.bottlenecks[0].span_name == "postgres.query"

    def test_no_slow_traces(self) -> None:
        result = LatencyDiagnosticResult.compute(
            request=LatencyDiagnosticRequest(service_name="svc", threshold_ms=500.0),
            slow_spans=[],
            total_traces=0,
        )
        assert result.slow_trace_count == 0
        assert result.bottlenecks == []
