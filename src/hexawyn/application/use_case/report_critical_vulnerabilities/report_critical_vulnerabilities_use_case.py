from __future__ import annotations

from hexawyn.application.ports.driving.report_critical_vulnerabilities.report_critical_vulnerabilities_command import (  # noqa: E501
    ReportCriticalVulnerabilitiesCommand,
)
from hexawyn.application.ports.driving.report_critical_vulnerabilities.report_critical_vulnerabilities_response import (  # noqa: E501
    ReportCriticalVulnerabilitiesResponse,
)
from hexawyn.application.ports.driving.report_critical_vulnerabilities.report_critical_vulnerabilities_service_port import (  # noqa: E501
    ReportCriticalVulnerabilitiesServicePort,
)


class ReportCriticalVulnerabilitiesUseCase:
    def __init__(self, service: ReportCriticalVulnerabilitiesServicePort) -> None:
        self._service = service

    def execute(
        self, command: ReportCriticalVulnerabilitiesCommand
    ) -> ReportCriticalVulnerabilitiesResponse:
        return self._service.report(command)
