from __future__ import annotations

from hexawyn.application.ports.driven.deployment_latency_comparison_port import (
    DeploymentLatencyComparisonPort,
)
from hexawyn.application.use_case.deployment_latency.command import DeploymentLatencyCommand
from hexawyn.application.use_case.deployment_latency.response import DeploymentLatencyResponse
from hexawyn.domain.models.deployment_latency import (
    DeploymentComparisonRequest,
    DeploymentComparisonResult,
)


class DeploymentLatencyUseCase:
    def __init__(self, port: DeploymentLatencyComparisonPort) -> None:
        self._port = port

    def execute(self, command: DeploymentLatencyCommand) -> DeploymentLatencyResponse:
        request = DeploymentComparisonRequest(
            service_name=command.service_name,
            regression_threshold_pct=command.regression_threshold_pct,
        )
        before = self._port.fetch_pre_deploy_latency(request)
        after = self._port.fetch_post_deploy_latency(request)
        result = DeploymentComparisonResult.compute(request, before, after)
        return DeploymentLatencyResponse(
            service_name=result.service_name,
            verdict=result.verdict.value,
            p50_delta_pct=result.p50_delta_pct,
            p95_delta_pct=result.p95_delta_pct,
            p99_delta_pct=result.p99_delta_pct,
            before_p99_ms=result.before.p99_ms,
            after_p99_ms=result.after.p99_ms,
            suggestion=result.suggestion,
        )
