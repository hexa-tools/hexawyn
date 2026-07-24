from __future__ import annotations

from hexawyn.application.ports.driven.adaptive_investigation_port import AdaptiveInvestigationPort
from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.use_case.adaptive_namespace_investigation.command import (
    AdaptiveNamespaceInvestigationCommand,
)
from hexawyn.application.use_case.adaptive_namespace_investigation.response import (
    AdaptiveNamespaceInvestigationResponse,
    ResourceInvestigationDict,
    RootCauseCandidateDict,
)
from hexawyn.application.ports.driving.adaptive_namespace_investigation.adaptive_namespace_investigation_service_port import (
    AdaptiveNamespaceInvestigationServicePort,
)
from hexawyn.application.use_case.conservative_namespace_overview.command import (
    ConservativeNamespaceOverviewCommand,
)
from hexawyn.application.use_case.conservative_namespace_overview.response import (
    ConservativeNamespaceOverviewResponse,
)
from hexawyn.application.ports.driving.conservative_namespace_overview.conservative_namespace_overview_service_port import (
    ConservativeNamespaceOverviewServicePort,
)
from hexawyn.domain.errors import ResourceNotFoundError
from hexawyn.domain.models.adaptive_namespace_investigation import (
    AdaptiveInvestigationReport,
    AdaptiveInvestigationRequest,
    OverviewSnapshot,
    ResourceInvestigation,
    UnhealthyResourceRef,
)
from hexawyn.domain.models.incident_triage import RootCauseCandidate
from hexawyn.domain.services.adaptive_namespace_investigation.criticality_ranking import (
    detect_node_pressure_context,
    select_top_critical,
)
from hexawyn.domain.services.adaptive_namespace_investigation.investigation_builder import (
    build_adaptive_investigation,
)


class AdaptiveNamespaceInvestigationService(AdaptiveNamespaceInvestigationServicePort):
    def __init__(
        self,
        overview_service: ConservativeNamespaceOverviewServicePort,
        k8s_port: K8sPort,
        investigation_port: AdaptiveInvestigationPort,
    ) -> None:
        self._overview_service = overview_service
        self._k8s_port = k8s_port
        self._investigation_port = investigation_port

    def investigate(
        self, command: AdaptiveNamespaceInvestigationCommand
    ) -> AdaptiveNamespaceInvestigationResponse:
        overview_response = self._overview_service.get_overview(
            ConservativeNamespaceOverviewCommand(namespace=command.namespace)
        )
        overview = _to_overview_snapshot(overview_response)
        restart_counts = self._restart_counts(command.namespace)

        ranked, has_more, remaining = select_top_critical(
            overview.unhealthy_resources, restart_counts, command.depth
        )
        node_pressure_context = detect_node_pressure_context(overview.unhealthy_resources, ranked)

        investigated_resources: list[ResourceInvestigation] = []
        skipped_resources: list[str] = []
        for resource in ranked:
            try:
                raw = self._investigation_port.investigate_resource(
                    command.namespace, resource.kind, resource.name
                )
            except ResourceNotFoundError:
                skipped_resources.append(resource.name)
                continue
            investigated_resources.append(
                ResourceInvestigation(
                    resource=resource,
                    events=raw["events"],
                    logs=raw["logs"],
                    last_termination_reason=raw["last_termination_reason"],
                )
            )

        report = build_adaptive_investigation(
            request=AdaptiveInvestigationRequest(namespace=command.namespace, depth=command.depth),
            overview=overview,
            investigated_resources=investigated_resources,
            skipped_resources=skipped_resources,
            node_pressure_context=node_pressure_context,
            has_more_failing=has_more,
            remaining_failing_count=remaining,
        )
        return _to_response(report)

    def _restart_counts(self, namespace: str) -> dict[str, int]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        return {str(pod["name"]): int(pod["restarts"]) for pod in pods}


def _to_overview_snapshot(response: ConservativeNamespaceOverviewResponse) -> OverviewSnapshot:
    return OverviewSnapshot(
        namespace=response.namespace,
        namespace_status=response.namespace_status,
        health_status=response.health_status,
        unhealthy_resources=[
            UnhealthyResourceRef(name=r["name"], kind=r["kind"], reason=r["reason"])
            for r in response.unhealthy_resources
        ],
        summary=response.summary,
    )


def _to_response(report: AdaptiveInvestigationReport) -> AdaptiveNamespaceInvestigationResponse:
    return AdaptiveNamespaceInvestigationResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        health_status=report.health_status,
        overview_summary=report.overview_summary,
        investigated_resources=[
            _to_investigation_dict(investigation) for investigation in report.investigated_resources
        ],
        root_cause_candidates=[_to_candidate_dict(c) for c in report.root_cause_candidates],
        recommended_actions=report.recommended_actions,
        skipped_resources=report.skipped_resources,
        node_pressure_context=report.node_pressure_context,
        has_more_failing=report.has_more_failing,
        remaining_failing_count=report.remaining_failing_count,
    )


def _to_investigation_dict(investigation: ResourceInvestigation) -> ResourceInvestigationDict:
    return ResourceInvestigationDict(
        name=investigation.resource.name,
        kind=investigation.resource.kind,
        reason=investigation.resource.reason,
        restart_count=investigation.resource.restart_count,
        events=investigation.events,
        logs=investigation.logs,
        last_termination_reason=investigation.last_termination_reason,
    )


def _to_candidate_dict(candidate: RootCauseCandidate) -> RootCauseCandidateDict:
    return RootCauseCandidateDict(
        description=candidate.description,
        category=candidate.category.value,
        confidence=candidate.confidence,
        evidence=candidate.evidence,
        involved_objects=candidate.involved_objects,
    )
