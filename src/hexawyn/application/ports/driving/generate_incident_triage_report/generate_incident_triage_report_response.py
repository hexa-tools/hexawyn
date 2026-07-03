from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypedDict


class TimelineEntryDict(TypedDict):
    timestamp: str
    source: str
    object: str
    reason: str
    message: str
    severity: str


class RootCauseCandidateDict(TypedDict):
    description: str
    category: str
    confidence: float
    evidence: list[str]
    involved_objects: list[str]


class ImpactAssessmentDict(TypedDict):
    affected_services: list[str]
    estimated_user_impact: str
    duration_minutes: int
    ongoing: bool


@dataclass
class GenerateIncidentTriageReportResponse:
    namespace: str = ""
    time_window_minutes: int = 0
    timeline: list[TimelineEntryDict] = field(default_factory=list)
    root_causes: list[RootCauseCandidateDict] = field(default_factory=list)
    impact: ImpactAssessmentDict | None = None
    remediation_steps: list[str] = field(default_factory=list)
    resolved: bool = False
    resolution_time: str | None = None
    mttr_minutes: int | None = None
    ntp_drift_detected: bool = False
    ntp_drift_note: str = ""
    cross_namespace_correlation: list[str] = field(default_factory=list)
    insufficient_data: bool = False
    data_checked: list[str] = field(default_factory=list)
    formatted_report: str = ""
    error: str | None = None
