from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypedDict


class TimelineBucketDict(TypedDict):
    minute: str
    count: int
    is_spike: bool


class EventStormDict(TypedDict):
    start_time: str
    end_time: str
    event_count: int


class ReasonCountDict(TypedDict):
    reason: str
    count: int


class SampleEventDict(TypedDict):
    reason: str
    message: str
    involved_object: str
    severity: str
    timestamp: str


class IncidentSummaryDict(TypedDict):
    reason: str
    involved_objects: list[str]
    event_count: int
    likely_root_cause: str
    sample_events: list[SampleEventDict]


@dataclass
class AdvancedNamespaceEventAnalyticsResponse:
    namespace: str = ""
    total_events: int = 0
    timeline: list[TimelineBucketDict] = field(default_factory=list)
    storms: list[EventStormDict] = field(default_factory=list)
    top_reasons: list[ReasonCountDict] = field(default_factory=list)
    correlated_incidents: list[IncidentSummaryDict] = field(default_factory=list)
    sampling_applied: bool = False
    error: str | None = None
