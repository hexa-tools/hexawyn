from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.audit_secret_rotation.audit_secret_rotation_command import (
    AuditSecretRotationCommand,
)
from hexawyn.application.ports.driving.audit_secret_rotation.audit_secret_rotation_response import (
    AuditSecretRotationResponse,
)
from hexawyn.application.ports.driving.audit_secret_rotation.audit_secret_rotation_service_port import (
    AuditSecretRotationServicePort,
)
from hexawyn.application.use_case.audit_secret_rotation.audit_secret_rotation_use_case import (
    AuditSecretRotationUseCase,
)


class TestAuditSecretRotationUseCase:
    def test_execute_delegates_to_service(self) -> None:
        service = MagicMock(spec=AuditSecretRotationServicePort)
        expected = AuditSecretRotationResponse()
        service.audit_secret_rotation.return_value = expected
        use_case = AuditSecretRotationUseCase(service=service)
        command = AuditSecretRotationCommand()

        result = use_case.execute(command)

        service.audit_secret_rotation.assert_called_once_with(command)
        assert result is expected
