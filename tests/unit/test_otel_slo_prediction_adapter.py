from __future__ import annotations

from hexawyn.adapters.secondary.gitops.otel_slo_prediction_adapter import (
    OTelSLOPredictionAdapter,
)
from hexawyn.application.ports.driven.slo_breach_prediction_port import (
    SLOBreachPredictionPort,
)
from hexawyn.domain.models.slo_breach_prediction import SLOBreachPredictionRequest


class TestOTelSLOPredictionAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(OTelSLOPredictionAdapter(), SLOBreachPredictionPort)

    def test_fetch_returns_empty(self) -> None:
        r = OTelSLOPredictionAdapter().fetch_trend_metrics(SLOBreachPredictionRequest())
        assert r == []
