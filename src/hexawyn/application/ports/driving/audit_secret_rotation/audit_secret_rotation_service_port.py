from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.security.audit_secret_rotation.command import (
    AuditSecretRotationCommand,
)
from hexawyn.application.use_case.security.audit_secret_rotation.response import (
    AuditSecretRotationResponse,
)


class AuditSecretRotationServicePort(ABC):
    @abstractmethod
    def audit_secret_rotation(
        self, command: AuditSecretRotationCommand
    ) -> AuditSecretRotationResponse: ...
