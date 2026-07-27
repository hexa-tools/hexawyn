from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.keda.keda_scaledjob_get.command import (  # type: ignore
    KedaScaledJobGetCommand,
)
from hexawyn.application.use_case.keda.keda_scaledjob_get.response import (  # type: ignore
    KedaScaledJobGetResponse,
)


class KedaScaledJobGetServicePort(ABC):
    @abstractmethod
    def get_job(self, command: KedaScaledJobGetCommand) -> KedaScaledJobGetResponse: ...
