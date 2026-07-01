from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.certs_detect.certs_detect_command import CertsDetectCommand
from hexawyn.application.ports.driving.certs_detect.certs_detect_response import CertsDetectResponse


class CertsDetectServicePort(ABC):
    @abstractmethod
    def detect(self, command: CertsDetectCommand) -> CertsDetectResponse: ...
