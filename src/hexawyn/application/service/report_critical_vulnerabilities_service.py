from __future__ import annotations

from hexawyn.application.ports.driven.critical_cve_port import CriticalCvePort
from hexawyn.application.ports.driving.report_critical_vulnerabilities.report_critical_vulnerabilities_command import (  # noqa: E501
    ReportCriticalVulnerabilitiesCommand,
)
from hexawyn.application.ports.driving.report_critical_vulnerabilities.report_critical_vulnerabilities_response import (  # noqa: E501
    ReportCriticalVulnerabilitiesResponse,
)
from hexawyn.application.ports.driving.report_critical_vulnerabilities.report_critical_vulnerabilities_service_port import (  # noqa: E501
    ReportCriticalVulnerabilitiesServicePort,
)
from hexawyn.domain.services.critical_cve.critical_cve_service import (
    compute_critical_cve_report,
)


class ReportCriticalVulnerabilitiesService(ReportCriticalVulnerabilitiesServicePort):
    def __init__(self, cve_port: CriticalCvePort) -> None:
        self._port = cve_port

    def report(
        self, command: ReportCriticalVulnerabilitiesCommand
    ) -> ReportCriticalVulnerabilitiesResponse:
        cves = self._port.get_critical_cves()
        has_data = bool(cves)
        result = compute_critical_cve_report(
            cves, total_scanned=len(cves), has_data=has_data, period="Dernier scan"
        )
        return ReportCriticalVulnerabilitiesResponse(result=result)
