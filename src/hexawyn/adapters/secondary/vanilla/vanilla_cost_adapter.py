from __future__ import annotations

from hexawyn.application.ports.driven.cost_estimation_port import (
    CostEstimationPort,
    CostReportRaw,
)


class VanillaCostAdapter(CostEstimationPort):
    """Fallback cost estimator when no cloud billing API is available.

    Returns a zero-cost report — the Free tier relies on the configurable
    pricing engine (ECA-113), not on real billing APIs.
    """

    def estimate_cluster_cost(self, cluster_name: str) -> CostReportRaw:
        return CostReportRaw(
            cluster_name=cluster_name,
            namespace_costs=[],
            total_monthly_cost_usd=0.0,
            data_source="vanilla",
            currency="USD",
        )
