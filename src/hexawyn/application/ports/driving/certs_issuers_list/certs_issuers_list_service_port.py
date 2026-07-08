from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.certs_issuers_list.certs_issuers_list_command import (
    CertsIssuersListCommand,
)
from hexawyn.application.ports.driving.certs_issuers_list.certs_issuers_list_response import (
    CertsIssuersListResponse,
)


class CertsIssuersListServicePort(ABC):
    @abstractmethod
    def list_issuers(self, command: CertsIssuersListCommand) -> CertsIssuersListResponse: ...
