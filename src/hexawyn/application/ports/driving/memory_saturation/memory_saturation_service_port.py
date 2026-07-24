from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.memory_saturation.command import (
    MemorySaturationCommand,
)
from hexawyn.application.use_case.memory_saturation.response import (
    MemorySaturationResponse,
)


class MemorySaturationServicePort(ABC):
    @abstractmethod
    def predict(self, command: MemorySaturationCommand) -> MemorySaturationResponse: ...
