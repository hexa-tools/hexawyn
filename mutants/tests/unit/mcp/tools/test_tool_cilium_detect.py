"""Unit tests for MCP tool: cilium_detect."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCiliumDetectTool:
    def test_cilium_detect_returns_dict(self) -> None:
        from hexawyn.mcp.tools.cilium_detect import cilium_detect

        mock_response = MagicMock()
        mock_response.installed = True
        mock_response.status = "installed"
        mock_response.version = "v1.16.3"
        mock_response.mode = "native-routing"
        mock_response.namespace = "kube-system"
        mock_response.total_agents = 2
        mock_response.ready_agents = 2
        mock_response.degraded_summary = None
        mock_response.agents = []
        mock_response.note = None
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_cilium_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.cilium_detect.CiliumDetectUseCase",
                return_value=mock_uc,
            ),
        ):
            result = cilium_detect()

        assert isinstance(result, dict)
        assert result["installed"] is True
        assert result["version"] == "v1.16.3"
        assert result["error"] is None

    def test_cilium_detect_error_returns_not_installed(self) -> None:
        from hexawyn.mcp.tools.cilium_detect import cilium_detect

        with patch(
            "hexawyn.mcp.server.build_cilium_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = cilium_detect()

        assert isinstance(result, dict)
        assert result["installed"] is False
        assert result["status"] == "unknown"
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.cilium_detect")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
