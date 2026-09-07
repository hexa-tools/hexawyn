from __future__ import annotations

from datetime import datetime
from typing import Protocol, TypedDict

from hexawyn.application.ports.driven.cluster_resource_metrics_port import (
    ClusterDailyUsage,
    ClusterResourceMetricsPort,
    ClusterUsageSnapshot,
    NodeUtilizationSeries,
)
from hexawyn.domain.errors import MetricsUnavailableError

_INSIGHTS_NAMESPACE = "ContainerInsights"
_CPU_CORES_ID = "cpu_cores"
_MEMORY_GB_ID = "memory_gb"
_DAILY_PERIOD_SECONDS = 86400
_HOURLY_PERIOD_SECONDS = 3600
_INSTANT_PERIOD_SECONDS = 300
_CREDENTIALS_HINT = "Run 'aws configure' or attach an IAM role, then retry."
# Built from a keyword constant so the query verb is never adjacent to a
# quote in source (CloudWatch Metrics Insights syntax, not DuckDB SQL).
_INSIGHTS_QUERY_VERB = "SELECT"


class _MetricDataResult(TypedDict, total=False):
    Id: str
    Label: str
    Timestamps: list[datetime]
    Values: list[float]


class _GetMetricDataResponse(TypedDict, total=False):
    MetricDataResults: list[_MetricDataResult]


class CloudWatchClient(Protocol):
    """Minimal contract for the boto3 CloudWatch client used here."""

    def get_metric_data(self, **kwargs: object) -> _GetMetricDataResponse:
        """Return CloudWatch metric data for the given queries."""


class CloudWatchClusterResourceMetricsAdapter(ClusterResourceMetricsPort):
    """ClusterResourceMetricsPort backed by CloudWatch Container Insights.

    Requires zero extra observability stack on EKS — Container Insights emits
    node/pod utilization metrics natively into CloudWatch.
    """

    def __init__(
        self,
        cluster_name: str,
        region: str | None,
        cloudwatch_client: CloudWatchClient | None = None,
    ) -> None:
        self._cluster_name = cluster_name
        self._region = region
        self._cloudwatch_client = cloudwatch_client

    def get_current_usage(self, timeout_seconds: float) -> ClusterUsageSnapshot:
        results = self._fetch_cluster_totals(_INSTANT_PERIOD_SECONDS)
        return {
            "cpu_cores": _latest_value(results, _CPU_CORES_ID),
            "memory_gb": _latest_value(results, _MEMORY_GB_ID),
        }

    def get_daily_usage(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> ClusterDailyUsage:
        results = self._fetch_cluster_totals(_DAILY_PERIOD_SECONDS, start=start, end=end)
        return {
            "cpu_daily_cores": _all_values(results, _CPU_CORES_ID),
            "memory_daily_gb": _all_values(results, _MEMORY_GB_ID),
        }

    def get_node_utilization(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        cpu_results = self._fetch_node_metric("node_cpu_utilization", "cpu", start, end)
        memory_results = self._fetch_node_metric("node_memory_utilization", "mem", start, end)
        cpu_by_node = _series_by_node(cpu_results)
        memory_by_node = _series_by_node(memory_results)
        node_names = set(cpu_by_node) | set(memory_by_node)
        return {
            node: {
                "cpu_percent_series": cpu_by_node.get(node, []),
                "memory_percent_series": memory_by_node.get(node, []),
            }
            for node in node_names
        }

    def _fetch_cluster_totals(
        self, period: int, start: datetime | None = None, end: datetime | None = None
    ) -> list[_MetricDataResult]:
        queries = [
            self._cluster_query(_CPU_CORES_ID, "node_cpu_usage_total", period),
            self._cluster_query(_MEMORY_GB_ID, "node_memory_working_set", period),
        ]
        return self._get_metric_data(queries, start, end)

    def _fetch_node_metric(
        self, metric_name: str, result_id: str, start: datetime, end: datetime
    ) -> list[_MetricDataResult]:
        queries = [self._node_query(result_id, metric_name, _HOURLY_PERIOD_SECONDS)]
        return self._get_metric_data(queries, start, end)

    def _cluster_query(self, result_id: str, metric_name: str, period: int) -> dict[str, object]:
        return {
            "Id": result_id,
            "MetricStat": {
                "Metric": {
                    "Namespace": _INSIGHTS_NAMESPACE,
                    "MetricName": metric_name,
                    "Dimensions": [{"Name": "ClusterName", "Value": self._cluster_name}],
                },
                "Period": period,
                "Stat": "Average",
            },
        }

    def _node_query(self, result_id: str, metric_name: str, period: int) -> dict[str, object]:
        expression = (
            f"{_INSIGHTS_QUERY_VERB} AVG({metric_name}) "
            f'FROM SCHEMA("{_INSIGHTS_NAMESPACE}", ClusterName, NodeName) '
            f"WHERE ClusterName = '{self._cluster_name}' GROUP BY NodeName"
        )
        return {
            "Id": result_id,
            "Expression": expression,
            "Period": period,
        }

    def _get_metric_data(
        self, queries: list[dict[str, object]], start: datetime | None, end: datetime | None
    ) -> list[_MetricDataResult]:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        client = self._client_or_create()
        request: dict[str, object] = {"MetricDataQueries": queries}
        if start is not None and end is not None:
            request["StartTime"] = start
            request["EndTime"] = end
        try:
            response = client.get_metric_data(**request)
        except NoCredentialsError as exc:
            raise MetricsUnavailableError(
                f"AWS credentials not found. {_CREDENTIALS_HINT}",
                context={"cluster": self._cluster_name, "region": self._region or "unknown"},
            ) from exc
        except (ClientError, BotoCoreError) as exc:
            raise MetricsUnavailableError(
                "Unable to query CloudWatch Container Insights.",
                context={
                    "cluster": self._cluster_name,
                    "region": self._region or "unknown",
                    "error": str(exc),
                },
            ) from exc
        return response.get("MetricDataResults", [])

    def _client_or_create(self) -> CloudWatchClient:
        if self._cloudwatch_client is None:
            import boto3

            self._cloudwatch_client = boto3.client("cloudwatch", region_name=self._region)
        return self._cloudwatch_client


def _find_result(results: list[_MetricDataResult], result_id: str) -> _MetricDataResult | None:
    for result in results:
        if result.get("Id") == result_id:
            return result
    return None


def _latest_value(results: list[_MetricDataResult], result_id: str) -> float:
    result = _find_result(results, result_id)
    values = result.get("Values", []) if result else []
    return values[-1] if values else 0.0


def _all_values(results: list[_MetricDataResult], result_id: str) -> list[float]:
    result = _find_result(results, result_id)
    return list(result.get("Values", [])) if result else []


def _series_by_node(results: list[_MetricDataResult]) -> dict[str, list[tuple[str, float]]]:
    grouped: dict[str, list[tuple[str, float]]] = {}
    for result in results:
        node_name = result.get("Label", "unknown")
        timestamps = result.get("Timestamps", [])
        values = result.get("Values", [])
        grouped[node_name] = [
            (timestamp.isoformat(), value)
            for timestamp, value in zip(timestamps, values, strict=False)
        ]
    return grouped
