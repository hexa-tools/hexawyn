from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.certs_issuer_get.certs_issuer_get_command import (
    CertsIssuerGetCommand,
)
from hexawyn.application.ports.driving.certs_issuer_get.certs_issuer_get_response import (
    CertsIssuerGetResponse,
)


class CertsIssuerGetServicePort(ABC):
    @abstractmethod
    def get_issuer(self, command: CertsIssuerGetCommand) -> CertsIssuerGetResponse: ...
