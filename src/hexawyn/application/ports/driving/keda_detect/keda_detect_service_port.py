from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.keda.keda_detect.command import (
    KedaDetectCommand,
)
from hexawyn.application.use_case.keda.keda_detect.response import (
    KedaDetectResponse,
)


class KedaDetectServicePort(ABC):
    @abstractmethod
    def detect(self, command: KedaDetectCommand) -> KedaDetectResponse: ...
