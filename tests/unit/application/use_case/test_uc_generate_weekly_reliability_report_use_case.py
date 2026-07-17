"""Unit tests for GenerateWeeklyReliabilityReportUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.generate_weekly_reliability_report.generate_weekly_reliability_report_service_port import (
    GenerateWeeklyReliabilityReportServicePort,
)
from hexawyn.application.use_case.generate_weekly_reliability_report.generate_weekly_reliability_report_use_case import (
    GenerateWeeklyReliabilityReportUseCase,
)


class TestGenerateWeeklyReliabilityReportUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=GenerateWeeklyReliabilityReportServicePort)
        use_case = GenerateWeeklyReliabilityReportUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.generate_report.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=GenerateWeeklyReliabilityReportServicePort)
        mock_service.generate_report.side_effect = RuntimeError("test error")
        use_case = GenerateWeeklyReliabilityReportUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
