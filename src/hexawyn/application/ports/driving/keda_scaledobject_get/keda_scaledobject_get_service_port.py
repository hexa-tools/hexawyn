from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.keda_scaledobject_get.keda_scaledobject_get_command import (
    KedaScaledObjectGetCommand,
)
from hexawyn.application.ports.driving.keda_scaledobject_get.keda_scaledobject_get_response import (
    KedaScaledObjectGetResponse,
)


class KedaScaledObjectGetServicePort(ABC):
    @abstractmethod
    def get_object(self, command: KedaScaledObjectGetCommand) -> KedaScaledObjectGetResponse: ...
