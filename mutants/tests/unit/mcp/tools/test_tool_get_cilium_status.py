"""Unit tests for MCP tool: get_cilium_status."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestGetCiliumStatusTool:
    def test_get_cilium_status_returns_dict(self) -> None:
        from hexawyn.mcp.tools.get_cilium_status import get_cilium_status

        mock_response = MagicMock()
        mock_response.installed = True
        mock_response.status = "degraded"
        mock_response.ready_agents = 1
        mock_response.total_agents = 2
        mock_response.degraded_summary = "1/2 agents ready"
        mock_response.controller_errors = 1
        mock_response.connectivity = "degraded"
        mock_response.nodes = []
        mock_response.note = None
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_cilium_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.get_cilium_status.GetCiliumStatusUseCase",
                return_value=mock_uc,
            ),
        ):
            result = get_cilium_status()

        assert isinstance(result, dict)
        assert result["installed"] is True
        assert result["status"] == "degraded"
        assert result["degraded_summary"] == "1/2 agents ready"
        assert result["error"] is None

    def test_get_cilium_status_error_returns_unknown(self) -> None:
        from hexawyn.mcp.tools.get_cilium_status import get_cilium_status

        with patch(
            "hexawyn.mcp.server.build_cilium_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = get_cilium_status()

        assert isinstance(result, dict)
        assert result["installed"] is False
        assert result["status"] == "unknown"
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.get_cilium_status")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
