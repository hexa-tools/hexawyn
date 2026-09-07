from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.calico.calico_policy_audit.command import (
    CalicoPolicyAuditCommand,
)
from hexawyn.application.use_case.calico.calico_policy_audit.response import (
    CalicoPolicyAuditResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CalicoPolicyAuditServicePort(ABC):
    """Inbound port for the Calico coverage audit."""

    @abstractmethod
    def audit(self, command: CalicoPolicyAuditCommand) -> CalicoPolicyAuditResponse: ...
