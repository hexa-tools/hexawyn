from __future__ import annotations

from hexawyn.application.ports.driven.version_regression_port import VersionRegressionPort
from hexawyn.application.use_case.version_regression.command import VersionRegressionCommand
from hexawyn.application.use_case.version_regression.response import VersionRegressionResponse
from hexawyn.domain.models.version_regression import (
    VersionComparisonRequest,
    VersionComparisonResult,
)


class VersionRegressionUseCase:
    def __init__(self, port: VersionRegressionPort) -> None:
        self._port = port

    def execute(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        request = VersionComparisonRequest(
            service_name=command.service_name, time_window_minutes=command.time_window_minutes
        )
        baseline = self._port.fetch_baseline_metrics(request)
        current = self._port.fetch_current_metrics(request)
        result = VersionComparisonResult.compute(request, baseline, current)

        flags: list[dict[str, object]] = [
            {
                "metric": f.metric,
                "baseline_value": f.baseline_value,
                "current_value": f.current_value,
                "delta_pct": f.delta_pct,
                "severity": f.severity,
            }
            for f in result.flags
        ]

        return VersionRegressionResponse(
            service_name=result.service_name,
            baseline_version=result.baseline_version,
            current_version=result.current_version,
            verdict=result.verdict,
            p99_delta_pct=result.p99_delta_pct,
            error_delta_pct=result.error_delta_pct,
            flags=flags,
        )
