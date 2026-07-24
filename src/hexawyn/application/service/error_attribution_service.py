from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.error_attribution_port import ErrorAttributionPort
from hexawyn.application.use_case.error_attribution.command import (
    ErrorAttributionCommand,
)
from hexawyn.application.use_case.error_attribution.response import (
    ErrorAttributionResponse,
)
from hexawyn.application.ports.driving.error_attribution.error_attribution_service_port import (
    ErrorAttributionServicePort,
)
from hexawyn.domain.models.error_attribution import ErrorAttributionRequest, ErrorAttributionResult


class ErrorAttributionService(ErrorAttributionServicePort):
    def __init__(self, port: ErrorAttributionPort) -> None:
        self._port = port

    def attribute(self, command: ErrorAttributionCommand) -> ErrorAttributionResponse:
        req = ErrorAttributionRequest(
            gateway=command.gateway, time_window_minutes=command.time_window_minutes
        )
        raw = self._port.fetch_error_attribution(req)
        r = ErrorAttributionResult.compute(request=req, raw_errors=raw)
        return ErrorAttributionResponse(
            gateway=r.gateway,
            total_errors=r.total_errors,
            attribution=[asdict(a) for a in r.attribution],
            pareto_culprit=r.pareto_culprit,
        )
