from __future__ import annotations

from collections import defaultdict

from hexawyn.application.ports.driven.cluster_resource_metrics_port import (
    NodeUtilizationSeries,
)
from hexawyn.application.ports.driven.hot_node_analysis_port import PodUsageRaw
from hexawyn.domain.models.hot_node_analysis import TopConsumer


def node_series(
    node_utilization: dict[str, NodeUtilizationSeries], node_name: str
) -> NodeUtilizationSeries:
    return node_utilization.get(node_name) or {
        "cpu_percent_series": [],
        "memory_percent_series": [],
    }


def group_non_daemonset_pods(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=raw["namespace"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node
