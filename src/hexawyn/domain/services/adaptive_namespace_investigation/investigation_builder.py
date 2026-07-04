from __future__ import annotations

from hexawyn.domain.models.adaptive_namespace_investigation import (
    AdaptiveInvestigationReport,
    AdaptiveInvestigationRequest,
    OverviewSnapshot,
    ResourceInvestigation,
)
from hexawyn.domain.models.incident_triage import IncidentCauseCategory, RootCauseCandidate
from hexawyn.domain.services.incident_triage.root_cause_classifier import (
    classify_incident_cause,
    remediation_for,
)

_RESOLVED_CONFIDENCE = 0.85
_UNKNOWN_CONFIDENCE = 0.3


def build_adaptive_investigation(
    request: AdaptiveInvestigationRequest,
    overview: OverviewSnapshot,
    investigated_resources: list[ResourceInvestigation],
    skipped_resources: list[str],
    node_pressure_context: str | None,
    has_more_failing: bool,
    remaining_failing_count: int,
) -> AdaptiveInvestigationReport:
    """Pure composition — investigated_resources are already ranked and
    already drilled (by the service, via select_top_critical +
    AdaptiveInvestigationPort); this function only builds root-cause
    candidates/recommendations from that already-fetched evidence."""
    candidates = [_build_candidate(investigation) for investigation in investigated_resources]
    candidates.sort(key=lambda candidate: candidate.confidence, reverse=True)

    recommended_actions: list[str] = []
    for candidate in candidates:
        action = remediation_for(candidate.category)
        if action not in recommended_actions:
            recommended_actions.append(action)

    return AdaptiveInvestigationReport(
        namespace=overview.namespace,
        namespace_status=overview.namespace_status,
        health_status=overview.health_status,
        overview_summary=overview.summary,
        investigated_resources=investigated_resources,
        root_cause_candidates=candidates,
        recommended_actions=recommended_actions,
        skipped_resources=skipped_resources,
        node_pressure_context=node_pressure_context,
        has_more_failing=has_more_failing,
        remaining_failing_count=remaining_failing_count,
    )


def _build_candidate(investigation: ResourceInvestigation) -> RootCauseCandidate:
    evidence = list(investigation.events) + list(investigation.logs)
    if investigation.last_termination_reason:
        evidence.append(f"Last termination reason: {investigation.last_termination_reason}")

    text = " ".join([investigation.resource.reason, *evidence])
    category = classify_incident_cause(text)
    confidence = (
        _RESOLVED_CONFIDENCE if category != IncidentCauseCategory.UNKNOWN else _UNKNOWN_CONFIDENCE
    )

    return RootCauseCandidate(
        description=f"{investigation.resource.name}: {investigation.resource.reason}",
        category=category,
        confidence=confidence,
        evidence=evidence,
        involved_objects=[investigation.resource.name],
    )
