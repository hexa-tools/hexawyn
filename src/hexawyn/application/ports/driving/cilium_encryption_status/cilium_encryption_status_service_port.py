from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cilium.cilium_encryption_status.command import (
    CiliumEncryptionStatusCommand,
)
from hexawyn.application.use_case.cilium.cilium_encryption_status.response import (
    CiliumEncryptionStatusResponse,
)


class CiliumEncryptionStatusServicePort(ABC):
    @abstractmethod
    def encrypt(self, command: CiliumEncryptionStatusCommand) -> CiliumEncryptionStatusResponse: ...
