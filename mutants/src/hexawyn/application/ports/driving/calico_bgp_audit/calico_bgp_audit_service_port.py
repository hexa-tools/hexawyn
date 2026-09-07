from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.calico.calico_bgp_audit.command import CalicoBgpAuditCommand
from hexawyn.application.use_case.calico.calico_bgp_audit.response import CalicoBgpAuditResponse


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CalicoBgpAuditServicePort(ABC):
    """Inbound port for the Calico BGP audit."""

    @abstractmethod
    def audit(self, command: CalicoBgpAuditCommand) -> CalicoBgpAuditResponse: ...
