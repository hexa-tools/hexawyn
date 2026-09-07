# mypy: ignore-errors
from __future__ import annotations

from hexawyn.application.ports.driven.adaptive_investigation_port import AdaptiveInvestigationPort
from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.use_case.troubleshooting.adaptive_namespace_investigation.command import (
    AdaptiveNamespaceInvestigationCommand,
)
from hexawyn.application.use_case.troubleshooting.adaptive_namespace_investigation.response import (
    AdaptiveNamespaceInvestigationResponse,
    ResourceInvestigationDict,
    RootCauseCandidateDict,
)
from hexawyn.application.use_case.troubleshooting.conservative_namespace_overview.command import (
    ConservativeNamespaceOverviewCommand,
)
from hexawyn.application.use_case.troubleshooting.conservative_namespace_overview.response import (
    ConservativeNamespaceOverviewResponse,
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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut: MutantDict = {}  # type: ignore


class AdaptiveNamespaceInvestigationUseCase:
    @_mutmut_mutated(mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁ__init____mutmut)
    def __init__(
        self,
        overview_service: ConservativeNamespaceOverviewServicePort,  # noqa: F821  # type: ignore
        k8s_port: K8sPort,
        investigation_port: AdaptiveInvestigationPort,
    ) -> None:
        self._overview_service = overview_service
        self._k8s_port = k8s_port
        self._investigation_port = investigation_port
    def xǁAdaptiveNamespaceInvestigationUseCaseǁ__init____mutmut_orig(
        self,
        overview_service: ConservativeNamespaceOverviewServicePort,  # noqa: F821  # type: ignore
        k8s_port: K8sPort,
        investigation_port: AdaptiveInvestigationPort,
    ) -> None:
        self._overview_service = overview_service
        self._k8s_port = k8s_port
        self._investigation_port = investigation_port
    def xǁAdaptiveNamespaceInvestigationUseCaseǁ__init____mutmut_1(
        self,
        overview_service: ConservativeNamespaceOverviewServicePort,  # noqa: F821  # type: ignore
        k8s_port: K8sPort,
        investigation_port: AdaptiveInvestigationPort,
    ) -> None:
        self._overview_service = None
        self._k8s_port = k8s_port
        self._investigation_port = investigation_port
    def xǁAdaptiveNamespaceInvestigationUseCaseǁ__init____mutmut_2(
        self,
        overview_service: ConservativeNamespaceOverviewServicePort,  # noqa: F821  # type: ignore
        k8s_port: K8sPort,
        investigation_port: AdaptiveInvestigationPort,
    ) -> None:
        self._overview_service = overview_service
        self._k8s_port = None
        self._investigation_port = investigation_port
    def xǁAdaptiveNamespaceInvestigationUseCaseǁ__init____mutmut_3(
        self,
        overview_service: ConservativeNamespaceOverviewServicePort,  # noqa: F821  # type: ignore
        k8s_port: K8sPort,
        investigation_port: AdaptiveInvestigationPort,
    ) -> None:
        self._overview_service = overview_service
        self._k8s_port = k8s_port
        self._investigation_port = None

    @_mutmut_mutated(mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut)
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_orig(
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_1(
        self, command: AdaptiveNamespaceInvestigationCommand
    ) -> AdaptiveNamespaceInvestigationResponse:
        overview_response = None
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_2(
        self, command: AdaptiveNamespaceInvestigationCommand
    ) -> AdaptiveNamespaceInvestigationResponse:
        overview_response = self._overview_service.get_overview(
            None
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_3(
        self, command: AdaptiveNamespaceInvestigationCommand
    ) -> AdaptiveNamespaceInvestigationResponse:
        overview_response = self._overview_service.get_overview(
            ConservativeNamespaceOverviewCommand(namespace=None)
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_4(
        self, command: AdaptiveNamespaceInvestigationCommand
    ) -> AdaptiveNamespaceInvestigationResponse:
        overview_response = self._overview_service.get_overview(
            ConservativeNamespaceOverviewCommand(namespace=command.namespace)
        )
        overview = None
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_5(
        self, command: AdaptiveNamespaceInvestigationCommand
    ) -> AdaptiveNamespaceInvestigationResponse:
        overview_response = self._overview_service.get_overview(
            ConservativeNamespaceOverviewCommand(namespace=command.namespace)
        )
        overview = _to_overview_snapshot(None)
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_6(
        self, command: AdaptiveNamespaceInvestigationCommand
    ) -> AdaptiveNamespaceInvestigationResponse:
        overview_response = self._overview_service.get_overview(
            ConservativeNamespaceOverviewCommand(namespace=command.namespace)
        )
        overview = _to_overview_snapshot(overview_response)
        restart_counts = None

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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_7(
        self, command: AdaptiveNamespaceInvestigationCommand
    ) -> AdaptiveNamespaceInvestigationResponse:
        overview_response = self._overview_service.get_overview(
            ConservativeNamespaceOverviewCommand(namespace=command.namespace)
        )
        overview = _to_overview_snapshot(overview_response)
        restart_counts = self._restart_counts(None)

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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_8(
        self, command: AdaptiveNamespaceInvestigationCommand
    ) -> AdaptiveNamespaceInvestigationResponse:
        overview_response = self._overview_service.get_overview(
            ConservativeNamespaceOverviewCommand(namespace=command.namespace)
        )
        overview = _to_overview_snapshot(overview_response)
        restart_counts = self._restart_counts(command.namespace)

        ranked, has_more, remaining = None
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_9(
        self, command: AdaptiveNamespaceInvestigationCommand
    ) -> AdaptiveNamespaceInvestigationResponse:
        overview_response = self._overview_service.get_overview(
            ConservativeNamespaceOverviewCommand(namespace=command.namespace)
        )
        overview = _to_overview_snapshot(overview_response)
        restart_counts = self._restart_counts(command.namespace)

        ranked, has_more, remaining = select_top_critical(
            None, restart_counts, command.depth
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_10(
        self, command: AdaptiveNamespaceInvestigationCommand
    ) -> AdaptiveNamespaceInvestigationResponse:
        overview_response = self._overview_service.get_overview(
            ConservativeNamespaceOverviewCommand(namespace=command.namespace)
        )
        overview = _to_overview_snapshot(overview_response)
        restart_counts = self._restart_counts(command.namespace)

        ranked, has_more, remaining = select_top_critical(
            overview.unhealthy_resources, None, command.depth
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_11(
        self, command: AdaptiveNamespaceInvestigationCommand
    ) -> AdaptiveNamespaceInvestigationResponse:
        overview_response = self._overview_service.get_overview(
            ConservativeNamespaceOverviewCommand(namespace=command.namespace)
        )
        overview = _to_overview_snapshot(overview_response)
        restart_counts = self._restart_counts(command.namespace)

        ranked, has_more, remaining = select_top_critical(
            overview.unhealthy_resources, restart_counts, None
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_12(
        self, command: AdaptiveNamespaceInvestigationCommand
    ) -> AdaptiveNamespaceInvestigationResponse:
        overview_response = self._overview_service.get_overview(
            ConservativeNamespaceOverviewCommand(namespace=command.namespace)
        )
        overview = _to_overview_snapshot(overview_response)
        restart_counts = self._restart_counts(command.namespace)

        ranked, has_more, remaining = select_top_critical(
            restart_counts, command.depth
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_13(
        self, command: AdaptiveNamespaceInvestigationCommand
    ) -> AdaptiveNamespaceInvestigationResponse:
        overview_response = self._overview_service.get_overview(
            ConservativeNamespaceOverviewCommand(namespace=command.namespace)
        )
        overview = _to_overview_snapshot(overview_response)
        restart_counts = self._restart_counts(command.namespace)

        ranked, has_more, remaining = select_top_critical(
            overview.unhealthy_resources, command.depth
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_14(
        self, command: AdaptiveNamespaceInvestigationCommand
    ) -> AdaptiveNamespaceInvestigationResponse:
        overview_response = self._overview_service.get_overview(
            ConservativeNamespaceOverviewCommand(namespace=command.namespace)
        )
        overview = _to_overview_snapshot(overview_response)
        restart_counts = self._restart_counts(command.namespace)

        ranked, has_more, remaining = select_top_critical(
            overview.unhealthy_resources, restart_counts, )
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_15(
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
        node_pressure_context = None

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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_16(
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
        node_pressure_context = detect_node_pressure_context(None, ranked)

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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_17(
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
        node_pressure_context = detect_node_pressure_context(overview.unhealthy_resources, None)

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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_18(
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
        node_pressure_context = detect_node_pressure_context(ranked)

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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_19(
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
        node_pressure_context = detect_node_pressure_context(overview.unhealthy_resources, )

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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_20(
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

        investigated_resources: list[ResourceInvestigation] = None
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_21(
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
        skipped_resources: list[str] = None
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_22(
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
                raw = None
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_23(
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
                    None, resource.kind, resource.name
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_24(
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
                    command.namespace, None, resource.name
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_25(
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
                    command.namespace, resource.kind, None
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_26(
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
                    resource.kind, resource.name
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_27(
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
                    command.namespace, resource.name
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_28(
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
                    command.namespace, resource.kind, )
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_29(
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
                skipped_resources.append(None)
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_30(
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
                break
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_31(
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
                None
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_32(
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
                    resource=None,
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_33(
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
                    events=None,
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_34(
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
                    logs=None,
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_35(
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
                    last_termination_reason=None,
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_36(
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_37(
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_38(
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_39(
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_40(
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
                    events=raw["XXeventsXX"],
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_41(
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
                    events=raw["EVENTS"],
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_42(
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
                    logs=raw["XXlogsXX"],
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_43(
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
                    logs=raw["LOGS"],
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_44(
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
                    last_termination_reason=raw["XXlast_termination_reasonXX"],
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_45(
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
                    last_termination_reason=raw["LAST_TERMINATION_REASON"],
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

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_46(
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

        report = None
        return _to_response(report)

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_47(
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
            request=None,
            overview=overview,
            investigated_resources=investigated_resources,
            skipped_resources=skipped_resources,
            node_pressure_context=node_pressure_context,
            has_more_failing=has_more,
            remaining_failing_count=remaining,
        )
        return _to_response(report)

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_48(
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
            overview=None,
            investigated_resources=investigated_resources,
            skipped_resources=skipped_resources,
            node_pressure_context=node_pressure_context,
            has_more_failing=has_more,
            remaining_failing_count=remaining,
        )
        return _to_response(report)

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_49(
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
            investigated_resources=None,
            skipped_resources=skipped_resources,
            node_pressure_context=node_pressure_context,
            has_more_failing=has_more,
            remaining_failing_count=remaining,
        )
        return _to_response(report)

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_50(
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
            skipped_resources=None,
            node_pressure_context=node_pressure_context,
            has_more_failing=has_more,
            remaining_failing_count=remaining,
        )
        return _to_response(report)

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_51(
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
            node_pressure_context=None,
            has_more_failing=has_more,
            remaining_failing_count=remaining,
        )
        return _to_response(report)

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_52(
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
            has_more_failing=None,
            remaining_failing_count=remaining,
        )
        return _to_response(report)

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_53(
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
            remaining_failing_count=None,
        )
        return _to_response(report)

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_54(
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
            overview=overview,
            investigated_resources=investigated_resources,
            skipped_resources=skipped_resources,
            node_pressure_context=node_pressure_context,
            has_more_failing=has_more,
            remaining_failing_count=remaining,
        )
        return _to_response(report)

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_55(
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
            investigated_resources=investigated_resources,
            skipped_resources=skipped_resources,
            node_pressure_context=node_pressure_context,
            has_more_failing=has_more,
            remaining_failing_count=remaining,
        )
        return _to_response(report)

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_56(
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
            skipped_resources=skipped_resources,
            node_pressure_context=node_pressure_context,
            has_more_failing=has_more,
            remaining_failing_count=remaining,
        )
        return _to_response(report)

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_57(
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
            node_pressure_context=node_pressure_context,
            has_more_failing=has_more,
            remaining_failing_count=remaining,
        )
        return _to_response(report)

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_58(
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
            has_more_failing=has_more,
            remaining_failing_count=remaining,
        )
        return _to_response(report)

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_59(
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
            remaining_failing_count=remaining,
        )
        return _to_response(report)

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_60(
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
            )
        return _to_response(report)

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_61(
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
            request=AdaptiveInvestigationRequest(namespace=None, depth=command.depth),
            overview=overview,
            investigated_resources=investigated_resources,
            skipped_resources=skipped_resources,
            node_pressure_context=node_pressure_context,
            has_more_failing=has_more,
            remaining_failing_count=remaining,
        )
        return _to_response(report)

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_62(
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
            request=AdaptiveInvestigationRequest(namespace=command.namespace, depth=None),
            overview=overview,
            investigated_resources=investigated_resources,
            skipped_resources=skipped_resources,
            node_pressure_context=node_pressure_context,
            has_more_failing=has_more,
            remaining_failing_count=remaining,
        )
        return _to_response(report)

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_63(
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
            request=AdaptiveInvestigationRequest(depth=command.depth),
            overview=overview,
            investigated_resources=investigated_resources,
            skipped_resources=skipped_resources,
            node_pressure_context=node_pressure_context,
            has_more_failing=has_more,
            remaining_failing_count=remaining,
        )
        return _to_response(report)

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_64(
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
            request=AdaptiveInvestigationRequest(namespace=command.namespace, ),
            overview=overview,
            investigated_resources=investigated_resources,
            skipped_resources=skipped_resources,
            node_pressure_context=node_pressure_context,
            has_more_failing=has_more,
            remaining_failing_count=remaining,
        )
        return _to_response(report)

    def xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_65(
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
        return _to_response(None)

    @_mutmut_mutated(mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut)
    def _restart_counts(self, namespace: str) -> dict[str, int]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        return {str(pod["name"]): int(pod["restarts"]) for pod in pods}

    def xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut_orig(self, namespace: str) -> dict[str, int]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        return {str(pod["name"]): int(pod["restarts"]) for pod in pods}

    def xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut_1(self, namespace: str) -> dict[str, int]:
        pods = None
        return {str(pod["name"]): int(pod["restarts"]) for pod in pods}

    def xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut_2(self, namespace: str) -> dict[str, int]:
        pods = self._k8s_port.list_pods(namespace=None)
        return {str(pod["name"]): int(pod["restarts"]) for pod in pods}

    def xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut_3(self, namespace: str) -> dict[str, int]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        return {str(None): int(pod["restarts"]) for pod in pods}

    def xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut_4(self, namespace: str) -> dict[str, int]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        return {str(pod["XXnameXX"]): int(pod["restarts"]) for pod in pods}

    def xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut_5(self, namespace: str) -> dict[str, int]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        return {str(pod["NAME"]): int(pod["restarts"]) for pod in pods}

    def xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut_6(self, namespace: str) -> dict[str, int]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        return {str(pod["name"]): int(None) for pod in pods}

    def xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut_7(self, namespace: str) -> dict[str, int]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        return {str(pod["name"]): int(pod["XXrestartsXX"]) for pod in pods}

    def xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut_8(self, namespace: str) -> dict[str, int]:
        pods = self._k8s_port.list_pods(namespace=namespace)
        return {str(pod["name"]): int(pod["RESTARTS"]) for pod in pods}

mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁ__init____mutmut['_mutmut_orig'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁ__init____mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁ__init____mutmut_1'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁ__init____mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁ__init____mutmut_2'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁ__init____mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁ__init____mutmut_3'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁ__init____mutmut_3 # type: ignore # mutmut generated

mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['_mutmut_orig'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_1'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_2'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_3'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_4'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_5'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_6'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_7'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_8'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_9'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_10'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_11'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_12'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_13'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_14'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_15'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_16'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_17'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_18'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_19'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_20'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_21'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_22'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_23'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_24'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_25'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_26'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_27'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_27 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_28'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_28 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_29'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_29 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_30'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_30 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_31'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_31 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_32'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_32 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_33'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_33 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_34'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_34 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_35'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_35 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_36'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_36 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_37'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_37 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_38'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_38 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_39'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_39 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_40'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_40 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_41'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_41 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_42'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_42 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_43'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_43 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_44'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_44 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_45'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_45 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_46'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_46 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_47'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_47 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_48'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_48 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_49'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_49 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_50'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_50 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_51'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_51 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_52'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_52 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_53'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_53 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_54'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_54 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_55'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_55 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_56'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_56 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_57'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_57 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_58'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_58 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_59'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_59 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_60'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_60 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_61'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_61 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_62'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_62 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_63'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_63 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_64'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_64 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_65'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁinvestigate__mutmut_65 # type: ignore # mutmut generated

mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut['_mutmut_orig'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut_1'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut_2'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut_3'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut_4'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut_5'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut_6'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut_7'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut['xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut_8'] = AdaptiveNamespaceInvestigationUseCase.xǁAdaptiveNamespaceInvestigationUseCaseǁ_restart_counts__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_overview_snapshot__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_overview_snapshot__mutmut)
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


def x__to_overview_snapshot__mutmut_orig(response: ConservativeNamespaceOverviewResponse) -> OverviewSnapshot:
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


def x__to_overview_snapshot__mutmut_1(response: ConservativeNamespaceOverviewResponse) -> OverviewSnapshot:
    return OverviewSnapshot(
        namespace=None,
        namespace_status=response.namespace_status,
        health_status=response.health_status,
        unhealthy_resources=[
            UnhealthyResourceRef(name=r["name"], kind=r["kind"], reason=r["reason"])
            for r in response.unhealthy_resources
        ],
        summary=response.summary,
    )


def x__to_overview_snapshot__mutmut_2(response: ConservativeNamespaceOverviewResponse) -> OverviewSnapshot:
    return OverviewSnapshot(
        namespace=response.namespace,
        namespace_status=None,
        health_status=response.health_status,
        unhealthy_resources=[
            UnhealthyResourceRef(name=r["name"], kind=r["kind"], reason=r["reason"])
            for r in response.unhealthy_resources
        ],
        summary=response.summary,
    )


def x__to_overview_snapshot__mutmut_3(response: ConservativeNamespaceOverviewResponse) -> OverviewSnapshot:
    return OverviewSnapshot(
        namespace=response.namespace,
        namespace_status=response.namespace_status,
        health_status=None,
        unhealthy_resources=[
            UnhealthyResourceRef(name=r["name"], kind=r["kind"], reason=r["reason"])
            for r in response.unhealthy_resources
        ],
        summary=response.summary,
    )


def x__to_overview_snapshot__mutmut_4(response: ConservativeNamespaceOverviewResponse) -> OverviewSnapshot:
    return OverviewSnapshot(
        namespace=response.namespace,
        namespace_status=response.namespace_status,
        health_status=response.health_status,
        unhealthy_resources=None,
        summary=response.summary,
    )


def x__to_overview_snapshot__mutmut_5(response: ConservativeNamespaceOverviewResponse) -> OverviewSnapshot:
    return OverviewSnapshot(
        namespace=response.namespace,
        namespace_status=response.namespace_status,
        health_status=response.health_status,
        unhealthy_resources=[
            UnhealthyResourceRef(name=r["name"], kind=r["kind"], reason=r["reason"])
            for r in response.unhealthy_resources
        ],
        summary=None,
    )


def x__to_overview_snapshot__mutmut_6(response: ConservativeNamespaceOverviewResponse) -> OverviewSnapshot:
    return OverviewSnapshot(
        namespace_status=response.namespace_status,
        health_status=response.health_status,
        unhealthy_resources=[
            UnhealthyResourceRef(name=r["name"], kind=r["kind"], reason=r["reason"])
            for r in response.unhealthy_resources
        ],
        summary=response.summary,
    )


def x__to_overview_snapshot__mutmut_7(response: ConservativeNamespaceOverviewResponse) -> OverviewSnapshot:
    return OverviewSnapshot(
        namespace=response.namespace,
        health_status=response.health_status,
        unhealthy_resources=[
            UnhealthyResourceRef(name=r["name"], kind=r["kind"], reason=r["reason"])
            for r in response.unhealthy_resources
        ],
        summary=response.summary,
    )


def x__to_overview_snapshot__mutmut_8(response: ConservativeNamespaceOverviewResponse) -> OverviewSnapshot:
    return OverviewSnapshot(
        namespace=response.namespace,
        namespace_status=response.namespace_status,
        unhealthy_resources=[
            UnhealthyResourceRef(name=r["name"], kind=r["kind"], reason=r["reason"])
            for r in response.unhealthy_resources
        ],
        summary=response.summary,
    )


def x__to_overview_snapshot__mutmut_9(response: ConservativeNamespaceOverviewResponse) -> OverviewSnapshot:
    return OverviewSnapshot(
        namespace=response.namespace,
        namespace_status=response.namespace_status,
        health_status=response.health_status,
        summary=response.summary,
    )


def x__to_overview_snapshot__mutmut_10(response: ConservativeNamespaceOverviewResponse) -> OverviewSnapshot:
    return OverviewSnapshot(
        namespace=response.namespace,
        namespace_status=response.namespace_status,
        health_status=response.health_status,
        unhealthy_resources=[
            UnhealthyResourceRef(name=r["name"], kind=r["kind"], reason=r["reason"])
            for r in response.unhealthy_resources
        ],
        )


def x__to_overview_snapshot__mutmut_11(response: ConservativeNamespaceOverviewResponse) -> OverviewSnapshot:
    return OverviewSnapshot(
        namespace=response.namespace,
        namespace_status=response.namespace_status,
        health_status=response.health_status,
        unhealthy_resources=[
            UnhealthyResourceRef(name=None, kind=r["kind"], reason=r["reason"])
            for r in response.unhealthy_resources
        ],
        summary=response.summary,
    )


def x__to_overview_snapshot__mutmut_12(response: ConservativeNamespaceOverviewResponse) -> OverviewSnapshot:
    return OverviewSnapshot(
        namespace=response.namespace,
        namespace_status=response.namespace_status,
        health_status=response.health_status,
        unhealthy_resources=[
            UnhealthyResourceRef(name=r["name"], kind=None, reason=r["reason"])
            for r in response.unhealthy_resources
        ],
        summary=response.summary,
    )


def x__to_overview_snapshot__mutmut_13(response: ConservativeNamespaceOverviewResponse) -> OverviewSnapshot:
    return OverviewSnapshot(
        namespace=response.namespace,
        namespace_status=response.namespace_status,
        health_status=response.health_status,
        unhealthy_resources=[
            UnhealthyResourceRef(name=r["name"], kind=r["kind"], reason=None)
            for r in response.unhealthy_resources
        ],
        summary=response.summary,
    )


def x__to_overview_snapshot__mutmut_14(response: ConservativeNamespaceOverviewResponse) -> OverviewSnapshot:
    return OverviewSnapshot(
        namespace=response.namespace,
        namespace_status=response.namespace_status,
        health_status=response.health_status,
        unhealthy_resources=[
            UnhealthyResourceRef(kind=r["kind"], reason=r["reason"])
            for r in response.unhealthy_resources
        ],
        summary=response.summary,
    )


def x__to_overview_snapshot__mutmut_15(response: ConservativeNamespaceOverviewResponse) -> OverviewSnapshot:
    return OverviewSnapshot(
        namespace=response.namespace,
        namespace_status=response.namespace_status,
        health_status=response.health_status,
        unhealthy_resources=[
            UnhealthyResourceRef(name=r["name"], reason=r["reason"])
            for r in response.unhealthy_resources
        ],
        summary=response.summary,
    )


def x__to_overview_snapshot__mutmut_16(response: ConservativeNamespaceOverviewResponse) -> OverviewSnapshot:
    return OverviewSnapshot(
        namespace=response.namespace,
        namespace_status=response.namespace_status,
        health_status=response.health_status,
        unhealthy_resources=[
            UnhealthyResourceRef(name=r["name"], kind=r["kind"], )
            for r in response.unhealthy_resources
        ],
        summary=response.summary,
    )


def x__to_overview_snapshot__mutmut_17(response: ConservativeNamespaceOverviewResponse) -> OverviewSnapshot:
    return OverviewSnapshot(
        namespace=response.namespace,
        namespace_status=response.namespace_status,
        health_status=response.health_status,
        unhealthy_resources=[
            UnhealthyResourceRef(name=r["XXnameXX"], kind=r["kind"], reason=r["reason"])
            for r in response.unhealthy_resources
        ],
        summary=response.summary,
    )


def x__to_overview_snapshot__mutmut_18(response: ConservativeNamespaceOverviewResponse) -> OverviewSnapshot:
    return OverviewSnapshot(
        namespace=response.namespace,
        namespace_status=response.namespace_status,
        health_status=response.health_status,
        unhealthy_resources=[
            UnhealthyResourceRef(name=r["NAME"], kind=r["kind"], reason=r["reason"])
            for r in response.unhealthy_resources
        ],
        summary=response.summary,
    )


def x__to_overview_snapshot__mutmut_19(response: ConservativeNamespaceOverviewResponse) -> OverviewSnapshot:
    return OverviewSnapshot(
        namespace=response.namespace,
        namespace_status=response.namespace_status,
        health_status=response.health_status,
        unhealthy_resources=[
            UnhealthyResourceRef(name=r["name"], kind=r["XXkindXX"], reason=r["reason"])
            for r in response.unhealthy_resources
        ],
        summary=response.summary,
    )


def x__to_overview_snapshot__mutmut_20(response: ConservativeNamespaceOverviewResponse) -> OverviewSnapshot:
    return OverviewSnapshot(
        namespace=response.namespace,
        namespace_status=response.namespace_status,
        health_status=response.health_status,
        unhealthy_resources=[
            UnhealthyResourceRef(name=r["name"], kind=r["KIND"], reason=r["reason"])
            for r in response.unhealthy_resources
        ],
        summary=response.summary,
    )


def x__to_overview_snapshot__mutmut_21(response: ConservativeNamespaceOverviewResponse) -> OverviewSnapshot:
    return OverviewSnapshot(
        namespace=response.namespace,
        namespace_status=response.namespace_status,
        health_status=response.health_status,
        unhealthy_resources=[
            UnhealthyResourceRef(name=r["name"], kind=r["kind"], reason=r["XXreasonXX"])
            for r in response.unhealthy_resources
        ],
        summary=response.summary,
    )


def x__to_overview_snapshot__mutmut_22(response: ConservativeNamespaceOverviewResponse) -> OverviewSnapshot:
    return OverviewSnapshot(
        namespace=response.namespace,
        namespace_status=response.namespace_status,
        health_status=response.health_status,
        unhealthy_resources=[
            UnhealthyResourceRef(name=r["name"], kind=r["kind"], reason=r["REASON"])
            for r in response.unhealthy_resources
        ],
        summary=response.summary,
    )

mutants_x__to_overview_snapshot__mutmut['_mutmut_orig'] = x__to_overview_snapshot__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_overview_snapshot__mutmut['x__to_overview_snapshot__mutmut_1'] = x__to_overview_snapshot__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_overview_snapshot__mutmut['x__to_overview_snapshot__mutmut_2'] = x__to_overview_snapshot__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_overview_snapshot__mutmut['x__to_overview_snapshot__mutmut_3'] = x__to_overview_snapshot__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_overview_snapshot__mutmut['x__to_overview_snapshot__mutmut_4'] = x__to_overview_snapshot__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_overview_snapshot__mutmut['x__to_overview_snapshot__mutmut_5'] = x__to_overview_snapshot__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_overview_snapshot__mutmut['x__to_overview_snapshot__mutmut_6'] = x__to_overview_snapshot__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_overview_snapshot__mutmut['x__to_overview_snapshot__mutmut_7'] = x__to_overview_snapshot__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_overview_snapshot__mutmut['x__to_overview_snapshot__mutmut_8'] = x__to_overview_snapshot__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_overview_snapshot__mutmut['x__to_overview_snapshot__mutmut_9'] = x__to_overview_snapshot__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_overview_snapshot__mutmut['x__to_overview_snapshot__mutmut_10'] = x__to_overview_snapshot__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_overview_snapshot__mutmut['x__to_overview_snapshot__mutmut_11'] = x__to_overview_snapshot__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_overview_snapshot__mutmut['x__to_overview_snapshot__mutmut_12'] = x__to_overview_snapshot__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_overview_snapshot__mutmut['x__to_overview_snapshot__mutmut_13'] = x__to_overview_snapshot__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_overview_snapshot__mutmut['x__to_overview_snapshot__mutmut_14'] = x__to_overview_snapshot__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_overview_snapshot__mutmut['x__to_overview_snapshot__mutmut_15'] = x__to_overview_snapshot__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_overview_snapshot__mutmut['x__to_overview_snapshot__mutmut_16'] = x__to_overview_snapshot__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_overview_snapshot__mutmut['x__to_overview_snapshot__mutmut_17'] = x__to_overview_snapshot__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_overview_snapshot__mutmut['x__to_overview_snapshot__mutmut_18'] = x__to_overview_snapshot__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_overview_snapshot__mutmut['x__to_overview_snapshot__mutmut_19'] = x__to_overview_snapshot__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_overview_snapshot__mutmut['x__to_overview_snapshot__mutmut_20'] = x__to_overview_snapshot__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_overview_snapshot__mutmut['x__to_overview_snapshot__mutmut_21'] = x__to_overview_snapshot__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_overview_snapshot__mutmut['x__to_overview_snapshot__mutmut_22'] = x__to_overview_snapshot__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_response__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_response__mutmut)
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
        recommended_actions=report.recommended_actions,  # type: ignore
        skipped_resources=report.skipped_resources,
        node_pressure_context=report.node_pressure_context,  # type: ignore
        has_more_failing=report.has_more_failing,  # type: ignore
        remaining_failing_count=report.remaining_failing_count,
    )


def x__to_response__mutmut_orig(report: AdaptiveInvestigationReport) -> AdaptiveNamespaceInvestigationResponse:
    return AdaptiveNamespaceInvestigationResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        health_status=report.health_status,
        overview_summary=report.overview_summary,
        investigated_resources=[
            _to_investigation_dict(investigation) for investigation in report.investigated_resources
        ],
        root_cause_candidates=[_to_candidate_dict(c) for c in report.root_cause_candidates],
        recommended_actions=report.recommended_actions,  # type: ignore
        skipped_resources=report.skipped_resources,
        node_pressure_context=report.node_pressure_context,  # type: ignore
        has_more_failing=report.has_more_failing,  # type: ignore
        remaining_failing_count=report.remaining_failing_count,
    )


def x__to_response__mutmut_1(report: AdaptiveInvestigationReport) -> AdaptiveNamespaceInvestigationResponse:
    return AdaptiveNamespaceInvestigationResponse(
        namespace=None,
        namespace_status=report.namespace_status,
        health_status=report.health_status,
        overview_summary=report.overview_summary,
        investigated_resources=[
            _to_investigation_dict(investigation) for investigation in report.investigated_resources
        ],
        root_cause_candidates=[_to_candidate_dict(c) for c in report.root_cause_candidates],
        recommended_actions=report.recommended_actions,  # type: ignore
        skipped_resources=report.skipped_resources,
        node_pressure_context=report.node_pressure_context,  # type: ignore
        has_more_failing=report.has_more_failing,  # type: ignore
        remaining_failing_count=report.remaining_failing_count,
    )


def x__to_response__mutmut_2(report: AdaptiveInvestigationReport) -> AdaptiveNamespaceInvestigationResponse:
    return AdaptiveNamespaceInvestigationResponse(
        namespace=report.namespace,
        namespace_status=None,
        health_status=report.health_status,
        overview_summary=report.overview_summary,
        investigated_resources=[
            _to_investigation_dict(investigation) for investigation in report.investigated_resources
        ],
        root_cause_candidates=[_to_candidate_dict(c) for c in report.root_cause_candidates],
        recommended_actions=report.recommended_actions,  # type: ignore
        skipped_resources=report.skipped_resources,
        node_pressure_context=report.node_pressure_context,  # type: ignore
        has_more_failing=report.has_more_failing,  # type: ignore
        remaining_failing_count=report.remaining_failing_count,
    )


def x__to_response__mutmut_3(report: AdaptiveInvestigationReport) -> AdaptiveNamespaceInvestigationResponse:
    return AdaptiveNamespaceInvestigationResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        health_status=None,
        overview_summary=report.overview_summary,
        investigated_resources=[
            _to_investigation_dict(investigation) for investigation in report.investigated_resources
        ],
        root_cause_candidates=[_to_candidate_dict(c) for c in report.root_cause_candidates],
        recommended_actions=report.recommended_actions,  # type: ignore
        skipped_resources=report.skipped_resources,
        node_pressure_context=report.node_pressure_context,  # type: ignore
        has_more_failing=report.has_more_failing,  # type: ignore
        remaining_failing_count=report.remaining_failing_count,
    )


def x__to_response__mutmut_4(report: AdaptiveInvestigationReport) -> AdaptiveNamespaceInvestigationResponse:
    return AdaptiveNamespaceInvestigationResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        health_status=report.health_status,
        overview_summary=None,
        investigated_resources=[
            _to_investigation_dict(investigation) for investigation in report.investigated_resources
        ],
        root_cause_candidates=[_to_candidate_dict(c) for c in report.root_cause_candidates],
        recommended_actions=report.recommended_actions,  # type: ignore
        skipped_resources=report.skipped_resources,
        node_pressure_context=report.node_pressure_context,  # type: ignore
        has_more_failing=report.has_more_failing,  # type: ignore
        remaining_failing_count=report.remaining_failing_count,
    )


def x__to_response__mutmut_5(report: AdaptiveInvestigationReport) -> AdaptiveNamespaceInvestigationResponse:
    return AdaptiveNamespaceInvestigationResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        health_status=report.health_status,
        overview_summary=report.overview_summary,
        investigated_resources=None,
        root_cause_candidates=[_to_candidate_dict(c) for c in report.root_cause_candidates],
        recommended_actions=report.recommended_actions,  # type: ignore
        skipped_resources=report.skipped_resources,
        node_pressure_context=report.node_pressure_context,  # type: ignore
        has_more_failing=report.has_more_failing,  # type: ignore
        remaining_failing_count=report.remaining_failing_count,
    )


def x__to_response__mutmut_6(report: AdaptiveInvestigationReport) -> AdaptiveNamespaceInvestigationResponse:
    return AdaptiveNamespaceInvestigationResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        health_status=report.health_status,
        overview_summary=report.overview_summary,
        investigated_resources=[
            _to_investigation_dict(investigation) for investigation in report.investigated_resources
        ],
        root_cause_candidates=None,
        recommended_actions=report.recommended_actions,  # type: ignore
        skipped_resources=report.skipped_resources,
        node_pressure_context=report.node_pressure_context,  # type: ignore
        has_more_failing=report.has_more_failing,  # type: ignore
        remaining_failing_count=report.remaining_failing_count,
    )


def x__to_response__mutmut_7(report: AdaptiveInvestigationReport) -> AdaptiveNamespaceInvestigationResponse:
    return AdaptiveNamespaceInvestigationResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        health_status=report.health_status,
        overview_summary=report.overview_summary,
        investigated_resources=[
            _to_investigation_dict(investigation) for investigation in report.investigated_resources
        ],
        root_cause_candidates=[_to_candidate_dict(c) for c in report.root_cause_candidates],
        recommended_actions=None,  # type: ignore
        skipped_resources=report.skipped_resources,
        node_pressure_context=report.node_pressure_context,  # type: ignore
        has_more_failing=report.has_more_failing,  # type: ignore
        remaining_failing_count=report.remaining_failing_count,
    )


def x__to_response__mutmut_8(report: AdaptiveInvestigationReport) -> AdaptiveNamespaceInvestigationResponse:
    return AdaptiveNamespaceInvestigationResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        health_status=report.health_status,
        overview_summary=report.overview_summary,
        investigated_resources=[
            _to_investigation_dict(investigation) for investigation in report.investigated_resources
        ],
        root_cause_candidates=[_to_candidate_dict(c) for c in report.root_cause_candidates],
        recommended_actions=report.recommended_actions,  # type: ignore
        skipped_resources=None,
        node_pressure_context=report.node_pressure_context,  # type: ignore
        has_more_failing=report.has_more_failing,  # type: ignore
        remaining_failing_count=report.remaining_failing_count,
    )


def x__to_response__mutmut_9(report: AdaptiveInvestigationReport) -> AdaptiveNamespaceInvestigationResponse:
    return AdaptiveNamespaceInvestigationResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        health_status=report.health_status,
        overview_summary=report.overview_summary,
        investigated_resources=[
            _to_investigation_dict(investigation) for investigation in report.investigated_resources
        ],
        root_cause_candidates=[_to_candidate_dict(c) for c in report.root_cause_candidates],
        recommended_actions=report.recommended_actions,  # type: ignore
        skipped_resources=report.skipped_resources,
        node_pressure_context=None,  # type: ignore
        has_more_failing=report.has_more_failing,  # type: ignore
        remaining_failing_count=report.remaining_failing_count,
    )


def x__to_response__mutmut_10(report: AdaptiveInvestigationReport) -> AdaptiveNamespaceInvestigationResponse:
    return AdaptiveNamespaceInvestigationResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        health_status=report.health_status,
        overview_summary=report.overview_summary,
        investigated_resources=[
            _to_investigation_dict(investigation) for investigation in report.investigated_resources
        ],
        root_cause_candidates=[_to_candidate_dict(c) for c in report.root_cause_candidates],
        recommended_actions=report.recommended_actions,  # type: ignore
        skipped_resources=report.skipped_resources,
        node_pressure_context=report.node_pressure_context,  # type: ignore
        has_more_failing=None,  # type: ignore
        remaining_failing_count=report.remaining_failing_count,
    )


def x__to_response__mutmut_11(report: AdaptiveInvestigationReport) -> AdaptiveNamespaceInvestigationResponse:
    return AdaptiveNamespaceInvestigationResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        health_status=report.health_status,
        overview_summary=report.overview_summary,
        investigated_resources=[
            _to_investigation_dict(investigation) for investigation in report.investigated_resources
        ],
        root_cause_candidates=[_to_candidate_dict(c) for c in report.root_cause_candidates],
        recommended_actions=report.recommended_actions,  # type: ignore
        skipped_resources=report.skipped_resources,
        node_pressure_context=report.node_pressure_context,  # type: ignore
        has_more_failing=report.has_more_failing,  # type: ignore
        remaining_failing_count=None,
    )


def x__to_response__mutmut_12(report: AdaptiveInvestigationReport) -> AdaptiveNamespaceInvestigationResponse:
    return AdaptiveNamespaceInvestigationResponse(
        namespace_status=report.namespace_status,
        health_status=report.health_status,
        overview_summary=report.overview_summary,
        investigated_resources=[
            _to_investigation_dict(investigation) for investigation in report.investigated_resources
        ],
        root_cause_candidates=[_to_candidate_dict(c) for c in report.root_cause_candidates],
        recommended_actions=report.recommended_actions,  # type: ignore
        skipped_resources=report.skipped_resources,
        node_pressure_context=report.node_pressure_context,  # type: ignore
        has_more_failing=report.has_more_failing,  # type: ignore
        remaining_failing_count=report.remaining_failing_count,
    )


def x__to_response__mutmut_13(report: AdaptiveInvestigationReport) -> AdaptiveNamespaceInvestigationResponse:
    return AdaptiveNamespaceInvestigationResponse(
        namespace=report.namespace,
        health_status=report.health_status,
        overview_summary=report.overview_summary,
        investigated_resources=[
            _to_investigation_dict(investigation) for investigation in report.investigated_resources
        ],
        root_cause_candidates=[_to_candidate_dict(c) for c in report.root_cause_candidates],
        recommended_actions=report.recommended_actions,  # type: ignore
        skipped_resources=report.skipped_resources,
        node_pressure_context=report.node_pressure_context,  # type: ignore
        has_more_failing=report.has_more_failing,  # type: ignore
        remaining_failing_count=report.remaining_failing_count,
    )


def x__to_response__mutmut_14(report: AdaptiveInvestigationReport) -> AdaptiveNamespaceInvestigationResponse:
    return AdaptiveNamespaceInvestigationResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        overview_summary=report.overview_summary,
        investigated_resources=[
            _to_investigation_dict(investigation) for investigation in report.investigated_resources
        ],
        root_cause_candidates=[_to_candidate_dict(c) for c in report.root_cause_candidates],
        recommended_actions=report.recommended_actions,  # type: ignore
        skipped_resources=report.skipped_resources,
        node_pressure_context=report.node_pressure_context,  # type: ignore
        has_more_failing=report.has_more_failing,  # type: ignore
        remaining_failing_count=report.remaining_failing_count,
    )


def x__to_response__mutmut_15(report: AdaptiveInvestigationReport) -> AdaptiveNamespaceInvestigationResponse:
    return AdaptiveNamespaceInvestigationResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        health_status=report.health_status,
        investigated_resources=[
            _to_investigation_dict(investigation) for investigation in report.investigated_resources
        ],
        root_cause_candidates=[_to_candidate_dict(c) for c in report.root_cause_candidates],
        recommended_actions=report.recommended_actions,  # type: ignore
        skipped_resources=report.skipped_resources,
        node_pressure_context=report.node_pressure_context,  # type: ignore
        has_more_failing=report.has_more_failing,  # type: ignore
        remaining_failing_count=report.remaining_failing_count,
    )


def x__to_response__mutmut_16(report: AdaptiveInvestigationReport) -> AdaptiveNamespaceInvestigationResponse:
    return AdaptiveNamespaceInvestigationResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        health_status=report.health_status,
        overview_summary=report.overview_summary,
        root_cause_candidates=[_to_candidate_dict(c) for c in report.root_cause_candidates],
        recommended_actions=report.recommended_actions,  # type: ignore
        skipped_resources=report.skipped_resources,
        node_pressure_context=report.node_pressure_context,  # type: ignore
        has_more_failing=report.has_more_failing,  # type: ignore
        remaining_failing_count=report.remaining_failing_count,
    )


def x__to_response__mutmut_17(report: AdaptiveInvestigationReport) -> AdaptiveNamespaceInvestigationResponse:
    return AdaptiveNamespaceInvestigationResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        health_status=report.health_status,
        overview_summary=report.overview_summary,
        investigated_resources=[
            _to_investigation_dict(investigation) for investigation in report.investigated_resources
        ],
        recommended_actions=report.recommended_actions,  # type: ignore
        skipped_resources=report.skipped_resources,
        node_pressure_context=report.node_pressure_context,  # type: ignore
        has_more_failing=report.has_more_failing,  # type: ignore
        remaining_failing_count=report.remaining_failing_count,
    )


def x__to_response__mutmut_18(report: AdaptiveInvestigationReport) -> AdaptiveNamespaceInvestigationResponse:
    return AdaptiveNamespaceInvestigationResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        health_status=report.health_status,
        overview_summary=report.overview_summary,
        investigated_resources=[
            _to_investigation_dict(investigation) for investigation in report.investigated_resources
        ],
        root_cause_candidates=[_to_candidate_dict(c) for c in report.root_cause_candidates],
        skipped_resources=report.skipped_resources,
        node_pressure_context=report.node_pressure_context,  # type: ignore
        has_more_failing=report.has_more_failing,  # type: ignore
        remaining_failing_count=report.remaining_failing_count,
    )


def x__to_response__mutmut_19(report: AdaptiveInvestigationReport) -> AdaptiveNamespaceInvestigationResponse:
    return AdaptiveNamespaceInvestigationResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        health_status=report.health_status,
        overview_summary=report.overview_summary,
        investigated_resources=[
            _to_investigation_dict(investigation) for investigation in report.investigated_resources
        ],
        root_cause_candidates=[_to_candidate_dict(c) for c in report.root_cause_candidates],
        recommended_actions=report.recommended_actions,  # type: ignore
        node_pressure_context=report.node_pressure_context,  # type: ignore
        has_more_failing=report.has_more_failing,  # type: ignore
        remaining_failing_count=report.remaining_failing_count,
    )


def x__to_response__mutmut_20(report: AdaptiveInvestigationReport) -> AdaptiveNamespaceInvestigationResponse:
    return AdaptiveNamespaceInvestigationResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        health_status=report.health_status,
        overview_summary=report.overview_summary,
        investigated_resources=[
            _to_investigation_dict(investigation) for investigation in report.investigated_resources
        ],
        root_cause_candidates=[_to_candidate_dict(c) for c in report.root_cause_candidates],
        recommended_actions=report.recommended_actions,  # type: ignore
        skipped_resources=report.skipped_resources,
        has_more_failing=report.has_more_failing,  # type: ignore
        remaining_failing_count=report.remaining_failing_count,
    )


def x__to_response__mutmut_21(report: AdaptiveInvestigationReport) -> AdaptiveNamespaceInvestigationResponse:
    return AdaptiveNamespaceInvestigationResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        health_status=report.health_status,
        overview_summary=report.overview_summary,
        investigated_resources=[
            _to_investigation_dict(investigation) for investigation in report.investigated_resources
        ],
        root_cause_candidates=[_to_candidate_dict(c) for c in report.root_cause_candidates],
        recommended_actions=report.recommended_actions,  # type: ignore
        skipped_resources=report.skipped_resources,
        node_pressure_context=report.node_pressure_context,  # type: ignore
        remaining_failing_count=report.remaining_failing_count,
    )


def x__to_response__mutmut_22(report: AdaptiveInvestigationReport) -> AdaptiveNamespaceInvestigationResponse:
    return AdaptiveNamespaceInvestigationResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        health_status=report.health_status,
        overview_summary=report.overview_summary,
        investigated_resources=[
            _to_investigation_dict(investigation) for investigation in report.investigated_resources
        ],
        root_cause_candidates=[_to_candidate_dict(c) for c in report.root_cause_candidates],
        recommended_actions=report.recommended_actions,  # type: ignore
        skipped_resources=report.skipped_resources,
        node_pressure_context=report.node_pressure_context,  # type: ignore
        has_more_failing=report.has_more_failing,  # type: ignore
        )


def x__to_response__mutmut_23(report: AdaptiveInvestigationReport) -> AdaptiveNamespaceInvestigationResponse:
    return AdaptiveNamespaceInvestigationResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        health_status=report.health_status,
        overview_summary=report.overview_summary,
        investigated_resources=[
            _to_investigation_dict(None) for investigation in report.investigated_resources
        ],
        root_cause_candidates=[_to_candidate_dict(c) for c in report.root_cause_candidates],
        recommended_actions=report.recommended_actions,  # type: ignore
        skipped_resources=report.skipped_resources,
        node_pressure_context=report.node_pressure_context,  # type: ignore
        has_more_failing=report.has_more_failing,  # type: ignore
        remaining_failing_count=report.remaining_failing_count,
    )


def x__to_response__mutmut_24(report: AdaptiveInvestigationReport) -> AdaptiveNamespaceInvestigationResponse:
    return AdaptiveNamespaceInvestigationResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        health_status=report.health_status,
        overview_summary=report.overview_summary,
        investigated_resources=[
            _to_investigation_dict(investigation) for investigation in report.investigated_resources
        ],
        root_cause_candidates=[_to_candidate_dict(None) for c in report.root_cause_candidates],
        recommended_actions=report.recommended_actions,  # type: ignore
        skipped_resources=report.skipped_resources,
        node_pressure_context=report.node_pressure_context,  # type: ignore
        has_more_failing=report.has_more_failing,  # type: ignore
        remaining_failing_count=report.remaining_failing_count,
    )

mutants_x__to_response__mutmut['_mutmut_orig'] = x__to_response__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_1'] = x__to_response__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_2'] = x__to_response__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_3'] = x__to_response__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_4'] = x__to_response__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_5'] = x__to_response__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_6'] = x__to_response__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_7'] = x__to_response__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_8'] = x__to_response__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_9'] = x__to_response__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_10'] = x__to_response__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_11'] = x__to_response__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_12'] = x__to_response__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_13'] = x__to_response__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_14'] = x__to_response__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_15'] = x__to_response__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_16'] = x__to_response__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_17'] = x__to_response__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_18'] = x__to_response__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_19'] = x__to_response__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_20'] = x__to_response__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_21'] = x__to_response__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_22'] = x__to_response__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_23'] = x__to_response__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_response__mutmut['x__to_response__mutmut_24'] = x__to_response__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_investigation_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_investigation_dict__mutmut)
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


def x__to_investigation_dict__mutmut_orig(investigation: ResourceInvestigation) -> ResourceInvestigationDict:
    return ResourceInvestigationDict(
        name=investigation.resource.name,
        kind=investigation.resource.kind,
        reason=investigation.resource.reason,
        restart_count=investigation.resource.restart_count,
        events=investigation.events,
        logs=investigation.logs,
        last_termination_reason=investigation.last_termination_reason,
    )


def x__to_investigation_dict__mutmut_1(investigation: ResourceInvestigation) -> ResourceInvestigationDict:
    return ResourceInvestigationDict(
        name=None,
        kind=investigation.resource.kind,
        reason=investigation.resource.reason,
        restart_count=investigation.resource.restart_count,
        events=investigation.events,
        logs=investigation.logs,
        last_termination_reason=investigation.last_termination_reason,
    )


def x__to_investigation_dict__mutmut_2(investigation: ResourceInvestigation) -> ResourceInvestigationDict:
    return ResourceInvestigationDict(
        name=investigation.resource.name,
        kind=None,
        reason=investigation.resource.reason,
        restart_count=investigation.resource.restart_count,
        events=investigation.events,
        logs=investigation.logs,
        last_termination_reason=investigation.last_termination_reason,
    )


def x__to_investigation_dict__mutmut_3(investigation: ResourceInvestigation) -> ResourceInvestigationDict:
    return ResourceInvestigationDict(
        name=investigation.resource.name,
        kind=investigation.resource.kind,
        reason=None,
        restart_count=investigation.resource.restart_count,
        events=investigation.events,
        logs=investigation.logs,
        last_termination_reason=investigation.last_termination_reason,
    )


def x__to_investigation_dict__mutmut_4(investigation: ResourceInvestigation) -> ResourceInvestigationDict:
    return ResourceInvestigationDict(
        name=investigation.resource.name,
        kind=investigation.resource.kind,
        reason=investigation.resource.reason,
        restart_count=None,
        events=investigation.events,
        logs=investigation.logs,
        last_termination_reason=investigation.last_termination_reason,
    )


def x__to_investigation_dict__mutmut_5(investigation: ResourceInvestigation) -> ResourceInvestigationDict:
    return ResourceInvestigationDict(
        name=investigation.resource.name,
        kind=investigation.resource.kind,
        reason=investigation.resource.reason,
        restart_count=investigation.resource.restart_count,
        events=None,
        logs=investigation.logs,
        last_termination_reason=investigation.last_termination_reason,
    )


def x__to_investigation_dict__mutmut_6(investigation: ResourceInvestigation) -> ResourceInvestigationDict:
    return ResourceInvestigationDict(
        name=investigation.resource.name,
        kind=investigation.resource.kind,
        reason=investigation.resource.reason,
        restart_count=investigation.resource.restart_count,
        events=investigation.events,
        logs=None,
        last_termination_reason=investigation.last_termination_reason,
    )


def x__to_investigation_dict__mutmut_7(investigation: ResourceInvestigation) -> ResourceInvestigationDict:
    return ResourceInvestigationDict(
        name=investigation.resource.name,
        kind=investigation.resource.kind,
        reason=investigation.resource.reason,
        restart_count=investigation.resource.restart_count,
        events=investigation.events,
        logs=investigation.logs,
        last_termination_reason=None,
    )


def x__to_investigation_dict__mutmut_8(investigation: ResourceInvestigation) -> ResourceInvestigationDict:
    return ResourceInvestigationDict(
        kind=investigation.resource.kind,
        reason=investigation.resource.reason,
        restart_count=investigation.resource.restart_count,
        events=investigation.events,
        logs=investigation.logs,
        last_termination_reason=investigation.last_termination_reason,
    )


def x__to_investigation_dict__mutmut_9(investigation: ResourceInvestigation) -> ResourceInvestigationDict:
    return ResourceInvestigationDict(
        name=investigation.resource.name,
        reason=investigation.resource.reason,
        restart_count=investigation.resource.restart_count,
        events=investigation.events,
        logs=investigation.logs,
        last_termination_reason=investigation.last_termination_reason,
    )


def x__to_investigation_dict__mutmut_10(investigation: ResourceInvestigation) -> ResourceInvestigationDict:
    return ResourceInvestigationDict(
        name=investigation.resource.name,
        kind=investigation.resource.kind,
        restart_count=investigation.resource.restart_count,
        events=investigation.events,
        logs=investigation.logs,
        last_termination_reason=investigation.last_termination_reason,
    )


def x__to_investigation_dict__mutmut_11(investigation: ResourceInvestigation) -> ResourceInvestigationDict:
    return ResourceInvestigationDict(
        name=investigation.resource.name,
        kind=investigation.resource.kind,
        reason=investigation.resource.reason,
        events=investigation.events,
        logs=investigation.logs,
        last_termination_reason=investigation.last_termination_reason,
    )


def x__to_investigation_dict__mutmut_12(investigation: ResourceInvestigation) -> ResourceInvestigationDict:
    return ResourceInvestigationDict(
        name=investigation.resource.name,
        kind=investigation.resource.kind,
        reason=investigation.resource.reason,
        restart_count=investigation.resource.restart_count,
        logs=investigation.logs,
        last_termination_reason=investigation.last_termination_reason,
    )


def x__to_investigation_dict__mutmut_13(investigation: ResourceInvestigation) -> ResourceInvestigationDict:
    return ResourceInvestigationDict(
        name=investigation.resource.name,
        kind=investigation.resource.kind,
        reason=investigation.resource.reason,
        restart_count=investigation.resource.restart_count,
        events=investigation.events,
        last_termination_reason=investigation.last_termination_reason,
    )


def x__to_investigation_dict__mutmut_14(investigation: ResourceInvestigation) -> ResourceInvestigationDict:
    return ResourceInvestigationDict(
        name=investigation.resource.name,
        kind=investigation.resource.kind,
        reason=investigation.resource.reason,
        restart_count=investigation.resource.restart_count,
        events=investigation.events,
        logs=investigation.logs,
        )

mutants_x__to_investigation_dict__mutmut['_mutmut_orig'] = x__to_investigation_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_investigation_dict__mutmut['x__to_investigation_dict__mutmut_1'] = x__to_investigation_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_investigation_dict__mutmut['x__to_investigation_dict__mutmut_2'] = x__to_investigation_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_investigation_dict__mutmut['x__to_investigation_dict__mutmut_3'] = x__to_investigation_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_investigation_dict__mutmut['x__to_investigation_dict__mutmut_4'] = x__to_investigation_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_investigation_dict__mutmut['x__to_investigation_dict__mutmut_5'] = x__to_investigation_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_investigation_dict__mutmut['x__to_investigation_dict__mutmut_6'] = x__to_investigation_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_investigation_dict__mutmut['x__to_investigation_dict__mutmut_7'] = x__to_investigation_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_investigation_dict__mutmut['x__to_investigation_dict__mutmut_8'] = x__to_investigation_dict__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_investigation_dict__mutmut['x__to_investigation_dict__mutmut_9'] = x__to_investigation_dict__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_investigation_dict__mutmut['x__to_investigation_dict__mutmut_10'] = x__to_investigation_dict__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_investigation_dict__mutmut['x__to_investigation_dict__mutmut_11'] = x__to_investigation_dict__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_investigation_dict__mutmut['x__to_investigation_dict__mutmut_12'] = x__to_investigation_dict__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_investigation_dict__mutmut['x__to_investigation_dict__mutmut_13'] = x__to_investigation_dict__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_investigation_dict__mutmut['x__to_investigation_dict__mutmut_14'] = x__to_investigation_dict__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_candidate_dict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_candidate_dict__mutmut)
def _to_candidate_dict(candidate: RootCauseCandidate) -> RootCauseCandidateDict:
    return RootCauseCandidateDict(
        description=candidate.description,
        category=candidate.category.value,
        confidence=candidate.confidence,
        evidence=candidate.evidence,
        involved_objects=candidate.involved_objects,
    )


def x__to_candidate_dict__mutmut_orig(candidate: RootCauseCandidate) -> RootCauseCandidateDict:
    return RootCauseCandidateDict(
        description=candidate.description,
        category=candidate.category.value,
        confidence=candidate.confidence,
        evidence=candidate.evidence,
        involved_objects=candidate.involved_objects,
    )


def x__to_candidate_dict__mutmut_1(candidate: RootCauseCandidate) -> RootCauseCandidateDict:
    return RootCauseCandidateDict(
        description=None,
        category=candidate.category.value,
        confidence=candidate.confidence,
        evidence=candidate.evidence,
        involved_objects=candidate.involved_objects,
    )


def x__to_candidate_dict__mutmut_2(candidate: RootCauseCandidate) -> RootCauseCandidateDict:
    return RootCauseCandidateDict(
        description=candidate.description,
        category=None,
        confidence=candidate.confidence,
        evidence=candidate.evidence,
        involved_objects=candidate.involved_objects,
    )


def x__to_candidate_dict__mutmut_3(candidate: RootCauseCandidate) -> RootCauseCandidateDict:
    return RootCauseCandidateDict(
        description=candidate.description,
        category=candidate.category.value,
        confidence=None,
        evidence=candidate.evidence,
        involved_objects=candidate.involved_objects,
    )


def x__to_candidate_dict__mutmut_4(candidate: RootCauseCandidate) -> RootCauseCandidateDict:
    return RootCauseCandidateDict(
        description=candidate.description,
        category=candidate.category.value,
        confidence=candidate.confidence,
        evidence=None,
        involved_objects=candidate.involved_objects,
    )


def x__to_candidate_dict__mutmut_5(candidate: RootCauseCandidate) -> RootCauseCandidateDict:
    return RootCauseCandidateDict(
        description=candidate.description,
        category=candidate.category.value,
        confidence=candidate.confidence,
        evidence=candidate.evidence,
        involved_objects=None,
    )


def x__to_candidate_dict__mutmut_6(candidate: RootCauseCandidate) -> RootCauseCandidateDict:
    return RootCauseCandidateDict(
        category=candidate.category.value,
        confidence=candidate.confidence,
        evidence=candidate.evidence,
        involved_objects=candidate.involved_objects,
    )


def x__to_candidate_dict__mutmut_7(candidate: RootCauseCandidate) -> RootCauseCandidateDict:
    return RootCauseCandidateDict(
        description=candidate.description,
        confidence=candidate.confidence,
        evidence=candidate.evidence,
        involved_objects=candidate.involved_objects,
    )


def x__to_candidate_dict__mutmut_8(candidate: RootCauseCandidate) -> RootCauseCandidateDict:
    return RootCauseCandidateDict(
        description=candidate.description,
        category=candidate.category.value,
        evidence=candidate.evidence,
        involved_objects=candidate.involved_objects,
    )


def x__to_candidate_dict__mutmut_9(candidate: RootCauseCandidate) -> RootCauseCandidateDict:
    return RootCauseCandidateDict(
        description=candidate.description,
        category=candidate.category.value,
        confidence=candidate.confidence,
        involved_objects=candidate.involved_objects,
    )


def x__to_candidate_dict__mutmut_10(candidate: RootCauseCandidate) -> RootCauseCandidateDict:
    return RootCauseCandidateDict(
        description=candidate.description,
        category=candidate.category.value,
        confidence=candidate.confidence,
        evidence=candidate.evidence,
        )

mutants_x__to_candidate_dict__mutmut['_mutmut_orig'] = x__to_candidate_dict__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_candidate_dict__mutmut['x__to_candidate_dict__mutmut_1'] = x__to_candidate_dict__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_candidate_dict__mutmut['x__to_candidate_dict__mutmut_2'] = x__to_candidate_dict__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_candidate_dict__mutmut['x__to_candidate_dict__mutmut_3'] = x__to_candidate_dict__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_candidate_dict__mutmut['x__to_candidate_dict__mutmut_4'] = x__to_candidate_dict__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_candidate_dict__mutmut['x__to_candidate_dict__mutmut_5'] = x__to_candidate_dict__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_candidate_dict__mutmut['x__to_candidate_dict__mutmut_6'] = x__to_candidate_dict__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_candidate_dict__mutmut['x__to_candidate_dict__mutmut_7'] = x__to_candidate_dict__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_candidate_dict__mutmut['x__to_candidate_dict__mutmut_8'] = x__to_candidate_dict__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_candidate_dict__mutmut['x__to_candidate_dict__mutmut_9'] = x__to_candidate_dict__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_candidate_dict__mutmut['x__to_candidate_dict__mutmut_10'] = x__to_candidate_dict__mutmut_10 # type: ignore # mutmut generated
