from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.finops.compute_monthly_incident_report.command import (
    ComputeMonthlyIncidentReportCommand,
)
from hexawyn.application.use_case.finops.compute_monthly_incident_report.compute_monthly_incident_report_use_case import (  # noqa: E501
    ComputeMonthlyIncidentReportUseCase,
)
from hexawyn.application.use_case.finops.compute_monthly_incident_report.response import (  # noqa: E501
    ComputeMonthlyIncidentReportResponse,
)


class TestComputeMonthlyIncidentReportUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.fetch_incidents.return_value = []

        use_case = ComputeMonthlyIncidentReportUseCase(
            incident_port=port,
        )
        result = use_case.execute(ComputeMonthlyIncidentReportCommand())

        assert isinstance(result, ComputeMonthlyIncidentReportResponse)
