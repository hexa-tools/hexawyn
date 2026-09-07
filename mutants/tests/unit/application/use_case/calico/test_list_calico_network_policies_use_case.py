"""Tests for the ListCalicoNetworkPolicies use case."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.use_case.calico.list_calico_network_policies.command import (
    ListCalicoNetworkPoliciesCommand,
)
from hexawyn.application.use_case.calico.list_calico_network_policies.list_calico_network_policies_use_case import (  # noqa: E501
    ListCalicoNetworkPoliciesUseCase,
)
from hexawyn.application.use_case.calico.list_calico_network_policies.response import (
    ListCalicoNetworkPoliciesResponse,
)
from hexawyn.domain.errors import InsufficientPermissionsError
from hexawyn.domain.models.calico import (
    CalicoDetectionResult,
    CalicoDetectionStatus,
    CalicoNetworkPolicy,
    DataplaneMode,
)


class TestListCalicoNetworkPoliciesUseCase:
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

    def test_execute_lists_policies_with_counts(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection()
        port.list_network_policies.return_value = [
            CalicoNetworkPolicy(
                name="g-np",
                namespace="",
                kind="GlobalNetworkPolicy",
                selector="all()",
                action="allow",
                ingress_rules=(),
                egress_rules=(),
                ingress_rule_count=0,
                egress_rule_count=0,
                order=10.0,
                apply_on_forward=False,
            ),
            CalicoNetworkPolicy(
                name="np",
                namespace="ns",
                kind="CalicoNetworkPolicy",
                selector="app=='web'",
                action="deny",
                ingress_rules=("deny",),
                egress_rules=(),
                ingress_rule_count=1,
                egress_rule_count=0,
                order=10.0,
                apply_on_forward=False,
            ),
        ]

        result = ListCalicoNetworkPoliciesUseCase(port=port).execute(
            ListCalicoNetworkPoliciesCommand(namespace="ns")
        )

        assert isinstance(result, ListCalicoNetworkPoliciesResponse)
        assert result.installed is True
        assert result.total == 2  # noqa: PLR2004
        assert result.global_count == 1  # noqa: PLR2004
        assert result.namespaced_count == 1  # noqa: PLR2004

    def test_execute_empty_policies(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection()
        port.list_network_policies.return_value = []

        result = ListCalicoNetworkPoliciesUseCase(port=port).execute(
            ListCalicoNetworkPoliciesCommand()
        )

        assert result.installed is True
        assert result.total == 0
        assert result.policies == []

    def test_execute_not_installed(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection(installed=False)

        result = ListCalicoNetworkPoliciesUseCase(port=port).execute(
            ListCalicoNetworkPoliciesCommand()
        )

        assert result.installed is False
        assert result.not_installed_marker == "NOT_INSTALLED"
        assert result.policies == []

    def test_rbac_forbidden_propagates(self) -> None:
        port = MagicMock()
        port.detect.side_effect = InsufficientPermissionsError("denied")
        with pytest.raises(InsufficientPermissionsError):
            ListCalicoNetworkPoliciesUseCase(port=port).execute(ListCalicoNetworkPoliciesCommand())
