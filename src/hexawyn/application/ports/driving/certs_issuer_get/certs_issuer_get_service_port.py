from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cert_manager.certs_issuer_get.command import (
    CertsIssuerGetCommand,
)
from hexawyn.application.use_case.cert_manager.certs_issuer_get.response import (
    CertsIssuerGetResponse,
)


class CertsIssuerGetServicePort(ABC):
    @abstractmethod
    def get_issuer(self, command: CertsIssuerGetCommand) -> CertsIssuerGetResponse: ...
