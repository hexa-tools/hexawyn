from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypedDict


class ResourceInvestigationDict(TypedDict):
    name: str
    kind: str
    reason: str
    restart_count: int
    events: list[str]
    logs: list[str]
    last_termination_reason: str | None


class RootCauseCandidateDict(TypedDict):
    description: str
    category: str
    confidence: float
    evidence: list[str]
    involved_objects: list[str]


@dataclass
class AdaptiveNamespaceInvestigationResponse:
    namespace: str = ""
    namespace_status: str = ""
    health_status: str = ""
    overview_summary: str = ""
    investigated_resources: list[ResourceInvestigationDict] = field(default_factory=list)
    root_cause_candidates: list[RootCauseCandidateDict] = field(default_factory=list)
    recommended_actions: list[str] = field(default_factory=list)
    skipped_resources: list[str] = field(default_factory=list)
    node_pressure_context: str | None = None
    has_more_failing: bool = False
    remaining_failing_count: int = 0
    error: str | None = None
