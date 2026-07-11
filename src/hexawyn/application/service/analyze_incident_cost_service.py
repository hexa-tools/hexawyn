from __future__ import annotations

from hexawyn.application.ports.driven.incident_cost_port import IncidentCostPort
from hexawyn.application.ports.driving.analyze_incident_cost.analyze_incident_cost_command import (  # noqa: E501
    AnalyzeIncidentCostCommand,
)
from hexawyn.application.ports.driving.analyze_incident_cost.analyze_incident_cost_response import (  # noqa: E501
    AnalyzeIncidentCostResponse,
)
from hexawyn.application.ports.driving.analyze_incident_cost.analyze_incident_cost_service_port import (  # noqa: E501
    AnalyzeIncidentCostServicePort,
)
from hexawyn.domain.services.incident_cost.incident_cost_calculator import (
    compute_incident_cost,
)


class AnalyzeIncidentCostService(AnalyzeIncidentCostServicePort):
    def __init__(self, incident_cost_port: IncidentCostPort) -> None:
        self._port = incident_cost_port

    def analyze(self, command: AnalyzeIncidentCostCommand) -> AnalyzeIncidentCostResponse:
        data = self._port.get_incident_cost_data(command.incident_ref)
        result = compute_incident_cost(data)
        return AnalyzeIncidentCostResponse(result=result)
