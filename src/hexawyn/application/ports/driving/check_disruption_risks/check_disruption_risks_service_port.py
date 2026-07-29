from abc import ABC, abstractmethod

from hexawyn.application.use_case.cluster.check_disruption_risks.command import (  # noqa: E501
    CheckDisruptionRisksCommand,
)
from hexawyn.application.use_case.cluster.check_disruption_risks.response import (  # noqa: E501
    CheckDisruptionRisksResponse,
)


class CheckDisruptionRisksServicePort(ABC):
    @abstractmethod
    def check(self, command: CheckDisruptionRisksCommand) -> CheckDisruptionRisksResponse: ...
