"""Unit tests for MCP tool: gitops_app_status."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestGitopsAppStatusTool:
    def test_gitops_app_status_returns_dict(self) -> None:
        from hexawyn.mcp.tools.gitops_app_status import gitops_app_status

        with patch("hexawyn.mcp.server.build_gitops_adapter", return_value=MagicMock()):
            result = gitops_app_status()

        assert isinstance(result, dict)
        assert "error" in result

    def test_gitops_app_status_handles_error(self) -> None:
        from hexawyn.mcp.tools.gitops_app_status import gitops_app_status

        with patch(
            "hexawyn.mcp.server.build_gitops_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = gitops_app_status()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_gitops_app_status_success_path(self) -> None:
        from hexawyn.mcp.tools.gitops_app_status import gitops_app_status

        with (
            patch("hexawyn.mcp.server.build_gitops_adapter", return_value=MagicMock()),
            patch("hexawyn.mcp.tools.gitops_app_status.GitopsAppStatusUseCase") as mock_uc,
            patch("hexawyn.mcp.tools.gitops_app_status.GitopsAppStatusCommand"),
        ):
            mock_uc.return_value.execute.return_value = MagicMock()
            result = gitops_app_status()

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.gitops_app_status")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
