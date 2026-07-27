from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.workloads.report_platform_reliability.command import (  # noqa: E501
    ReportPlatformReliabilityCommand,
)
from hexawyn.application.use_case.workloads.report_platform_reliability.response import (  # noqa: E501
    ReportPlatformReliabilityResponse,
)


class ReportPlatformReliabilityServicePort(ABC):
    @abstractmethod
    def report(
        self, command: ReportPlatformReliabilityCommand
    ) -> ReportPlatformReliabilityResponse: ...
