"""Unit tests for ReportPlatformReliabilityUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.report_platform_reliability.report_platform_reliability_service_port import (
    ReportPlatformReliabilityServicePort,
)
from hexawyn.application.use_case.report_platform_reliability.report_platform_reliability_use_case import (
    ReportPlatformReliabilityUseCase,
)


class TestReportPlatformReliabilityUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=ReportPlatformReliabilityServicePort)
        use_case = ReportPlatformReliabilityUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.report.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=ReportPlatformReliabilityServicePort)
        mock_service.report.side_effect = RuntimeError("test error")
        use_case = ReportPlatformReliabilityUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
