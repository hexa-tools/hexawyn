from __future__ import annotations

import math

from hexawyn.domain.models.constants import HeadroomSimulationConstants
from hexawyn.domain.models.headroom_simulation import (
    BindingConstraint,
    ClusterHeadroomSnapshot,
    HeadroomSimulationReport,
    HeadroomSimulationRequest,
    HeadroomVerdict,
    ProposedWorkload,
)
from hexawyn.domain.services.headroom_simulation.workload_sizing import (
    compute_total_workload_needs,
    find_unschedulable_workloads,
)

_cfg = HeadroomSimulationConstants()


def simulate_headroom(
    request: HeadroomSimulationRequest, snapshot: ClusterHeadroomSnapshot
) -> HeadroomSimulationReport:
    total_new_cpu, total_new_memory = compute_total_workload_needs(request.proposed_workloads)
    unschedulable = find_unschedulable_workloads(
        request.proposed_workloads, snapshot.largest_node_cpu_cores, snapshot.largest_node_memory_gb
    )

    current_cpu_pct = _utilization_percent(
        snapshot.used_cpu_cores, snapshot.total_allocatable_cpu_cores
    )
    current_memory_pct = _utilization_percent(
        snapshot.used_memory_gb, snapshot.total_allocatable_memory_gb
    )

    post_cpu_used = snapshot.used_cpu_cores + total_new_cpu
    post_memory_used = snapshot.used_memory_gb + total_new_memory
    post_cpu_pct = _utilization_percent(post_cpu_used, snapshot.total_allocatable_cpu_cores)
    post_memory_pct = _utilization_percent(post_memory_used, snapshot.total_allocatable_memory_gb)

    verdict = _determine_verdict(post_cpu_pct, post_memory_pct, bool(unschedulable))
    binding_constraint = _binding_constraint(
        request.proposed_workloads, post_cpu_pct, post_memory_pct
    )

    recommended_nodes = 0
    if verdict == "needs_nodes":
        recommended_nodes = _recommend_additional_nodes(post_cpu_used, post_memory_used, snapshot)

    summary = _build_summary(
        has_workloads=bool(request.proposed_workloads),
        verdict=verdict,
        binding_constraint=binding_constraint,
        post_cpu_pct=post_cpu_pct,
        post_memory_pct=post_memory_pct,
        recommended_nodes=recommended_nodes,
        autoscaler_enabled=snapshot.autoscaler_enabled,
        unschedulable=unschedulable,
    )

    return HeadroomSimulationReport(
        current_cpu_utilization_percent=round(current_cpu_pct, 2),
        current_memory_utilization_percent=round(current_memory_pct, 2),
        total_new_cpu_cores=total_new_cpu,
        total_new_memory_gb=total_new_memory,
        post_cpu_utilization_percent=round(post_cpu_pct, 2),
        post_memory_utilization_percent=round(post_memory_pct, 2),
        binding_constraint=binding_constraint,
        verdict=verdict,
        recommended_additional_nodes=recommended_nodes,
        autoscaler_enabled=snapshot.autoscaler_enabled,
        unschedulable_workloads=unschedulable,
        summary=summary,
    )


def _utilization_percent(used: float, total: float) -> float:
    return used / total * 100 if total > 0 else 0.0


def _determine_verdict(
    post_cpu_pct: float, post_memory_pct: float, has_unschedulable: bool
) -> HeadroomVerdict:
    if has_unschedulable:
        return "needs_nodes"
    worst = max(post_cpu_pct, post_memory_pct)
    if worst >= _cfg.needs_nodes_utilization_threshold:
        return "needs_nodes"
    if worst >= _cfg.tight_utilization_threshold:
        return "tight"
    return "fits"


def _binding_constraint(
    workloads: list[ProposedWorkload], post_cpu_pct: float, post_memory_pct: float
) -> BindingConstraint:
    if not workloads:
        return "None"
    return "CPU" if post_cpu_pct >= post_memory_pct else "Memory"


def _recommend_additional_nodes(
    post_cpu_used: float, post_memory_used: float, snapshot: ClusterHeadroomSnapshot
) -> int:
    target_fraction = _cfg.target_utilization_after_scaling_percent / 100
    target_cpu = target_fraction * snapshot.total_allocatable_cpu_cores
    target_memory = target_fraction * snapshot.total_allocatable_memory_gb

    avg_node_cpu = (
        snapshot.total_allocatable_cpu_cores / snapshot.node_count if snapshot.node_count > 0 else 0
    )
    avg_node_memory = (
        snapshot.total_allocatable_memory_gb / snapshot.node_count if snapshot.node_count > 0 else 0
    )

    nodes_for_cpu = (
        math.ceil((post_cpu_used - target_cpu) / avg_node_cpu)
        if avg_node_cpu > 0 and post_cpu_used > target_cpu
        else 0
    )
    nodes_for_memory = (
        math.ceil((post_memory_used - target_memory) / avg_node_memory)
        if avg_node_memory > 0 and post_memory_used > target_memory
        else 0
    )
    return max(nodes_for_cpu, nodes_for_memory, 1)


def _build_summary(
    has_workloads: bool,
    verdict: HeadroomVerdict,
    binding_constraint: BindingConstraint,
    post_cpu_pct: float,
    post_memory_pct: float,
    recommended_nodes: int,
    autoscaler_enabled: bool,
    unschedulable: list[str],
) -> str:
    if not has_workloads:
        base = "No new workloads proposed — current headroom shown."
    elif unschedulable:
        base = (
            f"Unschedulable: {', '.join(unschedulable)} — request(s) exceed the largest "
            "available node; a larger node type is needed, not just more of the current size."
        )
    elif verdict == "needs_nodes":
        worst = max(post_cpu_pct, post_memory_pct)
        base = (
            f"Needs nodes — projected utilization would reach {worst:.1f}%. "
            f"Recommend adding {recommended_nodes} node(s)."
        )
    elif verdict == "tight":
        worst = max(post_cpu_pct, post_memory_pct)
        base = f"Tight — projected utilization would reach {worst:.1f}%. Monitor closely."
    else:
        base = "Fits comfortably within current cluster capacity."

    if has_workloads and binding_constraint != "None" and verdict != "fits":
        base += f" {binding_constraint} is the binding constraint."
    if autoscaler_enabled:
        base += " Cluster autoscaler is enabled as a safety net."
    return base
