"""Unit tests for MCP tool: manual_change_outside_gitops_detection."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestManualChangeOutsideGitopsDetectionTool:
    def test_detect_manual_changes_outside_gitops_returns_dict(self) -> None:
        from hexawyn.mcp.tools.manual_change_outside_gitops_detection import (
            detect_manual_changes_outside_gitops,
        )

        mock_response = MagicMock()
        mock_response.manual_changes = []
        mock_response.total_manual_changes = 0
        mock_response.excluded_gitops_change_count = 0
        mock_response.used_managed_fields_fallback = False
        mock_response.partial_window = False
        mock_response.notes = []
        mock_uc = MagicMock()
        mock_uc.detect_manual_changes.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_audit_log_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.manual_change_outside_gitops_detection.ManualChangeOutsideGitopsUseCase",
                return_value=mock_uc,
            ),
        ):
            result = detect_manual_changes_outside_gitops()

        assert isinstance(result, dict)
        assert "manual_changes" in result

    def test_detect_manual_changes_outside_gitops_handles_error(self) -> None:
        from hexawyn.mcp.tools.manual_change_outside_gitops_detection import (
            detect_manual_changes_outside_gitops,
        )

        with patch(
            "hexawyn.mcp.server.build_audit_log_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = detect_manual_changes_outside_gitops()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.manual_change_outside_gitops_detection")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
