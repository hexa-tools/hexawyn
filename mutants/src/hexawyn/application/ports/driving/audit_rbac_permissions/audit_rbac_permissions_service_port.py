from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.security.audit_rbac_permissions.command import (  # type: ignore
    AuditRBACPermissionsCommand,
)
from hexawyn.application.use_case.security.audit_rbac_permissions.response import (  # type: ignore
    AuditRBACPermissionsResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class AuditRBACPermissionsServicePort(ABC):
    @abstractmethod
    def audit_permissions(
        self, command: AuditRBACPermissionsCommand
    ) -> AuditRBACPermissionsResponse: ...
