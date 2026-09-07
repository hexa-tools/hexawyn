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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_simulate_headroom__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_simulate_headroom__mutmut)
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


def x_simulate_headroom__mutmut_orig(
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


def x_simulate_headroom__mutmut_1(
    request: HeadroomSimulationRequest, snapshot: ClusterHeadroomSnapshot
) -> HeadroomSimulationReport:
    total_new_cpu, total_new_memory = None
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


def x_simulate_headroom__mutmut_2(
    request: HeadroomSimulationRequest, snapshot: ClusterHeadroomSnapshot
) -> HeadroomSimulationReport:
    total_new_cpu, total_new_memory = compute_total_workload_needs(None)
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


def x_simulate_headroom__mutmut_3(
    request: HeadroomSimulationRequest, snapshot: ClusterHeadroomSnapshot
) -> HeadroomSimulationReport:
    total_new_cpu, total_new_memory = compute_total_workload_needs(request.proposed_workloads)
    unschedulable = None

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


def x_simulate_headroom__mutmut_4(
    request: HeadroomSimulationRequest, snapshot: ClusterHeadroomSnapshot
) -> HeadroomSimulationReport:
    total_new_cpu, total_new_memory = compute_total_workload_needs(request.proposed_workloads)
    unschedulable = find_unschedulable_workloads(
        None, snapshot.largest_node_cpu_cores, snapshot.largest_node_memory_gb
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


def x_simulate_headroom__mutmut_5(
    request: HeadroomSimulationRequest, snapshot: ClusterHeadroomSnapshot
) -> HeadroomSimulationReport:
    total_new_cpu, total_new_memory = compute_total_workload_needs(request.proposed_workloads)
    unschedulable = find_unschedulable_workloads(
        request.proposed_workloads, None, snapshot.largest_node_memory_gb
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


def x_simulate_headroom__mutmut_6(
    request: HeadroomSimulationRequest, snapshot: ClusterHeadroomSnapshot
) -> HeadroomSimulationReport:
    total_new_cpu, total_new_memory = compute_total_workload_needs(request.proposed_workloads)
    unschedulable = find_unschedulable_workloads(
        request.proposed_workloads, snapshot.largest_node_cpu_cores, None
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


def x_simulate_headroom__mutmut_7(
    request: HeadroomSimulationRequest, snapshot: ClusterHeadroomSnapshot
) -> HeadroomSimulationReport:
    total_new_cpu, total_new_memory = compute_total_workload_needs(request.proposed_workloads)
    unschedulable = find_unschedulable_workloads(
        snapshot.largest_node_cpu_cores, snapshot.largest_node_memory_gb
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


def x_simulate_headroom__mutmut_8(
    request: HeadroomSimulationRequest, snapshot: ClusterHeadroomSnapshot
) -> HeadroomSimulationReport:
    total_new_cpu, total_new_memory = compute_total_workload_needs(request.proposed_workloads)
    unschedulable = find_unschedulable_workloads(
        request.proposed_workloads, snapshot.largest_node_memory_gb
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


def x_simulate_headroom__mutmut_9(
    request: HeadroomSimulationRequest, snapshot: ClusterHeadroomSnapshot
) -> HeadroomSimulationReport:
    total_new_cpu, total_new_memory = compute_total_workload_needs(request.proposed_workloads)
    unschedulable = find_unschedulable_workloads(
        request.proposed_workloads, snapshot.largest_node_cpu_cores, )

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


def x_simulate_headroom__mutmut_10(
    request: HeadroomSimulationRequest, snapshot: ClusterHeadroomSnapshot
) -> HeadroomSimulationReport:
    total_new_cpu, total_new_memory = compute_total_workload_needs(request.proposed_workloads)
    unschedulable = find_unschedulable_workloads(
        request.proposed_workloads, snapshot.largest_node_cpu_cores, snapshot.largest_node_memory_gb
    )

    current_cpu_pct = None
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


def x_simulate_headroom__mutmut_11(
    request: HeadroomSimulationRequest, snapshot: ClusterHeadroomSnapshot
) -> HeadroomSimulationReport:
    total_new_cpu, total_new_memory = compute_total_workload_needs(request.proposed_workloads)
    unschedulable = find_unschedulable_workloads(
        request.proposed_workloads, snapshot.largest_node_cpu_cores, snapshot.largest_node_memory_gb
    )

    current_cpu_pct = _utilization_percent(
        None, snapshot.total_allocatable_cpu_cores
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


def x_simulate_headroom__mutmut_12(
    request: HeadroomSimulationRequest, snapshot: ClusterHeadroomSnapshot
) -> HeadroomSimulationReport:
    total_new_cpu, total_new_memory = compute_total_workload_needs(request.proposed_workloads)
    unschedulable = find_unschedulable_workloads(
        request.proposed_workloads, snapshot.largest_node_cpu_cores, snapshot.largest_node_memory_gb
    )

    current_cpu_pct = _utilization_percent(
        snapshot.used_cpu_cores, None
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


def x_simulate_headroom__mutmut_13(
    request: HeadroomSimulationRequest, snapshot: ClusterHeadroomSnapshot
) -> HeadroomSimulationReport:
    total_new_cpu, total_new_memory = compute_total_workload_needs(request.proposed_workloads)
    unschedulable = find_unschedulable_workloads(
        request.proposed_workloads, snapshot.largest_node_cpu_cores, snapshot.largest_node_memory_gb
    )

    current_cpu_pct = _utilization_percent(
        snapshot.total_allocatable_cpu_cores
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


def x_simulate_headroom__mutmut_14(
    request: HeadroomSimulationRequest, snapshot: ClusterHeadroomSnapshot
) -> HeadroomSimulationReport:
    total_new_cpu, total_new_memory = compute_total_workload_needs(request.proposed_workloads)
    unschedulable = find_unschedulable_workloads(
        request.proposed_workloads, snapshot.largest_node_cpu_cores, snapshot.largest_node_memory_gb
    )

    current_cpu_pct = _utilization_percent(
        snapshot.used_cpu_cores, )
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


def x_simulate_headroom__mutmut_15(
    request: HeadroomSimulationRequest, snapshot: ClusterHeadroomSnapshot
) -> HeadroomSimulationReport:
    total_new_cpu, total_new_memory = compute_total_workload_needs(request.proposed_workloads)
    unschedulable = find_unschedulable_workloads(
        request.proposed_workloads, snapshot.largest_node_cpu_cores, snapshot.largest_node_memory_gb
    )

    current_cpu_pct = _utilization_percent(
        snapshot.used_cpu_cores, snapshot.total_allocatable_cpu_cores
    )
    current_memory_pct = None

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


def x_simulate_headroom__mutmut_16(
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
        None, snapshot.total_allocatable_memory_gb
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


def x_simulate_headroom__mutmut_17(
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
        snapshot.used_memory_gb, None
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


def x_simulate_headroom__mutmut_18(
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
        snapshot.total_allocatable_memory_gb
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


def x_simulate_headroom__mutmut_19(
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
        snapshot.used_memory_gb, )

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


def x_simulate_headroom__mutmut_20(
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

    post_cpu_used = None
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


def x_simulate_headroom__mutmut_21(
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

    post_cpu_used = snapshot.used_cpu_cores - total_new_cpu
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


def x_simulate_headroom__mutmut_22(
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
    post_memory_used = None
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


def x_simulate_headroom__mutmut_23(
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
    post_memory_used = snapshot.used_memory_gb - total_new_memory
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


def x_simulate_headroom__mutmut_24(
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
    post_cpu_pct = None
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


def x_simulate_headroom__mutmut_25(
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
    post_cpu_pct = _utilization_percent(None, snapshot.total_allocatable_cpu_cores)
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


def x_simulate_headroom__mutmut_26(
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
    post_cpu_pct = _utilization_percent(post_cpu_used, None)
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


def x_simulate_headroom__mutmut_27(
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
    post_cpu_pct = _utilization_percent(snapshot.total_allocatable_cpu_cores)
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


def x_simulate_headroom__mutmut_28(
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
    post_cpu_pct = _utilization_percent(post_cpu_used, )
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


def x_simulate_headroom__mutmut_29(
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
    post_memory_pct = None

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


def x_simulate_headroom__mutmut_30(
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
    post_memory_pct = _utilization_percent(None, snapshot.total_allocatable_memory_gb)

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


def x_simulate_headroom__mutmut_31(
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
    post_memory_pct = _utilization_percent(post_memory_used, None)

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


def x_simulate_headroom__mutmut_32(
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
    post_memory_pct = _utilization_percent(snapshot.total_allocatable_memory_gb)

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


def x_simulate_headroom__mutmut_33(
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
    post_memory_pct = _utilization_percent(post_memory_used, )

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


def x_simulate_headroom__mutmut_34(
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

    verdict = None
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


def x_simulate_headroom__mutmut_35(
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

    verdict = _determine_verdict(None, post_memory_pct, bool(unschedulable))
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


def x_simulate_headroom__mutmut_36(
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

    verdict = _determine_verdict(post_cpu_pct, None, bool(unschedulable))
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


def x_simulate_headroom__mutmut_37(
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

    verdict = _determine_verdict(post_cpu_pct, post_memory_pct, None)
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


def x_simulate_headroom__mutmut_38(
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

    verdict = _determine_verdict(post_memory_pct, bool(unschedulable))
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


def x_simulate_headroom__mutmut_39(
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

    verdict = _determine_verdict(post_cpu_pct, bool(unschedulable))
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


def x_simulate_headroom__mutmut_40(
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

    verdict = _determine_verdict(post_cpu_pct, post_memory_pct, )
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


def x_simulate_headroom__mutmut_41(
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

    verdict = _determine_verdict(post_cpu_pct, post_memory_pct, bool(None))
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


def x_simulate_headroom__mutmut_42(
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
    binding_constraint = None

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


def x_simulate_headroom__mutmut_43(
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
        None, post_cpu_pct, post_memory_pct
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


def x_simulate_headroom__mutmut_44(
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
        request.proposed_workloads, None, post_memory_pct
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


def x_simulate_headroom__mutmut_45(
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
        request.proposed_workloads, post_cpu_pct, None
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


def x_simulate_headroom__mutmut_46(
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
        post_cpu_pct, post_memory_pct
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


def x_simulate_headroom__mutmut_47(
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
        request.proposed_workloads, post_memory_pct
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


def x_simulate_headroom__mutmut_48(
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
        request.proposed_workloads, post_cpu_pct, )

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


def x_simulate_headroom__mutmut_49(
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

    recommended_nodes = None
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


def x_simulate_headroom__mutmut_50(
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

    recommended_nodes = 1
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


def x_simulate_headroom__mutmut_51(
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
    if verdict != "needs_nodes":
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


def x_simulate_headroom__mutmut_52(
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
    if verdict == "XXneeds_nodesXX":
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


def x_simulate_headroom__mutmut_53(
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
    if verdict == "NEEDS_NODES":
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


def x_simulate_headroom__mutmut_54(
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
        recommended_nodes = None

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


def x_simulate_headroom__mutmut_55(
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
        recommended_nodes = _recommend_additional_nodes(None, post_memory_used, snapshot)

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


def x_simulate_headroom__mutmut_56(
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
        recommended_nodes = _recommend_additional_nodes(post_cpu_used, None, snapshot)

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


def x_simulate_headroom__mutmut_57(
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
        recommended_nodes = _recommend_additional_nodes(post_cpu_used, post_memory_used, None)

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


def x_simulate_headroom__mutmut_58(
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
        recommended_nodes = _recommend_additional_nodes(post_memory_used, snapshot)

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


def x_simulate_headroom__mutmut_59(
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
        recommended_nodes = _recommend_additional_nodes(post_cpu_used, snapshot)

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


def x_simulate_headroom__mutmut_60(
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
        recommended_nodes = _recommend_additional_nodes(post_cpu_used, post_memory_used, )

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


def x_simulate_headroom__mutmut_61(
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

    summary = None

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


def x_simulate_headroom__mutmut_62(
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
        has_workloads=None,
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


def x_simulate_headroom__mutmut_63(
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
        verdict=None,
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


def x_simulate_headroom__mutmut_64(
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
        binding_constraint=None,
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


def x_simulate_headroom__mutmut_65(
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
        post_cpu_pct=None,
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


def x_simulate_headroom__mutmut_66(
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
        post_memory_pct=None,
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


def x_simulate_headroom__mutmut_67(
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
        recommended_nodes=None,
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


def x_simulate_headroom__mutmut_68(
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
        autoscaler_enabled=None,
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


def x_simulate_headroom__mutmut_69(
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
        unschedulable=None,
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


def x_simulate_headroom__mutmut_70(
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


def x_simulate_headroom__mutmut_71(
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


def x_simulate_headroom__mutmut_72(
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


def x_simulate_headroom__mutmut_73(
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


def x_simulate_headroom__mutmut_74(
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


def x_simulate_headroom__mutmut_75(
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


def x_simulate_headroom__mutmut_76(
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


def x_simulate_headroom__mutmut_77(
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


def x_simulate_headroom__mutmut_78(
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
        has_workloads=bool(None),
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


def x_simulate_headroom__mutmut_79(
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
        current_cpu_utilization_percent=None,
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


def x_simulate_headroom__mutmut_80(
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
        current_memory_utilization_percent=None,
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


def x_simulate_headroom__mutmut_81(
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
        total_new_cpu_cores=None,
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


def x_simulate_headroom__mutmut_82(
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
        total_new_memory_gb=None,
        post_cpu_utilization_percent=round(post_cpu_pct, 2),
        post_memory_utilization_percent=round(post_memory_pct, 2),
        binding_constraint=binding_constraint,
        verdict=verdict,
        recommended_additional_nodes=recommended_nodes,
        autoscaler_enabled=snapshot.autoscaler_enabled,
        unschedulable_workloads=unschedulable,
        summary=summary,
    )


def x_simulate_headroom__mutmut_83(
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
        post_cpu_utilization_percent=None,
        post_memory_utilization_percent=round(post_memory_pct, 2),
        binding_constraint=binding_constraint,
        verdict=verdict,
        recommended_additional_nodes=recommended_nodes,
        autoscaler_enabled=snapshot.autoscaler_enabled,
        unschedulable_workloads=unschedulable,
        summary=summary,
    )


def x_simulate_headroom__mutmut_84(
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
        post_memory_utilization_percent=None,
        binding_constraint=binding_constraint,
        verdict=verdict,
        recommended_additional_nodes=recommended_nodes,
        autoscaler_enabled=snapshot.autoscaler_enabled,
        unschedulable_workloads=unschedulable,
        summary=summary,
    )


def x_simulate_headroom__mutmut_85(
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
        binding_constraint=None,
        verdict=verdict,
        recommended_additional_nodes=recommended_nodes,
        autoscaler_enabled=snapshot.autoscaler_enabled,
        unschedulable_workloads=unschedulable,
        summary=summary,
    )


def x_simulate_headroom__mutmut_86(
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
        verdict=None,
        recommended_additional_nodes=recommended_nodes,
        autoscaler_enabled=snapshot.autoscaler_enabled,
        unschedulable_workloads=unschedulable,
        summary=summary,
    )


def x_simulate_headroom__mutmut_87(
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
        recommended_additional_nodes=None,
        autoscaler_enabled=snapshot.autoscaler_enabled,
        unschedulable_workloads=unschedulable,
        summary=summary,
    )


def x_simulate_headroom__mutmut_88(
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
        autoscaler_enabled=None,
        unschedulable_workloads=unschedulable,
        summary=summary,
    )


def x_simulate_headroom__mutmut_89(
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
        unschedulable_workloads=None,
        summary=summary,
    )


def x_simulate_headroom__mutmut_90(
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
        summary=None,
    )


def x_simulate_headroom__mutmut_91(
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


def x_simulate_headroom__mutmut_92(
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


def x_simulate_headroom__mutmut_93(
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


def x_simulate_headroom__mutmut_94(
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
        post_cpu_utilization_percent=round(post_cpu_pct, 2),
        post_memory_utilization_percent=round(post_memory_pct, 2),
        binding_constraint=binding_constraint,
        verdict=verdict,
        recommended_additional_nodes=recommended_nodes,
        autoscaler_enabled=snapshot.autoscaler_enabled,
        unschedulable_workloads=unschedulable,
        summary=summary,
    )


def x_simulate_headroom__mutmut_95(
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
        post_memory_utilization_percent=round(post_memory_pct, 2),
        binding_constraint=binding_constraint,
        verdict=verdict,
        recommended_additional_nodes=recommended_nodes,
        autoscaler_enabled=snapshot.autoscaler_enabled,
        unschedulable_workloads=unschedulable,
        summary=summary,
    )


def x_simulate_headroom__mutmut_96(
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
        binding_constraint=binding_constraint,
        verdict=verdict,
        recommended_additional_nodes=recommended_nodes,
        autoscaler_enabled=snapshot.autoscaler_enabled,
        unschedulable_workloads=unschedulable,
        summary=summary,
    )


def x_simulate_headroom__mutmut_97(
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
        verdict=verdict,
        recommended_additional_nodes=recommended_nodes,
        autoscaler_enabled=snapshot.autoscaler_enabled,
        unschedulable_workloads=unschedulable,
        summary=summary,
    )


def x_simulate_headroom__mutmut_98(
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
        recommended_additional_nodes=recommended_nodes,
        autoscaler_enabled=snapshot.autoscaler_enabled,
        unschedulable_workloads=unschedulable,
        summary=summary,
    )


def x_simulate_headroom__mutmut_99(
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
        autoscaler_enabled=snapshot.autoscaler_enabled,
        unschedulable_workloads=unschedulable,
        summary=summary,
    )


def x_simulate_headroom__mutmut_100(
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
        unschedulable_workloads=unschedulable,
        summary=summary,
    )


def x_simulate_headroom__mutmut_101(
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
        summary=summary,
    )


def x_simulate_headroom__mutmut_102(
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
        )


def x_simulate_headroom__mutmut_103(
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
        current_cpu_utilization_percent=round(None, 2),
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


def x_simulate_headroom__mutmut_104(
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
        current_cpu_utilization_percent=round(current_cpu_pct, None),
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


def x_simulate_headroom__mutmut_105(
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
        current_cpu_utilization_percent=round(2),
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


def x_simulate_headroom__mutmut_106(
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
        current_cpu_utilization_percent=round(current_cpu_pct, ),
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


def x_simulate_headroom__mutmut_107(
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
        current_cpu_utilization_percent=round(current_cpu_pct, 3),
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


def x_simulate_headroom__mutmut_108(
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
        current_memory_utilization_percent=round(None, 2),
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


def x_simulate_headroom__mutmut_109(
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
        current_memory_utilization_percent=round(current_memory_pct, None),
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


def x_simulate_headroom__mutmut_110(
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
        current_memory_utilization_percent=round(2),
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


def x_simulate_headroom__mutmut_111(
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
        current_memory_utilization_percent=round(current_memory_pct, ),
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


def x_simulate_headroom__mutmut_112(
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
        current_memory_utilization_percent=round(current_memory_pct, 3),
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


def x_simulate_headroom__mutmut_113(
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
        post_cpu_utilization_percent=round(None, 2),
        post_memory_utilization_percent=round(post_memory_pct, 2),
        binding_constraint=binding_constraint,
        verdict=verdict,
        recommended_additional_nodes=recommended_nodes,
        autoscaler_enabled=snapshot.autoscaler_enabled,
        unschedulable_workloads=unschedulable,
        summary=summary,
    )


def x_simulate_headroom__mutmut_114(
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
        post_cpu_utilization_percent=round(post_cpu_pct, None),
        post_memory_utilization_percent=round(post_memory_pct, 2),
        binding_constraint=binding_constraint,
        verdict=verdict,
        recommended_additional_nodes=recommended_nodes,
        autoscaler_enabled=snapshot.autoscaler_enabled,
        unschedulable_workloads=unschedulable,
        summary=summary,
    )


def x_simulate_headroom__mutmut_115(
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
        post_cpu_utilization_percent=round(2),
        post_memory_utilization_percent=round(post_memory_pct, 2),
        binding_constraint=binding_constraint,
        verdict=verdict,
        recommended_additional_nodes=recommended_nodes,
        autoscaler_enabled=snapshot.autoscaler_enabled,
        unschedulable_workloads=unschedulable,
        summary=summary,
    )


def x_simulate_headroom__mutmut_116(
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
        post_cpu_utilization_percent=round(post_cpu_pct, ),
        post_memory_utilization_percent=round(post_memory_pct, 2),
        binding_constraint=binding_constraint,
        verdict=verdict,
        recommended_additional_nodes=recommended_nodes,
        autoscaler_enabled=snapshot.autoscaler_enabled,
        unschedulable_workloads=unschedulable,
        summary=summary,
    )


def x_simulate_headroom__mutmut_117(
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
        post_cpu_utilization_percent=round(post_cpu_pct, 3),
        post_memory_utilization_percent=round(post_memory_pct, 2),
        binding_constraint=binding_constraint,
        verdict=verdict,
        recommended_additional_nodes=recommended_nodes,
        autoscaler_enabled=snapshot.autoscaler_enabled,
        unschedulable_workloads=unschedulable,
        summary=summary,
    )


def x_simulate_headroom__mutmut_118(
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
        post_memory_utilization_percent=round(None, 2),
        binding_constraint=binding_constraint,
        verdict=verdict,
        recommended_additional_nodes=recommended_nodes,
        autoscaler_enabled=snapshot.autoscaler_enabled,
        unschedulable_workloads=unschedulable,
        summary=summary,
    )


def x_simulate_headroom__mutmut_119(
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
        post_memory_utilization_percent=round(post_memory_pct, None),
        binding_constraint=binding_constraint,
        verdict=verdict,
        recommended_additional_nodes=recommended_nodes,
        autoscaler_enabled=snapshot.autoscaler_enabled,
        unschedulable_workloads=unschedulable,
        summary=summary,
    )


def x_simulate_headroom__mutmut_120(
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
        post_memory_utilization_percent=round(2),
        binding_constraint=binding_constraint,
        verdict=verdict,
        recommended_additional_nodes=recommended_nodes,
        autoscaler_enabled=snapshot.autoscaler_enabled,
        unschedulable_workloads=unschedulable,
        summary=summary,
    )


def x_simulate_headroom__mutmut_121(
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
        post_memory_utilization_percent=round(post_memory_pct, ),
        binding_constraint=binding_constraint,
        verdict=verdict,
        recommended_additional_nodes=recommended_nodes,
        autoscaler_enabled=snapshot.autoscaler_enabled,
        unschedulable_workloads=unschedulable,
        summary=summary,
    )


def x_simulate_headroom__mutmut_122(
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
        post_memory_utilization_percent=round(post_memory_pct, 3),
        binding_constraint=binding_constraint,
        verdict=verdict,
        recommended_additional_nodes=recommended_nodes,
        autoscaler_enabled=snapshot.autoscaler_enabled,
        unschedulable_workloads=unschedulable,
        summary=summary,
    )

mutants_x_simulate_headroom__mutmut['_mutmut_orig'] = x_simulate_headroom__mutmut_orig # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_1'] = x_simulate_headroom__mutmut_1 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_2'] = x_simulate_headroom__mutmut_2 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_3'] = x_simulate_headroom__mutmut_3 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_4'] = x_simulate_headroom__mutmut_4 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_5'] = x_simulate_headroom__mutmut_5 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_6'] = x_simulate_headroom__mutmut_6 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_7'] = x_simulate_headroom__mutmut_7 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_8'] = x_simulate_headroom__mutmut_8 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_9'] = x_simulate_headroom__mutmut_9 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_10'] = x_simulate_headroom__mutmut_10 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_11'] = x_simulate_headroom__mutmut_11 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_12'] = x_simulate_headroom__mutmut_12 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_13'] = x_simulate_headroom__mutmut_13 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_14'] = x_simulate_headroom__mutmut_14 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_15'] = x_simulate_headroom__mutmut_15 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_16'] = x_simulate_headroom__mutmut_16 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_17'] = x_simulate_headroom__mutmut_17 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_18'] = x_simulate_headroom__mutmut_18 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_19'] = x_simulate_headroom__mutmut_19 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_20'] = x_simulate_headroom__mutmut_20 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_21'] = x_simulate_headroom__mutmut_21 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_22'] = x_simulate_headroom__mutmut_22 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_23'] = x_simulate_headroom__mutmut_23 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_24'] = x_simulate_headroom__mutmut_24 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_25'] = x_simulate_headroom__mutmut_25 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_26'] = x_simulate_headroom__mutmut_26 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_27'] = x_simulate_headroom__mutmut_27 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_28'] = x_simulate_headroom__mutmut_28 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_29'] = x_simulate_headroom__mutmut_29 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_30'] = x_simulate_headroom__mutmut_30 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_31'] = x_simulate_headroom__mutmut_31 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_32'] = x_simulate_headroom__mutmut_32 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_33'] = x_simulate_headroom__mutmut_33 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_34'] = x_simulate_headroom__mutmut_34 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_35'] = x_simulate_headroom__mutmut_35 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_36'] = x_simulate_headroom__mutmut_36 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_37'] = x_simulate_headroom__mutmut_37 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_38'] = x_simulate_headroom__mutmut_38 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_39'] = x_simulate_headroom__mutmut_39 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_40'] = x_simulate_headroom__mutmut_40 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_41'] = x_simulate_headroom__mutmut_41 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_42'] = x_simulate_headroom__mutmut_42 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_43'] = x_simulate_headroom__mutmut_43 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_44'] = x_simulate_headroom__mutmut_44 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_45'] = x_simulate_headroom__mutmut_45 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_46'] = x_simulate_headroom__mutmut_46 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_47'] = x_simulate_headroom__mutmut_47 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_48'] = x_simulate_headroom__mutmut_48 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_49'] = x_simulate_headroom__mutmut_49 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_50'] = x_simulate_headroom__mutmut_50 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_51'] = x_simulate_headroom__mutmut_51 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_52'] = x_simulate_headroom__mutmut_52 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_53'] = x_simulate_headroom__mutmut_53 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_54'] = x_simulate_headroom__mutmut_54 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_55'] = x_simulate_headroom__mutmut_55 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_56'] = x_simulate_headroom__mutmut_56 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_57'] = x_simulate_headroom__mutmut_57 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_58'] = x_simulate_headroom__mutmut_58 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_59'] = x_simulate_headroom__mutmut_59 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_60'] = x_simulate_headroom__mutmut_60 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_61'] = x_simulate_headroom__mutmut_61 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_62'] = x_simulate_headroom__mutmut_62 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_63'] = x_simulate_headroom__mutmut_63 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_64'] = x_simulate_headroom__mutmut_64 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_65'] = x_simulate_headroom__mutmut_65 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_66'] = x_simulate_headroom__mutmut_66 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_67'] = x_simulate_headroom__mutmut_67 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_68'] = x_simulate_headroom__mutmut_68 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_69'] = x_simulate_headroom__mutmut_69 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_70'] = x_simulate_headroom__mutmut_70 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_71'] = x_simulate_headroom__mutmut_71 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_72'] = x_simulate_headroom__mutmut_72 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_73'] = x_simulate_headroom__mutmut_73 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_74'] = x_simulate_headroom__mutmut_74 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_75'] = x_simulate_headroom__mutmut_75 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_76'] = x_simulate_headroom__mutmut_76 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_77'] = x_simulate_headroom__mutmut_77 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_78'] = x_simulate_headroom__mutmut_78 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_79'] = x_simulate_headroom__mutmut_79 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_80'] = x_simulate_headroom__mutmut_80 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_81'] = x_simulate_headroom__mutmut_81 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_82'] = x_simulate_headroom__mutmut_82 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_83'] = x_simulate_headroom__mutmut_83 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_84'] = x_simulate_headroom__mutmut_84 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_85'] = x_simulate_headroom__mutmut_85 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_86'] = x_simulate_headroom__mutmut_86 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_87'] = x_simulate_headroom__mutmut_87 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_88'] = x_simulate_headroom__mutmut_88 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_89'] = x_simulate_headroom__mutmut_89 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_90'] = x_simulate_headroom__mutmut_90 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_91'] = x_simulate_headroom__mutmut_91 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_92'] = x_simulate_headroom__mutmut_92 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_93'] = x_simulate_headroom__mutmut_93 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_94'] = x_simulate_headroom__mutmut_94 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_95'] = x_simulate_headroom__mutmut_95 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_96'] = x_simulate_headroom__mutmut_96 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_97'] = x_simulate_headroom__mutmut_97 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_98'] = x_simulate_headroom__mutmut_98 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_99'] = x_simulate_headroom__mutmut_99 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_100'] = x_simulate_headroom__mutmut_100 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_101'] = x_simulate_headroom__mutmut_101 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_102'] = x_simulate_headroom__mutmut_102 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_103'] = x_simulate_headroom__mutmut_103 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_104'] = x_simulate_headroom__mutmut_104 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_105'] = x_simulate_headroom__mutmut_105 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_106'] = x_simulate_headroom__mutmut_106 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_107'] = x_simulate_headroom__mutmut_107 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_108'] = x_simulate_headroom__mutmut_108 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_109'] = x_simulate_headroom__mutmut_109 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_110'] = x_simulate_headroom__mutmut_110 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_111'] = x_simulate_headroom__mutmut_111 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_112'] = x_simulate_headroom__mutmut_112 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_113'] = x_simulate_headroom__mutmut_113 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_114'] = x_simulate_headroom__mutmut_114 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_115'] = x_simulate_headroom__mutmut_115 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_116'] = x_simulate_headroom__mutmut_116 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_117'] = x_simulate_headroom__mutmut_117 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_118'] = x_simulate_headroom__mutmut_118 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_119'] = x_simulate_headroom__mutmut_119 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_120'] = x_simulate_headroom__mutmut_120 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_121'] = x_simulate_headroom__mutmut_121 # type: ignore # mutmut generated
mutants_x_simulate_headroom__mutmut['x_simulate_headroom__mutmut_122'] = x_simulate_headroom__mutmut_122 # type: ignore # mutmut generated
mutants_x__utilization_percent__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__utilization_percent__mutmut)
def _utilization_percent(used: float, total: float) -> float:
    return used / total * 100 if total > 0 else 0.0


def x__utilization_percent__mutmut_orig(used: float, total: float) -> float:
    return used / total * 100 if total > 0 else 0.0


def x__utilization_percent__mutmut_1(used: float, total: float) -> float:
    return used / total / 100 if total > 0 else 0.0


def x__utilization_percent__mutmut_2(used: float, total: float) -> float:
    return used * total * 100 if total > 0 else 0.0


def x__utilization_percent__mutmut_3(used: float, total: float) -> float:
    return used / total * 101 if total > 0 else 0.0


def x__utilization_percent__mutmut_4(used: float, total: float) -> float:
    return used / total * 100 if total >= 0 else 0.0


def x__utilization_percent__mutmut_5(used: float, total: float) -> float:
    return used / total * 100 if total > 1 else 0.0


def x__utilization_percent__mutmut_6(used: float, total: float) -> float:
    return used / total * 100 if total > 0 else 1.0

mutants_x__utilization_percent__mutmut['_mutmut_orig'] = x__utilization_percent__mutmut_orig # type: ignore # mutmut generated
mutants_x__utilization_percent__mutmut['x__utilization_percent__mutmut_1'] = x__utilization_percent__mutmut_1 # type: ignore # mutmut generated
mutants_x__utilization_percent__mutmut['x__utilization_percent__mutmut_2'] = x__utilization_percent__mutmut_2 # type: ignore # mutmut generated
mutants_x__utilization_percent__mutmut['x__utilization_percent__mutmut_3'] = x__utilization_percent__mutmut_3 # type: ignore # mutmut generated
mutants_x__utilization_percent__mutmut['x__utilization_percent__mutmut_4'] = x__utilization_percent__mutmut_4 # type: ignore # mutmut generated
mutants_x__utilization_percent__mutmut['x__utilization_percent__mutmut_5'] = x__utilization_percent__mutmut_5 # type: ignore # mutmut generated
mutants_x__utilization_percent__mutmut['x__utilization_percent__mutmut_6'] = x__utilization_percent__mutmut_6 # type: ignore # mutmut generated
mutants_x__determine_verdict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__determine_verdict__mutmut)
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


def x__determine_verdict__mutmut_orig(
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


def x__determine_verdict__mutmut_1(
    post_cpu_pct: float, post_memory_pct: float, has_unschedulable: bool
) -> HeadroomVerdict:
    if has_unschedulable:
        return "XXneeds_nodesXX"
    worst = max(post_cpu_pct, post_memory_pct)
    if worst >= _cfg.needs_nodes_utilization_threshold:
        return "needs_nodes"
    if worst >= _cfg.tight_utilization_threshold:
        return "tight"
    return "fits"


def x__determine_verdict__mutmut_2(
    post_cpu_pct: float, post_memory_pct: float, has_unschedulable: bool
) -> HeadroomVerdict:
    if has_unschedulable:
        return "NEEDS_NODES"
    worst = max(post_cpu_pct, post_memory_pct)
    if worst >= _cfg.needs_nodes_utilization_threshold:
        return "needs_nodes"
    if worst >= _cfg.tight_utilization_threshold:
        return "tight"
    return "fits"


def x__determine_verdict__mutmut_3(
    post_cpu_pct: float, post_memory_pct: float, has_unschedulable: bool
) -> HeadroomVerdict:
    if has_unschedulable:
        return "needs_nodes"
    worst = None
    if worst >= _cfg.needs_nodes_utilization_threshold:
        return "needs_nodes"
    if worst >= _cfg.tight_utilization_threshold:
        return "tight"
    return "fits"


def x__determine_verdict__mutmut_4(
    post_cpu_pct: float, post_memory_pct: float, has_unschedulable: bool
) -> HeadroomVerdict:
    if has_unschedulable:
        return "needs_nodes"
    worst = max(None, post_memory_pct)
    if worst >= _cfg.needs_nodes_utilization_threshold:
        return "needs_nodes"
    if worst >= _cfg.tight_utilization_threshold:
        return "tight"
    return "fits"


def x__determine_verdict__mutmut_5(
    post_cpu_pct: float, post_memory_pct: float, has_unschedulable: bool
) -> HeadroomVerdict:
    if has_unschedulable:
        return "needs_nodes"
    worst = max(post_cpu_pct, None)
    if worst >= _cfg.needs_nodes_utilization_threshold:
        return "needs_nodes"
    if worst >= _cfg.tight_utilization_threshold:
        return "tight"
    return "fits"


def x__determine_verdict__mutmut_6(
    post_cpu_pct: float, post_memory_pct: float, has_unschedulable: bool
) -> HeadroomVerdict:
    if has_unschedulable:
        return "needs_nodes"
    worst = max(post_memory_pct)
    if worst >= _cfg.needs_nodes_utilization_threshold:
        return "needs_nodes"
    if worst >= _cfg.tight_utilization_threshold:
        return "tight"
    return "fits"


def x__determine_verdict__mutmut_7(
    post_cpu_pct: float, post_memory_pct: float, has_unschedulable: bool
) -> HeadroomVerdict:
    if has_unschedulable:
        return "needs_nodes"
    worst = max(post_cpu_pct, )
    if worst >= _cfg.needs_nodes_utilization_threshold:
        return "needs_nodes"
    if worst >= _cfg.tight_utilization_threshold:
        return "tight"
    return "fits"


def x__determine_verdict__mutmut_8(
    post_cpu_pct: float, post_memory_pct: float, has_unschedulable: bool
) -> HeadroomVerdict:
    if has_unschedulable:
        return "needs_nodes"
    worst = max(post_cpu_pct, post_memory_pct)
    if worst > _cfg.needs_nodes_utilization_threshold:
        return "needs_nodes"
    if worst >= _cfg.tight_utilization_threshold:
        return "tight"
    return "fits"


def x__determine_verdict__mutmut_9(
    post_cpu_pct: float, post_memory_pct: float, has_unschedulable: bool
) -> HeadroomVerdict:
    if has_unschedulable:
        return "needs_nodes"
    worst = max(post_cpu_pct, post_memory_pct)
    if worst >= _cfg.needs_nodes_utilization_threshold:
        return "XXneeds_nodesXX"
    if worst >= _cfg.tight_utilization_threshold:
        return "tight"
    return "fits"


def x__determine_verdict__mutmut_10(
    post_cpu_pct: float, post_memory_pct: float, has_unschedulable: bool
) -> HeadroomVerdict:
    if has_unschedulable:
        return "needs_nodes"
    worst = max(post_cpu_pct, post_memory_pct)
    if worst >= _cfg.needs_nodes_utilization_threshold:
        return "NEEDS_NODES"
    if worst >= _cfg.tight_utilization_threshold:
        return "tight"
    return "fits"


def x__determine_verdict__mutmut_11(
    post_cpu_pct: float, post_memory_pct: float, has_unschedulable: bool
) -> HeadroomVerdict:
    if has_unschedulable:
        return "needs_nodes"
    worst = max(post_cpu_pct, post_memory_pct)
    if worst >= _cfg.needs_nodes_utilization_threshold:
        return "needs_nodes"
    if worst > _cfg.tight_utilization_threshold:
        return "tight"
    return "fits"


def x__determine_verdict__mutmut_12(
    post_cpu_pct: float, post_memory_pct: float, has_unschedulable: bool
) -> HeadroomVerdict:
    if has_unschedulable:
        return "needs_nodes"
    worst = max(post_cpu_pct, post_memory_pct)
    if worst >= _cfg.needs_nodes_utilization_threshold:
        return "needs_nodes"
    if worst >= _cfg.tight_utilization_threshold:
        return "XXtightXX"
    return "fits"


def x__determine_verdict__mutmut_13(
    post_cpu_pct: float, post_memory_pct: float, has_unschedulable: bool
) -> HeadroomVerdict:
    if has_unschedulable:
        return "needs_nodes"
    worst = max(post_cpu_pct, post_memory_pct)
    if worst >= _cfg.needs_nodes_utilization_threshold:
        return "needs_nodes"
    if worst >= _cfg.tight_utilization_threshold:
        return "TIGHT"
    return "fits"


def x__determine_verdict__mutmut_14(
    post_cpu_pct: float, post_memory_pct: float, has_unschedulable: bool
) -> HeadroomVerdict:
    if has_unschedulable:
        return "needs_nodes"
    worst = max(post_cpu_pct, post_memory_pct)
    if worst >= _cfg.needs_nodes_utilization_threshold:
        return "needs_nodes"
    if worst >= _cfg.tight_utilization_threshold:
        return "tight"
    return "XXfitsXX"


def x__determine_verdict__mutmut_15(
    post_cpu_pct: float, post_memory_pct: float, has_unschedulable: bool
) -> HeadroomVerdict:
    if has_unschedulable:
        return "needs_nodes"
    worst = max(post_cpu_pct, post_memory_pct)
    if worst >= _cfg.needs_nodes_utilization_threshold:
        return "needs_nodes"
    if worst >= _cfg.tight_utilization_threshold:
        return "tight"
    return "FITS"

mutants_x__determine_verdict__mutmut['_mutmut_orig'] = x__determine_verdict__mutmut_orig # type: ignore # mutmut generated
mutants_x__determine_verdict__mutmut['x__determine_verdict__mutmut_1'] = x__determine_verdict__mutmut_1 # type: ignore # mutmut generated
mutants_x__determine_verdict__mutmut['x__determine_verdict__mutmut_2'] = x__determine_verdict__mutmut_2 # type: ignore # mutmut generated
mutants_x__determine_verdict__mutmut['x__determine_verdict__mutmut_3'] = x__determine_verdict__mutmut_3 # type: ignore # mutmut generated
mutants_x__determine_verdict__mutmut['x__determine_verdict__mutmut_4'] = x__determine_verdict__mutmut_4 # type: ignore # mutmut generated
mutants_x__determine_verdict__mutmut['x__determine_verdict__mutmut_5'] = x__determine_verdict__mutmut_5 # type: ignore # mutmut generated
mutants_x__determine_verdict__mutmut['x__determine_verdict__mutmut_6'] = x__determine_verdict__mutmut_6 # type: ignore # mutmut generated
mutants_x__determine_verdict__mutmut['x__determine_verdict__mutmut_7'] = x__determine_verdict__mutmut_7 # type: ignore # mutmut generated
mutants_x__determine_verdict__mutmut['x__determine_verdict__mutmut_8'] = x__determine_verdict__mutmut_8 # type: ignore # mutmut generated
mutants_x__determine_verdict__mutmut['x__determine_verdict__mutmut_9'] = x__determine_verdict__mutmut_9 # type: ignore # mutmut generated
mutants_x__determine_verdict__mutmut['x__determine_verdict__mutmut_10'] = x__determine_verdict__mutmut_10 # type: ignore # mutmut generated
mutants_x__determine_verdict__mutmut['x__determine_verdict__mutmut_11'] = x__determine_verdict__mutmut_11 # type: ignore # mutmut generated
mutants_x__determine_verdict__mutmut['x__determine_verdict__mutmut_12'] = x__determine_verdict__mutmut_12 # type: ignore # mutmut generated
mutants_x__determine_verdict__mutmut['x__determine_verdict__mutmut_13'] = x__determine_verdict__mutmut_13 # type: ignore # mutmut generated
mutants_x__determine_verdict__mutmut['x__determine_verdict__mutmut_14'] = x__determine_verdict__mutmut_14 # type: ignore # mutmut generated
mutants_x__determine_verdict__mutmut['x__determine_verdict__mutmut_15'] = x__determine_verdict__mutmut_15 # type: ignore # mutmut generated
mutants_x__binding_constraint__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__binding_constraint__mutmut)
def _binding_constraint(
    workloads: list[ProposedWorkload], post_cpu_pct: float, post_memory_pct: float
) -> BindingConstraint:
    if not workloads:
        return "None"
    return "CPU" if post_cpu_pct >= post_memory_pct else "Memory"


def x__binding_constraint__mutmut_orig(
    workloads: list[ProposedWorkload], post_cpu_pct: float, post_memory_pct: float
) -> BindingConstraint:
    if not workloads:
        return "None"
    return "CPU" if post_cpu_pct >= post_memory_pct else "Memory"


def x__binding_constraint__mutmut_1(
    workloads: list[ProposedWorkload], post_cpu_pct: float, post_memory_pct: float
) -> BindingConstraint:
    if workloads:
        return "None"
    return "CPU" if post_cpu_pct >= post_memory_pct else "Memory"


def x__binding_constraint__mutmut_2(
    workloads: list[ProposedWorkload], post_cpu_pct: float, post_memory_pct: float
) -> BindingConstraint:
    if not workloads:
        return "XXNoneXX"
    return "CPU" if post_cpu_pct >= post_memory_pct else "Memory"


def x__binding_constraint__mutmut_3(
    workloads: list[ProposedWorkload], post_cpu_pct: float, post_memory_pct: float
) -> BindingConstraint:
    if not workloads:
        return "none"
    return "CPU" if post_cpu_pct >= post_memory_pct else "Memory"


def x__binding_constraint__mutmut_4(
    workloads: list[ProposedWorkload], post_cpu_pct: float, post_memory_pct: float
) -> BindingConstraint:
    if not workloads:
        return "NONE"
    return "CPU" if post_cpu_pct >= post_memory_pct else "Memory"


def x__binding_constraint__mutmut_5(
    workloads: list[ProposedWorkload], post_cpu_pct: float, post_memory_pct: float
) -> BindingConstraint:
    if not workloads:
        return "None"
    return "XXCPUXX" if post_cpu_pct >= post_memory_pct else "Memory"


def x__binding_constraint__mutmut_6(
    workloads: list[ProposedWorkload], post_cpu_pct: float, post_memory_pct: float
) -> BindingConstraint:
    if not workloads:
        return "None"
    return "cpu" if post_cpu_pct >= post_memory_pct else "Memory"


def x__binding_constraint__mutmut_7(
    workloads: list[ProposedWorkload], post_cpu_pct: float, post_memory_pct: float
) -> BindingConstraint:
    if not workloads:
        return "None"
    return "CPU" if post_cpu_pct > post_memory_pct else "Memory"


def x__binding_constraint__mutmut_8(
    workloads: list[ProposedWorkload], post_cpu_pct: float, post_memory_pct: float
) -> BindingConstraint:
    if not workloads:
        return "None"
    return "CPU" if post_cpu_pct >= post_memory_pct else "XXMemoryXX"


def x__binding_constraint__mutmut_9(
    workloads: list[ProposedWorkload], post_cpu_pct: float, post_memory_pct: float
) -> BindingConstraint:
    if not workloads:
        return "None"
    return "CPU" if post_cpu_pct >= post_memory_pct else "memory"


def x__binding_constraint__mutmut_10(
    workloads: list[ProposedWorkload], post_cpu_pct: float, post_memory_pct: float
) -> BindingConstraint:
    if not workloads:
        return "None"
    return "CPU" if post_cpu_pct >= post_memory_pct else "MEMORY"

mutants_x__binding_constraint__mutmut['_mutmut_orig'] = x__binding_constraint__mutmut_orig # type: ignore # mutmut generated
mutants_x__binding_constraint__mutmut['x__binding_constraint__mutmut_1'] = x__binding_constraint__mutmut_1 # type: ignore # mutmut generated
mutants_x__binding_constraint__mutmut['x__binding_constraint__mutmut_2'] = x__binding_constraint__mutmut_2 # type: ignore # mutmut generated
mutants_x__binding_constraint__mutmut['x__binding_constraint__mutmut_3'] = x__binding_constraint__mutmut_3 # type: ignore # mutmut generated
mutants_x__binding_constraint__mutmut['x__binding_constraint__mutmut_4'] = x__binding_constraint__mutmut_4 # type: ignore # mutmut generated
mutants_x__binding_constraint__mutmut['x__binding_constraint__mutmut_5'] = x__binding_constraint__mutmut_5 # type: ignore # mutmut generated
mutants_x__binding_constraint__mutmut['x__binding_constraint__mutmut_6'] = x__binding_constraint__mutmut_6 # type: ignore # mutmut generated
mutants_x__binding_constraint__mutmut['x__binding_constraint__mutmut_7'] = x__binding_constraint__mutmut_7 # type: ignore # mutmut generated
mutants_x__binding_constraint__mutmut['x__binding_constraint__mutmut_8'] = x__binding_constraint__mutmut_8 # type: ignore # mutmut generated
mutants_x__binding_constraint__mutmut['x__binding_constraint__mutmut_9'] = x__binding_constraint__mutmut_9 # type: ignore # mutmut generated
mutants_x__binding_constraint__mutmut['x__binding_constraint__mutmut_10'] = x__binding_constraint__mutmut_10 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__recommend_additional_nodes__mutmut)
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


def x__recommend_additional_nodes__mutmut_orig(
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


def x__recommend_additional_nodes__mutmut_1(
    post_cpu_used: float, post_memory_used: float, snapshot: ClusterHeadroomSnapshot
) -> int:
    target_fraction = None
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


def x__recommend_additional_nodes__mutmut_2(
    post_cpu_used: float, post_memory_used: float, snapshot: ClusterHeadroomSnapshot
) -> int:
    target_fraction = _cfg.target_utilization_after_scaling_percent * 100
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


def x__recommend_additional_nodes__mutmut_3(
    post_cpu_used: float, post_memory_used: float, snapshot: ClusterHeadroomSnapshot
) -> int:
    target_fraction = _cfg.target_utilization_after_scaling_percent / 101
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


def x__recommend_additional_nodes__mutmut_4(
    post_cpu_used: float, post_memory_used: float, snapshot: ClusterHeadroomSnapshot
) -> int:
    target_fraction = _cfg.target_utilization_after_scaling_percent / 100
    target_cpu = None
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


def x__recommend_additional_nodes__mutmut_5(
    post_cpu_used: float, post_memory_used: float, snapshot: ClusterHeadroomSnapshot
) -> int:
    target_fraction = _cfg.target_utilization_after_scaling_percent / 100
    target_cpu = target_fraction / snapshot.total_allocatable_cpu_cores
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


def x__recommend_additional_nodes__mutmut_6(
    post_cpu_used: float, post_memory_used: float, snapshot: ClusterHeadroomSnapshot
) -> int:
    target_fraction = _cfg.target_utilization_after_scaling_percent / 100
    target_cpu = target_fraction * snapshot.total_allocatable_cpu_cores
    target_memory = None

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


def x__recommend_additional_nodes__mutmut_7(
    post_cpu_used: float, post_memory_used: float, snapshot: ClusterHeadroomSnapshot
) -> int:
    target_fraction = _cfg.target_utilization_after_scaling_percent / 100
    target_cpu = target_fraction * snapshot.total_allocatable_cpu_cores
    target_memory = target_fraction / snapshot.total_allocatable_memory_gb

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


def x__recommend_additional_nodes__mutmut_8(
    post_cpu_used: float, post_memory_used: float, snapshot: ClusterHeadroomSnapshot
) -> int:
    target_fraction = _cfg.target_utilization_after_scaling_percent / 100
    target_cpu = target_fraction * snapshot.total_allocatable_cpu_cores
    target_memory = target_fraction * snapshot.total_allocatable_memory_gb

    avg_node_cpu = None
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


def x__recommend_additional_nodes__mutmut_9(
    post_cpu_used: float, post_memory_used: float, snapshot: ClusterHeadroomSnapshot
) -> int:
    target_fraction = _cfg.target_utilization_after_scaling_percent / 100
    target_cpu = target_fraction * snapshot.total_allocatable_cpu_cores
    target_memory = target_fraction * snapshot.total_allocatable_memory_gb

    avg_node_cpu = (
        snapshot.total_allocatable_cpu_cores * snapshot.node_count if snapshot.node_count > 0 else 0
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


def x__recommend_additional_nodes__mutmut_10(
    post_cpu_used: float, post_memory_used: float, snapshot: ClusterHeadroomSnapshot
) -> int:
    target_fraction = _cfg.target_utilization_after_scaling_percent / 100
    target_cpu = target_fraction * snapshot.total_allocatable_cpu_cores
    target_memory = target_fraction * snapshot.total_allocatable_memory_gb

    avg_node_cpu = (
        snapshot.total_allocatable_cpu_cores / snapshot.node_count if snapshot.node_count >= 0 else 0
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


def x__recommend_additional_nodes__mutmut_11(
    post_cpu_used: float, post_memory_used: float, snapshot: ClusterHeadroomSnapshot
) -> int:
    target_fraction = _cfg.target_utilization_after_scaling_percent / 100
    target_cpu = target_fraction * snapshot.total_allocatable_cpu_cores
    target_memory = target_fraction * snapshot.total_allocatable_memory_gb

    avg_node_cpu = (
        snapshot.total_allocatable_cpu_cores / snapshot.node_count if snapshot.node_count > 1 else 0
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


def x__recommend_additional_nodes__mutmut_12(
    post_cpu_used: float, post_memory_used: float, snapshot: ClusterHeadroomSnapshot
) -> int:
    target_fraction = _cfg.target_utilization_after_scaling_percent / 100
    target_cpu = target_fraction * snapshot.total_allocatable_cpu_cores
    target_memory = target_fraction * snapshot.total_allocatable_memory_gb

    avg_node_cpu = (
        snapshot.total_allocatable_cpu_cores / snapshot.node_count if snapshot.node_count > 0 else 1
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


def x__recommend_additional_nodes__mutmut_13(
    post_cpu_used: float, post_memory_used: float, snapshot: ClusterHeadroomSnapshot
) -> int:
    target_fraction = _cfg.target_utilization_after_scaling_percent / 100
    target_cpu = target_fraction * snapshot.total_allocatable_cpu_cores
    target_memory = target_fraction * snapshot.total_allocatable_memory_gb

    avg_node_cpu = (
        snapshot.total_allocatable_cpu_cores / snapshot.node_count if snapshot.node_count > 0 else 0
    )
    avg_node_memory = None

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


def x__recommend_additional_nodes__mutmut_14(
    post_cpu_used: float, post_memory_used: float, snapshot: ClusterHeadroomSnapshot
) -> int:
    target_fraction = _cfg.target_utilization_after_scaling_percent / 100
    target_cpu = target_fraction * snapshot.total_allocatable_cpu_cores
    target_memory = target_fraction * snapshot.total_allocatable_memory_gb

    avg_node_cpu = (
        snapshot.total_allocatable_cpu_cores / snapshot.node_count if snapshot.node_count > 0 else 0
    )
    avg_node_memory = (
        snapshot.total_allocatable_memory_gb * snapshot.node_count if snapshot.node_count > 0 else 0
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


def x__recommend_additional_nodes__mutmut_15(
    post_cpu_used: float, post_memory_used: float, snapshot: ClusterHeadroomSnapshot
) -> int:
    target_fraction = _cfg.target_utilization_after_scaling_percent / 100
    target_cpu = target_fraction * snapshot.total_allocatable_cpu_cores
    target_memory = target_fraction * snapshot.total_allocatable_memory_gb

    avg_node_cpu = (
        snapshot.total_allocatable_cpu_cores / snapshot.node_count if snapshot.node_count > 0 else 0
    )
    avg_node_memory = (
        snapshot.total_allocatable_memory_gb / snapshot.node_count if snapshot.node_count >= 0 else 0
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


def x__recommend_additional_nodes__mutmut_16(
    post_cpu_used: float, post_memory_used: float, snapshot: ClusterHeadroomSnapshot
) -> int:
    target_fraction = _cfg.target_utilization_after_scaling_percent / 100
    target_cpu = target_fraction * snapshot.total_allocatable_cpu_cores
    target_memory = target_fraction * snapshot.total_allocatable_memory_gb

    avg_node_cpu = (
        snapshot.total_allocatable_cpu_cores / snapshot.node_count if snapshot.node_count > 0 else 0
    )
    avg_node_memory = (
        snapshot.total_allocatable_memory_gb / snapshot.node_count if snapshot.node_count > 1 else 0
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


def x__recommend_additional_nodes__mutmut_17(
    post_cpu_used: float, post_memory_used: float, snapshot: ClusterHeadroomSnapshot
) -> int:
    target_fraction = _cfg.target_utilization_after_scaling_percent / 100
    target_cpu = target_fraction * snapshot.total_allocatable_cpu_cores
    target_memory = target_fraction * snapshot.total_allocatable_memory_gb

    avg_node_cpu = (
        snapshot.total_allocatable_cpu_cores / snapshot.node_count if snapshot.node_count > 0 else 0
    )
    avg_node_memory = (
        snapshot.total_allocatable_memory_gb / snapshot.node_count if snapshot.node_count > 0 else 1
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


def x__recommend_additional_nodes__mutmut_18(
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

    nodes_for_cpu = None
    nodes_for_memory = (
        math.ceil((post_memory_used - target_memory) / avg_node_memory)
        if avg_node_memory > 0 and post_memory_used > target_memory
        else 0
    )
    return max(nodes_for_cpu, nodes_for_memory, 1)


def x__recommend_additional_nodes__mutmut_19(
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
        math.ceil(None)
        if avg_node_cpu > 0 and post_cpu_used > target_cpu
        else 0
    )
    nodes_for_memory = (
        math.ceil((post_memory_used - target_memory) / avg_node_memory)
        if avg_node_memory > 0 and post_memory_used > target_memory
        else 0
    )
    return max(nodes_for_cpu, nodes_for_memory, 1)


def x__recommend_additional_nodes__mutmut_20(
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
        math.ceil((post_cpu_used - target_cpu) * avg_node_cpu)
        if avg_node_cpu > 0 and post_cpu_used > target_cpu
        else 0
    )
    nodes_for_memory = (
        math.ceil((post_memory_used - target_memory) / avg_node_memory)
        if avg_node_memory > 0 and post_memory_used > target_memory
        else 0
    )
    return max(nodes_for_cpu, nodes_for_memory, 1)


def x__recommend_additional_nodes__mutmut_21(
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
        math.ceil((post_cpu_used + target_cpu) / avg_node_cpu)
        if avg_node_cpu > 0 and post_cpu_used > target_cpu
        else 0
    )
    nodes_for_memory = (
        math.ceil((post_memory_used - target_memory) / avg_node_memory)
        if avg_node_memory > 0 and post_memory_used > target_memory
        else 0
    )
    return max(nodes_for_cpu, nodes_for_memory, 1)


def x__recommend_additional_nodes__mutmut_22(
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
        if avg_node_cpu > 0 or post_cpu_used > target_cpu
        else 0
    )
    nodes_for_memory = (
        math.ceil((post_memory_used - target_memory) / avg_node_memory)
        if avg_node_memory > 0 and post_memory_used > target_memory
        else 0
    )
    return max(nodes_for_cpu, nodes_for_memory, 1)


def x__recommend_additional_nodes__mutmut_23(
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
        if avg_node_cpu >= 0 and post_cpu_used > target_cpu
        else 0
    )
    nodes_for_memory = (
        math.ceil((post_memory_used - target_memory) / avg_node_memory)
        if avg_node_memory > 0 and post_memory_used > target_memory
        else 0
    )
    return max(nodes_for_cpu, nodes_for_memory, 1)


def x__recommend_additional_nodes__mutmut_24(
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
        if avg_node_cpu > 1 and post_cpu_used > target_cpu
        else 0
    )
    nodes_for_memory = (
        math.ceil((post_memory_used - target_memory) / avg_node_memory)
        if avg_node_memory > 0 and post_memory_used > target_memory
        else 0
    )
    return max(nodes_for_cpu, nodes_for_memory, 1)


def x__recommend_additional_nodes__mutmut_25(
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
        if avg_node_cpu > 0 and post_cpu_used >= target_cpu
        else 0
    )
    nodes_for_memory = (
        math.ceil((post_memory_used - target_memory) / avg_node_memory)
        if avg_node_memory > 0 and post_memory_used > target_memory
        else 0
    )
    return max(nodes_for_cpu, nodes_for_memory, 1)


def x__recommend_additional_nodes__mutmut_26(
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
        else 1
    )
    nodes_for_memory = (
        math.ceil((post_memory_used - target_memory) / avg_node_memory)
        if avg_node_memory > 0 and post_memory_used > target_memory
        else 0
    )
    return max(nodes_for_cpu, nodes_for_memory, 1)


def x__recommend_additional_nodes__mutmut_27(
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
    nodes_for_memory = None
    return max(nodes_for_cpu, nodes_for_memory, 1)


def x__recommend_additional_nodes__mutmut_28(
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
        math.ceil(None)
        if avg_node_memory > 0 and post_memory_used > target_memory
        else 0
    )
    return max(nodes_for_cpu, nodes_for_memory, 1)


def x__recommend_additional_nodes__mutmut_29(
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
        math.ceil((post_memory_used - target_memory) * avg_node_memory)
        if avg_node_memory > 0 and post_memory_used > target_memory
        else 0
    )
    return max(nodes_for_cpu, nodes_for_memory, 1)


def x__recommend_additional_nodes__mutmut_30(
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
        math.ceil((post_memory_used + target_memory) / avg_node_memory)
        if avg_node_memory > 0 and post_memory_used > target_memory
        else 0
    )
    return max(nodes_for_cpu, nodes_for_memory, 1)


def x__recommend_additional_nodes__mutmut_31(
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
        if avg_node_memory > 0 or post_memory_used > target_memory
        else 0
    )
    return max(nodes_for_cpu, nodes_for_memory, 1)


def x__recommend_additional_nodes__mutmut_32(
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
        if avg_node_memory >= 0 and post_memory_used > target_memory
        else 0
    )
    return max(nodes_for_cpu, nodes_for_memory, 1)


def x__recommend_additional_nodes__mutmut_33(
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
        if avg_node_memory > 1 and post_memory_used > target_memory
        else 0
    )
    return max(nodes_for_cpu, nodes_for_memory, 1)


def x__recommend_additional_nodes__mutmut_34(
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
        if avg_node_memory > 0 and post_memory_used >= target_memory
        else 0
    )
    return max(nodes_for_cpu, nodes_for_memory, 1)


def x__recommend_additional_nodes__mutmut_35(
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
        else 1
    )
    return max(nodes_for_cpu, nodes_for_memory, 1)


def x__recommend_additional_nodes__mutmut_36(
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
    return max(None, nodes_for_memory, 1)


def x__recommend_additional_nodes__mutmut_37(
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
    return max(nodes_for_cpu, None, 1)


def x__recommend_additional_nodes__mutmut_38(
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
    return max(nodes_for_cpu, nodes_for_memory, None)


def x__recommend_additional_nodes__mutmut_39(
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
    return max(nodes_for_memory, 1)


def x__recommend_additional_nodes__mutmut_40(
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
    return max(nodes_for_cpu, 1)


def x__recommend_additional_nodes__mutmut_41(
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
    return max(nodes_for_cpu, nodes_for_memory, )


def x__recommend_additional_nodes__mutmut_42(
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
    return max(nodes_for_cpu, nodes_for_memory, 2)

mutants_x__recommend_additional_nodes__mutmut['_mutmut_orig'] = x__recommend_additional_nodes__mutmut_orig # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_1'] = x__recommend_additional_nodes__mutmut_1 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_2'] = x__recommend_additional_nodes__mutmut_2 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_3'] = x__recommend_additional_nodes__mutmut_3 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_4'] = x__recommend_additional_nodes__mutmut_4 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_5'] = x__recommend_additional_nodes__mutmut_5 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_6'] = x__recommend_additional_nodes__mutmut_6 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_7'] = x__recommend_additional_nodes__mutmut_7 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_8'] = x__recommend_additional_nodes__mutmut_8 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_9'] = x__recommend_additional_nodes__mutmut_9 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_10'] = x__recommend_additional_nodes__mutmut_10 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_11'] = x__recommend_additional_nodes__mutmut_11 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_12'] = x__recommend_additional_nodes__mutmut_12 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_13'] = x__recommend_additional_nodes__mutmut_13 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_14'] = x__recommend_additional_nodes__mutmut_14 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_15'] = x__recommend_additional_nodes__mutmut_15 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_16'] = x__recommend_additional_nodes__mutmut_16 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_17'] = x__recommend_additional_nodes__mutmut_17 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_18'] = x__recommend_additional_nodes__mutmut_18 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_19'] = x__recommend_additional_nodes__mutmut_19 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_20'] = x__recommend_additional_nodes__mutmut_20 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_21'] = x__recommend_additional_nodes__mutmut_21 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_22'] = x__recommend_additional_nodes__mutmut_22 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_23'] = x__recommend_additional_nodes__mutmut_23 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_24'] = x__recommend_additional_nodes__mutmut_24 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_25'] = x__recommend_additional_nodes__mutmut_25 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_26'] = x__recommend_additional_nodes__mutmut_26 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_27'] = x__recommend_additional_nodes__mutmut_27 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_28'] = x__recommend_additional_nodes__mutmut_28 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_29'] = x__recommend_additional_nodes__mutmut_29 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_30'] = x__recommend_additional_nodes__mutmut_30 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_31'] = x__recommend_additional_nodes__mutmut_31 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_32'] = x__recommend_additional_nodes__mutmut_32 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_33'] = x__recommend_additional_nodes__mutmut_33 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_34'] = x__recommend_additional_nodes__mutmut_34 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_35'] = x__recommend_additional_nodes__mutmut_35 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_36'] = x__recommend_additional_nodes__mutmut_36 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_37'] = x__recommend_additional_nodes__mutmut_37 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_38'] = x__recommend_additional_nodes__mutmut_38 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_39'] = x__recommend_additional_nodes__mutmut_39 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_40'] = x__recommend_additional_nodes__mutmut_40 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_41'] = x__recommend_additional_nodes__mutmut_41 # type: ignore # mutmut generated
mutants_x__recommend_additional_nodes__mutmut['x__recommend_additional_nodes__mutmut_42'] = x__recommend_additional_nodes__mutmut_42 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_summary__mutmut)
def _build_summary(  # noqa: PLR0913
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


def x__build_summary__mutmut_orig(  # noqa: PLR0913
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


def x__build_summary__mutmut_1(  # noqa: PLR0913
    has_workloads: bool,
    verdict: HeadroomVerdict,
    binding_constraint: BindingConstraint,
    post_cpu_pct: float,
    post_memory_pct: float,
    recommended_nodes: int,
    autoscaler_enabled: bool,
    unschedulable: list[str],
) -> str:
    if has_workloads:
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


def x__build_summary__mutmut_2(  # noqa: PLR0913
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
        base = None
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


def x__build_summary__mutmut_3(  # noqa: PLR0913
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
        base = "XXNo new workloads proposed — current headroom shown.XX"
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


def x__build_summary__mutmut_4(  # noqa: PLR0913
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
        base = "no new workloads proposed — current headroom shown."
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


def x__build_summary__mutmut_5(  # noqa: PLR0913
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
        base = "NO NEW WORKLOADS PROPOSED — CURRENT HEADROOM SHOWN."
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


def x__build_summary__mutmut_6(  # noqa: PLR0913
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
        base = None
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


def x__build_summary__mutmut_7(  # noqa: PLR0913
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
            f"Unschedulable: {', '.join(None)} — request(s) exceed the largest "
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


def x__build_summary__mutmut_8(  # noqa: PLR0913
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
            f"Unschedulable: {'XX, XX'.join(unschedulable)} — request(s) exceed the largest "
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


def x__build_summary__mutmut_9(  # noqa: PLR0913
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
            "XXavailable node; a larger node type is needed, not just more of the current size.XX"
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


def x__build_summary__mutmut_10(  # noqa: PLR0913
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
            "AVAILABLE NODE; A LARGER NODE TYPE IS NEEDED, NOT JUST MORE OF THE CURRENT SIZE."
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


def x__build_summary__mutmut_11(  # noqa: PLR0913
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
    elif verdict != "needs_nodes":
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


def x__build_summary__mutmut_12(  # noqa: PLR0913
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
    elif verdict == "XXneeds_nodesXX":
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


def x__build_summary__mutmut_13(  # noqa: PLR0913
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
    elif verdict == "NEEDS_NODES":
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


def x__build_summary__mutmut_14(  # noqa: PLR0913
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
        worst = None
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


def x__build_summary__mutmut_15(  # noqa: PLR0913
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
        worst = max(None, post_memory_pct)
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


def x__build_summary__mutmut_16(  # noqa: PLR0913
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
        worst = max(post_cpu_pct, None)
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


def x__build_summary__mutmut_17(  # noqa: PLR0913
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
        worst = max(post_memory_pct)
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


def x__build_summary__mutmut_18(  # noqa: PLR0913
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
        worst = max(post_cpu_pct, )
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


def x__build_summary__mutmut_19(  # noqa: PLR0913
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
        base = None
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


def x__build_summary__mutmut_20(  # noqa: PLR0913
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
    elif verdict != "tight":
        worst = max(post_cpu_pct, post_memory_pct)
        base = f"Tight — projected utilization would reach {worst:.1f}%. Monitor closely."
    else:
        base = "Fits comfortably within current cluster capacity."

    if has_workloads and binding_constraint != "None" and verdict != "fits":
        base += f" {binding_constraint} is the binding constraint."
    if autoscaler_enabled:
        base += " Cluster autoscaler is enabled as a safety net."
    return base


def x__build_summary__mutmut_21(  # noqa: PLR0913
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
    elif verdict == "XXtightXX":
        worst = max(post_cpu_pct, post_memory_pct)
        base = f"Tight — projected utilization would reach {worst:.1f}%. Monitor closely."
    else:
        base = "Fits comfortably within current cluster capacity."

    if has_workloads and binding_constraint != "None" and verdict != "fits":
        base += f" {binding_constraint} is the binding constraint."
    if autoscaler_enabled:
        base += " Cluster autoscaler is enabled as a safety net."
    return base


def x__build_summary__mutmut_22(  # noqa: PLR0913
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
    elif verdict == "TIGHT":
        worst = max(post_cpu_pct, post_memory_pct)
        base = f"Tight — projected utilization would reach {worst:.1f}%. Monitor closely."
    else:
        base = "Fits comfortably within current cluster capacity."

    if has_workloads and binding_constraint != "None" and verdict != "fits":
        base += f" {binding_constraint} is the binding constraint."
    if autoscaler_enabled:
        base += " Cluster autoscaler is enabled as a safety net."
    return base


def x__build_summary__mutmut_23(  # noqa: PLR0913
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
        worst = None
        base = f"Tight — projected utilization would reach {worst:.1f}%. Monitor closely."
    else:
        base = "Fits comfortably within current cluster capacity."

    if has_workloads and binding_constraint != "None" and verdict != "fits":
        base += f" {binding_constraint} is the binding constraint."
    if autoscaler_enabled:
        base += " Cluster autoscaler is enabled as a safety net."
    return base


def x__build_summary__mutmut_24(  # noqa: PLR0913
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
        worst = max(None, post_memory_pct)
        base = f"Tight — projected utilization would reach {worst:.1f}%. Monitor closely."
    else:
        base = "Fits comfortably within current cluster capacity."

    if has_workloads and binding_constraint != "None" and verdict != "fits":
        base += f" {binding_constraint} is the binding constraint."
    if autoscaler_enabled:
        base += " Cluster autoscaler is enabled as a safety net."
    return base


def x__build_summary__mutmut_25(  # noqa: PLR0913
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
        worst = max(post_cpu_pct, None)
        base = f"Tight — projected utilization would reach {worst:.1f}%. Monitor closely."
    else:
        base = "Fits comfortably within current cluster capacity."

    if has_workloads and binding_constraint != "None" and verdict != "fits":
        base += f" {binding_constraint} is the binding constraint."
    if autoscaler_enabled:
        base += " Cluster autoscaler is enabled as a safety net."
    return base


def x__build_summary__mutmut_26(  # noqa: PLR0913
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
        worst = max(post_memory_pct)
        base = f"Tight — projected utilization would reach {worst:.1f}%. Monitor closely."
    else:
        base = "Fits comfortably within current cluster capacity."

    if has_workloads and binding_constraint != "None" and verdict != "fits":
        base += f" {binding_constraint} is the binding constraint."
    if autoscaler_enabled:
        base += " Cluster autoscaler is enabled as a safety net."
    return base


def x__build_summary__mutmut_27(  # noqa: PLR0913
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
        worst = max(post_cpu_pct, )
        base = f"Tight — projected utilization would reach {worst:.1f}%. Monitor closely."
    else:
        base = "Fits comfortably within current cluster capacity."

    if has_workloads and binding_constraint != "None" and verdict != "fits":
        base += f" {binding_constraint} is the binding constraint."
    if autoscaler_enabled:
        base += " Cluster autoscaler is enabled as a safety net."
    return base


def x__build_summary__mutmut_28(  # noqa: PLR0913
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
        base = None
    else:
        base = "Fits comfortably within current cluster capacity."

    if has_workloads and binding_constraint != "None" and verdict != "fits":
        base += f" {binding_constraint} is the binding constraint."
    if autoscaler_enabled:
        base += " Cluster autoscaler is enabled as a safety net."
    return base


def x__build_summary__mutmut_29(  # noqa: PLR0913
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
        base = None

    if has_workloads and binding_constraint != "None" and verdict != "fits":
        base += f" {binding_constraint} is the binding constraint."
    if autoscaler_enabled:
        base += " Cluster autoscaler is enabled as a safety net."
    return base


def x__build_summary__mutmut_30(  # noqa: PLR0913
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
        base = "XXFits comfortably within current cluster capacity.XX"

    if has_workloads and binding_constraint != "None" and verdict != "fits":
        base += f" {binding_constraint} is the binding constraint."
    if autoscaler_enabled:
        base += " Cluster autoscaler is enabled as a safety net."
    return base


def x__build_summary__mutmut_31(  # noqa: PLR0913
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
        base = "fits comfortably within current cluster capacity."

    if has_workloads and binding_constraint != "None" and verdict != "fits":
        base += f" {binding_constraint} is the binding constraint."
    if autoscaler_enabled:
        base += " Cluster autoscaler is enabled as a safety net."
    return base


def x__build_summary__mutmut_32(  # noqa: PLR0913
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
        base = "FITS COMFORTABLY WITHIN CURRENT CLUSTER CAPACITY."

    if has_workloads and binding_constraint != "None" and verdict != "fits":
        base += f" {binding_constraint} is the binding constraint."
    if autoscaler_enabled:
        base += " Cluster autoscaler is enabled as a safety net."
    return base


def x__build_summary__mutmut_33(  # noqa: PLR0913
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

    if has_workloads and binding_constraint != "None" or verdict != "fits":
        base += f" {binding_constraint} is the binding constraint."
    if autoscaler_enabled:
        base += " Cluster autoscaler is enabled as a safety net."
    return base


def x__build_summary__mutmut_34(  # noqa: PLR0913
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

    if has_workloads or binding_constraint != "None" and verdict != "fits":
        base += f" {binding_constraint} is the binding constraint."
    if autoscaler_enabled:
        base += " Cluster autoscaler is enabled as a safety net."
    return base


def x__build_summary__mutmut_35(  # noqa: PLR0913
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

    if has_workloads and binding_constraint == "None" and verdict != "fits":
        base += f" {binding_constraint} is the binding constraint."
    if autoscaler_enabled:
        base += " Cluster autoscaler is enabled as a safety net."
    return base


def x__build_summary__mutmut_36(  # noqa: PLR0913
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

    if has_workloads and binding_constraint != "XXNoneXX" and verdict != "fits":
        base += f" {binding_constraint} is the binding constraint."
    if autoscaler_enabled:
        base += " Cluster autoscaler is enabled as a safety net."
    return base


def x__build_summary__mutmut_37(  # noqa: PLR0913
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

    if has_workloads and binding_constraint != "none" and verdict != "fits":
        base += f" {binding_constraint} is the binding constraint."
    if autoscaler_enabled:
        base += " Cluster autoscaler is enabled as a safety net."
    return base


def x__build_summary__mutmut_38(  # noqa: PLR0913
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

    if has_workloads and binding_constraint != "NONE" and verdict != "fits":
        base += f" {binding_constraint} is the binding constraint."
    if autoscaler_enabled:
        base += " Cluster autoscaler is enabled as a safety net."
    return base


def x__build_summary__mutmut_39(  # noqa: PLR0913
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

    if has_workloads and binding_constraint != "None" and verdict == "fits":
        base += f" {binding_constraint} is the binding constraint."
    if autoscaler_enabled:
        base += " Cluster autoscaler is enabled as a safety net."
    return base


def x__build_summary__mutmut_40(  # noqa: PLR0913
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

    if has_workloads and binding_constraint != "None" and verdict != "XXfitsXX":
        base += f" {binding_constraint} is the binding constraint."
    if autoscaler_enabled:
        base += " Cluster autoscaler is enabled as a safety net."
    return base


def x__build_summary__mutmut_41(  # noqa: PLR0913
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

    if has_workloads and binding_constraint != "None" and verdict != "FITS":
        base += f" {binding_constraint} is the binding constraint."
    if autoscaler_enabled:
        base += " Cluster autoscaler is enabled as a safety net."
    return base


def x__build_summary__mutmut_42(  # noqa: PLR0913
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
        base = f" {binding_constraint} is the binding constraint."
    if autoscaler_enabled:
        base += " Cluster autoscaler is enabled as a safety net."
    return base


def x__build_summary__mutmut_43(  # noqa: PLR0913
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
        base -= f" {binding_constraint} is the binding constraint."
    if autoscaler_enabled:
        base += " Cluster autoscaler is enabled as a safety net."
    return base


def x__build_summary__mutmut_44(  # noqa: PLR0913
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
        base = " Cluster autoscaler is enabled as a safety net."
    return base


def x__build_summary__mutmut_45(  # noqa: PLR0913
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
        base -= " Cluster autoscaler is enabled as a safety net."
    return base


def x__build_summary__mutmut_46(  # noqa: PLR0913
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
        base += "XX Cluster autoscaler is enabled as a safety net.XX"
    return base


def x__build_summary__mutmut_47(  # noqa: PLR0913
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
        base += " cluster autoscaler is enabled as a safety net."
    return base


def x__build_summary__mutmut_48(  # noqa: PLR0913
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
        base += " CLUSTER AUTOSCALER IS ENABLED AS A SAFETY NET."
    return base

mutants_x__build_summary__mutmut['_mutmut_orig'] = x__build_summary__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_1'] = x__build_summary__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_2'] = x__build_summary__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_3'] = x__build_summary__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_4'] = x__build_summary__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_5'] = x__build_summary__mutmut_5 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_6'] = x__build_summary__mutmut_6 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_7'] = x__build_summary__mutmut_7 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_8'] = x__build_summary__mutmut_8 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_9'] = x__build_summary__mutmut_9 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_10'] = x__build_summary__mutmut_10 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_11'] = x__build_summary__mutmut_11 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_12'] = x__build_summary__mutmut_12 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_13'] = x__build_summary__mutmut_13 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_14'] = x__build_summary__mutmut_14 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_15'] = x__build_summary__mutmut_15 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_16'] = x__build_summary__mutmut_16 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_17'] = x__build_summary__mutmut_17 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_18'] = x__build_summary__mutmut_18 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_19'] = x__build_summary__mutmut_19 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_20'] = x__build_summary__mutmut_20 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_21'] = x__build_summary__mutmut_21 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_22'] = x__build_summary__mutmut_22 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_23'] = x__build_summary__mutmut_23 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_24'] = x__build_summary__mutmut_24 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_25'] = x__build_summary__mutmut_25 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_26'] = x__build_summary__mutmut_26 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_27'] = x__build_summary__mutmut_27 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_28'] = x__build_summary__mutmut_28 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_29'] = x__build_summary__mutmut_29 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_30'] = x__build_summary__mutmut_30 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_31'] = x__build_summary__mutmut_31 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_32'] = x__build_summary__mutmut_32 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_33'] = x__build_summary__mutmut_33 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_34'] = x__build_summary__mutmut_34 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_35'] = x__build_summary__mutmut_35 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_36'] = x__build_summary__mutmut_36 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_37'] = x__build_summary__mutmut_37 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_38'] = x__build_summary__mutmut_38 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_39'] = x__build_summary__mutmut_39 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_40'] = x__build_summary__mutmut_40 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_41'] = x__build_summary__mutmut_41 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_42'] = x__build_summary__mutmut_42 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_43'] = x__build_summary__mutmut_43 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_44'] = x__build_summary__mutmut_44 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_45'] = x__build_summary__mutmut_45 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_46'] = x__build_summary__mutmut_46 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_47'] = x__build_summary__mutmut_47 # type: ignore # mutmut generated
mutants_x__build_summary__mutmut['x__build_summary__mutmut_48'] = x__build_summary__mutmut_48 # type: ignore # mutmut generated
