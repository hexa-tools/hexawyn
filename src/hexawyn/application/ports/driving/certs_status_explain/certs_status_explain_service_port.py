from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cert_manager.certs_status_explain.command import (
    CertsStatusExplainCommand,
)
from hexawyn.application.use_case.cert_manager.certs_status_explain.response import (
    CertsStatusExplainResponse,
)


class CertsStatusExplainServicePort(ABC):
    @abstractmethod
    def explain(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse: ...
