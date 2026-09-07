from abc import ABC, abstractmethod

from hexawyn.application.use_case.troubleshooting.detect_recurring_incidents.command import (  # noqa: E501
    DetectRecurringIncidentsCommand,
)
from hexawyn.application.use_case.troubleshooting.detect_recurring_incidents.response import (  # noqa: E501
    DetectRecurringIncidentsResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class DetectRecurringIncidentsServicePort(ABC):
    @abstractmethod
    def detect(  # noqa: E501
        self, command: DetectRecurringIncidentsCommand
    ) -> DetectRecurringIncidentsResponse: ...
