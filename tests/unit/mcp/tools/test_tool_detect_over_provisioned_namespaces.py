"""Unit tests for MCP tool: detect_over_provisioned_namespaces."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestDetectOverProvisionedNamespacesTool:
    def test_detect_over_provisioned_namespaces_returns_dict(self) -> None:
        from hexawyn.mcp.tools.detect_over_provisioned_namespaces import (
            detect_over_provisioned_namespaces,
        )

        with patch("hexawyn.mcp.server.build_waste_adapter", return_value=MagicMock()):
            result = detect_over_provisioned_namespaces()

        assert isinstance(result, dict)
        assert "error" in result

    def test_detect_over_provisioned_namespaces_handles_error(self) -> None:
        from hexawyn.mcp.tools.detect_over_provisioned_namespaces import (
            detect_over_provisioned_namespaces,
        )

        with patch(
            "hexawyn.mcp.server.build_waste_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = detect_over_provisioned_namespaces()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_detect_over_provisioned_namespaces_success_path(self) -> None:
        from hexawyn.mcp.tools.detect_over_provisioned_namespaces import (
            detect_over_provisioned_namespaces,
        )

        mock_ns = MagicMock()
        mock_ns.namespace = "test-ns"
        mock_ns.cpu_requested_cores = 2.0
        mock_ns.cpu_actual_avg_cores = 0.5
        mock_ns.cpu_waste_pct = 75.0
        mock_ns.cpu_wasted_cores = 1.5
        mock_ns.memory_requested_gb = 4.0
        mock_ns.memory_actual_avg_gb = 1.0
        mock_ns.memory_waste_pct = 75.0
        mock_ns.memory_wasted_gb = 3.0
        mock_ns.is_over_provisioned = True
        mock_excluded = MagicMock()
        mock_excluded.namespace = "excluded-ns"
        mock_excluded.reason = "no metrics"
        mock_report = MagicMock()
        mock_report.namespaces = [mock_ns]
        mock_report.excluded = [mock_excluded]
        mock_report.total_wasted_cpu_cores = 1.5
        mock_report.total_wasted_memory_gb = 3.0
        mock_report.analysis_window_days = 7
        mock_response = MagicMock()
        mock_response.report = mock_report
        mock_response.prometheus_available = True
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_waste_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.detect_over_provisioned_namespaces.DetectOverProvisionedNamespacesUseCase",
                return_value=mock_uc,
            ),
        ):
            result = detect_over_provisioned_namespaces()

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.detect_over_provisioned_namespaces")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
