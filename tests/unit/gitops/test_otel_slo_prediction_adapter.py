# Auto-generated test for otel_slo_prediction_adapter

from __future__ import annotations


class TestOtelSLOPredictionAdapterUnit:
    def test_returns_list(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_slo_prediction_adapter import (
            OTelSLOPredictionAdapter,
        )
        from hexawyn.domain.models.slo_breach_prediction import SLOBreachPredictionRequest

        adapter = OTelSLOPredictionAdapter()
        result = adapter.fetch_trend_metrics(SLOBreachPredictionRequest())
        assert isinstance(result, list)
