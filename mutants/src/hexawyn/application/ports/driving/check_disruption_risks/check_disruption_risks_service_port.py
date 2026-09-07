from abc import ABC, abstractmethod

from hexawyn.application.use_case.cluster.check_disruption_risks.command import (  # noqa: E501
    CheckDisruptionRisksCommand,
)
from hexawyn.application.use_case.cluster.check_disruption_risks.response import (  # noqa: E501
    CheckDisruptionRisksResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CheckDisruptionRisksServicePort(ABC):
    @abstractmethod
    def check(self, command: CheckDisruptionRisksCommand) -> CheckDisruptionRisksResponse: ...
