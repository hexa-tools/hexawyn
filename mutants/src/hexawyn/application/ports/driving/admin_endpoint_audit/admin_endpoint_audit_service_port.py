from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.security.admin_endpoint_audit.command import (
    AdminEndpointAuditCommand,
)
from hexawyn.application.use_case.security.admin_endpoint_audit.response import (
    AdminEndpointAuditResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class AdminEndpointAuditServicePort(ABC):
    @abstractmethod
    def audit(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse: ...
