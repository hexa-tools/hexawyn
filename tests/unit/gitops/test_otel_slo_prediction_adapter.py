from __future__ import annotations

from unittest.mock import patch


class TestOtelSLOPredictionAdapterUnit:
    def test_returns_list(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_slo_prediction_adapter import (
            OTelSLOPredictionAdapter,
        )
        from hexawyn.domain.models.slo_breach_prediction import SLOBreachPredictionRequest

        adapter = OTelSLOPredictionAdapter()
        result = adapter.fetch_trend_metrics(SLOBreachPredictionRequest())
        assert isinstance(result, list)

    def test_metrics_populated_with_mocked_traces(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_slo_prediction_adapter import (
            OTelSLOPredictionAdapter,
        )
        from hexawyn.domain.models.slo_breach_prediction import SLOBreachPredictionRequest

        mock_traces = [
            {"traceID": "abcdef1234567890", "duration": 200000, "hasErrors": True},
        ]
        with patch(
            "hexawyn.adapters.secondary.gitops.otel_slo_prediction_adapter.search_jaeger_traces",
            return_value=mock_traces,
        ):
            adapter = OTelSLOPredictionAdapter()
            result = adapter.fetch_trend_metrics(SLOBreachPredictionRequest())
            assert len(result) == 1
            assert result[0]["trace_id"] == "abcdef1234567890"
