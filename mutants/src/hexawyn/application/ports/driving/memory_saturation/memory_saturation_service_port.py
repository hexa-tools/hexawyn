from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.troubleshooting.memory_saturation.command import (
    MemorySaturationCommand,
)
from hexawyn.application.use_case.troubleshooting.memory_saturation.response import (
    MemorySaturationResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class MemorySaturationServicePort(ABC):
    @abstractmethod
    def predict(self, command: MemorySaturationCommand) -> MemorySaturationResponse: ...
