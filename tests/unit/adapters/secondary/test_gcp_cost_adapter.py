from __future__ import annotations

from unittest.mock import Mock

from hexawyn.adapters.secondary.gcp.gcp_cost_adapter import (
    GCPCostAdapter,
    _parse_gcp_rows,
)


class TestParseGcpRows:
    def test_empty(self) -> None:
        assert _parse_gcp_rows({}) == []

    def test_no_rows(self) -> None:
        assert _parse_gcp_rows({"rows": "bad"}) == []

    def test_with_data(self) -> None:
        response = {
            "rows": [
                {
                    "labels": [{"key": "k8s-namespace", "value": "default"}],
                    "cost": "100.50",
                }
            ]
        }
        result = _parse_gcp_rows(response)
        assert len(result) == 1
        assert result[0]["namespace"] == "default"
        assert result[0]["monthly_cost_usd"] == 100.50  # noqa: PLR2004

    def test_no_namespace_skipped(self) -> None:
        response = {
            "rows": [
                {"labels": [], "cost": "50.0"},
            ]
        }
        assert _parse_gcp_rows(response) == []

    def test_multiple_namespaces(self) -> None:
        response = {
            "rows": [
                {"labels": [{"key": "k8s-namespace", "value": "ns1"}], "cost": "10.0"},
                {"labels": [{"key": "k8s-namespace", "value": "ns2"}], "cost": "20.0"},
            ]
        }
        result = _parse_gcp_rows(response)
        assert len(result) == 2  # noqa: PLR2004


class TestGCPCostAdapter:
    def test_estimate_with_mock_client(self) -> None:
        client = Mock()
        client.query_billing_data.return_value = {
            "rows": [
                {"labels": [{"key": "k8s-namespace", "value": "prod"}], "cost": "500.0"},
            ]
        }
        adapter = GCPCostAdapter(project_id="my-project", billing_client=client)
        result = adapter.estimate_cluster_cost("prod-cluster")
        assert result["cluster_name"] == "prod-cluster"
        assert result["total_monthly_cost_usd"] == 500.0  # noqa: PLR2004
        assert result["data_source"] == "gcp"

    def test_estimate_empty(self) -> None:
        client = Mock()
        client.query_billing_data.return_value = {"rows": []}
        adapter = GCPCostAdapter(project_id="p", billing_client=client)
        result = adapter.estimate_cluster_cost("empty")
        assert result["total_monthly_cost_usd"] == 0.0
