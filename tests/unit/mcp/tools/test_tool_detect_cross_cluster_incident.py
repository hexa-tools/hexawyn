"""Unit tests for MCP tool: detect_cross_cluster_incident."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestDetectCrossClusterIncidentTool:
    def test_detect_cross_cluster_incident_returns_dict(self) -> None:
        from hexawyn.mcp.tools.detect_cross_cluster_incident import detect_cross_cluster_incident

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.server.build_cross_cluster_incident_adapter", return_value=MagicMock()
            ),
        ):
            result = detect_cross_cluster_incident()

        assert isinstance(result, dict)

    def test_detect_cross_cluster_incident_handles_error(self) -> None:
        from hexawyn.mcp.tools.detect_cross_cluster_incident import detect_cross_cluster_incident

        with (
            patch(
                "hexawyn.mcp.server.build_cross_cluster_incident_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = detect_cross_cluster_incident()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.detect_cross_cluster_incident")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
