from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.security.audit_rbac_permissions.command import (  # type: ignore
    AuditRBACPermissionsCommand,
)
from hexawyn.application.use_case.security.audit_rbac_permissions.response import (  # type: ignore
    AuditRBACPermissionsResponse,
)


class AuditRBACPermissionsServicePort(ABC):
    @abstractmethod
    def audit_permissions(
        self, command: AuditRBACPermissionsCommand
    ) -> AuditRBACPermissionsResponse: ...
