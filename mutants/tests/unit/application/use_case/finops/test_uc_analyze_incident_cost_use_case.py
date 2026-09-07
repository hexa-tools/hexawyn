from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.finops.analyze_incident_cost.analyze_incident_cost_use_case import (  # noqa: E501
    AnalyzeIncidentCostUseCase,
)
from hexawyn.application.use_case.finops.analyze_incident_cost.command import (
    AnalyzeIncidentCostCommand,
)
from hexawyn.application.use_case.finops.analyze_incident_cost.response import (  # noqa: E501
    AnalyzeIncidentCostResponse,
)


class TestAnalyzeIncidentCostUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.get_incident_costs.return_value = []

        use_case = AnalyzeIncidentCostUseCase(incident_cost_port=port)
        result = use_case.execute(AnalyzeIncidentCostCommand(incident_ref="INC-001"))

        assert isinstance(result, AnalyzeIncidentCostResponse)

    def test_execute_with_no_incidents(self) -> None:
        port = MagicMock()
        port.get_incident_costs.return_value = []

        use_case = AnalyzeIncidentCostUseCase(incident_cost_port=port)
        result = use_case.execute(AnalyzeIncidentCostCommand(incident_ref="NONEXISTENT"))

        assert isinstance(result, AnalyzeIncidentCostResponse)
