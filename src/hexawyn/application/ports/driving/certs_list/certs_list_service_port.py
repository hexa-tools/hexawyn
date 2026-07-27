from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cert_manager.certs_list.command import (
    CertsListCommand,
)
from hexawyn.application.use_case.cert_manager.certs_list.response import (
    CertsListResponse,
)


class CertsListServicePort(ABC):
    @abstractmethod
    def list_certs(self, command: CertsListCommand) -> CertsListResponse: ...
