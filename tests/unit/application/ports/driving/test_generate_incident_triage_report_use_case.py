from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.generate_incident_triage_report.generate_incident_triage_report_command import (
    GenerateIncidentTriageReportCommand,
)
from hexawyn.application.ports.driving.generate_incident_triage_report.generate_incident_triage_report_response import (
    GenerateIncidentTriageReportResponse,
)
from hexawyn.application.ports.driving.generate_incident_triage_report.generate_incident_triage_report_service_port import (
    GenerateIncidentTriageReportServicePort,
)
from hexawyn.application.use_case.generate_incident_triage_report.generate_incident_triage_report_use_case import (
    GenerateIncidentTriageReportUseCase,
)


class TestGenerateIncidentTriageReportUseCase:
    def test_execute_delegates_to_service(self) -> None:
        service = MagicMock(spec=GenerateIncidentTriageReportServicePort)
        expected = GenerateIncidentTriageReportResponse(namespace="payment")
        service.generate.return_value = expected
        use_case = GenerateIncidentTriageReportUseCase(service=service)
        command = GenerateIncidentTriageReportCommand(namespace="payment")

        result = use_case.execute(command)

        service.generate.assert_called_once_with(command)
        assert result is expected
