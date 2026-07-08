from __future__ import annotations

from hexawyn.application.ports.driving.generate_incident_triage_report.generate_incident_triage_report_command import (
    GenerateIncidentTriageReportCommand,
)
from hexawyn.application.ports.driving.generate_incident_triage_report.generate_incident_triage_report_response import (
    GenerateIncidentTriageReportResponse,
)
from hexawyn.application.ports.driving.generate_incident_triage_report.generate_incident_triage_report_service_port import (
    GenerateIncidentTriageReportServicePort,
)


class GenerateIncidentTriageReportUseCase:
    def __init__(self, service: GenerateIncidentTriageReportServicePort) -> None:
        self._svc = service

    def execute(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse:
        return self._svc.generate(command)
