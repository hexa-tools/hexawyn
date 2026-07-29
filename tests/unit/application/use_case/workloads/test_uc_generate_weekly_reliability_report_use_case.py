from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.workloads.generate_weekly_reliability_report.command import (
    GenerateWeeklyReliabilityReportCommand,
)
from hexawyn.application.use_case.workloads.generate_weekly_reliability_report.generate_weekly_reliability_report_use_case import (  # noqa: E501
    GenerateWeeklyReliabilityReportUseCase,
)
from hexawyn.application.use_case.workloads.generate_weekly_reliability_report.response import (
    GenerateWeeklyReliabilityReportResponse,
)


class TestGenerateWeeklyReliabilityReportUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.fetch_service_reliability.return_value = []
        port.fetch_incidents.return_value = []

        use_case = GenerateWeeklyReliabilityReportUseCase(
            reliability_port=port,
        )
        result = use_case.generate_report(GenerateWeeklyReliabilityReportCommand(window_days=7))

        assert isinstance(result, GenerateWeeklyReliabilityReportResponse)

    def test_execute_empty_window(self) -> None:
        port = MagicMock()
        port.fetch_service_reliability.return_value = []
        port.fetch_incidents.return_value = []

        use_case = GenerateWeeklyReliabilityReportUseCase(
            reliability_port=port,
        )
        result = use_case.generate_report(GenerateWeeklyReliabilityReportCommand(window_days=0))

        assert isinstance(result, GenerateWeeklyReliabilityReportResponse)
