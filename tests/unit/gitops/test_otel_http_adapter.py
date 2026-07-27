from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestOtelHTTPAdapter:
    def test_fetch_slow_spans_returns_list(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter
        from hexawyn.domain.models.latency_diagnostic import LatencyDiagnosticRequest

        with patch.object(
            OTelHTTPAdapter,
            "fetch_slow_spans",
            return_value=[[MagicMock()]],
        ):
            adapter = OTelHTTPAdapter()
            result = adapter.fetch_slow_spans(LatencyDiagnosticRequest(service_name="test"))
            assert isinstance(result, list)
            assert len(result) >= 1

    def test_fetch_slow_spans_empty_on_no_service(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter
        from hexawyn.domain.models.latency_diagnostic import LatencyDiagnosticRequest

        adapter = OTelHTTPAdapter()
        result = adapter.fetch_slow_spans(LatencyDiagnosticRequest(service_name=""))

        assert result == []

    def test_fetch_total_traces_returns_int(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter
        from hexawyn.domain.models.latency_diagnostic import LatencyDiagnosticRequest

        with patch.object(
            OTelHTTPAdapter,
            "fetch_total_traces",
            return_value=2,
        ):
            adapter = OTelHTTPAdapter()
            result = adapter.fetch_total_traces(LatencyDiagnosticRequest(service_name="test"))
            assert result == 2  # noqa: PLR2004
