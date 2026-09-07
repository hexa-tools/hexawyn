"""Pure Cilium datapath status classification — no infra imports."""

from __future__ import annotations

from hexawyn.domain.models.cilium import CiliumAgentHealth, CiliumStatusResult

_NOT_INSTALLED_NOTE = "Cilium is not installed in this cluster"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_status_result__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_status_result__mutmut)
def build_status_result(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_orig(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_1(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = None
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_2(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = None
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_3(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(None)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_4(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(2 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_5(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total != 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_6(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 1:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_7(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=None,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_8(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status=None,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_9(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=None,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_10(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=None,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_11(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=None,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_12(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=None,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_13(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=None,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_14(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_15(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_16(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_17(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_18(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_19(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_20(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_21(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_22(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_23(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=False,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_24(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="XXunknownXX",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_25(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="UNKNOWN",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_26(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=1,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_27(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=1,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_28(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=1,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_29(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = None
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_30(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready <= total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_31(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_32(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = None
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_33(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(None)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_34(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(2 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_35(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready and node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_36(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_37(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count >= 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_38(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 1)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_39(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=None,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_40(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status=None,
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_41(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=None,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_42(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=None,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_43(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=None,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_44(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=None,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_45(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity=None,
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_46(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=None,
        note=note,
    )


def x_build_status_result__mutmut_47(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=None,
    )


def x_build_status_result__mutmut_48(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_49(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_50(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_51(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_52(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_53(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_54(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_55(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        note=note,
    )


def x_build_status_result__mutmut_56(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        )


def x_build_status_result__mutmut_57(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=False,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_58(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="XXdegradedXX" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_59(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="DEGRADED" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_60(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "XXhealthyXX",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_61(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "HEALTHY",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_62(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="XXdegradedXX" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_63(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="DEGRADED" if degraded else "ok",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_64(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "XXokXX",
        nodes=nodes,
        note=note,
    )


def x_build_status_result__mutmut_65(
    nodes: list[CiliumAgentHealth], note: str | None = None
) -> CiliumStatusResult:
    """Aggregate per-node agent health into a CiliumStatusResult.

    Healthy means every observed agent is ready; a cluster with no observed
    agents is reported as ``unknown`` rather than healthy (never invented).
    """
    total = len(nodes)
    ready = sum(1 for node in nodes if node.ready)
    if total == 0:
        return CiliumStatusResult(
            installed=True,
            status="unknown",
            ready_agents=0,
            total_agents=0,
            degraded_summary=None,
            controller_errors=0,
            connectivity=None,
            nodes=nodes,
            note=note,
        )
    degraded = ready < total
    degraded_summary = f"{ready}/{total} agents ready" if degraded else None
    controller_errors = sum(1 for node in nodes if not node.ready or node.restart_count > 0)
    return CiliumStatusResult(
        installed=True,
        status="degraded" if degraded else "healthy",
        ready_agents=ready,
        total_agents=total,
        degraded_summary=degraded_summary,
        controller_errors=controller_errors,
        connectivity="degraded" if degraded else "OK",
        nodes=nodes,
        note=note,
    )

mutants_x_build_status_result__mutmut['_mutmut_orig'] = x_build_status_result__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_1'] = x_build_status_result__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_2'] = x_build_status_result__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_3'] = x_build_status_result__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_4'] = x_build_status_result__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_5'] = x_build_status_result__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_6'] = x_build_status_result__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_7'] = x_build_status_result__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_8'] = x_build_status_result__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_9'] = x_build_status_result__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_10'] = x_build_status_result__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_11'] = x_build_status_result__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_12'] = x_build_status_result__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_13'] = x_build_status_result__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_14'] = x_build_status_result__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_15'] = x_build_status_result__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_16'] = x_build_status_result__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_17'] = x_build_status_result__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_18'] = x_build_status_result__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_19'] = x_build_status_result__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_20'] = x_build_status_result__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_21'] = x_build_status_result__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_22'] = x_build_status_result__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_23'] = x_build_status_result__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_24'] = x_build_status_result__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_25'] = x_build_status_result__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_26'] = x_build_status_result__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_27'] = x_build_status_result__mutmut_27 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_28'] = x_build_status_result__mutmut_28 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_29'] = x_build_status_result__mutmut_29 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_30'] = x_build_status_result__mutmut_30 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_31'] = x_build_status_result__mutmut_31 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_32'] = x_build_status_result__mutmut_32 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_33'] = x_build_status_result__mutmut_33 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_34'] = x_build_status_result__mutmut_34 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_35'] = x_build_status_result__mutmut_35 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_36'] = x_build_status_result__mutmut_36 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_37'] = x_build_status_result__mutmut_37 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_38'] = x_build_status_result__mutmut_38 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_39'] = x_build_status_result__mutmut_39 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_40'] = x_build_status_result__mutmut_40 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_41'] = x_build_status_result__mutmut_41 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_42'] = x_build_status_result__mutmut_42 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_43'] = x_build_status_result__mutmut_43 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_44'] = x_build_status_result__mutmut_44 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_45'] = x_build_status_result__mutmut_45 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_46'] = x_build_status_result__mutmut_46 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_47'] = x_build_status_result__mutmut_47 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_48'] = x_build_status_result__mutmut_48 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_49'] = x_build_status_result__mutmut_49 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_50'] = x_build_status_result__mutmut_50 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_51'] = x_build_status_result__mutmut_51 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_52'] = x_build_status_result__mutmut_52 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_53'] = x_build_status_result__mutmut_53 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_54'] = x_build_status_result__mutmut_54 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_55'] = x_build_status_result__mutmut_55 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_56'] = x_build_status_result__mutmut_56 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_57'] = x_build_status_result__mutmut_57 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_58'] = x_build_status_result__mutmut_58 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_59'] = x_build_status_result__mutmut_59 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_60'] = x_build_status_result__mutmut_60 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_61'] = x_build_status_result__mutmut_61 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_62'] = x_build_status_result__mutmut_62 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_63'] = x_build_status_result__mutmut_63 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_64'] = x_build_status_result__mutmut_64 # type: ignore # mutmut generated
mutants_x_build_status_result__mutmut['x_build_status_result__mutmut_65'] = x_build_status_result__mutmut_65 # type: ignore # mutmut generated
mutants_x_not_installed_result__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_not_installed_result__mutmut)
def not_installed_result() -> CiliumStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated agent or status value."""
    return CiliumStatusResult(
        installed=False,
        status="not_installed",
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_result__mutmut_orig() -> CiliumStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated agent or status value."""
    return CiliumStatusResult(
        installed=False,
        status="not_installed",
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_result__mutmut_1() -> CiliumStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated agent or status value."""
    return CiliumStatusResult(
        installed=None,
        status="not_installed",
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_result__mutmut_2() -> CiliumStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated agent or status value."""
    return CiliumStatusResult(
        installed=False,
        status=None,
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_result__mutmut_3() -> CiliumStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated agent or status value."""
    return CiliumStatusResult(
        installed=False,
        status="not_installed",
        ready_agents=None,
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_result__mutmut_4() -> CiliumStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated agent or status value."""
    return CiliumStatusResult(
        installed=False,
        status="not_installed",
        ready_agents=0,
        total_agents=None,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_result__mutmut_5() -> CiliumStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated agent or status value."""
    return CiliumStatusResult(
        installed=False,
        status="not_installed",
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        controller_errors=None,
        connectivity=None,
        nodes=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_result__mutmut_6() -> CiliumStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated agent or status value."""
    return CiliumStatusResult(
        installed=False,
        status="not_installed",
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=None,
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_result__mutmut_7() -> CiliumStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated agent or status value."""
    return CiliumStatusResult(
        installed=False,
        status="not_installed",
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=None,
    )


def x_not_installed_result__mutmut_8() -> CiliumStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated agent or status value."""
    return CiliumStatusResult(
        status="not_installed",
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_result__mutmut_9() -> CiliumStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated agent or status value."""
    return CiliumStatusResult(
        installed=False,
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_result__mutmut_10() -> CiliumStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated agent or status value."""
    return CiliumStatusResult(
        installed=False,
        status="not_installed",
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_result__mutmut_11() -> CiliumStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated agent or status value."""
    return CiliumStatusResult(
        installed=False,
        status="not_installed",
        ready_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_result__mutmut_12() -> CiliumStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated agent or status value."""
    return CiliumStatusResult(
        installed=False,
        status="not_installed",
        ready_agents=0,
        total_agents=0,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_result__mutmut_13() -> CiliumStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated agent or status value."""
    return CiliumStatusResult(
        installed=False,
        status="not_installed",
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        connectivity=None,
        nodes=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_result__mutmut_14() -> CiliumStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated agent or status value."""
    return CiliumStatusResult(
        installed=False,
        status="not_installed",
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        nodes=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_result__mutmut_15() -> CiliumStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated agent or status value."""
    return CiliumStatusResult(
        installed=False,
        status="not_installed",
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_result__mutmut_16() -> CiliumStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated agent or status value."""
    return CiliumStatusResult(
        installed=False,
        status="not_installed",
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        )


def x_not_installed_result__mutmut_17() -> CiliumStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated agent or status value."""
    return CiliumStatusResult(
        installed=True,
        status="not_installed",
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_result__mutmut_18() -> CiliumStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated agent or status value."""
    return CiliumStatusResult(
        installed=False,
        status="XXnot_installedXX",
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_result__mutmut_19() -> CiliumStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated agent or status value."""
    return CiliumStatusResult(
        installed=False,
        status="NOT_INSTALLED",
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_result__mutmut_20() -> CiliumStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated agent or status value."""
    return CiliumStatusResult(
        installed=False,
        status="not_installed",
        ready_agents=1,
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_result__mutmut_21() -> CiliumStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated agent or status value."""
    return CiliumStatusResult(
        installed=False,
        status="not_installed",
        ready_agents=0,
        total_agents=1,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=_NOT_INSTALLED_NOTE,
    )


def x_not_installed_result__mutmut_22() -> CiliumStatusResult:
    """Honest NOT_INSTALLED marker — no fabricated agent or status value."""
    return CiliumStatusResult(
        installed=False,
        status="not_installed",
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        controller_errors=1,
        connectivity=None,
        nodes=[],
        note=_NOT_INSTALLED_NOTE,
    )

mutants_x_not_installed_result__mutmut['_mutmut_orig'] = x_not_installed_result__mutmut_orig # type: ignore # mutmut generated
mutants_x_not_installed_result__mutmut['x_not_installed_result__mutmut_1'] = x_not_installed_result__mutmut_1 # type: ignore # mutmut generated
mutants_x_not_installed_result__mutmut['x_not_installed_result__mutmut_2'] = x_not_installed_result__mutmut_2 # type: ignore # mutmut generated
mutants_x_not_installed_result__mutmut['x_not_installed_result__mutmut_3'] = x_not_installed_result__mutmut_3 # type: ignore # mutmut generated
mutants_x_not_installed_result__mutmut['x_not_installed_result__mutmut_4'] = x_not_installed_result__mutmut_4 # type: ignore # mutmut generated
mutants_x_not_installed_result__mutmut['x_not_installed_result__mutmut_5'] = x_not_installed_result__mutmut_5 # type: ignore # mutmut generated
mutants_x_not_installed_result__mutmut['x_not_installed_result__mutmut_6'] = x_not_installed_result__mutmut_6 # type: ignore # mutmut generated
mutants_x_not_installed_result__mutmut['x_not_installed_result__mutmut_7'] = x_not_installed_result__mutmut_7 # type: ignore # mutmut generated
mutants_x_not_installed_result__mutmut['x_not_installed_result__mutmut_8'] = x_not_installed_result__mutmut_8 # type: ignore # mutmut generated
mutants_x_not_installed_result__mutmut['x_not_installed_result__mutmut_9'] = x_not_installed_result__mutmut_9 # type: ignore # mutmut generated
mutants_x_not_installed_result__mutmut['x_not_installed_result__mutmut_10'] = x_not_installed_result__mutmut_10 # type: ignore # mutmut generated
mutants_x_not_installed_result__mutmut['x_not_installed_result__mutmut_11'] = x_not_installed_result__mutmut_11 # type: ignore # mutmut generated
mutants_x_not_installed_result__mutmut['x_not_installed_result__mutmut_12'] = x_not_installed_result__mutmut_12 # type: ignore # mutmut generated
mutants_x_not_installed_result__mutmut['x_not_installed_result__mutmut_13'] = x_not_installed_result__mutmut_13 # type: ignore # mutmut generated
mutants_x_not_installed_result__mutmut['x_not_installed_result__mutmut_14'] = x_not_installed_result__mutmut_14 # type: ignore # mutmut generated
mutants_x_not_installed_result__mutmut['x_not_installed_result__mutmut_15'] = x_not_installed_result__mutmut_15 # type: ignore # mutmut generated
mutants_x_not_installed_result__mutmut['x_not_installed_result__mutmut_16'] = x_not_installed_result__mutmut_16 # type: ignore # mutmut generated
mutants_x_not_installed_result__mutmut['x_not_installed_result__mutmut_17'] = x_not_installed_result__mutmut_17 # type: ignore # mutmut generated
mutants_x_not_installed_result__mutmut['x_not_installed_result__mutmut_18'] = x_not_installed_result__mutmut_18 # type: ignore # mutmut generated
mutants_x_not_installed_result__mutmut['x_not_installed_result__mutmut_19'] = x_not_installed_result__mutmut_19 # type: ignore # mutmut generated
mutants_x_not_installed_result__mutmut['x_not_installed_result__mutmut_20'] = x_not_installed_result__mutmut_20 # type: ignore # mutmut generated
mutants_x_not_installed_result__mutmut['x_not_installed_result__mutmut_21'] = x_not_installed_result__mutmut_21 # type: ignore # mutmut generated
mutants_x_not_installed_result__mutmut['x_not_installed_result__mutmut_22'] = x_not_installed_result__mutmut_22 # type: ignore # mutmut generated
mutants_x_crds_only_result__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_crds_only_result__mutmut)
def crds_only_result(note: str | None = None) -> CiliumStatusResult:
    """Cilium CRDs present but no agent DaemonSet — unknown datapath health."""
    return CiliumStatusResult(
        installed=True,
        status="unknown",
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=note,
    )


def x_crds_only_result__mutmut_orig(note: str | None = None) -> CiliumStatusResult:
    """Cilium CRDs present but no agent DaemonSet — unknown datapath health."""
    return CiliumStatusResult(
        installed=True,
        status="unknown",
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=note,
    )


def x_crds_only_result__mutmut_1(note: str | None = None) -> CiliumStatusResult:
    """Cilium CRDs present but no agent DaemonSet — unknown datapath health."""
    return CiliumStatusResult(
        installed=None,
        status="unknown",
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=note,
    )


def x_crds_only_result__mutmut_2(note: str | None = None) -> CiliumStatusResult:
    """Cilium CRDs present but no agent DaemonSet — unknown datapath health."""
    return CiliumStatusResult(
        installed=True,
        status=None,
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=note,
    )


def x_crds_only_result__mutmut_3(note: str | None = None) -> CiliumStatusResult:
    """Cilium CRDs present but no agent DaemonSet — unknown datapath health."""
    return CiliumStatusResult(
        installed=True,
        status="unknown",
        ready_agents=None,
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=note,
    )


def x_crds_only_result__mutmut_4(note: str | None = None) -> CiliumStatusResult:
    """Cilium CRDs present but no agent DaemonSet — unknown datapath health."""
    return CiliumStatusResult(
        installed=True,
        status="unknown",
        ready_agents=0,
        total_agents=None,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=note,
    )


def x_crds_only_result__mutmut_5(note: str | None = None) -> CiliumStatusResult:
    """Cilium CRDs present but no agent DaemonSet — unknown datapath health."""
    return CiliumStatusResult(
        installed=True,
        status="unknown",
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        controller_errors=None,
        connectivity=None,
        nodes=[],
        note=note,
    )


def x_crds_only_result__mutmut_6(note: str | None = None) -> CiliumStatusResult:
    """Cilium CRDs present but no agent DaemonSet — unknown datapath health."""
    return CiliumStatusResult(
        installed=True,
        status="unknown",
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=None,
        note=note,
    )


def x_crds_only_result__mutmut_7(note: str | None = None) -> CiliumStatusResult:
    """Cilium CRDs present but no agent DaemonSet — unknown datapath health."""
    return CiliumStatusResult(
        installed=True,
        status="unknown",
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=None,
    )


def x_crds_only_result__mutmut_8(note: str | None = None) -> CiliumStatusResult:
    """Cilium CRDs present but no agent DaemonSet — unknown datapath health."""
    return CiliumStatusResult(
        status="unknown",
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=note,
    )


def x_crds_only_result__mutmut_9(note: str | None = None) -> CiliumStatusResult:
    """Cilium CRDs present but no agent DaemonSet — unknown datapath health."""
    return CiliumStatusResult(
        installed=True,
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=note,
    )


def x_crds_only_result__mutmut_10(note: str | None = None) -> CiliumStatusResult:
    """Cilium CRDs present but no agent DaemonSet — unknown datapath health."""
    return CiliumStatusResult(
        installed=True,
        status="unknown",
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=note,
    )


def x_crds_only_result__mutmut_11(note: str | None = None) -> CiliumStatusResult:
    """Cilium CRDs present but no agent DaemonSet — unknown datapath health."""
    return CiliumStatusResult(
        installed=True,
        status="unknown",
        ready_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=note,
    )


def x_crds_only_result__mutmut_12(note: str | None = None) -> CiliumStatusResult:
    """Cilium CRDs present but no agent DaemonSet — unknown datapath health."""
    return CiliumStatusResult(
        installed=True,
        status="unknown",
        ready_agents=0,
        total_agents=0,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=note,
    )


def x_crds_only_result__mutmut_13(note: str | None = None) -> CiliumStatusResult:
    """Cilium CRDs present but no agent DaemonSet — unknown datapath health."""
    return CiliumStatusResult(
        installed=True,
        status="unknown",
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        connectivity=None,
        nodes=[],
        note=note,
    )


def x_crds_only_result__mutmut_14(note: str | None = None) -> CiliumStatusResult:
    """Cilium CRDs present but no agent DaemonSet — unknown datapath health."""
    return CiliumStatusResult(
        installed=True,
        status="unknown",
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        nodes=[],
        note=note,
    )


def x_crds_only_result__mutmut_15(note: str | None = None) -> CiliumStatusResult:
    """Cilium CRDs present but no agent DaemonSet — unknown datapath health."""
    return CiliumStatusResult(
        installed=True,
        status="unknown",
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        note=note,
    )


def x_crds_only_result__mutmut_16(note: str | None = None) -> CiliumStatusResult:
    """Cilium CRDs present but no agent DaemonSet — unknown datapath health."""
    return CiliumStatusResult(
        installed=True,
        status="unknown",
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        )


def x_crds_only_result__mutmut_17(note: str | None = None) -> CiliumStatusResult:
    """Cilium CRDs present but no agent DaemonSet — unknown datapath health."""
    return CiliumStatusResult(
        installed=False,
        status="unknown",
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=note,
    )


def x_crds_only_result__mutmut_18(note: str | None = None) -> CiliumStatusResult:
    """Cilium CRDs present but no agent DaemonSet — unknown datapath health."""
    return CiliumStatusResult(
        installed=True,
        status="XXunknownXX",
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=note,
    )


def x_crds_only_result__mutmut_19(note: str | None = None) -> CiliumStatusResult:
    """Cilium CRDs present but no agent DaemonSet — unknown datapath health."""
    return CiliumStatusResult(
        installed=True,
        status="UNKNOWN",
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=note,
    )


def x_crds_only_result__mutmut_20(note: str | None = None) -> CiliumStatusResult:
    """Cilium CRDs present but no agent DaemonSet — unknown datapath health."""
    return CiliumStatusResult(
        installed=True,
        status="unknown",
        ready_agents=1,
        total_agents=0,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=note,
    )


def x_crds_only_result__mutmut_21(note: str | None = None) -> CiliumStatusResult:
    """Cilium CRDs present but no agent DaemonSet — unknown datapath health."""
    return CiliumStatusResult(
        installed=True,
        status="unknown",
        ready_agents=0,
        total_agents=1,
        degraded_summary=None,
        controller_errors=0,
        connectivity=None,
        nodes=[],
        note=note,
    )


def x_crds_only_result__mutmut_22(note: str | None = None) -> CiliumStatusResult:
    """Cilium CRDs present but no agent DaemonSet — unknown datapath health."""
    return CiliumStatusResult(
        installed=True,
        status="unknown",
        ready_agents=0,
        total_agents=0,
        degraded_summary=None,
        controller_errors=1,
        connectivity=None,
        nodes=[],
        note=note,
    )

mutants_x_crds_only_result__mutmut['_mutmut_orig'] = x_crds_only_result__mutmut_orig # type: ignore # mutmut generated
mutants_x_crds_only_result__mutmut['x_crds_only_result__mutmut_1'] = x_crds_only_result__mutmut_1 # type: ignore # mutmut generated
mutants_x_crds_only_result__mutmut['x_crds_only_result__mutmut_2'] = x_crds_only_result__mutmut_2 # type: ignore # mutmut generated
mutants_x_crds_only_result__mutmut['x_crds_only_result__mutmut_3'] = x_crds_only_result__mutmut_3 # type: ignore # mutmut generated
mutants_x_crds_only_result__mutmut['x_crds_only_result__mutmut_4'] = x_crds_only_result__mutmut_4 # type: ignore # mutmut generated
mutants_x_crds_only_result__mutmut['x_crds_only_result__mutmut_5'] = x_crds_only_result__mutmut_5 # type: ignore # mutmut generated
mutants_x_crds_only_result__mutmut['x_crds_only_result__mutmut_6'] = x_crds_only_result__mutmut_6 # type: ignore # mutmut generated
mutants_x_crds_only_result__mutmut['x_crds_only_result__mutmut_7'] = x_crds_only_result__mutmut_7 # type: ignore # mutmut generated
mutants_x_crds_only_result__mutmut['x_crds_only_result__mutmut_8'] = x_crds_only_result__mutmut_8 # type: ignore # mutmut generated
mutants_x_crds_only_result__mutmut['x_crds_only_result__mutmut_9'] = x_crds_only_result__mutmut_9 # type: ignore # mutmut generated
mutants_x_crds_only_result__mutmut['x_crds_only_result__mutmut_10'] = x_crds_only_result__mutmut_10 # type: ignore # mutmut generated
mutants_x_crds_only_result__mutmut['x_crds_only_result__mutmut_11'] = x_crds_only_result__mutmut_11 # type: ignore # mutmut generated
mutants_x_crds_only_result__mutmut['x_crds_only_result__mutmut_12'] = x_crds_only_result__mutmut_12 # type: ignore # mutmut generated
mutants_x_crds_only_result__mutmut['x_crds_only_result__mutmut_13'] = x_crds_only_result__mutmut_13 # type: ignore # mutmut generated
mutants_x_crds_only_result__mutmut['x_crds_only_result__mutmut_14'] = x_crds_only_result__mutmut_14 # type: ignore # mutmut generated
mutants_x_crds_only_result__mutmut['x_crds_only_result__mutmut_15'] = x_crds_only_result__mutmut_15 # type: ignore # mutmut generated
mutants_x_crds_only_result__mutmut['x_crds_only_result__mutmut_16'] = x_crds_only_result__mutmut_16 # type: ignore # mutmut generated
mutants_x_crds_only_result__mutmut['x_crds_only_result__mutmut_17'] = x_crds_only_result__mutmut_17 # type: ignore # mutmut generated
mutants_x_crds_only_result__mutmut['x_crds_only_result__mutmut_18'] = x_crds_only_result__mutmut_18 # type: ignore # mutmut generated
mutants_x_crds_only_result__mutmut['x_crds_only_result__mutmut_19'] = x_crds_only_result__mutmut_19 # type: ignore # mutmut generated
mutants_x_crds_only_result__mutmut['x_crds_only_result__mutmut_20'] = x_crds_only_result__mutmut_20 # type: ignore # mutmut generated
mutants_x_crds_only_result__mutmut['x_crds_only_result__mutmut_21'] = x_crds_only_result__mutmut_21 # type: ignore # mutmut generated
mutants_x_crds_only_result__mutmut['x_crds_only_result__mutmut_22'] = x_crds_only_result__mutmut_22 # type: ignore # mutmut generated
