from abc import ABC, abstractmethod

from hexawyn.application.use_case.security.report_critical_vulnerabilities.command import (  # noqa: E501
    ReportCriticalVulnerabilitiesCommand,
)
from hexawyn.application.use_case.security.report_critical_vulnerabilities.response import (  # noqa: E501
    ReportCriticalVulnerabilitiesResponse,
)


class ReportCriticalVulnerabilitiesServicePort(ABC):
    @abstractmethod
    def report(
        self, command: ReportCriticalVulnerabilitiesCommand
    ) -> ReportCriticalVulnerabilitiesResponse: ...
