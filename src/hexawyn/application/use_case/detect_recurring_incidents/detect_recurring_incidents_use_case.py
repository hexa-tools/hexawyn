from hexawyn.application.ports.driven.recurring_incident_port import RecurringIncidentPort
from hexawyn.application.use_case.detect_recurring_incidents.command import (
    DetectRecurringIncidentsCommand,
)
from hexawyn.application.use_case.detect_recurring_incidents.response import (
    DetectRecurringIncidentsResponse,
)
from hexawyn.domain.services.recurring_incident.recurring_incident_engine import (
    RecurringIncidentEngine,
)


class DetectRecurringIncidentsUseCase:
    def __init__(self, incident_port: RecurringIncidentPort) -> None:
        self._port = incident_port
        self._engine = RecurringIncidentEngine()

    def execute(self, command: DetectRecurringIncidentsCommand) -> DetectRecurringIncidentsResponse:
        raw = self._port.fetch_incidents(command.window_days)
        incidents: list[dict[str, object]] = [dict(i) for i in raw]
        result = self._engine.compute(incidents)
        return DetectRecurringIncidentsResponse(result=result)
