from __future__ import annotations


class TestOTelCrossNamespaceTrafficAdapter:
    def test_implements_cross_namespace_traffic_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_cross_namespace_traffic_adapter import (
            OTelCrossNamespaceTrafficAdapter,
        )
        from hexawyn.application.ports.driven.cross_namespace_traffic_port import (
            CrossNamespaceTrafficPort,
        )

        adapter = OTelCrossNamespaceTrafficAdapter()

        assert isinstance(adapter, CrossNamespaceTrafficPort)

    def test_list_cross_namespace_flows_returns_empty_list(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_cross_namespace_traffic_adapter import (
            OTelCrossNamespaceTrafficAdapter,
        )

        adapter = OTelCrossNamespaceTrafficAdapter()
        result = adapter.list_cross_namespace_flows()

        assert result == []
