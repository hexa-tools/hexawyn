from hexawyn.application.ports.driven.platform_reliability_port import PlatformReliabilityPort
from hexawyn.application.use_case.report_platform_reliability.command import (
    ReportPlatformReliabilityCommand,
)
from hexawyn.application.use_case.report_platform_reliability.response import (
    ReportPlatformReliabilityResponse,
)


class ReportPlatformReliabilityUseCase:
    def __init__(self, reliability_port: PlatformReliabilityPort) -> None:
        self._port = reliability_port

    def execute(
        self, command: ReportPlatformReliabilityCommand
    ) -> ReportPlatformReliabilityResponse:
        return ReportPlatformReliabilityResponse()
