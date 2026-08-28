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
    endpoint_labels: tuple[tuple[str, str], ...] | None = None


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


@dataclass(frozen=True)
class CiliumL7RuleSummary:
    """One L7 rule (HTTP/gRPC/Kafka/DNS) with its observed match values."""

    protocol: str
    match: tuple[str, ...]


@dataclass(frozen=True)
class CiliumRuleSummary:
    """Summarised ingress/egress rule: endpoints, ports and L7 rules."""

    direction: str
    endpoints: tuple[str, ...]
    ports: tuple[str, ...]
    l7: tuple[CiliumL7RuleSummary, ...]


@dataclass(frozen=True)
class CiliumNetworkPolicyDetail:
    """Full detail of a single Cilium network policy, incl. raw spec."""

    installed: bool
    status: str
    kind: str
    name: str
    namespace: str | None
    endpoint_selector: str
    ingress_rules: tuple[CiliumRuleSummary, ...]
    egress_rules: tuple[CiliumRuleSummary, ...]
    l7_protocols: tuple[str, ...]
    spec: dict[str, object]
    note: str | None


@dataclass(frozen=True)
class CiliumWorkload:
    """A workload (pod) carrying labels that Cilium endpoint selectors match."""

    namespace: str
    name: str
    labels: dict[str, str]


@dataclass(frozen=True)
class CiliumAuditFinding:
    """A coverage gap or a partially restricted Cilium workload."""

    namespace: str
    workload: str
    coverage: str
    ingress_restricted: bool
    egress_restricted: bool
    l7_restricted: bool
    risk: str
    note: str | None


@dataclass(frozen=True)
class CiliumPolicyAuditResult:
    """Aggregated Cilium network-policy coverage audit."""

    installed: bool
    status: str
    view: str
    total_workloads: int
    uncovered_count: int
    findings: list[CiliumAuditFinding]
    summary: str
    note: str | None


@dataclass(frozen=True)
class CiliumIdentityInfo:
    """One Cilium security identity: numeric id, label set, endpoint count."""

    id: str
    labels: tuple[str, ...]
    endpoint_count: int


@dataclass(frozen=True)
class CiliumIdentitiesResult:
    """List of Cilium security identities with their endpoint counts."""

    installed: bool
    status: str
    total_identities: int
    identities: list[CiliumIdentityInfo]
    note: str | None


@dataclass(frozen=True)
class CiliumPathFinding:
    """An allowed-but-unrestricted east-west path between two identities."""

    source_id: str
    destination_id: str
    source_labels: tuple[str, ...]
    destination_labels: tuple[str, ...]
    severity: str
    note: str | None


@dataclass(frozen=True)
class CiliumSegmentationAuditResult:
    """East-west reachability audit built from Cilium identities and policies."""

    installed: bool
    status: str
    view: str
    total_identities: int
    total_paths: int
    uncovered_paths: int
    findings: list[CiliumPathFinding]
    summary: str
    note: str | None


@dataclass(frozen=True)
class CiliumFlowQuery:
    """Filter parameters for a Hubble flow query."""

    namespace: str | None = None
    pod: str | None = None
    direction: str | None = None
    verdict: str | None = None
    window_minutes: int = 15
    limit: int = 100


@dataclass(frozen=True)
class CiliumFlowEntry:
    """One Hubble flow observation between two workloads."""

    timestamp: str
    source: str
    destination: str
    source_namespace: str | None
    destination_namespace: str | None
    source_identity: str | None
    destination_identity: str | None
    verdict: str
    drop_reason: str | None
    protocol: str | None
    destination_port: str | None
    l7_protocol: str | None
    direction: str | None
    policy: str | None = None


@dataclass(frozen=True)
class CiliumFlowsResult:
    """Hubble flow log query result."""

    installed: bool
    status: str
    total_flows: int
    flows: list[CiliumFlowEntry]
    note: str | None


@dataclass(frozen=True)
class CiliumDenialsQuery:
    """Filter parameters for a Cilium dropped-flow (denial) query."""

    namespace: str | None = None
    window_minutes: int = 5
    limit: int = 100


@dataclass(frozen=True)
class CiliumDenialGroup:
    """Aggregated dropped-flow group by policy / source / destination / reason."""

    policy: str | None
    source: str
    destination: str
    source_namespace: str | None
    destination_namespace: str | None
    reason: str
    count: int


@dataclass(frozen=True)
class CiliumDenialsResult:
    """Aggregated Cilium policy-denial counts."""

    installed: bool
    status: str
    total_denials: int
    groups: list[CiliumDenialGroup]
    note: str | None
