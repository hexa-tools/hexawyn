from __future__ import annotations

from datetime import UTC, datetime
from unittest.mock import MagicMock

import pytest
from botocore.exceptions import ClientError, NoCredentialsError
from hexawyn.adapters.secondary.aws.cloudwatch_metrics_adapter import (
    CloudWatchClusterResourceMetricsAdapter,
    _all_values,
    _find_result,
    _latest_value,
    _series_by_node,
)
from hexawyn.domain.errors import MetricsUnavailableError


class TestCloudWatchClusterResourceMetricsAdapter:
    @staticmethod
    def _adapter(
        cluster_name: str = "test-cluster",
        region: str | None = "us-east-1",
        cloudwatch_client: object | None = None,
    ) -> CloudWatchClusterResourceMetricsAdapter:
        return CloudWatchClusterResourceMetricsAdapter(
            cluster_name=cluster_name,
            region=region,
            cloudwatch_client=cloudwatch_client,
        )

    def test_get_current_usage_empty_response_returns_zeros(self) -> None:
        mock_client = MagicMock()
        mock_client.get_metric_data.return_value = {"MetricDataResults": []}
        adapter = self._adapter(cloudwatch_client=mock_client)

        result = adapter.get_current_usage(timeout_seconds=30.0)

        assert result["cpu_cores"] == 0.0  # noqa: PLR2004
        assert result["memory_gb"] == 0.0  # noqa: PLR2004

    def test_get_current_usage_parses_data(self) -> None:
        mock_client = MagicMock()
        mock_client.get_metric_data.return_value = {
            "MetricDataResults": [
                {"Id": "cpu_cores", "Label": "cpu", "Values": [2.5], "Timestamps": []},
                {"Id": "memory_gb", "Label": "mem", "Values": [8.0], "Timestamps": []},
            ]
        }
        adapter = self._adapter(cloudwatch_client=mock_client)

        result = adapter.get_current_usage(timeout_seconds=30.0)

        assert result["cpu_cores"] == 2.5  # noqa: PLR2004
        assert result["memory_gb"] == 8.0  # noqa: PLR2004

    def test_get_daily_usage_empty_response_returns_empty_lists(self) -> None:
        mock_client = MagicMock()
        mock_client.get_metric_data.return_value = {"MetricDataResults": []}
        adapter = self._adapter(cloudwatch_client=mock_client)

        result = adapter.get_daily_usage(
            start=datetime(2024, 1, 1, tzinfo=UTC),
            end=datetime(2024, 1, 2, tzinfo=UTC),
            timeout_seconds=30.0,
        )

        assert result["cpu_daily_cores"] == []
        assert result["memory_daily_gb"] == []

    def test_get_daily_usage_parses_data(self) -> None:
        mock_client = MagicMock()
        mock_client.get_metric_data.return_value = {
            "MetricDataResults": [
                {"Id": "cpu_cores", "Values": [1.0, 2.0, 3.0], "Timestamps": []},
                {"Id": "memory_gb", "Values": [4.0, 5.0], "Timestamps": []},
            ]
        }
        adapter = self._adapter(cloudwatch_client=mock_client)

        result = adapter.get_daily_usage(
            start=datetime(2024, 1, 1, tzinfo=UTC),
            end=datetime(2024, 1, 2, tzinfo=UTC),
            timeout_seconds=30.0,
        )

        assert result["cpu_daily_cores"] == [1.0, 2.0, 3.0]
        assert result["memory_daily_gb"] == [4.0, 5.0]

    def test_get_node_utilization_empty_response_returns_empty_dict(self) -> None:
        mock_client = MagicMock()
        mock_client.get_metric_data.return_value = {"MetricDataResults": []}
        adapter = self._adapter(cloudwatch_client=mock_client)

        result = adapter.get_node_utilization(
            start=datetime(2024, 1, 1, tzinfo=UTC),
            end=datetime(2024, 1, 2, tzinfo=UTC),
            timeout_seconds=30.0,
        )

        assert result == {}

    def test_get_node_utilization_groups_by_node(self) -> None:
        mock_client = MagicMock()
        call_count = [0]

        def _side_effect(**kwargs: object) -> dict[str, object]:
            call_count[0] += 1
            if call_count[0] == 1:
                return {
                    "MetricDataResults": [
                        {
                            "Id": "cpu",
                            "Label": "node-1",
                            "Timestamps": [datetime(2024, 1, 1, tzinfo=UTC)],
                            "Values": [55.0],
                        },
                    ]
                }
            return {
                "MetricDataResults": [
                    {
                        "Id": "mem",
                        "Label": "node-1",
                        "Timestamps": [datetime(2024, 1, 1, tzinfo=UTC)],
                        "Values": [70.0],
                    },
                ]
            }

        mock_client.get_metric_data.side_effect = _side_effect
        adapter = self._adapter(cloudwatch_client=mock_client)

        result = adapter.get_node_utilization(
            start=datetime(2024, 1, 1, tzinfo=UTC),
            end=datetime(2024, 1, 2, tzinfo=UTC),
            timeout_seconds=30.0,
        )

        assert "node-1" in result
        assert len(result) == 1  # noqa: PLR2004
        assert len(result["node-1"]["cpu_percent_series"]) == 1  # noqa: PLR2004
        assert len(result["node-1"]["memory_percent_series"]) == 1  # noqa: PLR2004

    def test_no_credentials_raises_metrics_unavailable(self) -> None:
        mock_client = MagicMock()
        mock_client.get_metric_data.side_effect = NoCredentialsError()
        adapter = self._adapter(cloudwatch_client=mock_client)

        with pytest.raises(MetricsUnavailableError, match="credentials"):
            adapter.get_current_usage(timeout_seconds=30.0)

    def test_client_error_raises_metrics_unavailable(self) -> None:
        mock_client = MagicMock()
        error_response = {"Error": {"Code": "InternalError", "Message": "boom"}}
        mock_client.get_metric_data.side_effect = ClientError(error_response, "GetMetricData")
        adapter = self._adapter(cloudwatch_client=mock_client)

        with pytest.raises(MetricsUnavailableError, match="CloudWatch"):
            adapter.get_current_usage(timeout_seconds=30.0)

    def test_client_or_create_returns_injected_client(self) -> None:
        mock_client = MagicMock()
        adapter = self._adapter(cloudwatch_client=mock_client)

        result = adapter._client_or_create()

        assert result is mock_client

    def test_client_or_create_lazy_init_calls_boto3(self) -> None:
        import sys

        mock_boto3 = MagicMock()
        mock_boto3.client.return_value = MagicMock()
        adapter = self._adapter(cloudwatch_client=None)

        with pytest.MonkeyPatch.context() as mp:
            mp.setitem(sys.modules, "boto3", mock_boto3)
            result = adapter._client_or_create()
            assert result is not None
            mock_boto3.client.assert_called_once_with("cloudwatch", region_name="us-east-1")


class TestFindResult:
    def test_finds_by_id(self) -> None:
        result = _find_result([{"Id": "cpu"}, {"Id": "mem"}], "cpu")
        assert result == {"Id": "cpu"}

    def test_returns_none_when_missing(self) -> None:
        result = _find_result([{"Id": "cpu"}], "mem")
        assert result is None

    def test_returns_none_for_empty_list(self) -> None:
        assert _find_result([], "cpu") is None


class TestLatestValue:
    def test_returns_last_value(self) -> None:
        results = [{"Id": "cpu", "Values": [1.0, 2.0, 5.5]}]
        assert _latest_value(results, "cpu") == 5.5  # noqa: PLR2004

    def test_returns_zero_when_no_values(self) -> None:
        results = [{"Id": "cpu", "Values": []}]
        assert _latest_value(results, "cpu") == 0.0  # noqa: PLR2004

    def test_returns_zero_when_id_missing(self) -> None:
        assert _latest_value([], "cpu") == 0.0  # noqa: PLR2004


class TestAllValues:
    def test_returns_all_values(self) -> None:
        results = [{"Id": "cpu", "Values": [1.0, 2.0, 3.0]}]
        assert _all_values(results, "cpu") == [1.0, 2.0, 3.0]

    def test_returns_empty_list_when_id_missing(self) -> None:
        assert _all_values([], "cpu") == []

    def test_returns_empty_list_when_no_values(self) -> None:
        results = [{"Id": "cpu"}]
        assert _all_values(results, "cpu") == []


class TestSeriesByNode:
    def test_groups_by_label(self) -> None:
        t1 = datetime(2024, 1, 1, 0, 0, 0, tzinfo=UTC)
        t2 = datetime(2024, 1, 1, 1, 0, 0, tzinfo=UTC)
        results = [
            {"Id": "a", "Label": "node-1", "Timestamps": [t1], "Values": [10.0]},
            {"Id": "b", "Label": "node-2", "Timestamps": [t2], "Values": [20.0]},
        ]
        grouped = _series_by_node(results)

        assert set(grouped.keys()) == {"node-1", "node-2"}
        assert len(grouped["node-1"]) == 1  # noqa: PLR2004
        assert grouped["node-1"][0][1] == 10.0  # noqa: PLR2004
        assert grouped["node-2"][0][1] == 20.0  # noqa: PLR2004

    def test_last_result_wins_for_same_label(self) -> None:
        t1 = datetime(2024, 1, 1, 0, 0, 0, tzinfo=UTC)
        t2 = datetime(2024, 1, 1, 1, 0, 0, tzinfo=UTC)
        results = [
            {"Id": "a", "Label": "node-1", "Timestamps": [t1], "Values": [10.0]},
            {"Id": "b", "Label": "node-1", "Timestamps": [t2], "Values": [20.0]},
        ]
        grouped = _series_by_node(results)

        assert len(grouped["node-1"]) == 1  # noqa: PLR2004
        assert grouped["node-1"][0][1] == 20.0  # noqa: PLR2004

    def test_uses_unknown_label_when_missing(self) -> None:
        t1 = datetime(2024, 1, 1, tzinfo=UTC)
        results = [{"Id": "a", "Timestamps": [t1], "Values": [42.0]}]
        grouped = _series_by_node(results)

        assert "unknown" in grouped
        assert grouped["unknown"][0][1] == 42.0  # noqa: PLR2004

    def test_returns_empty_on_no_results(self) -> None:
        assert _series_by_node([]) == {}
