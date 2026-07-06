from __future__ import annotations

from hexawyn.application.ports.driving.compute_mttr_trend.compute_mttr_trend_command import (
    ComputeMTTRTrendCommand,
)
from hexawyn.application.ports.driving.compute_mttr_trend.compute_mttr_trend_response import (
    ComputeMTTRTrendResponse,
)
from hexawyn.application.ports.driving.compute_mttr_trend.compute_mttr_trend_service_port import (
    ComputeMTTRTrendServicePort,
)


class ComputeMTTRTrendUseCase:
    def __init__(self, service: ComputeMTTRTrendServicePort) -> None:
        self._service = service

    def execute(self, command: ComputeMTTRTrendCommand) -> ComputeMTTRTrendResponse:
        return self._service.compute(command)
