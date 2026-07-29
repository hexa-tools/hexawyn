"""Unit tests for MCP tool: gitops_source_get."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestGitopsSourceGetTool:
    def test_gitops_source_get_returns_dict(self) -> None:
        from hexawyn.mcp.tools.gitops_source_get import gitops_source_get

        with patch("hexawyn.mcp.server.build_gitops_adapter", return_value=MagicMock()):
            result = gitops_source_get()

        assert isinstance(result, dict)
        assert "error" in result

    def test_gitops_source_get_handles_error(self) -> None:
        from hexawyn.mcp.tools.gitops_source_get import gitops_source_get

        with patch(
            "hexawyn.mcp.server.build_gitops_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = gitops_source_get()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.gitops_source_get")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
