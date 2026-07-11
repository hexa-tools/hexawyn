from abc import ABC, abstractmethod
from typing import TypedDict


class MonthlyCostRaw(TypedDict):
    month: str
    total_usd: float
    compute_usd: float
    storage_usd: float
    network_usd: float


class BudgetProjectionPort(ABC):
    """Driven port — provides historical monthly cost, split by category.

    A secondary adapter aggregates the underlying daily cost source into whole
    months and attributes each month's spend to compute / storage / network.
    """

    @abstractmethod
    def get_monthly_cost_history(self, months: int) -> list[MonthlyCostRaw]:
        """Return up to *months* of historical monthly cost, oldest first.

        Raises ClusterUnreachableError on cost-source failures.
        """
