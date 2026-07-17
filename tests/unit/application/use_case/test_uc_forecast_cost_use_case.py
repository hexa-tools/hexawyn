"""Unit tests for ForecastCostUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.forecast_cost.forecast_cost_service_port import (
    ForecastCostServicePort,
)
from hexawyn.application.use_case.forecast_cost.forecast_cost_use_case import ForecastCostUseCase


class TestForecastCostUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=ForecastCostServicePort)
        use_case = ForecastCostUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.forecast_cost.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=ForecastCostServicePort)
        mock_service.forecast_cost.side_effect = RuntimeError("test error")
        use_case = ForecastCostUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
