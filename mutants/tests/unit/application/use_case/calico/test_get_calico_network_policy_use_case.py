"""Tests for the GetCalicoNetworkPolicy use case."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.use_case.calico.get_calico_network_policy.command import (
    GetCalicoNetworkPolicyCommand,
)
from hexawyn.application.use_case.calico.get_calico_network_policy.get_calico_network_policy_use_case import (  # noqa: E501
    GetCalicoNetworkPolicyUseCase,
)
from hexawyn.application.use_case.calico.get_calico_network_policy.response import (
    GetCalicoNetworkPolicyResponse,
)
from hexawyn.domain.errors import (
    InsufficientDataError,
    InsufficientPermissionsError,
    ResourceNotFoundError,
)
from hexawyn.domain.models.calico import (
    CalicoDetectionResult,
    CalicoDetectionStatus,
    CalicoNetworkPolicy,
    DataplaneMode,
)


class TestGetCalicoNetworkPolicyUseCase:
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

    def _namespaced_policy(self) -> CalicoNetworkPolicy:
        return CalicoNetworkPolicy(
            name="np",
            namespace="ns",
            kind="CalicoNetworkPolicy",
            selector="app=='web'",
            action="deny",
            ingress_rules=("deny tcp 80",),
            egress_rules=(),
            ingress_rule_count=1,
            egress_rule_count=0,
            order=30.0,
            apply_on_forward=False,
        )

    def test_execute_returns_full_spec(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection()
        port.get_network_policy.return_value = self._namespaced_policy()

        result = GetCalicoNetworkPolicyUseCase(port=port).execute(
            GetCalicoNetworkPolicyCommand(name="np", namespace="ns")
        )

        assert isinstance(result, GetCalicoNetworkPolicyResponse)
        assert result.installed is True
        assert result.found is True
        assert result.name == "np"
        assert result.namespace == "ns"
        assert result.scope == "namespaced"
        assert result.kind == "CalicoNetworkPolicy"
        assert result.selector == "app=='web'"
        assert result.action == "deny"
        assert result.ingress_rule_count == 1  # noqa: PLR2004

    def test_execute_global_policy_is_cluster_wide(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection()
        port.get_network_policy.return_value = CalicoNetworkPolicy(
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
        )

        result = GetCalicoNetworkPolicyUseCase(port=port).execute(
            GetCalicoNetworkPolicyCommand(name="g-np")
        )

        assert result.scope == "cluster-wide"
        assert result.kind == "GlobalNetworkPolicy"

    def test_not_installed(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection(installed=False)

        result = GetCalicoNetworkPolicyUseCase(port=port).execute(
            GetCalicoNetworkPolicyCommand(name="np", namespace="ns")
        )

        assert result.installed is False
        assert result.not_installed_marker == "NOT_INSTALLED"
        assert result.found is False

    def test_not_found_raises_resource_not_found(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection()
        port.get_network_policy.side_effect = ResourceNotFoundError("missing")

        with pytest.raises(ResourceNotFoundError):
            GetCalicoNetworkPolicyUseCase(port=port).execute(
                GetCalicoNetworkPolicyCommand(name="np", namespace="ns")
            )

    def test_none_policy_raises_resource_not_found(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection()
        port.get_network_policy.return_value = None

        with pytest.raises(ResourceNotFoundError):
            GetCalicoNetworkPolicyUseCase(port=port).execute(
                GetCalicoNetworkPolicyCommand(name="np", namespace="ns")
            )

    def test_missing_name_raises_validation(self) -> None:
        port = MagicMock()
        with pytest.raises(InsufficientDataError):
            GetCalicoNetworkPolicyUseCase(port=port).execute(GetCalicoNetworkPolicyCommand(name=""))

    def test_rbac_forbidden_propagates(self) -> None:
        port = MagicMock()
        port.detect.return_value = self._detection()
        port.get_network_policy.side_effect = InsufficientPermissionsError("denied")

        with pytest.raises(InsufficientPermissionsError):
            GetCalicoNetworkPolicyUseCase(port=port).execute(
                GetCalicoNetworkPolicyCommand(name="np", namespace="ns")
            )
