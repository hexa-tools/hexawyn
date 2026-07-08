from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.cost_forecast import CostForecast


@dataclass
class ForecastCostResponse:
    forecast: CostForecast
