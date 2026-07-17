"""Unit tests for AuditRBACPermissionsUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.audit_rbac_permissions.audit_rbac_permissions_service_port import (
    AuditRBACPermissionsServicePort,
)
from hexawyn.application.use_case.audit_rbac_permissions.audit_rbac_permissions_use_case import (
    AuditRBACPermissionsUseCase,
)


class TestAuditRBACPermissionsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=AuditRBACPermissionsServicePort)
        use_case = AuditRBACPermissionsUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.audit_permissions.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=AuditRBACPermissionsServicePort)
        mock_service.audit_permissions.side_effect = RuntimeError("test error")
        use_case = AuditRBACPermissionsUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
