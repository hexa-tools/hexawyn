"""Unit tests for GenerateIncidentTriageReportUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.generate_incident_triage_report.generate_incident_triage_report_service_port import (
    GenerateIncidentTriageReportServicePort,
)
from hexawyn.application.use_case.generate_incident_triage_report.generate_incident_triage_report_use_case import (
    GenerateIncidentTriageReportUseCase,
)


class TestGenerateIncidentTriageReportUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=GenerateIncidentTriageReportServicePort)
        use_case = GenerateIncidentTriageReportUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.generate.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=GenerateIncidentTriageReportServicePort)
        mock_service.generate.side_effect = RuntimeError("test error")
        use_case = GenerateIncidentTriageReportUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
