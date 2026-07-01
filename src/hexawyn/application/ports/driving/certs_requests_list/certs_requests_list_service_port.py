from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.certs_requests_list.certs_requests_list_command import (
    CertsRequestsListCommand,
)
from hexawyn.application.ports.driving.certs_requests_list.certs_requests_list_response import (
    CertsRequestsListResponse,
)


class CertsRequestsListServicePort(ABC):
    @abstractmethod
    def list_requests(self, command: CertsRequestsListCommand) -> CertsRequestsListResponse: ...
