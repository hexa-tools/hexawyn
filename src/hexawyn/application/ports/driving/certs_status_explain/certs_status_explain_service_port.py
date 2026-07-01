from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.certs_status_explain.certs_status_explain_command import (
    CertsStatusExplainCommand,
)
from hexawyn.application.ports.driving.certs_status_explain.certs_status_explain_response import (
    CertsStatusExplainResponse,
)


class CertsStatusExplainServicePort(ABC):
    @abstractmethod
    def explain(self, command: CertsStatusExplainCommand) -> CertsStatusExplainResponse: ...
