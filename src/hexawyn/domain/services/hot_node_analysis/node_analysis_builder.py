from __future__ import annotations

from hexawyn.domain.models.constants import HotNodeAnalysisConstants
from hexawyn.domain.models.hot_node_analysis import (
    ClusterNodeSnapshot,
    HotNodeAnalysisReport,
    HotNodeAnalysisRequest,
    HotNodeResult,
    Recommendation,
    TopConsumer,
)
from hexawyn.domain.services.hot_node_analysis.hot_node_detection import (
    HotStatus,
    compute_hot_status,
)
from hexawyn.domain.services.hot_node_analysis.redistribution import (
    RedistributionResult,
    find_redistribution_target,
)
from hexawyn.domain.services.hot_node_analysis.top_consumers import select_top_consumers

_cfg = HotNodeAnalysisConstants()


def analyze_hot_nodes(
    request: HotNodeAnalysisRequest, snapshots: list[ClusterNodeSnapshot]
) -> HotNodeAnalysisReport:
    excluded_cordoned = [snap.node_name for snap in snapshots if snap.cordoned]
    eligible = [snap for snap in snapshots if not snap.cordoned]

    warnings: list[str] = []
    analyzable: list[ClusterNodeSnapshot] = []
    for snap in eligible:
        if not snap.cpu_percent_series and not snap.memory_percent_series:
            warnings.append(
                f"Metrics unavailable for node {snap.node_name!r} — excluded from analysis."
            )
            continue
        analyzable.append(snap)

    statuses = {
        snap.node_name: (
            compute_hot_status(
                snap.cpu_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
            compute_hot_status(
                snap.memory_percent_series, _cfg.hot_threshold_percent, _cfg.hot_duration_percent
            ),
        )
        for snap in analyzable
    }

    hot_names = {
        snap.node_name
        for snap in analyzable
        if statuses[snap.node_name][0].is_hot or statuses[snap.node_name][1].is_hot
    }
    hot_snapshots = [snap for snap in analyzable if snap.node_name in hot_names]
    non_hot_snapshots = [snap for snap in analyzable if snap.node_name not in hot_names]

    hot_results = [
        _build_hot_node_result(snap, statuses[snap.node_name], non_hot_snapshots)
        for snap in hot_snapshots
    ]

    return HotNodeAnalysisReport(
        hot_nodes=hot_results,
        healthy_node_count=len(non_hot_snapshots),
        excluded_cordoned_nodes=excluded_cordoned,
        warnings=warnings,
        summary=_build_summary(hot_results, len(non_hot_snapshots), warnings),
    )


def _build_hot_node_result(
    snap: ClusterNodeSnapshot,
    status_pair: tuple[HotStatus, HotStatus],
    non_hot_snapshots: list[ClusterNodeSnapshot],
) -> HotNodeResult:
    cpu_status, memory_status = status_pair
    top_consumers = select_top_consumers(snap.pods, _cfg.top_consumers_count)
    redistribution = find_redistribution_target(top_consumers, non_hot_snapshots)

    return HotNodeResult(
        node_name=snap.node_name,
        cpu_avg_percent=cpu_status.avg_percent,
        memory_avg_percent=memory_status.avg_percent,
        cpu_hot=cpu_status.is_hot,
        memory_hot=memory_status.is_hot,
        hot_hours=max(cpu_status.hot_hours, memory_status.hot_hours),
        top_consumers=top_consumers,
        feasible_redistribution=redistribution.feasible,
        target_node=redistribution.target_node,
        recommendation=_decide_recommendation(redistribution, snap.pods),
        business_hours_pattern=cpu_status.business_hours_pattern
        or memory_status.business_hours_pattern,
    )


def _decide_recommendation(
    redistribution: RedistributionResult, pods: list[TopConsumer]
) -> Recommendation:
    if redistribution.feasible:
        return "redistribute"
    if _has_single_dominant_pod(pods):
        return "scale_vertically"
    return "add_node"


def _has_single_dominant_pod(pods: list[TopConsumer]) -> bool:
    if not pods:
        return False
    total = sum(pod.cpu_usage_cores for pod in pods)
    if total <= 0:
        return False
    largest = max(pod.cpu_usage_cores for pod in pods)
    return (largest / total) >= _cfg.single_dominant_pod_ratio


def _build_summary(
    hot_results: list[HotNodeResult], healthy_node_count: int, warnings: list[str]
) -> str:
    if not hot_results:
        return (
            f"All {healthy_node_count} node(s) healthy — no nodes consistently "
            f"above {_cfg.hot_threshold_percent:.0f}%."
        )
    names = ", ".join(result.node_name for result in hot_results)
    summary = f"{len(hot_results)} hot node(s) detected: {names}."
    if warnings:
        summary += f" {len(warnings)} node(s) excluded due to missing metrics."
    return summary
