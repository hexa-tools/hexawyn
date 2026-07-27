from dataclasses import dataclass

from hexawyn.domain.models.incident_cost import IncidentCostReport


@dataclass
class AnalyzeIncidentCostResponse:
    result: IncidentCostReport
