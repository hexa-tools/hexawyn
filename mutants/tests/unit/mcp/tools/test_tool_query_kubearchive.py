"""Unit tests for MCP tool: query_kubearchive."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestQueryKubearchiveTool:
    def test_query_kubearchive_returns_dict(self) -> None:
        from hexawyn.mcp.tools.query_kubearchive import query_kubearchive

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_k8s_adapter", return_value=MagicMock()),
        ):
            result = query_kubearchive(namespace="test-ns")

        assert isinstance(result, dict)

    def test_query_kubearchive_handles_error(self) -> None:
        from hexawyn.mcp.tools.query_kubearchive import query_kubearchive

        with (
            patch("hexawyn.mcp.server.build_k8s_adapter", side_effect=RuntimeError("test error")),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = query_kubearchive(namespace="test-ns")

        assert isinstance(result, dict)

    def test_query_kubearchive_success_path(self) -> None:
        from hexawyn.mcp.tools.query_kubearchive import query_kubearchive

        with (
            patch(
                "hexawyn.mcp.server.build_k8s_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.server.get_connection",
                return_value=MagicMock(),
            ),
            patch("hexawyn.mcp.tools.query_kubearchive.QueryKubeArchiveUseCase"),
            patch("hexawyn.mcp.tools.query_kubearchive.QueryKubearchiveCommand"),
        ):
            result = query_kubearchive()

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.query_kubearchive")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
