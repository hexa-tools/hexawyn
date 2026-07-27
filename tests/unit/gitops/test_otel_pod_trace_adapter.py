# Auto-generated test for otel_pod_trace_adapter

from __future__ import annotations


class TestOtelPodTraceAdapterUnit:
    def test_returns_list(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_pod_trace_adapter import OTelPodTraceAdapter
        from hexawyn.domain.models.slowest_traces import SlowestTracesRequest

        adapter = OTelPodTraceAdapter()
        result = adapter.search_pod_traces(SlowestTracesRequest(pod_name="test-pod"))
        assert isinstance(result, list)
