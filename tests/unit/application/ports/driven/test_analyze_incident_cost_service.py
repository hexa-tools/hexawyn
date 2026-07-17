from unittest.mock import MagicMock

from hexawyn.application.ports.driven.incident_cost_port import (
    IncidentCostData,
    IncidentCostPort,
)
from hexawyn.application.ports.driving.analyze_incident_cost.analyze_incident_cost_command import (  # noqa: E501
    AnalyzeIncidentCostCommand,
)


def _data(revenue: float | None = 500.0) -> IncidentCostData:
    return IncidentCostData(
        business_service_name="Service Paiement",
        downtime_minutes=27,
        impacted_service_count=3,
        resolved_at="14h23",
        sla_breached=False,
        business_config={
            "revenue_per_minute": revenue,
            "support_cost_per_hour": None,
            "sla_penalty_per_hour": None,
        },
    )


class TestAnalyzeIncidentCostService:
    def test_implements_service_port(self) -> None:
        from hexawyn.application.ports.driving.analyze_incident_cost.analyze_incident_cost_service_port import (  # noqa: E501
            AnalyzeIncidentCostServicePort,
        )
        from hexawyn.application.service.analyze_incident_cost_service import (
            AnalyzeIncidentCostService,
        )

        service = AnalyzeIncidentCostService(incident_cost_port=MagicMock(spec=IncidentCostPort))

        assert isinstance(service, AnalyzeIncidentCostServicePort)

    def test_analyze_returns_report(self) -> None:
        from hexawyn.application.service.analyze_incident_cost_service import (
            AnalyzeIncidentCostService,
        )

        port = MagicMock(spec=IncidentCostPort)
        port.get_incident_cost_data.return_value = _data()
        service = AnalyzeIncidentCostService(incident_cost_port=port)

        response = service.analyze(AnalyzeIncidentCostCommand(incident_ref="yesterday"))

        port.get_incident_cost_data.assert_called_once_with("yesterday")
        assert response.result.total_cost_eur == 13500.0

    def test_analyze_missing_config_returns_explanation(self) -> None:
        from hexawyn.application.service.analyze_incident_cost_service import (
            AnalyzeIncidentCostService,
        )

        port = MagicMock(spec=IncidentCostPort)
        port.get_incident_cost_data.return_value = _data(revenue=None)
        service = AnalyzeIncidentCostService(incident_cost_port=port)

        response = service.analyze(AnalyzeIncidentCostCommand(incident_ref="yesterday"))

        assert response.result.config_available is False
        assert response.result.total_cost_eur is None

    def test_analyze_lets_error_propagate(self) -> None:
        import pytest
        from hexawyn.application.service.analyze_incident_cost_service import (
            AnalyzeIncidentCostService,
        )
        from hexawyn.domain.errors import ClusterUnreachableError

        port = MagicMock(spec=IncidentCostPort)
        port.get_incident_cost_data.side_effect = ClusterUnreachableError("down")
        service = AnalyzeIncidentCostService(incident_cost_port=port)

        with pytest.raises(ClusterUnreachableError):
            service.analyze(AnalyzeIncidentCostCommand(incident_ref="yesterday"))
