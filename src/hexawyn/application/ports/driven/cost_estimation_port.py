from abc import ABC, abstractmethod
from typing import TypedDict


class NamespaceCostRaw(TypedDict):
    namespace: str
    monthly_cost_usd: float


class CostReportRaw(TypedDict):
    cluster_name: str
    namespace_costs: list[NamespaceCostRaw]
    total_monthly_cost_usd: float
    data_source: str
    currency: str


class CostEstimationPort(ABC):
    """Driven port — real cloud billing costs per namespace and cluster.

    Implemented by cloud-provider billing APIs (AWS Cost Explorer, Azure Cost
    Management, GCP Cloud Billing) and by a vanilla estimator fallback.
    All implementations are read-only — no write permissions required.
    """

    @abstractmethod
    def estimate_cluster_cost(self, cluster_name: str) -> CostReportRaw:
        """Return the real (or estimated) monthly cost for *cluster_name*.

        Raises ClusterUnreachableError when the billing API is unreachable.
        Raises InsufficientPermissionsError when credentials are missing.
        """
