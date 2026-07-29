from __future__ import annotations

from unittest.mock import patch


class TestOtelRedundantCallAdapterUnit:
    def test_returns_list(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_redundant_call_adapter import (
            OTelRedundantCallAdapter,
        )
        from hexawyn.domain.models.redundant_calls import RedundantCallRequest

        adapter = OTelRedundantCallAdapter()
        result = adapter.fetch_spans(RedundantCallRequest(flow="flow-a"))
        assert isinstance(result, list)

    def test_spans_populated_with_mocked_traces(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_redundant_call_adapter import (
            OTelRedundantCallAdapter,
        )
        from hexawyn.domain.models.redundant_calls import RedundantCallRequest

        mock_traces = [
            {"traceID": "deadbeef1234567890abcdef", "duration": 300000, "hasErrors": True},
        ]
        with patch(
            "hexawyn.adapters.secondary.gitops.otel_redundant_call_adapter.search_jaeger_traces",
            return_value=mock_traces,
        ):
            adapter = OTelRedundantCallAdapter()
            result = adapter.fetch_spans(RedundantCallRequest(flow="flow-a"))
            assert len(result) == 1
            assert result[0].span_name == "trace:deadbeef"
