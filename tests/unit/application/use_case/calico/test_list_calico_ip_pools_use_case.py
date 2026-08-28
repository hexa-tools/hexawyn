"""Tests for the ListCalicoIpPools use case."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.use_case.calico.list_calico_ip_pools.command import (
    ListCalicoIpPoolsCommand,
)
from hexawyn.application.use_case.calico.list_calico_ip_pools.list_calico_ip_pools_use_case import (
    ListCalicoIpPoolsUseCase,
)
from hexawyn.application.use_case.calico.list_calico_ip_pools.response import (
    ListCalicoIpPoolsResponse,
)
from hexawyn.domain.errors import InsufficientPermissionsError
from hexawyn.domain.models.calico import (
    CalicoDetectionResult,
    CalicoDetectionStatus,
    CalicoIPPool,
    DataplaneMode,
)


class TestListCalicoIpPoolsUseCase:
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

    def test_execute_lists_pools(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection()
        port.list_ip_pools.return_value = [
            CalicoIPPool(
                name="pool-1",
                cidr="10.1.0.0/16",
                ipip_mode="Always",
                vxlan_mode="Never",
                disabled=False,
                nat_outgoing=True,
                node_selector="all()",
            )
        ]

        result = ListCalicoIpPoolsUseCase(port=port).execute(ListCalicoIpPoolsCommand())

        assert isinstance(result, ListCalicoIpPoolsResponse)
        assert result.installed is True
        assert result.total == 1  # noqa: PLR2004
        assert result.pools[0].cidr == "10.1.0.0/16"
        assert result.pools[0].nat_outgoing is True

    def test_execute_empty_pools(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection()
        port.list_ip_pools.return_value = []

        result = ListCalicoIpPoolsUseCase(port=port).execute(ListCalicoIpPoolsCommand())

        assert result.installed is True
        assert result.total == 0
        assert result.pools == []

    def test_execute_not_installed(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection(installed=False)

        result = ListCalicoIpPoolsUseCase(port=port).execute(ListCalicoIpPoolsCommand())

        assert result.installed is False
        assert result.not_installed_marker == "NOT_INSTALLED"
        assert result.pools == []

    def test_rbac_forbidden_propagates(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection()
        port.list_ip_pools.side_effect = InsufficientPermissionsError("denied")

        with pytest.raises(InsufficientPermissionsError):
            ListCalicoIpPoolsUseCase(port=port).execute(ListCalicoIpPoolsCommand())
