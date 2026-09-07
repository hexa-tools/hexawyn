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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_adaptive_investigation__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_adaptive_investigation__mutmut)
def build_adaptive_investigation(  # noqa: PLR0913
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


def x_build_adaptive_investigation__mutmut_orig(  # noqa: PLR0913
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


def x_build_adaptive_investigation__mutmut_1(  # noqa: PLR0913
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
    candidates = None
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


def x_build_adaptive_investigation__mutmut_2(  # noqa: PLR0913
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
    candidates = [_build_candidate(None) for investigation in investigated_resources]
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


def x_build_adaptive_investigation__mutmut_3(  # noqa: PLR0913
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
    candidates.sort(key=None, reverse=True)

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


def x_build_adaptive_investigation__mutmut_4(  # noqa: PLR0913
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
    candidates.sort(key=lambda candidate: candidate.confidence, reverse=None)

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


def x_build_adaptive_investigation__mutmut_5(  # noqa: PLR0913
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
    candidates.sort(reverse=True)

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


def x_build_adaptive_investigation__mutmut_6(  # noqa: PLR0913
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
    candidates.sort(key=lambda candidate: candidate.confidence, )

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


def x_build_adaptive_investigation__mutmut_7(  # noqa: PLR0913
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
    candidates.sort(key=lambda candidate: None, reverse=True)

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


def x_build_adaptive_investigation__mutmut_8(  # noqa: PLR0913
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
    candidates.sort(key=lambda candidate: candidate.confidence, reverse=False)

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


def x_build_adaptive_investigation__mutmut_9(  # noqa: PLR0913
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

    recommended_actions: list[str] = None
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


def x_build_adaptive_investigation__mutmut_10(  # noqa: PLR0913
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
        action = None
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


def x_build_adaptive_investigation__mutmut_11(  # noqa: PLR0913
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
        action = remediation_for(None)
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


def x_build_adaptive_investigation__mutmut_12(  # noqa: PLR0913
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
        if action in recommended_actions:
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


def x_build_adaptive_investigation__mutmut_13(  # noqa: PLR0913
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
            recommended_actions.append(None)

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


def x_build_adaptive_investigation__mutmut_14(  # noqa: PLR0913
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
        namespace=None,
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


def x_build_adaptive_investigation__mutmut_15(  # noqa: PLR0913
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
        namespace_status=None,
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


def x_build_adaptive_investigation__mutmut_16(  # noqa: PLR0913
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
        health_status=None,
        overview_summary=overview.summary,
        investigated_resources=investigated_resources,
        root_cause_candidates=candidates,
        recommended_actions=recommended_actions,
        skipped_resources=skipped_resources,
        node_pressure_context=node_pressure_context,
        has_more_failing=has_more_failing,
        remaining_failing_count=remaining_failing_count,
    )


def x_build_adaptive_investigation__mutmut_17(  # noqa: PLR0913
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
        overview_summary=None,
        investigated_resources=investigated_resources,
        root_cause_candidates=candidates,
        recommended_actions=recommended_actions,
        skipped_resources=skipped_resources,
        node_pressure_context=node_pressure_context,
        has_more_failing=has_more_failing,
        remaining_failing_count=remaining_failing_count,
    )


def x_build_adaptive_investigation__mutmut_18(  # noqa: PLR0913
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
        investigated_resources=None,
        root_cause_candidates=candidates,
        recommended_actions=recommended_actions,
        skipped_resources=skipped_resources,
        node_pressure_context=node_pressure_context,
        has_more_failing=has_more_failing,
        remaining_failing_count=remaining_failing_count,
    )


def x_build_adaptive_investigation__mutmut_19(  # noqa: PLR0913
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
        root_cause_candidates=None,
        recommended_actions=recommended_actions,
        skipped_resources=skipped_resources,
        node_pressure_context=node_pressure_context,
        has_more_failing=has_more_failing,
        remaining_failing_count=remaining_failing_count,
    )


def x_build_adaptive_investigation__mutmut_20(  # noqa: PLR0913
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
        recommended_actions=None,
        skipped_resources=skipped_resources,
        node_pressure_context=node_pressure_context,
        has_more_failing=has_more_failing,
        remaining_failing_count=remaining_failing_count,
    )


def x_build_adaptive_investigation__mutmut_21(  # noqa: PLR0913
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
        skipped_resources=None,
        node_pressure_context=node_pressure_context,
        has_more_failing=has_more_failing,
        remaining_failing_count=remaining_failing_count,
    )


def x_build_adaptive_investigation__mutmut_22(  # noqa: PLR0913
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
        node_pressure_context=None,
        has_more_failing=has_more_failing,
        remaining_failing_count=remaining_failing_count,
    )


def x_build_adaptive_investigation__mutmut_23(  # noqa: PLR0913
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
        has_more_failing=None,
        remaining_failing_count=remaining_failing_count,
    )


def x_build_adaptive_investigation__mutmut_24(  # noqa: PLR0913
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
        remaining_failing_count=None,
    )


def x_build_adaptive_investigation__mutmut_25(  # noqa: PLR0913
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


def x_build_adaptive_investigation__mutmut_26(  # noqa: PLR0913
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


def x_build_adaptive_investigation__mutmut_27(  # noqa: PLR0913
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
        overview_summary=overview.summary,
        investigated_resources=investigated_resources,
        root_cause_candidates=candidates,
        recommended_actions=recommended_actions,
        skipped_resources=skipped_resources,
        node_pressure_context=node_pressure_context,
        has_more_failing=has_more_failing,
        remaining_failing_count=remaining_failing_count,
    )


def x_build_adaptive_investigation__mutmut_28(  # noqa: PLR0913
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
        investigated_resources=investigated_resources,
        root_cause_candidates=candidates,
        recommended_actions=recommended_actions,
        skipped_resources=skipped_resources,
        node_pressure_context=node_pressure_context,
        has_more_failing=has_more_failing,
        remaining_failing_count=remaining_failing_count,
    )


def x_build_adaptive_investigation__mutmut_29(  # noqa: PLR0913
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
        root_cause_candidates=candidates,
        recommended_actions=recommended_actions,
        skipped_resources=skipped_resources,
        node_pressure_context=node_pressure_context,
        has_more_failing=has_more_failing,
        remaining_failing_count=remaining_failing_count,
    )


def x_build_adaptive_investigation__mutmut_30(  # noqa: PLR0913
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
        recommended_actions=recommended_actions,
        skipped_resources=skipped_resources,
        node_pressure_context=node_pressure_context,
        has_more_failing=has_more_failing,
        remaining_failing_count=remaining_failing_count,
    )


def x_build_adaptive_investigation__mutmut_31(  # noqa: PLR0913
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
        skipped_resources=skipped_resources,
        node_pressure_context=node_pressure_context,
        has_more_failing=has_more_failing,
        remaining_failing_count=remaining_failing_count,
    )


def x_build_adaptive_investigation__mutmut_32(  # noqa: PLR0913
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
        node_pressure_context=node_pressure_context,
        has_more_failing=has_more_failing,
        remaining_failing_count=remaining_failing_count,
    )


def x_build_adaptive_investigation__mutmut_33(  # noqa: PLR0913
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
        has_more_failing=has_more_failing,
        remaining_failing_count=remaining_failing_count,
    )


def x_build_adaptive_investigation__mutmut_34(  # noqa: PLR0913
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
        remaining_failing_count=remaining_failing_count,
    )


def x_build_adaptive_investigation__mutmut_35(  # noqa: PLR0913
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
        )

mutants_x_build_adaptive_investigation__mutmut['_mutmut_orig'] = x_build_adaptive_investigation__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_1'] = x_build_adaptive_investigation__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_2'] = x_build_adaptive_investigation__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_3'] = x_build_adaptive_investigation__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_4'] = x_build_adaptive_investigation__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_5'] = x_build_adaptive_investigation__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_6'] = x_build_adaptive_investigation__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_7'] = x_build_adaptive_investigation__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_8'] = x_build_adaptive_investigation__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_9'] = x_build_adaptive_investigation__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_10'] = x_build_adaptive_investigation__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_11'] = x_build_adaptive_investigation__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_12'] = x_build_adaptive_investigation__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_13'] = x_build_adaptive_investigation__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_14'] = x_build_adaptive_investigation__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_15'] = x_build_adaptive_investigation__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_16'] = x_build_adaptive_investigation__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_17'] = x_build_adaptive_investigation__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_18'] = x_build_adaptive_investigation__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_19'] = x_build_adaptive_investigation__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_20'] = x_build_adaptive_investigation__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_21'] = x_build_adaptive_investigation__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_22'] = x_build_adaptive_investigation__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_23'] = x_build_adaptive_investigation__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_24'] = x_build_adaptive_investigation__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_25'] = x_build_adaptive_investigation__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_26'] = x_build_adaptive_investigation__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_27'] = x_build_adaptive_investigation__mutmut_27 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_28'] = x_build_adaptive_investigation__mutmut_28 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_29'] = x_build_adaptive_investigation__mutmut_29 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_30'] = x_build_adaptive_investigation__mutmut_30 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_31'] = x_build_adaptive_investigation__mutmut_31 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_32'] = x_build_adaptive_investigation__mutmut_32 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_33'] = x_build_adaptive_investigation__mutmut_33 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_34'] = x_build_adaptive_investigation__mutmut_34 # type: ignore # mutmut generated
mutants_x_build_adaptive_investigation__mutmut['x_build_adaptive_investigation__mutmut_35'] = x_build_adaptive_investigation__mutmut_35 # type: ignore # mutmut generated
mutants_x__build_candidate__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_candidate__mutmut)
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


def x__build_candidate__mutmut_orig(investigation: ResourceInvestigation) -> RootCauseCandidate:
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


def x__build_candidate__mutmut_1(investigation: ResourceInvestigation) -> RootCauseCandidate:
    evidence = None
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


def x__build_candidate__mutmut_2(investigation: ResourceInvestigation) -> RootCauseCandidate:
    evidence = list(investigation.events) - list(investigation.logs)
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


def x__build_candidate__mutmut_3(investigation: ResourceInvestigation) -> RootCauseCandidate:
    evidence = list(None) + list(investigation.logs)
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


def x__build_candidate__mutmut_4(investigation: ResourceInvestigation) -> RootCauseCandidate:
    evidence = list(investigation.events) + list(None)
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


def x__build_candidate__mutmut_5(investigation: ResourceInvestigation) -> RootCauseCandidate:
    evidence = list(investigation.events) + list(investigation.logs)
    if investigation.last_termination_reason:
        evidence.append(None)

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


def x__build_candidate__mutmut_6(investigation: ResourceInvestigation) -> RootCauseCandidate:
    evidence = list(investigation.events) + list(investigation.logs)
    if investigation.last_termination_reason:
        evidence.append(f"Last termination reason: {investigation.last_termination_reason}")

    text = None
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


def x__build_candidate__mutmut_7(investigation: ResourceInvestigation) -> RootCauseCandidate:
    evidence = list(investigation.events) + list(investigation.logs)
    if investigation.last_termination_reason:
        evidence.append(f"Last termination reason: {investigation.last_termination_reason}")

    text = " ".join(None)
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


def x__build_candidate__mutmut_8(investigation: ResourceInvestigation) -> RootCauseCandidate:
    evidence = list(investigation.events) + list(investigation.logs)
    if investigation.last_termination_reason:
        evidence.append(f"Last termination reason: {investigation.last_termination_reason}")

    text = "XX XX".join([investigation.resource.reason, *evidence])
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


def x__build_candidate__mutmut_9(investigation: ResourceInvestigation) -> RootCauseCandidate:
    evidence = list(investigation.events) + list(investigation.logs)
    if investigation.last_termination_reason:
        evidence.append(f"Last termination reason: {investigation.last_termination_reason}")

    text = " ".join([investigation.resource.reason, *evidence])
    category = None
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


def x__build_candidate__mutmut_10(investigation: ResourceInvestigation) -> RootCauseCandidate:
    evidence = list(investigation.events) + list(investigation.logs)
    if investigation.last_termination_reason:
        evidence.append(f"Last termination reason: {investigation.last_termination_reason}")

    text = " ".join([investigation.resource.reason, *evidence])
    category = classify_incident_cause(None)
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


def x__build_candidate__mutmut_11(investigation: ResourceInvestigation) -> RootCauseCandidate:
    evidence = list(investigation.events) + list(investigation.logs)
    if investigation.last_termination_reason:
        evidence.append(f"Last termination reason: {investigation.last_termination_reason}")

    text = " ".join([investigation.resource.reason, *evidence])
    category = classify_incident_cause(text)
    confidence = None

    return RootCauseCandidate(
        description=f"{investigation.resource.name}: {investigation.resource.reason}",
        category=category,
        confidence=confidence,
        evidence=evidence,
        involved_objects=[investigation.resource.name],
    )


def x__build_candidate__mutmut_12(investigation: ResourceInvestigation) -> RootCauseCandidate:
    evidence = list(investigation.events) + list(investigation.logs)
    if investigation.last_termination_reason:
        evidence.append(f"Last termination reason: {investigation.last_termination_reason}")

    text = " ".join([investigation.resource.reason, *evidence])
    category = classify_incident_cause(text)
    confidence = (
        _RESOLVED_CONFIDENCE if category == IncidentCauseCategory.UNKNOWN else _UNKNOWN_CONFIDENCE
    )

    return RootCauseCandidate(
        description=f"{investigation.resource.name}: {investigation.resource.reason}",
        category=category,
        confidence=confidence,
        evidence=evidence,
        involved_objects=[investigation.resource.name],
    )


def x__build_candidate__mutmut_13(investigation: ResourceInvestigation) -> RootCauseCandidate:
    evidence = list(investigation.events) + list(investigation.logs)
    if investigation.last_termination_reason:
        evidence.append(f"Last termination reason: {investigation.last_termination_reason}")

    text = " ".join([investigation.resource.reason, *evidence])
    category = classify_incident_cause(text)
    confidence = (
        _RESOLVED_CONFIDENCE if category != IncidentCauseCategory.UNKNOWN else _UNKNOWN_CONFIDENCE
    )

    return RootCauseCandidate(
        description=None,
        category=category,
        confidence=confidence,
        evidence=evidence,
        involved_objects=[investigation.resource.name],
    )


def x__build_candidate__mutmut_14(investigation: ResourceInvestigation) -> RootCauseCandidate:
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
        category=None,
        confidence=confidence,
        evidence=evidence,
        involved_objects=[investigation.resource.name],
    )


def x__build_candidate__mutmut_15(investigation: ResourceInvestigation) -> RootCauseCandidate:
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
        confidence=None,
        evidence=evidence,
        involved_objects=[investigation.resource.name],
    )


def x__build_candidate__mutmut_16(investigation: ResourceInvestigation) -> RootCauseCandidate:
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
        evidence=None,
        involved_objects=[investigation.resource.name],
    )


def x__build_candidate__mutmut_17(investigation: ResourceInvestigation) -> RootCauseCandidate:
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
        involved_objects=None,
    )


def x__build_candidate__mutmut_18(investigation: ResourceInvestigation) -> RootCauseCandidate:
    evidence = list(investigation.events) + list(investigation.logs)
    if investigation.last_termination_reason:
        evidence.append(f"Last termination reason: {investigation.last_termination_reason}")

    text = " ".join([investigation.resource.reason, *evidence])
    category = classify_incident_cause(text)
    confidence = (
        _RESOLVED_CONFIDENCE if category != IncidentCauseCategory.UNKNOWN else _UNKNOWN_CONFIDENCE
    )

    return RootCauseCandidate(
        category=category,
        confidence=confidence,
        evidence=evidence,
        involved_objects=[investigation.resource.name],
    )


def x__build_candidate__mutmut_19(investigation: ResourceInvestigation) -> RootCauseCandidate:
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
        confidence=confidence,
        evidence=evidence,
        involved_objects=[investigation.resource.name],
    )


def x__build_candidate__mutmut_20(investigation: ResourceInvestigation) -> RootCauseCandidate:
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
        evidence=evidence,
        involved_objects=[investigation.resource.name],
    )


def x__build_candidate__mutmut_21(investigation: ResourceInvestigation) -> RootCauseCandidate:
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
        involved_objects=[investigation.resource.name],
    )


def x__build_candidate__mutmut_22(investigation: ResourceInvestigation) -> RootCauseCandidate:
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
        )

mutants_x__build_candidate__mutmut['_mutmut_orig'] = x__build_candidate__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_candidate__mutmut['x__build_candidate__mutmut_1'] = x__build_candidate__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_candidate__mutmut['x__build_candidate__mutmut_2'] = x__build_candidate__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_candidate__mutmut['x__build_candidate__mutmut_3'] = x__build_candidate__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_candidate__mutmut['x__build_candidate__mutmut_4'] = x__build_candidate__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_candidate__mutmut['x__build_candidate__mutmut_5'] = x__build_candidate__mutmut_5 # type: ignore # mutmut generated
mutants_x__build_candidate__mutmut['x__build_candidate__mutmut_6'] = x__build_candidate__mutmut_6 # type: ignore # mutmut generated
mutants_x__build_candidate__mutmut['x__build_candidate__mutmut_7'] = x__build_candidate__mutmut_7 # type: ignore # mutmut generated
mutants_x__build_candidate__mutmut['x__build_candidate__mutmut_8'] = x__build_candidate__mutmut_8 # type: ignore # mutmut generated
mutants_x__build_candidate__mutmut['x__build_candidate__mutmut_9'] = x__build_candidate__mutmut_9 # type: ignore # mutmut generated
mutants_x__build_candidate__mutmut['x__build_candidate__mutmut_10'] = x__build_candidate__mutmut_10 # type: ignore # mutmut generated
mutants_x__build_candidate__mutmut['x__build_candidate__mutmut_11'] = x__build_candidate__mutmut_11 # type: ignore # mutmut generated
mutants_x__build_candidate__mutmut['x__build_candidate__mutmut_12'] = x__build_candidate__mutmut_12 # type: ignore # mutmut generated
mutants_x__build_candidate__mutmut['x__build_candidate__mutmut_13'] = x__build_candidate__mutmut_13 # type: ignore # mutmut generated
mutants_x__build_candidate__mutmut['x__build_candidate__mutmut_14'] = x__build_candidate__mutmut_14 # type: ignore # mutmut generated
mutants_x__build_candidate__mutmut['x__build_candidate__mutmut_15'] = x__build_candidate__mutmut_15 # type: ignore # mutmut generated
mutants_x__build_candidate__mutmut['x__build_candidate__mutmut_16'] = x__build_candidate__mutmut_16 # type: ignore # mutmut generated
mutants_x__build_candidate__mutmut['x__build_candidate__mutmut_17'] = x__build_candidate__mutmut_17 # type: ignore # mutmut generated
mutants_x__build_candidate__mutmut['x__build_candidate__mutmut_18'] = x__build_candidate__mutmut_18 # type: ignore # mutmut generated
mutants_x__build_candidate__mutmut['x__build_candidate__mutmut_19'] = x__build_candidate__mutmut_19 # type: ignore # mutmut generated
mutants_x__build_candidate__mutmut['x__build_candidate__mutmut_20'] = x__build_candidate__mutmut_20 # type: ignore # mutmut generated
mutants_x__build_candidate__mutmut['x__build_candidate__mutmut_21'] = x__build_candidate__mutmut_21 # type: ignore # mutmut generated
mutants_x__build_candidate__mutmut['x__build_candidate__mutmut_22'] = x__build_candidate__mutmut_22 # type: ignore # mutmut generated
