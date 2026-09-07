from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.security.report_critical_vulnerabilities.command import (
    ReportCriticalVulnerabilitiesCommand,
)
from hexawyn.application.use_case.security.report_critical_vulnerabilities.report_critical_vulnerabilities_use_case import (  # noqa: E501
    ReportCriticalVulnerabilitiesUseCase,
)
from hexawyn.application.use_case.security.report_critical_vulnerabilities.response import (
    ReportCriticalVulnerabilitiesResponse,
)


class TestReportCriticalVulnerabilitiesUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.get_critical_cves.return_value = []

        use_case = ReportCriticalVulnerabilitiesUseCase(cve_port=port)
        result = use_case.execute(ReportCriticalVulnerabilitiesCommand())

        assert isinstance(result, ReportCriticalVulnerabilitiesResponse)

    def test_execute_with_cves(self) -> None:
        port = MagicMock()
        port.get_critical_cves.return_value = [
            {"cve_id": "CVE-2024-0001", "severity": "HIGH", "image": "nginx:1.25"},
        ]

        use_case = ReportCriticalVulnerabilitiesUseCase(cve_port=port)
        result = use_case.execute(ReportCriticalVulnerabilitiesCommand())

        assert isinstance(result, ReportCriticalVulnerabilitiesResponse)
        assert result.result is not None
