from __future__ import annotations

from hexawyn.application.ports.driven.rightsizing_port import RightsizingPort, WorkloadRawData
from hexawyn.application.use_case.estimate_rightsizing_savings.command import (
    EstimateRightsizingSavingsCommand,
)
from hexawyn.application.use_case.estimate_rightsizing_savings.response import (
    EstimateRightsizingSavingsResponse,
)
from hexawyn.application.ports.driving.estimate_rightsizing_savings.estimate_rightsizing_savings_service_port import (
    EstimateRightsizingSavingsServicePort,
)
from hexawyn.domain.services.rightsizing.rightsizing_analysis_service import (
    RightsizingAnalysisService,
)


class EstimateRightsizingSavingsService(EstimateRightsizingSavingsServicePort):
    def __init__(self, rightsizing_port: RightsizingPort) -> None:
        self._port = rightsizing_port
        self._domain_service = RightsizingAnalysisService()

    def estimate_rightsizing_savings(
        self,
        command: EstimateRightsizingSavingsCommand,
    ) -> EstimateRightsizingSavingsResponse:
        raw_data = self._port.get_workload_rightsizing_data()
        metrics_available = _any_actual_present(raw_data)
        report = self._domain_service.analyze(
            raw_data=[dict(item) for item in raw_data],
            top_n=command.top_n,
        )
        return EstimateRightsizingSavingsResponse(
            report=report,
            metrics_server_available=metrics_available,
        )


def _any_actual_present(raw_data: list[WorkloadRawData]) -> bool:
    return any(
        item["cpu_actual_cores"] is not None or item["memory_actual_mi"] is not None
        for item in raw_data
    )
