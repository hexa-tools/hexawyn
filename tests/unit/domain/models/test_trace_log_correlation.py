from __future__ import annotations

from hexawyn.domain.models.trace_log_correlation import (
    CorrelatedLog,
    TraceLogCorrelationRequest,
    TraceLogResult,
    TraceLogSpan,
)


class TestTraceLogSpan:
    def test_create(self) -> None:
        span = TraceLogSpan(
            span_name="order-service.createOrder",
            error_message="ValidationException: invalid SKU",
            timestamp="10:32:15.421",
            trace_id="abc-def-123",
        )
        assert span.span_name == "order-service.createOrder"
        assert span.error_message == "ValidationException: invalid SKU"


class TestCorrelatedLog:
    def test_create(self) -> None:
        log = CorrelatedLog(
            timestamp="10:32:14.100",
            level="ERROR",
            message="inventory-service: timeout connecting to postgres",
        )
        assert log.level == "ERROR"
        assert "postgres" in log.message


class TestTraceLogResult:
    def test_correlation_found(self) -> None:
        spans = [
            TraceLogSpan(
                span_name="inventory-service.checkStock",
                error_message="timeout after 1500ms",
                timestamp="10:32:14.100",
                trace_id="abc-def-123",
            ),
            TraceLogSpan(
                span_name="order-service.createOrder",
                error_message="ValidationException: invalid SKU",
                timestamp="10:32:15.421",
                trace_id="abc-def-123",
            ),
        ]
        logs = [
            CorrelatedLog(
                timestamp="10:32:14.100", level="ERROR", message="timeout connecting to postgres"
            ),
            CorrelatedLog(
                timestamp="10:32:15.421",
                level="ERROR",
                message="ValidationException: invalid SKU abc-123",
            ),
        ]
        result = TraceLogResult.compute(
            request=TraceLogCorrelationRequest(operation="POST /order"),
            error_spans=spans,
            logs=logs,
        )
        assert result.trace_id == "abc-def-123"
        assert result.error_span_count == 2
        assert result.correlated_log_count == 2

    def test_spans_but_no_logs(self) -> None:
        spans = [
            TraceLogSpan(
                span_name="svc.create",
                error_message="timeout",
                timestamp="10:32:14.100",
                trace_id="abc",
            ),
        ]
        result = TraceLogResult.compute(
            request=TraceLogCorrelationRequest(operation="POST /x"),
            error_spans=spans,
            logs=[],
        )
        assert result.trace_id == "abc"
        assert result.correlated_log_count == 0

    def test_no_error_spans_found(self) -> None:
        result = TraceLogResult.compute(
            request=TraceLogCorrelationRequest(operation="POST /ghost"),
            error_spans=[],
            logs=[],
        )
        assert result.trace_id is None
        assert result.error_span_count == 0
