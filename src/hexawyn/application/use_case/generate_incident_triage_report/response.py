from dataclasses import dataclass

from hexawyn.domain.models.incident_triage import IncidentTriageReport


@dataclass
class GenerateIncidentTriageReportResponse:
    result: IncidentTriageReport | None = None
    error: str | None = None
