from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.audit_rbac_permissions.audit_rbac_permissions_command import (
    AuditRBACPermissionsCommand,
)
from hexawyn.application.ports.driving.audit_rbac_permissions.audit_rbac_permissions_response import (
    AuditRBACPermissionsResponse,
)


class AuditRBACPermissionsServicePort(ABC):
    @abstractmethod
    def audit_permissions(
        self, command: AuditRBACPermissionsCommand
    ) -> AuditRBACPermissionsResponse: ...
