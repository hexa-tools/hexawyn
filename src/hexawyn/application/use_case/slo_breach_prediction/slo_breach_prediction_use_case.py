from __future__ import annotations

from hexawyn.application.ports.driving.slo_breach_prediction.slo_breach_prediction_command import (
    SLOBreachPredictionCommand,
)
from hexawyn.application.ports.driving.slo_breach_prediction.slo_breach_prediction_response import (
    SLOBreachPredictionResponse,
)
from hexawyn.application.ports.driving.slo_breach_prediction.slo_breach_prediction_service_port import (
    SLOBreachPredictionServicePort,
)


class SLOBreachPredictionUseCase:
    def __init__(self, service: SLOBreachPredictionServicePort) -> None:
        self._svc = service

    def execute(self, cmd: SLOBreachPredictionCommand) -> SLOBreachPredictionResponse:
        return self._svc.predict(cmd)
