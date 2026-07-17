from unittest.mock import MagicMock

from hexawyn.application.ports.driven.critical_cve_port import CriticalCvePort
from hexawyn.application.ports.driving.report_critical_vulnerabilities.report_critical_vulnerabilities_command import (  # noqa: E501
    ReportCriticalVulnerabilitiesCommand,
)


class TestReportCriticalVulnerabilitiesService:
    def test_implements_service_port(self) -> None:
        from hexawyn.application.ports.driving.report_critical_vulnerabilities.report_critical_vulnerabilities_service_port import (  # noqa: E501
            ReportCriticalVulnerabilitiesServicePort,
        )
        from hexawyn.application.service.report_critical_vulnerabilities_service import (
            ReportCriticalVulnerabilitiesService,
        )

        service = ReportCriticalVulnerabilitiesService(cve_port=MagicMock(spec=CriticalCvePort))

        assert isinstance(service, ReportCriticalVulnerabilitiesServicePort)

    def test_report_returns_result(self) -> None:
        from hexawyn.application.service.report_critical_vulnerabilities_service import (
            ReportCriticalVulnerabilitiesService,
        )

        port = MagicMock(spec=CriticalCvePort)
        port.get_critical_cves.return_value = []
        service = ReportCriticalVulnerabilitiesService(cve_port=port)

        response = service.report(ReportCriticalVulnerabilitiesCommand())

        assert response.result.total_critical_cves == 0
