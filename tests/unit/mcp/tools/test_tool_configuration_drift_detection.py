"""Unit tests for MCP tool: configuration_drift_detection."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestConfigurationDriftDetectionTool:
    def test_configuration_drift_detection_returns_dict(self) -> None:
        from hexawyn.mcp.tools.configuration_drift_detection import (
            configuration_drift_detection,
        )

        with (
            patch("hexawyn.mcp.server.build_live_resource_adapter", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_helm_drift_adapter", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_kustomize_drift_adapter", return_value=MagicMock()),
        ):
            result = configuration_drift_detection(namespace="test-ns")

        assert isinstance(result, dict)
        assert "error" in result

    def test_configuration_drift_detection_handles_error(self) -> None:
        from hexawyn.mcp.tools.configuration_drift_detection import (
            configuration_drift_detection,
        )

        with patch(
            "hexawyn.mcp.server.build_live_resource_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = configuration_drift_detection(namespace="test-ns")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_configuration_drift_detection_success_path(self) -> None:
        from hexawyn.mcp.tools.configuration_drift_detection import (
            configuration_drift_detection,
        )

        mock_response = MagicMock()
        mock_response.drifted_resources = []
        mock_response.drifted_by_namespace = {}
        mock_response.in_sync_count = 10
        mock_response.excluded_resources = []
        mock_response.total_checked = 10
        mock_response.summary = "No drift detected"
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.server.build_live_resource_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.server.build_helm_drift_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.server.build_kustomize_drift_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.configuration_drift_detection.ConfigurationDriftDetectionUseCase",
                return_value=mock_uc,
            ),
        ):
            result = configuration_drift_detection(namespace="test-ns")

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.configuration_drift_detection")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
