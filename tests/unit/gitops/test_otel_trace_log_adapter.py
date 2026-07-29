from __future__ import annotations

from unittest.mock import patch


class TestOtelTraceLogAdapterUnit:
    def test_returns_list(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_trace_log_adapter import OTelTraceLogAdapter
        from hexawyn.domain.models.trace_log_correlation import TraceLogCorrelationRequest

        adapter = OTelTraceLogAdapter()
        result = adapter.fetch_error_spans(TraceLogCorrelationRequest(operation="/api/op"))
        assert isinstance(result, list)

    def test_empty_operation_returns_empty_list(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_trace_log_adapter import OTelTraceLogAdapter
        from hexawyn.domain.models.trace_log_correlation import TraceLogCorrelationRequest

        adapter = OTelTraceLogAdapter()
        result = adapter.fetch_error_spans(TraceLogCorrelationRequest(operation=""))
        assert result == []

    def test_mocked_traces_populate_error_spans(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_trace_log_adapter import OTelTraceLogAdapter
        from hexawyn.domain.models.trace_log_correlation import TraceLogCorrelationRequest

        mock_traces = [
            {"traceID": "trace-log-001", "hasErrors": True},
            {"traceID": "trace-log-002", "hasErrors": False},
        ]
        with patch(
            "hexawyn.adapters.secondary.gitops.otel_trace_log_adapter.search_jaeger_traces",
            return_value=mock_traces,
        ):
            adapter = OTelTraceLogAdapter()
            result = adapter.fetch_error_spans(TraceLogCorrelationRequest(operation="/api/op"))
            assert len(result) == 2  # noqa: PLR2004
            assert result[0].trace_id == "trace-log-001"
            assert result[0].span_name == "trace-log-001"
            assert result[0].error_message == "error detected"
            assert result[1].error_message == ""

    def test_fetch_correlated_logs_empty_trace_id(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_trace_log_adapter import OTelTraceLogAdapter

        adapter = OTelTraceLogAdapter()
        result = adapter.fetch_correlated_logs("")
        assert result == []

    def test_fetch_correlated_logs_with_trace_id(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_trace_log_adapter import OTelTraceLogAdapter

        adapter = OTelTraceLogAdapter()
        result = adapter.fetch_correlated_logs("trace-abc")
        assert len(result) == 1
        assert result[0].level == "info"
        assert result[0].message == "log data not available without log backend"
