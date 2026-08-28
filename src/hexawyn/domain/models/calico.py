"""Calico domain models — pure dataclasses and enums.

No infrastructure imports. This module only holds the vocabulary of the Calico
series (detect, status, network policies, IP pools, host endpoints) and the pure
helpers needed to interpret it.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

# Marker returned (never fabricated) when Calico is genuinely absent.
NOT_INSTALLED_MARKER = "NOT_INSTALLED"


class DataplaneMode(Enum):
    """Calico dataplane datapath as reported by the observed CRDs."""

    EBPF = "eBPF"
    VXLAN = "VXLAN"
    IPIP = "IPIP"
    UNKNOWN = "UNKNOWN"


class CalicoAgentPhase(Enum):
    """Health phase of a single calico-node agent."""

    READY = "ready"
    RUNNING = "running"
    NOT_READY = "not_ready"
    UNKNOWN = "unknown"


class CalicoDetectionStatus(Enum):
    """Overall Calico detection status."""

    INSTALLED = "installed"
    DEGRADED = "degraded"
    NOT_INSTALLED = "not_installed"


@dataclass(frozen=True)
class CalicoNodeAgent:
    """Health snapshot of one calico-node agent (one per node)."""

    node: str
    phase: CalicoAgentPhase
    ready: bool
    ready_replicas: int
    desired_replicas: int
    available_replicas: int
    message: str | None = None

    @property
    def healthy(self) -> bool:
        """True when the agent is ready at full desired replicas."""
        return (
            self.ready
            and self.desired_replicas > 0
            and self.ready_replicas >= self.desired_replicas
        )


@dataclass(frozen=True)
class CalicoNetworkPolicy:
    """A Calico NetworkPolicy / GlobalNetworkPolicy projection."""

    name: str
    namespace: str
    order: float
    selector: str
    ingress_rules: tuple[str, ...]
    egress_rules: tuple[str, ...]
    apply_on_forward: bool
    kind: str = "CalicoNetworkPolicy"
    action: str | None = None
    ingress_rule_count: int = 0
    egress_rule_count: int = 0
    has_l7_rule: bool = False


@dataclass(frozen=True)
class CalicoIPPool:
    """A Calico IPPool projection."""

    name: str
    cidr: str
    ipip_mode: str
    vxlan_mode: str
    disabled: bool
    nat_outgoing: bool = False
    node_selector: str = ""


@dataclass(frozen=True)
class CalicoHostEndpoint:
    """A Calico HostEndpoint projection (non-pod host interface)."""

    name: str
    node: str
    interface_name: str
    expected_ip: str
    expected_ips: tuple[str, ...] = ()
    labels: tuple[tuple[str, str], ...] = ()
    applied_policies: tuple[str, ...] = ()


@dataclass(frozen=True)
class CalicoDetectionSignals:
    """Raw, adapter-gathered signals — the pure service turns these into a result."""

    installed: bool
    version: str | None
    namespace: str | None
    mode_signals: set[str]
    tigera_operator: bool
    enterprise: bool
    agents: list[CalicoNodeAgent]
    error: str | None


@dataclass(frozen=True)
class CalicoDetectionResult:
    """Result of Calico detection — honours NOT_INSTALLED honestly."""

    installed: bool
    status: CalicoDetectionStatus
    not_installed_marker: str | None
    version: str | None
    mode: DataplaneMode
    namespace: str | None
    tigera_operator: bool
    enterprise: bool
    agents: list[CalicoNodeAgent]
    total_nodes: int
    ready_agents: int
    degraded_agents: int
    degraded_summary: str | None
    error: str | None

    @property
    def not_installed(self) -> bool:
        """Honest flag — never inferred from an absent check, only from absence."""
        return not self.installed

    @property
    def marker(self) -> str | None:
        """The explicit NOT_INSTALLED marker when Calico is absent."""
        return self.not_installed_marker


@dataclass(frozen=True)
class CalicoStatusResult:
    """Aggregated datapath health: agents + felix errors + connectivity probe."""

    installed: bool
    not_installed_marker: str | None
    status: CalicoDetectionStatus
    ready_agents: int
    total_agents: int
    degraded_summary: str | None
    agents: list[CalicoNodeAgent]
    felix_errors_available: bool
    felix_errors: int | None
    connectivity_available: bool
    connectivity_status: str | None
    connectivity_detail: str | None
    error: str | None

    @property
    def not_installed(self) -> bool:
        """Honest flag — Calico absence is never invented."""
        return not self.installed


@dataclass(frozen=True)
class CalicoWorkload:
    """Workload population of a namespace (pod count) for coverage auditing."""

    namespace: str
    pod_count: int


@dataclass(frozen=True)
class CalicoCoverageGap:
    """A namespace with workloads lacking full L3/L4 (or L7) restriction."""

    namespace: str
    workload_count: int
    policy_count: int
    issue: str
    network_status: str
    risk_level: str
    selectors: list[str]
    note: str | None


@dataclass(frozen=True)
class CalicoPolicyAuditResult:
    """Calico policy coverage audit — gaps ranked by risk."""

    installed: bool
    not_installed_marker: str | None
    total_namespaces_checked: int
    gap_count: int
    findings: list[CalicoCoverageGap]
    summary: str | None
    error: str | None

    @property
    def not_installed(self) -> bool:
        """Honest flag — Calico absence is never invented."""
        return not self.installed


@dataclass(frozen=True)
class CalicoSegmentationEdge:
    """One directed tier-to-tier path of the Calico segmentation matrix."""

    source: str
    destination: str
    restricted: bool
    selectors: list[str]
    note: str | None


@dataclass(frozen=True)
class CalicoSegmentationAuditResult:
    """Calico east-west segmentation matrix (tiers = namespaces).

    Calico has no Cilium-like identities, so reachability is derived from the
    endpoint selectors and the default-deny presence (allow/deny) per tier.
    """

    installed: bool
    not_installed_marker: str | None
    view: str
    tiers: list[str]
    edges: list[CalicoSegmentationEdge]
    gap_count: int
    total_paths: int
    summary: str | None
    error: str | None

    @property
    def not_installed(self) -> bool:
        """Honest flag — Calico absence is never invented."""
        return not self.installed


@dataclass(frozen=True)
class CalicoBgpConfiguration:
    """A Calico BGPConfiguration projection (cluster-scoped)."""

    name: str
    as_number: str | None
    node_to_node_mesh_enabled: bool | None
    service_cluster_ips: tuple[str, ...]


@dataclass(frozen=True)
class CalicoBgpPeer:
    """A Calico BGPPeer projection (peer IP/ASN + node selector)."""

    name: str
    peer_ip: str
    as_number: str | None
    node_selector: str


@dataclass(frozen=True)
class CalicoBgpAuditResult:
    """Calico BGP configuration + peer + session-state audit."""

    installed: bool
    not_installed_marker: str | None
    as_number: str | None
    node_to_node_mesh_enabled: bool | None
    service_cluster_ips: tuple[str, ...]
    peers: list[CalicoBgpPeer]
    peer_count: int
    session_state: str
    session_note: str | None
    summary: str | None
    error: str | None

    @property
    def not_installed(self) -> bool:
        """Honest flag — Calico absence is never invented."""
        return not self.installed
