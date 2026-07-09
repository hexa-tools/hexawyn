from datetime import UTC, datetime
from unittest.mock import MagicMock, patch

import pytest

boto3 = pytest.importorskip("boto3")
from botocore.exceptions import (  # noqa: E402
    ClientError,
    EndpointConnectionError,
    NoCredentialsError,
)
from hexawyn.application.ports.driven.cluster_resource_metrics_port import (  # noqa: E402
    ClusterResourceMetricsPort,
)
from hexawyn.domain.errors import MetricsUnavailableError  # noqa: E402


def _start_end() -> tuple[datetime, datetime]:
    return datetime(2026, 1, 1, tzinfo=UTC), datetime(2026, 1, 10, tzinfo=UTC)


def _result(result_id: str, label: str, values: list[float]) -> dict:
    base = datetime(2026, 1, 1, tzinfo=UTC)
    return {
        "Id": result_id,
        "Label": label,
        "Timestamps": [base for _ in values],
        "Values": values,
    }


class TestContract:
    def test_is_a_cluster_resource_metrics_port(self) -> None:
        from hexawyn.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )

        adapter = CloudWatchClusterResourceMetricsAdapter(
            cluster_name="prod", region="eu-west-1", cloudwatch_client=MagicMock()
        )

        assert isinstance(adapter, ClusterResourceMetricsPort)


class TestGetCurrentUsage:
    def test_returns_latest_cpu_and_memory(self) -> None:
        from hexawyn.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )

        client = MagicMock()
        client.get_metric_data.return_value = {
            "MetricDataResults": [
                _result("cpu_cores", "cpu", [10.0, 12.5]),
                _result("memory_gb", "memory", [40.0, 48.0]),
            ]
        }
        adapter = CloudWatchClusterResourceMetricsAdapter(
            cluster_name="prod", region="eu-west-1", cloudwatch_client=client
        )

        usage = adapter.get_current_usage(timeout_seconds=15.0)

        assert usage == {"cpu_cores": 12.5, "memory_gb": 48.0}

    def test_defaults_to_zero_when_no_datapoints(self) -> None:
        from hexawyn.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )

        client = MagicMock()
        client.get_metric_data.return_value = {"MetricDataResults": []}
        adapter = CloudWatchClusterResourceMetricsAdapter(
            cluster_name="prod", region="eu-west-1", cloudwatch_client=client
        )

        usage = adapter.get_current_usage(timeout_seconds=15.0)

        assert usage == {"cpu_cores": 0.0, "memory_gb": 0.0}


class TestGetDailyUsage:
    def test_returns_value_series(self) -> None:
        from hexawyn.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )

        client = MagicMock()
        client.get_metric_data.return_value = {
            "MetricDataResults": [
                _result("cpu_cores", "cpu", [1.0, 2.0, 3.0]),
                _result("memory_gb", "memory", [4.0, 5.0, 6.0]),
            ]
        }
        adapter = CloudWatchClusterResourceMetricsAdapter(
            cluster_name="prod", region="eu-west-1", cloudwatch_client=client
        )
        start, end = _start_end()

        daily = adapter.get_daily_usage(start, end, timeout_seconds=15.0)

        assert daily == {
            "cpu_daily_cores": [1.0, 2.0, 3.0],
            "memory_daily_gb": [4.0, 5.0, 6.0],
        }


class TestGetNodeUtilization:
    def test_groups_series_by_node_label(self) -> None:
        from hexawyn.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )

        client = MagicMock()
        client.get_metric_data.side_effect = [
            {"MetricDataResults": [_result("cpu", "node-a", [80.0])]},
            {"MetricDataResults": [_result("mem", "node-a", [55.0])]},
        ]
        adapter = CloudWatchClusterResourceMetricsAdapter(
            cluster_name="prod", region="eu-west-1", cloudwatch_client=client
        )
        start, end = _start_end()

        result = adapter.get_node_utilization(start, end, timeout_seconds=15.0)

        assert result["node-a"]["cpu_percent_series"][0][1] == 80.0
        assert result["node-a"]["memory_percent_series"][0][1] == 55.0


class TestErrorTranslation:
    def _adapter_with_error(self, exc: Exception) -> object:
        from hexawyn.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )

        client = MagicMock()
        client.get_metric_data.side_effect = exc
        return CloudWatchClusterResourceMetricsAdapter(
            cluster_name="prod", region="eu-west-1", cloudwatch_client=client
        )

    def test_missing_credentials(self) -> None:
        adapter = self._adapter_with_error(NoCredentialsError())

        with pytest.raises(MetricsUnavailableError) as exc_info:
            adapter.get_current_usage(timeout_seconds=15.0)  # type: ignore[attr-defined]

        assert "aws configure" in str(exc_info.value).lower()

    def test_client_error(self) -> None:
        adapter = self._adapter_with_error(
            ClientError({"Error": {"Code": "AccessDenied", "Message": "no"}}, "GetMetricData")
        )

        with pytest.raises(MetricsUnavailableError):
            adapter.get_current_usage(timeout_seconds=15.0)  # type: ignore[attr-defined]

    def test_endpoint_connection_error(self) -> None:
        adapter = self._adapter_with_error(
            EndpointConnectionError(endpoint_url="https://monitoring.eu-west-1.amazonaws.com")
        )

        with pytest.raises(MetricsUnavailableError):
            adapter.get_current_usage(timeout_seconds=15.0)  # type: ignore[attr-defined]


class TestLazyClientCreation:
    def test_lazily_creates_boto3_client(self) -> None:
        from hexawyn.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )

        created = MagicMock()
        created.get_metric_data.return_value = {"MetricDataResults": []}
        adapter = CloudWatchClusterResourceMetricsAdapter(cluster_name="prod", region="eu-west-1")

        with patch.object(boto3, "client", return_value=created) as mock_client:
            adapter.get_current_usage(timeout_seconds=15.0)

        mock_client.assert_called_once_with("cloudwatch", region_name="eu-west-1")
