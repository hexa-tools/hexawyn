from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cilium.cilium_encryption_status.command import (
    CiliumEncryptionStatusCommand,
)
from hexawyn.application.use_case.cilium.cilium_encryption_status.response import (
    CiliumEncryptionStatusResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CiliumEncryptionStatusServicePort(ABC):
    @abstractmethod
    def encrypt(self, command: CiliumEncryptionStatusCommand) -> CiliumEncryptionStatusResponse: ...
