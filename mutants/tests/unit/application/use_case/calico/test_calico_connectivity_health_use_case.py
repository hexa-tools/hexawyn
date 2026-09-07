"""Tests for the CalicoConnectivityHealth use case."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.use_case.calico.calico_connectivity_health.calico_connectivity_health_use_case import (  # noqa: E501
    CalicoConnectivityHealthUseCase,
)
from hexawyn.application.use_case.calico.calico_connectivity_health.command import (
    CalicoConnectivityHealthCommand,
)
from hexawyn.application.use_case.calico.calico_connectivity_health.response import (
    CalicoConnectivityHealthResponse,
)
from hexawyn.domain.errors import InsufficientPermissionsError
from hexawyn.domain.models.calico import (
    CalicoAgentPhase,
    CalicoDetectionResult,
    CalicoDetectionStatus,
    CalicoNodeAgent,
    DataplaneMode,
)


class TestCalicoConnectivityHealthUseCase:
    def _detection(self, installed: bool = True) -> CalicoDetectionResult:
        agent = CalicoNodeAgent(
            node="node-1",
            phase=CalicoAgentPhase.READY,
            ready=True,
            ready_replicas=1,
            desired_replicas=1,
            available_replicas=1,
        )
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
            agents=[agent] if installed else [],
            total_nodes=1 if installed else 0,
            ready_agents=1 if installed else 0,
            degraded_agents=0,
            degraded_summary=None,
            error=None,
        )

    def test_execute_returns_health(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection()
        port.connectivity_health.return_value = {"available": True, "status": "healthy"}

        result = CalicoConnectivityHealthUseCase(port=port).execute(
            CalicoConnectivityHealthCommand()
        )

        assert isinstance(result, CalicoConnectivityHealthResponse)
        assert result.installed is True
        assert result.verdict == "healthy"
        assert result.tunnel_summary == "IPIP tunnel"
        assert result.connectivity_probe == "healthy"

    def test_execute_not_installed(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection(installed=False)

        result = CalicoConnectivityHealthUseCase(port=port).execute(
            CalicoConnectivityHealthCommand()
        )

        assert result.installed is False
        assert result.not_installed_marker == "NOT_INSTALLED"
        assert result.verdict == "unknown"

    def test_rbac_forbidden_propagates(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection()
        port.connectivity_health.side_effect = InsufficientPermissionsError("denied")

        with pytest.raises(InsufficientPermissionsError):
            CalicoConnectivityHealthUseCase(port=port).execute(CalicoConnectivityHealthCommand())
