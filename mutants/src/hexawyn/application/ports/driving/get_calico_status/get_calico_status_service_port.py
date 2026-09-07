from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.calico.get_calico_status.command import (
    GetCalicoStatusCommand,
)
from hexawyn.application.use_case.calico.get_calico_status.response import (
    GetCalicoStatusResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class GetCalicoStatusServicePort(ABC):
    """Inbound port for Calico datapath status."""

    @abstractmethod
    def get_status(self, command: GetCalicoStatusCommand) -> GetCalicoStatusResponse: ...
