from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.security.audit_secret_rotation.command import (
    AuditSecretRotationCommand,
)
from hexawyn.application.use_case.security.audit_secret_rotation.response import (
    AuditSecretRotationResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class AuditSecretRotationServicePort(ABC):
    @abstractmethod
    def audit_secret_rotation(
        self, command: AuditSecretRotationCommand
    ) -> AuditSecretRotationResponse: ...
