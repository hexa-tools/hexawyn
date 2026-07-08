from __future__ import annotations

from hexawyn.application.ports.driven.deployment_latency_comparison_port import (
    DeploymentLatencyComparisonPort,
)
from hexawyn.domain.models.deployment_latency import DeploymentComparisonRequest, WindowLatency


class OTelDeploymentComparisonAdapter(DeploymentLatencyComparisonPort):
    def fetch_pre_deploy_latency(self, request: DeploymentComparisonRequest) -> WindowLatency:
        return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def fetch_post_deploy_latency(self, request: DeploymentComparisonRequest) -> WindowLatency:
        return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
