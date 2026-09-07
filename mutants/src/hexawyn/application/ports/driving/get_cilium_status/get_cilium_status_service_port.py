from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cilium.get_cilium_status.command import (
    GetCiliumStatusCommand,
)
from hexawyn.application.use_case.cilium.get_cilium_status.response import (
    GetCiliumStatusResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class GetCiliumStatusServicePort(ABC):
    @abstractmethod
    def status(self, command: GetCiliumStatusCommand) -> GetCiliumStatusResponse: ...
