from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cert_manager.certs_requests_list.command import (
    CertsRequestsListCommand,
)
from hexawyn.application.use_case.cert_manager.certs_requests_list.response import (
    CertsRequestsListResponse,
)


class CertsRequestsListServicePort(ABC):
    @abstractmethod
    def list_requests(self, command: CertsRequestsListCommand) -> CertsRequestsListResponse: ...
