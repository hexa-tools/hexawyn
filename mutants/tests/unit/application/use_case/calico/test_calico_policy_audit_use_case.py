"""Tests for the CalicoPolicyAudit use case."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.use_case.calico.calico_policy_audit.calico_policy_audit_use_case import (
    CalicoPolicyAuditUseCase,
)
from hexawyn.application.use_case.calico.calico_policy_audit.command import (
    CalicoPolicyAuditCommand,
)
from hexawyn.application.use_case.calico.calico_policy_audit.response import (
    CalicoPolicyAuditResponse,
)
from hexawyn.domain.errors import InsufficientPermissionsError
from hexawyn.domain.models.calico import (
    CalicoDetectionResult,
    CalicoDetectionStatus,
    CalicoNetworkPolicy,
    CalicoWorkload,
    DataplaneMode,
)


class TestCalicoPolicyAuditUseCase:
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

    def test_execute_returns_gaps(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection()
        port.list_workloads.return_value = [CalicoWorkload(namespace="ns1", pod_count=3)]
        port.list_network_policies.return_value = []

        result = CalicoPolicyAuditUseCase(port=port).execute(CalicoPolicyAuditCommand())

        assert isinstance(result, CalicoPolicyAuditResponse)
        assert result.installed is True
        assert result.gap_count == 1  # noqa: PLR2004
        assert result.total_namespaces_checked == 1  # noqa: PLR2004

    def test_execute_covered(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection()
        port.list_workloads.return_value = [CalicoWorkload(namespace="ns1", pod_count=2)]
        port.list_network_policies.return_value = [
            CalicoNetworkPolicy(
                name="np",
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
            )
        ]

        result = CalicoPolicyAuditUseCase(port=port).execute(CalicoPolicyAuditCommand())

        assert result.gap_count == 0

    def test_execute_not_installed_degrades_to_vanilla(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection(installed=False)

        result = CalicoPolicyAuditUseCase(port=port).execute(CalicoPolicyAuditCommand())

        assert result.installed is False
        assert result.not_installed_marker == "NOT_INSTALLED"
        assert result.degraded_to_vanilla is True
        assert result.gap_count == 0

    def test_rbac_forbidden_propagates(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection()
        port.list_workloads.side_effect = InsufficientPermissionsError("denied")

        with pytest.raises(InsufficientPermissionsError):
            CalicoPolicyAuditUseCase(port=port).execute(CalicoPolicyAuditCommand())
