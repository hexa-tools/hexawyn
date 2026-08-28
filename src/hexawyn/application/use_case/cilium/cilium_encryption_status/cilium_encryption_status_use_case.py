from __future__ import annotations

from hexawyn.application.ports.driven.cilium_port import CiliumPort
from hexawyn.application.use_case.cilium.cilium_encryption_status.command import (
    CiliumEncryptionStatusCommand,
)
from hexawyn.application.use_case.cilium.cilium_encryption_status.response import (
    CiliumEncryptionStatusResponse,
)


class CiliumEncryptionStatusUseCase:
    def __init__(self, port: CiliumPort) -> None:
        self._port = port

    def execute(self, command: CiliumEncryptionStatusCommand) -> CiliumEncryptionStatusResponse:
        result = self._port.encryption_status()
        return CiliumEncryptionStatusResponse(
            installed=result.installed,
            status=result.status,
            mode=result.mode,
            encrypted_nodes=result.encrypted_nodes,
            total_nodes=result.total_nodes,
            coverage=result.coverage,
            note=result.note,
        )
