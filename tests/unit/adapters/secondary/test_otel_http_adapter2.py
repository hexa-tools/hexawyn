from __future__ import annotations

from hexawyn.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter
from hexawyn.application.ports.driven.trace_query_port import TraceQueryPort
from hexawyn.domain.models.latency_diagnostic import LatencyDiagnosticRequest


class TestOTelHTTPAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(OTelHTTPAdapter(), TraceQueryPort)

    def test_fetch_slow_returns_empty(self) -> None:
        r = OTelHTTPAdapter().fetch_slow_spans(LatencyDiagnosticRequest(service_name="x"))
        assert r == []

    def test_fetch_total_returns_zero(self) -> None:
        r = OTelHTTPAdapter().fetch_total_traces(LatencyDiagnosticRequest(service_name="x"))
        assert r == 0
