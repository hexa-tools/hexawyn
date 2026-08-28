"""Tests for the CalicoBgpAudit use case."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.use_case.calico.calico_bgp_audit.calico_bgp_audit_use_case import (
    CalicoBgpAuditUseCase,
)
from hexawyn.application.use_case.calico.calico_bgp_audit.command import CalicoBgpAuditCommand
from hexawyn.application.use_case.calico.calico_bgp_audit.response import CalicoBgpAuditResponse
from hexawyn.domain.errors import InsufficientPermissionsError
from hexawyn.domain.models.calico import (
    CalicoBgpConfiguration,
    CalicoBgpPeer,
    CalicoDetectionResult,
    CalicoDetectionStatus,
    DataplaneMode,
)


class TestCalicoBgpAuditUseCase:
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

    def test_execute_returns_bgp_audit(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection()
        port.list_bgp_configurations.return_value = [
            CalicoBgpConfiguration(
                name="default",
                as_number="64512",
                node_to_node_mesh_enabled=True,
                service_cluster_ips=("10.96.0.0/16",),
            )
        ]
        port.list_bgp_peers.return_value = [
            CalicoBgpPeer(name="p1", peer_ip="10.0.0.2", as_number="64513", node_selector="all()"),
        ]

        result = CalicoBgpAuditUseCase(port=port).execute(CalicoBgpAuditCommand())

        assert isinstance(result, CalicoBgpAuditResponse)
        assert result.installed is True
        assert result.as_number == "64512"
        assert result.peer_count == 1  # noqa: PLR2004
        assert result.session_state == "reachable"

    def test_execute_mesh_only(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection()
        port.list_bgp_configurations.return_value = [
            CalicoBgpConfiguration(
                name="default",
                as_number=None,
                node_to_node_mesh_enabled=True,
                service_cluster_ips=(),
            ),
        ]
        port.list_bgp_peers.return_value = []

        result = CalicoBgpAuditUseCase(port=port).execute(CalicoBgpAuditCommand())

        assert result.node_to_node_mesh_enabled is True
        assert result.peer_count == 0

    def test_execute_not_installed(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection(installed=False)

        result = CalicoBgpAuditUseCase(port=port).execute(CalicoBgpAuditCommand())

        assert result.installed is False
        assert result.not_installed_marker == "NOT_INSTALLED"
        assert result.peer_count == 0

    def test_rbac_forbidden_propagates(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection()
        port.list_bgp_configurations.side_effect = InsufficientPermissionsError("denied")

        with pytest.raises(InsufficientPermissionsError):
            CalicoBgpAuditUseCase(port=port).execute(CalicoBgpAuditCommand())
