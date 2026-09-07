from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cilium.cilium_service_graph.command import (
    CiliumServiceGraphCommand,
)
from hexawyn.application.use_case.cilium.cilium_service_graph.response import (
    CiliumServiceGraphResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CiliumServiceGraphServicePort(ABC):
    @abstractmethod
    def build(self, command: CiliumServiceGraphCommand) -> CiliumServiceGraphResponse: ...
