from __future__ import annotations

from hexawyn.application.ports.driven.platform_reliability_port import (
    PlatformReliabilityPort,
)
from hexawyn.application.use_case.workloads.report_platform_reliability.command import (  # noqa: E501
    ReportPlatformReliabilityCommand,
)
from hexawyn.application.use_case.workloads.report_platform_reliability.response import (  # noqa: E501
    ReportPlatformReliabilityResponse,
)
from hexawyn.domain.services.platform_reliability.platform_reliability_service import (
    PlatformReliabilityService,
)


class ReportPlatformReliabilityUseCase:
    def __init__(self, reliability_port: PlatformReliabilityPort) -> None:
        self._port = reliability_port
        self._engine = PlatformReliabilityService()

    def execute(
        self, command: ReportPlatformReliabilityCommand
    ) -> ReportPlatformReliabilityResponse:
        data = self._port.get_reliability_data(command.period)
        result = self._engine.generate(data, period=command.period)
        return ReportPlatformReliabilityResponse(result=result)
