"""Pure Calico detection logic — no infrastructure imports.

Interprets raw adapter signals (`CalicoDetectionSignals`) into the truthful
detection result, computing the dataplane mode and the per-node degradation
summary. Honesty is guaranteed: a `NOT_INSTALLED` marker is only ever emitted
when the adapter could not find Calico artefacts.
"""

from __future__ import annotations

from hexawyn.domain.models.calico import (
    NOT_INSTALLED_MARKER,
    CalicoAgentPhase,
    CalicoDetectionResult,
    CalicoDetectionSignals,
    CalicoDetectionStatus,
    CalicoNodeAgent,
    DataplaneMode,
)

_EBPF = "ebpf"
_VXLAN = "vxlan"
_IPIP = "ipip"
_READY_TRUE = "True"
_READY_FALSE = "False"


def resolve_dataplane_mode(mode_signals: set[str]) -> DataplaneMode:
    """Pick the dataplane mode from observed CRD signals, with priority.

    eBPF > VXLAN > IPIP > UNKNOWN. Unknown signals are ignored so the result is
    never invented — an unknown mode stays UNKNOWN.
    """
    normalized = {str(signal).lower() for signal in mode_signals}
    if _EBPF in normalized:
        return DataplaneMode.EBPF
    if _VXLAN in normalized:
        return DataplaneMode.VXLAN
    if _IPIP in normalized:
        return DataplaneMode.IPIP
    return DataplaneMode.UNKNOWN


def build_agent_phase(pod_phase: str, ready_status: str) -> CalicoAgentPhase:
    """Derive the agent phase from the pod phase and Ready condition string.

    The condition status is kept as the raw ``True``/``False``/``Unknown``
    string so nothing is fabricated.
    """
    if ready_status == _READY_TRUE:
        return CalicoAgentPhase.READY
    if ready_status == _READY_FALSE:
        return CalicoAgentPhase.NOT_READY
    if pod_phase.strip().lower() == "running":
        return CalicoAgentPhase.RUNNING
    return CalicoAgentPhase.UNKNOWN


def build_degraded_summary(agents: list[CalicoNodeAgent]) -> str | None:
    """Human-readable summary of degraded agents, or None when fully healthy."""
    if not agents:
        return None
    ready = sum(1 for agent in agents if agent.healthy)
    degraded = len(agents) - ready
    if degraded <= 0:
        return None
    return f"{ready}/{len(agents)} calico-node agents ready ({degraded} degraded)"


def build_detection_result(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
    """Interpret raw signals into the final detection result.

    Degradation is truthful: an installed cluster with no running agents is
    reported DEGRADED rather than silently healthy, and an absent Calico is
    reported NOT_INSTALLED with the explicit marker.
    """
    agents = list(signals.agents)
    total = len(agents)
    ready = sum(1 for agent in agents if agent.healthy)
    degraded = total - ready
    mode = resolve_dataplane_mode(signals.mode_signals)

    if not signals.installed:
        status = CalicoDetectionStatus.NOT_INSTALLED
        degraded_summary = None
    elif degraded > 0 or total == 0:
        status = CalicoDetectionStatus.DEGRADED
        degraded_summary = build_degraded_summary(agents) or "0 calico-node agents detected"
    else:
        status = CalicoDetectionStatus.INSTALLED
        degraded_summary = None

    return CalicoDetectionResult(
        installed=signals.installed,
        status=status,
        not_installed_marker=NOT_INSTALLED_MARKER if not signals.installed else None,
        version=signals.version,
        mode=mode,
        namespace=signals.namespace,
        tigera_operator=signals.tigera_operator,
        enterprise=signals.enterprise,
        agents=agents,
        total_nodes=total,
        ready_agents=ready,
        degraded_agents=degraded,
        degraded_summary=degraded_summary,
        error=signals.error,
    )
