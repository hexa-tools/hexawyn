"""Unit tests for MCP tool: gitops_detect."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestGitopsDetectTool:
    def test_gitops_detect_returns_dict(self) -> None:
        from hexawyn.mcp.tools.gitops_detect import gitops_detect

        mock_response = MagicMock()
        mock_response.engine = "argocd"
        mock_response.version = "v1.0"
        mock_response.namespace = "argocd"
        mock_response.apps_count = 5
        mock_response.out_of_sync_count = 1
        mock_response.failed_count = 0
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_gitops_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.gitops_detect.GitopsDetectUseCase",
                return_value=mock_uc,
            ),
        ):
            result = gitops_detect()

        assert isinstance(result, dict)
        assert result["error"] is None

    def test_gitops_detect_handles_error(self) -> None:
        from hexawyn.mcp.tools.gitops_detect import gitops_detect

        with patch(
            "hexawyn.mcp.server.build_gitops_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = gitops_detect()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.gitops_detect")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
