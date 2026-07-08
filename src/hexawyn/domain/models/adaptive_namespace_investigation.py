from __future__ import annotations

from dataclasses import dataclass, field

from hexawyn.domain.models.incident_triage import RootCauseCandidate


@dataclass(frozen=True)
class UnhealthyResourceRef:
    name: str
    kind: str
    reason: str


@dataclass(frozen=True)
class OverviewSnapshot:
    """Plain domain view of a ConservativeNamespaceOverviewResponse — extracted by
    the service so this feature's domain layer never depends on an
    application-layer DTO."""

    namespace: str
    namespace_status: str
    health_status: str
    unhealthy_resources: list[UnhealthyResourceRef] = field(default_factory=list)
    summary: str = ""


@dataclass(frozen=True)
class RankedFailingResource:
    name: str
    kind: str
    reason: str
    restart_count: int
    rank: int


@dataclass(frozen=True)
class ResourceInvestigation:
    resource: RankedFailingResource
    events: list[str] = field(default_factory=list)
    logs: list[str] = field(default_factory=list)
    last_termination_reason: str | None = None


@dataclass(frozen=True)
class AdaptiveInvestigationRequest:
    namespace: str
    depth: int = 3


@dataclass(frozen=True)
class AdaptiveInvestigationReport:
    namespace: str
    namespace_status: str
    health_status: str
    overview_summary: str
    investigated_resources: list[ResourceInvestigation] = field(default_factory=list)
    root_cause_candidates: list[RootCauseCandidate] = field(default_factory=list)
    recommended_actions: list[str] = field(default_factory=list)
    skipped_resources: list[str] = field(default_factory=list)
    node_pressure_context: str | None = None
    has_more_failing: bool = False
    remaining_failing_count: int = 0
