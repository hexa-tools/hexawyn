from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.finops.forecast_cost.command import (
    ForecastCostCommand,
)
from hexawyn.application.use_case.finops.forecast_cost.forecast_cost_use_case import (
    ForecastCostUseCase,
)
from hexawyn.application.use_case.finops.forecast_cost.response import (
    ForecastCostResponse,
)


class TestForecastCostUseCase:
    def test_execute_returns_forecast_cost_response(self) -> None:
        port = MagicMock()
        port.get_daily_costs.return_value = []

        use_case = ForecastCostUseCase(cost_forecast_port=port)
        result = use_case.execute(ForecastCostCommand())

        assert isinstance(result, ForecastCostResponse)
        assert result.forecast.cluster_name == "default"

    def test_execute_calls_port_with_historical_days(self) -> None:
        port = MagicMock()
        port.get_daily_costs.return_value = []

        use_case = ForecastCostUseCase(cost_forecast_port=port)
        use_case.execute(ForecastCostCommand(historical_days=14))

        port.get_daily_costs.assert_called_once_with(14)

    def test_execute_respects_top_n_drivers(self) -> None:
        port = MagicMock()
        port.get_daily_costs.return_value = []

        use_case = ForecastCostUseCase(cost_forecast_port=port)
        result = use_case.execute(ForecastCostCommand(top_n_drivers=5))

        assert result.forecast.top_cost_drivers == []
