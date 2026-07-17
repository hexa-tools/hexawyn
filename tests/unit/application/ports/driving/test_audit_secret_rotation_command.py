from __future__ import annotations


class TestAuditSecretRotationCommand:
    def test_defaults_rotation_threshold_days_to_ninety(self) -> None:
        from hexawyn.application.ports.driving.audit_secret_rotation.audit_secret_rotation_command import (
            AuditSecretRotationCommand,
        )

        command = AuditSecretRotationCommand()

        assert command.rotation_threshold_days == 90

    def test_accepts_custom_rotation_threshold_days(self) -> None:
        from hexawyn.application.ports.driving.audit_secret_rotation.audit_secret_rotation_command import (
            AuditSecretRotationCommand,
        )

        command = AuditSecretRotationCommand(rotation_threshold_days=30)

        assert command.rotation_threshold_days == 30
