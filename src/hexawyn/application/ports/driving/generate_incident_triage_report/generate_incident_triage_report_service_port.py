from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.generate_incident_triage_report.generate_incident_triage_report_command import (
    GenerateIncidentTriageReportCommand,
)
from hexawyn.application.ports.driving.generate_incident_triage_report.generate_incident_triage_report_response import (
    GenerateIncidentTriageReportResponse,
)


class GenerateIncidentTriageReportServicePort(ABC):
    @abstractmethod
    def generate(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse: ...
