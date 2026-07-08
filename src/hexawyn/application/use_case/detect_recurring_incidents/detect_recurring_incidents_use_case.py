from __future__ import annotations

from hexawyn.application.ports.driving.detect_recurring_incidents.detect_recurring_incidents_command import (
    DetectRecurringIncidentsCommand,
)
from hexawyn.application.ports.driving.detect_recurring_incidents.detect_recurring_incidents_response import (
    DetectRecurringIncidentsResponse,
)
from hexawyn.application.ports.driving.detect_recurring_incidents.detect_recurring_incidents_service_port import (
    DetectRecurringIncidentsServicePort,
)


class DetectRecurringIncidentsUseCase:
    def __init__(self, service: DetectRecurringIncidentsServicePort) -> None:
        self._service = service

    def execute(self, command: DetectRecurringIncidentsCommand) -> DetectRecurringIncidentsResponse:
        return self._service.detect(command)
