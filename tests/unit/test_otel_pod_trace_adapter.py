from __future__ import annotations

from hexawyn.adapters.secondary.gitops.otel_pod_trace_adapter import (
    OTelPodTraceAdapter,
)
from hexawyn.application.ports.driven.slow_trace_search_port import SlowTraceSearchPort
from hexawyn.domain.models.slowest_traces import SlowestTracesRequest


class TestOTelPodTraceAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(OTelPodTraceAdapter(), SlowTraceSearchPort)

    def test_search_returns_empty(self) -> None:
        r = OTelPodTraceAdapter().search_pod_traces(SlowestTracesRequest(pod_name="x"))
        assert r == []
