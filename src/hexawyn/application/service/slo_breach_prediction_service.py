from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.slo_breach_prediction_port import SLOBreachPredictionPort
from hexawyn.application.ports.driving.slo_breach_prediction.slo_breach_prediction_command import (
    SLOBreachPredictionCommand,
)
from hexawyn.application.ports.driving.slo_breach_prediction.slo_breach_prediction_response import (
    SLOBreachPredictionResponse,
)
from hexawyn.application.ports.driving.slo_breach_prediction.slo_breach_prediction_service_port import (
    SLOBreachPredictionServicePort,
)
from hexawyn.domain.models.slo_breach_prediction import (
    SLOBreachPredictionRequest,
    SLOBreachPredictionResult,
)


class SLOBreachPredictionService(SLOBreachPredictionServicePort):
    def __init__(self, port: SLOBreachPredictionPort) -> None:
        self._port = port

    def predict(self, command: SLOBreachPredictionCommand) -> SLOBreachPredictionResponse:
        req = SLOBreachPredictionRequest(
            prediction_window_minutes=command.prediction_window_minutes
        )
        raw = self._port.fetch_trend_metrics(req)
        r = SLOBreachPredictionResult.compute(request=req, raw_metrics=raw)
        return SLOBreachPredictionResponse(
            at_risk=[asdict(a) for a in r.at_risk], safe_count=r.safe_count
        )
