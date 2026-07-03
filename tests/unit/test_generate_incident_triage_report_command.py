from __future__ import annotations

from hexawyn.application.ports.driving.generate_incident_triage_report.generate_incident_triage_report_command import (
    GenerateIncidentTriageReportCommand,
)


class TestGenerateIncidentTriageReportCommand:
    def test_defaults(self) -> None:
        cmd = GenerateIncidentTriageReportCommand(namespace="payment")
        assert cmd.time_window_minutes == 120
        assert cmd.related_namespaces == []

    def test_explicit_value(self) -> None:
        cmd = GenerateIncidentTriageReportCommand(
            namespace="payment", time_window_minutes=60, related_namespaces=["billing"]
        )
        assert cmd.time_window_minutes == 60
        assert cmd.related_namespaces == ["billing"]
