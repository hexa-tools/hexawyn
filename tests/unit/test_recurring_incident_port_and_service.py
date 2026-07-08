"""RED → GREEN — Layers 3-6: driven port, driving ports, app service, use case."""

import inspect
from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driven.recurring_incident_port import (
    IncidentFrequencyData,
    RecurringIncidentPort,
)
from hexawyn.application.ports.driving.detect_recurring_incidents.detect_recurring_incidents_command import (
    DetectRecurringIncidentsCommand,
)
from hexawyn.application.ports.driving.detect_recurring_incidents.detect_recurring_incidents_response import (
    DetectRecurringIncidentsResponse,
)
from hexawyn.application.ports.driving.detect_recurring_incidents.detect_recurring_incidents_service_port import (
    DetectRecurringIncidentsServicePort,
)
from hexawyn.application.service.detect_recurring_incidents_service import (
    DetectRecurringIncidentsService,
)
from hexawyn.application.use_case.detect_recurring_incidents.detect_recurring_incidents_use_case import (
    DetectRecurringIncidentsUseCase,
)
from hexawyn.domain.models.recurring_incident import RecurringIncidentReport


class TestRecurringIncidentPort:
    def test_is_abstract(self) -> None:
        assert inspect.isabstract(RecurringIncidentPort)


class TestDetectRecurringIncidentsCommand:
    def test_default_window_is_30(self) -> None:
        cmd = DetectRecurringIncidentsCommand()
        assert cmd.window_days == 30

    def test_is_frozen(self) -> None:
        cmd = DetectRecurringIncidentsCommand()
        with pytest.raises(Exception):
            cmd.window_days = 7  # type: ignore[misc]


class TestDetectRecurringIncidentsResponse:
    def test_holds_result(self) -> None:
        inner = RecurringIncidentReport()
        resp = DetectRecurringIncidentsResponse(result=inner)
        assert resp.result is inner


class TestDetectRecurringIncidentsService:
    def _mock_port(self) -> MagicMock:
        port = MagicMock(spec=RecurringIncidentPort)
        port.fetch_incidents.return_value = []
        return port

    def test_calls_port_with_window(self) -> None:
        port = self._mock_port()
        service = DetectRecurringIncidentsService(incident_port=port)

        service.detect(DetectRecurringIncidentsCommand(window_days=30))

        port.fetch_incidents.assert_called_once_with(30)

    def test_detects_recurring_pattern(self) -> None:
        port = MagicMock(spec=RecurringIncidentPort)
        port.fetch_incidents.return_value = [
            IncidentFrequencyData(
                incident_id="INC-001",
                service_name="payment-service",
                root_cause="DB pool exhausted",
                duration_minutes=20,
                timestamp="2026-07-01T10:00:00Z",
            ),
            IncidentFrequencyData(
                incident_id="INC-002",
                service_name="payment-service",
                root_cause="DB pool exhausted",
                duration_minutes=15,
                timestamp="2026-07-05T10:00:00Z",
            ),
            IncidentFrequencyData(
                incident_id="INC-003",
                service_name="payment-service",
                root_cause="DB pool exhausted",
                duration_minutes=25,
                timestamp="2026-07-10T10:00:00Z",
            ),
            IncidentFrequencyData(
                incident_id="INC-004",
                service_name="payment-service",
                root_cause="DB pool exhausted",
                duration_minutes=10,
                timestamp="2026-07-15T10:00:00Z",
            ),
        ]
        service = DetectRecurringIncidentsService(incident_port=port)

        response = service.detect(DetectRecurringIncidentsCommand())

        assert response.result.services[0].is_recurring is True
        assert response.result.services[0].recurrence_count == 4


class TestDetectRecurringIncidentsUseCase:
    def test_delegates_to_service(self) -> None:
        service = MagicMock(spec=DetectRecurringIncidentsServicePort)
        inner = RecurringIncidentReport()
        service.detect.return_value = DetectRecurringIncidentsResponse(result=inner)
        use_case = DetectRecurringIncidentsUseCase(service=service)

        result = use_case.execute(DetectRecurringIncidentsCommand())

        service.detect.assert_called_once()
        assert result.result is inner
