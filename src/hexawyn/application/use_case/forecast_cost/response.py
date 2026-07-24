from dataclasses import dataclass, field


@dataclass
class CostDriver:
    name: str = ""
    kind: str = ""
    monthly_cost_usd: float = 0.0
    percentage: float = 0.0


@dataclass
class CostForecastResult:
    cluster_name: str = ""
    month: str = ""
    days_elapsed: int = 0
    days_remaining: int = 0
    current_spend_usd: float = 0.0
    projected_total_usd: float = 0.0
    previous_month_usd: float | None = None
    month_over_month_delta: float = 0.0
    trend_factor: float = 1.0
    top_cost_drivers: list[CostDriver] = field(default_factory=list)
    forecast_confidence: str = "low"
    historical_days_used: int = 0
    data_source: str = "estimated"


@dataclass
class ForecastCostResponse:
    forecast: CostForecastResult = field(default_factory=CostForecastResult)
    error: str | None = None
