from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.cilium.cilium_encryption_status.cilium_encryption_status_use_case import (  # noqa: E501
    CiliumEncryptionStatusUseCase,
)
from hexawyn.application.use_case.cilium.cilium_encryption_status.command import (
    CiliumEncryptionStatusCommand,
)
from hexawyn.application.use_case.cilium.cilium_encryption_status.response import (
    CiliumEncryptionStatusResponse,
)
from hexawyn.domain.models.cilium import CiliumEncryptionStatusResult


class TestCiliumEncryptionStatusUseCase:
    def test_execute_returns_status(self) -> None:
        result = CiliumEncryptionStatusResult(
            installed=True,
            status="enabled",
            mode="wireguard",
            encrypted_nodes=3,
            total_nodes=4,
            coverage="3/4",
            note=None,
        )
        port = MagicMock()
        port.encryption_status.return_value = result

        response = CiliumEncryptionStatusUseCase(port=port).execute(CiliumEncryptionStatusCommand())

        assert isinstance(response, CiliumEncryptionStatusResponse)
        assert response.mode == "wireguard"
        assert response.coverage == "3/4"

    def test_execute_not_installed(self) -> None:
        result = CiliumEncryptionStatusResult(
            installed=False,
            status="not_installed",
            mode="UNKNOWN",
            encrypted_nodes=0,
            total_nodes=0,
            coverage=None,
            note="Cilium is not installed in this cluster",
        )
        port = MagicMock()
        port.encryption_status.return_value = result

        response = CiliumEncryptionStatusUseCase(port=port).execute(CiliumEncryptionStatusCommand())

        assert response.installed is False
        assert response.status == "not_installed"
