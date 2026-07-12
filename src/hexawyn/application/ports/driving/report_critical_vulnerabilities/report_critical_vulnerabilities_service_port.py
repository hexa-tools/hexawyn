from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.report_critical_vulnerabilities.report_critical_vulnerabilities_command import (  # noqa: E501
    ReportCriticalVulnerabilitiesCommand,
)
from hexawyn.application.ports.driving.report_critical_vulnerabilities.report_critical_vulnerabilities_response import (  # noqa: E501
    ReportCriticalVulnerabilitiesResponse,
)


class ReportCriticalVulnerabilitiesServicePort(ABC):
    @abstractmethod
    def report(
        self, command: ReportCriticalVulnerabilitiesCommand
    ) -> ReportCriticalVulnerabilitiesResponse: ...
