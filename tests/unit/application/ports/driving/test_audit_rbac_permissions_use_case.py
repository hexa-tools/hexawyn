from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.audit_rbac_permissions.audit_rbac_permissions_command import (
    AuditRBACPermissionsCommand,
)
from hexawyn.application.ports.driving.audit_rbac_permissions.audit_rbac_permissions_response import (
    AuditRBACPermissionsResponse,
)
from hexawyn.application.ports.driving.audit_rbac_permissions.audit_rbac_permissions_service_port import (
    AuditRBACPermissionsServicePort,
)
from hexawyn.application.use_case.audit_rbac_permissions.audit_rbac_permissions_use_case import (
    AuditRBACPermissionsUseCase,
)


class TestAuditRBACPermissionsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        service = MagicMock(spec=AuditRBACPermissionsServicePort)
        expected = AuditRBACPermissionsResponse()
        service.audit_permissions.return_value = expected
        use_case = AuditRBACPermissionsUseCase(service=service)
        command = AuditRBACPermissionsCommand()

        result = use_case.execute(command)

        service.audit_permissions.assert_called_once_with(command)
        assert result is expected
