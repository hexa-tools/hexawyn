from __future__ import annotations

from collections import defaultdict

from hexawyn.application.ports.driven.cluster_resource_metrics_port import (
    NodeUtilizationSeries,
)
from hexawyn.application.ports.driven.hot_node_analysis_port import PodUsageRaw
from hexawyn.domain.models.hot_node_analysis import TopConsumer


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_node_series__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_node_series__mutmut)
def node_series(
    node_utilization: dict[str, NodeUtilizationSeries], node_name: str
) -> NodeUtilizationSeries:
    return node_utilization.get(node_name) or {
        "cpu_percent_series": [],
        "memory_percent_series": [],
    }


def x_node_series__mutmut_orig(
    node_utilization: dict[str, NodeUtilizationSeries], node_name: str
) -> NodeUtilizationSeries:
    return node_utilization.get(node_name) or {
        "cpu_percent_series": [],
        "memory_percent_series": [],
    }


def x_node_series__mutmut_1(
    node_utilization: dict[str, NodeUtilizationSeries], node_name: str
) -> NodeUtilizationSeries:
    return node_utilization.get(node_name) and {
        "cpu_percent_series": [],
        "memory_percent_series": [],
    }


def x_node_series__mutmut_2(
    node_utilization: dict[str, NodeUtilizationSeries], node_name: str
) -> NodeUtilizationSeries:
    return node_utilization.get(None) or {
        "cpu_percent_series": [],
        "memory_percent_series": [],
    }


def x_node_series__mutmut_3(
    node_utilization: dict[str, NodeUtilizationSeries], node_name: str
) -> NodeUtilizationSeries:
    return node_utilization.get(node_name) or {
        "XXcpu_percent_seriesXX": [],
        "memory_percent_series": [],
    }


def x_node_series__mutmut_4(
    node_utilization: dict[str, NodeUtilizationSeries], node_name: str
) -> NodeUtilizationSeries:
    return node_utilization.get(node_name) or {
        "CPU_PERCENT_SERIES": [],
        "memory_percent_series": [],
    }


def x_node_series__mutmut_5(
    node_utilization: dict[str, NodeUtilizationSeries], node_name: str
) -> NodeUtilizationSeries:
    return node_utilization.get(node_name) or {
        "cpu_percent_series": [],
        "XXmemory_percent_seriesXX": [],
    }


def x_node_series__mutmut_6(
    node_utilization: dict[str, NodeUtilizationSeries], node_name: str
) -> NodeUtilizationSeries:
    return node_utilization.get(node_name) or {
        "cpu_percent_series": [],
        "MEMORY_PERCENT_SERIES": [],
    }

mutants_x_node_series__mutmut['_mutmut_orig'] = x_node_series__mutmut_orig # type: ignore # mutmut generated
mutants_x_node_series__mutmut['x_node_series__mutmut_1'] = x_node_series__mutmut_1 # type: ignore # mutmut generated
mutants_x_node_series__mutmut['x_node_series__mutmut_2'] = x_node_series__mutmut_2 # type: ignore # mutmut generated
mutants_x_node_series__mutmut['x_node_series__mutmut_3'] = x_node_series__mutmut_3 # type: ignore # mutmut generated
mutants_x_node_series__mutmut['x_node_series__mutmut_4'] = x_node_series__mutmut_4 # type: ignore # mutmut generated
mutants_x_node_series__mutmut['x_node_series__mutmut_5'] = x_node_series__mutmut_5 # type: ignore # mutmut generated
mutants_x_node_series__mutmut['x_node_series__mutmut_6'] = x_node_series__mutmut_6 # type: ignore # mutmut generated
mutants_x_group_non_daemonset_pods__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_group_non_daemonset_pods__mutmut)
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


def x_group_non_daemonset_pods__mutmut_orig(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
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


def x_group_non_daemonset_pods__mutmut_1(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = None
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


def x_group_non_daemonset_pods__mutmut_2(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(None)
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


def x_group_non_daemonset_pods__mutmut_3(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["XXis_daemonsetXX"]:
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


def x_group_non_daemonset_pods__mutmut_4(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["IS_DAEMONSET"]:
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


def x_group_non_daemonset_pods__mutmut_5(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            break
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=raw["namespace"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x_group_non_daemonset_pods__mutmut_6(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            None
        )
    return pods_by_node


def x_group_non_daemonset_pods__mutmut_7(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["XXnode_nameXX"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=raw["namespace"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x_group_non_daemonset_pods__mutmut_8(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["NODE_NAME"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=raw["namespace"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x_group_non_daemonset_pods__mutmut_9(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=None,
                namespace=raw["namespace"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x_group_non_daemonset_pods__mutmut_10(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=None,
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x_group_non_daemonset_pods__mutmut_11(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=raw["namespace"],
                cpu_usage_cores=None,
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x_group_non_daemonset_pods__mutmut_12(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=raw["namespace"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=None,
            )
        )
    return pods_by_node


def x_group_non_daemonset_pods__mutmut_13(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                namespace=raw["namespace"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x_group_non_daemonset_pods__mutmut_14(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x_group_non_daemonset_pods__mutmut_15(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=raw["namespace"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x_group_non_daemonset_pods__mutmut_16(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=raw["namespace"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                )
        )
    return pods_by_node


def x_group_non_daemonset_pods__mutmut_17(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["XXpod_nameXX"],
                namespace=raw["namespace"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x_group_non_daemonset_pods__mutmut_18(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["POD_NAME"],
                namespace=raw["namespace"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x_group_non_daemonset_pods__mutmut_19(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=raw["XXnamespaceXX"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x_group_non_daemonset_pods__mutmut_20(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=raw["NAMESPACE"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x_group_non_daemonset_pods__mutmut_21(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=raw["namespace"],
                cpu_usage_cores=raw["XXcpu_usage_coresXX"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x_group_non_daemonset_pods__mutmut_22(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=raw["namespace"],
                cpu_usage_cores=raw["CPU_USAGE_CORES"],
                memory_usage_gb=raw["memory_usage_gb"],
            )
        )
    return pods_by_node


def x_group_non_daemonset_pods__mutmut_23(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=raw["namespace"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=raw["XXmemory_usage_gbXX"],
            )
        )
    return pods_by_node


def x_group_non_daemonset_pods__mutmut_24(pod_usage: list[PodUsageRaw]) -> dict[str, list[TopConsumer]]:
    pods_by_node: dict[str, list[TopConsumer]] = defaultdict(list)
    for raw in pod_usage:
        if raw["is_daemonset"]:
            continue
        pods_by_node[raw["node_name"]].append(
            TopConsumer(
                pod_name=raw["pod_name"],
                namespace=raw["namespace"],
                cpu_usage_cores=raw["cpu_usage_cores"],
                memory_usage_gb=raw["MEMORY_USAGE_GB"],
            )
        )
    return pods_by_node

mutants_x_group_non_daemonset_pods__mutmut['_mutmut_orig'] = x_group_non_daemonset_pods__mutmut_orig # type: ignore # mutmut generated
mutants_x_group_non_daemonset_pods__mutmut['x_group_non_daemonset_pods__mutmut_1'] = x_group_non_daemonset_pods__mutmut_1 # type: ignore # mutmut generated
mutants_x_group_non_daemonset_pods__mutmut['x_group_non_daemonset_pods__mutmut_2'] = x_group_non_daemonset_pods__mutmut_2 # type: ignore # mutmut generated
mutants_x_group_non_daemonset_pods__mutmut['x_group_non_daemonset_pods__mutmut_3'] = x_group_non_daemonset_pods__mutmut_3 # type: ignore # mutmut generated
mutants_x_group_non_daemonset_pods__mutmut['x_group_non_daemonset_pods__mutmut_4'] = x_group_non_daemonset_pods__mutmut_4 # type: ignore # mutmut generated
mutants_x_group_non_daemonset_pods__mutmut['x_group_non_daemonset_pods__mutmut_5'] = x_group_non_daemonset_pods__mutmut_5 # type: ignore # mutmut generated
mutants_x_group_non_daemonset_pods__mutmut['x_group_non_daemonset_pods__mutmut_6'] = x_group_non_daemonset_pods__mutmut_6 # type: ignore # mutmut generated
mutants_x_group_non_daemonset_pods__mutmut['x_group_non_daemonset_pods__mutmut_7'] = x_group_non_daemonset_pods__mutmut_7 # type: ignore # mutmut generated
mutants_x_group_non_daemonset_pods__mutmut['x_group_non_daemonset_pods__mutmut_8'] = x_group_non_daemonset_pods__mutmut_8 # type: ignore # mutmut generated
mutants_x_group_non_daemonset_pods__mutmut['x_group_non_daemonset_pods__mutmut_9'] = x_group_non_daemonset_pods__mutmut_9 # type: ignore # mutmut generated
mutants_x_group_non_daemonset_pods__mutmut['x_group_non_daemonset_pods__mutmut_10'] = x_group_non_daemonset_pods__mutmut_10 # type: ignore # mutmut generated
mutants_x_group_non_daemonset_pods__mutmut['x_group_non_daemonset_pods__mutmut_11'] = x_group_non_daemonset_pods__mutmut_11 # type: ignore # mutmut generated
mutants_x_group_non_daemonset_pods__mutmut['x_group_non_daemonset_pods__mutmut_12'] = x_group_non_daemonset_pods__mutmut_12 # type: ignore # mutmut generated
mutants_x_group_non_daemonset_pods__mutmut['x_group_non_daemonset_pods__mutmut_13'] = x_group_non_daemonset_pods__mutmut_13 # type: ignore # mutmut generated
mutants_x_group_non_daemonset_pods__mutmut['x_group_non_daemonset_pods__mutmut_14'] = x_group_non_daemonset_pods__mutmut_14 # type: ignore # mutmut generated
mutants_x_group_non_daemonset_pods__mutmut['x_group_non_daemonset_pods__mutmut_15'] = x_group_non_daemonset_pods__mutmut_15 # type: ignore # mutmut generated
mutants_x_group_non_daemonset_pods__mutmut['x_group_non_daemonset_pods__mutmut_16'] = x_group_non_daemonset_pods__mutmut_16 # type: ignore # mutmut generated
mutants_x_group_non_daemonset_pods__mutmut['x_group_non_daemonset_pods__mutmut_17'] = x_group_non_daemonset_pods__mutmut_17 # type: ignore # mutmut generated
mutants_x_group_non_daemonset_pods__mutmut['x_group_non_daemonset_pods__mutmut_18'] = x_group_non_daemonset_pods__mutmut_18 # type: ignore # mutmut generated
mutants_x_group_non_daemonset_pods__mutmut['x_group_non_daemonset_pods__mutmut_19'] = x_group_non_daemonset_pods__mutmut_19 # type: ignore # mutmut generated
mutants_x_group_non_daemonset_pods__mutmut['x_group_non_daemonset_pods__mutmut_20'] = x_group_non_daemonset_pods__mutmut_20 # type: ignore # mutmut generated
mutants_x_group_non_daemonset_pods__mutmut['x_group_non_daemonset_pods__mutmut_21'] = x_group_non_daemonset_pods__mutmut_21 # type: ignore # mutmut generated
mutants_x_group_non_daemonset_pods__mutmut['x_group_non_daemonset_pods__mutmut_22'] = x_group_non_daemonset_pods__mutmut_22 # type: ignore # mutmut generated
mutants_x_group_non_daemonset_pods__mutmut['x_group_non_daemonset_pods__mutmut_23'] = x_group_non_daemonset_pods__mutmut_23 # type: ignore # mutmut generated
mutants_x_group_non_daemonset_pods__mutmut['x_group_non_daemonset_pods__mutmut_24'] = x_group_non_daemonset_pods__mutmut_24 # type: ignore # mutmut generated
