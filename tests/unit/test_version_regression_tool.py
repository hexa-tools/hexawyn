from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.version_regression_port import VersionRegressionPort
from hexawyn.domain.models.version_regression import VersionMetrics


class TestVersionRegressionTool:
    def test_returns_regression(self) -> None:
        from hexawyn.mcp.tools.version_regression import version_regression

        with patch("hexawyn.mcp.server.build_version_regression_adapter") as m:
            a = MagicMock(spec=VersionRegressionPort)
            a.fetch_baseline_metrics.return_value = VersionMetrics(
                version="v1.2",
                p50_ms=45.0,
                p95_ms=120.0,
                p99_ms=150.0,
                error_rate_pct=0.1,
                request_count=5000,
            )
            a.fetch_current_metrics.return_value = VersionMetrics(
                version="v1.3",
                p50_ms=52.0,
                p95_ms=250.0,
                p99_ms=380.0,
                error_rate_pct=0.8,
                request_count=4000,
            )
            m.return_value = a
            r = version_regression(service_name="recommendation-service")
        assert r["error"] is None
        assert r["verdict"] == "regression_detected"
        assert len(r["flags"]) >= 2

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.version_regression import version_regression

        with patch(
            "hexawyn.mcp.server.build_version_regression_adapter",
            side_effect=RuntimeError("boom"),
        ):
            r = version_regression(service_name="x")
        assert r["error"] == "boom"


class TestBuildVersionRegressionAdapter:
    def test_returns_port(self) -> None:
        from hexawyn.application.ports.driven.version_regression_port import (
            VersionRegressionPort,
        )
        from hexawyn.mcp.server import build_version_regression_adapter

        assert isinstance(build_version_regression_adapter(), VersionRegressionPort)


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.version_regression")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
