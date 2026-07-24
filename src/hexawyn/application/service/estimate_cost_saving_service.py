from __future__ import annotations

from hexawyn.application.ports.driven.cost_saving_estimation_port import (
    CostSavingEstimationPort,
)
from hexawyn.application.use_case.estimate_cost_saving.command import (
    EstimateCostSavingCommand,
)
from hexawyn.application.use_case.estimate_cost_saving.response import (
    EstimateCostSavingResponse,
)
from hexawyn.application.ports.driving.estimate_cost_saving.estimate_cost_saving_service_port import (
    EstimateCostSavingServicePort,
)
from hexawyn.domain.services.cost_saving.cost_saving_estimation_service import (
    RightSizingCostEstimationService,
)

_SIGNIFICANT_TREND_PCT = 0.10  # 10% change triggers trend flag


class EstimateCostSavingService(EstimateCostSavingServicePort):
    def __init__(self, cost_saving_port: CostSavingEstimationPort) -> None:
        self._port = cost_saving_port
        self._domain_service = RightSizingCostEstimationService()

    def estimate_cost_saving(
        self,
        command: EstimateCostSavingCommand,
    ) -> EstimateCostSavingResponse:
        pods_raw = self._port.get_pod_resource_data()
        previous_saving = self._port.get_previous_total_saving()

        report = self._domain_service.estimate(
            pods=[dict(p) for p in pods_raw],
            top_n=command.top_n,
            cpu_price=command.cpu_per_core_per_hour_usd,
            mem_price=command.memory_per_gb_per_hour_usd,
        )

        trend = _compute_trend(previous_saving, report.total_monthly_saving_usd)

        if report.total_monthly_saving_usd is not None:
            self._port.store_total_saving(report.total_monthly_saving_usd)

        return EstimateCostSavingResponse(
            report=report,
            previous_total_saving_usd=previous_saving,
            saving_trend=trend,
        )


def _compute_trend(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "stable"
