from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.keda_detect.keda_detect_command import KedaDetectCommand
from hexawyn.application.ports.driving.keda_detect.keda_detect_response import KedaDetectResponse


class KedaDetectServicePort(ABC):
    @abstractmethod
    def detect(self, command: KedaDetectCommand) -> KedaDetectResponse: ...
