"""CalicoEncryptionStatusUseCase — WireGuard encryption status."""

from __future__ import annotations

from hexawyn.application.ports.driven.calico_port import CalicoPort
from hexawyn.application.use_case.calico.calico_encryption_status.command import (
    CalicoEncryptionStatusCommand,
)
from hexawyn.application.use_case.calico.calico_encryption_status.response import (
    CalicoEncryptionStatusResponse,
)
from hexawyn.domain.models.calico import DataplaneMode
from hexawyn.domain.services.calico.encryption_status_service import (
    build_calico_encryption_status,
)


class CalicoEncryptionStatusUseCase:
    """Orchestrates WireGuard status — depends only on ``CalicoPort``."""

    def __init__(self, port: CalicoPort) -> None:
        self._port = port

    def execute(self, command: CalicoEncryptionStatusCommand) -> CalicoEncryptionStatusResponse:
        detection = self._port.detect()
        if not detection.installed:
            return CalicoEncryptionStatusResponse(
                installed=False,
                not_installed_marker=detection.not_installed_marker,
                wireguard_enabled=None,
                mode=None,
                per_node=[],
                error=detection.error,
            )
        config = self._port.encryption_status()
        result = build_calico_encryption_status(detection=detection, config=config)
        mode = result.mode.value if isinstance(result.mode, DataplaneMode) else result.mode
        return CalicoEncryptionStatusResponse(
            installed=result.installed,
            not_installed_marker=result.not_installed_marker,
            wireguard_enabled=result.wireguard_enabled,
            mode=mode,
            per_node=list(result.per_node),
            summary=result.summary,
            error=result.error,
        )
