"""Unit tests for MCP tool: list_pods."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestListPodsTool:
    def test_list_pods_returns_dict(self) -> None:
        from hexawyn.mcp.tools.list_pods import list_pods

        mock_response = MagicMock()
        mock_response.pods = []
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_k8s_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.list_pods.ListPodsUseCase",
                return_value=mock_uc,
            ),
        ):
            result = list_pods("test-ns")

        assert isinstance(result, dict)
        assert "pods" in result

    def test_list_pods_handles_error(self) -> None:
        from hexawyn.mcp.tools.list_pods import list_pods

        with patch(
            "hexawyn.mcp.server.build_k8s_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = list_pods("test-ns")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.list_pods")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
