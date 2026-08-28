"""Pure Calico connectivity health — no infrastructure imports.

Aggregates the observed per-node calico-node readiness into a global verdict
and derives the tunnel/BGP state summaries honestly from the dataplane mode and
agent health. A healthy verdict is never invented: it requires every observed
calico-node agent to be ready, and unknown tunnel/BGP states are reported as
UNKNOWN rather than guessed.
"""

from __future__ import annotations

from collections.abc import Mapping

from hexawyn.domain.models.calico import (
    NOT_INSTALLED_MARKER,
    CalicoConnectivityHealthResult,
    CalicoDetectionResult,
    CalicoNodeConnectivity,
    DataplaneMode,
)

_TUNNEL_BY_MODE: dict[DataplaneMode, str] = {
    DataplaneMode.IPIP: "IPIP tunnel",
    DataplaneMode.VXLAN: "VXLAN tunnel",
    DataplaneMode.EBPF: "eBPF dataplane (no IPIP/VXLAN tunnel)",
}
_UNKNOWN = "UNKNOWN"


def build_calico_connectivity_health(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
) -> CalicoConnectivityHealthResult:
    """Compose the Calico dataplane connectivity verdict."""
    if not detection.installed:
        return CalicoConnectivityHealthResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            verdict="unknown",
            ready_agents=0,
            total_agents=0,
            dataplane_mode=None,
            tunnel_summary=_UNKNOWN,
            bgp_summary=_UNKNOWN,
            connectivity_probe=None,
            nodes=[],
            degraded_nodes=[],
            summary=None,
            error=detection.error,
        )

    nodes = [
        CalicoNodeConnectivity(node=agent.node, ready=agent.healthy) for agent in detection.agents
    ]
    ready = sum(1 for node in nodes if node.ready)
    total = len(nodes)
    degraded_nodes = [node.node for node in nodes if not node.ready]

    if total == 0:
        verdict = "unknown"
    elif ready == total:
        verdict = "healthy"
    else:
        verdict = "degraded"

    tunnel_summary = _tunnel_summary(detection.mode)
    bgp_summary = _bgp_summary(ready, total)
    probe = (
        str(connectivity.get("status"))
        if connectivity.get("available") and connectivity.get("status") is not None
        else None
    )

    return CalicoConnectivityHealthResult(
        installed=True,
        not_installed_marker=None,
        verdict=verdict,
        ready_agents=ready,
        total_agents=total,
        dataplane_mode=detection.mode,
        tunnel_summary=tunnel_summary,
        bgp_summary=bgp_summary,
        connectivity_probe=probe,
        nodes=nodes,
        degraded_nodes=degraded_nodes,
        summary=_summary(verdict, ready, total),
        error=detection.error,
    )


def _tunnel_summary(mode: DataplaneMode | None) -> str:
    if mode is None:
        return _UNKNOWN
    return _TUNNEL_BY_MODE.get(mode, _UNKNOWN)


def _bgp_summary(ready: int, total: int) -> str:
    if total == 0:
        return f"{_UNKNOWN} — no calico-node agents observed"
    if ready == total:
        return "BGP node-to-node mesh reachable (all calico-node agents ready)"
    degraded = total - ready
    return f"{degraded} calico-node agent(s) degraded — BGP sessions may be affected"


def _summary(verdict: str, ready: int, total: int) -> str:
    return f"Calico dataplane {verdict}: {ready}/{total} calico-node agents ready"
