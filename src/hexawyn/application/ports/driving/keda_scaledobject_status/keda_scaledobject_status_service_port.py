from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.keda_scaledobject_status.keda_scaledobject_status_command import (
    KedaScaledObjectStatusCommand,
)
from hexawyn.application.ports.driving.keda_scaledobject_status.keda_scaledobject_status_response import (
    KedaScaledObjectStatusResponse,
)


class KedaScaledObjectStatusServicePort(ABC):
    @abstractmethod
    def get_status(
        self, command: KedaScaledObjectStatusCommand
    ) -> KedaScaledObjectStatusResponse: ...
