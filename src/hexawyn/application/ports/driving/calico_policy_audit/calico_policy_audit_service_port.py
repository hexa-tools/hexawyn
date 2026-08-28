from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.calico.calico_policy_audit.command import (
    CalicoPolicyAuditCommand,
)
from hexawyn.application.use_case.calico.calico_policy_audit.response import (
    CalicoPolicyAuditResponse,
)


class CalicoPolicyAuditServicePort(ABC):
    """Inbound port for the Calico coverage audit."""

    @abstractmethod
    def audit(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse: ...
