from __future__ import annotations

from hexawyn.application.ports.driving.generate_incident_triage_report.generate_incident_triage_report_response import (
    GenerateIncidentTriageReportResponse,
)


class TestGenerateIncidentTriageReportResponse:
    def test_defaults(self) -> None:
        response = GenerateIncidentTriageReportResponse()
        assert response.timeline == []
        assert response.root_causes == []
        assert response.remediation_steps == []
        assert response.resolved is False
        assert response.resolution_time is None
        assert response.mttr_minutes is None
        assert response.ntp_drift_detected is False
        assert response.cross_namespace_correlation == []
        assert response.insufficient_data is False
        assert response.data_checked == []
        assert response.formatted_report == ""
        assert response.error is None

    def test_error_field(self) -> None:
        response = GenerateIncidentTriageReportResponse(error="Namespace 'ghost' not found")
        assert response.error == "Namespace 'ghost' not found"
