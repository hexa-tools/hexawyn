"""Unit tests for ReportCriticalVulnerabilitiesUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.report_critical_vulnerabilities.report_critical_vulnerabilities_service_port import (
    ReportCriticalVulnerabilitiesServicePort,
)
from hexawyn.application.use_case.report_critical_vulnerabilities.report_critical_vulnerabilities_use_case import (
    ReportCriticalVulnerabilitiesUseCase,
)


class TestReportCriticalVulnerabilitiesUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=ReportCriticalVulnerabilitiesServicePort)
        use_case = ReportCriticalVulnerabilitiesUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.report.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=ReportCriticalVulnerabilitiesServicePort)
        mock_service.report.side_effect = RuntimeError("test error")
        use_case = ReportCriticalVulnerabilitiesUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
