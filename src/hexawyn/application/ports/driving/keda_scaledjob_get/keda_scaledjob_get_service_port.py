from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.keda_scaledjob_get.keda_scaledjob_get_command import (
    KedaScaledJobGetCommand,
)
from hexawyn.application.ports.driving.keda_scaledjob_get.keda_scaledjob_get_response import (
    KedaScaledJobGetResponse,
)


class KedaScaledJobGetServicePort(ABC):
    @abstractmethod
    def get_job(self, command: KedaScaledJobGetCommand) -> KedaScaledJobGetResponse: ...
