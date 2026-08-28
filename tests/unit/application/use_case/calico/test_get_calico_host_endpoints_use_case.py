"""Tests for the GetCalicoHostEndpoints use case."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.use_case.calico.get_calico_host_endpoints.command import (
    GetCalicoHostEndpointsCommand,
)
from hexawyn.application.use_case.calico.get_calico_host_endpoints.get_calico_host_endpoints_use_case import (  # noqa: E501
    GetCalicoHostEndpointsUseCase,
)
from hexawyn.application.use_case.calico.get_calico_host_endpoints.response import (
    GetCalicoHostEndpointsResponse,
)
from hexawyn.domain.errors import InsufficientPermissionsError
from hexawyn.domain.models.calico import (
    CalicoDetectionResult,
    CalicoDetectionStatus,
    CalicoHostEndpoint,
    DataplaneMode,
)


class TestGetCalicoHostEndpointsUseCase:
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
            total_nodes=1,
            ready_agents=1,
            degraded_agents=0,
            degraded_summary=None,
            error=None,
        )

    def test_execute_lists_endpoints(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection()
        port.list_host_endpoints.return_value = [
            CalicoHostEndpoint(
                name="he",
                node="node-1",
                interface_name="eth0",
                expected_ip="10.0.0.1",
                expected_ips=("10.0.0.1",),
                labels=(("kubernetes.io/hostname", "node-1"),),
                applied_policies=("default.host-endpoints",),
            )
        ]

        result = GetCalicoHostEndpointsUseCase(port=port).execute(GetCalicoHostEndpointsCommand())

        assert isinstance(result, GetCalicoHostEndpointsResponse)
        assert result.installed is True
        assert result.total == 1  # noqa: PLR2004
        assert result.endpoints[0].expected_ip == "10.0.0.1"
        assert result.endpoints[0].applied_policies == ("default.host-endpoints",)

    def test_execute_empty(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection()
        port.list_host_endpoints.return_value = []

        result = GetCalicoHostEndpointsUseCase(port=port).execute(GetCalicoHostEndpointsCommand())

        assert result.installed is True
        assert result.total == 0
        assert result.endpoints == []

    def test_execute_not_installed(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection(installed=False)

        result = GetCalicoHostEndpointsUseCase(port=port).execute(GetCalicoHostEndpointsCommand())

        assert result.installed is False
        assert result.not_installed_marker == "NOT_INSTALLED"
        assert result.endpoints == []

    def test_rbac_forbidden_propagates(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection()
        port.list_host_endpoints.side_effect = InsufficientPermissionsError("denied")

        with pytest.raises(InsufficientPermissionsError):
            GetCalicoHostEndpointsUseCase(port=port).execute(GetCalicoHostEndpointsCommand())
