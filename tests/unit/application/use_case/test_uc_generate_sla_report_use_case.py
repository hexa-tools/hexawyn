"""Unit tests for GenerateSlaReportUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.generate_sla_report.generate_sla_report_service_port import (
    GenerateSlaReportServicePort,
)
from hexawyn.application.use_case.generate_sla_report.generate_sla_report_use_case import (
    GenerateSlaReportUseCase,
)


class TestGenerateSlaReportUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=GenerateSlaReportServicePort)
        use_case = GenerateSlaReportUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.generate.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=GenerateSlaReportServicePort)
        mock_service.generate.side_effect = RuntimeError("test error")
        use_case = GenerateSlaReportUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
