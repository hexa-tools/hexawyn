"""Unit tests for MCP tool: get_cilium_network_policy."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestGetCiliumNetworkPolicyTool:
    def test_get_cilium_network_policy_returns_dict(self) -> None:
        from hexawyn.mcp.tools.get_cilium_network_policy import (
            get_cilium_network_policy,
        )

        mock_response = MagicMock()
        mock_response.installed = True
        mock_response.status = "ok"
        mock_response.kind = "CiliumNetworkPolicy"
        mock_response.name = "allow-db"
        mock_response.namespace = "payments"
        mock_response.endpoint_selector = "matchLabels: app=db"
        mock_response.ingress_rules = []
        mock_response.egress_rules = []
        mock_response.l7_protocols = ["http"]
        mock_response.spec = {"endpointSelector": {"matchLabels": {"app": "db"}}}
        mock_response.note = None
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_cilium_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.get_cilium_network_policy.GetCiliumNetworkPolicyUseCase",
                return_value=mock_uc,
            ),
        ):
            result = get_cilium_network_policy(name="allow-db", namespace="payments")

        assert isinstance(result, dict)
        assert result["installed"] is True
        assert result["kind"] == "CiliumNetworkPolicy"
        assert result["error"] is None

    def test_get_cilium_network_policy_error_returns_unknown(self) -> None:
        from hexawyn.mcp.tools.get_cilium_network_policy import (
            get_cilium_network_policy,
        )

        with patch(
            "hexawyn.mcp.server.build_cilium_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = get_cilium_network_policy(name="x")

        assert isinstance(result, dict)
        assert result["installed"] is False
        assert result["status"] == "unknown"
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.get_cilium_network_policy")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
