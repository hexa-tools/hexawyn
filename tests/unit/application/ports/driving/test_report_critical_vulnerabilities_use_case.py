from unittest.mock import MagicMock

from hexawyn.application.ports.driving.report_critical_vulnerabilities.report_critical_vulnerabilities_command import (  # noqa: E501
    ReportCriticalVulnerabilitiesCommand,
)
from hexawyn.application.ports.driving.report_critical_vulnerabilities.report_critical_vulnerabilities_response import (  # noqa: E501
    ReportCriticalVulnerabilitiesResponse,
)
from hexawyn.application.ports.driving.report_critical_vulnerabilities.report_critical_vulnerabilities_service_port import (  # noqa: E501
    ReportCriticalVulnerabilitiesServicePort,
)
from hexawyn.domain.models.critical_cve import CriticalCveReport


class TestReportCriticalVulnerabilitiesUseCase:
    def test_delegates(self) -> None:
        from hexawyn.application.use_case.report_critical_vulnerabilities.report_critical_vulnerabilities_use_case import (  # noqa: E501
            ReportCriticalVulnerabilitiesUseCase,
        )

        service = MagicMock(spec=ReportCriticalVulnerabilitiesServicePort)
        expected = ReportCriticalVulnerabilitiesResponse(
            result=CriticalCveReport(period_label="Dernier scan")
        )
        service.report.return_value = expected
        use_case = ReportCriticalVulnerabilitiesUseCase(service=service)

        response = use_case.execute(ReportCriticalVulnerabilitiesCommand())

        assert response is expected
