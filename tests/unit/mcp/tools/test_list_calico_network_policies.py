"""Unit tests for MCP tool: list_calico_network_policies."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestListCalicoNetworkPoliciesTool:
    def test_list_returns_dict(self) -> None:
        from hexawyn.mcp.tools.list_calico_network_policies import list_calico_network_policies

        mock_response = MagicMock()
        mock_response.installed = True
        mock_response.not_installed_marker = None
        mock_response.total = 2
        mock_response.global_count = 1
        mock_response.namespaced_count = 1
        mock_response.policies = []
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_calico_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.list_calico_network_policies.ListCalicoNetworkPoliciesUseCase",
                return_value=mock_uc,
            ),
        ):
            result = list_calico_network_policies(namespace="ns")

        assert isinstance(result, dict)
        assert result["installed"] is True
        assert result["total"] == 2  # noqa: PLR2004
        assert result["namespace"] == "ns"
        assert result["error"] is None

    def test_list_handles_error(self) -> None:
        from hexawyn.mcp.tools.list_calico_network_policies import list_calico_network_policies

        with patch(
            "hexawyn.mcp.server.build_calico_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = list_calico_network_policies()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"
        assert result.get("installed") is False

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.list_calico_network_policies")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))

    def test_policy_dict(self) -> None:
        from hexawyn.domain.models.calico import CalicoNetworkPolicy
        from hexawyn.mcp.tools.list_calico_network_policies import _policy_dict

        policy = CalicoNetworkPolicy(
            name="g-np",
            namespace="",
            kind="GlobalNetworkPolicy",
            selector="all()",
            action="allow",
            ingress_rules=("allow tcp 80",),
            egress_rules=(),
            ingress_rule_count=1,
            egress_rule_count=0,
            order=10.0,
            apply_on_forward=False,
        )
        result = _policy_dict(policy)

        assert result["name"] == "g-np"
        assert result["kind"] == "GlobalNetworkPolicy"
        assert result["action"] == "allow"
        assert result["ingress_rule_count"] == 1  # noqa: PLR2004
        assert result["ingress_rules"] == ["allow tcp 80"]
