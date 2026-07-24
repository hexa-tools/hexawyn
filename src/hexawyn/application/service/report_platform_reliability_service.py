from __future__ import annotations

from hexawyn.application.ports.driven.platform_reliability_port import (
    PlatformReliabilityPort,
)
from hexawyn.application.use_case.report_platform_reliability.command import (  # noqa: E501
    ReportPlatformReliabilityCommand,
)
from hexawyn.application.use_case.report_platform_reliability.response import (  # noqa: E501
    ReportPlatformReliabilityResponse,
)
from hexawyn.application.ports.driving.report_platform_reliability.report_platform_reliability_service_port import (  # noqa: E501
    ReportPlatformReliabilityServicePort,
)
from hexawyn.domain.services.platform_reliability.platform_reliability_service import (
    PlatformReliabilityService,
)


class ReportPlatformReliabilityService(ReportPlatformReliabilityServicePort):
    def __init__(self, reliability_port: PlatformReliabilityPort) -> None:
        self._port = reliability_port
        self._engine = PlatformReliabilityService()

    def report(
        self, command: ReportPlatformReliabilityCommand
    ) -> ReportPlatformReliabilityResponse:
        data = self._port.get_reliability_data(command.period)
        result = self._engine.generate(data, period=command.period)
        return ReportPlatformReliabilityResponse(result=result)
