from __future__ import annotations

from hexawyn.application.ports.driving.audit_secret_rotation.audit_secret_rotation_command import (
    AuditSecretRotationCommand,
)
from hexawyn.application.ports.driving.audit_secret_rotation.audit_secret_rotation_response import (
    AuditSecretRotationResponse,
)
from hexawyn.application.ports.driving.audit_secret_rotation.audit_secret_rotation_service_port import (
    AuditSecretRotationServicePort,
)


class AuditSecretRotationUseCase:
    def __init__(self, service: AuditSecretRotationServicePort) -> None:
        self._svc = service

    def execute(self, command: AuditSecretRotationCommand) -> AuditSecretRotationResponse:
        return self._svc.audit_secret_rotation(command)
