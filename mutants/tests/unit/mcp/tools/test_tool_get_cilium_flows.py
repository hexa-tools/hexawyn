"""Unit tests for MCP tool: get_cilium_flows."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestGetCiliumFlowsTool:
    def test_get_cilium_flows_returns_dict(self) -> None:
        from hexawyn.mcp.tools.get_cilium_flows import get_cilium_flows

        mock_flow = MagicMock()
        mock_flow.source = "web-0"
        mock_response = MagicMock()
        mock_response.installed = True
        mock_response.status = "present"
        mock_response.total_flows = 1
        mock_response.flows = [mock_flow]
        mock_response.note = None
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.server.build_cilium_hubble_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.get_cilium_flows.GetCiliumFlowsUseCase",
                return_value=mock_uc,
            ),
        ):
            result = get_cilium_flows(namespace="payments")

        assert isinstance(result, dict)
        assert result["installed"] is True
        assert result["status"] == "present"
        assert result["error"] is None

    def test_get_cilium_flows_error_returns_unknown(self) -> None:
        from hexawyn.mcp.tools.get_cilium_flows import get_cilium_flows

        with patch(
            "hexawyn.mcp.server.build_cilium_hubble_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = get_cilium_flows()

        assert isinstance(result, dict)
        assert result["installed"] is False
        assert result["status"] == "unknown"
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.get_cilium_flows")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
