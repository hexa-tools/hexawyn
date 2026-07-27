from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.security.audit_rbac_permissions.command import (
    AuditRbacPermissionsCommand,
)
from hexawyn.application.use_case.security.audit_rbac_permissions.response import (
    AuditRbacPermissionsResponse,
)


class TestAuditRbacPermissionsUseCase:
    """RED phase — will fail until use case is properly wired."""

    def test_execute_returns_response_with_empty_cluster(self) -> None:
        from hexawyn.application.use_case.security.audit_rbac_permissions.audit_rbac_permissions_use_case import (  # noqa: E501
            AuditRbacPermissionsUseCase,
        )

        port = MagicMock()
        port.list_service_accounts.return_value = []
        port.list_role_bindings.return_value = []
        port.list_roles.return_value = []
        port.list_pods_by_service_account.return_value = []
        port.fetch_api_usage.return_value = {"events": [], "available": []}

        use_case = AuditRbacPermissionsUseCase(rbac_port=port)
        result = use_case.audit_permissions(AuditRbacPermissionsCommand(window_days=30))

        assert isinstance(result, AuditRbacPermissionsResponse)
        assert result.total_service_accounts_checked == 0

    def test_execute_excludes_system_namespace_service_accounts(self) -> None:
        from hexawyn.application.use_case.security.audit_rbac_permissions.audit_rbac_permissions_use_case import (  # noqa: E501
            AuditRbacPermissionsUseCase,
        )

        port = MagicMock()
        port.list_service_accounts.return_value = [
            {"name": "default", "namespace": "kube-system", "annotations": {}},
        ]
        port.list_role_bindings.return_value = []
        port.list_roles.return_value = []
        port.list_pods_by_service_account.return_value = []
        port.fetch_api_usage.return_value = {"events": [], "available": []}

        use_case = AuditRbacPermissionsUseCase(rbac_port=port)
        result = use_case.audit_permissions(AuditRbacPermissionsCommand())

        assert result.total_service_accounts_checked == 1
        assert len(result.excluded_system_service_accounts) == 1

    def test_execute_detects_unused_service_account(self) -> None:
        from hexawyn.application.use_case.security.audit_rbac_permissions.audit_rbac_permissions_use_case import (  # noqa: E501
            AuditRbacPermissionsUseCase,
        )

        port = MagicMock()
        port.list_service_accounts.return_value = [
            {"name": "unused-sa", "namespace": "default", "annotations": {}},
        ]
        port.list_role_bindings.return_value = []
        port.list_roles.return_value = []
        port.list_pods_by_service_account.return_value = []
        port.fetch_api_usage.return_value = {"events": [], "available": []}

        use_case = AuditRbacPermissionsUseCase(rbac_port=port)
        result = use_case.audit_permissions(AuditRbacPermissionsCommand())

        assert len(result.unused_service_accounts) == 1
        assert result.unused_service_accounts[0]["name"] == "unused-sa"
