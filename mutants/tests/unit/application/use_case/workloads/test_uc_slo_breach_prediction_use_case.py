from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.workloads.slo_breach_prediction.command import (
    SLOBreachPredictionCommand,
)
from hexawyn.application.use_case.workloads.slo_breach_prediction.response import (
    SLOBreachPredictionResponse,
)
from hexawyn.application.use_case.workloads.slo_breach_prediction.slo_breach_prediction_use_case import (  # noqa: E501
    SLOBreachPredictionUseCase,
)


class TestSLOBreachPredictionUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.fetch_trend_metrics.return_value = []

        use_case = SLOBreachPredictionUseCase(port=port)
        result = use_case.execute(SLOBreachPredictionCommand())

        assert isinstance(result, SLOBreachPredictionResponse)

    def test_execute_empty_metrics(self) -> None:
        port = MagicMock()
        port.fetch_trend_metrics.return_value = []

        use_case = SLOBreachPredictionUseCase(port=port)
        result = use_case.execute(SLOBreachPredictionCommand())

        assert isinstance(result, SLOBreachPredictionResponse)
