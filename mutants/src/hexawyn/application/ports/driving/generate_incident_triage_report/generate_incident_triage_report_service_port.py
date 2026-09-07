from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.troubleshooting.generate_incident_triage_report.command import (
    GenerateIncidentTriageReportCommand,
)
from hexawyn.application.use_case.troubleshooting.generate_incident_triage_report.response import (
    GenerateIncidentTriageReportResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class GenerateIncidentTriageReportServicePort(ABC):
    @abstractmethod
    def generate(
        self, command: GenerateIncidentTriageReportCommand
    ) -> GenerateIncidentTriageReportResponse: ...
