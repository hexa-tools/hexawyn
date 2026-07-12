from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driven.cost_estimation_port import CostEstimationPort
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError


def _azure_response() -> dict[str, object]:
    return {
        "properties": {
            "rows": [
                ["payments", "1600.00"],
                ["monitoring", "200.00"],
            ]
        }
    }


class TestPortImplementation:
    def test_is_cost_estimation_port(self) -> None:
        from hexawyn.adapters.secondary.azure.azure_cost_adapter import AzureCostAdapter

        adapter = AzureCostAdapter(subscription_id="sub-1", cm_client=MagicMock())

        assert isinstance(adapter, CostEstimationPort)


class TestEstimateClusterCost:
    def test_aggregates_namespace_costs(self) -> None:
        from hexawyn.adapters.secondary.azure.azure_cost_adapter import AzureCostAdapter

        client = MagicMock()
        client.query_usage.return_value = _azure_response()
        adapter = AzureCostAdapter(subscription_id="sub-1", cm_client=client)

        report = adapter.estimate_cluster_cost("aks-prod")

        assert report["data_source"] == "azure"
        assert report["total_monthly_cost_usd"] == 1800.00
        assert report["namespace_costs"][0]["namespace"] == "payments"

    def test_auth_error_raises_insufficient_permissions(self) -> None:
        from azure.core.exceptions import ClientAuthenticationError
        from hexawyn.adapters.secondary.azure.azure_cost_adapter import AzureCostAdapter

        client = MagicMock()
        client.query_usage.side_effect = ClientAuthenticationError("auth failed")
        adapter = AzureCostAdapter(subscription_id="sub-1", cm_client=client)

        with pytest.raises(InsufficientPermissionsError):
            adapter.estimate_cluster_cost("aks-prod")

    def test_api_error_raises_cluster_unreachable(self) -> None:
        from azure.core.exceptions import HttpResponseError
        from hexawyn.adapters.secondary.azure.azure_cost_adapter import AzureCostAdapter

        client = MagicMock()
        client.query_usage.side_effect = HttpResponseError(message="denied", response=MagicMock())
        adapter = AzureCostAdapter(subscription_id="sub-1", cm_client=client)

        with pytest.raises(ClusterUnreachableError):
            adapter.estimate_cluster_cost("aks-prod")

    def test_empty_response_defaults(self) -> None:
        from hexawyn.adapters.secondary.azure.azure_cost_adapter import AzureCostAdapter

        client = MagicMock()
        client.query_usage.return_value = {"properties": {"rows": []}}
        adapter = AzureCostAdapter(subscription_id="sub-1", cm_client=client)

        report = adapter.estimate_cluster_cost("aks-prod")

        assert report["total_monthly_cost_usd"] == 0.0

    def test_properties_missing_returns_empty(self) -> None:
        from hexawyn.adapters.secondary.azure.azure_cost_adapter import AzureCostAdapter

        client = MagicMock()
        client.query_usage.return_value = {}
        adapter = AzureCostAdapter(subscription_id="sub-1", cm_client=client)

        report = adapter.estimate_cluster_cost("aks-prod")
        assert report["total_monthly_cost_usd"] == 0.0

    def test_rows_not_a_list(self) -> None:
        from hexawyn.adapters.secondary.azure.azure_cost_adapter import AzureCostAdapter

        client = MagicMock()
        client.query_usage.return_value = {"properties": {"rows": "oops"}}
        adapter = AzureCostAdapter(subscription_id="sub-1", cm_client=client)

        report = adapter.estimate_cluster_cost("aks-prod")
        assert report["total_monthly_cost_usd"] == 0.0

    def test_unexpected_error_translated(self) -> None:
        import pytest
        from hexawyn.adapters.secondary.azure.azure_cost_adapter import AzureCostAdapter
        from hexawyn.domain.errors import ClusterUnreachableError

        client = MagicMock()
        client.query_usage.side_effect = RuntimeError("boom")
        adapter = AzureCostAdapter(subscription_id="sub-1", cm_client=client)

        with pytest.raises(ClusterUnreachableError):
            adapter.estimate_cluster_cost("aks-prod")
