# mypy: ignore-errors
from dataclasses import dataclass, field
from typing import TypedDict

from hexawyn.domain.models.incident_triage import IncidentTriageReport


class ImpactAssessmentDict(TypedDict):
    affected_services: list[str]
    estimated_user_impact: str
    duration_minutes: int
    ongoing: bool


class RootCauseCandidateDict(TypedDict):
    description: str
    category: str
    confidence: float
    evidence: list[str]


class TimelineEntryDict(TypedDict):
    timestamp: str
    event: str
    severity: str


@dataclass
class GenerateIncidentTriageReportResponse:
    namespace: str = ""
    time_window_minutes: int = 0
    total_unhealthy_pods: int = 0
    timeline: list[TimelineEntryDict] = field(default_factory=list)
    root_causes: list[RootCauseCandidateDict] = field(default_factory=list)
    impact: ImpactAssessmentDict = field(default_factory=dict)  # type: ignore[arg-type]
    remediation_steps: list[str] = field(default_factory=list)
    resolved: bool = False
    resolution_time: str = ""
    mttr_minutes: int = 0
    ntp_drift_detected: bool = False
    ntp_drift_note: str = ""
    cross_namespace_correlation: str = ""
    insufficient_data: bool = False
    summary: str = ""
    result: IncidentTriageReport | None = None
    data_checked: str = ""
    source: str = ""
    object: str = ""
    reason: str = ""
    message: str = ""
    message: str = ""  # type: ignore
    reason: str = ""  # type: ignore
    object: str = ""  # type: ignore
    source: str = ""  # type: ignore
    formatted_report: str = ""
    error: str | None = None
