from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driving.generate_incident_triage_report.generate_incident_triage_report_service_port import (
    GenerateIncidentTriageReportServicePort,
)


class TestGenerateIncidentTriageReportServicePort:
    def test_is_abstract(self) -> None:
        assert issubclass(GenerateIncidentTriageReportServicePort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            GenerateIncidentTriageReportServicePort()  # type: ignore[abstract]
