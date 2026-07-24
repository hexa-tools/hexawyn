from hexawyn.application.ports.driven.critical_cve_port import CriticalCvePort
from hexawyn.application.use_case.report_critical_vulnerabilities.command import (
    ReportCriticalVulnerabilitiesCommand,
)
from hexawyn.application.use_case.report_critical_vulnerabilities.response import (
    ReportCriticalVulnerabilitiesResponse,
)
from hexawyn.domain.services.critical_cve.critical_cve_service import compute_critical_cve_report


class ReportCriticalVulnerabilitiesUseCase:
    def __init__(self, cve_port: CriticalCvePort) -> None:
        self._port = cve_port

    def execute(
        self, command: ReportCriticalVulnerabilitiesCommand
    ) -> ReportCriticalVulnerabilitiesResponse:
        cves = self._port.get_critical_cves()
        result = compute_critical_cve_report(
            cves, total_scanned=len(cves), has_data=bool(cves), period="Dernier scan"
        )
        return ReportCriticalVulnerabilitiesResponse(result=result)
