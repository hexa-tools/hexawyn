from __future__ import annotations


class TestAuditRBACPermissionsCommand:
    def test_defaults_window_days_to_thirty(self) -> None:
        from hexawyn.application.ports.driving.audit_rbac_permissions.audit_rbac_permissions_command import (
            AuditRBACPermissionsCommand,
        )

        command = AuditRBACPermissionsCommand()

        assert command.window_days == 30

    def test_accepts_custom_window_days(self) -> None:
        from hexawyn.application.ports.driving.audit_rbac_permissions.audit_rbac_permissions_command import (
            AuditRBACPermissionsCommand,
        )

        command = AuditRBACPermissionsCommand(window_days=7)

        assert command.window_days == 7
