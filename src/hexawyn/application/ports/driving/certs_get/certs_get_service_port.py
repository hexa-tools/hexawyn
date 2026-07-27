from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cert_manager.certs_get.command import (
    CertsGetCommand,
)
from hexawyn.application.use_case.cert_manager.certs_get.response import (
    CertsGetResponse,
)


class CertsGetServicePort(ABC):
    @abstractmethod
    def get_cert(self, command: CertsGetCommand) -> CertsGetResponse: ...
