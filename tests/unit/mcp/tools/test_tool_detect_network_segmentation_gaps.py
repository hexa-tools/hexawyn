"""Unit tests for MCP tool: detect_network_segmentation_gaps."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestDetectNetworkSegmentationGapsTool:
    def test_detect_network_segmentation_gaps_returns_dict(self) -> None:
        from hexawyn.mcp.tools.detect_network_segmentation_gaps import (
            detect_network_segmentation_gaps,
        )

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.server.build_network_policy_audit_adapter", return_value=MagicMock()
            ),
        ):
            result = detect_network_segmentation_gaps()

        assert isinstance(result, dict)

    def test_detect_network_segmentation_gaps_handles_error(self) -> None:
        from hexawyn.mcp.tools.detect_network_segmentation_gaps import (
            detect_network_segmentation_gaps,
        )

        with (
            patch(
                "hexawyn.mcp.server.build_network_policy_audit_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = detect_network_segmentation_gaps()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.detect_network_segmentation_gaps")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
