from __future__ import annotations

from hexawyn.adapters.secondary.gitops.otel_trace_log_adapter import (
    OTelTraceLogAdapter,
)
from hexawyn.application.ports.driven.trace_log_correlation_port import (
    TraceLogCorrelationPort,
)
from hexawyn.domain.models.trace_log_correlation import TraceLogCorrelationRequest


class TestOTelTraceLogAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(OTelTraceLogAdapter(), TraceLogCorrelationPort)

    def test_fetch_error_spans_returns_empty(self) -> None:
        r = OTelTraceLogAdapter().fetch_error_spans(
            TraceLogCorrelationRequest(operation="POST /test")
        )
        assert r == []

    def test_fetch_correlated_logs_returns_empty(self) -> None:
        r = OTelTraceLogAdapter().fetch_correlated_logs(trace_id="abc")
        assert r == []
