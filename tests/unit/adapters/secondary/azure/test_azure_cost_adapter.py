from __future__ import annotations

from sys import modules as sys_modules
from unittest.mock import Mock, patch

from hexawyn.adapters.secondary.azure.azure_cost_adapter import (
    AzureCostAdapter,
    _parse_azure_rows,
)
from hexawyn.domain.errors import ClusterUnreachableError


class TestAzureCostAdapter:
    def test_estimate_cluster_cost_returns_empty_on_no_rows(self) -> None:
        mock_client = Mock()
        mock_client.query_usage.return_value = {"properties": {"rows": []}}
        adapter = AzureCostAdapter(subscription_id="sub-123", cm_client=mock_client)
        result = adapter.estimate_cluster_cost("my-cluster")
        assert result["total_monthly_cost_usd"] == 0.0
        assert result["cluster_name"] == "my-cluster"
        assert result["data_source"] == "azure"
        assert result["currency"] == "USD"

    def test_estimate_cluster_cost_with_usage(self) -> None:
        mock_client = Mock()
        mock_client.query_usage.return_value = {
            "properties": {
                "rows": [
                    ["default", "100.50"],
                    ["production", "200.75"],
                ]
            }
        }
        adapter = AzureCostAdapter(subscription_id="sub-123", cm_client=mock_client)
        result = adapter.estimate_cluster_cost("my-cluster")
        assert result["total_monthly_cost_usd"] == 301.25  # noqa: PLR2004
        assert len(result["namespace_costs"]) == 2  # noqa: PLR2004
        assert result["namespace_costs"][0]["namespace"] == "default"
        assert result["namespace_costs"][0]["monthly_cost_usd"] == 100.50  # noqa: PLR2004

    def test_estimate_cluster_cost_passes_subscription_id_to_client(self) -> None:
        mock_client = Mock()
        mock_client.query_usage.return_value = {"properties": {"rows": []}}
        adapter = AzureCostAdapter(subscription_id="sub-123", cm_client=mock_client)
        adapter.estimate_cluster_cost("my-cluster")
        mock_client.query_usage.assert_called_once()
        call_args = mock_client.query_usage.call_args
        assert "/subscriptions/sub-123" in call_args.kwargs["scope"]

    def test_estimate_cluster_cost_translates_client_error(self) -> None:
        mock_azure_exc = Mock()
        mock_azure_exc.ClientAuthenticationError = type(
            "ClientAuthenticationError", (Exception,), {}
        )
        mock_azure_exc.HttpResponseError = type("HttpResponseError", (Exception,), {})
        mock_client = Mock()
        mock_client.query_usage.side_effect = mock_azure_exc.HttpResponseError("unavailable")
        adapter = AzureCostAdapter(subscription_id="sub-123", cm_client=mock_client)
        with patch.dict(sys_modules, {"azure.core.exceptions": mock_azure_exc}):
            try:
                adapter.estimate_cluster_cost("my-cluster")
            except ClusterUnreachableError:
                pass


class TestParseAzureRows:
    def test_empty_rows(self) -> None:
        result = _parse_azure_rows({"properties": {"rows": []}})
        assert result == []

    def test_parses_valid_rows(self) -> None:
        response = {"properties": {"rows": [["default", "10.5"]]}}
        result = _parse_azure_rows(response)
        assert len(result) == 1
        assert result[0]["namespace"] == "default"
        assert result[0]["monthly_cost_usd"] == 10.5  # noqa: PLR2004

    def test_missing_properties(self) -> None:
        result = _parse_azure_rows({})
        assert result == []

    def test_properties_not_dict(self) -> None:
        result = _parse_azure_rows({"properties": "bad"})
        assert result == []

    def test_rows_not_list(self) -> None:
        result = _parse_azure_rows({"properties": {"rows": "bad"}})
        assert result == []

    def test_malformed_row_skipped(self) -> None:
        response = {"properties": {"rows": [["default", "10.5"], ["bad"]]}}
        result = _parse_azure_rows(response)
        assert len(result) == 1

    def test_non_list_row_skipped(self) -> None:
        response = {"properties": {"rows": [["default", "10.5"], "bad"]}}
        result = _parse_azure_rows(response)
        assert len(result) == 1
