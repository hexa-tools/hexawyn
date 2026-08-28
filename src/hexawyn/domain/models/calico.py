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


@dataclass(frozen=True)
class CalicoIPPool:
    """A Calico IPPool projection."""

    name: str
    cidr: str
    ipip_mode: str
    vxlan_mode: str
    disabled: bool


@dataclass(frozen=True)
class CalicoHostEndpoint:
    """A Calico HostEndpoint projection."""

    name: str
    node: str
    interface_name: str
    expected_ip: str


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
