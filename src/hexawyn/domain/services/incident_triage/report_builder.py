from __future__ import annotations

from collections import defaultdict
from datetime import UTC, datetime

from hexawyn.application.ports.driven.k8s_port import PodInfo
from hexawyn.domain.models.analyze_pod_logs import PodLogLine
from hexawyn.domain.models.constants import IncidentTriageConstants
from hexawyn.domain.models.incident_triage import (
    ImpactAssessment,
    IncidentCauseCategory,
    IncidentTriageReport,
    IncidentTriageRequest,
    RootCauseCandidate,
    TimelineEntry,
)
from hexawyn.domain.models.namespace_event import NamespaceEvent
from hexawyn.domain.models.pipeline_failure_analysis import FailureAnalysis, FailureType
from hexawyn.domain.models.scoring import RcaScoringConfig
from hexawyn.domain.services.failure_analysis.scorer import RcaScorer
from hexawyn.domain.services.incident_triage.root_cause_classifier import (
    classify_incident_cause,
    remediation_for,
)

_cfg = IncidentTriageConstants()
_scorer = RcaScorer(RcaScoringConfig())
_NORMAL_EVENT_TYPE = "Normal"
_FAILURE_EVENT_TYPES = frozenset({"Warning", "Error"})

_FAILURE_TYPE_TO_CAUSE_CATEGORY: dict[FailureType, IncidentCauseCategory] = {
    FailureType.FLAKY_TEST: IncidentCauseCategory.DEPLOYMENT,
    FailureType.REGRESSION: IncidentCauseCategory.DEPLOYMENT,
    FailureType.INFRASTRUCTURE: IncidentCauseCategory.NETWORK,
    FailureType.DEPENDENCY: IncidentCauseCategory.IMAGE_OR_CONFIG,
    FailureType.CONFIG_ERROR: IncidentCauseCategory.IMAGE_OR_CONFIG,
}


def generate_incident_triage_report(
    request: IncidentTriageRequest,
    events: list[NamespaceEvent],
    pods: list[PodInfo],
    pod_logs: dict[str, list[PodLogLine]],
    pipeline_failures: list[tuple[str, FailureAnalysis]],
    related_namespace_events: dict[str, list[NamespaceEvent]] | None = None,
    observed_at: datetime | None = None,
) -> IncidentTriageReport:
    """Composes namespace events, pod logs, pod status, and pipeline-failure
    RCA into a single incident triage report. Pure domain function — all
    inputs are already fetched through their respective driven ports.
    """
    observed_at = observed_at or datetime.now(UTC)
    related_namespace_events = related_namespace_events or {}

    if not events and not pods and not any(pod_logs.values()) and not pipeline_failures:
        return IncidentTriageReport(
            namespace=request.namespace,
            time_window_minutes=request.time_window_minutes,
            insufficient_data=True,
            data_checked=[
                f"namespace events ({request.time_window_minutes}m window)",
                "pod status",
                "pod logs",
                "pipeline runs",
            ],
        )

    all_entries = _build_all_entries(events, pod_logs, pipeline_failures)
    failure_entries = [entry for entry in all_entries if entry.severity in _FAILURE_EVENT_TYPES]

    root_causes = _build_root_causes(failure_entries, pipeline_failures)
    remediation_steps = list(dict.fromkeys(remediation_for(c.category) for c in root_causes))

    resolved, resolution_time, mttr_minutes = _detect_resolution(all_entries, failure_entries)

    timeline = sorted(
        [
            entry
            for entry in all_entries
            if entry.severity != _NORMAL_EVENT_TYPE or entry.timestamp == resolution_time
        ],
        key=lambda entry: entry.timestamp,
    )

    impact = _build_impact(
        failure_entries, pods, root_causes, resolved, resolution_time, observed_at
    )

    ntp_drift_detected, ntp_drift_note = _detect_ntp_drift(all_entries)

    cross_namespace_correlation = _correlate_cross_namespace(root_causes, related_namespace_events)

    return IncidentTriageReport(
        namespace=request.namespace,
        time_window_minutes=request.time_window_minutes,
        timeline=timeline,
        root_causes=root_causes,
        impact=impact,
        remediation_steps=remediation_steps,
        resolved=resolved,
        resolution_time=resolution_time,
        mttr_minutes=mttr_minutes,
        ntp_drift_detected=ntp_drift_detected,
        ntp_drift_note=ntp_drift_note,
        cross_namespace_correlation=cross_namespace_correlation,
    )


def _build_all_entries(
    events: list[NamespaceEvent],
    pod_logs: dict[str, list[PodLogLine]],
    pipeline_failures: list[tuple[str, FailureAnalysis]],
) -> list[TimelineEntry]:
    entries: list[TimelineEntry] = []

    for event in events:
        entries.append(
            TimelineEntry(
                timestamp=event.last_seen,
                source="event",
                namespace="",
                object=event.object,
                reason=event.reason,
                message=event.message,
                severity=event.event_type,
            )
        )

    for pod_name, lines in pod_logs.items():
        for line in lines:
            if not (line.is_error or line.is_warning):
                continue
            entries.append(
                TimelineEntry(
                    timestamp=line.timestamp,
                    source="log",
                    namespace="",
                    object=pod_name,
                    reason="log_error" if line.is_error else "log_warning",
                    message=line.message,
                    severity="Error" if line.is_error else "Warning",
                )
            )

    for start_time, failure in pipeline_failures:
        entries.append(
            TimelineEntry(
                timestamp=start_time,
                source="pipeline",
                namespace="",
                object=failure.task_name,
                reason=failure.failure_type.value,
                message=failure.root_cause,
                severity="Error",
            )
        )

    return sorted(entries, key=lambda entry: entry.timestamp)


def _build_root_causes(
    failure_entries: list[TimelineEntry],
    pipeline_failures: list[tuple[str, FailureAnalysis]],
) -> list[RootCauseCandidate]:
    candidates: list[RootCauseCandidate] = []

    by_category: dict[IncidentCauseCategory, list[TimelineEntry]] = defaultdict(list)
    for entry in failure_entries:
        if entry.source == "pipeline":
            continue
        category = classify_incident_cause(f"{entry.reason} {entry.message}")
        by_category[category].append(entry)

    for category, group in by_category.items():
        involved_objects = list(dict.fromkeys(entry.object for entry in group))
        confidence = _scorer.calculate_confidence(
            logs_analyzed=any(entry.source == "log" for entry in group),
            root_cause_found=category != IncidentCauseCategory.UNKNOWN,
            timeline_available=len(group) > 1,
        )
        candidates.append(
            RootCauseCandidate(
                description=_describe_candidate(category, involved_objects),
                category=category,
                confidence=confidence.value,
                evidence=[f"{e.timestamp} {e.object}: {e.reason} — {e.message}" for e in group],
                involved_objects=involved_objects,
            )
        )

    for start_time, failure in pipeline_failures:
        candidates.append(
            RootCauseCandidate(
                description=f"{failure.task_name}: {failure.root_cause}",
                category=_FAILURE_TYPE_TO_CAUSE_CATEGORY[failure.failure_type],
                confidence=failure.confidence,
                evidence=[f"{start_time} {failure.task_name}: {failure.root_cause}"],
                involved_objects=[failure.task_name],
            )
        )

    candidates.sort(key=lambda candidate: candidate.confidence, reverse=True)
    return candidates


def _describe_candidate(category: IncidentCauseCategory, involved_objects: list[str]) -> str:
    if len(involved_objects) > 1:
        return (
            f"{category.value.replace('_', ' ')} issue affecting {len(involved_objects)} "
            f"objects — likely a shared root cause"
        )
    return f"{category.value.replace('_', ' ')} issue on {involved_objects[0]}"


def _detect_resolution(
    all_entries: list[TimelineEntry], failure_entries: list[TimelineEntry]
) -> tuple[bool, str | None, int | None]:
    if not failure_entries:
        return False, None, None

    first_failure_time = min(entry.timestamp for entry in failure_entries)
    last_failure_time = max(entry.timestamp for entry in failure_entries)

    recovery_candidates = [
        entry
        for entry in all_entries
        if entry.severity == _NORMAL_EVENT_TYPE and entry.timestamp > last_failure_time
    ]
    if not recovery_candidates:
        return False, None, None

    resolution_time = min(entry.timestamp for entry in recovery_candidates)
    mttr_minutes = int(
        (_parse_timestamp(resolution_time) - _parse_timestamp(first_failure_time)).total_seconds()
        // 60
    )
    return True, resolution_time, mttr_minutes


def _build_impact(
    failure_entries: list[TimelineEntry],
    pods: list[PodInfo],
    root_causes: list[RootCauseCandidate],
    resolved: bool,
    resolution_time: str | None,
    observed_at: datetime,
) -> ImpactAssessment:
    if not failure_entries:
        return ImpactAssessment()

    affected_services = set(entry.object for entry in failure_entries)
    affected_services.update(pod["name"] for pod in pods if pod["status"] != "Running")

    impact_score = _scorer.calculate_impact(
        affected_tasks=len(affected_services),
        related_incidents=max(len(root_causes) - 1, 0),
        timeline_events=len(failure_entries),
    )

    first_failure_time = min(entry.timestamp for entry in failure_entries)
    if resolved and resolution_time:
        duration_minutes = int(
            (
                _parse_timestamp(resolution_time) - _parse_timestamp(first_failure_time)
            ).total_seconds()
            // 60
        )
    else:
        duration_minutes = int(
            (observed_at - _parse_timestamp(first_failure_time)).total_seconds() // 60
        )

    estimated_user_impact = (
        f"{impact_score.label.capitalize()} — {len(affected_services)} service(s) affected "
        f"(cascade risk: {impact_score.cascade_risk})"
    )

    return ImpactAssessment(
        affected_services=sorted(affected_services),
        estimated_user_impact=estimated_user_impact,
        duration_minutes=duration_minutes,
        ongoing=not resolved,
    )


def _detect_ntp_drift(all_entries: list[TimelineEntry]) -> tuple[bool, str]:
    earliest_event_by_object: dict[str, str] = {}
    for entry in all_entries:
        if entry.source != "event":
            continue
        existing = earliest_event_by_object.get(entry.object)
        if existing is None or entry.timestamp < existing:
            earliest_event_by_object[entry.object] = entry.timestamp

    for entry in all_entries:
        if entry.source != "log" or entry.object not in earliest_event_by_object:
            continue
        event_time = earliest_event_by_object[entry.object]
        diff_seconds = (
            _parse_timestamp(event_time) - _parse_timestamp(entry.timestamp)
        ).total_seconds()
        if diff_seconds > _cfg.ntp_drift_threshold_seconds:
            return True, (
                f"Log and event timestamps for {entry.object} differ by {int(diff_seconds)}s "
                "— possible clock drift between log shipper and API server."
            )
    return False, ""


def _correlate_cross_namespace(
    root_causes: list[RootCauseCandidate],
    related_namespace_events: dict[str, list[NamespaceEvent]],
) -> list[str]:
    if not root_causes or not related_namespace_events:
        return []

    top_category = root_causes[0].category
    correlated: list[str] = []
    for namespace, events in related_namespace_events.items():
        for event in events:
            if event.event_type not in _FAILURE_EVENT_TYPES:
                continue
            category = classify_incident_cause(f"{event.reason} {event.message}")
            if category == top_category:
                correlated.append(f"{namespace}: {event.object} ({event.reason})")
    return correlated


def _parse_timestamp(raw: str) -> datetime:
    return datetime.fromisoformat(raw.replace("Z", "+00:00"))
