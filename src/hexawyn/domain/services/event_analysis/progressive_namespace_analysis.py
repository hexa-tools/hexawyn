from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field

from hexawyn.domain.models.event import EventSeverity
from hexawyn.domain.models.namespace_event import NamespaceEvent
from hexawyn.domain.services.event_analysis.classifier import ProgressiveEventAnalyzer
from hexawyn.domain.services.event_analysis.correlator import CorrelatedIncident, EventCorrelator
from hexawyn.domain.services.event_analysis.namespace_event_classifier import (
    classify_namespace_event,
)
from hexawyn.domain.services.event_analysis.runbook import (
    RunbookSuggestion,
    RunbookSuggestionEngine,
)

_TOP_AFFECTED_PODS_LIMIT = 3


@dataclass(frozen=True)
class NamespaceEventsSummary:
    """Phase 1 — high-level overview: total events, severity breakdown,
    and the pods most affected by event volume."""

    namespace: str
    total_events: int
    severity_breakdown: dict[str, int] = field(default_factory=dict)
    top_affected_pods: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class IncidentWithRunbook:
    incident: CorrelatedIncident
    runbook: RunbookSuggestion


@dataclass(frozen=True)
class CriticalEventsAnalysis:
    """Phase 2 — critical events correlated into incidents, each with its
    most relevant runbook suggestion."""

    namespace: str
    critical_incidents: list[IncidentWithRunbook] = field(default_factory=list)


def summarize_namespace_events(
    namespace: str, events: list[NamespaceEvent]
) -> NamespaceEventsSummary:
    """Phase 1 — ECA-19 provides the raw NamespaceEvent list (all types,
    including Normal); this reduces it to a triage-ready overview."""
    if not events:
        return NamespaceEventsSummary(namespace=namespace, total_events=0)

    classified = [classify_namespace_event(event, namespace) for event in events]
    overview = ProgressiveEventAnalyzer(classified).get_overview()

    return NamespaceEventsSummary(
        namespace=namespace,
        total_events=overview.total_events,
        severity_breakdown=overview.severity_distribution,
        top_affected_pods=_top_affected_pods(events),
    )


def analyze_critical_events(namespace: str, events: list[NamespaceEvent]) -> CriticalEventsAnalysis:
    """Phase 2 — on-demand drill-down: correlate critical events into
    incidents and attach the most relevant runbook to each."""
    classified = [classify_namespace_event(event, namespace) for event in events]
    critical = [event for event in classified if event.severity == EventSeverity.CRITICAL]

    incidents = EventCorrelator().correlate(critical)
    engine = RunbookSuggestionEngine()

    critical_incidents = [
        IncidentWithRunbook(incident=incident, runbook=engine.suggest(incident.reason))
        for incident in incidents
    ]
    return CriticalEventsAnalysis(namespace=namespace, critical_incidents=critical_incidents)


def _top_affected_pods(events: list[NamespaceEvent]) -> list[str]:
    counts = Counter(event.object for event in events)
    return [obj for obj, _ in counts.most_common(_TOP_AFFECTED_PODS_LIMIT)]
