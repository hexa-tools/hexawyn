from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.memory_saturation.memory_saturation_command import (
    MemorySaturationCommand,
)
from hexawyn.application.ports.driving.memory_saturation.memory_saturation_response import (
    MemorySaturationResponse,
)


class MemorySaturationServicePort(ABC):
    @abstractmethod
    def predict(self, command: MemorySaturationCommand) -> MemorySaturationResponse: ...
