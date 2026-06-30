from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class ResourceCost:
    name: str
    kind: str  # "namespace"
    monthly_cost_usd: float
    percentage: float  # % of total cluster cost


@dataclass(frozen=True)
class BillingEvent:
    date: str  # "2026-06-30"
    description: str
    cost_impact_usd: float  # positive = surcoût, negative = économie
    provider: str  # "aws" | "azure" | "gcp"


@dataclass
class CostForecast:
    cluster_name: str
    month: str  # "2026-06"
    days_elapsed: int
    days_remaining: int
    current_spend_usd: float
    projected_total_usd: float
    previous_month_usd: float | None
    month_over_month_delta: float  # percentage, None-safe
    trend_factor: float  # >1.0 = acceleration
    top_cost_drivers: list[ResourceCost] = field(default_factory=list)
    billing_events: list[BillingEvent] = field(default_factory=list)
    forecast_confidence: str = "low"  # "low" | "medium" | "high"
    historical_days_used: int = 0
    data_source: str = "estimated"  # "estimated" | "aws" | "azure" | "gcp"
