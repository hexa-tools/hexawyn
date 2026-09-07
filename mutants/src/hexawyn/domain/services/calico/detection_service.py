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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_resolve_dataplane_mode__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_resolve_dataplane_mode__mutmut)
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


def x_resolve_dataplane_mode__mutmut_orig(mode_signals: set[str]) -> DataplaneMode:
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


def x_resolve_dataplane_mode__mutmut_1(mode_signals: set[str]) -> DataplaneMode:
    """Pick the dataplane mode from observed CRD signals, with priority.

    eBPF > VXLAN > IPIP > UNKNOWN. Unknown signals are ignored so the result is
    never invented — an unknown mode stays UNKNOWN.
    """
    normalized = None
    if _EBPF in normalized:
        return DataplaneMode.EBPF
    if _VXLAN in normalized:
        return DataplaneMode.VXLAN
    if _IPIP in normalized:
        return DataplaneMode.IPIP
    return DataplaneMode.UNKNOWN


def x_resolve_dataplane_mode__mutmut_2(mode_signals: set[str]) -> DataplaneMode:
    """Pick the dataplane mode from observed CRD signals, with priority.

    eBPF > VXLAN > IPIP > UNKNOWN. Unknown signals are ignored so the result is
    never invented — an unknown mode stays UNKNOWN.
    """
    normalized = {str(signal).upper() for signal in mode_signals}
    if _EBPF in normalized:
        return DataplaneMode.EBPF
    if _VXLAN in normalized:
        return DataplaneMode.VXLAN
    if _IPIP in normalized:
        return DataplaneMode.IPIP
    return DataplaneMode.UNKNOWN


def x_resolve_dataplane_mode__mutmut_3(mode_signals: set[str]) -> DataplaneMode:
    """Pick the dataplane mode from observed CRD signals, with priority.

    eBPF > VXLAN > IPIP > UNKNOWN. Unknown signals are ignored so the result is
    never invented — an unknown mode stays UNKNOWN.
    """
    normalized = {str(None).lower() for signal in mode_signals}
    if _EBPF in normalized:
        return DataplaneMode.EBPF
    if _VXLAN in normalized:
        return DataplaneMode.VXLAN
    if _IPIP in normalized:
        return DataplaneMode.IPIP
    return DataplaneMode.UNKNOWN


def x_resolve_dataplane_mode__mutmut_4(mode_signals: set[str]) -> DataplaneMode:
    """Pick the dataplane mode from observed CRD signals, with priority.

    eBPF > VXLAN > IPIP > UNKNOWN. Unknown signals are ignored so the result is
    never invented — an unknown mode stays UNKNOWN.
    """
    normalized = {str(signal).lower() for signal in mode_signals}
    if _EBPF not in normalized:
        return DataplaneMode.EBPF
    if _VXLAN in normalized:
        return DataplaneMode.VXLAN
    if _IPIP in normalized:
        return DataplaneMode.IPIP
    return DataplaneMode.UNKNOWN


def x_resolve_dataplane_mode__mutmut_5(mode_signals: set[str]) -> DataplaneMode:
    """Pick the dataplane mode from observed CRD signals, with priority.

    eBPF > VXLAN > IPIP > UNKNOWN. Unknown signals are ignored so the result is
    never invented — an unknown mode stays UNKNOWN.
    """
    normalized = {str(signal).lower() for signal in mode_signals}
    if _EBPF in normalized:
        return DataplaneMode.EBPF
    if _VXLAN not in normalized:
        return DataplaneMode.VXLAN
    if _IPIP in normalized:
        return DataplaneMode.IPIP
    return DataplaneMode.UNKNOWN


def x_resolve_dataplane_mode__mutmut_6(mode_signals: set[str]) -> DataplaneMode:
    """Pick the dataplane mode from observed CRD signals, with priority.

    eBPF > VXLAN > IPIP > UNKNOWN. Unknown signals are ignored so the result is
    never invented — an unknown mode stays UNKNOWN.
    """
    normalized = {str(signal).lower() for signal in mode_signals}
    if _EBPF in normalized:
        return DataplaneMode.EBPF
    if _VXLAN in normalized:
        return DataplaneMode.VXLAN
    if _IPIP not in normalized:
        return DataplaneMode.IPIP
    return DataplaneMode.UNKNOWN

mutants_x_resolve_dataplane_mode__mutmut['_mutmut_orig'] = x_resolve_dataplane_mode__mutmut_orig # type: ignore # mutmut generated
mutants_x_resolve_dataplane_mode__mutmut['x_resolve_dataplane_mode__mutmut_1'] = x_resolve_dataplane_mode__mutmut_1 # type: ignore # mutmut generated
mutants_x_resolve_dataplane_mode__mutmut['x_resolve_dataplane_mode__mutmut_2'] = x_resolve_dataplane_mode__mutmut_2 # type: ignore # mutmut generated
mutants_x_resolve_dataplane_mode__mutmut['x_resolve_dataplane_mode__mutmut_3'] = x_resolve_dataplane_mode__mutmut_3 # type: ignore # mutmut generated
mutants_x_resolve_dataplane_mode__mutmut['x_resolve_dataplane_mode__mutmut_4'] = x_resolve_dataplane_mode__mutmut_4 # type: ignore # mutmut generated
mutants_x_resolve_dataplane_mode__mutmut['x_resolve_dataplane_mode__mutmut_5'] = x_resolve_dataplane_mode__mutmut_5 # type: ignore # mutmut generated
mutants_x_resolve_dataplane_mode__mutmut['x_resolve_dataplane_mode__mutmut_6'] = x_resolve_dataplane_mode__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_agent_phase__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_agent_phase__mutmut)
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


def x_build_agent_phase__mutmut_orig(pod_phase: str, ready_status: str) -> CalicoAgentPhase:
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


def x_build_agent_phase__mutmut_1(pod_phase: str, ready_status: str) -> CalicoAgentPhase:
    """Derive the agent phase from the pod phase and Ready condition string.

    The condition status is kept as the raw ``True``/``False``/``Unknown``
    string so nothing is fabricated.
    """
    if ready_status != _READY_TRUE:
        return CalicoAgentPhase.READY
    if ready_status == _READY_FALSE:
        return CalicoAgentPhase.NOT_READY
    if pod_phase.strip().lower() == "running":
        return CalicoAgentPhase.RUNNING
    return CalicoAgentPhase.UNKNOWN


def x_build_agent_phase__mutmut_2(pod_phase: str, ready_status: str) -> CalicoAgentPhase:
    """Derive the agent phase from the pod phase and Ready condition string.

    The condition status is kept as the raw ``True``/``False``/``Unknown``
    string so nothing is fabricated.
    """
    if ready_status == _READY_TRUE:
        return CalicoAgentPhase.READY
    if ready_status != _READY_FALSE:
        return CalicoAgentPhase.NOT_READY
    if pod_phase.strip().lower() == "running":
        return CalicoAgentPhase.RUNNING
    return CalicoAgentPhase.UNKNOWN


def x_build_agent_phase__mutmut_3(pod_phase: str, ready_status: str) -> CalicoAgentPhase:
    """Derive the agent phase from the pod phase and Ready condition string.

    The condition status is kept as the raw ``True``/``False``/``Unknown``
    string so nothing is fabricated.
    """
    if ready_status == _READY_TRUE:
        return CalicoAgentPhase.READY
    if ready_status == _READY_FALSE:
        return CalicoAgentPhase.NOT_READY
    if pod_phase.strip().upper() == "running":
        return CalicoAgentPhase.RUNNING
    return CalicoAgentPhase.UNKNOWN


def x_build_agent_phase__mutmut_4(pod_phase: str, ready_status: str) -> CalicoAgentPhase:
    """Derive the agent phase from the pod phase and Ready condition string.

    The condition status is kept as the raw ``True``/``False``/``Unknown``
    string so nothing is fabricated.
    """
    if ready_status == _READY_TRUE:
        return CalicoAgentPhase.READY
    if ready_status == _READY_FALSE:
        return CalicoAgentPhase.NOT_READY
    if pod_phase.strip().lower() != "running":
        return CalicoAgentPhase.RUNNING
    return CalicoAgentPhase.UNKNOWN


def x_build_agent_phase__mutmut_5(pod_phase: str, ready_status: str) -> CalicoAgentPhase:
    """Derive the agent phase from the pod phase and Ready condition string.

    The condition status is kept as the raw ``True``/``False``/``Unknown``
    string so nothing is fabricated.
    """
    if ready_status == _READY_TRUE:
        return CalicoAgentPhase.READY
    if ready_status == _READY_FALSE:
        return CalicoAgentPhase.NOT_READY
    if pod_phase.strip().lower() == "XXrunningXX":
        return CalicoAgentPhase.RUNNING
    return CalicoAgentPhase.UNKNOWN


def x_build_agent_phase__mutmut_6(pod_phase: str, ready_status: str) -> CalicoAgentPhase:
    """Derive the agent phase from the pod phase and Ready condition string.

    The condition status is kept as the raw ``True``/``False``/``Unknown``
    string so nothing is fabricated.
    """
    if ready_status == _READY_TRUE:
        return CalicoAgentPhase.READY
    if ready_status == _READY_FALSE:
        return CalicoAgentPhase.NOT_READY
    if pod_phase.strip().lower() == "RUNNING":
        return CalicoAgentPhase.RUNNING
    return CalicoAgentPhase.UNKNOWN

mutants_x_build_agent_phase__mutmut['_mutmut_orig'] = x_build_agent_phase__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_agent_phase__mutmut['x_build_agent_phase__mutmut_1'] = x_build_agent_phase__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_agent_phase__mutmut['x_build_agent_phase__mutmut_2'] = x_build_agent_phase__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_agent_phase__mutmut['x_build_agent_phase__mutmut_3'] = x_build_agent_phase__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_agent_phase__mutmut['x_build_agent_phase__mutmut_4'] = x_build_agent_phase__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_agent_phase__mutmut['x_build_agent_phase__mutmut_5'] = x_build_agent_phase__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_agent_phase__mutmut['x_build_agent_phase__mutmut_6'] = x_build_agent_phase__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_degraded_summary__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_degraded_summary__mutmut)
def build_degraded_summary(agents: list[CalicoNodeAgent]) -> str | None:
    """Human-readable summary of degraded agents, or None when fully healthy."""
    if not agents:
        return None
    ready = sum(1 for agent in agents if agent.healthy)
    degraded = len(agents) - ready
    if degraded <= 0:
        return None
    return f"{ready}/{len(agents)} calico-node agents ready ({degraded} degraded)"


def x_build_degraded_summary__mutmut_orig(agents: list[CalicoNodeAgent]) -> str | None:
    """Human-readable summary of degraded agents, or None when fully healthy."""
    if not agents:
        return None
    ready = sum(1 for agent in agents if agent.healthy)
    degraded = len(agents) - ready
    if degraded <= 0:
        return None
    return f"{ready}/{len(agents)} calico-node agents ready ({degraded} degraded)"


def x_build_degraded_summary__mutmut_1(agents: list[CalicoNodeAgent]) -> str | None:
    """Human-readable summary of degraded agents, or None when fully healthy."""
    if agents:
        return None
    ready = sum(1 for agent in agents if agent.healthy)
    degraded = len(agents) - ready
    if degraded <= 0:
        return None
    return f"{ready}/{len(agents)} calico-node agents ready ({degraded} degraded)"


def x_build_degraded_summary__mutmut_2(agents: list[CalicoNodeAgent]) -> str | None:
    """Human-readable summary of degraded agents, or None when fully healthy."""
    if not agents:
        return None
    ready = None
    degraded = len(agents) - ready
    if degraded <= 0:
        return None
    return f"{ready}/{len(agents)} calico-node agents ready ({degraded} degraded)"


def x_build_degraded_summary__mutmut_3(agents: list[CalicoNodeAgent]) -> str | None:
    """Human-readable summary of degraded agents, or None when fully healthy."""
    if not agents:
        return None
    ready = sum(None)
    degraded = len(agents) - ready
    if degraded <= 0:
        return None
    return f"{ready}/{len(agents)} calico-node agents ready ({degraded} degraded)"


def x_build_degraded_summary__mutmut_4(agents: list[CalicoNodeAgent]) -> str | None:
    """Human-readable summary of degraded agents, or None when fully healthy."""
    if not agents:
        return None
    ready = sum(2 for agent in agents if agent.healthy)
    degraded = len(agents) - ready
    if degraded <= 0:
        return None
    return f"{ready}/{len(agents)} calico-node agents ready ({degraded} degraded)"


def x_build_degraded_summary__mutmut_5(agents: list[CalicoNodeAgent]) -> str | None:
    """Human-readable summary of degraded agents, or None when fully healthy."""
    if not agents:
        return None
    ready = sum(1 for agent in agents if agent.healthy)
    degraded = None
    if degraded <= 0:
        return None
    return f"{ready}/{len(agents)} calico-node agents ready ({degraded} degraded)"


def x_build_degraded_summary__mutmut_6(agents: list[CalicoNodeAgent]) -> str | None:
    """Human-readable summary of degraded agents, or None when fully healthy."""
    if not agents:
        return None
    ready = sum(1 for agent in agents if agent.healthy)
    degraded = len(agents) + ready
    if degraded <= 0:
        return None
    return f"{ready}/{len(agents)} calico-node agents ready ({degraded} degraded)"


def x_build_degraded_summary__mutmut_7(agents: list[CalicoNodeAgent]) -> str | None:
    """Human-readable summary of degraded agents, or None when fully healthy."""
    if not agents:
        return None
    ready = sum(1 for agent in agents if agent.healthy)
    degraded = len(agents) - ready
    if degraded < 0:
        return None
    return f"{ready}/{len(agents)} calico-node agents ready ({degraded} degraded)"


def x_build_degraded_summary__mutmut_8(agents: list[CalicoNodeAgent]) -> str | None:
    """Human-readable summary of degraded agents, or None when fully healthy."""
    if not agents:
        return None
    ready = sum(1 for agent in agents if agent.healthy)
    degraded = len(agents) - ready
    if degraded <= 1:
        return None
    return f"{ready}/{len(agents)} calico-node agents ready ({degraded} degraded)"

mutants_x_build_degraded_summary__mutmut['_mutmut_orig'] = x_build_degraded_summary__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_degraded_summary__mutmut['x_build_degraded_summary__mutmut_1'] = x_build_degraded_summary__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_degraded_summary__mutmut['x_build_degraded_summary__mutmut_2'] = x_build_degraded_summary__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_degraded_summary__mutmut['x_build_degraded_summary__mutmut_3'] = x_build_degraded_summary__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_degraded_summary__mutmut['x_build_degraded_summary__mutmut_4'] = x_build_degraded_summary__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_degraded_summary__mutmut['x_build_degraded_summary__mutmut_5'] = x_build_degraded_summary__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_degraded_summary__mutmut['x_build_degraded_summary__mutmut_6'] = x_build_degraded_summary__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_degraded_summary__mutmut['x_build_degraded_summary__mutmut_7'] = x_build_degraded_summary__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_degraded_summary__mutmut['x_build_degraded_summary__mutmut_8'] = x_build_degraded_summary__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_detection_result__mutmut)
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


def x_build_detection_result__mutmut_orig(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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


def x_build_detection_result__mutmut_1(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
    """Interpret raw signals into the final detection result.

    Degradation is truthful: an installed cluster with no running agents is
    reported DEGRADED rather than silently healthy, and an absent Calico is
    reported NOT_INSTALLED with the explicit marker.
    """
    agents = None
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


def x_build_detection_result__mutmut_2(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
    """Interpret raw signals into the final detection result.

    Degradation is truthful: an installed cluster with no running agents is
    reported DEGRADED rather than silently healthy, and an absent Calico is
    reported NOT_INSTALLED with the explicit marker.
    """
    agents = list(None)
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


def x_build_detection_result__mutmut_3(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
    """Interpret raw signals into the final detection result.

    Degradation is truthful: an installed cluster with no running agents is
    reported DEGRADED rather than silently healthy, and an absent Calico is
    reported NOT_INSTALLED with the explicit marker.
    """
    agents = list(signals.agents)
    total = None
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


def x_build_detection_result__mutmut_4(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
    """Interpret raw signals into the final detection result.

    Degradation is truthful: an installed cluster with no running agents is
    reported DEGRADED rather than silently healthy, and an absent Calico is
    reported NOT_INSTALLED with the explicit marker.
    """
    agents = list(signals.agents)
    total = len(agents)
    ready = None
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


def x_build_detection_result__mutmut_5(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
    """Interpret raw signals into the final detection result.

    Degradation is truthful: an installed cluster with no running agents is
    reported DEGRADED rather than silently healthy, and an absent Calico is
    reported NOT_INSTALLED with the explicit marker.
    """
    agents = list(signals.agents)
    total = len(agents)
    ready = sum(None)
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


def x_build_detection_result__mutmut_6(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
    """Interpret raw signals into the final detection result.

    Degradation is truthful: an installed cluster with no running agents is
    reported DEGRADED rather than silently healthy, and an absent Calico is
    reported NOT_INSTALLED with the explicit marker.
    """
    agents = list(signals.agents)
    total = len(agents)
    ready = sum(2 for agent in agents if agent.healthy)
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


def x_build_detection_result__mutmut_7(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
    """Interpret raw signals into the final detection result.

    Degradation is truthful: an installed cluster with no running agents is
    reported DEGRADED rather than silently healthy, and an absent Calico is
    reported NOT_INSTALLED with the explicit marker.
    """
    agents = list(signals.agents)
    total = len(agents)
    ready = sum(1 for agent in agents if agent.healthy)
    degraded = None
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


def x_build_detection_result__mutmut_8(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
    """Interpret raw signals into the final detection result.

    Degradation is truthful: an installed cluster with no running agents is
    reported DEGRADED rather than silently healthy, and an absent Calico is
    reported NOT_INSTALLED with the explicit marker.
    """
    agents = list(signals.agents)
    total = len(agents)
    ready = sum(1 for agent in agents if agent.healthy)
    degraded = total + ready
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


def x_build_detection_result__mutmut_9(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
    """Interpret raw signals into the final detection result.

    Degradation is truthful: an installed cluster with no running agents is
    reported DEGRADED rather than silently healthy, and an absent Calico is
    reported NOT_INSTALLED with the explicit marker.
    """
    agents = list(signals.agents)
    total = len(agents)
    ready = sum(1 for agent in agents if agent.healthy)
    degraded = total - ready
    mode = None

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


def x_build_detection_result__mutmut_10(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
    """Interpret raw signals into the final detection result.

    Degradation is truthful: an installed cluster with no running agents is
    reported DEGRADED rather than silently healthy, and an absent Calico is
    reported NOT_INSTALLED with the explicit marker.
    """
    agents = list(signals.agents)
    total = len(agents)
    ready = sum(1 for agent in agents if agent.healthy)
    degraded = total - ready
    mode = resolve_dataplane_mode(None)

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


def x_build_detection_result__mutmut_11(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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

    if signals.installed:
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


def x_build_detection_result__mutmut_12(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        status = None
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


def x_build_detection_result__mutmut_13(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        degraded_summary = ""
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


def x_build_detection_result__mutmut_14(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
    elif degraded > 0 and total == 0:
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


def x_build_detection_result__mutmut_15(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
    elif degraded >= 0 or total == 0:
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


def x_build_detection_result__mutmut_16(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
    elif degraded > 1 or total == 0:
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


def x_build_detection_result__mutmut_17(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
    elif degraded > 0 or total != 0:
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


def x_build_detection_result__mutmut_18(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
    elif degraded > 0 or total == 1:
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


def x_build_detection_result__mutmut_19(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        status = None
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


def x_build_detection_result__mutmut_20(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        degraded_summary = None
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


def x_build_detection_result__mutmut_21(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        degraded_summary = build_degraded_summary(agents) and "0 calico-node agents detected"
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


def x_build_detection_result__mutmut_22(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        degraded_summary = build_degraded_summary(None) or "0 calico-node agents detected"
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


def x_build_detection_result__mutmut_23(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        degraded_summary = build_degraded_summary(agents) or "XX0 calico-node agents detectedXX"
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


def x_build_detection_result__mutmut_24(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        degraded_summary = build_degraded_summary(agents) or "0 CALICO-NODE AGENTS DETECTED"
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


def x_build_detection_result__mutmut_25(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        status = None
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


def x_build_detection_result__mutmut_26(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        degraded_summary = ""

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


def x_build_detection_result__mutmut_27(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        installed=None,
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


def x_build_detection_result__mutmut_28(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        status=None,
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


def x_build_detection_result__mutmut_29(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        not_installed_marker=None,
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


def x_build_detection_result__mutmut_30(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        version=None,
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


def x_build_detection_result__mutmut_31(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        mode=None,
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


def x_build_detection_result__mutmut_32(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        namespace=None,
        tigera_operator=signals.tigera_operator,
        enterprise=signals.enterprise,
        agents=agents,
        total_nodes=total,
        ready_agents=ready,
        degraded_agents=degraded,
        degraded_summary=degraded_summary,
        error=signals.error,
    )


def x_build_detection_result__mutmut_33(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        tigera_operator=None,
        enterprise=signals.enterprise,
        agents=agents,
        total_nodes=total,
        ready_agents=ready,
        degraded_agents=degraded,
        degraded_summary=degraded_summary,
        error=signals.error,
    )


def x_build_detection_result__mutmut_34(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        enterprise=None,
        agents=agents,
        total_nodes=total,
        ready_agents=ready,
        degraded_agents=degraded,
        degraded_summary=degraded_summary,
        error=signals.error,
    )


def x_build_detection_result__mutmut_35(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        agents=None,
        total_nodes=total,
        ready_agents=ready,
        degraded_agents=degraded,
        degraded_summary=degraded_summary,
        error=signals.error,
    )


def x_build_detection_result__mutmut_36(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        total_nodes=None,
        ready_agents=ready,
        degraded_agents=degraded,
        degraded_summary=degraded_summary,
        error=signals.error,
    )


def x_build_detection_result__mutmut_37(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        ready_agents=None,
        degraded_agents=degraded,
        degraded_summary=degraded_summary,
        error=signals.error,
    )


def x_build_detection_result__mutmut_38(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        degraded_agents=None,
        degraded_summary=degraded_summary,
        error=signals.error,
    )


def x_build_detection_result__mutmut_39(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        degraded_summary=None,
        error=signals.error,
    )


def x_build_detection_result__mutmut_40(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        error=None,
    )


def x_build_detection_result__mutmut_41(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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


def x_build_detection_result__mutmut_42(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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


def x_build_detection_result__mutmut_43(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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


def x_build_detection_result__mutmut_44(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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


def x_build_detection_result__mutmut_45(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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


def x_build_detection_result__mutmut_46(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        tigera_operator=signals.tigera_operator,
        enterprise=signals.enterprise,
        agents=agents,
        total_nodes=total,
        ready_agents=ready,
        degraded_agents=degraded,
        degraded_summary=degraded_summary,
        error=signals.error,
    )


def x_build_detection_result__mutmut_47(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        enterprise=signals.enterprise,
        agents=agents,
        total_nodes=total,
        ready_agents=ready,
        degraded_agents=degraded,
        degraded_summary=degraded_summary,
        error=signals.error,
    )


def x_build_detection_result__mutmut_48(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        agents=agents,
        total_nodes=total,
        ready_agents=ready,
        degraded_agents=degraded,
        degraded_summary=degraded_summary,
        error=signals.error,
    )


def x_build_detection_result__mutmut_49(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        total_nodes=total,
        ready_agents=ready,
        degraded_agents=degraded,
        degraded_summary=degraded_summary,
        error=signals.error,
    )


def x_build_detection_result__mutmut_50(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        ready_agents=ready,
        degraded_agents=degraded,
        degraded_summary=degraded_summary,
        error=signals.error,
    )


def x_build_detection_result__mutmut_51(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        degraded_agents=degraded,
        degraded_summary=degraded_summary,
        error=signals.error,
    )


def x_build_detection_result__mutmut_52(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        degraded_summary=degraded_summary,
        error=signals.error,
    )


def x_build_detection_result__mutmut_53(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        error=signals.error,
    )


def x_build_detection_result__mutmut_54(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        )


def x_build_detection_result__mutmut_55(signals: CalicoDetectionSignals) -> CalicoDetectionResult:
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
        not_installed_marker=NOT_INSTALLED_MARKER if signals.installed else None,
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

mutants_x_build_detection_result__mutmut['_mutmut_orig'] = x_build_detection_result__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_1'] = x_build_detection_result__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_2'] = x_build_detection_result__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_3'] = x_build_detection_result__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_4'] = x_build_detection_result__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_5'] = x_build_detection_result__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_6'] = x_build_detection_result__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_7'] = x_build_detection_result__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_8'] = x_build_detection_result__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_9'] = x_build_detection_result__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_10'] = x_build_detection_result__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_11'] = x_build_detection_result__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_12'] = x_build_detection_result__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_13'] = x_build_detection_result__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_14'] = x_build_detection_result__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_15'] = x_build_detection_result__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_16'] = x_build_detection_result__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_17'] = x_build_detection_result__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_18'] = x_build_detection_result__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_19'] = x_build_detection_result__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_20'] = x_build_detection_result__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_21'] = x_build_detection_result__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_22'] = x_build_detection_result__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_23'] = x_build_detection_result__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_24'] = x_build_detection_result__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_25'] = x_build_detection_result__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_26'] = x_build_detection_result__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_27'] = x_build_detection_result__mutmut_27 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_28'] = x_build_detection_result__mutmut_28 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_29'] = x_build_detection_result__mutmut_29 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_30'] = x_build_detection_result__mutmut_30 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_31'] = x_build_detection_result__mutmut_31 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_32'] = x_build_detection_result__mutmut_32 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_33'] = x_build_detection_result__mutmut_33 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_34'] = x_build_detection_result__mutmut_34 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_35'] = x_build_detection_result__mutmut_35 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_36'] = x_build_detection_result__mutmut_36 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_37'] = x_build_detection_result__mutmut_37 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_38'] = x_build_detection_result__mutmut_38 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_39'] = x_build_detection_result__mutmut_39 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_40'] = x_build_detection_result__mutmut_40 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_41'] = x_build_detection_result__mutmut_41 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_42'] = x_build_detection_result__mutmut_42 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_43'] = x_build_detection_result__mutmut_43 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_44'] = x_build_detection_result__mutmut_44 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_45'] = x_build_detection_result__mutmut_45 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_46'] = x_build_detection_result__mutmut_46 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_47'] = x_build_detection_result__mutmut_47 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_48'] = x_build_detection_result__mutmut_48 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_49'] = x_build_detection_result__mutmut_49 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_50'] = x_build_detection_result__mutmut_50 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_51'] = x_build_detection_result__mutmut_51 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_52'] = x_build_detection_result__mutmut_52 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_53'] = x_build_detection_result__mutmut_53 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_54'] = x_build_detection_result__mutmut_54 # type: ignore # mutmut generated
mutants_x_build_detection_result__mutmut['x_build_detection_result__mutmut_55'] = x_build_detection_result__mutmut_55 # type: ignore # mutmut generated
