from dataclasses import dataclass


@dataclass(frozen=True)
class ForecastCostCommand:
    historical_days: int = 7
    top_n_drivers: int = 3
