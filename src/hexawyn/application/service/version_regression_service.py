from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.version_regression_port import VersionRegressionPort
from hexawyn.application.ports.driving.version_regression.version_regression_command import (
    VersionRegressionCommand,
)
from hexawyn.application.ports.driving.version_regression.version_regression_response import (
    VersionRegressionResponse,
)
from hexawyn.application.ports.driving.version_regression.version_regression_service_port import (
    VersionRegressionServicePort,
)
from hexawyn.domain.models.version_regression import (
    VersionComparisonRequest,
    VersionComparisonResult,
)


class VersionRegressionService(VersionRegressionServicePort):
    def __init__(self, port: VersionRegressionPort) -> None:
        self._port = port

    def detect(self, command: VersionRegressionCommand) -> VersionRegressionResponse:
        req = VersionComparisonRequest(
            service_name=command.service_name, time_window_minutes=command.time_window_minutes
        )
        base = self._port.fetch_baseline_metrics(req)
        curr = self._port.fetch_current_metrics(req)
        r = VersionComparisonResult.compute(request=req, baseline=base, current=curr)
        return VersionRegressionResponse(
            service_name=r.service_name,
            baseline_version=r.baseline_version,
            current_version=r.current_version,
            verdict=r.verdict,
            p99_delta_pct=r.p99_delta_pct,
            error_delta_pct=r.error_delta_pct,
            flags=[asdict(f) for f in r.flags],
        )
