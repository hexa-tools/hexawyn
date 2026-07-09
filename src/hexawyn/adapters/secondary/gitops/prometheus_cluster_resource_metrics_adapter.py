from __future__ import annotations

from datetime import datetime

from hexawyn.application.ports.driven.cluster_resource_metrics_port import (
    ClusterDailyUsage,
    ClusterResourceMetricsPort,
    ClusterUsageSnapshot,
    NodeUtilizationSeries,
)
from hexawyn.application.ports.driven.metrics_query_port import (
    MetricsQueryPort,
    PrometheusRangeSample,
)

_CPU_USAGE_PROMQL = 'sum(rate(container_cpu_usage_seconds_total{container!=""}[5m]))'
_MEMORY_USAGE_PROMQL = 'sum(container_memory_working_set_bytes{container!=""}) / (1024*1024*1024)'
_CPU_UTIL_BY_NODE_PROMQL = (
    '100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)'
)
_MEMORY_UTIL_BY_NODE_PROMQL = (
    "(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100"
)
_DAILY_STEP = "1d"
_HOURLY_STEP = "1h"


class PrometheusClusterResourceMetricsAdapter(ClusterResourceMetricsPort):
    """ClusterResourceMetricsPort backed by Prometheus (PromQL).

    Owns the PromQL definitions so that consuming services stay
    query-language agnostic.
    """

    def __init__(self, metrics_query_port: MetricsQueryPort) -> None:
        self._metrics = metrics_query_port

    def get_current_usage(self, timeout_seconds: float) -> ClusterUsageSnapshot:
        return {
            "cpu_cores": self._instant_value(_CPU_USAGE_PROMQL, timeout_seconds),
            "memory_gb": self._instant_value(_MEMORY_USAGE_PROMQL, timeout_seconds),
        }

    def get_daily_usage(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> ClusterDailyUsage:
        return {
            "cpu_daily_cores": self._single_series(
                _CPU_USAGE_PROMQL, start, end, _DAILY_STEP, timeout_seconds
            ),
            "memory_daily_gb": self._single_series(
                _MEMORY_USAGE_PROMQL, start, end, _DAILY_STEP, timeout_seconds
            ),
        }

    def get_node_utilization(
        self, start: datetime, end: datetime, timeout_seconds: float
    ) -> dict[str, NodeUtilizationSeries]:
        cpu_by_node = self._series_by_node(
            _CPU_UTIL_BY_NODE_PROMQL, start, end, _HOURLY_STEP, timeout_seconds
        )
        memory_by_node = self._series_by_node(
            _MEMORY_UTIL_BY_NODE_PROMQL, start, end, _HOURLY_STEP, timeout_seconds
        )
        node_names = set(cpu_by_node) | set(memory_by_node)
        return {
            node: {
                "cpu_percent_series": cpu_by_node.get(node, []),
                "memory_percent_series": memory_by_node.get(node, []),
            }
            for node in node_names
        }

    def _instant_value(self, promql: str, timeout_seconds: float) -> float:
        samples = self._metrics.instant_query(promql, timeout_seconds=timeout_seconds)
        return samples[0]["value"] if samples else 0.0

    def _single_series(
        self, promql: str, start: datetime, end: datetime, step: str, timeout_seconds: float
    ) -> list[float]:
        samples = self._range_query(promql, start, end, step, timeout_seconds)
        if not samples:
            return []
        return [value for _, value in samples[0]["values"]]

    def _series_by_node(
        self, promql: str, start: datetime, end: datetime, step: str, timeout_seconds: float
    ) -> dict[str, list[tuple[str, float]]]:
        samples = self._range_query(promql, start, end, step, timeout_seconds)
        grouped: dict[str, list[tuple[str, float]]] = {}
        for sample in samples:
            node_name = (
                sample["metric"].get("instance") or sample["metric"].get("node") or "unknown"
            )
            grouped[node_name] = sample["values"]
        return grouped

    def _range_query(
        self, promql: str, start: datetime, end: datetime, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        return self._metrics.range_query(
            promql,
            start=start.isoformat(),
            end=end.isoformat(),
            step=step,
            timeout_seconds=timeout_seconds,
        )
