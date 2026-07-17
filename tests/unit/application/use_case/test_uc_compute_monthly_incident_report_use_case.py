"""Unit tests for ComputeMonthlyIncidentReportUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.compute_monthly_incident_report.compute_monthly_incident_report_service_port import (
    ComputeMonthlyIncidentReportServicePort,
)
from hexawyn.application.use_case.compute_monthly_incident_report.compute_monthly_incident_report_use_case import (
    ComputeMonthlyIncidentReportUseCase,
)


class TestComputeMonthlyIncidentReportUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=ComputeMonthlyIncidentReportServicePort)
        use_case = ComputeMonthlyIncidentReportUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.compute.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=ComputeMonthlyIncidentReportServicePort)
        mock_service.compute.side_effect = RuntimeError("test error")
        use_case = ComputeMonthlyIncidentReportUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
