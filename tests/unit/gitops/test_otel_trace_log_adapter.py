# Auto-generated test for otel_trace_log_adapter

from __future__ import annotations


class TestOtelTraceLogAdapterUnit:
    def test_returns_list(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_trace_log_adapter import OTelTraceLogAdapter
        from hexawyn.domain.models.trace_log_correlation import TraceLogCorrelationRequest

        adapter = OTelTraceLogAdapter()
        result = adapter.fetch_error_spans(TraceLogCorrelationRequest(operation="/api/op"))
        assert isinstance(result, list)
