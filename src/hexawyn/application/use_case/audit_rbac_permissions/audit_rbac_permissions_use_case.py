from __future__ import annotations

from hexawyn.application.ports.driving.audit_rbac_permissions.audit_rbac_permissions_command import (
    AuditRBACPermissionsCommand,
)
from hexawyn.application.ports.driving.audit_rbac_permissions.audit_rbac_permissions_response import (
    AuditRBACPermissionsResponse,
)
from hexawyn.application.ports.driving.audit_rbac_permissions.audit_rbac_permissions_service_port import (
    AuditRBACPermissionsServicePort,
)


class AuditRBACPermissionsUseCase:
    def __init__(self, service: AuditRBACPermissionsServicePort) -> None:
        self._svc = service

    def execute(self, command: AuditRBACPermissionsCommand) -> AuditRBACPermissionsResponse:
        return self._svc.audit_permissions(command)
