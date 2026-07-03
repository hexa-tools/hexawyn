from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime

from hexawyn.domain.models.constants import AdvancedEventAnalyticsConstants
from hexawyn.domain.models.event import ClassifiedEvent
from hexawyn.domain.models.namespace_event import NamespaceEvent
from hexawyn.domain.services.event_analysis.correlator import CorrelatedIncident, EventCorrelator
from hexawyn.domain.services.event_analysis.event_storm_detector import (
    EventStorm,
    EventStormDetector,
)
from hexawyn.domain.services.event_analysis.namespace_event_classifier import (
    classify_namespace_event,
)

_cfg = AdvancedEventAnalyticsConstants()
_NORMAL_EVENT_TYPE = "Normal"


@dataclass(frozen=True)
class TimelineBucket:
    minute: str
    count: int
    is_spike: bool = False


@dataclass(frozen=True)
class ReasonCount:
    reason: str
    count: int


@dataclass(frozen=True)
class IncidentSummary:
    reason: str
    involved_objects: list[str] = field(default_factory=list)
    event_count: int = 0
    likely_root_cause: str = ""
    sample_events: list[ClassifiedEvent] = field(default_factory=list)


@dataclass(frozen=True)
class AdvancedEventAnalyticsReport:
    namespace: str
    total_events: int
    timeline: list[TimelineBucket] = field(default_factory=list)
    storms: list[EventStorm] = field(default_factory=list)
    top_reasons: list[ReasonCount] = field(default_factory=list)
    correlated_incidents: list[IncidentSummary] = field(default_factory=list)
    sampling_applied: bool = False


def generate_advanced_event_analytics(
    namespace: str, events: list[NamespaceEvent]
) -> AdvancedEventAnalyticsReport:
    """6h advanced analytics report (ECA-19 data source, ECA-20 EventCorrelator reuse).

    Timeline and storm detection run over ALL events (a rolling restart's
    flood of Normal events is exactly the kind of volume spike this should
    surface), while top reasons and correlated incidents only consider
    non-Normal events — those are the actionable signal.
    """
    if not events:
        return AdvancedEventAnalyticsReport(namespace=namespace, total_events=0)

    sorted_events = sorted(events, key=lambda event: _parse_timestamp(event.last_seen))

    storms = EventStormDetector().detect(sorted_events)
    timeline = _build_timeline(sorted_events, storms)

    actionable = [event for event in sorted_events if event.event_type != _NORMAL_EVENT_TYPE]
    top_reasons = _top_reasons(actionable)

    classified = [classify_namespace_event(event, namespace) for event in actionable]
    incidents = EventCorrelator().correlate(classified)

    sampling_applied = len(events) > _cfg.sampling_threshold
    correlated_incidents = [
        _to_incident_summary(incident, sampling_applied) for incident in incidents
    ]

    return AdvancedEventAnalyticsReport(
        namespace=namespace,
        total_events=len(events),
        timeline=timeline,
        storms=storms,
        top_reasons=top_reasons,
        correlated_incidents=correlated_incidents,
        sampling_applied=sampling_applied,
    )


def _build_timeline(
    sorted_events: list[NamespaceEvent], storms: list[EventStorm]
) -> list[TimelineBucket]:
    buckets: dict[str, int] = defaultdict(int)
    for event in sorted_events:
        buckets[event.last_seen[:16]] += 1

    spike_minutes: set[str] = set()
    for storm in storms:
        start_minute = storm.start_time[:16]
        end_minute = storm.end_time[:16]
        spike_minutes.update(minute for minute in buckets if start_minute <= minute <= end_minute)

    return [
        TimelineBucket(minute=minute, count=count, is_spike=minute in spike_minutes)
        for minute, count in sorted(buckets.items())
    ]


def _top_reasons(actionable_events: list[NamespaceEvent]) -> list[ReasonCount]:
    counts = Counter(event.reason for event in actionable_events)
    return [
        ReasonCount(reason=reason, count=count)
        for reason, count in counts.most_common(_cfg.top_reasons_limit)
    ]


def _to_incident_summary(incident: CorrelatedIncident, sampling_applied: bool) -> IncidentSummary:
    sample = (
        incident.events[: _cfg.sample_events_per_incident] if sampling_applied else incident.events
    )
    return IncidentSummary(
        reason=incident.reason,
        involved_objects=incident.involved_objects,
        event_count=len(incident.events),
        likely_root_cause=incident.likely_root_cause,
        sample_events=sample,
    )


def _parse_timestamp(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("Z", "+00:00"))
