from __future__ import annotations

from hexawyn.application.ports.driven.canary_comparison_port import CanaryComparisonPort
from hexawyn.application.use_case.pipelines.canary_comparison.command import (
    CanaryComparisonCommand,
)
from hexawyn.application.use_case.pipelines.canary_comparison.response import (
    CanaryComparisonResponse,
)
from hexawyn.domain.models.canary_comparison import CanaryComparisonRequest, ComparisonResult


class CanaryComparisonUseCase:
    def __init__(self, port: CanaryComparisonPort) -> None:
        self._port = port

    def execute(self, command: CanaryComparisonCommand) -> CanaryComparisonResponse:
        req = CanaryComparisonRequest(
            service_name=command.service_name,
            time_window_minutes=command.time_window_minutes,
            traffic_split_pct=command.traffic_split_pct,
        )
        stable = self._port.fetch_stable_metrics(req)
        canary = self._port.fetch_canary_metrics(req)
        result = ComparisonResult.compute(
            canary=canary,
            stable=stable,
            traffic_split_pct=req.traffic_split_pct,
            min_sample_threshold=req.min_sample_threshold,
        )
        return CanaryComparisonResponse(
            service_name=command.service_name,
            canary_version=result.canary_version,
            stable_version=result.stable_version,
            verdict=result.verdict.value,
            confidence=result.confidence.value,
            p99_delta_pct=result.p99_delta_pct,
            error_rate_delta_pct=result.error_rate_delta_pct,
            canary_count=result.canary_count,
            stable_count=result.stable_count,
            traffic_split_pct=result.traffic_split_pct,
            reasons=result.reasons,
        )
