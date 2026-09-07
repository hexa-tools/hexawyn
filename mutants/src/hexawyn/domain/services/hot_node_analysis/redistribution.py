from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.hot_node_analysis import ClusterNodeSnapshot, TopConsumer


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass(frozen=True)
class RedistributionResult:
    feasible: bool
    target_node: str | None
    moved_pod_count: int
mutants_x_find_redistribution_target__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_find_redistribution_target__mutmut)
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


def x_find_redistribution_target__mutmut_orig(
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


def x_find_redistribution_target__mutmut_1(
    top_consumers: list[TopConsumer], candidate_nodes: list[ClusterNodeSnapshot]
) -> RedistributionResult:
    """Greedy partial-fit simulation — a candidate node absorbing *some* of
    the top consumers (not necessarily all) still counts as feasible, since
    partial redistribution is a real, useful outcome (see ticket TC2)."""
    if not top_consumers and not candidate_nodes:
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


def x_find_redistribution_target__mutmut_2(
    top_consumers: list[TopConsumer], candidate_nodes: list[ClusterNodeSnapshot]
) -> RedistributionResult:
    """Greedy partial-fit simulation — a candidate node absorbing *some* of
    the top consumers (not necessarily all) still counts as feasible, since
    partial redistribution is a real, useful outcome (see ticket TC2)."""
    if top_consumers or not candidate_nodes:
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


def x_find_redistribution_target__mutmut_3(
    top_consumers: list[TopConsumer], candidate_nodes: list[ClusterNodeSnapshot]
) -> RedistributionResult:
    """Greedy partial-fit simulation — a candidate node absorbing *some* of
    the top consumers (not necessarily all) still counts as feasible, since
    partial redistribution is a real, useful outcome (see ticket TC2)."""
    if not top_consumers or candidate_nodes:
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


def x_find_redistribution_target__mutmut_4(
    top_consumers: list[TopConsumer], candidate_nodes: list[ClusterNodeSnapshot]
) -> RedistributionResult:
    """Greedy partial-fit simulation — a candidate node absorbing *some* of
    the top consumers (not necessarily all) still counts as feasible, since
    partial redistribution is a real, useful outcome (see ticket TC2)."""
    if not top_consumers or not candidate_nodes:
        return RedistributionResult(feasible=None, target_node=None, moved_pod_count=0)

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


def x_find_redistribution_target__mutmut_5(
    top_consumers: list[TopConsumer], candidate_nodes: list[ClusterNodeSnapshot]
) -> RedistributionResult:
    """Greedy partial-fit simulation — a candidate node absorbing *some* of
    the top consumers (not necessarily all) still counts as feasible, since
    partial redistribution is a real, useful outcome (see ticket TC2)."""
    if not top_consumers or not candidate_nodes:
        return RedistributionResult(feasible=False, target_node=None, moved_pod_count=None)

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


def x_find_redistribution_target__mutmut_6(
    top_consumers: list[TopConsumer], candidate_nodes: list[ClusterNodeSnapshot]
) -> RedistributionResult:
    """Greedy partial-fit simulation — a candidate node absorbing *some* of
    the top consumers (not necessarily all) still counts as feasible, since
    partial redistribution is a real, useful outcome (see ticket TC2)."""
    if not top_consumers or not candidate_nodes:
        return RedistributionResult(target_node=None, moved_pod_count=0)

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


def x_find_redistribution_target__mutmut_7(
    top_consumers: list[TopConsumer], candidate_nodes: list[ClusterNodeSnapshot]
) -> RedistributionResult:
    """Greedy partial-fit simulation — a candidate node absorbing *some* of
    the top consumers (not necessarily all) still counts as feasible, since
    partial redistribution is a real, useful outcome (see ticket TC2)."""
    if not top_consumers or not candidate_nodes:
        return RedistributionResult(feasible=False, moved_pod_count=0)

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


def x_find_redistribution_target__mutmut_8(
    top_consumers: list[TopConsumer], candidate_nodes: list[ClusterNodeSnapshot]
) -> RedistributionResult:
    """Greedy partial-fit simulation — a candidate node absorbing *some* of
    the top consumers (not necessarily all) still counts as feasible, since
    partial redistribution is a real, useful outcome (see ticket TC2)."""
    if not top_consumers or not candidate_nodes:
        return RedistributionResult(feasible=False, target_node=None, )

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


def x_find_redistribution_target__mutmut_9(
    top_consumers: list[TopConsumer], candidate_nodes: list[ClusterNodeSnapshot]
) -> RedistributionResult:
    """Greedy partial-fit simulation — a candidate node absorbing *some* of
    the top consumers (not necessarily all) still counts as feasible, since
    partial redistribution is a real, useful outcome (see ticket TC2)."""
    if not top_consumers or not candidate_nodes:
        return RedistributionResult(feasible=True, target_node=None, moved_pod_count=0)

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


def x_find_redistribution_target__mutmut_10(
    top_consumers: list[TopConsumer], candidate_nodes: list[ClusterNodeSnapshot]
) -> RedistributionResult:
    """Greedy partial-fit simulation — a candidate node absorbing *some* of
    the top consumers (not necessarily all) still counts as feasible, since
    partial redistribution is a real, useful outcome (see ticket TC2)."""
    if not top_consumers or not candidate_nodes:
        return RedistributionResult(feasible=False, target_node=None, moved_pod_count=1)

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


def x_find_redistribution_target__mutmut_11(
    top_consumers: list[TopConsumer], candidate_nodes: list[ClusterNodeSnapshot]
) -> RedistributionResult:
    """Greedy partial-fit simulation — a candidate node absorbing *some* of
    the top consumers (not necessarily all) still counts as feasible, since
    partial redistribution is a real, useful outcome (see ticket TC2)."""
    if not top_consumers or not candidate_nodes:
        return RedistributionResult(feasible=False, target_node=None, moved_pod_count=0)

    ranked = None

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


def x_find_redistribution_target__mutmut_12(
    top_consumers: list[TopConsumer], candidate_nodes: list[ClusterNodeSnapshot]
) -> RedistributionResult:
    """Greedy partial-fit simulation — a candidate node absorbing *some* of
    the top consumers (not necessarily all) still counts as feasible, since
    partial redistribution is a real, useful outcome (see ticket TC2)."""
    if not top_consumers or not candidate_nodes:
        return RedistributionResult(feasible=False, target_node=None, moved_pod_count=0)

    ranked = sorted(None, key=_available_headroom, reverse=True)

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


def x_find_redistribution_target__mutmut_13(
    top_consumers: list[TopConsumer], candidate_nodes: list[ClusterNodeSnapshot]
) -> RedistributionResult:
    """Greedy partial-fit simulation — a candidate node absorbing *some* of
    the top consumers (not necessarily all) still counts as feasible, since
    partial redistribution is a real, useful outcome (see ticket TC2)."""
    if not top_consumers or not candidate_nodes:
        return RedistributionResult(feasible=False, target_node=None, moved_pod_count=0)

    ranked = sorted(candidate_nodes, key=None, reverse=True)

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


def x_find_redistribution_target__mutmut_14(
    top_consumers: list[TopConsumer], candidate_nodes: list[ClusterNodeSnapshot]
) -> RedistributionResult:
    """Greedy partial-fit simulation — a candidate node absorbing *some* of
    the top consumers (not necessarily all) still counts as feasible, since
    partial redistribution is a real, useful outcome (see ticket TC2)."""
    if not top_consumers or not candidate_nodes:
        return RedistributionResult(feasible=False, target_node=None, moved_pod_count=0)

    ranked = sorted(candidate_nodes, key=_available_headroom, reverse=None)

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


def x_find_redistribution_target__mutmut_15(
    top_consumers: list[TopConsumer], candidate_nodes: list[ClusterNodeSnapshot]
) -> RedistributionResult:
    """Greedy partial-fit simulation — a candidate node absorbing *some* of
    the top consumers (not necessarily all) still counts as feasible, since
    partial redistribution is a real, useful outcome (see ticket TC2)."""
    if not top_consumers or not candidate_nodes:
        return RedistributionResult(feasible=False, target_node=None, moved_pod_count=0)

    ranked = sorted(key=_available_headroom, reverse=True)

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


def x_find_redistribution_target__mutmut_16(
    top_consumers: list[TopConsumer], candidate_nodes: list[ClusterNodeSnapshot]
) -> RedistributionResult:
    """Greedy partial-fit simulation — a candidate node absorbing *some* of
    the top consumers (not necessarily all) still counts as feasible, since
    partial redistribution is a real, useful outcome (see ticket TC2)."""
    if not top_consumers or not candidate_nodes:
        return RedistributionResult(feasible=False, target_node=None, moved_pod_count=0)

    ranked = sorted(candidate_nodes, reverse=True)

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


def x_find_redistribution_target__mutmut_17(
    top_consumers: list[TopConsumer], candidate_nodes: list[ClusterNodeSnapshot]
) -> RedistributionResult:
    """Greedy partial-fit simulation — a candidate node absorbing *some* of
    the top consumers (not necessarily all) still counts as feasible, since
    partial redistribution is a real, useful outcome (see ticket TC2)."""
    if not top_consumers or not candidate_nodes:
        return RedistributionResult(feasible=False, target_node=None, moved_pod_count=0)

    ranked = sorted(candidate_nodes, key=_available_headroom, )

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


def x_find_redistribution_target__mutmut_18(
    top_consumers: list[TopConsumer], candidate_nodes: list[ClusterNodeSnapshot]
) -> RedistributionResult:
    """Greedy partial-fit simulation — a candidate node absorbing *some* of
    the top consumers (not necessarily all) still counts as feasible, since
    partial redistribution is a real, useful outcome (see ticket TC2)."""
    if not top_consumers or not candidate_nodes:
        return RedistributionResult(feasible=False, target_node=None, moved_pod_count=0)

    ranked = sorted(candidate_nodes, key=_available_headroom, reverse=False)

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


def x_find_redistribution_target__mutmut_19(
    top_consumers: list[TopConsumer], candidate_nodes: list[ClusterNodeSnapshot]
) -> RedistributionResult:
    """Greedy partial-fit simulation — a candidate node absorbing *some* of
    the top consumers (not necessarily all) still counts as feasible, since
    partial redistribution is a real, useful outcome (see ticket TC2)."""
    if not top_consumers or not candidate_nodes:
        return RedistributionResult(feasible=False, target_node=None, moved_pod_count=0)

    ranked = sorted(candidate_nodes, key=_available_headroom, reverse=True)

    best_target: str | None = ""
    best_moved = 0
    for node in ranked:
        moved = _count_fitting(top_consumers, _available_headroom(node))
        if moved > best_moved:
            best_moved = moved
            best_target = node.node_name

    return RedistributionResult(
        feasible=best_moved > 0, target_node=best_target, moved_pod_count=best_moved
    )


def x_find_redistribution_target__mutmut_20(
    top_consumers: list[TopConsumer], candidate_nodes: list[ClusterNodeSnapshot]
) -> RedistributionResult:
    """Greedy partial-fit simulation — a candidate node absorbing *some* of
    the top consumers (not necessarily all) still counts as feasible, since
    partial redistribution is a real, useful outcome (see ticket TC2)."""
    if not top_consumers or not candidate_nodes:
        return RedistributionResult(feasible=False, target_node=None, moved_pod_count=0)

    ranked = sorted(candidate_nodes, key=_available_headroom, reverse=True)

    best_target: str | None = None
    best_moved = None
    for node in ranked:
        moved = _count_fitting(top_consumers, _available_headroom(node))
        if moved > best_moved:
            best_moved = moved
            best_target = node.node_name

    return RedistributionResult(
        feasible=best_moved > 0, target_node=best_target, moved_pod_count=best_moved
    )


def x_find_redistribution_target__mutmut_21(
    top_consumers: list[TopConsumer], candidate_nodes: list[ClusterNodeSnapshot]
) -> RedistributionResult:
    """Greedy partial-fit simulation — a candidate node absorbing *some* of
    the top consumers (not necessarily all) still counts as feasible, since
    partial redistribution is a real, useful outcome (see ticket TC2)."""
    if not top_consumers or not candidate_nodes:
        return RedistributionResult(feasible=False, target_node=None, moved_pod_count=0)

    ranked = sorted(candidate_nodes, key=_available_headroom, reverse=True)

    best_target: str | None = None
    best_moved = 1
    for node in ranked:
        moved = _count_fitting(top_consumers, _available_headroom(node))
        if moved > best_moved:
            best_moved = moved
            best_target = node.node_name

    return RedistributionResult(
        feasible=best_moved > 0, target_node=best_target, moved_pod_count=best_moved
    )


def x_find_redistribution_target__mutmut_22(
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
        moved = None
        if moved > best_moved:
            best_moved = moved
            best_target = node.node_name

    return RedistributionResult(
        feasible=best_moved > 0, target_node=best_target, moved_pod_count=best_moved
    )


def x_find_redistribution_target__mutmut_23(
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
        moved = _count_fitting(None, _available_headroom(node))
        if moved > best_moved:
            best_moved = moved
            best_target = node.node_name

    return RedistributionResult(
        feasible=best_moved > 0, target_node=best_target, moved_pod_count=best_moved
    )


def x_find_redistribution_target__mutmut_24(
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
        moved = _count_fitting(top_consumers, None)
        if moved > best_moved:
            best_moved = moved
            best_target = node.node_name

    return RedistributionResult(
        feasible=best_moved > 0, target_node=best_target, moved_pod_count=best_moved
    )


def x_find_redistribution_target__mutmut_25(
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
        moved = _count_fitting(_available_headroom(node))
        if moved > best_moved:
            best_moved = moved
            best_target = node.node_name

    return RedistributionResult(
        feasible=best_moved > 0, target_node=best_target, moved_pod_count=best_moved
    )


def x_find_redistribution_target__mutmut_26(
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
        moved = _count_fitting(top_consumers, )
        if moved > best_moved:
            best_moved = moved
            best_target = node.node_name

    return RedistributionResult(
        feasible=best_moved > 0, target_node=best_target, moved_pod_count=best_moved
    )


def x_find_redistribution_target__mutmut_27(
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
        moved = _count_fitting(top_consumers, _available_headroom(None))
        if moved > best_moved:
            best_moved = moved
            best_target = node.node_name

    return RedistributionResult(
        feasible=best_moved > 0, target_node=best_target, moved_pod_count=best_moved
    )


def x_find_redistribution_target__mutmut_28(
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
        if moved >= best_moved:
            best_moved = moved
            best_target = node.node_name

    return RedistributionResult(
        feasible=best_moved > 0, target_node=best_target, moved_pod_count=best_moved
    )


def x_find_redistribution_target__mutmut_29(
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
            best_moved = None
            best_target = node.node_name

    return RedistributionResult(
        feasible=best_moved > 0, target_node=best_target, moved_pod_count=best_moved
    )


def x_find_redistribution_target__mutmut_30(
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
            best_target = None

    return RedistributionResult(
        feasible=best_moved > 0, target_node=best_target, moved_pod_count=best_moved
    )


def x_find_redistribution_target__mutmut_31(
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
        feasible=None, target_node=best_target, moved_pod_count=best_moved
    )


def x_find_redistribution_target__mutmut_32(
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
        feasible=best_moved > 0, target_node=None, moved_pod_count=best_moved
    )


def x_find_redistribution_target__mutmut_33(
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
        feasible=best_moved > 0, target_node=best_target, moved_pod_count=None
    )


def x_find_redistribution_target__mutmut_34(
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
        target_node=best_target, moved_pod_count=best_moved
    )


def x_find_redistribution_target__mutmut_35(
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
        feasible=best_moved > 0, moved_pod_count=best_moved
    )


def x_find_redistribution_target__mutmut_36(
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
        feasible=best_moved > 0, target_node=best_target, )


def x_find_redistribution_target__mutmut_37(
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
        feasible=best_moved >= 0, target_node=best_target, moved_pod_count=best_moved
    )


def x_find_redistribution_target__mutmut_38(
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
        feasible=best_moved > 1, target_node=best_target, moved_pod_count=best_moved
    )

mutants_x_find_redistribution_target__mutmut['_mutmut_orig'] = x_find_redistribution_target__mutmut_orig # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_1'] = x_find_redistribution_target__mutmut_1 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_2'] = x_find_redistribution_target__mutmut_2 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_3'] = x_find_redistribution_target__mutmut_3 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_4'] = x_find_redistribution_target__mutmut_4 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_5'] = x_find_redistribution_target__mutmut_5 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_6'] = x_find_redistribution_target__mutmut_6 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_7'] = x_find_redistribution_target__mutmut_7 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_8'] = x_find_redistribution_target__mutmut_8 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_9'] = x_find_redistribution_target__mutmut_9 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_10'] = x_find_redistribution_target__mutmut_10 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_11'] = x_find_redistribution_target__mutmut_11 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_12'] = x_find_redistribution_target__mutmut_12 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_13'] = x_find_redistribution_target__mutmut_13 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_14'] = x_find_redistribution_target__mutmut_14 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_15'] = x_find_redistribution_target__mutmut_15 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_16'] = x_find_redistribution_target__mutmut_16 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_17'] = x_find_redistribution_target__mutmut_17 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_18'] = x_find_redistribution_target__mutmut_18 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_19'] = x_find_redistribution_target__mutmut_19 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_20'] = x_find_redistribution_target__mutmut_20 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_21'] = x_find_redistribution_target__mutmut_21 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_22'] = x_find_redistribution_target__mutmut_22 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_23'] = x_find_redistribution_target__mutmut_23 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_24'] = x_find_redistribution_target__mutmut_24 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_25'] = x_find_redistribution_target__mutmut_25 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_26'] = x_find_redistribution_target__mutmut_26 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_27'] = x_find_redistribution_target__mutmut_27 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_28'] = x_find_redistribution_target__mutmut_28 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_29'] = x_find_redistribution_target__mutmut_29 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_30'] = x_find_redistribution_target__mutmut_30 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_31'] = x_find_redistribution_target__mutmut_31 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_32'] = x_find_redistribution_target__mutmut_32 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_33'] = x_find_redistribution_target__mutmut_33 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_34'] = x_find_redistribution_target__mutmut_34 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_35'] = x_find_redistribution_target__mutmut_35 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_36'] = x_find_redistribution_target__mutmut_36 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_37'] = x_find_redistribution_target__mutmut_37 # type: ignore # mutmut generated
mutants_x_find_redistribution_target__mutmut['x_find_redistribution_target__mutmut_38'] = x_find_redistribution_target__mutmut_38 # type: ignore # mutmut generated
mutants_x__available_headroom__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__available_headroom__mutmut)
def _available_headroom(node: ClusterNodeSnapshot) -> float:
    used = sum(pod.cpu_usage_cores for pod in node.pods)
    return node.allocatable_cpu_cores - used


def x__available_headroom__mutmut_orig(node: ClusterNodeSnapshot) -> float:
    used = sum(pod.cpu_usage_cores for pod in node.pods)
    return node.allocatable_cpu_cores - used


def x__available_headroom__mutmut_1(node: ClusterNodeSnapshot) -> float:
    used = None
    return node.allocatable_cpu_cores - used


def x__available_headroom__mutmut_2(node: ClusterNodeSnapshot) -> float:
    used = sum(None)
    return node.allocatable_cpu_cores - used


def x__available_headroom__mutmut_3(node: ClusterNodeSnapshot) -> float:
    used = sum(pod.cpu_usage_cores for pod in node.pods)
    return node.allocatable_cpu_cores + used

mutants_x__available_headroom__mutmut['_mutmut_orig'] = x__available_headroom__mutmut_orig # type: ignore # mutmut generated
mutants_x__available_headroom__mutmut['x__available_headroom__mutmut_1'] = x__available_headroom__mutmut_1 # type: ignore # mutmut generated
mutants_x__available_headroom__mutmut['x__available_headroom__mutmut_2'] = x__available_headroom__mutmut_2 # type: ignore # mutmut generated
mutants_x__available_headroom__mutmut['x__available_headroom__mutmut_3'] = x__available_headroom__mutmut_3 # type: ignore # mutmut generated
mutants_x__count_fitting__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__count_fitting__mutmut)
def _count_fitting(consumers: list[TopConsumer], available_headroom: float) -> int:
    remaining = available_headroom
    moved = 0
    for consumer in consumers:
        if consumer.cpu_usage_cores <= remaining:
            remaining -= consumer.cpu_usage_cores
            moved += 1
    return moved


def x__count_fitting__mutmut_orig(consumers: list[TopConsumer], available_headroom: float) -> int:
    remaining = available_headroom
    moved = 0
    for consumer in consumers:
        if consumer.cpu_usage_cores <= remaining:
            remaining -= consumer.cpu_usage_cores
            moved += 1
    return moved


def x__count_fitting__mutmut_1(consumers: list[TopConsumer], available_headroom: float) -> int:
    remaining = None
    moved = 0
    for consumer in consumers:
        if consumer.cpu_usage_cores <= remaining:
            remaining -= consumer.cpu_usage_cores
            moved += 1
    return moved


def x__count_fitting__mutmut_2(consumers: list[TopConsumer], available_headroom: float) -> int:
    remaining = available_headroom
    moved = None
    for consumer in consumers:
        if consumer.cpu_usage_cores <= remaining:
            remaining -= consumer.cpu_usage_cores
            moved += 1
    return moved


def x__count_fitting__mutmut_3(consumers: list[TopConsumer], available_headroom: float) -> int:
    remaining = available_headroom
    moved = 1
    for consumer in consumers:
        if consumer.cpu_usage_cores <= remaining:
            remaining -= consumer.cpu_usage_cores
            moved += 1
    return moved


def x__count_fitting__mutmut_4(consumers: list[TopConsumer], available_headroom: float) -> int:
    remaining = available_headroom
    moved = 0
    for consumer in consumers:
        if consumer.cpu_usage_cores < remaining:
            remaining -= consumer.cpu_usage_cores
            moved += 1
    return moved


def x__count_fitting__mutmut_5(consumers: list[TopConsumer], available_headroom: float) -> int:
    remaining = available_headroom
    moved = 0
    for consumer in consumers:
        if consumer.cpu_usage_cores <= remaining:
            remaining = consumer.cpu_usage_cores
            moved += 1
    return moved


def x__count_fitting__mutmut_6(consumers: list[TopConsumer], available_headroom: float) -> int:
    remaining = available_headroom
    moved = 0
    for consumer in consumers:
        if consumer.cpu_usage_cores <= remaining:
            remaining += consumer.cpu_usage_cores
            moved += 1
    return moved


def x__count_fitting__mutmut_7(consumers: list[TopConsumer], available_headroom: float) -> int:
    remaining = available_headroom
    moved = 0
    for consumer in consumers:
        if consumer.cpu_usage_cores <= remaining:
            remaining -= consumer.cpu_usage_cores
            moved = 1
    return moved


def x__count_fitting__mutmut_8(consumers: list[TopConsumer], available_headroom: float) -> int:
    remaining = available_headroom
    moved = 0
    for consumer in consumers:
        if consumer.cpu_usage_cores <= remaining:
            remaining -= consumer.cpu_usage_cores
            moved -= 1
    return moved


def x__count_fitting__mutmut_9(consumers: list[TopConsumer], available_headroom: float) -> int:
    remaining = available_headroom
    moved = 0
    for consumer in consumers:
        if consumer.cpu_usage_cores <= remaining:
            remaining -= consumer.cpu_usage_cores
            moved += 2
    return moved

mutants_x__count_fitting__mutmut['_mutmut_orig'] = x__count_fitting__mutmut_orig # type: ignore # mutmut generated
mutants_x__count_fitting__mutmut['x__count_fitting__mutmut_1'] = x__count_fitting__mutmut_1 # type: ignore # mutmut generated
mutants_x__count_fitting__mutmut['x__count_fitting__mutmut_2'] = x__count_fitting__mutmut_2 # type: ignore # mutmut generated
mutants_x__count_fitting__mutmut['x__count_fitting__mutmut_3'] = x__count_fitting__mutmut_3 # type: ignore # mutmut generated
mutants_x__count_fitting__mutmut['x__count_fitting__mutmut_4'] = x__count_fitting__mutmut_4 # type: ignore # mutmut generated
mutants_x__count_fitting__mutmut['x__count_fitting__mutmut_5'] = x__count_fitting__mutmut_5 # type: ignore # mutmut generated
mutants_x__count_fitting__mutmut['x__count_fitting__mutmut_6'] = x__count_fitting__mutmut_6 # type: ignore # mutmut generated
mutants_x__count_fitting__mutmut['x__count_fitting__mutmut_7'] = x__count_fitting__mutmut_7 # type: ignore # mutmut generated
mutants_x__count_fitting__mutmut['x__count_fitting__mutmut_8'] = x__count_fitting__mutmut_8 # type: ignore # mutmut generated
mutants_x__count_fitting__mutmut['x__count_fitting__mutmut_9'] = x__count_fitting__mutmut_9 # type: ignore # mutmut generated
