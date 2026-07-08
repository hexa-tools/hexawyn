from __future__ import annotations

from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.ports.driven.namespace_overview_port import NamespaceOverviewPort
from hexawyn.application.ports.driving.conservative_namespace_overview.conservative_namespace_overview_command import (
    ConservativeNamespaceOverviewCommand,
)
from hexawyn.application.ports.driving.conservative_namespace_overview.conservative_namespace_overview_response import (
    ConservativeNamespaceOverviewResponse,
    NamespaceCountsDict,
    UnhealthyResourceDict,
)
from hexawyn.application.ports.driving.conservative_namespace_overview.conservative_namespace_overview_service_port import (
    ConservativeNamespaceOverviewServicePort,
)
from hexawyn.domain.errors import ResourceNotFoundError
from hexawyn.domain.models.namespace_overview import (
    NamespaceOverviewReport,
    NamespaceOverviewRequest,
    UnhealthyResource,
)
from hexawyn.domain.services.namespace_overview.overview import build_namespace_overview


class ConservativeNamespaceOverviewService(ConservativeNamespaceOverviewServicePort):
    def __init__(self, port: NamespaceOverviewPort, k8s_port: K8sPort) -> None:
        self._port = port
        self._k8s_port = k8s_port

    def get_overview(
        self, command: ConservativeNamespaceOverviewCommand
    ) -> ConservativeNamespaceOverviewResponse:
        self._validate_namespace_exists(command.namespace)

        raw_data = self._port.get_namespace_overview_data(command.namespace)
        request = NamespaceOverviewRequest(
            namespace=command.namespace, max_tokens=command.max_tokens
        )
        report = build_namespace_overview(request, raw_data)
        return _to_response(report)

    def _validate_namespace_exists(self, namespace: str) -> None:
        namespaces = self._k8s_port.list_namespaces()
        if not any(ns["name"] == namespace for ns in namespaces):
            raise ResourceNotFoundError(
                f"Namespace {namespace!r} not found", context={"namespace": namespace}
            )


def _to_response(report: NamespaceOverviewReport) -> ConservativeNamespaceOverviewResponse:
    return ConservativeNamespaceOverviewResponse(
        namespace=report.namespace,
        namespace_status=report.namespace_status,
        counts=NamespaceCountsDict(
            pods_total=report.counts.pods_total,
            pods_running=report.counts.pods_running,
            pods_failed=report.counts.pods_failed,
            deployments_total=report.counts.deployments_total,
            deployments_ready=report.counts.deployments_ready,
            services_total=report.counts.services_total,
        ),
        health_status=report.health_status.value,
        root_cause=report.root_cause,
        unhealthy_resources=[
            _to_resource_dict(resource) for resource in report.unhealthy_resources
        ],
        warnings=report.warnings,
        has_more_unhealthy=report.has_more_unhealthy,
        remaining_unhealthy_count=report.remaining_unhealthy_count,
        estimated_tokens=report.estimated_tokens,
        is_empty=report.is_empty,
        summary=report.summary,
    )


def _to_resource_dict(resource: UnhealthyResource) -> UnhealthyResourceDict:
    return UnhealthyResourceDict(name=resource.name, kind=resource.kind, reason=resource.reason)
