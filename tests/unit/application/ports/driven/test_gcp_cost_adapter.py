from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driven.cost_estimation_port import CostEstimationPort
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError

_GCP_DATA = {
    "rows": [
        {"labels": [{"key": "k8s-namespace", "value": "payments"}], "cost": 1800.0},
        {"labels": [{"key": "k8s-namespace", "value": "monitoring"}], "cost": 250.0},
    ]
}


class TestPortImplementation:
    def test_is_cost_estimation_port(self) -> None:
        from hexawyn.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        adapter = GCPCostAdapter(project_id="proj-1", billing_client=MagicMock())

        assert isinstance(adapter, CostEstimationPort)


class TestEstimateClusterCost:
    def test_aggregates_namespace_costs(self) -> None:
        from hexawyn.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        client = MagicMock()
        client.query_billing_data.return_value = _GCP_DATA
        adapter = GCPCostAdapter(project_id="proj-1", billing_client=client)

        report = adapter.estimate_cluster_cost("gke-prod")

        assert report["data_source"] == "gcp"
        assert report["total_monthly_cost_usd"] == 2050.0
        assert report["namespace_costs"][0]["namespace"] == "payments"

    def test_credentials_error_raises_insufficient_permissions(self) -> None:
        from google.auth.exceptions import DefaultCredentialsError
        from hexawyn.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        client = MagicMock()
        client.query_billing_data.side_effect = DefaultCredentialsError()
        adapter = GCPCostAdapter(project_id="proj-1", billing_client=client)

        with pytest.raises(InsufficientPermissionsError):
            adapter.estimate_cluster_cost("gke-prod")

    def test_api_error_raises_cluster_unreachable(self) -> None:
        from google.api_core.exceptions import PermissionDenied
        from hexawyn.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        client = MagicMock()
        client.query_billing_data.side_effect = PermissionDenied("denied")
        adapter = GCPCostAdapter(project_id="proj-1", billing_client=client)

        with pytest.raises(ClusterUnreachableError):
            adapter.estimate_cluster_cost("gke-prod")

    def test_empty_response_defaults(self) -> None:
        from hexawyn.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        client = MagicMock()
        client.query_billing_data.return_value = {"rows": []}
        adapter = GCPCostAdapter(project_id="proj-1", billing_client=client)

        report = adapter.estimate_cluster_cost("gke-prod")

        assert report["total_monthly_cost_usd"] == 0.0

    def test_rows_not_a_list(self) -> None:
        from hexawyn.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        client = MagicMock()
        client.query_billing_data.return_value = {}
        adapter = GCPCostAdapter(project_id="proj-1", billing_client=client)

        report = adapter.estimate_cluster_cost("gke-prod")
        assert report["total_monthly_cost_usd"] == 0.0

    def test_non_dict_row_skipped(self) -> None:
        from hexawyn.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        client = MagicMock()
        client.query_billing_data.return_value = {
            "rows": [None, {"labels": [{"key": "k8s-namespace", "value": "ns"}], "cost": 50.0}]
        }
        adapter = GCPCostAdapter(project_id="proj-1", billing_client=client)

        report = adapter.estimate_cluster_cost("gke-prod")
        assert report["total_monthly_cost_usd"] == 50.0

    def test_unexpected_error_translated(self) -> None:
        from hexawyn.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        client = MagicMock()
        client.query_billing_data.side_effect = RuntimeError("boom")
        adapter = GCPCostAdapter(project_id="proj-1", billing_client=client)

        with pytest.raises(ClusterUnreachableError):
            adapter.estimate_cluster_cost("gke-prod")
