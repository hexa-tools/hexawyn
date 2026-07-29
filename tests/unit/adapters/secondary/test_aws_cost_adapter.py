from __future__ import annotations

from unittest.mock import Mock

from hexawyn.adapters.secondary.aws.aws_cost_adapter import (
    AWSCostAdapter,
    _parse_namespace_costs,
)


class TestParseNamespaceCosts:
    def test_empty(self) -> None:
        assert _parse_namespace_costs({}) == []

    def test_with_data(self) -> None:
        response = {
            "ResultsByTime": [
                {
                    "Groups": [
                        {
                            "Keys": ["default"],
                            "Metrics": {"UnblendedCost": {"Amount": "100.50"}},
                        }
                    ]
                }
            ]
        }
        result = _parse_namespace_costs(response)
        assert len(result) == 1
        assert result[0]["namespace"] == "default"
        assert result[0]["monthly_cost_usd"] == 100.50  # noqa: PLR2004

    def test_no_results(self) -> None:
        assert _parse_namespace_costs({"ResultsByTime": "bad"}) == []

    def test_no_groups(self) -> None:
        assert _parse_namespace_costs({"ResultsByTime": [{}]}) == []

    def test_no_keys(self) -> None:
        response = {"ResultsByTime": [{"Groups": [{"Keys": []}]}]}
        assert _parse_namespace_costs(response) == []

    def test_no_metrics(self) -> None:
        response = {"ResultsByTime": [{"Groups": [{"Keys": ["ns"]}]}]}
        assert _parse_namespace_costs(response) == []


class TestAWSCostAdapter:
    def test_estimate_with_mock(self) -> None:
        client = Mock()
        client.get_cost_and_usage.return_value = {
            "ResultsByTime": [
                {"Groups": [{"Keys": ["prod"], "Metrics": {"UnblendedCost": {"Amount": "500.0"}}}]}
            ]
        }
        adapter = AWSCostAdapter(region="us-east-1", ce_client=client)
        result = adapter.estimate_cluster_cost("prod-cluster")
        assert result["cluster_name"] == "prod-cluster"
        assert result["total_monthly_cost_usd"] == 500.0  # noqa: PLR2004
        assert result["data_source"] == "aws"

    def test_estimate_empty(self) -> None:
        client = Mock()
        client.get_cost_and_usage.return_value = {"ResultsByTime": []}
        adapter = AWSCostAdapter(region="us-east-1", ce_client=client)
        result = adapter.estimate_cluster_cost("empty")
        assert result["total_monthly_cost_usd"] == 0.0
