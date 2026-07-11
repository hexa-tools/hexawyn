from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.report_platform_reliability.report_platform_reliability_command import (  # noqa: E501
    ReportPlatformReliabilityCommand,
)
from hexawyn.application.ports.driving.report_platform_reliability.report_platform_reliability_response import (  # noqa: E501
    ReportPlatformReliabilityResponse,
)


class ReportPlatformReliabilityServicePort(ABC):
    @abstractmethod
    def report(
        self, command: ReportPlatformReliabilityCommand
    ) -> ReportPlatformReliabilityResponse: ...
