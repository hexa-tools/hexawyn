from hexawyn.domain.models.incident_cost import IncidentCostReport


class TestAnalyzeIncidentCostResponse:
    def test_wraps_report(self) -> None:
        from hexawyn.application.ports.driving.analyze_incident_cost.analyze_incident_cost_response import (  # noqa: E501
            AnalyzeIncidentCostResponse,
        )

        report = IncidentCostReport(business_service_name="Service Paiement", downtime_minutes=27)
        response = AnalyzeIncidentCostResponse(result=report)

        assert response.result is report
        assert response.result.downtime_minutes == 27
