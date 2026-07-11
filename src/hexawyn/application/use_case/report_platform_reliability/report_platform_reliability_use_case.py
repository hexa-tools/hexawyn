from __future__ import annotations

from hexawyn.application.ports.driving.report_platform_reliability.report_platform_reliability_command import (  # noqa: E501
    ReportPlatformReliabilityCommand,
)
from hexawyn.application.ports.driving.report_platform_reliability.report_platform_reliability_response import (  # noqa: E501
    ReportPlatformReliabilityResponse,
)
from hexawyn.application.ports.driving.report_platform_reliability.report_platform_reliability_service_port import (  # noqa: E501
    ReportPlatformReliabilityServicePort,
)


class ReportPlatformReliabilityUseCase:
    def __init__(self, service: ReportPlatformReliabilityServicePort) -> None:
        self._service = service

    def execute(
        self, command: ReportPlatformReliabilityCommand
    ) -> ReportPlatformReliabilityResponse:
        return self._service.report(command)
