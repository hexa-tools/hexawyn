from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.calico.calico_encryption_status.command import (
    CalicoEncryptionStatusCommand,
)
from hexawyn.application.use_case.calico.calico_encryption_status.response import (
    CalicoEncryptionStatusResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CalicoEncryptionStatusServicePort(ABC):
    """Inbound port for the Calico WireGuard encryption status."""

    @abstractmethod
    def encryption_status(
        self, command: CalicoEncryptionStatusCommand
    ) -> CalicoEncryptionStatusResponse: ...
