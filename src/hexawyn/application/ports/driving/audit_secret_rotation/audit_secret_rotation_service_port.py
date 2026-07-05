from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.audit_secret_rotation.audit_secret_rotation_command import (
    AuditSecretRotationCommand,
)
from hexawyn.application.ports.driving.audit_secret_rotation.audit_secret_rotation_response import (
    AuditSecretRotationResponse,
)


class AuditSecretRotationServicePort(ABC):
    @abstractmethod
    def audit_secret_rotation(
        self, command: AuditSecretRotationCommand
    ) -> AuditSecretRotationResponse: ...
