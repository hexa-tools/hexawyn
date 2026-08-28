"""Tests for the CalicoSegmentationAudit use case."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.use_case.calico.calico_segmentation_audit.calico_segmentation_audit_use_case import (  # noqa: E501
    CalicoSegmentationAuditUseCase,
)
from hexawyn.application.use_case.calico.calico_segmentation_audit.command import (
    CalicoSegmentationAuditCommand,
)
from hexawyn.application.use_case.calico.calico_segmentation_audit.response import (
    CalicoSegmentationAuditResponse,
)
from hexawyn.domain.errors import InsufficientPermissionsError
from hexawyn.domain.models.calico import (
    CalicoDetectionResult,
    CalicoDetectionStatus,
    CalicoNetworkPolicy,
    CalicoWorkload,
    DataplaneMode,
)


class TestCalicoSegmentationAuditUseCase:
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

    def test_execute_builds_matrix(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection()
        port.list_workloads.return_value = [CalicoWorkload(namespace="ns1", pod_count=2)]
        port.list_network_policies.return_value = []

        result = CalicoSegmentationAuditUseCase(port=port).execute(CalicoSegmentationAuditCommand())

        assert isinstance(result, CalicoSegmentationAuditResponse)
        assert result.installed is True
        assert result.view == "calico"
        assert result.tiers == ["ns1"]
        assert result.total_paths == 0

    def test_execute_fully_segmented(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection()
        port.list_workloads.return_value = [
            CalicoWorkload(namespace="ns1", pod_count=2),
            CalicoWorkload(namespace="ns2", pod_count=1),
        ]
        port.list_network_policies.return_value = [
            CalicoNetworkPolicy(
                name="np1",
                namespace="ns1",
                kind="CalicoNetworkPolicy",
                selector="app=='web'",
                action="deny",
                ingress_rules=("deny",),
                egress_rules=("deny",),
                ingress_rule_count=1,
                egress_rule_count=1,
                order=10.0,
                apply_on_forward=False,
                has_l7_rule=True,
            ),
            CalicoNetworkPolicy(
                name="np2",
                namespace="ns2",
                kind="CalicoNetworkPolicy",
                selector="app=='web'",
                action="deny",
                ingress_rules=("deny",),
                egress_rules=("deny",),
                ingress_rule_count=1,
                egress_rule_count=1,
                order=10.0,
                apply_on_forward=False,
                has_l7_rule=True,
            ),
        ]

        result = CalicoSegmentationAuditUseCase(port=port).execute(CalicoSegmentationAuditCommand())

        assert result.gap_count == 0
        assert result.total_paths == 2  # noqa: PLR2004

    def test_execute_not_installed_vanilla_view(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection(installed=False)

        result = CalicoSegmentationAuditUseCase(port=port).execute(CalicoSegmentationAuditCommand())

        assert result.installed is False
        assert result.not_installed_marker == "NOT_INSTALLED"
        assert result.view == "vanilla"
        assert result.edges == []

    def test_rbac_forbidden_propagates(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection()
        port.list_workloads.side_effect = InsufficientPermissionsError("denied")

        with pytest.raises(InsufficientPermissionsError):
            CalicoSegmentationAuditUseCase(port=port).execute(CalicoSegmentationAuditCommand())
