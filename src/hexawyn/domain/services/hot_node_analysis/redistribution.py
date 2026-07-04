from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.hot_node_analysis import ClusterNodeSnapshot, TopConsumer


@dataclass(frozen=True)
class RedistributionResult:
    feasible: bool
    target_node: str | None
    moved_pod_count: int


def find_redistribution_target(
    top_consumers: list[TopConsumer], candidate_nodes: list[ClusterNodeSnapshot]
) -> RedistributionResult:
    """Greedy partial-fit simulation — a candidate node absorbing *some* of
    the top consumers (not necessarily all) still counts as feasible, since
    partial redistribution is a real, useful outcome (see ticket TC2)."""
    if not top_consumers or not candidate_nodes:
        return RedistributionResult(feasible=False, target_node=None, moved_pod_count=0)

    ranked = sorted(candidate_nodes, key=_available_headroom, reverse=True)

    best_target: str | None = None
    best_moved = 0
    for node in ranked:
        moved = _count_fitting(top_consumers, _available_headroom(node))
        if moved > best_moved:
            best_moved = moved
            best_target = node.node_name

    return RedistributionResult(
        feasible=best_moved > 0, target_node=best_target, moved_pod_count=best_moved
    )


def _available_headroom(node: ClusterNodeSnapshot) -> float:
    used = sum(pod.cpu_usage_cores for pod in node.pods)
    return node.allocatable_cpu_cores - used


def _count_fitting(consumers: list[TopConsumer], available_headroom: float) -> int:
    remaining = available_headroom
    moved = 0
    for consumer in consumers:
        if consumer.cpu_usage_cores <= remaining:
            remaining -= consumer.cpu_usage_cores
            moved += 1
    return moved
