"""Unit tests for MCP tool: check_cluster_certificate_health."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCheckClusterCertificateHealthTool:
    def test_check_cluster_certificate_health_returns_dict(self) -> None:
        from hexawyn.mcp.tools.check_cluster_certificate_health import (
            check_cluster_certificate_health,
        )

        mock_report = MagicMock()
        mock_report.cluster_name = "test"
        mock_report.total_scanned = 10
        mock_report.expired = []
        mock_report.critical = []
        mock_report.warning = []
        mock_report.healthy = []

        mock_response = MagicMock()
        mock_response.report = mock_report
        mock_uc = MagicMock()
        mock_uc.check_cluster_certificate_health.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.server.build_cluster_certificate_health_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.check_cluster_certificate_health.ClusterCertificateHealthUseCase",
                return_value=mock_uc,
            ),
        ):
            result = check_cluster_certificate_health()

        assert isinstance(result, dict)
        assert result["cluster_name"] == "test"

    def test_check_cluster_certificate_health_handles_error(self) -> None:
        from hexawyn.mcp.tools.check_cluster_certificate_health import (
            check_cluster_certificate_health,
        )

        with patch(
            "hexawyn.mcp.server.build_cluster_certificate_health_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = check_cluster_certificate_health()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.check_cluster_certificate_health")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
