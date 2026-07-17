"""Unit tests for ReportNightInterventionsUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.report_night_interventions.report_night_interventions_service_port import (
    ReportNightInterventionsServicePort,
)
from hexawyn.application.use_case.report_night_interventions.report_night_interventions_use_case import (
    ReportNightInterventionsUseCase,
)


class TestReportNightInterventionsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=ReportNightInterventionsServicePort)
        use_case = ReportNightInterventionsUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.report.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=ReportNightInterventionsServicePort)
        mock_service.report.side_effect = RuntimeError("test error")
        use_case = ReportNightInterventionsUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
