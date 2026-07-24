from hexawyn.application.ports.driven.namespace_waste_port import (
    NamespaceWasteAnalysisPort,
)
from hexawyn.application.use_case.detect_over_provisioned_namespaces.command import (
    DetectOverProvisionedNamespacesCommand,
)
from hexawyn.application.use_case.detect_over_provisioned_namespaces.response import (
    DetectOverProvisionedNamespacesResponse,
)
from hexawyn.domain.services.namespace_waste.namespace_over_provisioning_service import (
    NamespaceOverProvisioningService,
)


from typing import Any


def _any_actual_usage_present(raw_data: list[dict[str, Any]]) -> bool:
    return any(
        (rd.get("cpu_actual_avg_cores", 0) or 0) > 0
        or (rd.get("memory_actual_avg_gb", 0) or 0) > 0
        for rd in raw_data
    )


class DetectOverProvisionedNamespacesUseCase:
    def __init__(self, waste_port: NamespaceWasteAnalysisPort) -> None:
        self._waste_port = waste_port
        self._domain = NamespaceOverProvisioningService()

    def execute(
        self, command: DetectOverProvisionedNamespacesCommand
    ) -> DetectOverProvisionedNamespacesResponse:
        raw_data = self._waste_port.get_all_namespace_waste_data(
            window_days=command.analysis_window_days
        )
        prometheus_available = _any_actual_usage_present(raw_data)  # type: ignore[arg-type]
        report = self._domain.analyze(
            raw_data=raw_data,
            top_n=command.top_n,
            analysis_window_days=command.analysis_window_days,
        )
        return DetectOverProvisionedNamespacesResponse(
            report=report,
            prometheus_available=prometheus_available,
        )
