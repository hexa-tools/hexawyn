from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.detect_recurring_incidents.detect_recurring_incidents_command import (
    DetectRecurringIncidentsCommand,
)
from hexawyn.application.ports.driving.detect_recurring_incidents.detect_recurring_incidents_response import (
    DetectRecurringIncidentsResponse,
)


class DetectRecurringIncidentsServicePort(ABC):
    @abstractmethod
    def detect(
        self, command: DetectRecurringIncidentsCommand
    ) -> DetectRecurringIncidentsResponse: ...
