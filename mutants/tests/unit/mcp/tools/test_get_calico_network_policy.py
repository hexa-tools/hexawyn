"""Unit tests for MCP tool: get_calico_network_policy."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestGetCalicoNetworkPolicyTool:
    def test_get_returns_dict(self) -> None:
        from hexawyn.mcp.tools.get_calico_network_policy import get_calico_network_policy

        mock_response = MagicMock()
        mock_response.installed = True
        mock_response.not_installed_marker = None
        mock_response.found = True
        mock_response.name = "np"
        mock_response.namespace = "ns"
        mock_response.scope = "namespaced"
        mock_response.kind = "CalicoNetworkPolicy"
        mock_response.selector = "app=='web'"
        mock_response.action = "deny"
        mock_response.ingress_rules = ["deny tcp 80"]
        mock_response.egress_rules = []
        mock_response.ingress_rule_count = 1
        mock_response.egress_rule_count = 0
        mock_response.order = 30.0
        mock_response.apply_on_forward = False
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_calico_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.get_calico_network_policy.GetCalicoNetworkPolicyUseCase",
                return_value=mock_uc,
            ),
        ):
            result = get_calico_network_policy(name="np", namespace="ns")

        assert isinstance(result, dict)
        assert result["installed"] is True
        assert result["found"] is True
        assert result["name"] == "np"
        assert result["action"] == "deny"
        assert result["error"] is None

    def test_get_handles_error(self) -> None:
        from hexawyn.mcp.tools.get_calico_network_policy import get_calico_network_policy

        with patch(
            "hexawyn.mcp.server.build_calico_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = get_calico_network_policy(name="np")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"
        assert result.get("installed") is False

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.get_calico_network_policy")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))

    def test_policy_fields(self) -> None:
        from hexawyn.domain.models.calico import CalicoNetworkPolicy
        from hexawyn.mcp.tools.get_calico_network_policy import _policy_fields

        policy = CalicoNetworkPolicy(
            name="np",
            namespace="ns",
            kind="CalicoNetworkPolicy",
            selector="app=='web'",
            action="allow",
            ingress_rules=("allow tcp 80",),
            egress_rules=(),
            ingress_rule_count=1,
            egress_rule_count=0,
            order=30.0,
            apply_on_forward=False,
        )
        result = _policy_fields(policy)

        assert result["name"] == "np"
        assert result["selector"] == "app=='web'"
        assert result["action"] == "allow"
        assert result["ingress_rules"] == ["allow tcp 80"]
