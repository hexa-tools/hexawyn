from __future__ import annotations

from hexawyn.application.ports.driven.slo_breach_prediction_port import SLOBreachPredictionPort
from hexawyn.domain.models.slo_breach_prediction import SLOBreachPredictionRequest


class OTelSLOPredictionAdapter(SLOBreachPredictionPort):
    def fetch_trend_metrics(self, request: SLOBreachPredictionRequest) -> list[dict[str, object]]:
        return []
