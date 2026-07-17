"""Unit tests for MCP tool: manual_change_outside_gitops_detection."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestManualChangeOutsideGitopsDetectionTool:
    def test_detect_manual_changes_outside_gitops_returns_dict(self) -> None:
        from hexawyn.mcp.tools.manual_change_outside_gitops_detection import (
            detect_manual_changes_outside_gitops,
        )

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_audit_log_adapter", return_value=MagicMock()),
        ):
            result = detect_manual_changes_outside_gitops(namespace="test-ns")

        assert isinstance(result, dict)

    def test_detect_manual_changes_outside_gitops_handles_error(self) -> None:
        from hexawyn.mcp.tools.manual_change_outside_gitops_detection import (
            detect_manual_changes_outside_gitops,
        )

        with (
            patch(
                "hexawyn.mcp.server.build_audit_log_adapter", side_effect=RuntimeError("test error")
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = detect_manual_changes_outside_gitops(namespace="test-ns")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.manual_change_outside_gitops_detection")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
