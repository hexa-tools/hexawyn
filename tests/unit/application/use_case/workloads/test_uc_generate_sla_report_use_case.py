from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.workloads.generate_sla_report.command import (
    GenerateSLAReportCommand,
)
from hexawyn.application.use_case.workloads.generate_sla_report.generate_sla_report_use_case import (  # noqa: E501
    GenerateSLAReportUseCase,
)
from hexawyn.application.use_case.workloads.generate_sla_report.response import (
    GenerateSLAReportResponse,
)


class TestGenerateSLAReportUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.get_quarter_sla_data.return_value = {
            "has_data": True,
            "services": [],
            "breaches": [],
        }
        port.get_previous_quarter_avg_uptime.return_value = 99.5

        use_case = GenerateSLAReportUseCase(sla_port=port)
        result = use_case.execute(GenerateSLAReportCommand(quarter="2025-Q1"))

        assert isinstance(result, GenerateSLAReportResponse)

    def test_execute_no_data_quarter(self) -> None:
        port = MagicMock()
        port.get_quarter_sla_data.return_value = {
            "has_data": False,
            "services": [],
            "breaches": [],
        }
        port.get_previous_quarter_avg_uptime.return_value = None

        use_case = GenerateSLAReportUseCase(sla_port=port)
        result = use_case.execute(GenerateSLAReportCommand(quarter="2020-Q1"))

        assert isinstance(result, GenerateSLAReportResponse)
