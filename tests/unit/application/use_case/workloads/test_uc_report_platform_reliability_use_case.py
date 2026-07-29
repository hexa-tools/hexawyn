from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.workloads.report_platform_reliability.command import (
    ReportPlatformReliabilityCommand,
)
from hexawyn.application.use_case.workloads.report_platform_reliability.report_platform_reliability_use_case import (  # noqa: E501
    ReportPlatformReliabilityUseCase,
)
from hexawyn.application.use_case.workloads.report_platform_reliability.response import (
    ReportPlatformReliabilityResponse,
)


class TestReportPlatformReliabilityUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.get_reliability_data.return_value = {
            "period_minutes": 43200,
            "incidents": [],
            "previous_avg_resolution_minutes": 30,
            "cost_per_downtime_minute_eur": 10.0,
        }

        use_case = ReportPlatformReliabilityUseCase(
            reliability_port=port,
        )
        result = use_case.execute(ReportPlatformReliabilityCommand(period="2025-06"))

        assert isinstance(result, ReportPlatformReliabilityResponse)

    def test_execute_no_data(self) -> None:
        port = MagicMock()
        port.get_reliability_data.return_value = {
            "period_minutes": 0,
            "incidents": [],
            "previous_avg_resolution_minutes": None,
            "cost_per_downtime_minute_eur": None,
        }

        use_case = ReportPlatformReliabilityUseCase(
            reliability_port=port,
        )
        result = use_case.execute(ReportPlatformReliabilityCommand(period="2025-01"))

        assert isinstance(result, ReportPlatformReliabilityResponse)
