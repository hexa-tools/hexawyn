from unittest.mock import MagicMock

from hexawyn.application.ports.driving.analyze_incident_cost.analyze_incident_cost_command import (  # noqa: E501
    AnalyzeIncidentCostCommand,
)
from hexawyn.application.ports.driving.analyze_incident_cost.analyze_incident_cost_response import (  # noqa: E501
    AnalyzeIncidentCostResponse,
)
from hexawyn.application.ports.driving.analyze_incident_cost.analyze_incident_cost_service_port import (  # noqa: E501
    AnalyzeIncidentCostServicePort,
)
from hexawyn.domain.models.incident_cost import IncidentCostReport


class TestAnalyzeIncidentCostUseCase:
    def test_execute_delegates_to_service(self) -> None:
        from hexawyn.application.use_case.analyze_incident_cost.analyze_incident_cost_use_case import (  # noqa: E501
            AnalyzeIncidentCostUseCase,
        )

        service = MagicMock(spec=AnalyzeIncidentCostServicePort)
        expected = AnalyzeIncidentCostResponse(
            result=IncidentCostReport(business_service_name="Service Paiement", downtime_minutes=27)
        )
        service.analyze.return_value = expected
        use_case = AnalyzeIncidentCostUseCase(service=service)
        command = AnalyzeIncidentCostCommand(incident_ref="yesterday")

        response = use_case.execute(command)

        service.analyze.assert_called_once_with(command)
        assert response is expected
