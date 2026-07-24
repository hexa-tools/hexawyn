from hexawyn.application.ports.driven.namespace_waste_port import (
    NamespaceRawData,
    NamespaceWasteAnalysisPort,
)
from hexawyn.application.use_case.detect_over_provisioned_namespaces.command import (
    DetectOverProvisionedNamespacesCommand,
)
from hexawyn.application.use_case.detect_over_provisioned_namespaces.response import (
    DetectOverProvisionedNamespacesResponse,
)
from hexawyn.application.ports.driving.detect_over_provisioned_namespaces.detect_over_provisioned_namespaces_service_port import (
    DetectOverProvisionedNamespacesServicePort,
)
from hexawyn.domain.services.namespace_waste.namespace_over_provisioning_service import (
    NamespaceOverProvisioningService,
)


class DetectOverProvisionedNamespacesService(DetectOverProvisionedNamespacesServicePort):
    """Orchestrates K8s+Prometheus data fetch and domain-level waste analysis."""

    def __init__(self, waste_port: NamespaceWasteAnalysisPort) -> None:
        self._waste_port = waste_port
        self._domain_service = NamespaceOverProvisioningService()

    def detect_over_provisioned_namespaces(
        self, command: DetectOverProvisionedNamespacesCommand
    ) -> DetectOverProvisionedNamespacesResponse:
        raw_data = self._waste_port.get_all_namespace_waste_data(
            window_days=command.analysis_window_days
        )
        prometheus_available = _any_actual_usage_present(raw_data)
        report = self._domain_service.analyze(
            raw_data=raw_data,
            top_n=command.top_n,
            analysis_window_days=command.analysis_window_days,
        )
        return DetectOverProvisionedNamespacesResponse(
            report=report,
            prometheus_available=prometheus_available,
        )


def _any_actual_usage_present(
    raw_data: list[NamespaceRawData],
) -> bool:
    return any(
        item["cpu_actual_avg_cores"] is not None or item["memory_actual_avg_gb"] is not None
        for item in raw_data
    )
