from abc import ABC


class TestAnalyzeIncidentCostServicePort:
    def test_is_abstract_base_class(self) -> None:
        from hexawyn.application.ports.driving.analyze_incident_cost.analyze_incident_cost_service_port import (  # noqa: E501
            AnalyzeIncidentCostServicePort,
        )

        assert issubclass(AnalyzeIncidentCostServicePort, ABC)

    def test_declares_analyze_method(self) -> None:
        from hexawyn.application.ports.driving.analyze_incident_cost.analyze_incident_cost_service_port import (  # noqa: E501
            AnalyzeIncidentCostServicePort,
        )

        assert "analyze" in AnalyzeIncidentCostServicePort.__abstractmethods__
