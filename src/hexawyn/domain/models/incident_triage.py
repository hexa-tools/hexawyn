from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Literal

TimelineSource = Literal["event", "log", "pipeline"]


class IncidentCauseCategory(Enum):
    """Functional category of an incident's likely root cause."""

    DATABASE = "database"
    RESOURCE_EXHAUSTION = "resource_exhaustion"
    NETWORK = "network"
    IMAGE_OR_CONFIG = "image_or_config"
    DEPLOYMENT = "deployment"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class TimelineEntry:
    """One reconstructed event in the incident timeline."""

    timestamp: str
    source: TimelineSource
    namespace: str
    object: str
    reason: str
    message: str
    severity: str


@dataclass(frozen=True)
class RootCauseCandidate:
    """A possible root cause, ranked by confidence against other candidates."""

    description: str
    category: IncidentCauseCategory
    confidence: float
    evidence: list[str] = field(default_factory=list)
    involved_objects: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class ImpactAssessment:
    affected_services: list[str] = field(default_factory=list)
    estimated_user_impact: str = ""
    duration_minutes: int = 0
    ongoing: bool = False


@dataclass(frozen=True)
class IncidentTriageRequest:
    namespace: str
    time_window_minutes: int = 120
    related_namespaces: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class IncidentTriageReport:
    """Structured triage/RCA report — timeline, impact, root cause, remediation."""

    namespace: str
    time_window_minutes: int
    timeline: list[TimelineEntry] = field(default_factory=list)
    root_causes: list[RootCauseCandidate] = field(default_factory=list)
    impact: ImpactAssessment = field(default_factory=ImpactAssessment)
    remediation_steps: list[str] = field(default_factory=list)
    resolved: bool = False
    resolution_time: str | None = None
    mttr_minutes: int | None = None
    ntp_drift_detected: bool = False
    ntp_drift_note: str = ""
    cross_namespace_correlation: list[str] = field(default_factory=list)
    insufficient_data: bool = False
    data_checked: list[str] = field(default_factory=list)
