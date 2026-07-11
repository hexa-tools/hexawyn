from __future__ import annotations

from hexawyn.application.ports.driving.analyze_incident_cost.analyze_incident_cost_command import (  # noqa: E501
    AnalyzeIncidentCostCommand,
)
from hexawyn.application.ports.driving.analyze_incident_cost.analyze_incident_cost_response import (  # noqa: E501
    AnalyzeIncidentCostResponse,
)
from hexawyn.application.ports.driving.analyze_incident_cost.analyze_incident_cost_service_port import (  # noqa: E501
    AnalyzeIncidentCostServicePort,
)


class AnalyzeIncidentCostUseCase:
    def __init__(self, service: AnalyzeIncidentCostServicePort) -> None:
        self._service = service

    def execute(self, command: AnalyzeIncidentCostCommand) -> AnalyzeIncidentCostResponse:
        return self._service.analyze(command)
