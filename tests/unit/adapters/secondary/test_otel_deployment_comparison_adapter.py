from __future__ import annotations

from hexawyn.adapters.secondary.gitops.otel_deployment_comparison_adapter import (
    OTelDeploymentComparisonAdapter,
)
from hexawyn.application.ports.driven.deployment_latency_comparison_port import (
    DeploymentLatencyComparisonPort,
)
from hexawyn.domain.models.deployment_latency import DeploymentComparisonRequest


class TestOTelDeploymentComparisonAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(OTelDeploymentComparisonAdapter(), DeploymentLatencyComparisonPort)

    def test_fetch_pre_returns_zero(self) -> None:
        r = OTelDeploymentComparisonAdapter().fetch_pre_deploy_latency(
            DeploymentComparisonRequest(service_name="x")
        )
        assert r.sample_count == 0

    def test_fetch_post_returns_zero(self) -> None:
        r = OTelDeploymentComparisonAdapter().fetch_post_deploy_latency(
            DeploymentComparisonRequest(service_name="x")
        )
        assert r.sample_count == 0
