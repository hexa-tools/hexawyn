from __future__ import annotations

from unittest.mock import patch


class TestOtelPodTraceAdapterUnit:
    def test_returns_list(self) -> None:
        from hexawyn.domain.models.slowest_traces import SlowestTracesRequest
        from hexawyn.infrastructure.adapters.secondary.gitops.otel_pod_trace_adapter import (
            OTelPodTraceAdapter,
        )

        adapter = OTelPodTraceAdapter()
        result = adapter.search_pod_traces(SlowestTracesRequest(pod_name="test-pod"))
        assert isinstance(result, list)

    def test_traces_populated_with_mocked_data(self) -> None:
        from hexawyn.domain.models.slowest_traces import SlowestTracesRequest
        from hexawyn.infrastructure.adapters.secondary.gitops.otel_pod_trace_adapter import (
            OTelPodTraceAdapter,
        )

        mock_traces = [
            {"traceID": "abc123def4567890", "duration": 500000, "hasErrors": False},
        ]
        with patch(
            "hexawyn.infrastructure.adapters.secondary.gitops.otel_pod_trace_adapter.search_jaeger_traces",
            return_value=mock_traces,
        ):
            adapter = OTelPodTraceAdapter()
            result = adapter.search_pod_traces(SlowestTracesRequest(pod_name="test-pod"))
            assert len(result) == 1
            assert result[0].trace_id == "abc123def4567890"
            assert result[0].span_count == 0
