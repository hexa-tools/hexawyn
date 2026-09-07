"""Tests for the GetCalicoStatus use case — composes status/connectivity/felix."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.use_case.calico.get_calico_status.command import (
    GetCalicoStatusCommand,
)
from hexawyn.application.use_case.calico.get_calico_status.get_calico_status_use_case import (
    GetCalicoStatusUseCase,
)
from hexawyn.application.use_case.calico.get_calico_status.response import (
    GetCalicoStatusResponse,
)
from hexawyn.domain.errors import InsufficientPermissionsError
from hexawyn.domain.models.calico import (
    CalicoDetectionResult,
    CalicoDetectionStatus,
    DataplaneMode,
)


class TestGetCalicoStatusUseCase:
    def _detection(self, **overrides: object) -> CalicoDetectionResult:
        base: dict[str, object] = {
            "installed": True,
            "status": CalicoDetectionStatus.INSTALLED,
            "not_installed_marker": None,
            "version": "v3.26.1",
            "mode": DataplaneMode.IPIP,
            "namespace": "calico-system",
            "tigera_operator": False,
            "enterprise": False,
            "agents": [],
            "total_nodes": 2,
            "ready_agents": 2,
            "degraded_agents": 0,
            "degraded_summary": None,
            "error": None,
        }
        base.update(overrides)
        return CalicoDetectionResult(**base)  # type: ignore[arg-type]

    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.status.return_value = self._detection()
        port.connectivity_health.return_value = {"available": True, "status": "healthy"}
        port.felix_metrics.return_value = {"available": True, "metrics": {}}

        result = GetCalicoStatusUseCase(port=port).execute(GetCalicoStatusCommand())

        assert isinstance(result, GetCalicoStatusResponse)
        assert result.installed is True
        assert result.status == "installed"
        assert result.ready_agents == 2  # noqa: PLR2004
        assert result.total_agents == 2  # noqa: PLR2004

    def test_execute_not_installed(self) -> None:
        port = MagicMock()
        port.status.return_value = self._detection(
            installed=False,
            status=CalicoDetectionStatus.NOT_INSTALLED,
            not_installed_marker="NOT_INSTALLED",
            total_nodes=0,
            ready_agents=0,
        )
        port.connectivity_health.return_value = {"available": False}
        port.felix_metrics.return_value = {"available": False}

        result = GetCalicoStatusUseCase(port=port).execute(GetCalicoStatusCommand())

        assert result.installed is False
        assert result.not_installed_marker == "NOT_INSTALLED"

    def test_execute_degraded(self) -> None:
        port = MagicMock()
        port.status.return_value = self._detection(
            status=CalicoDetectionStatus.DEGRADED,
            total_nodes=2,
            ready_agents=1,
            degraded_agents=1,
            degraded_summary="1/2 calico-node agents ready (1 degraded)",
        )
        port.connectivity_health.return_value = {"available": True, "status": "degraded"}
        port.felix_metrics.return_value = {"available": True, "metrics": {"felix_error": 2.0}}

        result = GetCalicoStatusUseCase(port=port).execute(GetCalicoStatusCommand())

        assert result.status == "degraded"
        assert result.degraded_summary is not None

    def test_execute_surfaces_error(self) -> None:
        port = MagicMock()
        port.status.return_value = self._detection(error="boom")
        port.connectivity_health.return_value = {"available": False}
        port.felix_metrics.return_value = {"available": False}

        result = GetCalicoStatusUseCase(port=port).execute(GetCalicoStatusCommand())

        assert result.error == "boom"

    def test_rbac_forbidden_propagates(self) -> None:
        port = MagicMock()
        port.status.side_effect = InsufficientPermissionsError("denied")
        with pytest.raises(InsufficientPermissionsError):
            GetCalicoStatusUseCase(port=port).execute(GetCalicoStatusCommand())
