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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_calico_connectivity_health__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_calico_connectivity_health__mutmut)
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


def x_build_calico_connectivity_health__mutmut_orig(
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


def x_build_calico_connectivity_health__mutmut_1(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
) -> CalicoConnectivityHealthResult:
    """Compose the Calico dataplane connectivity verdict."""
    if detection.installed:
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


def x_build_calico_connectivity_health__mutmut_2(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
) -> CalicoConnectivityHealthResult:
    """Compose the Calico dataplane connectivity verdict."""
    if not detection.installed:
        return CalicoConnectivityHealthResult(
            installed=None,
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


def x_build_calico_connectivity_health__mutmut_3(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
) -> CalicoConnectivityHealthResult:
    """Compose the Calico dataplane connectivity verdict."""
    if not detection.installed:
        return CalicoConnectivityHealthResult(
            installed=False,
            not_installed_marker=None,
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


def x_build_calico_connectivity_health__mutmut_4(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
) -> CalicoConnectivityHealthResult:
    """Compose the Calico dataplane connectivity verdict."""
    if not detection.installed:
        return CalicoConnectivityHealthResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            verdict=None,
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


def x_build_calico_connectivity_health__mutmut_5(
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
            ready_agents=None,
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


def x_build_calico_connectivity_health__mutmut_6(
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
            total_agents=None,
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


def x_build_calico_connectivity_health__mutmut_7(
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
            tunnel_summary=None,
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


def x_build_calico_connectivity_health__mutmut_8(
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
            bgp_summary=None,
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


def x_build_calico_connectivity_health__mutmut_9(
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
            nodes=None,
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


def x_build_calico_connectivity_health__mutmut_10(
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
            degraded_nodes=None,
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


def x_build_calico_connectivity_health__mutmut_11(
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
            error=None,
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


def x_build_calico_connectivity_health__mutmut_12(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
) -> CalicoConnectivityHealthResult:
    """Compose the Calico dataplane connectivity verdict."""
    if not detection.installed:
        return CalicoConnectivityHealthResult(
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


def x_build_calico_connectivity_health__mutmut_13(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
) -> CalicoConnectivityHealthResult:
    """Compose the Calico dataplane connectivity verdict."""
    if not detection.installed:
        return CalicoConnectivityHealthResult(
            installed=False,
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


def x_build_calico_connectivity_health__mutmut_14(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
) -> CalicoConnectivityHealthResult:
    """Compose the Calico dataplane connectivity verdict."""
    if not detection.installed:
        return CalicoConnectivityHealthResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
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


def x_build_calico_connectivity_health__mutmut_15(
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


def x_build_calico_connectivity_health__mutmut_16(
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


def x_build_calico_connectivity_health__mutmut_17(
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


def x_build_calico_connectivity_health__mutmut_18(
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


def x_build_calico_connectivity_health__mutmut_19(
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


def x_build_calico_connectivity_health__mutmut_20(
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


def x_build_calico_connectivity_health__mutmut_21(
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


def x_build_calico_connectivity_health__mutmut_22(
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


def x_build_calico_connectivity_health__mutmut_23(
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


def x_build_calico_connectivity_health__mutmut_24(
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


def x_build_calico_connectivity_health__mutmut_25(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
) -> CalicoConnectivityHealthResult:
    """Compose the Calico dataplane connectivity verdict."""
    if not detection.installed:
        return CalicoConnectivityHealthResult(
            installed=True,
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


def x_build_calico_connectivity_health__mutmut_26(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
) -> CalicoConnectivityHealthResult:
    """Compose the Calico dataplane connectivity verdict."""
    if not detection.installed:
        return CalicoConnectivityHealthResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            verdict="XXunknownXX",
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


def x_build_calico_connectivity_health__mutmut_27(
    *,
    detection: CalicoDetectionResult,
    connectivity: Mapping[str, object],
) -> CalicoConnectivityHealthResult:
    """Compose the Calico dataplane connectivity verdict."""
    if not detection.installed:
        return CalicoConnectivityHealthResult(
            installed=False,
            not_installed_marker=NOT_INSTALLED_MARKER,
            verdict="UNKNOWN",
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


def x_build_calico_connectivity_health__mutmut_28(
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
            ready_agents=1,
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


def x_build_calico_connectivity_health__mutmut_29(
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
            total_agents=1,
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


def x_build_calico_connectivity_health__mutmut_30(
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

    nodes = None
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


def x_build_calico_connectivity_health__mutmut_31(
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
        CalicoNodeConnectivity(node=None, ready=agent.healthy) for agent in detection.agents
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


def x_build_calico_connectivity_health__mutmut_32(
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
        CalicoNodeConnectivity(node=agent.node, ready=None) for agent in detection.agents
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


def x_build_calico_connectivity_health__mutmut_33(
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
        CalicoNodeConnectivity(ready=agent.healthy) for agent in detection.agents
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


def x_build_calico_connectivity_health__mutmut_34(
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
        CalicoNodeConnectivity(node=agent.node, ) for agent in detection.agents
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


def x_build_calico_connectivity_health__mutmut_35(
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
    ready = None
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


def x_build_calico_connectivity_health__mutmut_36(
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
    ready = sum(None)
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


def x_build_calico_connectivity_health__mutmut_37(
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
    ready = sum(2 for node in nodes if node.ready)
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


def x_build_calico_connectivity_health__mutmut_38(
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
    total = None
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


def x_build_calico_connectivity_health__mutmut_39(
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
    degraded_nodes = None

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


def x_build_calico_connectivity_health__mutmut_40(
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
    degraded_nodes = [node.node for node in nodes if node.ready]

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


def x_build_calico_connectivity_health__mutmut_41(
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

    if total != 0:
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


def x_build_calico_connectivity_health__mutmut_42(
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

    if total == 1:
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


def x_build_calico_connectivity_health__mutmut_43(
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
        verdict = None
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


def x_build_calico_connectivity_health__mutmut_44(
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
        verdict = "XXunknownXX"
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


def x_build_calico_connectivity_health__mutmut_45(
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
        verdict = "UNKNOWN"
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


def x_build_calico_connectivity_health__mutmut_46(
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
    elif ready != total:
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


def x_build_calico_connectivity_health__mutmut_47(
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
        verdict = None
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


def x_build_calico_connectivity_health__mutmut_48(
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
        verdict = "XXhealthyXX"
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


def x_build_calico_connectivity_health__mutmut_49(
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
        verdict = "HEALTHY"
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


def x_build_calico_connectivity_health__mutmut_50(
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
        verdict = None

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


def x_build_calico_connectivity_health__mutmut_51(
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
        verdict = "XXdegradedXX"

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


def x_build_calico_connectivity_health__mutmut_52(
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
        verdict = "DEGRADED"

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


def x_build_calico_connectivity_health__mutmut_53(
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

    tunnel_summary = None
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


def x_build_calico_connectivity_health__mutmut_54(
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

    tunnel_summary = _tunnel_summary(None)
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


def x_build_calico_connectivity_health__mutmut_55(
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
    bgp_summary = None
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


def x_build_calico_connectivity_health__mutmut_56(
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
    bgp_summary = _bgp_summary(None, total)
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


def x_build_calico_connectivity_health__mutmut_57(
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
    bgp_summary = _bgp_summary(ready, None)
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


def x_build_calico_connectivity_health__mutmut_58(
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
    bgp_summary = _bgp_summary(total)
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


def x_build_calico_connectivity_health__mutmut_59(
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
    bgp_summary = _bgp_summary(ready, )
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


def x_build_calico_connectivity_health__mutmut_60(
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
    probe = None

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


def x_build_calico_connectivity_health__mutmut_61(
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
        str(None)
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


def x_build_calico_connectivity_health__mutmut_62(
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
        str(connectivity.get(None))
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


def x_build_calico_connectivity_health__mutmut_63(
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
        str(connectivity.get("XXstatusXX"))
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


def x_build_calico_connectivity_health__mutmut_64(
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
        str(connectivity.get("STATUS"))
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


def x_build_calico_connectivity_health__mutmut_65(
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
        if connectivity.get("available") or connectivity.get("status") is not None
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


def x_build_calico_connectivity_health__mutmut_66(
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
        if connectivity.get(None) and connectivity.get("status") is not None
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


def x_build_calico_connectivity_health__mutmut_67(
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
        if connectivity.get("XXavailableXX") and connectivity.get("status") is not None
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


def x_build_calico_connectivity_health__mutmut_68(
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
        if connectivity.get("AVAILABLE") and connectivity.get("status") is not None
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


def x_build_calico_connectivity_health__mutmut_69(
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
        if connectivity.get("available") and connectivity.get(None) is not None
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


def x_build_calico_connectivity_health__mutmut_70(
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
        if connectivity.get("available") and connectivity.get("XXstatusXX") is not None
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


def x_build_calico_connectivity_health__mutmut_71(
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
        if connectivity.get("available") and connectivity.get("STATUS") is not None
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


def x_build_calico_connectivity_health__mutmut_72(
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
        if connectivity.get("available") and connectivity.get("status") is None
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


def x_build_calico_connectivity_health__mutmut_73(
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
        installed=None,
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


def x_build_calico_connectivity_health__mutmut_74(
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
        verdict=None,
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


def x_build_calico_connectivity_health__mutmut_75(
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
        ready_agents=None,
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


def x_build_calico_connectivity_health__mutmut_76(
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
        total_agents=None,
        dataplane_mode=detection.mode,
        tunnel_summary=tunnel_summary,
        bgp_summary=bgp_summary,
        connectivity_probe=probe,
        nodes=nodes,
        degraded_nodes=degraded_nodes,
        summary=_summary(verdict, ready, total),
        error=detection.error,
    )


def x_build_calico_connectivity_health__mutmut_77(
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
        dataplane_mode=None,
        tunnel_summary=tunnel_summary,
        bgp_summary=bgp_summary,
        connectivity_probe=probe,
        nodes=nodes,
        degraded_nodes=degraded_nodes,
        summary=_summary(verdict, ready, total),
        error=detection.error,
    )


def x_build_calico_connectivity_health__mutmut_78(
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
        tunnel_summary=None,
        bgp_summary=bgp_summary,
        connectivity_probe=probe,
        nodes=nodes,
        degraded_nodes=degraded_nodes,
        summary=_summary(verdict, ready, total),
        error=detection.error,
    )


def x_build_calico_connectivity_health__mutmut_79(
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
        bgp_summary=None,
        connectivity_probe=probe,
        nodes=nodes,
        degraded_nodes=degraded_nodes,
        summary=_summary(verdict, ready, total),
        error=detection.error,
    )


def x_build_calico_connectivity_health__mutmut_80(
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
        connectivity_probe=None,
        nodes=nodes,
        degraded_nodes=degraded_nodes,
        summary=_summary(verdict, ready, total),
        error=detection.error,
    )


def x_build_calico_connectivity_health__mutmut_81(
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
        nodes=None,
        degraded_nodes=degraded_nodes,
        summary=_summary(verdict, ready, total),
        error=detection.error,
    )


def x_build_calico_connectivity_health__mutmut_82(
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
        degraded_nodes=None,
        summary=_summary(verdict, ready, total),
        error=detection.error,
    )


def x_build_calico_connectivity_health__mutmut_83(
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
        summary=None,
        error=detection.error,
    )


def x_build_calico_connectivity_health__mutmut_84(
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
        error=None,
    )


def x_build_calico_connectivity_health__mutmut_85(
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


def x_build_calico_connectivity_health__mutmut_86(
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


def x_build_calico_connectivity_health__mutmut_87(
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


def x_build_calico_connectivity_health__mutmut_88(
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


def x_build_calico_connectivity_health__mutmut_89(
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
        dataplane_mode=detection.mode,
        tunnel_summary=tunnel_summary,
        bgp_summary=bgp_summary,
        connectivity_probe=probe,
        nodes=nodes,
        degraded_nodes=degraded_nodes,
        summary=_summary(verdict, ready, total),
        error=detection.error,
    )


def x_build_calico_connectivity_health__mutmut_90(
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
        tunnel_summary=tunnel_summary,
        bgp_summary=bgp_summary,
        connectivity_probe=probe,
        nodes=nodes,
        degraded_nodes=degraded_nodes,
        summary=_summary(verdict, ready, total),
        error=detection.error,
    )


def x_build_calico_connectivity_health__mutmut_91(
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
        bgp_summary=bgp_summary,
        connectivity_probe=probe,
        nodes=nodes,
        degraded_nodes=degraded_nodes,
        summary=_summary(verdict, ready, total),
        error=detection.error,
    )


def x_build_calico_connectivity_health__mutmut_92(
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
        connectivity_probe=probe,
        nodes=nodes,
        degraded_nodes=degraded_nodes,
        summary=_summary(verdict, ready, total),
        error=detection.error,
    )


def x_build_calico_connectivity_health__mutmut_93(
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
        nodes=nodes,
        degraded_nodes=degraded_nodes,
        summary=_summary(verdict, ready, total),
        error=detection.error,
    )


def x_build_calico_connectivity_health__mutmut_94(
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
        degraded_nodes=degraded_nodes,
        summary=_summary(verdict, ready, total),
        error=detection.error,
    )


def x_build_calico_connectivity_health__mutmut_95(
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
        summary=_summary(verdict, ready, total),
        error=detection.error,
    )


def x_build_calico_connectivity_health__mutmut_96(
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
        error=detection.error,
    )


def x_build_calico_connectivity_health__mutmut_97(
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
        )


def x_build_calico_connectivity_health__mutmut_98(
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
        installed=False,
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


def x_build_calico_connectivity_health__mutmut_99(
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
        summary=_summary(None, ready, total),
        error=detection.error,
    )


def x_build_calico_connectivity_health__mutmut_100(
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
        summary=_summary(verdict, None, total),
        error=detection.error,
    )


def x_build_calico_connectivity_health__mutmut_101(
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
        summary=_summary(verdict, ready, None),
        error=detection.error,
    )


def x_build_calico_connectivity_health__mutmut_102(
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
        summary=_summary(ready, total),
        error=detection.error,
    )


def x_build_calico_connectivity_health__mutmut_103(
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
        summary=_summary(verdict, total),
        error=detection.error,
    )


def x_build_calico_connectivity_health__mutmut_104(
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
        summary=_summary(verdict, ready, ),
        error=detection.error,
    )

mutants_x_build_calico_connectivity_health__mutmut['_mutmut_orig'] = x_build_calico_connectivity_health__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_1'] = x_build_calico_connectivity_health__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_2'] = x_build_calico_connectivity_health__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_3'] = x_build_calico_connectivity_health__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_4'] = x_build_calico_connectivity_health__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_5'] = x_build_calico_connectivity_health__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_6'] = x_build_calico_connectivity_health__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_7'] = x_build_calico_connectivity_health__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_8'] = x_build_calico_connectivity_health__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_9'] = x_build_calico_connectivity_health__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_10'] = x_build_calico_connectivity_health__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_11'] = x_build_calico_connectivity_health__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_12'] = x_build_calico_connectivity_health__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_13'] = x_build_calico_connectivity_health__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_14'] = x_build_calico_connectivity_health__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_15'] = x_build_calico_connectivity_health__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_16'] = x_build_calico_connectivity_health__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_17'] = x_build_calico_connectivity_health__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_18'] = x_build_calico_connectivity_health__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_19'] = x_build_calico_connectivity_health__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_20'] = x_build_calico_connectivity_health__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_21'] = x_build_calico_connectivity_health__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_22'] = x_build_calico_connectivity_health__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_23'] = x_build_calico_connectivity_health__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_24'] = x_build_calico_connectivity_health__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_25'] = x_build_calico_connectivity_health__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_26'] = x_build_calico_connectivity_health__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_27'] = x_build_calico_connectivity_health__mutmut_27 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_28'] = x_build_calico_connectivity_health__mutmut_28 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_29'] = x_build_calico_connectivity_health__mutmut_29 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_30'] = x_build_calico_connectivity_health__mutmut_30 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_31'] = x_build_calico_connectivity_health__mutmut_31 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_32'] = x_build_calico_connectivity_health__mutmut_32 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_33'] = x_build_calico_connectivity_health__mutmut_33 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_34'] = x_build_calico_connectivity_health__mutmut_34 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_35'] = x_build_calico_connectivity_health__mutmut_35 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_36'] = x_build_calico_connectivity_health__mutmut_36 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_37'] = x_build_calico_connectivity_health__mutmut_37 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_38'] = x_build_calico_connectivity_health__mutmut_38 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_39'] = x_build_calico_connectivity_health__mutmut_39 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_40'] = x_build_calico_connectivity_health__mutmut_40 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_41'] = x_build_calico_connectivity_health__mutmut_41 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_42'] = x_build_calico_connectivity_health__mutmut_42 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_43'] = x_build_calico_connectivity_health__mutmut_43 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_44'] = x_build_calico_connectivity_health__mutmut_44 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_45'] = x_build_calico_connectivity_health__mutmut_45 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_46'] = x_build_calico_connectivity_health__mutmut_46 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_47'] = x_build_calico_connectivity_health__mutmut_47 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_48'] = x_build_calico_connectivity_health__mutmut_48 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_49'] = x_build_calico_connectivity_health__mutmut_49 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_50'] = x_build_calico_connectivity_health__mutmut_50 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_51'] = x_build_calico_connectivity_health__mutmut_51 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_52'] = x_build_calico_connectivity_health__mutmut_52 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_53'] = x_build_calico_connectivity_health__mutmut_53 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_54'] = x_build_calico_connectivity_health__mutmut_54 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_55'] = x_build_calico_connectivity_health__mutmut_55 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_56'] = x_build_calico_connectivity_health__mutmut_56 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_57'] = x_build_calico_connectivity_health__mutmut_57 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_58'] = x_build_calico_connectivity_health__mutmut_58 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_59'] = x_build_calico_connectivity_health__mutmut_59 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_60'] = x_build_calico_connectivity_health__mutmut_60 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_61'] = x_build_calico_connectivity_health__mutmut_61 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_62'] = x_build_calico_connectivity_health__mutmut_62 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_63'] = x_build_calico_connectivity_health__mutmut_63 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_64'] = x_build_calico_connectivity_health__mutmut_64 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_65'] = x_build_calico_connectivity_health__mutmut_65 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_66'] = x_build_calico_connectivity_health__mutmut_66 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_67'] = x_build_calico_connectivity_health__mutmut_67 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_68'] = x_build_calico_connectivity_health__mutmut_68 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_69'] = x_build_calico_connectivity_health__mutmut_69 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_70'] = x_build_calico_connectivity_health__mutmut_70 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_71'] = x_build_calico_connectivity_health__mutmut_71 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_72'] = x_build_calico_connectivity_health__mutmut_72 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_73'] = x_build_calico_connectivity_health__mutmut_73 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_74'] = x_build_calico_connectivity_health__mutmut_74 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_75'] = x_build_calico_connectivity_health__mutmut_75 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_76'] = x_build_calico_connectivity_health__mutmut_76 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_77'] = x_build_calico_connectivity_health__mutmut_77 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_78'] = x_build_calico_connectivity_health__mutmut_78 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_79'] = x_build_calico_connectivity_health__mutmut_79 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_80'] = x_build_calico_connectivity_health__mutmut_80 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_81'] = x_build_calico_connectivity_health__mutmut_81 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_82'] = x_build_calico_connectivity_health__mutmut_82 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_83'] = x_build_calico_connectivity_health__mutmut_83 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_84'] = x_build_calico_connectivity_health__mutmut_84 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_85'] = x_build_calico_connectivity_health__mutmut_85 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_86'] = x_build_calico_connectivity_health__mutmut_86 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_87'] = x_build_calico_connectivity_health__mutmut_87 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_88'] = x_build_calico_connectivity_health__mutmut_88 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_89'] = x_build_calico_connectivity_health__mutmut_89 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_90'] = x_build_calico_connectivity_health__mutmut_90 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_91'] = x_build_calico_connectivity_health__mutmut_91 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_92'] = x_build_calico_connectivity_health__mutmut_92 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_93'] = x_build_calico_connectivity_health__mutmut_93 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_94'] = x_build_calico_connectivity_health__mutmut_94 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_95'] = x_build_calico_connectivity_health__mutmut_95 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_96'] = x_build_calico_connectivity_health__mutmut_96 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_97'] = x_build_calico_connectivity_health__mutmut_97 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_98'] = x_build_calico_connectivity_health__mutmut_98 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_99'] = x_build_calico_connectivity_health__mutmut_99 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_100'] = x_build_calico_connectivity_health__mutmut_100 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_101'] = x_build_calico_connectivity_health__mutmut_101 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_102'] = x_build_calico_connectivity_health__mutmut_102 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_103'] = x_build_calico_connectivity_health__mutmut_103 # type: ignore # mutmut generated
mutants_x_build_calico_connectivity_health__mutmut['x_build_calico_connectivity_health__mutmut_104'] = x_build_calico_connectivity_health__mutmut_104 # type: ignore # mutmut generated
mutants_x__tunnel_summary__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__tunnel_summary__mutmut)
def _tunnel_summary(mode: DataplaneMode | None) -> str:
    if mode is None:
        return _UNKNOWN
    return _TUNNEL_BY_MODE.get(mode, _UNKNOWN)


def x__tunnel_summary__mutmut_orig(mode: DataplaneMode | None) -> str:
    if mode is None:
        return _UNKNOWN
    return _TUNNEL_BY_MODE.get(mode, _UNKNOWN)


def x__tunnel_summary__mutmut_1(mode: DataplaneMode | None) -> str:
    if mode is not None:
        return _UNKNOWN
    return _TUNNEL_BY_MODE.get(mode, _UNKNOWN)


def x__tunnel_summary__mutmut_2(mode: DataplaneMode | None) -> str:
    if mode is None:
        return _UNKNOWN
    return _TUNNEL_BY_MODE.get(None, _UNKNOWN)


def x__tunnel_summary__mutmut_3(mode: DataplaneMode | None) -> str:
    if mode is None:
        return _UNKNOWN
    return _TUNNEL_BY_MODE.get(mode, None)


def x__tunnel_summary__mutmut_4(mode: DataplaneMode | None) -> str:
    if mode is None:
        return _UNKNOWN
    return _TUNNEL_BY_MODE.get(_UNKNOWN)


def x__tunnel_summary__mutmut_5(mode: DataplaneMode | None) -> str:
    if mode is None:
        return _UNKNOWN
    return _TUNNEL_BY_MODE.get(mode, )

mutants_x__tunnel_summary__mutmut['_mutmut_orig'] = x__tunnel_summary__mutmut_orig # type: ignore # mutmut generated
mutants_x__tunnel_summary__mutmut['x__tunnel_summary__mutmut_1'] = x__tunnel_summary__mutmut_1 # type: ignore # mutmut generated
mutants_x__tunnel_summary__mutmut['x__tunnel_summary__mutmut_2'] = x__tunnel_summary__mutmut_2 # type: ignore # mutmut generated
mutants_x__tunnel_summary__mutmut['x__tunnel_summary__mutmut_3'] = x__tunnel_summary__mutmut_3 # type: ignore # mutmut generated
mutants_x__tunnel_summary__mutmut['x__tunnel_summary__mutmut_4'] = x__tunnel_summary__mutmut_4 # type: ignore # mutmut generated
mutants_x__tunnel_summary__mutmut['x__tunnel_summary__mutmut_5'] = x__tunnel_summary__mutmut_5 # type: ignore # mutmut generated
mutants_x__bgp_summary__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__bgp_summary__mutmut)
def _bgp_summary(ready: int, total: int) -> str:
    if total == 0:
        return f"{_UNKNOWN} — no calico-node agents observed"
    if ready == total:
        return "BGP node-to-node mesh reachable (all calico-node agents ready)"
    degraded = total - ready
    return f"{degraded} calico-node agent(s) degraded — BGP sessions may be affected"


def x__bgp_summary__mutmut_orig(ready: int, total: int) -> str:
    if total == 0:
        return f"{_UNKNOWN} — no calico-node agents observed"
    if ready == total:
        return "BGP node-to-node mesh reachable (all calico-node agents ready)"
    degraded = total - ready
    return f"{degraded} calico-node agent(s) degraded — BGP sessions may be affected"


def x__bgp_summary__mutmut_1(ready: int, total: int) -> str:
    if total != 0:
        return f"{_UNKNOWN} — no calico-node agents observed"
    if ready == total:
        return "BGP node-to-node mesh reachable (all calico-node agents ready)"
    degraded = total - ready
    return f"{degraded} calico-node agent(s) degraded — BGP sessions may be affected"


def x__bgp_summary__mutmut_2(ready: int, total: int) -> str:
    if total == 1:
        return f"{_UNKNOWN} — no calico-node agents observed"
    if ready == total:
        return "BGP node-to-node mesh reachable (all calico-node agents ready)"
    degraded = total - ready
    return f"{degraded} calico-node agent(s) degraded — BGP sessions may be affected"


def x__bgp_summary__mutmut_3(ready: int, total: int) -> str:
    if total == 0:
        return f"{_UNKNOWN} — no calico-node agents observed"
    if ready != total:
        return "BGP node-to-node mesh reachable (all calico-node agents ready)"
    degraded = total - ready
    return f"{degraded} calico-node agent(s) degraded — BGP sessions may be affected"


def x__bgp_summary__mutmut_4(ready: int, total: int) -> str:
    if total == 0:
        return f"{_UNKNOWN} — no calico-node agents observed"
    if ready == total:
        return "XXBGP node-to-node mesh reachable (all calico-node agents ready)XX"
    degraded = total - ready
    return f"{degraded} calico-node agent(s) degraded — BGP sessions may be affected"


def x__bgp_summary__mutmut_5(ready: int, total: int) -> str:
    if total == 0:
        return f"{_UNKNOWN} — no calico-node agents observed"
    if ready == total:
        return "bgp node-to-node mesh reachable (all calico-node agents ready)"
    degraded = total - ready
    return f"{degraded} calico-node agent(s) degraded — BGP sessions may be affected"


def x__bgp_summary__mutmut_6(ready: int, total: int) -> str:
    if total == 0:
        return f"{_UNKNOWN} — no calico-node agents observed"
    if ready == total:
        return "BGP NODE-TO-NODE MESH REACHABLE (ALL CALICO-NODE AGENTS READY)"
    degraded = total - ready
    return f"{degraded} calico-node agent(s) degraded — BGP sessions may be affected"


def x__bgp_summary__mutmut_7(ready: int, total: int) -> str:
    if total == 0:
        return f"{_UNKNOWN} — no calico-node agents observed"
    if ready == total:
        return "BGP node-to-node mesh reachable (all calico-node agents ready)"
    degraded = None
    return f"{degraded} calico-node agent(s) degraded — BGP sessions may be affected"


def x__bgp_summary__mutmut_8(ready: int, total: int) -> str:
    if total == 0:
        return f"{_UNKNOWN} — no calico-node agents observed"
    if ready == total:
        return "BGP node-to-node mesh reachable (all calico-node agents ready)"
    degraded = total + ready
    return f"{degraded} calico-node agent(s) degraded — BGP sessions may be affected"

mutants_x__bgp_summary__mutmut['_mutmut_orig'] = x__bgp_summary__mutmut_orig # type: ignore # mutmut generated
mutants_x__bgp_summary__mutmut['x__bgp_summary__mutmut_1'] = x__bgp_summary__mutmut_1 # type: ignore # mutmut generated
mutants_x__bgp_summary__mutmut['x__bgp_summary__mutmut_2'] = x__bgp_summary__mutmut_2 # type: ignore # mutmut generated
mutants_x__bgp_summary__mutmut['x__bgp_summary__mutmut_3'] = x__bgp_summary__mutmut_3 # type: ignore # mutmut generated
mutants_x__bgp_summary__mutmut['x__bgp_summary__mutmut_4'] = x__bgp_summary__mutmut_4 # type: ignore # mutmut generated
mutants_x__bgp_summary__mutmut['x__bgp_summary__mutmut_5'] = x__bgp_summary__mutmut_5 # type: ignore # mutmut generated
mutants_x__bgp_summary__mutmut['x__bgp_summary__mutmut_6'] = x__bgp_summary__mutmut_6 # type: ignore # mutmut generated
mutants_x__bgp_summary__mutmut['x__bgp_summary__mutmut_7'] = x__bgp_summary__mutmut_7 # type: ignore # mutmut generated
mutants_x__bgp_summary__mutmut['x__bgp_summary__mutmut_8'] = x__bgp_summary__mutmut_8 # type: ignore # mutmut generated


def _summary(verdict: str, ready: int, total: int) -> str:
    return f"Calico dataplane {verdict}: {ready}/{total} calico-node agents ready"
