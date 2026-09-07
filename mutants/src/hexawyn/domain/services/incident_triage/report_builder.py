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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_generate_incident_triage_report__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_generate_incident_triage_report__mutmut)
def generate_incident_triage_report(  # noqa: PLR0913
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


def x_generate_incident_triage_report__mutmut_orig(  # noqa: PLR0913
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


def x_generate_incident_triage_report__mutmut_1(  # noqa: PLR0913
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
    observed_at = None
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


def x_generate_incident_triage_report__mutmut_2(  # noqa: PLR0913
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
    observed_at = observed_at and datetime.now(UTC)
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


def x_generate_incident_triage_report__mutmut_3(  # noqa: PLR0913
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
    observed_at = observed_at or datetime.now(None)
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


def x_generate_incident_triage_report__mutmut_4(  # noqa: PLR0913
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
    related_namespace_events = None

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


def x_generate_incident_triage_report__mutmut_5(  # noqa: PLR0913
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
    related_namespace_events = related_namespace_events and {}

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


def x_generate_incident_triage_report__mutmut_6(  # noqa: PLR0913
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

    if not events and not pods and not any(pod_logs.values()) or not pipeline_failures:
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


def x_generate_incident_triage_report__mutmut_7(  # noqa: PLR0913
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

    if not events and not pods or not any(pod_logs.values()) and not pipeline_failures:
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


def x_generate_incident_triage_report__mutmut_8(  # noqa: PLR0913
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

    if not events or not pods and not any(pod_logs.values()) and not pipeline_failures:
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


def x_generate_incident_triage_report__mutmut_9(  # noqa: PLR0913
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

    if events and not pods and not any(pod_logs.values()) and not pipeline_failures:
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


def x_generate_incident_triage_report__mutmut_10(  # noqa: PLR0913
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

    if not events and pods and not any(pod_logs.values()) and not pipeline_failures:
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


def x_generate_incident_triage_report__mutmut_11(  # noqa: PLR0913
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

    if not events and not pods and any(pod_logs.values()) and not pipeline_failures:
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


def x_generate_incident_triage_report__mutmut_12(  # noqa: PLR0913
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

    if not events and not pods and not any(None) and not pipeline_failures:
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


def x_generate_incident_triage_report__mutmut_13(  # noqa: PLR0913
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

    if not events and not pods and not any(pod_logs.values()) and pipeline_failures:
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


def x_generate_incident_triage_report__mutmut_14(  # noqa: PLR0913
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
            namespace=None,
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


def x_generate_incident_triage_report__mutmut_15(  # noqa: PLR0913
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
            time_window_minutes=None,
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


def x_generate_incident_triage_report__mutmut_16(  # noqa: PLR0913
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
            insufficient_data=None,
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


def x_generate_incident_triage_report__mutmut_17(  # noqa: PLR0913
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
            data_checked=None,
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


def x_generate_incident_triage_report__mutmut_18(  # noqa: PLR0913
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


def x_generate_incident_triage_report__mutmut_19(  # noqa: PLR0913
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


def x_generate_incident_triage_report__mutmut_20(  # noqa: PLR0913
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


def x_generate_incident_triage_report__mutmut_21(  # noqa: PLR0913
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


def x_generate_incident_triage_report__mutmut_22(  # noqa: PLR0913
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
            insufficient_data=False,
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


def x_generate_incident_triage_report__mutmut_23(  # noqa: PLR0913
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
                "XXpod statusXX",
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


def x_generate_incident_triage_report__mutmut_24(  # noqa: PLR0913
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
                "POD STATUS",
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


def x_generate_incident_triage_report__mutmut_25(  # noqa: PLR0913
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
                "XXpod logsXX",
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


def x_generate_incident_triage_report__mutmut_26(  # noqa: PLR0913
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
                "POD LOGS",
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


def x_generate_incident_triage_report__mutmut_27(  # noqa: PLR0913
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
                "XXpipeline runsXX",
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


def x_generate_incident_triage_report__mutmut_28(  # noqa: PLR0913
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
                "PIPELINE RUNS",
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


def x_generate_incident_triage_report__mutmut_29(  # noqa: PLR0913
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

    all_entries = None
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


def x_generate_incident_triage_report__mutmut_30(  # noqa: PLR0913
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

    all_entries = _build_all_entries(None, pod_logs, pipeline_failures)
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


def x_generate_incident_triage_report__mutmut_31(  # noqa: PLR0913
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

    all_entries = _build_all_entries(events, None, pipeline_failures)
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


def x_generate_incident_triage_report__mutmut_32(  # noqa: PLR0913
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

    all_entries = _build_all_entries(events, pod_logs, None)
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


def x_generate_incident_triage_report__mutmut_33(  # noqa: PLR0913
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

    all_entries = _build_all_entries(pod_logs, pipeline_failures)
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


def x_generate_incident_triage_report__mutmut_34(  # noqa: PLR0913
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

    all_entries = _build_all_entries(events, pipeline_failures)
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


def x_generate_incident_triage_report__mutmut_35(  # noqa: PLR0913
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

    all_entries = _build_all_entries(events, pod_logs, )
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


def x_generate_incident_triage_report__mutmut_36(  # noqa: PLR0913
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
    failure_entries = None

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


def x_generate_incident_triage_report__mutmut_37(  # noqa: PLR0913
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
    failure_entries = [entry for entry in all_entries if entry.severity not in _FAILURE_EVENT_TYPES]

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


def x_generate_incident_triage_report__mutmut_38(  # noqa: PLR0913
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

    root_causes = None
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


def x_generate_incident_triage_report__mutmut_39(  # noqa: PLR0913
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

    root_causes = _build_root_causes(None, pipeline_failures)
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


def x_generate_incident_triage_report__mutmut_40(  # noqa: PLR0913
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

    root_causes = _build_root_causes(failure_entries, None)
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


def x_generate_incident_triage_report__mutmut_41(  # noqa: PLR0913
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

    root_causes = _build_root_causes(pipeline_failures)
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


def x_generate_incident_triage_report__mutmut_42(  # noqa: PLR0913
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

    root_causes = _build_root_causes(failure_entries, )
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


def x_generate_incident_triage_report__mutmut_43(  # noqa: PLR0913
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
    remediation_steps = None

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


def x_generate_incident_triage_report__mutmut_44(  # noqa: PLR0913
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
    remediation_steps = list(None)

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


def x_generate_incident_triage_report__mutmut_45(  # noqa: PLR0913
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
    remediation_steps = list(dict.fromkeys(None))

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


def x_generate_incident_triage_report__mutmut_46(  # noqa: PLR0913
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
    remediation_steps = list(dict.fromkeys(remediation_for(None) for c in root_causes))

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


def x_generate_incident_triage_report__mutmut_47(  # noqa: PLR0913
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

    resolved, resolution_time, mttr_minutes = None

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


def x_generate_incident_triage_report__mutmut_48(  # noqa: PLR0913
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

    resolved, resolution_time, mttr_minutes = _detect_resolution(None, failure_entries)

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


def x_generate_incident_triage_report__mutmut_49(  # noqa: PLR0913
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

    resolved, resolution_time, mttr_minutes = _detect_resolution(all_entries, None)

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


def x_generate_incident_triage_report__mutmut_50(  # noqa: PLR0913
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

    resolved, resolution_time, mttr_minutes = _detect_resolution(failure_entries)

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


def x_generate_incident_triage_report__mutmut_51(  # noqa: PLR0913
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

    resolved, resolution_time, mttr_minutes = _detect_resolution(all_entries, )

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


def x_generate_incident_triage_report__mutmut_52(  # noqa: PLR0913
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

    timeline = None

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


def x_generate_incident_triage_report__mutmut_53(  # noqa: PLR0913
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
        None,
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


def x_generate_incident_triage_report__mutmut_54(  # noqa: PLR0913
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
        key=None,
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


def x_generate_incident_triage_report__mutmut_55(  # noqa: PLR0913
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


def x_generate_incident_triage_report__mutmut_56(  # noqa: PLR0913
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


def x_generate_incident_triage_report__mutmut_57(  # noqa: PLR0913
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
            if entry.severity != _NORMAL_EVENT_TYPE and entry.timestamp == resolution_time
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


def x_generate_incident_triage_report__mutmut_58(  # noqa: PLR0913
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
            if entry.severity == _NORMAL_EVENT_TYPE or entry.timestamp == resolution_time
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


def x_generate_incident_triage_report__mutmut_59(  # noqa: PLR0913
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
            if entry.severity != _NORMAL_EVENT_TYPE or entry.timestamp != resolution_time
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


def x_generate_incident_triage_report__mutmut_60(  # noqa: PLR0913
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
        key=lambda entry: None,
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


def x_generate_incident_triage_report__mutmut_61(  # noqa: PLR0913
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

    impact = None

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


def x_generate_incident_triage_report__mutmut_62(  # noqa: PLR0913
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
        None, pods, root_causes, resolved, resolution_time, observed_at
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


def x_generate_incident_triage_report__mutmut_63(  # noqa: PLR0913
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
        failure_entries, None, root_causes, resolved, resolution_time, observed_at
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


def x_generate_incident_triage_report__mutmut_64(  # noqa: PLR0913
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
        failure_entries, pods, None, resolved, resolution_time, observed_at
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


def x_generate_incident_triage_report__mutmut_65(  # noqa: PLR0913
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
        failure_entries, pods, root_causes, None, resolution_time, observed_at
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


def x_generate_incident_triage_report__mutmut_66(  # noqa: PLR0913
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
        failure_entries, pods, root_causes, resolved, None, observed_at
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


def x_generate_incident_triage_report__mutmut_67(  # noqa: PLR0913
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
        failure_entries, pods, root_causes, resolved, resolution_time, None
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


def x_generate_incident_triage_report__mutmut_68(  # noqa: PLR0913
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
        pods, root_causes, resolved, resolution_time, observed_at
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


def x_generate_incident_triage_report__mutmut_69(  # noqa: PLR0913
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
        failure_entries, root_causes, resolved, resolution_time, observed_at
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


def x_generate_incident_triage_report__mutmut_70(  # noqa: PLR0913
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
        failure_entries, pods, resolved, resolution_time, observed_at
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


def x_generate_incident_triage_report__mutmut_71(  # noqa: PLR0913
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
        failure_entries, pods, root_causes, resolution_time, observed_at
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


def x_generate_incident_triage_report__mutmut_72(  # noqa: PLR0913
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
        failure_entries, pods, root_causes, resolved, observed_at
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


def x_generate_incident_triage_report__mutmut_73(  # noqa: PLR0913
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
        failure_entries, pods, root_causes, resolved, resolution_time, )

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


def x_generate_incident_triage_report__mutmut_74(  # noqa: PLR0913
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

    ntp_drift_detected, ntp_drift_note = None

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


def x_generate_incident_triage_report__mutmut_75(  # noqa: PLR0913
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

    ntp_drift_detected, ntp_drift_note = _detect_ntp_drift(None)

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


def x_generate_incident_triage_report__mutmut_76(  # noqa: PLR0913
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

    cross_namespace_correlation = None

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


def x_generate_incident_triage_report__mutmut_77(  # noqa: PLR0913
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

    cross_namespace_correlation = _correlate_cross_namespace(None, related_namespace_events)

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


def x_generate_incident_triage_report__mutmut_78(  # noqa: PLR0913
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

    cross_namespace_correlation = _correlate_cross_namespace(root_causes, None)

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


def x_generate_incident_triage_report__mutmut_79(  # noqa: PLR0913
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

    cross_namespace_correlation = _correlate_cross_namespace(related_namespace_events)

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


def x_generate_incident_triage_report__mutmut_80(  # noqa: PLR0913
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

    cross_namespace_correlation = _correlate_cross_namespace(root_causes, )

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


def x_generate_incident_triage_report__mutmut_81(  # noqa: PLR0913
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
        namespace=None,
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


def x_generate_incident_triage_report__mutmut_82(  # noqa: PLR0913
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
        time_window_minutes=None,
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


def x_generate_incident_triage_report__mutmut_83(  # noqa: PLR0913
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
        timeline=None,
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


def x_generate_incident_triage_report__mutmut_84(  # noqa: PLR0913
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
        root_causes=None,
        impact=impact,
        remediation_steps=remediation_steps,
        resolved=resolved,
        resolution_time=resolution_time,
        mttr_minutes=mttr_minutes,
        ntp_drift_detected=ntp_drift_detected,
        ntp_drift_note=ntp_drift_note,
        cross_namespace_correlation=cross_namespace_correlation,
    )


def x_generate_incident_triage_report__mutmut_85(  # noqa: PLR0913
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
        impact=None,
        remediation_steps=remediation_steps,
        resolved=resolved,
        resolution_time=resolution_time,
        mttr_minutes=mttr_minutes,
        ntp_drift_detected=ntp_drift_detected,
        ntp_drift_note=ntp_drift_note,
        cross_namespace_correlation=cross_namespace_correlation,
    )


def x_generate_incident_triage_report__mutmut_86(  # noqa: PLR0913
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
        remediation_steps=None,
        resolved=resolved,
        resolution_time=resolution_time,
        mttr_minutes=mttr_minutes,
        ntp_drift_detected=ntp_drift_detected,
        ntp_drift_note=ntp_drift_note,
        cross_namespace_correlation=cross_namespace_correlation,
    )


def x_generate_incident_triage_report__mutmut_87(  # noqa: PLR0913
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
        resolved=None,
        resolution_time=resolution_time,
        mttr_minutes=mttr_minutes,
        ntp_drift_detected=ntp_drift_detected,
        ntp_drift_note=ntp_drift_note,
        cross_namespace_correlation=cross_namespace_correlation,
    )


def x_generate_incident_triage_report__mutmut_88(  # noqa: PLR0913
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
        resolution_time=None,
        mttr_minutes=mttr_minutes,
        ntp_drift_detected=ntp_drift_detected,
        ntp_drift_note=ntp_drift_note,
        cross_namespace_correlation=cross_namespace_correlation,
    )


def x_generate_incident_triage_report__mutmut_89(  # noqa: PLR0913
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
        mttr_minutes=None,
        ntp_drift_detected=ntp_drift_detected,
        ntp_drift_note=ntp_drift_note,
        cross_namespace_correlation=cross_namespace_correlation,
    )


def x_generate_incident_triage_report__mutmut_90(  # noqa: PLR0913
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
        ntp_drift_detected=None,
        ntp_drift_note=ntp_drift_note,
        cross_namespace_correlation=cross_namespace_correlation,
    )


def x_generate_incident_triage_report__mutmut_91(  # noqa: PLR0913
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
        ntp_drift_note=None,
        cross_namespace_correlation=cross_namespace_correlation,
    )


def x_generate_incident_triage_report__mutmut_92(  # noqa: PLR0913
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
        cross_namespace_correlation=None,
    )


def x_generate_incident_triage_report__mutmut_93(  # noqa: PLR0913
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


def x_generate_incident_triage_report__mutmut_94(  # noqa: PLR0913
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


def x_generate_incident_triage_report__mutmut_95(  # noqa: PLR0913
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


def x_generate_incident_triage_report__mutmut_96(  # noqa: PLR0913
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
        impact=impact,
        remediation_steps=remediation_steps,
        resolved=resolved,
        resolution_time=resolution_time,
        mttr_minutes=mttr_minutes,
        ntp_drift_detected=ntp_drift_detected,
        ntp_drift_note=ntp_drift_note,
        cross_namespace_correlation=cross_namespace_correlation,
    )


def x_generate_incident_triage_report__mutmut_97(  # noqa: PLR0913
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
        remediation_steps=remediation_steps,
        resolved=resolved,
        resolution_time=resolution_time,
        mttr_minutes=mttr_minutes,
        ntp_drift_detected=ntp_drift_detected,
        ntp_drift_note=ntp_drift_note,
        cross_namespace_correlation=cross_namespace_correlation,
    )


def x_generate_incident_triage_report__mutmut_98(  # noqa: PLR0913
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
        resolved=resolved,
        resolution_time=resolution_time,
        mttr_minutes=mttr_minutes,
        ntp_drift_detected=ntp_drift_detected,
        ntp_drift_note=ntp_drift_note,
        cross_namespace_correlation=cross_namespace_correlation,
    )


def x_generate_incident_triage_report__mutmut_99(  # noqa: PLR0913
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
        resolution_time=resolution_time,
        mttr_minutes=mttr_minutes,
        ntp_drift_detected=ntp_drift_detected,
        ntp_drift_note=ntp_drift_note,
        cross_namespace_correlation=cross_namespace_correlation,
    )


def x_generate_incident_triage_report__mutmut_100(  # noqa: PLR0913
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
        mttr_minutes=mttr_minutes,
        ntp_drift_detected=ntp_drift_detected,
        ntp_drift_note=ntp_drift_note,
        cross_namespace_correlation=cross_namespace_correlation,
    )


def x_generate_incident_triage_report__mutmut_101(  # noqa: PLR0913
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
        ntp_drift_detected=ntp_drift_detected,
        ntp_drift_note=ntp_drift_note,
        cross_namespace_correlation=cross_namespace_correlation,
    )


def x_generate_incident_triage_report__mutmut_102(  # noqa: PLR0913
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
        ntp_drift_note=ntp_drift_note,
        cross_namespace_correlation=cross_namespace_correlation,
    )


def x_generate_incident_triage_report__mutmut_103(  # noqa: PLR0913
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
        cross_namespace_correlation=cross_namespace_correlation,
    )


def x_generate_incident_triage_report__mutmut_104(  # noqa: PLR0913
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
        )

mutants_x_generate_incident_triage_report__mutmut['_mutmut_orig'] = x_generate_incident_triage_report__mutmut_orig # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_1'] = x_generate_incident_triage_report__mutmut_1 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_2'] = x_generate_incident_triage_report__mutmut_2 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_3'] = x_generate_incident_triage_report__mutmut_3 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_4'] = x_generate_incident_triage_report__mutmut_4 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_5'] = x_generate_incident_triage_report__mutmut_5 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_6'] = x_generate_incident_triage_report__mutmut_6 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_7'] = x_generate_incident_triage_report__mutmut_7 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_8'] = x_generate_incident_triage_report__mutmut_8 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_9'] = x_generate_incident_triage_report__mutmut_9 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_10'] = x_generate_incident_triage_report__mutmut_10 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_11'] = x_generate_incident_triage_report__mutmut_11 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_12'] = x_generate_incident_triage_report__mutmut_12 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_13'] = x_generate_incident_triage_report__mutmut_13 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_14'] = x_generate_incident_triage_report__mutmut_14 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_15'] = x_generate_incident_triage_report__mutmut_15 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_16'] = x_generate_incident_triage_report__mutmut_16 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_17'] = x_generate_incident_triage_report__mutmut_17 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_18'] = x_generate_incident_triage_report__mutmut_18 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_19'] = x_generate_incident_triage_report__mutmut_19 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_20'] = x_generate_incident_triage_report__mutmut_20 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_21'] = x_generate_incident_triage_report__mutmut_21 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_22'] = x_generate_incident_triage_report__mutmut_22 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_23'] = x_generate_incident_triage_report__mutmut_23 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_24'] = x_generate_incident_triage_report__mutmut_24 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_25'] = x_generate_incident_triage_report__mutmut_25 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_26'] = x_generate_incident_triage_report__mutmut_26 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_27'] = x_generate_incident_triage_report__mutmut_27 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_28'] = x_generate_incident_triage_report__mutmut_28 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_29'] = x_generate_incident_triage_report__mutmut_29 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_30'] = x_generate_incident_triage_report__mutmut_30 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_31'] = x_generate_incident_triage_report__mutmut_31 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_32'] = x_generate_incident_triage_report__mutmut_32 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_33'] = x_generate_incident_triage_report__mutmut_33 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_34'] = x_generate_incident_triage_report__mutmut_34 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_35'] = x_generate_incident_triage_report__mutmut_35 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_36'] = x_generate_incident_triage_report__mutmut_36 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_37'] = x_generate_incident_triage_report__mutmut_37 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_38'] = x_generate_incident_triage_report__mutmut_38 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_39'] = x_generate_incident_triage_report__mutmut_39 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_40'] = x_generate_incident_triage_report__mutmut_40 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_41'] = x_generate_incident_triage_report__mutmut_41 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_42'] = x_generate_incident_triage_report__mutmut_42 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_43'] = x_generate_incident_triage_report__mutmut_43 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_44'] = x_generate_incident_triage_report__mutmut_44 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_45'] = x_generate_incident_triage_report__mutmut_45 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_46'] = x_generate_incident_triage_report__mutmut_46 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_47'] = x_generate_incident_triage_report__mutmut_47 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_48'] = x_generate_incident_triage_report__mutmut_48 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_49'] = x_generate_incident_triage_report__mutmut_49 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_50'] = x_generate_incident_triage_report__mutmut_50 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_51'] = x_generate_incident_triage_report__mutmut_51 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_52'] = x_generate_incident_triage_report__mutmut_52 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_53'] = x_generate_incident_triage_report__mutmut_53 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_54'] = x_generate_incident_triage_report__mutmut_54 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_55'] = x_generate_incident_triage_report__mutmut_55 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_56'] = x_generate_incident_triage_report__mutmut_56 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_57'] = x_generate_incident_triage_report__mutmut_57 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_58'] = x_generate_incident_triage_report__mutmut_58 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_59'] = x_generate_incident_triage_report__mutmut_59 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_60'] = x_generate_incident_triage_report__mutmut_60 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_61'] = x_generate_incident_triage_report__mutmut_61 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_62'] = x_generate_incident_triage_report__mutmut_62 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_63'] = x_generate_incident_triage_report__mutmut_63 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_64'] = x_generate_incident_triage_report__mutmut_64 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_65'] = x_generate_incident_triage_report__mutmut_65 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_66'] = x_generate_incident_triage_report__mutmut_66 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_67'] = x_generate_incident_triage_report__mutmut_67 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_68'] = x_generate_incident_triage_report__mutmut_68 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_69'] = x_generate_incident_triage_report__mutmut_69 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_70'] = x_generate_incident_triage_report__mutmut_70 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_71'] = x_generate_incident_triage_report__mutmut_71 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_72'] = x_generate_incident_triage_report__mutmut_72 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_73'] = x_generate_incident_triage_report__mutmut_73 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_74'] = x_generate_incident_triage_report__mutmut_74 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_75'] = x_generate_incident_triage_report__mutmut_75 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_76'] = x_generate_incident_triage_report__mutmut_76 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_77'] = x_generate_incident_triage_report__mutmut_77 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_78'] = x_generate_incident_triage_report__mutmut_78 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_79'] = x_generate_incident_triage_report__mutmut_79 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_80'] = x_generate_incident_triage_report__mutmut_80 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_81'] = x_generate_incident_triage_report__mutmut_81 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_82'] = x_generate_incident_triage_report__mutmut_82 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_83'] = x_generate_incident_triage_report__mutmut_83 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_84'] = x_generate_incident_triage_report__mutmut_84 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_85'] = x_generate_incident_triage_report__mutmut_85 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_86'] = x_generate_incident_triage_report__mutmut_86 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_87'] = x_generate_incident_triage_report__mutmut_87 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_88'] = x_generate_incident_triage_report__mutmut_88 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_89'] = x_generate_incident_triage_report__mutmut_89 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_90'] = x_generate_incident_triage_report__mutmut_90 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_91'] = x_generate_incident_triage_report__mutmut_91 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_92'] = x_generate_incident_triage_report__mutmut_92 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_93'] = x_generate_incident_triage_report__mutmut_93 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_94'] = x_generate_incident_triage_report__mutmut_94 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_95'] = x_generate_incident_triage_report__mutmut_95 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_96'] = x_generate_incident_triage_report__mutmut_96 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_97'] = x_generate_incident_triage_report__mutmut_97 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_98'] = x_generate_incident_triage_report__mutmut_98 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_99'] = x_generate_incident_triage_report__mutmut_99 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_100'] = x_generate_incident_triage_report__mutmut_100 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_101'] = x_generate_incident_triage_report__mutmut_101 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_102'] = x_generate_incident_triage_report__mutmut_102 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_103'] = x_generate_incident_triage_report__mutmut_103 # type: ignore # mutmut generated
mutants_x_generate_incident_triage_report__mutmut['x_generate_incident_triage_report__mutmut_104'] = x_generate_incident_triage_report__mutmut_104 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_all_entries__mutmut)
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


def x__build_all_entries__mutmut_orig(
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


def x__build_all_entries__mutmut_1(
    events: list[NamespaceEvent],
    pod_logs: dict[str, list[PodLogLine]],
    pipeline_failures: list[tuple[str, FailureAnalysis]],
) -> list[TimelineEntry]:
    entries: list[TimelineEntry] = None

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


def x__build_all_entries__mutmut_2(
    events: list[NamespaceEvent],
    pod_logs: dict[str, list[PodLogLine]],
    pipeline_failures: list[tuple[str, FailureAnalysis]],
) -> list[TimelineEntry]:
    entries: list[TimelineEntry] = []

    for event in events:
        entries.append(
            None
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


def x__build_all_entries__mutmut_3(
    events: list[NamespaceEvent],
    pod_logs: dict[str, list[PodLogLine]],
    pipeline_failures: list[tuple[str, FailureAnalysis]],
) -> list[TimelineEntry]:
    entries: list[TimelineEntry] = []

    for event in events:
        entries.append(
            TimelineEntry(
                timestamp=None,
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


def x__build_all_entries__mutmut_4(
    events: list[NamespaceEvent],
    pod_logs: dict[str, list[PodLogLine]],
    pipeline_failures: list[tuple[str, FailureAnalysis]],
) -> list[TimelineEntry]:
    entries: list[TimelineEntry] = []

    for event in events:
        entries.append(
            TimelineEntry(
                timestamp=event.last_seen,
                source=None,
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


def x__build_all_entries__mutmut_5(
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
                namespace=None,
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


def x__build_all_entries__mutmut_6(
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
                object=None,
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


def x__build_all_entries__mutmut_7(
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
                reason=None,
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


def x__build_all_entries__mutmut_8(
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
                message=None,
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


def x__build_all_entries__mutmut_9(
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
                severity=None,
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


def x__build_all_entries__mutmut_10(
    events: list[NamespaceEvent],
    pod_logs: dict[str, list[PodLogLine]],
    pipeline_failures: list[tuple[str, FailureAnalysis]],
) -> list[TimelineEntry]:
    entries: list[TimelineEntry] = []

    for event in events:
        entries.append(
            TimelineEntry(
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


def x__build_all_entries__mutmut_11(
    events: list[NamespaceEvent],
    pod_logs: dict[str, list[PodLogLine]],
    pipeline_failures: list[tuple[str, FailureAnalysis]],
) -> list[TimelineEntry]:
    entries: list[TimelineEntry] = []

    for event in events:
        entries.append(
            TimelineEntry(
                timestamp=event.last_seen,
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


def x__build_all_entries__mutmut_12(
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


def x__build_all_entries__mutmut_13(
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


def x__build_all_entries__mutmut_14(
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


def x__build_all_entries__mutmut_15(
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


def x__build_all_entries__mutmut_16(
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


def x__build_all_entries__mutmut_17(
    events: list[NamespaceEvent],
    pod_logs: dict[str, list[PodLogLine]],
    pipeline_failures: list[tuple[str, FailureAnalysis]],
) -> list[TimelineEntry]:
    entries: list[TimelineEntry] = []

    for event in events:
        entries.append(
            TimelineEntry(
                timestamp=event.last_seen,
                source="XXeventXX",
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


def x__build_all_entries__mutmut_18(
    events: list[NamespaceEvent],
    pod_logs: dict[str, list[PodLogLine]],
    pipeline_failures: list[tuple[str, FailureAnalysis]],
) -> list[TimelineEntry]:
    entries: list[TimelineEntry] = []

    for event in events:
        entries.append(
            TimelineEntry(
                timestamp=event.last_seen,
                source="EVENT",
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


def x__build_all_entries__mutmut_19(
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
                namespace="XXXX",
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


def x__build_all_entries__mutmut_20(
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
            if (line.is_error or line.is_warning):
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


def x__build_all_entries__mutmut_21(
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
            if not (line.is_error and line.is_warning):
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


def x__build_all_entries__mutmut_22(
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
                break
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


def x__build_all_entries__mutmut_23(
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
                None
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


def x__build_all_entries__mutmut_24(
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
                    timestamp=None,
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


def x__build_all_entries__mutmut_25(
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
                    source=None,
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


def x__build_all_entries__mutmut_26(
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
                    namespace=None,
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


def x__build_all_entries__mutmut_27(
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
                    object=None,
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


def x__build_all_entries__mutmut_28(
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
                    reason=None,
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


def x__build_all_entries__mutmut_29(
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
                    message=None,
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


def x__build_all_entries__mutmut_30(
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
                    severity=None,
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


def x__build_all_entries__mutmut_31(
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


def x__build_all_entries__mutmut_32(
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


def x__build_all_entries__mutmut_33(
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


def x__build_all_entries__mutmut_34(
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


def x__build_all_entries__mutmut_35(
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


def x__build_all_entries__mutmut_36(
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


def x__build_all_entries__mutmut_37(
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


def x__build_all_entries__mutmut_38(
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
                    source="XXlogXX",
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


def x__build_all_entries__mutmut_39(
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
                    source="LOG",
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


def x__build_all_entries__mutmut_40(
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
                    namespace="XXXX",
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


def x__build_all_entries__mutmut_41(
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
                    reason="XXlog_errorXX" if line.is_error else "log_warning",
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


def x__build_all_entries__mutmut_42(
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
                    reason="LOG_ERROR" if line.is_error else "log_warning",
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


def x__build_all_entries__mutmut_43(
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
                    reason="log_error" if line.is_error else "XXlog_warningXX",
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


def x__build_all_entries__mutmut_44(
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
                    reason="log_error" if line.is_error else "LOG_WARNING",
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


def x__build_all_entries__mutmut_45(
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
                    severity="XXErrorXX" if line.is_error else "Warning",
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


def x__build_all_entries__mutmut_46(
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
                    severity="error" if line.is_error else "Warning",
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


def x__build_all_entries__mutmut_47(
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
                    severity="ERROR" if line.is_error else "Warning",
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


def x__build_all_entries__mutmut_48(
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
                    severity="Error" if line.is_error else "XXWarningXX",
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


def x__build_all_entries__mutmut_49(
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
                    severity="Error" if line.is_error else "warning",
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


def x__build_all_entries__mutmut_50(
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
                    severity="Error" if line.is_error else "WARNING",
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


def x__build_all_entries__mutmut_51(
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
            None
        )

    return sorted(entries, key=lambda entry: entry.timestamp)


def x__build_all_entries__mutmut_52(
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
                timestamp=None,
                source="pipeline",
                namespace="",
                object=failure.task_name,
                reason=failure.failure_type.value,
                message=failure.root_cause,
                severity="Error",
            )
        )

    return sorted(entries, key=lambda entry: entry.timestamp)


def x__build_all_entries__mutmut_53(
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
                source=None,
                namespace="",
                object=failure.task_name,
                reason=failure.failure_type.value,
                message=failure.root_cause,
                severity="Error",
            )
        )

    return sorted(entries, key=lambda entry: entry.timestamp)


def x__build_all_entries__mutmut_54(
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
                namespace=None,
                object=failure.task_name,
                reason=failure.failure_type.value,
                message=failure.root_cause,
                severity="Error",
            )
        )

    return sorted(entries, key=lambda entry: entry.timestamp)


def x__build_all_entries__mutmut_55(
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
                object=None,
                reason=failure.failure_type.value,
                message=failure.root_cause,
                severity="Error",
            )
        )

    return sorted(entries, key=lambda entry: entry.timestamp)


def x__build_all_entries__mutmut_56(
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
                reason=None,
                message=failure.root_cause,
                severity="Error",
            )
        )

    return sorted(entries, key=lambda entry: entry.timestamp)


def x__build_all_entries__mutmut_57(
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
                message=None,
                severity="Error",
            )
        )

    return sorted(entries, key=lambda entry: entry.timestamp)


def x__build_all_entries__mutmut_58(
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
                severity=None,
            )
        )

    return sorted(entries, key=lambda entry: entry.timestamp)


def x__build_all_entries__mutmut_59(
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
                source="pipeline",
                namespace="",
                object=failure.task_name,
                reason=failure.failure_type.value,
                message=failure.root_cause,
                severity="Error",
            )
        )

    return sorted(entries, key=lambda entry: entry.timestamp)


def x__build_all_entries__mutmut_60(
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
                namespace="",
                object=failure.task_name,
                reason=failure.failure_type.value,
                message=failure.root_cause,
                severity="Error",
            )
        )

    return sorted(entries, key=lambda entry: entry.timestamp)


def x__build_all_entries__mutmut_61(
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
                object=failure.task_name,
                reason=failure.failure_type.value,
                message=failure.root_cause,
                severity="Error",
            )
        )

    return sorted(entries, key=lambda entry: entry.timestamp)


def x__build_all_entries__mutmut_62(
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
                reason=failure.failure_type.value,
                message=failure.root_cause,
                severity="Error",
            )
        )

    return sorted(entries, key=lambda entry: entry.timestamp)


def x__build_all_entries__mutmut_63(
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
                message=failure.root_cause,
                severity="Error",
            )
        )

    return sorted(entries, key=lambda entry: entry.timestamp)


def x__build_all_entries__mutmut_64(
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
                severity="Error",
            )
        )

    return sorted(entries, key=lambda entry: entry.timestamp)


def x__build_all_entries__mutmut_65(
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
                )
        )

    return sorted(entries, key=lambda entry: entry.timestamp)


def x__build_all_entries__mutmut_66(
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
                source="XXpipelineXX",
                namespace="",
                object=failure.task_name,
                reason=failure.failure_type.value,
                message=failure.root_cause,
                severity="Error",
            )
        )

    return sorted(entries, key=lambda entry: entry.timestamp)


def x__build_all_entries__mutmut_67(
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
                source="PIPELINE",
                namespace="",
                object=failure.task_name,
                reason=failure.failure_type.value,
                message=failure.root_cause,
                severity="Error",
            )
        )

    return sorted(entries, key=lambda entry: entry.timestamp)


def x__build_all_entries__mutmut_68(
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
                namespace="XXXX",
                object=failure.task_name,
                reason=failure.failure_type.value,
                message=failure.root_cause,
                severity="Error",
            )
        )

    return sorted(entries, key=lambda entry: entry.timestamp)


def x__build_all_entries__mutmut_69(
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
                severity="XXErrorXX",
            )
        )

    return sorted(entries, key=lambda entry: entry.timestamp)


def x__build_all_entries__mutmut_70(
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
                severity="error",
            )
        )

    return sorted(entries, key=lambda entry: entry.timestamp)


def x__build_all_entries__mutmut_71(
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
                severity="ERROR",
            )
        )

    return sorted(entries, key=lambda entry: entry.timestamp)


def x__build_all_entries__mutmut_72(
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

    return sorted(None, key=lambda entry: entry.timestamp)


def x__build_all_entries__mutmut_73(
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

    return sorted(entries, key=None)


def x__build_all_entries__mutmut_74(
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

    return sorted(key=lambda entry: entry.timestamp)


def x__build_all_entries__mutmut_75(
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

    return sorted(entries, )


def x__build_all_entries__mutmut_76(
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

    return sorted(entries, key=lambda entry: None)

mutants_x__build_all_entries__mutmut['_mutmut_orig'] = x__build_all_entries__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_1'] = x__build_all_entries__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_2'] = x__build_all_entries__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_3'] = x__build_all_entries__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_4'] = x__build_all_entries__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_5'] = x__build_all_entries__mutmut_5 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_6'] = x__build_all_entries__mutmut_6 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_7'] = x__build_all_entries__mutmut_7 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_8'] = x__build_all_entries__mutmut_8 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_9'] = x__build_all_entries__mutmut_9 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_10'] = x__build_all_entries__mutmut_10 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_11'] = x__build_all_entries__mutmut_11 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_12'] = x__build_all_entries__mutmut_12 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_13'] = x__build_all_entries__mutmut_13 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_14'] = x__build_all_entries__mutmut_14 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_15'] = x__build_all_entries__mutmut_15 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_16'] = x__build_all_entries__mutmut_16 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_17'] = x__build_all_entries__mutmut_17 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_18'] = x__build_all_entries__mutmut_18 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_19'] = x__build_all_entries__mutmut_19 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_20'] = x__build_all_entries__mutmut_20 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_21'] = x__build_all_entries__mutmut_21 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_22'] = x__build_all_entries__mutmut_22 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_23'] = x__build_all_entries__mutmut_23 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_24'] = x__build_all_entries__mutmut_24 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_25'] = x__build_all_entries__mutmut_25 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_26'] = x__build_all_entries__mutmut_26 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_27'] = x__build_all_entries__mutmut_27 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_28'] = x__build_all_entries__mutmut_28 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_29'] = x__build_all_entries__mutmut_29 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_30'] = x__build_all_entries__mutmut_30 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_31'] = x__build_all_entries__mutmut_31 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_32'] = x__build_all_entries__mutmut_32 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_33'] = x__build_all_entries__mutmut_33 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_34'] = x__build_all_entries__mutmut_34 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_35'] = x__build_all_entries__mutmut_35 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_36'] = x__build_all_entries__mutmut_36 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_37'] = x__build_all_entries__mutmut_37 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_38'] = x__build_all_entries__mutmut_38 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_39'] = x__build_all_entries__mutmut_39 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_40'] = x__build_all_entries__mutmut_40 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_41'] = x__build_all_entries__mutmut_41 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_42'] = x__build_all_entries__mutmut_42 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_43'] = x__build_all_entries__mutmut_43 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_44'] = x__build_all_entries__mutmut_44 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_45'] = x__build_all_entries__mutmut_45 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_46'] = x__build_all_entries__mutmut_46 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_47'] = x__build_all_entries__mutmut_47 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_48'] = x__build_all_entries__mutmut_48 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_49'] = x__build_all_entries__mutmut_49 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_50'] = x__build_all_entries__mutmut_50 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_51'] = x__build_all_entries__mutmut_51 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_52'] = x__build_all_entries__mutmut_52 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_53'] = x__build_all_entries__mutmut_53 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_54'] = x__build_all_entries__mutmut_54 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_55'] = x__build_all_entries__mutmut_55 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_56'] = x__build_all_entries__mutmut_56 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_57'] = x__build_all_entries__mutmut_57 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_58'] = x__build_all_entries__mutmut_58 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_59'] = x__build_all_entries__mutmut_59 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_60'] = x__build_all_entries__mutmut_60 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_61'] = x__build_all_entries__mutmut_61 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_62'] = x__build_all_entries__mutmut_62 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_63'] = x__build_all_entries__mutmut_63 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_64'] = x__build_all_entries__mutmut_64 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_65'] = x__build_all_entries__mutmut_65 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_66'] = x__build_all_entries__mutmut_66 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_67'] = x__build_all_entries__mutmut_67 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_68'] = x__build_all_entries__mutmut_68 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_69'] = x__build_all_entries__mutmut_69 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_70'] = x__build_all_entries__mutmut_70 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_71'] = x__build_all_entries__mutmut_71 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_72'] = x__build_all_entries__mutmut_72 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_73'] = x__build_all_entries__mutmut_73 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_74'] = x__build_all_entries__mutmut_74 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_75'] = x__build_all_entries__mutmut_75 # type: ignore # mutmut generated
mutants_x__build_all_entries__mutmut['x__build_all_entries__mutmut_76'] = x__build_all_entries__mutmut_76 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_root_causes__mutmut)
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


def x__build_root_causes__mutmut_orig(
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


def x__build_root_causes__mutmut_1(
    failure_entries: list[TimelineEntry],
    pipeline_failures: list[tuple[str, FailureAnalysis]],
) -> list[RootCauseCandidate]:
    candidates: list[RootCauseCandidate] = None

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


def x__build_root_causes__mutmut_2(
    failure_entries: list[TimelineEntry],
    pipeline_failures: list[tuple[str, FailureAnalysis]],
) -> list[RootCauseCandidate]:
    candidates: list[RootCauseCandidate] = []

    by_category: dict[IncidentCauseCategory, list[TimelineEntry]] = None
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


def x__build_root_causes__mutmut_3(
    failure_entries: list[TimelineEntry],
    pipeline_failures: list[tuple[str, FailureAnalysis]],
) -> list[RootCauseCandidate]:
    candidates: list[RootCauseCandidate] = []

    by_category: dict[IncidentCauseCategory, list[TimelineEntry]] = defaultdict(None)
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


def x__build_root_causes__mutmut_4(
    failure_entries: list[TimelineEntry],
    pipeline_failures: list[tuple[str, FailureAnalysis]],
) -> list[RootCauseCandidate]:
    candidates: list[RootCauseCandidate] = []

    by_category: dict[IncidentCauseCategory, list[TimelineEntry]] = defaultdict(list)
    for entry in failure_entries:
        if entry.source != "pipeline":
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


def x__build_root_causes__mutmut_5(
    failure_entries: list[TimelineEntry],
    pipeline_failures: list[tuple[str, FailureAnalysis]],
) -> list[RootCauseCandidate]:
    candidates: list[RootCauseCandidate] = []

    by_category: dict[IncidentCauseCategory, list[TimelineEntry]] = defaultdict(list)
    for entry in failure_entries:
        if entry.source == "XXpipelineXX":
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


def x__build_root_causes__mutmut_6(
    failure_entries: list[TimelineEntry],
    pipeline_failures: list[tuple[str, FailureAnalysis]],
) -> list[RootCauseCandidate]:
    candidates: list[RootCauseCandidate] = []

    by_category: dict[IncidentCauseCategory, list[TimelineEntry]] = defaultdict(list)
    for entry in failure_entries:
        if entry.source == "PIPELINE":
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


def x__build_root_causes__mutmut_7(
    failure_entries: list[TimelineEntry],
    pipeline_failures: list[tuple[str, FailureAnalysis]],
) -> list[RootCauseCandidate]:
    candidates: list[RootCauseCandidate] = []

    by_category: dict[IncidentCauseCategory, list[TimelineEntry]] = defaultdict(list)
    for entry in failure_entries:
        if entry.source == "pipeline":
            break
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


def x__build_root_causes__mutmut_8(
    failure_entries: list[TimelineEntry],
    pipeline_failures: list[tuple[str, FailureAnalysis]],
) -> list[RootCauseCandidate]:
    candidates: list[RootCauseCandidate] = []

    by_category: dict[IncidentCauseCategory, list[TimelineEntry]] = defaultdict(list)
    for entry in failure_entries:
        if entry.source == "pipeline":
            continue
        category = None
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


def x__build_root_causes__mutmut_9(
    failure_entries: list[TimelineEntry],
    pipeline_failures: list[tuple[str, FailureAnalysis]],
) -> list[RootCauseCandidate]:
    candidates: list[RootCauseCandidate] = []

    by_category: dict[IncidentCauseCategory, list[TimelineEntry]] = defaultdict(list)
    for entry in failure_entries:
        if entry.source == "pipeline":
            continue
        category = classify_incident_cause(None)
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


def x__build_root_causes__mutmut_10(
    failure_entries: list[TimelineEntry],
    pipeline_failures: list[tuple[str, FailureAnalysis]],
) -> list[RootCauseCandidate]:
    candidates: list[RootCauseCandidate] = []

    by_category: dict[IncidentCauseCategory, list[TimelineEntry]] = defaultdict(list)
    for entry in failure_entries:
        if entry.source == "pipeline":
            continue
        category = classify_incident_cause(f"{entry.reason} {entry.message}")
        by_category[category].append(None)

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


def x__build_root_causes__mutmut_11(
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
        involved_objects = None
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


def x__build_root_causes__mutmut_12(
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
        involved_objects = list(None)
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


def x__build_root_causes__mutmut_13(
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
        involved_objects = list(dict.fromkeys(None))
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


def x__build_root_causes__mutmut_14(
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
        confidence = None
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


def x__build_root_causes__mutmut_15(
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
            logs_analyzed=None,
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


def x__build_root_causes__mutmut_16(
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
            root_cause_found=None,
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


def x__build_root_causes__mutmut_17(
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
            timeline_available=None,
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


def x__build_root_causes__mutmut_18(
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


def x__build_root_causes__mutmut_19(
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


def x__build_root_causes__mutmut_20(
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


def x__build_root_causes__mutmut_21(
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
            logs_analyzed=any(None),
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


def x__build_root_causes__mutmut_22(
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
            logs_analyzed=any(entry.source != "log" for entry in group),
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


def x__build_root_causes__mutmut_23(
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
            logs_analyzed=any(entry.source == "XXlogXX" for entry in group),
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


def x__build_root_causes__mutmut_24(
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
            logs_analyzed=any(entry.source == "LOG" for entry in group),
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


def x__build_root_causes__mutmut_25(
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
            root_cause_found=category == IncidentCauseCategory.UNKNOWN,
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


def x__build_root_causes__mutmut_26(
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
            timeline_available=len(group) >= 1,
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


def x__build_root_causes__mutmut_27(
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
            timeline_available=len(group) > 2,
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


def x__build_root_causes__mutmut_28(
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
            None
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


def x__build_root_causes__mutmut_29(
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
                description=None,
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


def x__build_root_causes__mutmut_30(
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
                category=None,
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


def x__build_root_causes__mutmut_31(
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
                confidence=None,
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


def x__build_root_causes__mutmut_32(
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
                evidence=None,
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


def x__build_root_causes__mutmut_33(
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
                involved_objects=None,
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


def x__build_root_causes__mutmut_34(
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


def x__build_root_causes__mutmut_35(
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


def x__build_root_causes__mutmut_36(
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


def x__build_root_causes__mutmut_37(
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


def x__build_root_causes__mutmut_38(
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


def x__build_root_causes__mutmut_39(
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
                description=_describe_candidate(None, involved_objects),
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


def x__build_root_causes__mutmut_40(
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
                description=_describe_candidate(category, None),
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


def x__build_root_causes__mutmut_41(
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
                description=_describe_candidate(involved_objects),
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


def x__build_root_causes__mutmut_42(
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
                description=_describe_candidate(category, ),
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


def x__build_root_causes__mutmut_43(
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
            None
        )

    candidates.sort(key=lambda candidate: candidate.confidence, reverse=True)
    return candidates


def x__build_root_causes__mutmut_44(
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
                description=None,
                category=_FAILURE_TYPE_TO_CAUSE_CATEGORY[failure.failure_type],
                confidence=failure.confidence,
                evidence=[f"{start_time} {failure.task_name}: {failure.root_cause}"],
                involved_objects=[failure.task_name],
            )
        )

    candidates.sort(key=lambda candidate: candidate.confidence, reverse=True)
    return candidates


def x__build_root_causes__mutmut_45(
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
                category=None,
                confidence=failure.confidence,
                evidence=[f"{start_time} {failure.task_name}: {failure.root_cause}"],
                involved_objects=[failure.task_name],
            )
        )

    candidates.sort(key=lambda candidate: candidate.confidence, reverse=True)
    return candidates


def x__build_root_causes__mutmut_46(
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
                confidence=None,
                evidence=[f"{start_time} {failure.task_name}: {failure.root_cause}"],
                involved_objects=[failure.task_name],
            )
        )

    candidates.sort(key=lambda candidate: candidate.confidence, reverse=True)
    return candidates


def x__build_root_causes__mutmut_47(
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
                evidence=None,
                involved_objects=[failure.task_name],
            )
        )

    candidates.sort(key=lambda candidate: candidate.confidence, reverse=True)
    return candidates


def x__build_root_causes__mutmut_48(
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
                involved_objects=None,
            )
        )

    candidates.sort(key=lambda candidate: candidate.confidence, reverse=True)
    return candidates


def x__build_root_causes__mutmut_49(
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
                category=_FAILURE_TYPE_TO_CAUSE_CATEGORY[failure.failure_type],
                confidence=failure.confidence,
                evidence=[f"{start_time} {failure.task_name}: {failure.root_cause}"],
                involved_objects=[failure.task_name],
            )
        )

    candidates.sort(key=lambda candidate: candidate.confidence, reverse=True)
    return candidates


def x__build_root_causes__mutmut_50(
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
                confidence=failure.confidence,
                evidence=[f"{start_time} {failure.task_name}: {failure.root_cause}"],
                involved_objects=[failure.task_name],
            )
        )

    candidates.sort(key=lambda candidate: candidate.confidence, reverse=True)
    return candidates


def x__build_root_causes__mutmut_51(
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
                evidence=[f"{start_time} {failure.task_name}: {failure.root_cause}"],
                involved_objects=[failure.task_name],
            )
        )

    candidates.sort(key=lambda candidate: candidate.confidence, reverse=True)
    return candidates


def x__build_root_causes__mutmut_52(
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
                involved_objects=[failure.task_name],
            )
        )

    candidates.sort(key=lambda candidate: candidate.confidence, reverse=True)
    return candidates


def x__build_root_causes__mutmut_53(
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
                )
        )

    candidates.sort(key=lambda candidate: candidate.confidence, reverse=True)
    return candidates


def x__build_root_causes__mutmut_54(
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

    candidates.sort(key=None, reverse=True)
    return candidates


def x__build_root_causes__mutmut_55(
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

    candidates.sort(key=lambda candidate: candidate.confidence, reverse=None)
    return candidates


def x__build_root_causes__mutmut_56(
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

    candidates.sort(reverse=True)
    return candidates


def x__build_root_causes__mutmut_57(
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

    candidates.sort(key=lambda candidate: candidate.confidence, )
    return candidates


def x__build_root_causes__mutmut_58(
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

    candidates.sort(key=lambda candidate: None, reverse=True)
    return candidates


def x__build_root_causes__mutmut_59(
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

    candidates.sort(key=lambda candidate: candidate.confidence, reverse=False)
    return candidates

mutants_x__build_root_causes__mutmut['_mutmut_orig'] = x__build_root_causes__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_1'] = x__build_root_causes__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_2'] = x__build_root_causes__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_3'] = x__build_root_causes__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_4'] = x__build_root_causes__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_5'] = x__build_root_causes__mutmut_5 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_6'] = x__build_root_causes__mutmut_6 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_7'] = x__build_root_causes__mutmut_7 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_8'] = x__build_root_causes__mutmut_8 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_9'] = x__build_root_causes__mutmut_9 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_10'] = x__build_root_causes__mutmut_10 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_11'] = x__build_root_causes__mutmut_11 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_12'] = x__build_root_causes__mutmut_12 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_13'] = x__build_root_causes__mutmut_13 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_14'] = x__build_root_causes__mutmut_14 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_15'] = x__build_root_causes__mutmut_15 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_16'] = x__build_root_causes__mutmut_16 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_17'] = x__build_root_causes__mutmut_17 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_18'] = x__build_root_causes__mutmut_18 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_19'] = x__build_root_causes__mutmut_19 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_20'] = x__build_root_causes__mutmut_20 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_21'] = x__build_root_causes__mutmut_21 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_22'] = x__build_root_causes__mutmut_22 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_23'] = x__build_root_causes__mutmut_23 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_24'] = x__build_root_causes__mutmut_24 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_25'] = x__build_root_causes__mutmut_25 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_26'] = x__build_root_causes__mutmut_26 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_27'] = x__build_root_causes__mutmut_27 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_28'] = x__build_root_causes__mutmut_28 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_29'] = x__build_root_causes__mutmut_29 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_30'] = x__build_root_causes__mutmut_30 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_31'] = x__build_root_causes__mutmut_31 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_32'] = x__build_root_causes__mutmut_32 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_33'] = x__build_root_causes__mutmut_33 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_34'] = x__build_root_causes__mutmut_34 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_35'] = x__build_root_causes__mutmut_35 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_36'] = x__build_root_causes__mutmut_36 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_37'] = x__build_root_causes__mutmut_37 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_38'] = x__build_root_causes__mutmut_38 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_39'] = x__build_root_causes__mutmut_39 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_40'] = x__build_root_causes__mutmut_40 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_41'] = x__build_root_causes__mutmut_41 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_42'] = x__build_root_causes__mutmut_42 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_43'] = x__build_root_causes__mutmut_43 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_44'] = x__build_root_causes__mutmut_44 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_45'] = x__build_root_causes__mutmut_45 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_46'] = x__build_root_causes__mutmut_46 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_47'] = x__build_root_causes__mutmut_47 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_48'] = x__build_root_causes__mutmut_48 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_49'] = x__build_root_causes__mutmut_49 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_50'] = x__build_root_causes__mutmut_50 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_51'] = x__build_root_causes__mutmut_51 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_52'] = x__build_root_causes__mutmut_52 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_53'] = x__build_root_causes__mutmut_53 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_54'] = x__build_root_causes__mutmut_54 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_55'] = x__build_root_causes__mutmut_55 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_56'] = x__build_root_causes__mutmut_56 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_57'] = x__build_root_causes__mutmut_57 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_58'] = x__build_root_causes__mutmut_58 # type: ignore # mutmut generated
mutants_x__build_root_causes__mutmut['x__build_root_causes__mutmut_59'] = x__build_root_causes__mutmut_59 # type: ignore # mutmut generated
mutants_x__describe_candidate__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__describe_candidate__mutmut)
def _describe_candidate(category: IncidentCauseCategory, involved_objects: list[str]) -> str:
    if len(involved_objects) > 1:
        return (
            f"{category.value.replace('_', ' ')} issue affecting {len(involved_objects)} "
            f"objects — likely a shared root cause"
        )
    return f"{category.value.replace('_', ' ')} issue on {involved_objects[0]}"


def x__describe_candidate__mutmut_orig(category: IncidentCauseCategory, involved_objects: list[str]) -> str:
    if len(involved_objects) > 1:
        return (
            f"{category.value.replace('_', ' ')} issue affecting {len(involved_objects)} "
            f"objects — likely a shared root cause"
        )
    return f"{category.value.replace('_', ' ')} issue on {involved_objects[0]}"


def x__describe_candidate__mutmut_1(category: IncidentCauseCategory, involved_objects: list[str]) -> str:
    if len(involved_objects) >= 1:
        return (
            f"{category.value.replace('_', ' ')} issue affecting {len(involved_objects)} "
            f"objects — likely a shared root cause"
        )
    return f"{category.value.replace('_', ' ')} issue on {involved_objects[0]}"


def x__describe_candidate__mutmut_2(category: IncidentCauseCategory, involved_objects: list[str]) -> str:
    if len(involved_objects) > 2:
        return (
            f"{category.value.replace('_', ' ')} issue affecting {len(involved_objects)} "
            f"objects — likely a shared root cause"
        )
    return f"{category.value.replace('_', ' ')} issue on {involved_objects[0]}"


def x__describe_candidate__mutmut_3(category: IncidentCauseCategory, involved_objects: list[str]) -> str:
    if len(involved_objects) > 1:
        return (
            f"{category.value.replace(None, ' ')} issue affecting {len(involved_objects)} "
            f"objects — likely a shared root cause"
        )
    return f"{category.value.replace('_', ' ')} issue on {involved_objects[0]}"


def x__describe_candidate__mutmut_4(category: IncidentCauseCategory, involved_objects: list[str]) -> str:
    if len(involved_objects) > 1:
        return (
            f"{category.value.replace('_', None)} issue affecting {len(involved_objects)} "
            f"objects — likely a shared root cause"
        )
    return f"{category.value.replace('_', ' ')} issue on {involved_objects[0]}"


def x__describe_candidate__mutmut_5(category: IncidentCauseCategory, involved_objects: list[str]) -> str:
    if len(involved_objects) > 1:
        return (
            f"{category.value.replace(' ')} issue affecting {len(involved_objects)} "
            f"objects — likely a shared root cause"
        )
    return f"{category.value.replace('_', ' ')} issue on {involved_objects[0]}"


def x__describe_candidate__mutmut_6(category: IncidentCauseCategory, involved_objects: list[str]) -> str:
    if len(involved_objects) > 1:
        return (
            f"{category.value.replace('_', )} issue affecting {len(involved_objects)} "
            f"objects — likely a shared root cause"
        )
    return f"{category.value.replace('_', ' ')} issue on {involved_objects[0]}"


def x__describe_candidate__mutmut_7(category: IncidentCauseCategory, involved_objects: list[str]) -> str:
    if len(involved_objects) > 1:
        return (
            f"{category.value.replace('XX_XX', ' ')} issue affecting {len(involved_objects)} "
            f"objects — likely a shared root cause"
        )
    return f"{category.value.replace('_', ' ')} issue on {involved_objects[0]}"


def x__describe_candidate__mutmut_8(category: IncidentCauseCategory, involved_objects: list[str]) -> str:
    if len(involved_objects) > 1:
        return (
            f"{category.value.replace('_', 'XX XX')} issue affecting {len(involved_objects)} "
            f"objects — likely a shared root cause"
        )
    return f"{category.value.replace('_', ' ')} issue on {involved_objects[0]}"


def x__describe_candidate__mutmut_9(category: IncidentCauseCategory, involved_objects: list[str]) -> str:
    if len(involved_objects) > 1:
        return (
            f"{category.value.replace('_', ' ')} issue affecting {len(involved_objects)} "
            f"objects — likely a shared root cause"
        )
    return f"{category.value.replace(None, ' ')} issue on {involved_objects[0]}"


def x__describe_candidate__mutmut_10(category: IncidentCauseCategory, involved_objects: list[str]) -> str:
    if len(involved_objects) > 1:
        return (
            f"{category.value.replace('_', ' ')} issue affecting {len(involved_objects)} "
            f"objects — likely a shared root cause"
        )
    return f"{category.value.replace('_', None)} issue on {involved_objects[0]}"


def x__describe_candidate__mutmut_11(category: IncidentCauseCategory, involved_objects: list[str]) -> str:
    if len(involved_objects) > 1:
        return (
            f"{category.value.replace('_', ' ')} issue affecting {len(involved_objects)} "
            f"objects — likely a shared root cause"
        )
    return f"{category.value.replace(' ')} issue on {involved_objects[0]}"


def x__describe_candidate__mutmut_12(category: IncidentCauseCategory, involved_objects: list[str]) -> str:
    if len(involved_objects) > 1:
        return (
            f"{category.value.replace('_', ' ')} issue affecting {len(involved_objects)} "
            f"objects — likely a shared root cause"
        )
    return f"{category.value.replace('_', )} issue on {involved_objects[0]}"


def x__describe_candidate__mutmut_13(category: IncidentCauseCategory, involved_objects: list[str]) -> str:
    if len(involved_objects) > 1:
        return (
            f"{category.value.replace('_', ' ')} issue affecting {len(involved_objects)} "
            f"objects — likely a shared root cause"
        )
    return f"{category.value.replace('XX_XX', ' ')} issue on {involved_objects[0]}"


def x__describe_candidate__mutmut_14(category: IncidentCauseCategory, involved_objects: list[str]) -> str:
    if len(involved_objects) > 1:
        return (
            f"{category.value.replace('_', ' ')} issue affecting {len(involved_objects)} "
            f"objects — likely a shared root cause"
        )
    return f"{category.value.replace('_', 'XX XX')} issue on {involved_objects[0]}"


def x__describe_candidate__mutmut_15(category: IncidentCauseCategory, involved_objects: list[str]) -> str:
    if len(involved_objects) > 1:
        return (
            f"{category.value.replace('_', ' ')} issue affecting {len(involved_objects)} "
            f"objects — likely a shared root cause"
        )
    return f"{category.value.replace('_', ' ')} issue on {involved_objects[1]}"

mutants_x__describe_candidate__mutmut['_mutmut_orig'] = x__describe_candidate__mutmut_orig # type: ignore # mutmut generated
mutants_x__describe_candidate__mutmut['x__describe_candidate__mutmut_1'] = x__describe_candidate__mutmut_1 # type: ignore # mutmut generated
mutants_x__describe_candidate__mutmut['x__describe_candidate__mutmut_2'] = x__describe_candidate__mutmut_2 # type: ignore # mutmut generated
mutants_x__describe_candidate__mutmut['x__describe_candidate__mutmut_3'] = x__describe_candidate__mutmut_3 # type: ignore # mutmut generated
mutants_x__describe_candidate__mutmut['x__describe_candidate__mutmut_4'] = x__describe_candidate__mutmut_4 # type: ignore # mutmut generated
mutants_x__describe_candidate__mutmut['x__describe_candidate__mutmut_5'] = x__describe_candidate__mutmut_5 # type: ignore # mutmut generated
mutants_x__describe_candidate__mutmut['x__describe_candidate__mutmut_6'] = x__describe_candidate__mutmut_6 # type: ignore # mutmut generated
mutants_x__describe_candidate__mutmut['x__describe_candidate__mutmut_7'] = x__describe_candidate__mutmut_7 # type: ignore # mutmut generated
mutants_x__describe_candidate__mutmut['x__describe_candidate__mutmut_8'] = x__describe_candidate__mutmut_8 # type: ignore # mutmut generated
mutants_x__describe_candidate__mutmut['x__describe_candidate__mutmut_9'] = x__describe_candidate__mutmut_9 # type: ignore # mutmut generated
mutants_x__describe_candidate__mutmut['x__describe_candidate__mutmut_10'] = x__describe_candidate__mutmut_10 # type: ignore # mutmut generated
mutants_x__describe_candidate__mutmut['x__describe_candidate__mutmut_11'] = x__describe_candidate__mutmut_11 # type: ignore # mutmut generated
mutants_x__describe_candidate__mutmut['x__describe_candidate__mutmut_12'] = x__describe_candidate__mutmut_12 # type: ignore # mutmut generated
mutants_x__describe_candidate__mutmut['x__describe_candidate__mutmut_13'] = x__describe_candidate__mutmut_13 # type: ignore # mutmut generated
mutants_x__describe_candidate__mutmut['x__describe_candidate__mutmut_14'] = x__describe_candidate__mutmut_14 # type: ignore # mutmut generated
mutants_x__describe_candidate__mutmut['x__describe_candidate__mutmut_15'] = x__describe_candidate__mutmut_15 # type: ignore # mutmut generated
mutants_x__detect_resolution__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__detect_resolution__mutmut)
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


def x__detect_resolution__mutmut_orig(
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


def x__detect_resolution__mutmut_1(
    all_entries: list[TimelineEntry], failure_entries: list[TimelineEntry]
) -> tuple[bool, str | None, int | None]:
    if failure_entries:
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


def x__detect_resolution__mutmut_2(
    all_entries: list[TimelineEntry], failure_entries: list[TimelineEntry]
) -> tuple[bool, str | None, int | None]:
    if not failure_entries:
        return True, None, None

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


def x__detect_resolution__mutmut_3(
    all_entries: list[TimelineEntry], failure_entries: list[TimelineEntry]
) -> tuple[bool, str | None, int | None]:
    if not failure_entries:
        return False, None, None

    first_failure_time = None
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


def x__detect_resolution__mutmut_4(
    all_entries: list[TimelineEntry], failure_entries: list[TimelineEntry]
) -> tuple[bool, str | None, int | None]:
    if not failure_entries:
        return False, None, None

    first_failure_time = min(None)
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


def x__detect_resolution__mutmut_5(
    all_entries: list[TimelineEntry], failure_entries: list[TimelineEntry]
) -> tuple[bool, str | None, int | None]:
    if not failure_entries:
        return False, None, None

    first_failure_time = min(entry.timestamp for entry in failure_entries)
    last_failure_time = None

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


def x__detect_resolution__mutmut_6(
    all_entries: list[TimelineEntry], failure_entries: list[TimelineEntry]
) -> tuple[bool, str | None, int | None]:
    if not failure_entries:
        return False, None, None

    first_failure_time = min(entry.timestamp for entry in failure_entries)
    last_failure_time = max(None)

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


def x__detect_resolution__mutmut_7(
    all_entries: list[TimelineEntry], failure_entries: list[TimelineEntry]
) -> tuple[bool, str | None, int | None]:
    if not failure_entries:
        return False, None, None

    first_failure_time = min(entry.timestamp for entry in failure_entries)
    last_failure_time = max(entry.timestamp for entry in failure_entries)

    recovery_candidates = None
    if not recovery_candidates:
        return False, None, None

    resolution_time = min(entry.timestamp for entry in recovery_candidates)
    mttr_minutes = int(
        (_parse_timestamp(resolution_time) - _parse_timestamp(first_failure_time)).total_seconds()
        // 60
    )
    return True, resolution_time, mttr_minutes


def x__detect_resolution__mutmut_8(
    all_entries: list[TimelineEntry], failure_entries: list[TimelineEntry]
) -> tuple[bool, str | None, int | None]:
    if not failure_entries:
        return False, None, None

    first_failure_time = min(entry.timestamp for entry in failure_entries)
    last_failure_time = max(entry.timestamp for entry in failure_entries)

    recovery_candidates = [
        entry
        for entry in all_entries
        if entry.severity == _NORMAL_EVENT_TYPE or entry.timestamp > last_failure_time
    ]
    if not recovery_candidates:
        return False, None, None

    resolution_time = min(entry.timestamp for entry in recovery_candidates)
    mttr_minutes = int(
        (_parse_timestamp(resolution_time) - _parse_timestamp(first_failure_time)).total_seconds()
        // 60
    )
    return True, resolution_time, mttr_minutes


def x__detect_resolution__mutmut_9(
    all_entries: list[TimelineEntry], failure_entries: list[TimelineEntry]
) -> tuple[bool, str | None, int | None]:
    if not failure_entries:
        return False, None, None

    first_failure_time = min(entry.timestamp for entry in failure_entries)
    last_failure_time = max(entry.timestamp for entry in failure_entries)

    recovery_candidates = [
        entry
        for entry in all_entries
        if entry.severity != _NORMAL_EVENT_TYPE and entry.timestamp > last_failure_time
    ]
    if not recovery_candidates:
        return False, None, None

    resolution_time = min(entry.timestamp for entry in recovery_candidates)
    mttr_minutes = int(
        (_parse_timestamp(resolution_time) - _parse_timestamp(first_failure_time)).total_seconds()
        // 60
    )
    return True, resolution_time, mttr_minutes


def x__detect_resolution__mutmut_10(
    all_entries: list[TimelineEntry], failure_entries: list[TimelineEntry]
) -> tuple[bool, str | None, int | None]:
    if not failure_entries:
        return False, None, None

    first_failure_time = min(entry.timestamp for entry in failure_entries)
    last_failure_time = max(entry.timestamp for entry in failure_entries)

    recovery_candidates = [
        entry
        for entry in all_entries
        if entry.severity == _NORMAL_EVENT_TYPE and entry.timestamp >= last_failure_time
    ]
    if not recovery_candidates:
        return False, None, None

    resolution_time = min(entry.timestamp for entry in recovery_candidates)
    mttr_minutes = int(
        (_parse_timestamp(resolution_time) - _parse_timestamp(first_failure_time)).total_seconds()
        // 60
    )
    return True, resolution_time, mttr_minutes


def x__detect_resolution__mutmut_11(
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
    if recovery_candidates:
        return False, None, None

    resolution_time = min(entry.timestamp for entry in recovery_candidates)
    mttr_minutes = int(
        (_parse_timestamp(resolution_time) - _parse_timestamp(first_failure_time)).total_seconds()
        // 60
    )
    return True, resolution_time, mttr_minutes


def x__detect_resolution__mutmut_12(
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
        return True, None, None

    resolution_time = min(entry.timestamp for entry in recovery_candidates)
    mttr_minutes = int(
        (_parse_timestamp(resolution_time) - _parse_timestamp(first_failure_time)).total_seconds()
        // 60
    )
    return True, resolution_time, mttr_minutes


def x__detect_resolution__mutmut_13(
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

    resolution_time = None
    mttr_minutes = int(
        (_parse_timestamp(resolution_time) - _parse_timestamp(first_failure_time)).total_seconds()
        // 60
    )
    return True, resolution_time, mttr_minutes


def x__detect_resolution__mutmut_14(
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

    resolution_time = min(None)
    mttr_minutes = int(
        (_parse_timestamp(resolution_time) - _parse_timestamp(first_failure_time)).total_seconds()
        // 60
    )
    return True, resolution_time, mttr_minutes


def x__detect_resolution__mutmut_15(
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
    mttr_minutes = None
    return True, resolution_time, mttr_minutes


def x__detect_resolution__mutmut_16(
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
        None
    )
    return True, resolution_time, mttr_minutes


def x__detect_resolution__mutmut_17(
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
        (_parse_timestamp(resolution_time) - _parse_timestamp(first_failure_time)).total_seconds() / 60
    )
    return True, resolution_time, mttr_minutes


def x__detect_resolution__mutmut_18(
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
        (_parse_timestamp(resolution_time) + _parse_timestamp(first_failure_time)).total_seconds()
        // 60
    )
    return True, resolution_time, mttr_minutes


def x__detect_resolution__mutmut_19(
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
        (_parse_timestamp(None) - _parse_timestamp(first_failure_time)).total_seconds()
        // 60
    )
    return True, resolution_time, mttr_minutes


def x__detect_resolution__mutmut_20(
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
        (_parse_timestamp(resolution_time) - _parse_timestamp(None)).total_seconds()
        // 60
    )
    return True, resolution_time, mttr_minutes


def x__detect_resolution__mutmut_21(
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
        // 61
    )
    return True, resolution_time, mttr_minutes


def x__detect_resolution__mutmut_22(
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
    return False, resolution_time, mttr_minutes

mutants_x__detect_resolution__mutmut['_mutmut_orig'] = x__detect_resolution__mutmut_orig # type: ignore # mutmut generated
mutants_x__detect_resolution__mutmut['x__detect_resolution__mutmut_1'] = x__detect_resolution__mutmut_1 # type: ignore # mutmut generated
mutants_x__detect_resolution__mutmut['x__detect_resolution__mutmut_2'] = x__detect_resolution__mutmut_2 # type: ignore # mutmut generated
mutants_x__detect_resolution__mutmut['x__detect_resolution__mutmut_3'] = x__detect_resolution__mutmut_3 # type: ignore # mutmut generated
mutants_x__detect_resolution__mutmut['x__detect_resolution__mutmut_4'] = x__detect_resolution__mutmut_4 # type: ignore # mutmut generated
mutants_x__detect_resolution__mutmut['x__detect_resolution__mutmut_5'] = x__detect_resolution__mutmut_5 # type: ignore # mutmut generated
mutants_x__detect_resolution__mutmut['x__detect_resolution__mutmut_6'] = x__detect_resolution__mutmut_6 # type: ignore # mutmut generated
mutants_x__detect_resolution__mutmut['x__detect_resolution__mutmut_7'] = x__detect_resolution__mutmut_7 # type: ignore # mutmut generated
mutants_x__detect_resolution__mutmut['x__detect_resolution__mutmut_8'] = x__detect_resolution__mutmut_8 # type: ignore # mutmut generated
mutants_x__detect_resolution__mutmut['x__detect_resolution__mutmut_9'] = x__detect_resolution__mutmut_9 # type: ignore # mutmut generated
mutants_x__detect_resolution__mutmut['x__detect_resolution__mutmut_10'] = x__detect_resolution__mutmut_10 # type: ignore # mutmut generated
mutants_x__detect_resolution__mutmut['x__detect_resolution__mutmut_11'] = x__detect_resolution__mutmut_11 # type: ignore # mutmut generated
mutants_x__detect_resolution__mutmut['x__detect_resolution__mutmut_12'] = x__detect_resolution__mutmut_12 # type: ignore # mutmut generated
mutants_x__detect_resolution__mutmut['x__detect_resolution__mutmut_13'] = x__detect_resolution__mutmut_13 # type: ignore # mutmut generated
mutants_x__detect_resolution__mutmut['x__detect_resolution__mutmut_14'] = x__detect_resolution__mutmut_14 # type: ignore # mutmut generated
mutants_x__detect_resolution__mutmut['x__detect_resolution__mutmut_15'] = x__detect_resolution__mutmut_15 # type: ignore # mutmut generated
mutants_x__detect_resolution__mutmut['x__detect_resolution__mutmut_16'] = x__detect_resolution__mutmut_16 # type: ignore # mutmut generated
mutants_x__detect_resolution__mutmut['x__detect_resolution__mutmut_17'] = x__detect_resolution__mutmut_17 # type: ignore # mutmut generated
mutants_x__detect_resolution__mutmut['x__detect_resolution__mutmut_18'] = x__detect_resolution__mutmut_18 # type: ignore # mutmut generated
mutants_x__detect_resolution__mutmut['x__detect_resolution__mutmut_19'] = x__detect_resolution__mutmut_19 # type: ignore # mutmut generated
mutants_x__detect_resolution__mutmut['x__detect_resolution__mutmut_20'] = x__detect_resolution__mutmut_20 # type: ignore # mutmut generated
mutants_x__detect_resolution__mutmut['x__detect_resolution__mutmut_21'] = x__detect_resolution__mutmut_21 # type: ignore # mutmut generated
mutants_x__detect_resolution__mutmut['x__detect_resolution__mutmut_22'] = x__detect_resolution__mutmut_22 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_impact__mutmut)
def _build_impact(  # noqa: PLR0913
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


def x__build_impact__mutmut_orig(  # noqa: PLR0913
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


def x__build_impact__mutmut_1(  # noqa: PLR0913
    failure_entries: list[TimelineEntry],
    pods: list[PodInfo],
    root_causes: list[RootCauseCandidate],
    resolved: bool,
    resolution_time: str | None,
    observed_at: datetime,
) -> ImpactAssessment:
    if failure_entries:
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


def x__build_impact__mutmut_2(  # noqa: PLR0913
    failure_entries: list[TimelineEntry],
    pods: list[PodInfo],
    root_causes: list[RootCauseCandidate],
    resolved: bool,
    resolution_time: str | None,
    observed_at: datetime,
) -> ImpactAssessment:
    if not failure_entries:
        return ImpactAssessment()

    affected_services = None
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


def x__build_impact__mutmut_3(  # noqa: PLR0913
    failure_entries: list[TimelineEntry],
    pods: list[PodInfo],
    root_causes: list[RootCauseCandidate],
    resolved: bool,
    resolution_time: str | None,
    observed_at: datetime,
) -> ImpactAssessment:
    if not failure_entries:
        return ImpactAssessment()

    affected_services = set(None)
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


def x__build_impact__mutmut_4(  # noqa: PLR0913
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
    affected_services.update(None)

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


def x__build_impact__mutmut_5(  # noqa: PLR0913
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
    affected_services.update(pod["XXnameXX"] for pod in pods if pod["status"] != "Running")

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


def x__build_impact__mutmut_6(  # noqa: PLR0913
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
    affected_services.update(pod["NAME"] for pod in pods if pod["status"] != "Running")

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


def x__build_impact__mutmut_7(  # noqa: PLR0913
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
    affected_services.update(pod["name"] for pod in pods if pod["XXstatusXX"] != "Running")

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


def x__build_impact__mutmut_8(  # noqa: PLR0913
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
    affected_services.update(pod["name"] for pod in pods if pod["STATUS"] != "Running")

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


def x__build_impact__mutmut_9(  # noqa: PLR0913
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
    affected_services.update(pod["name"] for pod in pods if pod["status"] == "Running")

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


def x__build_impact__mutmut_10(  # noqa: PLR0913
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
    affected_services.update(pod["name"] for pod in pods if pod["status"] != "XXRunningXX")

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


def x__build_impact__mutmut_11(  # noqa: PLR0913
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
    affected_services.update(pod["name"] for pod in pods if pod["status"] != "running")

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


def x__build_impact__mutmut_12(  # noqa: PLR0913
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
    affected_services.update(pod["name"] for pod in pods if pod["status"] != "RUNNING")

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


def x__build_impact__mutmut_13(  # noqa: PLR0913
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

    impact_score = None

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


def x__build_impact__mutmut_14(  # noqa: PLR0913
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
        affected_tasks=None,
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


def x__build_impact__mutmut_15(  # noqa: PLR0913
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
        related_incidents=None,
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


def x__build_impact__mutmut_16(  # noqa: PLR0913
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
        timeline_events=None,
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


def x__build_impact__mutmut_17(  # noqa: PLR0913
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


def x__build_impact__mutmut_18(  # noqa: PLR0913
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


def x__build_impact__mutmut_19(  # noqa: PLR0913
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


def x__build_impact__mutmut_20(  # noqa: PLR0913
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
        related_incidents=max(None, 0),
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


def x__build_impact__mutmut_21(  # noqa: PLR0913
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
        related_incidents=max(len(root_causes) - 1, None),
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


def x__build_impact__mutmut_22(  # noqa: PLR0913
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
        related_incidents=max(0),
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


def x__build_impact__mutmut_23(  # noqa: PLR0913
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
        related_incidents=max(len(root_causes) - 1, ),
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


def x__build_impact__mutmut_24(  # noqa: PLR0913
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
        related_incidents=max(len(root_causes) + 1, 0),
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


def x__build_impact__mutmut_25(  # noqa: PLR0913
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
        related_incidents=max(len(root_causes) - 2, 0),
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


def x__build_impact__mutmut_26(  # noqa: PLR0913
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
        related_incidents=max(len(root_causes) - 1, 1),
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


def x__build_impact__mutmut_27(  # noqa: PLR0913
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

    first_failure_time = None
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


def x__build_impact__mutmut_28(  # noqa: PLR0913
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

    first_failure_time = min(None)
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


def x__build_impact__mutmut_29(  # noqa: PLR0913
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
    if resolved or resolution_time:
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


def x__build_impact__mutmut_30(  # noqa: PLR0913
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
        duration_minutes = None
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


def x__build_impact__mutmut_31(  # noqa: PLR0913
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
            None
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


def x__build_impact__mutmut_32(  # noqa: PLR0913
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
            ).total_seconds() / 60
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


def x__build_impact__mutmut_33(  # noqa: PLR0913
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
                _parse_timestamp(resolution_time) + _parse_timestamp(first_failure_time)
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


def x__build_impact__mutmut_34(  # noqa: PLR0913
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
                _parse_timestamp(None) - _parse_timestamp(first_failure_time)
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


def x__build_impact__mutmut_35(  # noqa: PLR0913
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
                _parse_timestamp(resolution_time) - _parse_timestamp(None)
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


def x__build_impact__mutmut_36(  # noqa: PLR0913
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
            // 61
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


def x__build_impact__mutmut_37(  # noqa: PLR0913
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
        duration_minutes = None

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


def x__build_impact__mutmut_38(  # noqa: PLR0913
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
            None
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


def x__build_impact__mutmut_39(  # noqa: PLR0913
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
            (observed_at - _parse_timestamp(first_failure_time)).total_seconds() / 60
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


def x__build_impact__mutmut_40(  # noqa: PLR0913
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
            (observed_at + _parse_timestamp(first_failure_time)).total_seconds() // 60
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


def x__build_impact__mutmut_41(  # noqa: PLR0913
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
            (observed_at - _parse_timestamp(None)).total_seconds() // 60
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


def x__build_impact__mutmut_42(  # noqa: PLR0913
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
            (observed_at - _parse_timestamp(first_failure_time)).total_seconds() // 61
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


def x__build_impact__mutmut_43(  # noqa: PLR0913
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

    estimated_user_impact = None

    return ImpactAssessment(
        affected_services=sorted(affected_services),
        estimated_user_impact=estimated_user_impact,
        duration_minutes=duration_minutes,
        ongoing=not resolved,
    )


def x__build_impact__mutmut_44(  # noqa: PLR0913
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
        affected_services=None,
        estimated_user_impact=estimated_user_impact,
        duration_minutes=duration_minutes,
        ongoing=not resolved,
    )


def x__build_impact__mutmut_45(  # noqa: PLR0913
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
        estimated_user_impact=None,
        duration_minutes=duration_minutes,
        ongoing=not resolved,
    )


def x__build_impact__mutmut_46(  # noqa: PLR0913
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
        duration_minutes=None,
        ongoing=not resolved,
    )


def x__build_impact__mutmut_47(  # noqa: PLR0913
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
        ongoing=None,
    )


def x__build_impact__mutmut_48(  # noqa: PLR0913
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
        estimated_user_impact=estimated_user_impact,
        duration_minutes=duration_minutes,
        ongoing=not resolved,
    )


def x__build_impact__mutmut_49(  # noqa: PLR0913
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
        duration_minutes=duration_minutes,
        ongoing=not resolved,
    )


def x__build_impact__mutmut_50(  # noqa: PLR0913
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
        ongoing=not resolved,
    )


def x__build_impact__mutmut_51(  # noqa: PLR0913
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
        )


def x__build_impact__mutmut_52(  # noqa: PLR0913
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
        affected_services=sorted(None),
        estimated_user_impact=estimated_user_impact,
        duration_minutes=duration_minutes,
        ongoing=not resolved,
    )


def x__build_impact__mutmut_53(  # noqa: PLR0913
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
        ongoing=resolved,
    )

mutants_x__build_impact__mutmut['_mutmut_orig'] = x__build_impact__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_1'] = x__build_impact__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_2'] = x__build_impact__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_3'] = x__build_impact__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_4'] = x__build_impact__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_5'] = x__build_impact__mutmut_5 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_6'] = x__build_impact__mutmut_6 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_7'] = x__build_impact__mutmut_7 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_8'] = x__build_impact__mutmut_8 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_9'] = x__build_impact__mutmut_9 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_10'] = x__build_impact__mutmut_10 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_11'] = x__build_impact__mutmut_11 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_12'] = x__build_impact__mutmut_12 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_13'] = x__build_impact__mutmut_13 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_14'] = x__build_impact__mutmut_14 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_15'] = x__build_impact__mutmut_15 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_16'] = x__build_impact__mutmut_16 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_17'] = x__build_impact__mutmut_17 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_18'] = x__build_impact__mutmut_18 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_19'] = x__build_impact__mutmut_19 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_20'] = x__build_impact__mutmut_20 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_21'] = x__build_impact__mutmut_21 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_22'] = x__build_impact__mutmut_22 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_23'] = x__build_impact__mutmut_23 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_24'] = x__build_impact__mutmut_24 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_25'] = x__build_impact__mutmut_25 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_26'] = x__build_impact__mutmut_26 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_27'] = x__build_impact__mutmut_27 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_28'] = x__build_impact__mutmut_28 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_29'] = x__build_impact__mutmut_29 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_30'] = x__build_impact__mutmut_30 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_31'] = x__build_impact__mutmut_31 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_32'] = x__build_impact__mutmut_32 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_33'] = x__build_impact__mutmut_33 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_34'] = x__build_impact__mutmut_34 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_35'] = x__build_impact__mutmut_35 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_36'] = x__build_impact__mutmut_36 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_37'] = x__build_impact__mutmut_37 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_38'] = x__build_impact__mutmut_38 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_39'] = x__build_impact__mutmut_39 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_40'] = x__build_impact__mutmut_40 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_41'] = x__build_impact__mutmut_41 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_42'] = x__build_impact__mutmut_42 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_43'] = x__build_impact__mutmut_43 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_44'] = x__build_impact__mutmut_44 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_45'] = x__build_impact__mutmut_45 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_46'] = x__build_impact__mutmut_46 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_47'] = x__build_impact__mutmut_47 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_48'] = x__build_impact__mutmut_48 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_49'] = x__build_impact__mutmut_49 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_50'] = x__build_impact__mutmut_50 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_51'] = x__build_impact__mutmut_51 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_52'] = x__build_impact__mutmut_52 # type: ignore # mutmut generated
mutants_x__build_impact__mutmut['x__build_impact__mutmut_53'] = x__build_impact__mutmut_53 # type: ignore # mutmut generated
mutants_x__detect_ntp_drift__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__detect_ntp_drift__mutmut)
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


def x__detect_ntp_drift__mutmut_orig(all_entries: list[TimelineEntry]) -> tuple[bool, str]:
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


def x__detect_ntp_drift__mutmut_1(all_entries: list[TimelineEntry]) -> tuple[bool, str]:
    earliest_event_by_object: dict[str, str] = None
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


def x__detect_ntp_drift__mutmut_2(all_entries: list[TimelineEntry]) -> tuple[bool, str]:
    earliest_event_by_object: dict[str, str] = {}
    for entry in all_entries:
        if entry.source == "event":
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


def x__detect_ntp_drift__mutmut_3(all_entries: list[TimelineEntry]) -> tuple[bool, str]:
    earliest_event_by_object: dict[str, str] = {}
    for entry in all_entries:
        if entry.source != "XXeventXX":
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


def x__detect_ntp_drift__mutmut_4(all_entries: list[TimelineEntry]) -> tuple[bool, str]:
    earliest_event_by_object: dict[str, str] = {}
    for entry in all_entries:
        if entry.source != "EVENT":
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


def x__detect_ntp_drift__mutmut_5(all_entries: list[TimelineEntry]) -> tuple[bool, str]:
    earliest_event_by_object: dict[str, str] = {}
    for entry in all_entries:
        if entry.source != "event":
            break
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


def x__detect_ntp_drift__mutmut_6(all_entries: list[TimelineEntry]) -> tuple[bool, str]:
    earliest_event_by_object: dict[str, str] = {}
    for entry in all_entries:
        if entry.source != "event":
            continue
        existing = None
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


def x__detect_ntp_drift__mutmut_7(all_entries: list[TimelineEntry]) -> tuple[bool, str]:
    earliest_event_by_object: dict[str, str] = {}
    for entry in all_entries:
        if entry.source != "event":
            continue
        existing = earliest_event_by_object.get(None)
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


def x__detect_ntp_drift__mutmut_8(all_entries: list[TimelineEntry]) -> tuple[bool, str]:
    earliest_event_by_object: dict[str, str] = {}
    for entry in all_entries:
        if entry.source != "event":
            continue
        existing = earliest_event_by_object.get(entry.object)
        if existing is None and entry.timestamp < existing:
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


def x__detect_ntp_drift__mutmut_9(all_entries: list[TimelineEntry]) -> tuple[bool, str]:
    earliest_event_by_object: dict[str, str] = {}
    for entry in all_entries:
        if entry.source != "event":
            continue
        existing = earliest_event_by_object.get(entry.object)
        if existing is not None or entry.timestamp < existing:
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


def x__detect_ntp_drift__mutmut_10(all_entries: list[TimelineEntry]) -> tuple[bool, str]:
    earliest_event_by_object: dict[str, str] = {}
    for entry in all_entries:
        if entry.source != "event":
            continue
        existing = earliest_event_by_object.get(entry.object)
        if existing is None or entry.timestamp <= existing:
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


def x__detect_ntp_drift__mutmut_11(all_entries: list[TimelineEntry]) -> tuple[bool, str]:
    earliest_event_by_object: dict[str, str] = {}
    for entry in all_entries:
        if entry.source != "event":
            continue
        existing = earliest_event_by_object.get(entry.object)
        if existing is None or entry.timestamp < existing:
            earliest_event_by_object[entry.object] = None

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


def x__detect_ntp_drift__mutmut_12(all_entries: list[TimelineEntry]) -> tuple[bool, str]:
    earliest_event_by_object: dict[str, str] = {}
    for entry in all_entries:
        if entry.source != "event":
            continue
        existing = earliest_event_by_object.get(entry.object)
        if existing is None or entry.timestamp < existing:
            earliest_event_by_object[entry.object] = entry.timestamp

    for entry in all_entries:
        if entry.source != "log" and entry.object not in earliest_event_by_object:
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


def x__detect_ntp_drift__mutmut_13(all_entries: list[TimelineEntry]) -> tuple[bool, str]:
    earliest_event_by_object: dict[str, str] = {}
    for entry in all_entries:
        if entry.source != "event":
            continue
        existing = earliest_event_by_object.get(entry.object)
        if existing is None or entry.timestamp < existing:
            earliest_event_by_object[entry.object] = entry.timestamp

    for entry in all_entries:
        if entry.source == "log" or entry.object not in earliest_event_by_object:
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


def x__detect_ntp_drift__mutmut_14(all_entries: list[TimelineEntry]) -> tuple[bool, str]:
    earliest_event_by_object: dict[str, str] = {}
    for entry in all_entries:
        if entry.source != "event":
            continue
        existing = earliest_event_by_object.get(entry.object)
        if existing is None or entry.timestamp < existing:
            earliest_event_by_object[entry.object] = entry.timestamp

    for entry in all_entries:
        if entry.source != "XXlogXX" or entry.object not in earliest_event_by_object:
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


def x__detect_ntp_drift__mutmut_15(all_entries: list[TimelineEntry]) -> tuple[bool, str]:
    earliest_event_by_object: dict[str, str] = {}
    for entry in all_entries:
        if entry.source != "event":
            continue
        existing = earliest_event_by_object.get(entry.object)
        if existing is None or entry.timestamp < existing:
            earliest_event_by_object[entry.object] = entry.timestamp

    for entry in all_entries:
        if entry.source != "LOG" or entry.object not in earliest_event_by_object:
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


def x__detect_ntp_drift__mutmut_16(all_entries: list[TimelineEntry]) -> tuple[bool, str]:
    earliest_event_by_object: dict[str, str] = {}
    for entry in all_entries:
        if entry.source != "event":
            continue
        existing = earliest_event_by_object.get(entry.object)
        if existing is None or entry.timestamp < existing:
            earliest_event_by_object[entry.object] = entry.timestamp

    for entry in all_entries:
        if entry.source != "log" or entry.object in earliest_event_by_object:
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


def x__detect_ntp_drift__mutmut_17(all_entries: list[TimelineEntry]) -> tuple[bool, str]:
    earliest_event_by_object: dict[str, str] = {}
    for entry in all_entries:
        if entry.source != "event":
            continue
        existing = earliest_event_by_object.get(entry.object)
        if existing is None or entry.timestamp < existing:
            earliest_event_by_object[entry.object] = entry.timestamp

    for entry in all_entries:
        if entry.source != "log" or entry.object not in earliest_event_by_object:
            break
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


def x__detect_ntp_drift__mutmut_18(all_entries: list[TimelineEntry]) -> tuple[bool, str]:
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
        event_time = None
        diff_seconds = (
            _parse_timestamp(event_time) - _parse_timestamp(entry.timestamp)
        ).total_seconds()
        if diff_seconds > _cfg.ntp_drift_threshold_seconds:
            return True, (
                f"Log and event timestamps for {entry.object} differ by {int(diff_seconds)}s "
                "— possible clock drift between log shipper and API server."
            )
    return False, ""


def x__detect_ntp_drift__mutmut_19(all_entries: list[TimelineEntry]) -> tuple[bool, str]:
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
        diff_seconds = None
        if diff_seconds > _cfg.ntp_drift_threshold_seconds:
            return True, (
                f"Log and event timestamps for {entry.object} differ by {int(diff_seconds)}s "
                "— possible clock drift between log shipper and API server."
            )
    return False, ""


def x__detect_ntp_drift__mutmut_20(all_entries: list[TimelineEntry]) -> tuple[bool, str]:
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
            _parse_timestamp(event_time) + _parse_timestamp(entry.timestamp)
        ).total_seconds()
        if diff_seconds > _cfg.ntp_drift_threshold_seconds:
            return True, (
                f"Log and event timestamps for {entry.object} differ by {int(diff_seconds)}s "
                "— possible clock drift between log shipper and API server."
            )
    return False, ""


def x__detect_ntp_drift__mutmut_21(all_entries: list[TimelineEntry]) -> tuple[bool, str]:
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
            _parse_timestamp(None) - _parse_timestamp(entry.timestamp)
        ).total_seconds()
        if diff_seconds > _cfg.ntp_drift_threshold_seconds:
            return True, (
                f"Log and event timestamps for {entry.object} differ by {int(diff_seconds)}s "
                "— possible clock drift between log shipper and API server."
            )
    return False, ""


def x__detect_ntp_drift__mutmut_22(all_entries: list[TimelineEntry]) -> tuple[bool, str]:
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
            _parse_timestamp(event_time) - _parse_timestamp(None)
        ).total_seconds()
        if diff_seconds > _cfg.ntp_drift_threshold_seconds:
            return True, (
                f"Log and event timestamps for {entry.object} differ by {int(diff_seconds)}s "
                "— possible clock drift between log shipper and API server."
            )
    return False, ""


def x__detect_ntp_drift__mutmut_23(all_entries: list[TimelineEntry]) -> tuple[bool, str]:
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
        if diff_seconds >= _cfg.ntp_drift_threshold_seconds:
            return True, (
                f"Log and event timestamps for {entry.object} differ by {int(diff_seconds)}s "
                "— possible clock drift between log shipper and API server."
            )
    return False, ""


def x__detect_ntp_drift__mutmut_24(all_entries: list[TimelineEntry]) -> tuple[bool, str]:
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
            return False, (
                f"Log and event timestamps for {entry.object} differ by {int(diff_seconds)}s "
                "— possible clock drift between log shipper and API server."
            )
    return False, ""


def x__detect_ntp_drift__mutmut_25(all_entries: list[TimelineEntry]) -> tuple[bool, str]:
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
                f"Log and event timestamps for {entry.object} differ by {int(None)}s "
                "— possible clock drift between log shipper and API server."
            )
    return False, ""


def x__detect_ntp_drift__mutmut_26(all_entries: list[TimelineEntry]) -> tuple[bool, str]:
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
                "XX— possible clock drift between log shipper and API server.XX"
            )
    return False, ""


def x__detect_ntp_drift__mutmut_27(all_entries: list[TimelineEntry]) -> tuple[bool, str]:
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
                "— possible clock drift between log shipper and api server."
            )
    return False, ""


def x__detect_ntp_drift__mutmut_28(all_entries: list[TimelineEntry]) -> tuple[bool, str]:
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
                "— POSSIBLE CLOCK DRIFT BETWEEN LOG SHIPPER AND API SERVER."
            )
    return False, ""


def x__detect_ntp_drift__mutmut_29(all_entries: list[TimelineEntry]) -> tuple[bool, str]:
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
    return True, ""


def x__detect_ntp_drift__mutmut_30(all_entries: list[TimelineEntry]) -> tuple[bool, str]:
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
    return False, "XXXX"

mutants_x__detect_ntp_drift__mutmut['_mutmut_orig'] = x__detect_ntp_drift__mutmut_orig # type: ignore # mutmut generated
mutants_x__detect_ntp_drift__mutmut['x__detect_ntp_drift__mutmut_1'] = x__detect_ntp_drift__mutmut_1 # type: ignore # mutmut generated
mutants_x__detect_ntp_drift__mutmut['x__detect_ntp_drift__mutmut_2'] = x__detect_ntp_drift__mutmut_2 # type: ignore # mutmut generated
mutants_x__detect_ntp_drift__mutmut['x__detect_ntp_drift__mutmut_3'] = x__detect_ntp_drift__mutmut_3 # type: ignore # mutmut generated
mutants_x__detect_ntp_drift__mutmut['x__detect_ntp_drift__mutmut_4'] = x__detect_ntp_drift__mutmut_4 # type: ignore # mutmut generated
mutants_x__detect_ntp_drift__mutmut['x__detect_ntp_drift__mutmut_5'] = x__detect_ntp_drift__mutmut_5 # type: ignore # mutmut generated
mutants_x__detect_ntp_drift__mutmut['x__detect_ntp_drift__mutmut_6'] = x__detect_ntp_drift__mutmut_6 # type: ignore # mutmut generated
mutants_x__detect_ntp_drift__mutmut['x__detect_ntp_drift__mutmut_7'] = x__detect_ntp_drift__mutmut_7 # type: ignore # mutmut generated
mutants_x__detect_ntp_drift__mutmut['x__detect_ntp_drift__mutmut_8'] = x__detect_ntp_drift__mutmut_8 # type: ignore # mutmut generated
mutants_x__detect_ntp_drift__mutmut['x__detect_ntp_drift__mutmut_9'] = x__detect_ntp_drift__mutmut_9 # type: ignore # mutmut generated
mutants_x__detect_ntp_drift__mutmut['x__detect_ntp_drift__mutmut_10'] = x__detect_ntp_drift__mutmut_10 # type: ignore # mutmut generated
mutants_x__detect_ntp_drift__mutmut['x__detect_ntp_drift__mutmut_11'] = x__detect_ntp_drift__mutmut_11 # type: ignore # mutmut generated
mutants_x__detect_ntp_drift__mutmut['x__detect_ntp_drift__mutmut_12'] = x__detect_ntp_drift__mutmut_12 # type: ignore # mutmut generated
mutants_x__detect_ntp_drift__mutmut['x__detect_ntp_drift__mutmut_13'] = x__detect_ntp_drift__mutmut_13 # type: ignore # mutmut generated
mutants_x__detect_ntp_drift__mutmut['x__detect_ntp_drift__mutmut_14'] = x__detect_ntp_drift__mutmut_14 # type: ignore # mutmut generated
mutants_x__detect_ntp_drift__mutmut['x__detect_ntp_drift__mutmut_15'] = x__detect_ntp_drift__mutmut_15 # type: ignore # mutmut generated
mutants_x__detect_ntp_drift__mutmut['x__detect_ntp_drift__mutmut_16'] = x__detect_ntp_drift__mutmut_16 # type: ignore # mutmut generated
mutants_x__detect_ntp_drift__mutmut['x__detect_ntp_drift__mutmut_17'] = x__detect_ntp_drift__mutmut_17 # type: ignore # mutmut generated
mutants_x__detect_ntp_drift__mutmut['x__detect_ntp_drift__mutmut_18'] = x__detect_ntp_drift__mutmut_18 # type: ignore # mutmut generated
mutants_x__detect_ntp_drift__mutmut['x__detect_ntp_drift__mutmut_19'] = x__detect_ntp_drift__mutmut_19 # type: ignore # mutmut generated
mutants_x__detect_ntp_drift__mutmut['x__detect_ntp_drift__mutmut_20'] = x__detect_ntp_drift__mutmut_20 # type: ignore # mutmut generated
mutants_x__detect_ntp_drift__mutmut['x__detect_ntp_drift__mutmut_21'] = x__detect_ntp_drift__mutmut_21 # type: ignore # mutmut generated
mutants_x__detect_ntp_drift__mutmut['x__detect_ntp_drift__mutmut_22'] = x__detect_ntp_drift__mutmut_22 # type: ignore # mutmut generated
mutants_x__detect_ntp_drift__mutmut['x__detect_ntp_drift__mutmut_23'] = x__detect_ntp_drift__mutmut_23 # type: ignore # mutmut generated
mutants_x__detect_ntp_drift__mutmut['x__detect_ntp_drift__mutmut_24'] = x__detect_ntp_drift__mutmut_24 # type: ignore # mutmut generated
mutants_x__detect_ntp_drift__mutmut['x__detect_ntp_drift__mutmut_25'] = x__detect_ntp_drift__mutmut_25 # type: ignore # mutmut generated
mutants_x__detect_ntp_drift__mutmut['x__detect_ntp_drift__mutmut_26'] = x__detect_ntp_drift__mutmut_26 # type: ignore # mutmut generated
mutants_x__detect_ntp_drift__mutmut['x__detect_ntp_drift__mutmut_27'] = x__detect_ntp_drift__mutmut_27 # type: ignore # mutmut generated
mutants_x__detect_ntp_drift__mutmut['x__detect_ntp_drift__mutmut_28'] = x__detect_ntp_drift__mutmut_28 # type: ignore # mutmut generated
mutants_x__detect_ntp_drift__mutmut['x__detect_ntp_drift__mutmut_29'] = x__detect_ntp_drift__mutmut_29 # type: ignore # mutmut generated
mutants_x__detect_ntp_drift__mutmut['x__detect_ntp_drift__mutmut_30'] = x__detect_ntp_drift__mutmut_30 # type: ignore # mutmut generated
mutants_x__correlate_cross_namespace__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__correlate_cross_namespace__mutmut)
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


def x__correlate_cross_namespace__mutmut_orig(
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


def x__correlate_cross_namespace__mutmut_1(
    root_causes: list[RootCauseCandidate],
    related_namespace_events: dict[str, list[NamespaceEvent]],
) -> list[str]:
    if not root_causes and not related_namespace_events:
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


def x__correlate_cross_namespace__mutmut_2(
    root_causes: list[RootCauseCandidate],
    related_namespace_events: dict[str, list[NamespaceEvent]],
) -> list[str]:
    if root_causes or not related_namespace_events:
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


def x__correlate_cross_namespace__mutmut_3(
    root_causes: list[RootCauseCandidate],
    related_namespace_events: dict[str, list[NamespaceEvent]],
) -> list[str]:
    if not root_causes or related_namespace_events:
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


def x__correlate_cross_namespace__mutmut_4(
    root_causes: list[RootCauseCandidate],
    related_namespace_events: dict[str, list[NamespaceEvent]],
) -> list[str]:
    if not root_causes or not related_namespace_events:
        return []

    top_category = None
    correlated: list[str] = []
    for namespace, events in related_namespace_events.items():
        for event in events:
            if event.event_type not in _FAILURE_EVENT_TYPES:
                continue
            category = classify_incident_cause(f"{event.reason} {event.message}")
            if category == top_category:
                correlated.append(f"{namespace}: {event.object} ({event.reason})")
    return correlated


def x__correlate_cross_namespace__mutmut_5(
    root_causes: list[RootCauseCandidate],
    related_namespace_events: dict[str, list[NamespaceEvent]],
) -> list[str]:
    if not root_causes or not related_namespace_events:
        return []

    top_category = root_causes[1].category
    correlated: list[str] = []
    for namespace, events in related_namespace_events.items():
        for event in events:
            if event.event_type not in _FAILURE_EVENT_TYPES:
                continue
            category = classify_incident_cause(f"{event.reason} {event.message}")
            if category == top_category:
                correlated.append(f"{namespace}: {event.object} ({event.reason})")
    return correlated


def x__correlate_cross_namespace__mutmut_6(
    root_causes: list[RootCauseCandidate],
    related_namespace_events: dict[str, list[NamespaceEvent]],
) -> list[str]:
    if not root_causes or not related_namespace_events:
        return []

    top_category = root_causes[0].category
    correlated: list[str] = None
    for namespace, events in related_namespace_events.items():
        for event in events:
            if event.event_type not in _FAILURE_EVENT_TYPES:
                continue
            category = classify_incident_cause(f"{event.reason} {event.message}")
            if category == top_category:
                correlated.append(f"{namespace}: {event.object} ({event.reason})")
    return correlated


def x__correlate_cross_namespace__mutmut_7(
    root_causes: list[RootCauseCandidate],
    related_namespace_events: dict[str, list[NamespaceEvent]],
) -> list[str]:
    if not root_causes or not related_namespace_events:
        return []

    top_category = root_causes[0].category
    correlated: list[str] = []
    for namespace, events in related_namespace_events.items():
        for event in events:
            if event.event_type in _FAILURE_EVENT_TYPES:
                continue
            category = classify_incident_cause(f"{event.reason} {event.message}")
            if category == top_category:
                correlated.append(f"{namespace}: {event.object} ({event.reason})")
    return correlated


def x__correlate_cross_namespace__mutmut_8(
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
                break
            category = classify_incident_cause(f"{event.reason} {event.message}")
            if category == top_category:
                correlated.append(f"{namespace}: {event.object} ({event.reason})")
    return correlated


def x__correlate_cross_namespace__mutmut_9(
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
            category = None
            if category == top_category:
                correlated.append(f"{namespace}: {event.object} ({event.reason})")
    return correlated


def x__correlate_cross_namespace__mutmut_10(
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
            category = classify_incident_cause(None)
            if category == top_category:
                correlated.append(f"{namespace}: {event.object} ({event.reason})")
    return correlated


def x__correlate_cross_namespace__mutmut_11(
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
            if category != top_category:
                correlated.append(f"{namespace}: {event.object} ({event.reason})")
    return correlated


def x__correlate_cross_namespace__mutmut_12(
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
                correlated.append(None)
    return correlated

mutants_x__correlate_cross_namespace__mutmut['_mutmut_orig'] = x__correlate_cross_namespace__mutmut_orig # type: ignore # mutmut generated
mutants_x__correlate_cross_namespace__mutmut['x__correlate_cross_namespace__mutmut_1'] = x__correlate_cross_namespace__mutmut_1 # type: ignore # mutmut generated
mutants_x__correlate_cross_namespace__mutmut['x__correlate_cross_namespace__mutmut_2'] = x__correlate_cross_namespace__mutmut_2 # type: ignore # mutmut generated
mutants_x__correlate_cross_namespace__mutmut['x__correlate_cross_namespace__mutmut_3'] = x__correlate_cross_namespace__mutmut_3 # type: ignore # mutmut generated
mutants_x__correlate_cross_namespace__mutmut['x__correlate_cross_namespace__mutmut_4'] = x__correlate_cross_namespace__mutmut_4 # type: ignore # mutmut generated
mutants_x__correlate_cross_namespace__mutmut['x__correlate_cross_namespace__mutmut_5'] = x__correlate_cross_namespace__mutmut_5 # type: ignore # mutmut generated
mutants_x__correlate_cross_namespace__mutmut['x__correlate_cross_namespace__mutmut_6'] = x__correlate_cross_namespace__mutmut_6 # type: ignore # mutmut generated
mutants_x__correlate_cross_namespace__mutmut['x__correlate_cross_namespace__mutmut_7'] = x__correlate_cross_namespace__mutmut_7 # type: ignore # mutmut generated
mutants_x__correlate_cross_namespace__mutmut['x__correlate_cross_namespace__mutmut_8'] = x__correlate_cross_namespace__mutmut_8 # type: ignore # mutmut generated
mutants_x__correlate_cross_namespace__mutmut['x__correlate_cross_namespace__mutmut_9'] = x__correlate_cross_namespace__mutmut_9 # type: ignore # mutmut generated
mutants_x__correlate_cross_namespace__mutmut['x__correlate_cross_namespace__mutmut_10'] = x__correlate_cross_namespace__mutmut_10 # type: ignore # mutmut generated
mutants_x__correlate_cross_namespace__mutmut['x__correlate_cross_namespace__mutmut_11'] = x__correlate_cross_namespace__mutmut_11 # type: ignore # mutmut generated
mutants_x__correlate_cross_namespace__mutmut['x__correlate_cross_namespace__mutmut_12'] = x__correlate_cross_namespace__mutmut_12 # type: ignore # mutmut generated
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
