"""Unit tests for MCP tool: gitops_detect."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestGitopsDetectTool:
    def test_gitops_detect_returns_dict(self) -> None:
        from hexawyn.mcp.tools.gitops_detect import gitops_detect

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_gitops_adapter", return_value=MagicMock()),
        ):
            result = gitops_detect()

        assert isinstance(result, dict)

    def test_gitops_detect_handles_error(self) -> None:
        from hexawyn.mcp.tools.gitops_detect import gitops_detect

        with (
            patch(
                "hexawyn.mcp.server.build_gitops_adapter", side_effect=RuntimeError("test error")
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = gitops_detect()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.gitops_detect")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
