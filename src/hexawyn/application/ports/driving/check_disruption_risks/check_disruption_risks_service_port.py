from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.check_disruption_risks.check_disruption_risks_command import (  # noqa: E501
    CheckDisruptionRisksCommand,
)
from hexawyn.application.ports.driving.check_disruption_risks.check_disruption_risks_response import (  # noqa: E501
    CheckDisruptionRisksResponse,
)


class CheckDisruptionRisksServicePort(ABC):
    @abstractmethod
    def check(self, command: CheckDisruptionRisksCommand) -> CheckDisruptionRisksResponse: ...
