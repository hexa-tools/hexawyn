from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TypedDict


class NamespaceCostData(TypedDict):
    name: str
    cost_usd: float


class DailyCostData(TypedDict):
    date: str  # "2026-06-22"
    total_usd: float
    namespace_costs: list[NamespaceCostData]


class CostForecastPort(ABC):
    @abstractmethod
    def get_daily_costs(self, days: int) -> list[DailyCostData]: ...
