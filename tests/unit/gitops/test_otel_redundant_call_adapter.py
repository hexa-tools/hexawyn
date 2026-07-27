# Auto-generated test for otel_redundant_call_adapter

from __future__ import annotations


class TestOtelRedundantCallAdapterUnit:
    def test_returns_list(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_redundant_call_adapter import (
            OTelRedundantCallAdapter,
        )
        from hexawyn.domain.models.redundant_calls import RedundantCallRequest

        adapter = OTelRedundantCallAdapter()
        result = adapter.fetch_spans(RedundantCallRequest(flow="flow-a"))
        assert isinstance(result, list)
