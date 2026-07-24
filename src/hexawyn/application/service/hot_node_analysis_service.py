from __future__ import annotations

from collections import defaultdict
from datetime import UTC, datetime, timedelta

from hexawyn.application.ports.driven.cluster_resource_metrics_port import (
    ClusterResourceMetricsPort,
    NodeUtilizationSeries,
)
from hexawyn.application.ports.driven.hot_node_analysis_port import (
    HotNodeAnalysisPort,
    PodUsageRaw,
)
from hexawyn.application.use_case.hot_node_analysis.command import (
    HotNodeAnalysisCommand,
)
from hexawyn.application.use_case.hot_node_analysis.response import (
    HotNodeAnalysisResponse,
    HotNodeResultDict,
    TopConsumerDict,
)
from hexawyn.application.ports.driving.hot_node_analysis.hot_node_analysis_service_port import (
    HotNodeAnalysisServicePort,
)
from hexawyn.domain.models.hot_node_analysis import (
    ClusterNodeSnapshot,
    HotNodeAnalysisReport,
    HotNodeAnalysisRequest,
    HotNodeResult,
    TopConsumer,
)
from hexawyn.domain.services.hot_node_analysis.node_analysis_builder import analyze_hot_nodes

_QUERY_TIMEOUT_SECONDS = 15.0


class HotNodeAnalysisService(HotNodeAnalysisServicePort):
    def __init__(
        self, metrics_port: ClusterResourceMetricsPort, node_port: HotNodeAnalysisPort
    ) -> None:
        self._metrics_port = metrics_port
        self._node_port = node_port

    def analyze(self, command: HotNodeAnalysisCommand) -> HotNodeAnalysisResponse:
        end = datetime.now(UTC)
        start = end - timedelta(hours=command.window_hours)

        node_utilization = self._metrics_port.get_node_utilization(
            start, end, timeout_seconds=_QUERY_TIMEOUT_SECONDS
        )

        node_infos = self._node_port.list_nodes()
        pods_by_node = _group_non_daemonset_pods(self._node_port.list_pod_usage())

        snapshots = [
            ClusterNodeSnapshot(
                node_name=info["name"],
                cordoned=info["cordoned"],
                allocatable_cpu_cores=info["allocatable_cpu_cores"],
                allocatable_memory_gb=info["allocatable_memory_gb"],
                cpu_percent_series=_node_series(node_utilization, info["name"])[
                    "cpu_percent_series"
                ],
                memory_percent_series=_node_series(node_utilization, info["name"])[
                    "memory_percent_series"
                ],
                pods=pods_by_node.get(info["name"], []),
            )
            for info in node_infos
        ]

        report = analyze_hot_nodes(
            HotNodeAnalysisRequest(window_hours=command.window_hours), snapshots
        )
        return _to_response(report)


def _node_series(
    node_utilization: dict[str, NodeUtilizationSeries], node_name: str
) -> NodeUtilizationSeries:
    return node_utilization.get(node_name) or {
        "cpu_percent_series": [],
        "memory_percent_series": [],
    }


def _group_non_daemonset_pods(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
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


def _to_response(report: HotNodeAnalysisReport) -> HotNodeAnalysisResponse:
    return HotNodeAnalysisResponse(
        hot_nodes=[_to_hot_node_dict(result) for result in report.hot_nodes],
        healthy_node_count=report.healthy_node_count,
        excluded_cordoned_nodes=report.excluded_cordoned_nodes,
        warnings=report.warnings,
        summary=report.summary,
    )


def _to_hot_node_dict(result: HotNodeResult) -> HotNodeResultDict:
    return HotNodeResultDict(
        node_name=result.node_name,
        cpu_avg_percent=result.cpu_avg_percent,
        memory_avg_percent=result.memory_avg_percent,
        cpu_hot=result.cpu_hot,
        memory_hot=result.memory_hot,
        hot_hours=result.hot_hours,
        top_consumers=[_to_consumer_dict(consumer) for consumer in result.top_consumers],
        feasible_redistribution=result.feasible_redistribution,
        target_node=result.target_node,
        recommendation=result.recommendation,
        business_hours_pattern=result.business_hours_pattern,
    )


def _to_consumer_dict(consumer: TopConsumer) -> TopConsumerDict:
    return TopConsumerDict(
        pod_name=consumer.pod_name,
        namespace=consumer.namespace,
        cpu_usage_cores=consumer.cpu_usage_cores,
        memory_usage_gb=consumer.memory_usage_gb,
    )
