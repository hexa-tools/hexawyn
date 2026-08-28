"""Pure Cilium datapath status classification — no infra imports."""

from __future__ import annotations

from hexawyn.domain.models.cilium import CiliumAgentHealth, CiliumStatusResult

_NOT_INSTALLED_NOTE = "Cilium is not installed in this cluster"


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
