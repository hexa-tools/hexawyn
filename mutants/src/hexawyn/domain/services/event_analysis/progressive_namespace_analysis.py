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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


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
mutants_x_summarize_namespace_events__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_summarize_namespace_events__mutmut)
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


def x_summarize_namespace_events__mutmut_orig(
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


def x_summarize_namespace_events__mutmut_1(
    namespace: str, events: list[NamespaceEvent]
) -> NamespaceEventsSummary:
    """Phase 1 — ECA-19 provides the raw NamespaceEvent list (all types,
    including Normal); this reduces it to a triage-ready overview."""
    if events:
        return NamespaceEventsSummary(namespace=namespace, total_events=0)

    classified = [classify_namespace_event(event, namespace) for event in events]
    overview = ProgressiveEventAnalyzer(classified).get_overview()

    return NamespaceEventsSummary(
        namespace=namespace,
        total_events=overview.total_events,
        severity_breakdown=overview.severity_distribution,
        top_affected_pods=_top_affected_pods(events),
    )


def x_summarize_namespace_events__mutmut_2(
    namespace: str, events: list[NamespaceEvent]
) -> NamespaceEventsSummary:
    """Phase 1 — ECA-19 provides the raw NamespaceEvent list (all types,
    including Normal); this reduces it to a triage-ready overview."""
    if not events:
        return NamespaceEventsSummary(namespace=None, total_events=0)

    classified = [classify_namespace_event(event, namespace) for event in events]
    overview = ProgressiveEventAnalyzer(classified).get_overview()

    return NamespaceEventsSummary(
        namespace=namespace,
        total_events=overview.total_events,
        severity_breakdown=overview.severity_distribution,
        top_affected_pods=_top_affected_pods(events),
    )


def x_summarize_namespace_events__mutmut_3(
    namespace: str, events: list[NamespaceEvent]
) -> NamespaceEventsSummary:
    """Phase 1 — ECA-19 provides the raw NamespaceEvent list (all types,
    including Normal); this reduces it to a triage-ready overview."""
    if not events:
        return NamespaceEventsSummary(namespace=namespace, total_events=None)

    classified = [classify_namespace_event(event, namespace) for event in events]
    overview = ProgressiveEventAnalyzer(classified).get_overview()

    return NamespaceEventsSummary(
        namespace=namespace,
        total_events=overview.total_events,
        severity_breakdown=overview.severity_distribution,
        top_affected_pods=_top_affected_pods(events),
    )


def x_summarize_namespace_events__mutmut_4(
    namespace: str, events: list[NamespaceEvent]
) -> NamespaceEventsSummary:
    """Phase 1 — ECA-19 provides the raw NamespaceEvent list (all types,
    including Normal); this reduces it to a triage-ready overview."""
    if not events:
        return NamespaceEventsSummary(total_events=0)

    classified = [classify_namespace_event(event, namespace) for event in events]
    overview = ProgressiveEventAnalyzer(classified).get_overview()

    return NamespaceEventsSummary(
        namespace=namespace,
        total_events=overview.total_events,
        severity_breakdown=overview.severity_distribution,
        top_affected_pods=_top_affected_pods(events),
    )


def x_summarize_namespace_events__mutmut_5(
    namespace: str, events: list[NamespaceEvent]
) -> NamespaceEventsSummary:
    """Phase 1 — ECA-19 provides the raw NamespaceEvent list (all types,
    including Normal); this reduces it to a triage-ready overview."""
    if not events:
        return NamespaceEventsSummary(namespace=namespace, )

    classified = [classify_namespace_event(event, namespace) for event in events]
    overview = ProgressiveEventAnalyzer(classified).get_overview()

    return NamespaceEventsSummary(
        namespace=namespace,
        total_events=overview.total_events,
        severity_breakdown=overview.severity_distribution,
        top_affected_pods=_top_affected_pods(events),
    )


def x_summarize_namespace_events__mutmut_6(
    namespace: str, events: list[NamespaceEvent]
) -> NamespaceEventsSummary:
    """Phase 1 — ECA-19 provides the raw NamespaceEvent list (all types,
    including Normal); this reduces it to a triage-ready overview."""
    if not events:
        return NamespaceEventsSummary(namespace=namespace, total_events=1)

    classified = [classify_namespace_event(event, namespace) for event in events]
    overview = ProgressiveEventAnalyzer(classified).get_overview()

    return NamespaceEventsSummary(
        namespace=namespace,
        total_events=overview.total_events,
        severity_breakdown=overview.severity_distribution,
        top_affected_pods=_top_affected_pods(events),
    )


def x_summarize_namespace_events__mutmut_7(
    namespace: str, events: list[NamespaceEvent]
) -> NamespaceEventsSummary:
    """Phase 1 — ECA-19 provides the raw NamespaceEvent list (all types,
    including Normal); this reduces it to a triage-ready overview."""
    if not events:
        return NamespaceEventsSummary(namespace=namespace, total_events=0)

    classified = None
    overview = ProgressiveEventAnalyzer(classified).get_overview()

    return NamespaceEventsSummary(
        namespace=namespace,
        total_events=overview.total_events,
        severity_breakdown=overview.severity_distribution,
        top_affected_pods=_top_affected_pods(events),
    )


def x_summarize_namespace_events__mutmut_8(
    namespace: str, events: list[NamespaceEvent]
) -> NamespaceEventsSummary:
    """Phase 1 — ECA-19 provides the raw NamespaceEvent list (all types,
    including Normal); this reduces it to a triage-ready overview."""
    if not events:
        return NamespaceEventsSummary(namespace=namespace, total_events=0)

    classified = [classify_namespace_event(None, namespace) for event in events]
    overview = ProgressiveEventAnalyzer(classified).get_overview()

    return NamespaceEventsSummary(
        namespace=namespace,
        total_events=overview.total_events,
        severity_breakdown=overview.severity_distribution,
        top_affected_pods=_top_affected_pods(events),
    )


def x_summarize_namespace_events__mutmut_9(
    namespace: str, events: list[NamespaceEvent]
) -> NamespaceEventsSummary:
    """Phase 1 — ECA-19 provides the raw NamespaceEvent list (all types,
    including Normal); this reduces it to a triage-ready overview."""
    if not events:
        return NamespaceEventsSummary(namespace=namespace, total_events=0)

    classified = [classify_namespace_event(event, None) for event in events]
    overview = ProgressiveEventAnalyzer(classified).get_overview()

    return NamespaceEventsSummary(
        namespace=namespace,
        total_events=overview.total_events,
        severity_breakdown=overview.severity_distribution,
        top_affected_pods=_top_affected_pods(events),
    )


def x_summarize_namespace_events__mutmut_10(
    namespace: str, events: list[NamespaceEvent]
) -> NamespaceEventsSummary:
    """Phase 1 — ECA-19 provides the raw NamespaceEvent list (all types,
    including Normal); this reduces it to a triage-ready overview."""
    if not events:
        return NamespaceEventsSummary(namespace=namespace, total_events=0)

    classified = [classify_namespace_event(namespace) for event in events]
    overview = ProgressiveEventAnalyzer(classified).get_overview()

    return NamespaceEventsSummary(
        namespace=namespace,
        total_events=overview.total_events,
        severity_breakdown=overview.severity_distribution,
        top_affected_pods=_top_affected_pods(events),
    )


def x_summarize_namespace_events__mutmut_11(
    namespace: str, events: list[NamespaceEvent]
) -> NamespaceEventsSummary:
    """Phase 1 — ECA-19 provides the raw NamespaceEvent list (all types,
    including Normal); this reduces it to a triage-ready overview."""
    if not events:
        return NamespaceEventsSummary(namespace=namespace, total_events=0)

    classified = [classify_namespace_event(event, ) for event in events]
    overview = ProgressiveEventAnalyzer(classified).get_overview()

    return NamespaceEventsSummary(
        namespace=namespace,
        total_events=overview.total_events,
        severity_breakdown=overview.severity_distribution,
        top_affected_pods=_top_affected_pods(events),
    )


def x_summarize_namespace_events__mutmut_12(
    namespace: str, events: list[NamespaceEvent]
) -> NamespaceEventsSummary:
    """Phase 1 — ECA-19 provides the raw NamespaceEvent list (all types,
    including Normal); this reduces it to a triage-ready overview."""
    if not events:
        return NamespaceEventsSummary(namespace=namespace, total_events=0)

    classified = [classify_namespace_event(event, namespace) for event in events]
    overview = None

    return NamespaceEventsSummary(
        namespace=namespace,
        total_events=overview.total_events,
        severity_breakdown=overview.severity_distribution,
        top_affected_pods=_top_affected_pods(events),
    )


def x_summarize_namespace_events__mutmut_13(
    namespace: str, events: list[NamespaceEvent]
) -> NamespaceEventsSummary:
    """Phase 1 — ECA-19 provides the raw NamespaceEvent list (all types,
    including Normal); this reduces it to a triage-ready overview."""
    if not events:
        return NamespaceEventsSummary(namespace=namespace, total_events=0)

    classified = [classify_namespace_event(event, namespace) for event in events]
    overview = ProgressiveEventAnalyzer(None).get_overview()

    return NamespaceEventsSummary(
        namespace=namespace,
        total_events=overview.total_events,
        severity_breakdown=overview.severity_distribution,
        top_affected_pods=_top_affected_pods(events),
    )


def x_summarize_namespace_events__mutmut_14(
    namespace: str, events: list[NamespaceEvent]
) -> NamespaceEventsSummary:
    """Phase 1 — ECA-19 provides the raw NamespaceEvent list (all types,
    including Normal); this reduces it to a triage-ready overview."""
    if not events:
        return NamespaceEventsSummary(namespace=namespace, total_events=0)

    classified = [classify_namespace_event(event, namespace) for event in events]
    overview = ProgressiveEventAnalyzer(classified).get_overview()

    return NamespaceEventsSummary(
        namespace=None,
        total_events=overview.total_events,
        severity_breakdown=overview.severity_distribution,
        top_affected_pods=_top_affected_pods(events),
    )


def x_summarize_namespace_events__mutmut_15(
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
        total_events=None,
        severity_breakdown=overview.severity_distribution,
        top_affected_pods=_top_affected_pods(events),
    )


def x_summarize_namespace_events__mutmut_16(
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
        severity_breakdown=None,
        top_affected_pods=_top_affected_pods(events),
    )


def x_summarize_namespace_events__mutmut_17(
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
        top_affected_pods=None,
    )


def x_summarize_namespace_events__mutmut_18(
    namespace: str, events: list[NamespaceEvent]
) -> NamespaceEventsSummary:
    """Phase 1 — ECA-19 provides the raw NamespaceEvent list (all types,
    including Normal); this reduces it to a triage-ready overview."""
    if not events:
        return NamespaceEventsSummary(namespace=namespace, total_events=0)

    classified = [classify_namespace_event(event, namespace) for event in events]
    overview = ProgressiveEventAnalyzer(classified).get_overview()

    return NamespaceEventsSummary(
        total_events=overview.total_events,
        severity_breakdown=overview.severity_distribution,
        top_affected_pods=_top_affected_pods(events),
    )


def x_summarize_namespace_events__mutmut_19(
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
        severity_breakdown=overview.severity_distribution,
        top_affected_pods=_top_affected_pods(events),
    )


def x_summarize_namespace_events__mutmut_20(
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
        top_affected_pods=_top_affected_pods(events),
    )


def x_summarize_namespace_events__mutmut_21(
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
        )


def x_summarize_namespace_events__mutmut_22(
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
        top_affected_pods=_top_affected_pods(None),
    )

mutants_x_summarize_namespace_events__mutmut['_mutmut_orig'] = x_summarize_namespace_events__mutmut_orig # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_1'] = x_summarize_namespace_events__mutmut_1 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_2'] = x_summarize_namespace_events__mutmut_2 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_3'] = x_summarize_namespace_events__mutmut_3 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_4'] = x_summarize_namespace_events__mutmut_4 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_5'] = x_summarize_namespace_events__mutmut_5 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_6'] = x_summarize_namespace_events__mutmut_6 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_7'] = x_summarize_namespace_events__mutmut_7 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_8'] = x_summarize_namespace_events__mutmut_8 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_9'] = x_summarize_namespace_events__mutmut_9 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_10'] = x_summarize_namespace_events__mutmut_10 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_11'] = x_summarize_namespace_events__mutmut_11 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_12'] = x_summarize_namespace_events__mutmut_12 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_13'] = x_summarize_namespace_events__mutmut_13 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_14'] = x_summarize_namespace_events__mutmut_14 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_15'] = x_summarize_namespace_events__mutmut_15 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_16'] = x_summarize_namespace_events__mutmut_16 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_17'] = x_summarize_namespace_events__mutmut_17 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_18'] = x_summarize_namespace_events__mutmut_18 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_19'] = x_summarize_namespace_events__mutmut_19 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_20'] = x_summarize_namespace_events__mutmut_20 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_21'] = x_summarize_namespace_events__mutmut_21 # type: ignore # mutmut generated
mutants_x_summarize_namespace_events__mutmut['x_summarize_namespace_events__mutmut_22'] = x_summarize_namespace_events__mutmut_22 # type: ignore # mutmut generated
mutants_x_analyze_critical_events__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_analyze_critical_events__mutmut)
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


def x_analyze_critical_events__mutmut_orig(namespace: str, events: list[NamespaceEvent]) -> CriticalEventsAnalysis:
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


def x_analyze_critical_events__mutmut_1(namespace: str, events: list[NamespaceEvent]) -> CriticalEventsAnalysis:
    """Phase 2 — on-demand drill-down: correlate critical events into
    incidents and attach the most relevant runbook to each."""
    classified = None
    critical = [event for event in classified if event.severity == EventSeverity.CRITICAL]

    incidents = EventCorrelator().correlate(critical)
    engine = RunbookSuggestionEngine()

    critical_incidents = [
        IncidentWithRunbook(incident=incident, runbook=engine.suggest(incident.reason))
        for incident in incidents
    ]
    return CriticalEventsAnalysis(namespace=namespace, critical_incidents=critical_incidents)


def x_analyze_critical_events__mutmut_2(namespace: str, events: list[NamespaceEvent]) -> CriticalEventsAnalysis:
    """Phase 2 — on-demand drill-down: correlate critical events into
    incidents and attach the most relevant runbook to each."""
    classified = [classify_namespace_event(None, namespace) for event in events]
    critical = [event for event in classified if event.severity == EventSeverity.CRITICAL]

    incidents = EventCorrelator().correlate(critical)
    engine = RunbookSuggestionEngine()

    critical_incidents = [
        IncidentWithRunbook(incident=incident, runbook=engine.suggest(incident.reason))
        for incident in incidents
    ]
    return CriticalEventsAnalysis(namespace=namespace, critical_incidents=critical_incidents)


def x_analyze_critical_events__mutmut_3(namespace: str, events: list[NamespaceEvent]) -> CriticalEventsAnalysis:
    """Phase 2 — on-demand drill-down: correlate critical events into
    incidents and attach the most relevant runbook to each."""
    classified = [classify_namespace_event(event, None) for event in events]
    critical = [event for event in classified if event.severity == EventSeverity.CRITICAL]

    incidents = EventCorrelator().correlate(critical)
    engine = RunbookSuggestionEngine()

    critical_incidents = [
        IncidentWithRunbook(incident=incident, runbook=engine.suggest(incident.reason))
        for incident in incidents
    ]
    return CriticalEventsAnalysis(namespace=namespace, critical_incidents=critical_incidents)


def x_analyze_critical_events__mutmut_4(namespace: str, events: list[NamespaceEvent]) -> CriticalEventsAnalysis:
    """Phase 2 — on-demand drill-down: correlate critical events into
    incidents and attach the most relevant runbook to each."""
    classified = [classify_namespace_event(namespace) for event in events]
    critical = [event for event in classified if event.severity == EventSeverity.CRITICAL]

    incidents = EventCorrelator().correlate(critical)
    engine = RunbookSuggestionEngine()

    critical_incidents = [
        IncidentWithRunbook(incident=incident, runbook=engine.suggest(incident.reason))
        for incident in incidents
    ]
    return CriticalEventsAnalysis(namespace=namespace, critical_incidents=critical_incidents)


def x_analyze_critical_events__mutmut_5(namespace: str, events: list[NamespaceEvent]) -> CriticalEventsAnalysis:
    """Phase 2 — on-demand drill-down: correlate critical events into
    incidents and attach the most relevant runbook to each."""
    classified = [classify_namespace_event(event, ) for event in events]
    critical = [event for event in classified if event.severity == EventSeverity.CRITICAL]

    incidents = EventCorrelator().correlate(critical)
    engine = RunbookSuggestionEngine()

    critical_incidents = [
        IncidentWithRunbook(incident=incident, runbook=engine.suggest(incident.reason))
        for incident in incidents
    ]
    return CriticalEventsAnalysis(namespace=namespace, critical_incidents=critical_incidents)


def x_analyze_critical_events__mutmut_6(namespace: str, events: list[NamespaceEvent]) -> CriticalEventsAnalysis:
    """Phase 2 — on-demand drill-down: correlate critical events into
    incidents and attach the most relevant runbook to each."""
    classified = [classify_namespace_event(event, namespace) for event in events]
    critical = None

    incidents = EventCorrelator().correlate(critical)
    engine = RunbookSuggestionEngine()

    critical_incidents = [
        IncidentWithRunbook(incident=incident, runbook=engine.suggest(incident.reason))
        for incident in incidents
    ]
    return CriticalEventsAnalysis(namespace=namespace, critical_incidents=critical_incidents)


def x_analyze_critical_events__mutmut_7(namespace: str, events: list[NamespaceEvent]) -> CriticalEventsAnalysis:
    """Phase 2 — on-demand drill-down: correlate critical events into
    incidents and attach the most relevant runbook to each."""
    classified = [classify_namespace_event(event, namespace) for event in events]
    critical = [event for event in classified if event.severity != EventSeverity.CRITICAL]

    incidents = EventCorrelator().correlate(critical)
    engine = RunbookSuggestionEngine()

    critical_incidents = [
        IncidentWithRunbook(incident=incident, runbook=engine.suggest(incident.reason))
        for incident in incidents
    ]
    return CriticalEventsAnalysis(namespace=namespace, critical_incidents=critical_incidents)


def x_analyze_critical_events__mutmut_8(namespace: str, events: list[NamespaceEvent]) -> CriticalEventsAnalysis:
    """Phase 2 — on-demand drill-down: correlate critical events into
    incidents and attach the most relevant runbook to each."""
    classified = [classify_namespace_event(event, namespace) for event in events]
    critical = [event for event in classified if event.severity == EventSeverity.CRITICAL]

    incidents = None
    engine = RunbookSuggestionEngine()

    critical_incidents = [
        IncidentWithRunbook(incident=incident, runbook=engine.suggest(incident.reason))
        for incident in incidents
    ]
    return CriticalEventsAnalysis(namespace=namespace, critical_incidents=critical_incidents)


def x_analyze_critical_events__mutmut_9(namespace: str, events: list[NamespaceEvent]) -> CriticalEventsAnalysis:
    """Phase 2 — on-demand drill-down: correlate critical events into
    incidents and attach the most relevant runbook to each."""
    classified = [classify_namespace_event(event, namespace) for event in events]
    critical = [event for event in classified if event.severity == EventSeverity.CRITICAL]

    incidents = EventCorrelator().correlate(None)
    engine = RunbookSuggestionEngine()

    critical_incidents = [
        IncidentWithRunbook(incident=incident, runbook=engine.suggest(incident.reason))
        for incident in incidents
    ]
    return CriticalEventsAnalysis(namespace=namespace, critical_incidents=critical_incidents)


def x_analyze_critical_events__mutmut_10(namespace: str, events: list[NamespaceEvent]) -> CriticalEventsAnalysis:
    """Phase 2 — on-demand drill-down: correlate critical events into
    incidents and attach the most relevant runbook to each."""
    classified = [classify_namespace_event(event, namespace) for event in events]
    critical = [event for event in classified if event.severity == EventSeverity.CRITICAL]

    incidents = EventCorrelator().correlate(critical)
    engine = None

    critical_incidents = [
        IncidentWithRunbook(incident=incident, runbook=engine.suggest(incident.reason))
        for incident in incidents
    ]
    return CriticalEventsAnalysis(namespace=namespace, critical_incidents=critical_incidents)


def x_analyze_critical_events__mutmut_11(namespace: str, events: list[NamespaceEvent]) -> CriticalEventsAnalysis:
    """Phase 2 — on-demand drill-down: correlate critical events into
    incidents and attach the most relevant runbook to each."""
    classified = [classify_namespace_event(event, namespace) for event in events]
    critical = [event for event in classified if event.severity == EventSeverity.CRITICAL]

    incidents = EventCorrelator().correlate(critical)
    engine = RunbookSuggestionEngine()

    critical_incidents = None
    return CriticalEventsAnalysis(namespace=namespace, critical_incidents=critical_incidents)


def x_analyze_critical_events__mutmut_12(namespace: str, events: list[NamespaceEvent]) -> CriticalEventsAnalysis:
    """Phase 2 — on-demand drill-down: correlate critical events into
    incidents and attach the most relevant runbook to each."""
    classified = [classify_namespace_event(event, namespace) for event in events]
    critical = [event for event in classified if event.severity == EventSeverity.CRITICAL]

    incidents = EventCorrelator().correlate(critical)
    engine = RunbookSuggestionEngine()

    critical_incidents = [
        IncidentWithRunbook(incident=None, runbook=engine.suggest(incident.reason))
        for incident in incidents
    ]
    return CriticalEventsAnalysis(namespace=namespace, critical_incidents=critical_incidents)


def x_analyze_critical_events__mutmut_13(namespace: str, events: list[NamespaceEvent]) -> CriticalEventsAnalysis:
    """Phase 2 — on-demand drill-down: correlate critical events into
    incidents and attach the most relevant runbook to each."""
    classified = [classify_namespace_event(event, namespace) for event in events]
    critical = [event for event in classified if event.severity == EventSeverity.CRITICAL]

    incidents = EventCorrelator().correlate(critical)
    engine = RunbookSuggestionEngine()

    critical_incidents = [
        IncidentWithRunbook(incident=incident, runbook=None)
        for incident in incidents
    ]
    return CriticalEventsAnalysis(namespace=namespace, critical_incidents=critical_incidents)


def x_analyze_critical_events__mutmut_14(namespace: str, events: list[NamespaceEvent]) -> CriticalEventsAnalysis:
    """Phase 2 — on-demand drill-down: correlate critical events into
    incidents and attach the most relevant runbook to each."""
    classified = [classify_namespace_event(event, namespace) for event in events]
    critical = [event for event in classified if event.severity == EventSeverity.CRITICAL]

    incidents = EventCorrelator().correlate(critical)
    engine = RunbookSuggestionEngine()

    critical_incidents = [
        IncidentWithRunbook(runbook=engine.suggest(incident.reason))
        for incident in incidents
    ]
    return CriticalEventsAnalysis(namespace=namespace, critical_incidents=critical_incidents)


def x_analyze_critical_events__mutmut_15(namespace: str, events: list[NamespaceEvent]) -> CriticalEventsAnalysis:
    """Phase 2 — on-demand drill-down: correlate critical events into
    incidents and attach the most relevant runbook to each."""
    classified = [classify_namespace_event(event, namespace) for event in events]
    critical = [event for event in classified if event.severity == EventSeverity.CRITICAL]

    incidents = EventCorrelator().correlate(critical)
    engine = RunbookSuggestionEngine()

    critical_incidents = [
        IncidentWithRunbook(incident=incident, )
        for incident in incidents
    ]
    return CriticalEventsAnalysis(namespace=namespace, critical_incidents=critical_incidents)


def x_analyze_critical_events__mutmut_16(namespace: str, events: list[NamespaceEvent]) -> CriticalEventsAnalysis:
    """Phase 2 — on-demand drill-down: correlate critical events into
    incidents and attach the most relevant runbook to each."""
    classified = [classify_namespace_event(event, namespace) for event in events]
    critical = [event for event in classified if event.severity == EventSeverity.CRITICAL]

    incidents = EventCorrelator().correlate(critical)
    engine = RunbookSuggestionEngine()

    critical_incidents = [
        IncidentWithRunbook(incident=incident, runbook=engine.suggest(None))
        for incident in incidents
    ]
    return CriticalEventsAnalysis(namespace=namespace, critical_incidents=critical_incidents)


def x_analyze_critical_events__mutmut_17(namespace: str, events: list[NamespaceEvent]) -> CriticalEventsAnalysis:
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
    return CriticalEventsAnalysis(namespace=None, critical_incidents=critical_incidents)


def x_analyze_critical_events__mutmut_18(namespace: str, events: list[NamespaceEvent]) -> CriticalEventsAnalysis:
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
    return CriticalEventsAnalysis(namespace=namespace, critical_incidents=None)


def x_analyze_critical_events__mutmut_19(namespace: str, events: list[NamespaceEvent]) -> CriticalEventsAnalysis:
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
    return CriticalEventsAnalysis(critical_incidents=critical_incidents)


def x_analyze_critical_events__mutmut_20(namespace: str, events: list[NamespaceEvent]) -> CriticalEventsAnalysis:
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
    return CriticalEventsAnalysis(namespace=namespace, )

mutants_x_analyze_critical_events__mutmut['_mutmut_orig'] = x_analyze_critical_events__mutmut_orig # type: ignore # mutmut generated
mutants_x_analyze_critical_events__mutmut['x_analyze_critical_events__mutmut_1'] = x_analyze_critical_events__mutmut_1 # type: ignore # mutmut generated
mutants_x_analyze_critical_events__mutmut['x_analyze_critical_events__mutmut_2'] = x_analyze_critical_events__mutmut_2 # type: ignore # mutmut generated
mutants_x_analyze_critical_events__mutmut['x_analyze_critical_events__mutmut_3'] = x_analyze_critical_events__mutmut_3 # type: ignore # mutmut generated
mutants_x_analyze_critical_events__mutmut['x_analyze_critical_events__mutmut_4'] = x_analyze_critical_events__mutmut_4 # type: ignore # mutmut generated
mutants_x_analyze_critical_events__mutmut['x_analyze_critical_events__mutmut_5'] = x_analyze_critical_events__mutmut_5 # type: ignore # mutmut generated
mutants_x_analyze_critical_events__mutmut['x_analyze_critical_events__mutmut_6'] = x_analyze_critical_events__mutmut_6 # type: ignore # mutmut generated
mutants_x_analyze_critical_events__mutmut['x_analyze_critical_events__mutmut_7'] = x_analyze_critical_events__mutmut_7 # type: ignore # mutmut generated
mutants_x_analyze_critical_events__mutmut['x_analyze_critical_events__mutmut_8'] = x_analyze_critical_events__mutmut_8 # type: ignore # mutmut generated
mutants_x_analyze_critical_events__mutmut['x_analyze_critical_events__mutmut_9'] = x_analyze_critical_events__mutmut_9 # type: ignore # mutmut generated
mutants_x_analyze_critical_events__mutmut['x_analyze_critical_events__mutmut_10'] = x_analyze_critical_events__mutmut_10 # type: ignore # mutmut generated
mutants_x_analyze_critical_events__mutmut['x_analyze_critical_events__mutmut_11'] = x_analyze_critical_events__mutmut_11 # type: ignore # mutmut generated
mutants_x_analyze_critical_events__mutmut['x_analyze_critical_events__mutmut_12'] = x_analyze_critical_events__mutmut_12 # type: ignore # mutmut generated
mutants_x_analyze_critical_events__mutmut['x_analyze_critical_events__mutmut_13'] = x_analyze_critical_events__mutmut_13 # type: ignore # mutmut generated
mutants_x_analyze_critical_events__mutmut['x_analyze_critical_events__mutmut_14'] = x_analyze_critical_events__mutmut_14 # type: ignore # mutmut generated
mutants_x_analyze_critical_events__mutmut['x_analyze_critical_events__mutmut_15'] = x_analyze_critical_events__mutmut_15 # type: ignore # mutmut generated
mutants_x_analyze_critical_events__mutmut['x_analyze_critical_events__mutmut_16'] = x_analyze_critical_events__mutmut_16 # type: ignore # mutmut generated
mutants_x_analyze_critical_events__mutmut['x_analyze_critical_events__mutmut_17'] = x_analyze_critical_events__mutmut_17 # type: ignore # mutmut generated
mutants_x_analyze_critical_events__mutmut['x_analyze_critical_events__mutmut_18'] = x_analyze_critical_events__mutmut_18 # type: ignore # mutmut generated
mutants_x_analyze_critical_events__mutmut['x_analyze_critical_events__mutmut_19'] = x_analyze_critical_events__mutmut_19 # type: ignore # mutmut generated
mutants_x_analyze_critical_events__mutmut['x_analyze_critical_events__mutmut_20'] = x_analyze_critical_events__mutmut_20 # type: ignore # mutmut generated
mutants_x__top_affected_pods__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__top_affected_pods__mutmut)
def _top_affected_pods(events: list[NamespaceEvent]) -> list[str]:
    counts = Counter(event.object for event in events)
    return [obj for obj, _ in counts.most_common(_TOP_AFFECTED_PODS_LIMIT)]


def x__top_affected_pods__mutmut_orig(events: list[NamespaceEvent]) -> list[str]:
    counts = Counter(event.object for event in events)
    return [obj for obj, _ in counts.most_common(_TOP_AFFECTED_PODS_LIMIT)]


def x__top_affected_pods__mutmut_1(events: list[NamespaceEvent]) -> list[str]:
    counts = None
    return [obj for obj, _ in counts.most_common(_TOP_AFFECTED_PODS_LIMIT)]


def x__top_affected_pods__mutmut_2(events: list[NamespaceEvent]) -> list[str]:
    counts = Counter(None)
    return [obj for obj, _ in counts.most_common(_TOP_AFFECTED_PODS_LIMIT)]


def x__top_affected_pods__mutmut_3(events: list[NamespaceEvent]) -> list[str]:
    counts = Counter(event.object for event in events)
    return [obj for obj, _ in counts.most_common(None)]

mutants_x__top_affected_pods__mutmut['_mutmut_orig'] = x__top_affected_pods__mutmut_orig # type: ignore # mutmut generated
mutants_x__top_affected_pods__mutmut['x__top_affected_pods__mutmut_1'] = x__top_affected_pods__mutmut_1 # type: ignore # mutmut generated
mutants_x__top_affected_pods__mutmut['x__top_affected_pods__mutmut_2'] = x__top_affected_pods__mutmut_2 # type: ignore # mutmut generated
mutants_x__top_affected_pods__mutmut['x__top_affected_pods__mutmut_3'] = x__top_affected_pods__mutmut_3 # type: ignore # mutmut generated
