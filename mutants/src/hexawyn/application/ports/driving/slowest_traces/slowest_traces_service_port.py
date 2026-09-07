from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.observability.slowest_traces.command import (
    SlowestTracesCommand,
)
from hexawyn.application.use_case.observability.slowest_traces.response import (
    SlowestTracesResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class SlowestTracesServicePort(ABC):
    @abstractmethod
    def find_slowest(self, command: SlowestTracesCommand) -> SlowestTracesResponse: ...
