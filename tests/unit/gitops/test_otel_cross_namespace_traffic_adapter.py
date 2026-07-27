# Auto-generated test for otel_cross_namespace_traffic_adapter

from __future__ import annotations


class TestOtelCrossNamespaceTrafficAdapterUnit:
    def test_returns_list(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_cross_namespace_traffic_adapter import (
            OTelCrossNamespaceTrafficAdapter,
        )

        adapter = OTelCrossNamespaceTrafficAdapter()
        result = adapter.list_cross_namespace_flows()
        assert isinstance(result, list)
