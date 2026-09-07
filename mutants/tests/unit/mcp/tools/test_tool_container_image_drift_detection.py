"""Unit tests for MCP tool: detect_container_image_drift."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestContainerImageDriftDetectionTool:
    def test_detect_container_image_drift_returns_dict(self) -> None:
        from hexawyn.mcp.tools.container_image_drift_detection import (
            detect_container_image_drift,
        )

        with patch("hexawyn.mcp.server.build_helm_drift_adapter", return_value=MagicMock()):
            result = detect_container_image_drift()

        assert isinstance(result, dict)
        assert "error" in result

    def test_detect_container_image_drift_handles_error(self) -> None:
        from hexawyn.mcp.tools.container_image_drift_detection import (
            detect_container_image_drift,
        )

        with patch(
            "hexawyn.mcp.server.build_helm_drift_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = detect_container_image_drift()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.container_image_drift_detection")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
