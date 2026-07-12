from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driven.cost_estimation_port import CostEstimationPort
from hexawyn.domain.errors import ClusterUnreachableError, InsufficientPermissionsError


def _cost_explorer_response() -> dict[str, object]:
    return {
        "ResultsByTime": [
            {
                "Groups": [
                    {
                        "Keys": ["payments"],
                        "Metrics": {"UnblendedCost": {"Amount": "1450.00"}},
                    },
                    {
                        "Keys": ["monitoring"],
                        "Metrics": {"UnblendedCost": {"Amount": "300.50"}},
                    },
                ]
            }
        ]
    }


class TestPortImplementation:
    def test_is_cost_estimation_port(self) -> None:
        from hexawyn.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        adapter = AWSCostAdapter(region="eu-west-1", ce_client=MagicMock())

        assert isinstance(adapter, CostEstimationPort)


class TestEstimateClusterCost:
    def test_aggregates_namespace_costs(self) -> None:
        from hexawyn.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        client = MagicMock()
        client.get_cost_and_usage.return_value = _cost_explorer_response()
        adapter = AWSCostAdapter(region="eu-west-1", ce_client=client)

        report = adapter.estimate_cluster_cost("eks-prod")

        assert report["cluster_name"] == "eks-prod"
        assert report["data_source"] == "aws"
        assert report["total_monthly_cost_usd"] == 1750.50
        assert report["namespace_costs"][0]["namespace"] == "payments"

    def test_missing_credentials_raises_insufficient_permissions(self) -> None:
        from botocore.exceptions import NoCredentialsError
        from hexawyn.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        client = MagicMock()
        client.get_cost_and_usage.side_effect = NoCredentialsError()
        adapter = AWSCostAdapter(region="eu-west-1", ce_client=client)

        with pytest.raises(InsufficientPermissionsError):
            adapter.estimate_cluster_cost("eks-prod")

    def test_api_error_raises_cluster_unreachable(self) -> None:
        from botocore.exceptions import ClientError
        from hexawyn.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        client = MagicMock()
        client.get_cost_and_usage.side_effect = ClientError(
            {"Error": {"Code": "AccessDenied", "Message": "denied"}}, "GetCostAndUsage"
        )
        adapter = AWSCostAdapter(region="eu-west-1", ce_client=client)

        with pytest.raises(ClusterUnreachableError):
            adapter.estimate_cluster_cost("eks-prod")

    def test_empty_response_returns_defaults(self) -> None:
        from hexawyn.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        client = MagicMock()
        client.get_cost_and_usage.return_value = {"ResultsByTime": []}
        adapter = AWSCostAdapter(region="eu-west-1", ce_client=client)

        report = adapter.estimate_cluster_cost("eks-prod")

        assert report["total_monthly_cost_usd"] == 0.0
        assert report["namespace_costs"] == []

    def test_non_dict_time_block_skipped(self) -> None:
        from hexawyn.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        client = MagicMock()
        client.get_cost_and_usage.return_value = {"ResultsByTime": [None, {"Groups": []}]}
        adapter = AWSCostAdapter(region="eu-west-1", ce_client=client)

        report = adapter.estimate_cluster_cost("eks-prod")
        assert report["total_monthly_cost_usd"] == 0.0

    def test_non_dict_group_skipped(self) -> None:
        from hexawyn.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        client = MagicMock()
        client.get_cost_and_usage.return_value = {
            "ResultsByTime": [
                {
                    "Groups": [
                        None,
                        {"Keys": ["ns"], "Metrics": {"UnblendedCost": {"Amount": "100.0"}}},
                    ]
                }
            ]
        }
        adapter = AWSCostAdapter(region="eu-west-1", ce_client=client)

        report = adapter.estimate_cluster_cost("eks-prod")
        assert report["total_monthly_cost_usd"] == 100.0

    def test_lazy_client_creation(self) -> None:
        from unittest.mock import patch

        from hexawyn.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        fake_client = MagicMock()
        fake_client.get_cost_and_usage.return_value = {"ResultsByTime": []}
        with patch("boto3.client", return_value=fake_client):
            adapter = AWSCostAdapter(region="eu-west-1", ce_client=None)

            report = adapter.estimate_cluster_cost("eks-prod")

        assert report["total_monthly_cost_usd"] == 0.0
        fake_client.get_cost_and_usage.assert_called_once()

    def test_results_by_time_not_a_list(self) -> None:
        from hexawyn.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        client = MagicMock()
        client.get_cost_and_usage.return_value = {}
        adapter = AWSCostAdapter(region="eu-west-1", ce_client=client)

        report = adapter.estimate_cluster_cost("eks-prod")
        assert report["total_monthly_cost_usd"] == 0.0

    def test_groups_not_a_list(self) -> None:
        from hexawyn.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        client = MagicMock()
        client.get_cost_and_usage.return_value = {"ResultsByTime": [{"Groups": "oops"}]}
        adapter = AWSCostAdapter(region="eu-west-1", ce_client=client)

        report = adapter.estimate_cluster_cost("eks-prod")
        assert report["total_monthly_cost_usd"] == 0.0

    def test_keys_not_list(self) -> None:
        from hexawyn.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        client = MagicMock()
        client.get_cost_and_usage.return_value = {
            "ResultsByTime": [
                {"Groups": [{"Keys": None, "Metrics": {"UnblendedCost": {"Amount": "100.0"}}}]}
            ]
        }
        adapter = AWSCostAdapter(region="eu-west-1", ce_client=client)

        report = adapter.estimate_cluster_cost("eks-prod")
        assert report["total_monthly_cost_usd"] == 0.0

    def test_metrics_not_a_dict(self) -> None:
        from hexawyn.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        client = MagicMock()
        client.get_cost_and_usage.return_value = {
            "ResultsByTime": [{"Groups": [{"Keys": ["ns"], "Metrics": "oops"}]}]
        }
        adapter = AWSCostAdapter(region="eu-west-1", ce_client=client)

        report = adapter.estimate_cluster_cost("eks-prod")
        assert report["total_monthly_cost_usd"] == 0.0

    def test_unexpected_error_translated(self) -> None:
        from hexawyn.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        client = MagicMock()
        client.get_cost_and_usage.side_effect = RuntimeError("boom")
        adapter = AWSCostAdapter(region="eu-west-1", ce_client=client)

        with pytest.raises(ClusterUnreachableError):
            adapter.estimate_cluster_cost("eks-prod")

    def test_unblended_cost_not_a_dict(self) -> None:
        from hexawyn.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        client = MagicMock()
        client.get_cost_and_usage.return_value = {
            "ResultsByTime": [{"Groups": [{"Keys": ["ns"], "Metrics": {"UnblendedCost": "bad"}}]}]
        }
        adapter = AWSCostAdapter(region="eu-west-1", ce_client=client)

        report = adapter.estimate_cluster_cost("eks-prod")
        assert report["total_monthly_cost_usd"] == 0.0
