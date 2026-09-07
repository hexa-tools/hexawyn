"""Unit tests for MCP tool: gitops_sources_list."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestGitopsSourcesListTool:
    def test_gitops_sources_list_returns_dict(self) -> None:
        from hexawyn.mcp.tools.gitops_sources_list import gitops_sources_list

        with patch("hexawyn.mcp.server.build_gitops_adapter", return_value=MagicMock()):
            result = gitops_sources_list()

        assert isinstance(result, dict)
        assert "error" in result

    def test_gitops_sources_list_handles_error(self) -> None:
        from hexawyn.mcp.tools.gitops_sources_list import gitops_sources_list

        with patch(
            "hexawyn.mcp.server.build_gitops_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = gitops_sources_list()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.gitops_sources_list")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
