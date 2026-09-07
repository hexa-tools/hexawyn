# Auto-generated test for otel_deployment_comparison_adapter

from __future__ import annotations


class TestOtelDeploymentComparisonAdapterUnit:
    def test_returns_window(self) -> None:
        from hexawyn.domain.models.deployment_latency import DeploymentComparisonRequest
        from hexawyn.infrastructure.adapters.secondary.gitops.otel_deployment_comparison_adapter import (  # noqa: E501
            OTelDeploymentComparisonAdapter,
        )

        adapter = OTelDeploymentComparisonAdapter()
        result = adapter.fetch_pre_deploy_latency(DeploymentComparisonRequest(service_name="test"))
        assert result.sample_count >= 0
