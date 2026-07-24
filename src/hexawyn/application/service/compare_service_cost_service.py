from __future__ import annotations

from calendar import monthrange
from datetime import UTC, datetime

from hexawyn.application.ports.driven.service_cost_port import ServiceCostPort
from hexawyn.application.use_case.compare_service_cost.command import (
    CompareServiceCostCommand,
)
from hexawyn.application.use_case.compare_service_cost.response import (
    CompareServiceCostResponse,
)
from hexawyn.application.ports.driving.compare_service_cost.compare_service_cost_service_port import (
    CompareServiceCostServicePort,
)
from hexawyn.domain.services.service_cost.service_cost_comparison_engine import (
    ServiceCostComparisonEngine,
)


class CompareServiceCostService(CompareServiceCostServicePort):
    def __init__(self, cost_port: ServiceCostPort) -> None:
        self._port = cost_port
        self._engine = ServiceCostComparisonEngine()

    def compare(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        now = datetime.now(UTC)
        current_month = now.strftime("%Y-%m")
        current_days = now.day

        if now.month == 1:
            previous_month = f"{now.year - 1}-12"
            previous_days = 31
        else:
            previous_month = f"{now.year}-{now.month - 1:02d}"
            previous_days = monthrange(now.year, now.month - 1)[1]

        current_pods_raw = self._port.fetch_pod_resources(command.service_name, current_month)
        previous_pods_raw = self._port.fetch_pod_resources(command.service_name, previous_month)

        current_pods: list[dict[str, object]] = [dict(p) for p in current_pods_raw]
        previous_pods: list[dict[str, object]] = [dict(p) for p in previous_pods_raw]

        result = self._engine.compute(
            service_name=command.service_name,
            current_month=current_month,
            current_days=current_days,
            previous_month=previous_month,
            previous_days=previous_days,
            current_pods=current_pods,
            previous_pods=previous_pods,
            cpu_price_per_core_hour=command.cpu_price_per_core_hour,
            memory_price_per_gb_hour=command.memory_price_per_gb_hour,
        )
        return CompareServiceCostResponse(result=result)
