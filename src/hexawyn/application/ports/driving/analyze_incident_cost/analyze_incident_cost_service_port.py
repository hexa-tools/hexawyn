from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.analyze_incident_cost.analyze_incident_cost_command import (  # noqa: E501
    AnalyzeIncidentCostCommand,
)
from hexawyn.application.ports.driving.analyze_incident_cost.analyze_incident_cost_response import (  # noqa: E501
    AnalyzeIncidentCostResponse,
)


class AnalyzeIncidentCostServicePort(ABC):
    @abstractmethod
    def analyze(self, command: AnalyzeIncidentCostCommand) -> AnalyzeIncidentCostResponse: ...
