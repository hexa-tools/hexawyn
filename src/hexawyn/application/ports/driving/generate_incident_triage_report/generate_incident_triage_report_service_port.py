from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.troubleshooting.generate_incident_triage_report.command import (
    GenerateIncidentTriageReportCommand,
)
from hexawyn.application.use_case.troubleshooting.generate_incident_triage_report.response import (
    GenerateIncidentTriageReportResponse,
)


class GenerateIncidentTriageReportServicePort(ABC):
    @abstractmethod
    def generate(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse: ...
