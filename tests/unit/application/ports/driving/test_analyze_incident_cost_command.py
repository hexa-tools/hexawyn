import dataclasses


class TestAnalyzeIncidentCostCommand:
    def test_holds_incident_ref(self) -> None:
        from hexawyn.application.ports.driving.analyze_incident_cost.analyze_incident_cost_command import (  # noqa: E501
            AnalyzeIncidentCostCommand,
        )

        command = AnalyzeIncidentCostCommand(incident_ref="yesterday")

        assert command.incident_ref == "yesterday"
        assert dataclasses.is_dataclass(AnalyzeIncidentCostCommand)
