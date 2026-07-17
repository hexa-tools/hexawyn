from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.deployment_latency_comparison_port import (
    DeploymentLatencyComparisonPort,
)
from hexawyn.domain.models.deployment_latency import WindowLatency


class TestDeploymentLatencyTool:
    def test_returns_regression(self) -> None:
        from hexawyn.mcp.tools.deployment_latency import deployment_latency

        with patch("hexawyn.mcp.server.build_deployment_latency_comparison_adapter") as m:
            a = MagicMock(spec=DeploymentLatencyComparisonPort)
            a.fetch_pre_deploy_latency.return_value = WindowLatency(
                p50_ms=85.0,
                p95_ms=180.0,
                p99_ms=210.0,
                sample_count=5000,
            )
            a.fetch_post_deploy_latency.return_value = WindowLatency(
                p50_ms=92.0,
                p95_ms=310.0,
                p99_ms=450.0,
                sample_count=4000,
            )
            m.return_value = a
            r = deployment_latency(service_name="payment-service")
        assert r["error"] is None
        assert r["verdict"] == "regression"
        assert r["p99_delta_pct"] > 100

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.deployment_latency import deployment_latency

        with patch(
            "hexawyn.mcp.server.build_deployment_latency_comparison_adapter",
            side_effect=RuntimeError("boom"),
        ):
            r = deployment_latency(service_name="x")
        assert r["error"] == "boom"
