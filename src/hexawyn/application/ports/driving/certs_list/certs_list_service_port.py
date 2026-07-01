from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.certs_list.certs_list_command import CertsListCommand
from hexawyn.application.ports.driving.certs_list.certs_list_response import CertsListResponse


class CertsListServicePort(ABC):
    @abstractmethod
    def list_certs(self, command: CertsListCommand) -> CertsListResponse: ...
