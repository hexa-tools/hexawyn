from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CiliumAgentHealth:
    """Health of a single Cilium agent pod on one node."""

    node: str
    pod_name: str
    namespace: str
    ready: bool
    phase: str
    restart_count: int
    image: str | None = None
    message: str | None = None


@dataclass(frozen=True)
class CiliumDetectionResult:
    """Observed Cilium installation state and agent health."""

    installed: bool
    status: str
    version: str | None
    mode: str
    namespace: str | None
    total_agents: int
    ready_agents: int
    degraded_summary: str | None
    agents: list[CiliumAgentHealth]
    note: str | None


@dataclass(frozen=True)
class CiliumStatusResult:
    """Aggregated health & connectivity status of the Cilium datapath."""

    installed: bool
    status: str
    ready_agents: int
    total_agents: int
    degraded_summary: str | None
    controller_errors: int
    connectivity: str | None
    nodes: list[CiliumAgentHealth]
    note: str | None


@dataclass(frozen=True)
class CiliumNetworkPolicyInfo:
    """Summary of one Cilium network policy (namespaced or cluster-wide)."""

    kind: str
    name: str
    namespace: str | None
    endpoint_selector: str
    ingress_rule_count: int
    egress_rule_count: int
    l7_rule_count: int
    l7_protocols: tuple[str, ...]


@dataclass(frozen=True)
class CiliumNetworkPoliciesResult:
    """Total Cilium network policy inventory with kind breakdown."""

    installed: bool
    status: str
    total_policies: int
    namespaced_count: int
    clusterwide_count: int
    policies: list[CiliumNetworkPolicyInfo]
    note: str | None
