"""Unit tests for SLOBreachPredictionUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.slo_breach_prediction.slo_breach_prediction_service_port import (
    SLOBreachPredictionServicePort,
)
from hexawyn.application.use_case.slo_breach_prediction.slo_breach_prediction_use_case import (
    SLOBreachPredictionUseCase,
)


class TestSLOBreachPredictionUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=SLOBreachPredictionServicePort)
        use_case = SLOBreachPredictionUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.predict.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=SLOBreachPredictionServicePort)
        mock_service.predict.side_effect = RuntimeError("test error")
        use_case = SLOBreachPredictionUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
