from abc import ABC, abstractmethod

from hexawyn.application.use_case.finops.analyze_incident_cost.command import (  # noqa: E501
    AnalyzeIncidentCostCommand,
)
from hexawyn.application.use_case.finops.analyze_incident_cost.response import (  # noqa: E501
    AnalyzeIncidentCostResponse,
)


class AnalyzeIncidentCostServicePort(ABC):
    @abstractmethod
    def analyze(self, command: AnalyzeIncidentCostCommand) -> AnalyzeIncidentCostResponse: ...
