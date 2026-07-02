from __future__ import annotations

from hexawyn.application.ports.driven.deployment_latency_comparison_port import (
    DeploymentLatencyComparisonPort,
)
from hexawyn.application.ports.driving.deployment_latency.deployment_latency_command import (
    DeploymentLatencyCommand,
)
from hexawyn.application.ports.driving.deployment_latency.deployment_latency_response import (
    DeploymentLatencyResponse,
)
from hexawyn.application.ports.driving.deployment_latency.deployment_latency_service_port import (
    DeploymentLatencyServicePort,
)
from hexawyn.domain.models.deployment_latency import (
    DeploymentComparisonRequest,
    DeploymentComparisonResult,
)


class DeploymentLatencyService(DeploymentLatencyServicePort):
    def __init__(self, port: DeploymentLatencyComparisonPort) -> None:
        self._port = port

    def compare(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        req = DeploymentComparisonRequest(
            service_name=command.service_name,
            regression_threshold_pct=command.regression_threshold_pct,
        )
        before = self._port.fetch_pre_deploy_latency(req)
        after = self._port.fetch_post_deploy_latency(req)
        r = DeploymentComparisonResult.compute(request=req, before=before, after=after)
        return DeploymentLatencyResponse(
            service_name=r.service_name,
            verdict=r.verdict.value,
            p50_delta_pct=r.p50_delta_pct,
            p95_delta_pct=r.p95_delta_pct,
            p99_delta_pct=r.p99_delta_pct,
            before_p99_ms=r.before.p99_ms,
            after_p99_ms=r.after.p99_ms,
            suggestion=r.suggestion,
        )
