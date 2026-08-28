"""Tests for the CalicoFelixMetrics use case."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.use_case.calico.calico_felix_metrics.calico_felix_metrics_use_case import (
    CalicoFelixMetricsUseCase,
)
from hexawyn.application.use_case.calico.calico_felix_metrics.command import (
    CalicoFelixMetricsCommand,
)
from hexawyn.application.use_case.calico.calico_felix_metrics.response import (
    CalicoFelixMetricsResponse,
)
from hexawyn.domain.errors import InsufficientPermissionsError
from hexawyn.domain.models.calico import (
    CalicoDetectionResult,
    CalicoDetectionStatus,
    DataplaneMode,
)


class TestCalicoFelixMetricsUseCase:
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

    def test_execute_returns_denies(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection()
        port.felix_policy_counters.return_value = {
            "available": True,
            "samples": [{"policy": "a", "kind": "deny_packets", "value": 10}],
        }

        result = CalicoFelixMetricsUseCase(port=port).execute(CalicoFelixMetricsCommand())

        assert isinstance(result, CalicoFelixMetricsResponse)
        assert result.installed is True
        assert result.metrics_available is True
        assert result.total_denies == 10  # noqa: PLR2004

    def test_execute_metrics_down(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection()
        port.felix_policy_counters.return_value = {
            "available": False,
            "message": "prometheus unreachable",
            "samples": [],
        }

        result = CalicoFelixMetricsUseCase(port=port).execute(CalicoFelixMetricsCommand())

        assert result.metrics_available is False
        assert result.metrics_message == "prometheus unreachable"

    def test_execute_not_installed(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection(installed=False)

        result = CalicoFelixMetricsUseCase(port=port).execute(CalicoFelixMetricsCommand())

        assert result.installed is False
        assert result.not_installed_marker == "NOT_INSTALLED"

    def test_rbac_forbidden_propagates(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection()
        port.felix_policy_counters.side_effect = InsufficientPermissionsError("denied")

        with pytest.raises(InsufficientPermissionsError):
            CalicoFelixMetricsUseCase(port=port).execute(CalicoFelixMetricsCommand())
