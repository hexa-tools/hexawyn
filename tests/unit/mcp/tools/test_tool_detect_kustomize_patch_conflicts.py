"""Unit tests for MCP tool: detect_kustomize_patch_conflicts."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestDetectKustomizePatchConflictsTool:
    def test_detect_kustomize_patch_conflicts_returns_dict(self) -> None:
        from hexawyn.mcp.tools.detect_kustomize_patch_conflicts import (
            detect_kustomize_patch_conflicts,
        )

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.server.build_kustomize_patch_analysis_adapter",
                return_value=MagicMock(),
            ),
        ):
            result = detect_kustomize_patch_conflicts(overlay_path="test")

        assert isinstance(result, dict)

    def test_detect_kustomize_patch_conflicts_handles_error(self) -> None:
        from hexawyn.mcp.tools.detect_kustomize_patch_conflicts import (
            detect_kustomize_patch_conflicts,
        )

        with (
            patch(
                "hexawyn.mcp.server.build_kustomize_patch_analysis_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = detect_kustomize_patch_conflicts(overlay_path="test")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.detect_kustomize_patch_conflicts")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
