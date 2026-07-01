from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.certs_get.certs_get_command import CertsGetCommand
from hexawyn.application.ports.driving.certs_get.certs_get_response import CertsGetResponse


class CertsGetServicePort(ABC):
    @abstractmethod
    def get_cert(self, command: CertsGetCommand) -> CertsGetResponse: ...
