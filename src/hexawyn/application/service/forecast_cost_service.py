from __future__ import annotations

import calendar
from datetime import date

from hexawyn.application.ports.driven.cost_forecast_port import CostForecastPort
from hexawyn.application.ports.driving.forecast_cost.forecast_cost_command import (
    ForecastCostCommand,
)
from hexawyn.application.ports.driving.forecast_cost.forecast_cost_response import (
    ForecastCostResponse,
)
from hexawyn.application.ports.driving.forecast_cost.forecast_cost_service_port import (
    ForecastCostServicePort,
)
from hexawyn.domain.services.cost_forecast.cost_forecast_engine import CostForecastEngine


class ForecastCostService(ForecastCostServicePort):
    def __init__(
        self,
        cost_forecast_port: CostForecastPort,
        cluster_name: str = "default",
        data_source: str = "estimated",
        forecast_confidence: str = "low",
    ) -> None:
        self._port = cost_forecast_port
        self._cluster_name = cluster_name
        self._data_source = data_source
        self._forecast_confidence = forecast_confidence
        self._engine = CostForecastEngine()

    def forecast_cost(self, command: ForecastCostCommand) -> ForecastCostResponse:
        daily_costs = self._port.get_daily_costs(command.historical_days)
        today = date.today()
        days_elapsed = today.day
        days_in_month = calendar.monthrange(today.year, today.month)[1]
        month = today.strftime("%Y-%m")

        forecast = self._engine.forecast(
            daily_costs=[dict(d) for d in daily_costs],
            cluster_name=self._cluster_name,
            month=month,
            days_elapsed=days_elapsed,
            days_in_month=days_in_month,
            top_n=command.top_n_drivers,
            data_source=self._data_source,
            forecast_confidence=self._forecast_confidence,
        )
        return ForecastCostResponse(forecast=forecast)
