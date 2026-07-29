# Auto-generated test for otel_deployment_comparison_adapter

from __future__ import annotations


class TestOtelDeploymentComparisonAdapterUnit:
    def test_returns_window(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_deployment_comparison_adapter import (
            OTelDeploymentComparisonAdapter,
        )
        from hexawyn.domain.models.deployment_latency import DeploymentComparisonRequest

        adapter = OTelDeploymentComparisonAdapter()
        result = adapter.fetch_pre_deploy_latency(DeploymentComparisonRequest(service_name="test"))
        assert result.sample_count >= 0
