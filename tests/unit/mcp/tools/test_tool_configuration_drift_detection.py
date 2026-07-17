"""Unit tests for MCP tool: configuration_drift_detection."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestConfigurationDriftDetectionTool:
    def test_configuration_drift_detection_returns_dict(self) -> None:
        from hexawyn.mcp.tools.configuration_drift_detection import configuration_drift_detection

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_helm_drift_adapter", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_kustomize_drift_adapter", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_live_resource_adapter", return_value=MagicMock()),
        ):
            result = configuration_drift_detection(namespace="test-ns")

        assert isinstance(result, dict)

    def test_configuration_drift_detection_handles_error(self) -> None:
        from hexawyn.mcp.tools.configuration_drift_detection import configuration_drift_detection

        with (
            patch(
                "hexawyn.mcp.server.build_helm_drift_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch(
                "hexawyn.mcp.server.build_kustomize_drift_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch(
                "hexawyn.mcp.server.build_live_resource_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = configuration_drift_detection(namespace="test-ns")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.configuration_drift_detection")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
