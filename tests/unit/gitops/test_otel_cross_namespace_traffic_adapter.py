from __future__ import annotations

from unittest.mock import patch


class TestOtelCrossNamespaceTrafficAdapterUnit:
    def test_returns_list(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_cross_namespace_traffic_adapter import (
            OTelCrossNamespaceTrafficAdapter,
        )

        adapter = OTelCrossNamespaceTrafficAdapter()
        result = adapter.list_cross_namespace_flows()
        assert isinstance(result, list)

    def test_flows_populated_with_mocked_services(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_cross_namespace_traffic_adapter import (
            OTelCrossNamespaceTrafficAdapter,
        )

        with patch(
            "hexawyn.adapters.secondary.gitops.otel_cross_namespace_traffic_adapter.list_jaeger_services",
            return_value=["hotrod", "jaeger"],
        ):
            adapter = OTelCrossNamespaceTrafficAdapter()
            result = adapter.list_cross_namespace_flows()
            assert len(result) == 2  # noqa: PLR2004
            assert result[0]["source_service"] == "hotrod"
            assert result[1]["source_service"] == "jaeger"
