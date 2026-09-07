from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.cilium.list_cilium_network_policies.command import (
    ListCiliumNetworkPoliciesCommand,
)
from hexawyn.application.use_case.cilium.list_cilium_network_policies.list_cilium_network_policies_use_case import (  # noqa: E501
    ListCiliumNetworkPoliciesUseCase,
)
from hexawyn.application.use_case.cilium.list_cilium_network_policies.response import (
    ListCiliumNetworkPoliciesResponse,
)
from hexawyn.domain.models.cilium import CiliumNetworkPoliciesResult, CiliumNetworkPolicyInfo


class TestListCiliumNetworkPoliciesUseCase:
    def test_execute_returns_policy_list(self) -> None:
        policies = [
            CiliumNetworkPolicyInfo(
                kind="CiliumNetworkPolicy",
                name="allow-db",
                namespace="payments",
                endpoint_selector="matchLabels: app=db",
                ingress_rule_count=2,
                egress_rule_count=1,
                l7_rule_count=1,
                l7_protocols=("http",),
            )
        ]
        result = CiliumNetworkPoliciesResult(
            installed=True,
            status="present",
            total_policies=1,
            namespaced_count=1,
            clusterwide_count=0,
            policies=policies,
            note=None,
        )
        port = MagicMock()
        port.list_network_policies.return_value = result

        response = ListCiliumNetworkPoliciesUseCase(port=port).execute(
            ListCiliumNetworkPoliciesCommand()
        )

        assert isinstance(response, ListCiliumNetworkPoliciesResponse)
        assert response.status == "present"
        assert response.total_policies == 1  # noqa: PLR2004
        assert response.policies == [
            {
                "kind": "CiliumNetworkPolicy",
                "name": "allow-db",
                "namespace": "payments",
                "endpoint_selector": "matchLabels: app=db",
                "ingress_rule_count": 2,  # noqa: PLR2004
                "egress_rule_count": 1,  # noqa: PLR2004
                "l7_rule_count": 1,  # noqa: PLR2004
                "l7_protocols": ["http"],
            }
        ]

    def test_execute_not_installed(self) -> None:
        result = CiliumNetworkPoliciesResult(
            installed=False,
            status="not_installed",
            total_policies=0,
            namespaced_count=0,
            clusterwide_count=0,
            policies=[],
            note="Cilium is not installed in this cluster",
        )
        port = MagicMock()
        port.list_network_policies.return_value = result

        response = ListCiliumNetworkPoliciesUseCase(port=port).execute(
            ListCiliumNetworkPoliciesCommand()
        )

        assert response.installed is False
        assert response.status == "not_installed"
        assert response.policies == []
