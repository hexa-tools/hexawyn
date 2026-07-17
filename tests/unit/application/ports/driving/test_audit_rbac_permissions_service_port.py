from __future__ import annotations

from abc import ABC

import pytest


class TestAuditRBACPermissionsServicePort:
    def test_is_abstract(self) -> None:
        from hexawyn.application.ports.driving.audit_rbac_permissions.audit_rbac_permissions_service_port import (
            AuditRBACPermissionsServicePort,
        )

        assert issubclass(AuditRBACPermissionsServicePort, ABC)

    def test_cannot_instantiate(self) -> None:
        from hexawyn.application.ports.driving.audit_rbac_permissions.audit_rbac_permissions_service_port import (
            AuditRBACPermissionsServicePort,
        )

        with pytest.raises(TypeError):
            AuditRBACPermissionsServicePort()  # type: ignore[abstract]
