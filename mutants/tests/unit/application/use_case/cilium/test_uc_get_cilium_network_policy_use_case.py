from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.use_case.cilium.get_cilium_network_policy.command import (
    GetCiliumNetworkPolicyCommand,
)
from hexawyn.application.use_case.cilium.get_cilium_network_policy.get_cilium_network_policy_use_case import (  # noqa: E501
    GetCiliumNetworkPolicyUseCase,
)
from hexawyn.application.use_case.cilium.get_cilium_network_policy.response import (
    GetCiliumNetworkPolicyResponse,
)
from hexawyn.domain.models.cilium import (
    CiliumL7RuleSummary,
    CiliumNetworkPolicyDetail,
    CiliumRuleSummary,
)


class TestGetCiliumNetworkPolicyUseCase:
    def test_execute_returns_full_detail(self) -> None:
        detail = CiliumNetworkPolicyDetail(
            installed=True,
            status="ok",
            kind="CiliumNetworkPolicy",
            name="allow-db",
            namespace="payments",
            endpoint_selector="matchLabels: app=db",
            ingress_rules=(
                CiliumRuleSummary(
                    direction="ingress",
                    endpoints=("matchLabels: app=web",),
                    ports=("443/TCP",),
                    l7=(CiliumL7RuleSummary(protocol="http", match=("GET",)),),
                ),
            ),
            egress_rules=(),
            l7_protocols=("http",),
            spec={"endpointSelector": {"matchLabels": {"app": "db"}}},
            note=None,
        )
        port = MagicMock()
        port.get_network_policy.return_value = detail

        result = GetCiliumNetworkPolicyUseCase(port=port).execute(
            GetCiliumNetworkPolicyCommand(name="allow-db", namespace="payments")
        )

        assert isinstance(result, GetCiliumNetworkPolicyResponse)
        assert result.kind == "CiliumNetworkPolicy"
        assert result.endpoint_selector == "matchLabels: app=db"
        assert result.ingress_rules == [
            {
                "direction": "ingress",
                "endpoints": ["matchLabels: app=web"],
                "ports": ["443/TCP"],
                "l7": [{"protocol": "http", "match": ["GET"]}],
            }
        ]
        assert result.l7_protocols == ["http"]

    def test_execute_not_installed(self) -> None:
        detail = CiliumNetworkPolicyDetail(
            installed=False,
            status="not_installed",
            kind="",
            name="",
            namespace=None,
            endpoint_selector="",
            ingress_rules=(),
            egress_rules=(),
            l7_protocols=(),
            spec={},
            note="Cilium is not installed in this cluster",
        )
        port = MagicMock()
        port.get_network_policy.return_value = detail

        result = GetCiliumNetworkPolicyUseCase(port=port).execute(
            GetCiliumNetworkPolicyCommand(name="x", namespace=None)
        )

        assert result.installed is False
        assert result.status == "not_installed"
        assert result.spec == {}

    def test_command_requires_name(self) -> None:
        with pytest.raises(ValueError):
            GetCiliumNetworkPolicyCommand(name="", namespace="ns")
