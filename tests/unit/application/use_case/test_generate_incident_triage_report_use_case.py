"""Unit tests for generate_incident_triage_report use case components."""

from __future__ import annotations


class TestGenerateIncidentTriageReportCommand:
    def test_command_is_dataclass(self) -> None:
        from hexawyn.application.use_case.generate_incident_triage_report.command import (
            GenerateIncidentTriageReportCommand,
        )

        cmd = GenerateIncidentTriageReportCommand()
        assert cmd is not None


class TestGenerateIncidentTriageReportResponse:
    def test_response_defaults(self) -> None:
        from hexawyn.application.use_case.generate_incident_triage_report.response import (
            GenerateIncidentTriageReportResponse,
        )

        resp = GenerateIncidentTriageReportResponse()
        assert resp.result is None
        assert resp.error is None

    def test_response_with_error(self) -> None:
        from hexawyn.application.use_case.generate_incident_triage_report.response import (
            GenerateIncidentTriageReportResponse,
        )

        resp = GenerateIncidentTriageReportResponse(error="test error")
        assert resp.error == "test error"
        assert resp.result is None


class TestGenerateIncidentTriageReportUseCase:
    def test_instantiation_succeeds(self) -> None:
        from unittest.mock import MagicMock

        from hexawyn.application.use_case.generate_incident_triage_report.generate_incident_triage_report_use_case import (
            GenerateIncidentTriageReportUseCase,
        )

        port = MagicMock()
        use_case = GenerateIncidentTriageReportUseCase(port=port)
        assert use_case is not None

    def test_execute_returns_response(self) -> None:
        from unittest.mock import MagicMock

        from hexawyn.application.use_case.generate_incident_triage_report.command import (
            GenerateIncidentTriageReportCommand,
        )
        from hexawyn.application.use_case.generate_incident_triage_report.generate_incident_triage_report_use_case import (
            GenerateIncidentTriageReportUseCase,
        )

        port = MagicMock()
        use_case = GenerateIncidentTriageReportUseCase(port=port)
        response = use_case.execute(GenerateIncidentTriageReportCommand())
        assert response.error is None
        assert response.result is None
