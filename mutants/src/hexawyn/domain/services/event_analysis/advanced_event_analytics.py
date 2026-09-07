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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


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
mutants_x_generate_advanced_event_analytics__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_generate_advanced_event_analytics__mutmut)
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


def x_generate_advanced_event_analytics__mutmut_orig(
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


def x_generate_advanced_event_analytics__mutmut_1(
    namespace: str, events: list[NamespaceEvent]
) -> AdvancedEventAnalyticsReport:
    """6h advanced analytics report (ECA-19 data source, ECA-20 EventCorrelator reuse).

    Timeline and storm detection run over ALL events (a rolling restart's
    flood of Normal events is exactly the kind of volume spike this should
    surface), while top reasons and correlated incidents only consider
    non-Normal events — those are the actionable signal.
    """
    if events:
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


def x_generate_advanced_event_analytics__mutmut_2(
    namespace: str, events: list[NamespaceEvent]
) -> AdvancedEventAnalyticsReport:
    """6h advanced analytics report (ECA-19 data source, ECA-20 EventCorrelator reuse).

    Timeline and storm detection run over ALL events (a rolling restart's
    flood of Normal events is exactly the kind of volume spike this should
    surface), while top reasons and correlated incidents only consider
    non-Normal events — those are the actionable signal.
    """
    if not events:
        return AdvancedEventAnalyticsReport(namespace=None, total_events=0)

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


def x_generate_advanced_event_analytics__mutmut_3(
    namespace: str, events: list[NamespaceEvent]
) -> AdvancedEventAnalyticsReport:
    """6h advanced analytics report (ECA-19 data source, ECA-20 EventCorrelator reuse).

    Timeline and storm detection run over ALL events (a rolling restart's
    flood of Normal events is exactly the kind of volume spike this should
    surface), while top reasons and correlated incidents only consider
    non-Normal events — those are the actionable signal.
    """
    if not events:
        return AdvancedEventAnalyticsReport(namespace=namespace, total_events=None)

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


def x_generate_advanced_event_analytics__mutmut_4(
    namespace: str, events: list[NamespaceEvent]
) -> AdvancedEventAnalyticsReport:
    """6h advanced analytics report (ECA-19 data source, ECA-20 EventCorrelator reuse).

    Timeline and storm detection run over ALL events (a rolling restart's
    flood of Normal events is exactly the kind of volume spike this should
    surface), while top reasons and correlated incidents only consider
    non-Normal events — those are the actionable signal.
    """
    if not events:
        return AdvancedEventAnalyticsReport(total_events=0)

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


def x_generate_advanced_event_analytics__mutmut_5(
    namespace: str, events: list[NamespaceEvent]
) -> AdvancedEventAnalyticsReport:
    """6h advanced analytics report (ECA-19 data source, ECA-20 EventCorrelator reuse).

    Timeline and storm detection run over ALL events (a rolling restart's
    flood of Normal events is exactly the kind of volume spike this should
    surface), while top reasons and correlated incidents only consider
    non-Normal events — those are the actionable signal.
    """
    if not events:
        return AdvancedEventAnalyticsReport(namespace=namespace, )

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


def x_generate_advanced_event_analytics__mutmut_6(
    namespace: str, events: list[NamespaceEvent]
) -> AdvancedEventAnalyticsReport:
    """6h advanced analytics report (ECA-19 data source, ECA-20 EventCorrelator reuse).

    Timeline and storm detection run over ALL events (a rolling restart's
    flood of Normal events is exactly the kind of volume spike this should
    surface), while top reasons and correlated incidents only consider
    non-Normal events — those are the actionable signal.
    """
    if not events:
        return AdvancedEventAnalyticsReport(namespace=namespace, total_events=1)

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


def x_generate_advanced_event_analytics__mutmut_7(
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

    sorted_events = None

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


def x_generate_advanced_event_analytics__mutmut_8(
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

    sorted_events = sorted(None, key=lambda event: _parse_timestamp(event.last_seen))

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


def x_generate_advanced_event_analytics__mutmut_9(
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

    sorted_events = sorted(events, key=None)

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


def x_generate_advanced_event_analytics__mutmut_10(
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

    sorted_events = sorted(key=lambda event: _parse_timestamp(event.last_seen))

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


def x_generate_advanced_event_analytics__mutmut_11(
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

    sorted_events = sorted(events, )

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


def x_generate_advanced_event_analytics__mutmut_12(
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

    sorted_events = sorted(events, key=lambda event: None)

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


def x_generate_advanced_event_analytics__mutmut_13(
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

    sorted_events = sorted(events, key=lambda event: _parse_timestamp(None))

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


def x_generate_advanced_event_analytics__mutmut_14(
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

    storms = None
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


def x_generate_advanced_event_analytics__mutmut_15(
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

    storms = EventStormDetector().detect(None)
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


def x_generate_advanced_event_analytics__mutmut_16(
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
    timeline = None

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


def x_generate_advanced_event_analytics__mutmut_17(
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
    timeline = _build_timeline(None, storms)

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


def x_generate_advanced_event_analytics__mutmut_18(
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
    timeline = _build_timeline(sorted_events, None)

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


def x_generate_advanced_event_analytics__mutmut_19(
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
    timeline = _build_timeline(storms)

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


def x_generate_advanced_event_analytics__mutmut_20(
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
    timeline = _build_timeline(sorted_events, )

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


def x_generate_advanced_event_analytics__mutmut_21(
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

    actionable = None
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


def x_generate_advanced_event_analytics__mutmut_22(
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

    actionable = [event for event in sorted_events if event.event_type == _NORMAL_EVENT_TYPE]
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


def x_generate_advanced_event_analytics__mutmut_23(
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
    top_reasons = None

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


def x_generate_advanced_event_analytics__mutmut_24(
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
    top_reasons = _top_reasons(None)

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


def x_generate_advanced_event_analytics__mutmut_25(
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

    classified = None
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


def x_generate_advanced_event_analytics__mutmut_26(
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

    classified = [classify_namespace_event(None, namespace) for event in actionable]
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


def x_generate_advanced_event_analytics__mutmut_27(
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

    classified = [classify_namespace_event(event, None) for event in actionable]
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


def x_generate_advanced_event_analytics__mutmut_28(
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

    classified = [classify_namespace_event(namespace) for event in actionable]
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


def x_generate_advanced_event_analytics__mutmut_29(
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

    classified = [classify_namespace_event(event, ) for event in actionable]
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


def x_generate_advanced_event_analytics__mutmut_30(
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
    incidents = None

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


def x_generate_advanced_event_analytics__mutmut_31(
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
    incidents = EventCorrelator().correlate(None)

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


def x_generate_advanced_event_analytics__mutmut_32(
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

    sampling_applied = None
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


def x_generate_advanced_event_analytics__mutmut_33(
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

    sampling_applied = len(events) >= _cfg.sampling_threshold
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


def x_generate_advanced_event_analytics__mutmut_34(
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
    correlated_incidents = None

    return AdvancedEventAnalyticsReport(
        namespace=namespace,
        total_events=len(events),
        timeline=timeline,
        storms=storms,
        top_reasons=top_reasons,
        correlated_incidents=correlated_incidents,
        sampling_applied=sampling_applied,
    )


def x_generate_advanced_event_analytics__mutmut_35(
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
        _to_incident_summary(None, sampling_applied) for incident in incidents
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


def x_generate_advanced_event_analytics__mutmut_36(
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
        _to_incident_summary(incident, None) for incident in incidents
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


def x_generate_advanced_event_analytics__mutmut_37(
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
        _to_incident_summary(sampling_applied) for incident in incidents
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


def x_generate_advanced_event_analytics__mutmut_38(
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
        _to_incident_summary(incident, ) for incident in incidents
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


def x_generate_advanced_event_analytics__mutmut_39(
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
        namespace=None,
        total_events=len(events),
        timeline=timeline,
        storms=storms,
        top_reasons=top_reasons,
        correlated_incidents=correlated_incidents,
        sampling_applied=sampling_applied,
    )


def x_generate_advanced_event_analytics__mutmut_40(
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
        total_events=None,
        timeline=timeline,
        storms=storms,
        top_reasons=top_reasons,
        correlated_incidents=correlated_incidents,
        sampling_applied=sampling_applied,
    )


def x_generate_advanced_event_analytics__mutmut_41(
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
        timeline=None,
        storms=storms,
        top_reasons=top_reasons,
        correlated_incidents=correlated_incidents,
        sampling_applied=sampling_applied,
    )


def x_generate_advanced_event_analytics__mutmut_42(
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
        storms=None,
        top_reasons=top_reasons,
        correlated_incidents=correlated_incidents,
        sampling_applied=sampling_applied,
    )


def x_generate_advanced_event_analytics__mutmut_43(
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
        top_reasons=None,
        correlated_incidents=correlated_incidents,
        sampling_applied=sampling_applied,
    )


def x_generate_advanced_event_analytics__mutmut_44(
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
        correlated_incidents=None,
        sampling_applied=sampling_applied,
    )


def x_generate_advanced_event_analytics__mutmut_45(
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
        sampling_applied=None,
    )


def x_generate_advanced_event_analytics__mutmut_46(
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
        total_events=len(events),
        timeline=timeline,
        storms=storms,
        top_reasons=top_reasons,
        correlated_incidents=correlated_incidents,
        sampling_applied=sampling_applied,
    )


def x_generate_advanced_event_analytics__mutmut_47(
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
        timeline=timeline,
        storms=storms,
        top_reasons=top_reasons,
        correlated_incidents=correlated_incidents,
        sampling_applied=sampling_applied,
    )


def x_generate_advanced_event_analytics__mutmut_48(
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
        storms=storms,
        top_reasons=top_reasons,
        correlated_incidents=correlated_incidents,
        sampling_applied=sampling_applied,
    )


def x_generate_advanced_event_analytics__mutmut_49(
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
        top_reasons=top_reasons,
        correlated_incidents=correlated_incidents,
        sampling_applied=sampling_applied,
    )


def x_generate_advanced_event_analytics__mutmut_50(
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
        correlated_incidents=correlated_incidents,
        sampling_applied=sampling_applied,
    )


def x_generate_advanced_event_analytics__mutmut_51(
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
        sampling_applied=sampling_applied,
    )


def x_generate_advanced_event_analytics__mutmut_52(
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
        )

mutants_x_generate_advanced_event_analytics__mutmut['_mutmut_orig'] = x_generate_advanced_event_analytics__mutmut_orig # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_1'] = x_generate_advanced_event_analytics__mutmut_1 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_2'] = x_generate_advanced_event_analytics__mutmut_2 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_3'] = x_generate_advanced_event_analytics__mutmut_3 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_4'] = x_generate_advanced_event_analytics__mutmut_4 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_5'] = x_generate_advanced_event_analytics__mutmut_5 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_6'] = x_generate_advanced_event_analytics__mutmut_6 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_7'] = x_generate_advanced_event_analytics__mutmut_7 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_8'] = x_generate_advanced_event_analytics__mutmut_8 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_9'] = x_generate_advanced_event_analytics__mutmut_9 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_10'] = x_generate_advanced_event_analytics__mutmut_10 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_11'] = x_generate_advanced_event_analytics__mutmut_11 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_12'] = x_generate_advanced_event_analytics__mutmut_12 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_13'] = x_generate_advanced_event_analytics__mutmut_13 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_14'] = x_generate_advanced_event_analytics__mutmut_14 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_15'] = x_generate_advanced_event_analytics__mutmut_15 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_16'] = x_generate_advanced_event_analytics__mutmut_16 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_17'] = x_generate_advanced_event_analytics__mutmut_17 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_18'] = x_generate_advanced_event_analytics__mutmut_18 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_19'] = x_generate_advanced_event_analytics__mutmut_19 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_20'] = x_generate_advanced_event_analytics__mutmut_20 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_21'] = x_generate_advanced_event_analytics__mutmut_21 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_22'] = x_generate_advanced_event_analytics__mutmut_22 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_23'] = x_generate_advanced_event_analytics__mutmut_23 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_24'] = x_generate_advanced_event_analytics__mutmut_24 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_25'] = x_generate_advanced_event_analytics__mutmut_25 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_26'] = x_generate_advanced_event_analytics__mutmut_26 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_27'] = x_generate_advanced_event_analytics__mutmut_27 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_28'] = x_generate_advanced_event_analytics__mutmut_28 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_29'] = x_generate_advanced_event_analytics__mutmut_29 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_30'] = x_generate_advanced_event_analytics__mutmut_30 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_31'] = x_generate_advanced_event_analytics__mutmut_31 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_32'] = x_generate_advanced_event_analytics__mutmut_32 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_33'] = x_generate_advanced_event_analytics__mutmut_33 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_34'] = x_generate_advanced_event_analytics__mutmut_34 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_35'] = x_generate_advanced_event_analytics__mutmut_35 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_36'] = x_generate_advanced_event_analytics__mutmut_36 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_37'] = x_generate_advanced_event_analytics__mutmut_37 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_38'] = x_generate_advanced_event_analytics__mutmut_38 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_39'] = x_generate_advanced_event_analytics__mutmut_39 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_40'] = x_generate_advanced_event_analytics__mutmut_40 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_41'] = x_generate_advanced_event_analytics__mutmut_41 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_42'] = x_generate_advanced_event_analytics__mutmut_42 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_43'] = x_generate_advanced_event_analytics__mutmut_43 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_44'] = x_generate_advanced_event_analytics__mutmut_44 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_45'] = x_generate_advanced_event_analytics__mutmut_45 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_46'] = x_generate_advanced_event_analytics__mutmut_46 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_47'] = x_generate_advanced_event_analytics__mutmut_47 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_48'] = x_generate_advanced_event_analytics__mutmut_48 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_49'] = x_generate_advanced_event_analytics__mutmut_49 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_50'] = x_generate_advanced_event_analytics__mutmut_50 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_51'] = x_generate_advanced_event_analytics__mutmut_51 # type: ignore # mutmut generated
mutants_x_generate_advanced_event_analytics__mutmut['x_generate_advanced_event_analytics__mutmut_52'] = x_generate_advanced_event_analytics__mutmut_52 # type: ignore # mutmut generated
mutants_x__build_timeline__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_timeline__mutmut)
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


def x__build_timeline__mutmut_orig(
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


def x__build_timeline__mutmut_1(
    sorted_events: list[NamespaceEvent], storms: list[EventStorm]
) -> list[TimelineBucket]:
    buckets: dict[str, int] = None
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


def x__build_timeline__mutmut_2(
    sorted_events: list[NamespaceEvent], storms: list[EventStorm]
) -> list[TimelineBucket]:
    buckets: dict[str, int] = defaultdict(None)
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


def x__build_timeline__mutmut_3(
    sorted_events: list[NamespaceEvent], storms: list[EventStorm]
) -> list[TimelineBucket]:
    buckets: dict[str, int] = defaultdict(int)
    for event in sorted_events:
        buckets[event.last_seen[:16]] = 1

    spike_minutes: set[str] = set()
    for storm in storms:
        start_minute = storm.start_time[:16]
        end_minute = storm.end_time[:16]
        spike_minutes.update(minute for minute in buckets if start_minute <= minute <= end_minute)

    return [
        TimelineBucket(minute=minute, count=count, is_spike=minute in spike_minutes)
        for minute, count in sorted(buckets.items())
    ]


def x__build_timeline__mutmut_4(
    sorted_events: list[NamespaceEvent], storms: list[EventStorm]
) -> list[TimelineBucket]:
    buckets: dict[str, int] = defaultdict(int)
    for event in sorted_events:
        buckets[event.last_seen[:16]] -= 1

    spike_minutes: set[str] = set()
    for storm in storms:
        start_minute = storm.start_time[:16]
        end_minute = storm.end_time[:16]
        spike_minutes.update(minute for minute in buckets if start_minute <= minute <= end_minute)

    return [
        TimelineBucket(minute=minute, count=count, is_spike=minute in spike_minutes)
        for minute, count in sorted(buckets.items())
    ]


def x__build_timeline__mutmut_5(
    sorted_events: list[NamespaceEvent], storms: list[EventStorm]
) -> list[TimelineBucket]:
    buckets: dict[str, int] = defaultdict(int)
    for event in sorted_events:
        buckets[event.last_seen[:17]] += 1

    spike_minutes: set[str] = set()
    for storm in storms:
        start_minute = storm.start_time[:16]
        end_minute = storm.end_time[:16]
        spike_minutes.update(minute for minute in buckets if start_minute <= minute <= end_minute)

    return [
        TimelineBucket(minute=minute, count=count, is_spike=minute in spike_minutes)
        for minute, count in sorted(buckets.items())
    ]


def x__build_timeline__mutmut_6(
    sorted_events: list[NamespaceEvent], storms: list[EventStorm]
) -> list[TimelineBucket]:
    buckets: dict[str, int] = defaultdict(int)
    for event in sorted_events:
        buckets[event.last_seen[:16]] += 2

    spike_minutes: set[str] = set()
    for storm in storms:
        start_minute = storm.start_time[:16]
        end_minute = storm.end_time[:16]
        spike_minutes.update(minute for minute in buckets if start_minute <= minute <= end_minute)

    return [
        TimelineBucket(minute=minute, count=count, is_spike=minute in spike_minutes)
        for minute, count in sorted(buckets.items())
    ]


def x__build_timeline__mutmut_7(
    sorted_events: list[NamespaceEvent], storms: list[EventStorm]
) -> list[TimelineBucket]:
    buckets: dict[str, int] = defaultdict(int)
    for event in sorted_events:
        buckets[event.last_seen[:16]] += 1

    spike_minutes: set[str] = None
    for storm in storms:
        start_minute = storm.start_time[:16]
        end_minute = storm.end_time[:16]
        spike_minutes.update(minute for minute in buckets if start_minute <= minute <= end_minute)

    return [
        TimelineBucket(minute=minute, count=count, is_spike=minute in spike_minutes)
        for minute, count in sorted(buckets.items())
    ]


def x__build_timeline__mutmut_8(
    sorted_events: list[NamespaceEvent], storms: list[EventStorm]
) -> list[TimelineBucket]:
    buckets: dict[str, int] = defaultdict(int)
    for event in sorted_events:
        buckets[event.last_seen[:16]] += 1

    spike_minutes: set[str] = set()
    for storm in storms:
        start_minute = None
        end_minute = storm.end_time[:16]
        spike_minutes.update(minute for minute in buckets if start_minute <= minute <= end_minute)

    return [
        TimelineBucket(minute=minute, count=count, is_spike=minute in spike_minutes)
        for minute, count in sorted(buckets.items())
    ]


def x__build_timeline__mutmut_9(
    sorted_events: list[NamespaceEvent], storms: list[EventStorm]
) -> list[TimelineBucket]:
    buckets: dict[str, int] = defaultdict(int)
    for event in sorted_events:
        buckets[event.last_seen[:16]] += 1

    spike_minutes: set[str] = set()
    for storm in storms:
        start_minute = storm.start_time[:17]
        end_minute = storm.end_time[:16]
        spike_minutes.update(minute for minute in buckets if start_minute <= minute <= end_minute)

    return [
        TimelineBucket(minute=minute, count=count, is_spike=minute in spike_minutes)
        for minute, count in sorted(buckets.items())
    ]


def x__build_timeline__mutmut_10(
    sorted_events: list[NamespaceEvent], storms: list[EventStorm]
) -> list[TimelineBucket]:
    buckets: dict[str, int] = defaultdict(int)
    for event in sorted_events:
        buckets[event.last_seen[:16]] += 1

    spike_minutes: set[str] = set()
    for storm in storms:
        start_minute = storm.start_time[:16]
        end_minute = None
        spike_minutes.update(minute for minute in buckets if start_minute <= minute <= end_minute)

    return [
        TimelineBucket(minute=minute, count=count, is_spike=minute in spike_minutes)
        for minute, count in sorted(buckets.items())
    ]


def x__build_timeline__mutmut_11(
    sorted_events: list[NamespaceEvent], storms: list[EventStorm]
) -> list[TimelineBucket]:
    buckets: dict[str, int] = defaultdict(int)
    for event in sorted_events:
        buckets[event.last_seen[:16]] += 1

    spike_minutes: set[str] = set()
    for storm in storms:
        start_minute = storm.start_time[:16]
        end_minute = storm.end_time[:17]
        spike_minutes.update(minute for minute in buckets if start_minute <= minute <= end_minute)

    return [
        TimelineBucket(minute=minute, count=count, is_spike=minute in spike_minutes)
        for minute, count in sorted(buckets.items())
    ]


def x__build_timeline__mutmut_12(
    sorted_events: list[NamespaceEvent], storms: list[EventStorm]
) -> list[TimelineBucket]:
    buckets: dict[str, int] = defaultdict(int)
    for event in sorted_events:
        buckets[event.last_seen[:16]] += 1

    spike_minutes: set[str] = set()
    for storm in storms:
        start_minute = storm.start_time[:16]
        end_minute = storm.end_time[:16]
        spike_minutes.update(None)

    return [
        TimelineBucket(minute=minute, count=count, is_spike=minute in spike_minutes)
        for minute, count in sorted(buckets.items())
    ]


def x__build_timeline__mutmut_13(
    sorted_events: list[NamespaceEvent], storms: list[EventStorm]
) -> list[TimelineBucket]:
    buckets: dict[str, int] = defaultdict(int)
    for event in sorted_events:
        buckets[event.last_seen[:16]] += 1

    spike_minutes: set[str] = set()
    for storm in storms:
        start_minute = storm.start_time[:16]
        end_minute = storm.end_time[:16]
        spike_minutes.update(minute for minute in buckets if start_minute < minute <= end_minute)

    return [
        TimelineBucket(minute=minute, count=count, is_spike=minute in spike_minutes)
        for minute, count in sorted(buckets.items())
    ]


def x__build_timeline__mutmut_14(
    sorted_events: list[NamespaceEvent], storms: list[EventStorm]
) -> list[TimelineBucket]:
    buckets: dict[str, int] = defaultdict(int)
    for event in sorted_events:
        buckets[event.last_seen[:16]] += 1

    spike_minutes: set[str] = set()
    for storm in storms:
        start_minute = storm.start_time[:16]
        end_minute = storm.end_time[:16]
        spike_minutes.update(minute for minute in buckets if start_minute <= minute < end_minute)

    return [
        TimelineBucket(minute=minute, count=count, is_spike=minute in spike_minutes)
        for minute, count in sorted(buckets.items())
    ]


def x__build_timeline__mutmut_15(
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
        TimelineBucket(minute=None, count=count, is_spike=minute in spike_minutes)
        for minute, count in sorted(buckets.items())
    ]


def x__build_timeline__mutmut_16(
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
        TimelineBucket(minute=minute, count=None, is_spike=minute in spike_minutes)
        for minute, count in sorted(buckets.items())
    ]


def x__build_timeline__mutmut_17(
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
        TimelineBucket(minute=minute, count=count, is_spike=None)
        for minute, count in sorted(buckets.items())
    ]


def x__build_timeline__mutmut_18(
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
        TimelineBucket(count=count, is_spike=minute in spike_minutes)
        for minute, count in sorted(buckets.items())
    ]


def x__build_timeline__mutmut_19(
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
        TimelineBucket(minute=minute, is_spike=minute in spike_minutes)
        for minute, count in sorted(buckets.items())
    ]


def x__build_timeline__mutmut_20(
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
        TimelineBucket(minute=minute, count=count, )
        for minute, count in sorted(buckets.items())
    ]


def x__build_timeline__mutmut_21(
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
        TimelineBucket(minute=minute, count=count, is_spike=minute not in spike_minutes)
        for minute, count in sorted(buckets.items())
    ]


def x__build_timeline__mutmut_22(
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
        for minute, count in sorted(None)
    ]

mutants_x__build_timeline__mutmut['_mutmut_orig'] = x__build_timeline__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_timeline__mutmut['x__build_timeline__mutmut_1'] = x__build_timeline__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_timeline__mutmut['x__build_timeline__mutmut_2'] = x__build_timeline__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_timeline__mutmut['x__build_timeline__mutmut_3'] = x__build_timeline__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_timeline__mutmut['x__build_timeline__mutmut_4'] = x__build_timeline__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_timeline__mutmut['x__build_timeline__mutmut_5'] = x__build_timeline__mutmut_5 # type: ignore # mutmut generated
mutants_x__build_timeline__mutmut['x__build_timeline__mutmut_6'] = x__build_timeline__mutmut_6 # type: ignore # mutmut generated
mutants_x__build_timeline__mutmut['x__build_timeline__mutmut_7'] = x__build_timeline__mutmut_7 # type: ignore # mutmut generated
mutants_x__build_timeline__mutmut['x__build_timeline__mutmut_8'] = x__build_timeline__mutmut_8 # type: ignore # mutmut generated
mutants_x__build_timeline__mutmut['x__build_timeline__mutmut_9'] = x__build_timeline__mutmut_9 # type: ignore # mutmut generated
mutants_x__build_timeline__mutmut['x__build_timeline__mutmut_10'] = x__build_timeline__mutmut_10 # type: ignore # mutmut generated
mutants_x__build_timeline__mutmut['x__build_timeline__mutmut_11'] = x__build_timeline__mutmut_11 # type: ignore # mutmut generated
mutants_x__build_timeline__mutmut['x__build_timeline__mutmut_12'] = x__build_timeline__mutmut_12 # type: ignore # mutmut generated
mutants_x__build_timeline__mutmut['x__build_timeline__mutmut_13'] = x__build_timeline__mutmut_13 # type: ignore # mutmut generated
mutants_x__build_timeline__mutmut['x__build_timeline__mutmut_14'] = x__build_timeline__mutmut_14 # type: ignore # mutmut generated
mutants_x__build_timeline__mutmut['x__build_timeline__mutmut_15'] = x__build_timeline__mutmut_15 # type: ignore # mutmut generated
mutants_x__build_timeline__mutmut['x__build_timeline__mutmut_16'] = x__build_timeline__mutmut_16 # type: ignore # mutmut generated
mutants_x__build_timeline__mutmut['x__build_timeline__mutmut_17'] = x__build_timeline__mutmut_17 # type: ignore # mutmut generated
mutants_x__build_timeline__mutmut['x__build_timeline__mutmut_18'] = x__build_timeline__mutmut_18 # type: ignore # mutmut generated
mutants_x__build_timeline__mutmut['x__build_timeline__mutmut_19'] = x__build_timeline__mutmut_19 # type: ignore # mutmut generated
mutants_x__build_timeline__mutmut['x__build_timeline__mutmut_20'] = x__build_timeline__mutmut_20 # type: ignore # mutmut generated
mutants_x__build_timeline__mutmut['x__build_timeline__mutmut_21'] = x__build_timeline__mutmut_21 # type: ignore # mutmut generated
mutants_x__build_timeline__mutmut['x__build_timeline__mutmut_22'] = x__build_timeline__mutmut_22 # type: ignore # mutmut generated
mutants_x__top_reasons__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__top_reasons__mutmut)
def _top_reasons(actionable_events: list[NamespaceEvent]) -> list[ReasonCount]:
    counts = Counter(event.reason for event in actionable_events)
    return [
        ReasonCount(reason=reason, count=count)
        for reason, count in counts.most_common(_cfg.top_reasons_limit)
    ]


def x__top_reasons__mutmut_orig(actionable_events: list[NamespaceEvent]) -> list[ReasonCount]:
    counts = Counter(event.reason for event in actionable_events)
    return [
        ReasonCount(reason=reason, count=count)
        for reason, count in counts.most_common(_cfg.top_reasons_limit)
    ]


def x__top_reasons__mutmut_1(actionable_events: list[NamespaceEvent]) -> list[ReasonCount]:
    counts = None
    return [
        ReasonCount(reason=reason, count=count)
        for reason, count in counts.most_common(_cfg.top_reasons_limit)
    ]


def x__top_reasons__mutmut_2(actionable_events: list[NamespaceEvent]) -> list[ReasonCount]:
    counts = Counter(None)
    return [
        ReasonCount(reason=reason, count=count)
        for reason, count in counts.most_common(_cfg.top_reasons_limit)
    ]


def x__top_reasons__mutmut_3(actionable_events: list[NamespaceEvent]) -> list[ReasonCount]:
    counts = Counter(event.reason for event in actionable_events)
    return [
        ReasonCount(reason=None, count=count)
        for reason, count in counts.most_common(_cfg.top_reasons_limit)
    ]


def x__top_reasons__mutmut_4(actionable_events: list[NamespaceEvent]) -> list[ReasonCount]:
    counts = Counter(event.reason for event in actionable_events)
    return [
        ReasonCount(reason=reason, count=None)
        for reason, count in counts.most_common(_cfg.top_reasons_limit)
    ]


def x__top_reasons__mutmut_5(actionable_events: list[NamespaceEvent]) -> list[ReasonCount]:
    counts = Counter(event.reason for event in actionable_events)
    return [
        ReasonCount(count=count)
        for reason, count in counts.most_common(_cfg.top_reasons_limit)
    ]


def x__top_reasons__mutmut_6(actionable_events: list[NamespaceEvent]) -> list[ReasonCount]:
    counts = Counter(event.reason for event in actionable_events)
    return [
        ReasonCount(reason=reason, )
        for reason, count in counts.most_common(_cfg.top_reasons_limit)
    ]


def x__top_reasons__mutmut_7(actionable_events: list[NamespaceEvent]) -> list[ReasonCount]:
    counts = Counter(event.reason for event in actionable_events)
    return [
        ReasonCount(reason=reason, count=count)
        for reason, count in counts.most_common(None)
    ]

mutants_x__top_reasons__mutmut['_mutmut_orig'] = x__top_reasons__mutmut_orig # type: ignore # mutmut generated
mutants_x__top_reasons__mutmut['x__top_reasons__mutmut_1'] = x__top_reasons__mutmut_1 # type: ignore # mutmut generated
mutants_x__top_reasons__mutmut['x__top_reasons__mutmut_2'] = x__top_reasons__mutmut_2 # type: ignore # mutmut generated
mutants_x__top_reasons__mutmut['x__top_reasons__mutmut_3'] = x__top_reasons__mutmut_3 # type: ignore # mutmut generated
mutants_x__top_reasons__mutmut['x__top_reasons__mutmut_4'] = x__top_reasons__mutmut_4 # type: ignore # mutmut generated
mutants_x__top_reasons__mutmut['x__top_reasons__mutmut_5'] = x__top_reasons__mutmut_5 # type: ignore # mutmut generated
mutants_x__top_reasons__mutmut['x__top_reasons__mutmut_6'] = x__top_reasons__mutmut_6 # type: ignore # mutmut generated
mutants_x__top_reasons__mutmut['x__top_reasons__mutmut_7'] = x__top_reasons__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_incident_summary__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_incident_summary__mutmut)
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


def x__to_incident_summary__mutmut_orig(incident: CorrelatedIncident, sampling_applied: bool) -> IncidentSummary:
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


def x__to_incident_summary__mutmut_1(incident: CorrelatedIncident, sampling_applied: bool) -> IncidentSummary:
    sample = None
    return IncidentSummary(
        reason=incident.reason,
        involved_objects=incident.involved_objects,
        event_count=len(incident.events),
        likely_root_cause=incident.likely_root_cause,
        sample_events=sample,
    )


def x__to_incident_summary__mutmut_2(incident: CorrelatedIncident, sampling_applied: bool) -> IncidentSummary:
    sample = (
        incident.events[: _cfg.sample_events_per_incident] if sampling_applied else incident.events
    )
    return IncidentSummary(
        reason=None,
        involved_objects=incident.involved_objects,
        event_count=len(incident.events),
        likely_root_cause=incident.likely_root_cause,
        sample_events=sample,
    )


def x__to_incident_summary__mutmut_3(incident: CorrelatedIncident, sampling_applied: bool) -> IncidentSummary:
    sample = (
        incident.events[: _cfg.sample_events_per_incident] if sampling_applied else incident.events
    )
    return IncidentSummary(
        reason=incident.reason,
        involved_objects=None,
        event_count=len(incident.events),
        likely_root_cause=incident.likely_root_cause,
        sample_events=sample,
    )


def x__to_incident_summary__mutmut_4(incident: CorrelatedIncident, sampling_applied: bool) -> IncidentSummary:
    sample = (
        incident.events[: _cfg.sample_events_per_incident] if sampling_applied else incident.events
    )
    return IncidentSummary(
        reason=incident.reason,
        involved_objects=incident.involved_objects,
        event_count=None,
        likely_root_cause=incident.likely_root_cause,
        sample_events=sample,
    )


def x__to_incident_summary__mutmut_5(incident: CorrelatedIncident, sampling_applied: bool) -> IncidentSummary:
    sample = (
        incident.events[: _cfg.sample_events_per_incident] if sampling_applied else incident.events
    )
    return IncidentSummary(
        reason=incident.reason,
        involved_objects=incident.involved_objects,
        event_count=len(incident.events),
        likely_root_cause=None,
        sample_events=sample,
    )


def x__to_incident_summary__mutmut_6(incident: CorrelatedIncident, sampling_applied: bool) -> IncidentSummary:
    sample = (
        incident.events[: _cfg.sample_events_per_incident] if sampling_applied else incident.events
    )
    return IncidentSummary(
        reason=incident.reason,
        involved_objects=incident.involved_objects,
        event_count=len(incident.events),
        likely_root_cause=incident.likely_root_cause,
        sample_events=None,
    )


def x__to_incident_summary__mutmut_7(incident: CorrelatedIncident, sampling_applied: bool) -> IncidentSummary:
    sample = (
        incident.events[: _cfg.sample_events_per_incident] if sampling_applied else incident.events
    )
    return IncidentSummary(
        involved_objects=incident.involved_objects,
        event_count=len(incident.events),
        likely_root_cause=incident.likely_root_cause,
        sample_events=sample,
    )


def x__to_incident_summary__mutmut_8(incident: CorrelatedIncident, sampling_applied: bool) -> IncidentSummary:
    sample = (
        incident.events[: _cfg.sample_events_per_incident] if sampling_applied else incident.events
    )
    return IncidentSummary(
        reason=incident.reason,
        event_count=len(incident.events),
        likely_root_cause=incident.likely_root_cause,
        sample_events=sample,
    )


def x__to_incident_summary__mutmut_9(incident: CorrelatedIncident, sampling_applied: bool) -> IncidentSummary:
    sample = (
        incident.events[: _cfg.sample_events_per_incident] if sampling_applied else incident.events
    )
    return IncidentSummary(
        reason=incident.reason,
        involved_objects=incident.involved_objects,
        likely_root_cause=incident.likely_root_cause,
        sample_events=sample,
    )


def x__to_incident_summary__mutmut_10(incident: CorrelatedIncident, sampling_applied: bool) -> IncidentSummary:
    sample = (
        incident.events[: _cfg.sample_events_per_incident] if sampling_applied else incident.events
    )
    return IncidentSummary(
        reason=incident.reason,
        involved_objects=incident.involved_objects,
        event_count=len(incident.events),
        sample_events=sample,
    )


def x__to_incident_summary__mutmut_11(incident: CorrelatedIncident, sampling_applied: bool) -> IncidentSummary:
    sample = (
        incident.events[: _cfg.sample_events_per_incident] if sampling_applied else incident.events
    )
    return IncidentSummary(
        reason=incident.reason,
        involved_objects=incident.involved_objects,
        event_count=len(incident.events),
        likely_root_cause=incident.likely_root_cause,
        )

mutants_x__to_incident_summary__mutmut['_mutmut_orig'] = x__to_incident_summary__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_incident_summary__mutmut['x__to_incident_summary__mutmut_1'] = x__to_incident_summary__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_incident_summary__mutmut['x__to_incident_summary__mutmut_2'] = x__to_incident_summary__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_incident_summary__mutmut['x__to_incident_summary__mutmut_3'] = x__to_incident_summary__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_incident_summary__mutmut['x__to_incident_summary__mutmut_4'] = x__to_incident_summary__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_incident_summary__mutmut['x__to_incident_summary__mutmut_5'] = x__to_incident_summary__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_incident_summary__mutmut['x__to_incident_summary__mutmut_6'] = x__to_incident_summary__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_incident_summary__mutmut['x__to_incident_summary__mutmut_7'] = x__to_incident_summary__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_incident_summary__mutmut['x__to_incident_summary__mutmut_8'] = x__to_incident_summary__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_incident_summary__mutmut['x__to_incident_summary__mutmut_9'] = x__to_incident_summary__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_incident_summary__mutmut['x__to_incident_summary__mutmut_10'] = x__to_incident_summary__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_incident_summary__mutmut['x__to_incident_summary__mutmut_11'] = x__to_incident_summary__mutmut_11 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse_timestamp__mutmut)
def _parse_timestamp(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("Z", "+00:00"))


def x__parse_timestamp__mutmut_orig(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("Z", "+00:00"))


def x__parse_timestamp__mutmut_1(raw: str) -> datetime:
    return datetime.fromisoformat(None)


def x__parse_timestamp__mutmut_2(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace(None, "+00:00"))


def x__parse_timestamp__mutmut_3(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("Z", None))


def x__parse_timestamp__mutmut_4(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("+00:00"))


def x__parse_timestamp__mutmut_5(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("Z", ))


def x__parse_timestamp__mutmut_6(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("XXZXX", "+00:00"))


def x__parse_timestamp__mutmut_7(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("z", "+00:00"))


def x__parse_timestamp__mutmut_8(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("Z", "XX+00:00XX"))

mutants_x__parse_timestamp__mutmut['_mutmut_orig'] = x__parse_timestamp__mutmut_orig # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut['x__parse_timestamp__mutmut_1'] = x__parse_timestamp__mutmut_1 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut['x__parse_timestamp__mutmut_2'] = x__parse_timestamp__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut['x__parse_timestamp__mutmut_3'] = x__parse_timestamp__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut['x__parse_timestamp__mutmut_4'] = x__parse_timestamp__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut['x__parse_timestamp__mutmut_5'] = x__parse_timestamp__mutmut_5 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut['x__parse_timestamp__mutmut_6'] = x__parse_timestamp__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut['x__parse_timestamp__mutmut_7'] = x__parse_timestamp__mutmut_7 # type: ignore # mutmut generated
mutants_x__parse_timestamp__mutmut['x__parse_timestamp__mutmut_8'] = x__parse_timestamp__mutmut_8 # type: ignore # mutmut generated
