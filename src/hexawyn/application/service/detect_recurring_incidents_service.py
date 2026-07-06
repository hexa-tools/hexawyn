from __future__ import annotations

from hexawyn.application.ports.driven.recurring_incident_port import (
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
from hexawyn.domain.services.recurring_incident.recurring_incident_engine import (
    RecurringIncidentEngine,
)


class DetectRecurringIncidentsService(DetectRecurringIncidentsServicePort):
    def __init__(self, incident_port: RecurringIncidentPort) -> None:
        self._port = incident_port
        self._engine = RecurringIncidentEngine()

    def detect(self, command: DetectRecurringIncidentsCommand) -> DetectRecurringIncidentsResponse:
        raw = self._port.fetch_incidents(command.window_days)
        incidents: list[dict[str, object]] = [dict(i) for i in raw]
        result = self._engine.compute(incidents)
        return DetectRecurringIncidentsResponse(result=result)
