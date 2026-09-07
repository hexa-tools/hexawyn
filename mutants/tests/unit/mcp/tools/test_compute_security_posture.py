"""Unit tests for MCP tool: compute_security_posture."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestComputeSecurityPostureTool:
    def test_compute_security_posture_returns_dict(self) -> None:
        from hexawyn.mcp.tools.compute_security_posture import compute_security_posture

        mock_report = MagicMock()
        mock_report.overall_score_pct = 45.0
        mock_report.categories = [MagicMock(name="vulnerability")]
        mock_report.trend = "degrading"
        mock_report.previous_score_pct = 55.0
        mock_response = MagicMock()
        mock_response.result = mock_report
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_optimization_roi_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.compute_security_posture.ComputeSecurityPostureUseCase",
                return_value=mock_uc,
            ),
        ):
            result = compute_security_posture()

        assert isinstance(result, dict)
        assert "error" in result
        assert result.get("error") is None
        assert result.get("overall_score_pct") == 45.0  # noqa: PLR2004
        assert result.get("trend") == "degrading"
        assert result.get("previous_score_pct") == 55.0  # noqa: PLR2004

    def test_compute_security_posture_maps_domain_attributes(self) -> None:
        from hexawyn.domain.models.security_posture import (
            CategoryScore,
            SecurityPostureReport,
            WorkloadCompliance,
        )
        from hexawyn.mcp.tools.compute_security_posture import compute_security_posture

        workload = WorkloadCompliance(
            workload="payments-api",
            namespace="production",
            category="rbac",
            status="non_compliant",
            remediation_priority=1,
            detail="missing policy",
        )
        category = CategoryScore(
            category="rbac",
            total=1,
            compliant=0,
            non_compliant=1,
            exempt=0,
            score_pct=0.0,
            policy_defined=True,
            non_compliant_workloads=[workload],
        )
        report = SecurityPostureReport(
            overall_score_pct=42.0,
            categories=[category],
            remediation_order=[workload],
            trend="stable",
            previous_score_pct=50.0,
        )
        mock_response = MagicMock()
        mock_response.result = report
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_optimization_roi_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.compute_security_posture.ComputeSecurityPostureUseCase",
                return_value=mock_uc,
            ),
        ):
            result = compute_security_posture()

        assert result["categories"][0]["name"] == "rbac"
        assert result["remediation_order"][0]["resource"] == "payments-api"

    def test_compute_security_posture_handles_error(self) -> None:
        from hexawyn.mcp.tools.compute_security_posture import compute_security_posture

        with patch(
            "hexawyn.mcp.server.build_optimization_roi_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = compute_security_posture()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.compute_security_posture")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
