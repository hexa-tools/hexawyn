"""Tests for the CalicoEncryptionStatus use case."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.use_case.calico.calico_encryption_status.calico_encryption_status_use_case import (  # noqa: E501
    CalicoEncryptionStatusUseCase,
)
from hexawyn.application.use_case.calico.calico_encryption_status.command import (
    CalicoEncryptionStatusCommand,
)
from hexawyn.application.use_case.calico.calico_encryption_status.response import (
    CalicoEncryptionStatusResponse,
)
from hexawyn.domain.errors import InsufficientPermissionsError
from hexawyn.domain.models.calico import (
    CalicoDetectionResult,
    CalicoDetectionStatus,
    DataplaneMode,
)


class TestCalicoEncryptionStatusUseCase:
    def _detection(self, installed: bool = True) -> CalicoDetectionResult:
        return CalicoDetectionResult(
            installed=installed,
            status=(
                CalicoDetectionStatus.INSTALLED
                if installed
                else CalicoDetectionStatus.NOT_INSTALLED
            ),
            not_installed_marker=None if installed else "NOT_INSTALLED",
            version="v3.26.1",
            mode=DataplaneMode.IPIP,
            namespace="calico-system",
            tigera_operator=False,
            enterprise=False,
            agents=[],
            total_nodes=3,
            ready_agents=3,
            degraded_agents=0,
            degraded_summary=None,
            error=None,
        )

    def test_execute_wireguard_on(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection()
        port.encryption_status.return_value = {"wireguard_enabled": True, "per_node": []}

        result = CalicoEncryptionStatusUseCase(port=port).execute(CalicoEncryptionStatusCommand())

        assert isinstance(result, CalicoEncryptionStatusResponse)
        assert result.installed is True
        assert result.wireguard_enabled is True
        assert result.mode == "IPIP"

    def test_execute_wireguard_off(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection()
        port.encryption_status.return_value = {"wireguard_enabled": False, "per_node": []}

        result = CalicoEncryptionStatusUseCase(port=port).execute(CalicoEncryptionStatusCommand())

        assert result.wireguard_enabled is False

    def test_execute_not_installed(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection(installed=False)

        result = CalicoEncryptionStatusUseCase(port=port).execute(CalicoEncryptionStatusCommand())

        assert result.installed is False
        assert result.not_installed_marker == "NOT_INSTALLED"
        assert result.wireguard_enabled is None

    def test_rbac_forbidden_propagates(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection()
        port.encryption_status.side_effect = InsufficientPermissionsError("denied")

        with pytest.raises(InsufficientPermissionsError):
            CalicoEncryptionStatusUseCase(port=port).execute(CalicoEncryptionStatusCommand())
