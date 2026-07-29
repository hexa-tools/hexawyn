from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestGitopsDetectMCPTool:
    def test_returns_dict_with_error_none_on_success(self) -> None:
        from hexawyn.mcp.tools.gitops_detect import gitops_detect

        detection_result = MagicMock()
        detection_result.engine = MagicMock()
        detection_result.engine.value = "argocd"
        detection_result.version = "v2.12.0"
        detection_result.namespace = "argocd"
        detection_result.apps_count = 42
        detection_result.out_of_sync_count = 5
        detection_result.failed_count = 2

        mock_port = MagicMock()
        mock_port.detect_engine.return_value = detection_result

        with patch(
            "hexawyn.mcp.server.build_gitops_adapter",
            return_value=mock_port,
        ):
            result = gitops_detect()

        assert isinstance(result, dict)
        assert result["error"] is None
        assert result["engine"] == "argocd"
        assert result["apps_count"] == 42  # noqa: PLR2004

    def test_returns_error_on_exception(self) -> None:
        from hexawyn.mcp.tools.gitops_detect import gitops_detect

        with patch(
            "hexawyn.mcp.server.build_gitops_adapter",
            side_effect=RuntimeError("no gitops engine found"),
        ):
            result = gitops_detect()

        assert isinstance(result, dict)
        assert "no gitops engine found" in str(result["error"])
