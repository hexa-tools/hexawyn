"""RED → GREEN — Layers 3-6: driven port, driving ports, app service, use case."""

import inspect
from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driven.monthly_incident_port import (
    IncidentSnapshotData,
    MonthlyIncidentPort,
)
from hexawyn.application.ports.driving.compute_monthly_incident_report.compute_monthly_incident_report_command import (
    ComputeMonthlyIncidentReportCommand,
)
from hexawyn.application.ports.driving.compute_monthly_incident_report.compute_monthly_incident_report_response import (
    ComputeMonthlyIncidentReportResponse,
)
from hexawyn.application.ports.driving.compute_monthly_incident_report.compute_monthly_incident_report_service_port import (
    ComputeMonthlyIncidentReportServicePort,
)
from hexawyn.application.service.compute_monthly_incident_report_service import (
    ComputeMonthlyIncidentReportService,
    _previous_month,
)
from hexawyn.application.use_case.compute_monthly_incident_report.compute_monthly_incident_report_use_case import (
    ComputeMonthlyIncidentReportUseCase,
)
from hexawyn.domain.models.monthly_incident_report import MonthlyIncidentReport


class TestMonthlyIncidentPort:
    def test_is_abstract(self) -> None:
        assert inspect.isabstract(MonthlyIncidentPort)


class TestComputeMonthlyIncidentReportCommand:
    def test_default_month_is_none(self) -> None:
        cmd = ComputeMonthlyIncidentReportCommand()
        assert cmd.month is None

    def test_is_frozen(self) -> None:
        cmd = ComputeMonthlyIncidentReportCommand()
        with pytest.raises(Exception):
            cmd.month = "2026-06"  # type: ignore[misc]


class TestComputeMonthlyIncidentReportResponse:
    def test_holds_result(self) -> None:
        inner = MonthlyIncidentReport(total_count=8)
        resp = ComputeMonthlyIncidentReportResponse(result=inner)
        assert resp.result is inner


class TestComputeMonthlyIncidentReportService:
    def _mock_port(self) -> MagicMock:
        port = MagicMock(spec=MonthlyIncidentPort)
        port.fetch_incidents.return_value = []
        return port

    def test_calls_port_for_current_and_previous_month(self) -> None:
        port = self._mock_port()
        service = ComputeMonthlyIncidentReportService(incident_port=port)

        service.compute(ComputeMonthlyIncidentReportCommand(month="2026-07"))

        assert port.fetch_incidents.call_count == 2

    def test_counts_incidents_by_severity(self) -> None:
        port = MagicMock(spec=MonthlyIncidentPort)
        port.fetch_incidents.return_value = [
            IncidentSnapshotData(
                incident_id="INC-001",
                service_name="payment-service",
                severity="P1",
                downtime_minutes=45,
                timestamp="2026-07-15T10:00:00Z",
                resolved_at="2026-07-15T10:45:00Z",
                is_planned_maintenance=False,
                reopened=False,
            ),
        ]
        service = ComputeMonthlyIncidentReportService(incident_port=port)

        response = service.compute(ComputeMonthlyIncidentReportCommand(month="2026-07"))

        assert response.result.total_count == 1
        assert response.result.per_severity["P1"].count == 1

    def test_default_month_uses_current(self) -> None:
        port = self._mock_port()
        service = ComputeMonthlyIncidentReportService(incident_port=port)

        response = service.compute(ComputeMonthlyIncidentReportCommand())

        assert isinstance(response, ComputeMonthlyIncidentReportResponse)

    def test_january_previous_is_december(self) -> None:
        port = self._mock_port()
        service = ComputeMonthlyIncidentReportService(incident_port=port)

        response = service.compute(ComputeMonthlyIncidentReportCommand(month="2026-01"))

        assert response.result.total_count == 0


class TestPreviousMonth:
    def test_january_previous_is_december(self) -> None:
        assert _previous_month(2026, 1) == "2025-12"

    def test_july_previous_is_june(self) -> None:
        assert _previous_month(2026, 7) == "2026-06"


class TestComputeMonthlyIncidentReportUseCase:
    def test_delegates_to_service(self) -> None:
        service = MagicMock(spec=ComputeMonthlyIncidentReportServicePort)
        inner = MonthlyIncidentReport(total_count=5)
        service.compute.return_value = ComputeMonthlyIncidentReportResponse(result=inner)
        use_case = ComputeMonthlyIncidentReportUseCase(service=service)

        result = use_case.execute(ComputeMonthlyIncidentReportCommand())

        service.compute.assert_called_once()
        assert result.result is inner
