"""Unit tests for MCP tool: gitops_app_sync."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestGitopsAppSyncTool:
    def test_gitops_app_sync_returns_dict(self) -> None:
        from hexawyn.mcp.tools.gitops_app_sync import gitops_app_sync

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_gitops_adapter", return_value=MagicMock()),
        ):
            result = gitops_app_sync(name="test-name", namespace="test-ns")

        assert isinstance(result, dict)

    def test_gitops_app_sync_handles_error(self) -> None:
        from hexawyn.mcp.tools.gitops_app_sync import gitops_app_sync

        with (
            patch(
                "hexawyn.mcp.server.build_gitops_adapter", side_effect=RuntimeError("test error")
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = gitops_app_sync(name="test-name", namespace="test-ns")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.gitops_app_sync")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
