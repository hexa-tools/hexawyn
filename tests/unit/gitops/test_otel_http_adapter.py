from __future__ import annotations

from unittest.mock import patch

from hexawyn.domain.models.latency_diagnostic import LatencyDiagnosticRequest


class TestOtelHTTPAdapter:
    def test_fetch_slow_spans_empty_on_no_service(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

        adapter = OTelHTTPAdapter()
        result = adapter.fetch_slow_spans(LatencyDiagnosticRequest(service_name=""))

        assert result == []

    def test_fetch_slow_spans_with_mocked_traces(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

        mock_traces = [
            {"traceID": "trace11122233344455", "duration": 150000, "hasErrors": False},
            {"traceID": "trace55566677788899", "duration": 250000, "hasErrors": True},
        ]
        with patch(
            "hexawyn.adapters.secondary.gitops.otel_http_adapter.search_jaeger_traces",
            return_value=mock_traces,
        ):
            adapter = OTelHTTPAdapter()
            result = adapter.fetch_slow_spans(LatencyDiagnosticRequest(service_name="test-svc"))
            assert len(result) == 2  # noqa: PLR2004
            assert len(result[0]) == 1  # noqa: PLR2004
            assert result[0][0].trace_id == "trace11122233344455"
            assert result[1][0].span_name == "trace:trace555"

    def test_fetch_total_traces_returns_zero_on_empty_service(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

        adapter = OTelHTTPAdapter()
        result = adapter.fetch_total_traces(LatencyDiagnosticRequest(service_name=""))
        assert result == 0

    def test_fetch_total_traces_with_mocked_traces(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

        mock_traces = [
            {"traceID": "trace-aaa", "duration": 100000, "hasErrors": False},
            {"traceID": "trace-bbb", "duration": 200000, "hasErrors": False},
        ]
        with patch(
            "hexawyn.adapters.secondary.gitops.otel_http_adapter.search_jaeger_traces",
            return_value=mock_traces,
        ):
            adapter = OTelHTTPAdapter()
            result = adapter.fetch_total_traces(LatencyDiagnosticRequest(service_name="test-svc"))
            assert result == 2  # noqa: PLR2004
