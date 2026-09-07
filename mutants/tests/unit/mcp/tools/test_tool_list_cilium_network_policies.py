"""Unit tests for MCP tool: list_cilium_network_policies."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestListCiliumNetworkPoliciesTool:
    def test_list_cilium_network_policies_returns_dict(self) -> None:
        from hexawyn.mcp.tools.list_cilium_network_policies import (
            list_cilium_network_policies,
        )

        mock_policy = MagicMock()
        mock_policy.kind = "CiliumNetworkPolicy"
        mock_policy.name = "allow-db"
        mock_response = MagicMock()
        mock_response.installed = True
        mock_response.status = "present"
        mock_response.total_policies = 1
        mock_response.namespaced_count = 1
        mock_response.clusterwide_count = 0
        mock_response.policies = [mock_policy]
        mock_response.note = None
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_cilium_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.list_cilium_network_policies.ListCiliumNetworkPoliciesUseCase",
                return_value=mock_uc,
            ),
        ):
            result = list_cilium_network_policies()

        assert isinstance(result, dict)
        assert result["installed"] is True
        assert result["status"] == "present"
        assert result["error"] is None

    def test_list_cilium_network_policies_error_returns_unknown(self) -> None:
        from hexawyn.mcp.tools.list_cilium_network_policies import (
            list_cilium_network_policies,
        )

        with patch(
            "hexawyn.mcp.server.build_cilium_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = list_cilium_network_policies()

        assert isinstance(result, dict)
        assert result["installed"] is False
        assert result["status"] == "unknown"
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.list_cilium_network_policies")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
