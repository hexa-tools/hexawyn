from __future__ import annotations

from hexawyn.application.ports.driven.rightsizing_port import RightsizingPort
from hexawyn.application.use_case.estimate_rightsizing_savings.command import (
    EstimateRightsizingSavingsCommand,
)
from hexawyn.application.use_case.estimate_rightsizing_savings.response import (
    EstimateRightsizingSavingsResponse,
    RightsizingRecommendation,
    RightsizingReport,
)


class EstimateRightsizingSavingsUseCase:
    def __init__(self, port: RightsizingPort) -> None:
        self._port = port

    def execute(
        self, command: EstimateRightsizingSavingsCommand
    ) -> EstimateRightsizingSavingsResponse:
        raw_data = self._port.get_workload_rightsizing_data()

        recommendations: list[RightsizingRecommendation] = []
        skipped = 0
        total_savings = 0.0
        metrics_available = True

        for wl in raw_data:
            cpu_req = wl["cpu_requested_cores"]
            mem_req = wl["memory_requested_mi"]
            cpu_act = wl.get("cpu_actual_cores")
            mem_act = wl.get("memory_actual_mi")

            if cpu_act is None or mem_act is None:
                metrics_available = False
                skipped += 1
                continue

            rec_cpu = cpu_act * 1.2
            rec_mem = mem_act * 1.2
            cpu_saving = max(0.0, cpu_req - rec_cpu)
            mem_saving = max(0.0, mem_req - rec_mem)
            monthly_saving = cpu_saving * 0.03 * 730 + (mem_saving / 1024) * 0.01 * 730
            waste_pct = ((cpu_req - rec_cpu) / cpu_req * 100) if cpu_req > 0 else 0.0

            rtype = "oversized" if cpu_saving > 0 or mem_saving > 0 else "optimized"
            priority = "high" if monthly_saving > 50 else "medium" if monthly_saving > 10 else "low"

            recommendations.append(
                RightsizingRecommendation(
                    resource_name=wl["resource_name"],
                    namespace=wl["namespace"],
                    kind=wl["kind"],
                    rightsizing_type=rtype,
                    current_cpu_cores=cpu_req,
                    recommended_cpu_cores=round(rec_cpu, 2),
                    current_memory_mi=mem_req,
                    recommended_memory_mi=round(rec_mem, 1),
                    monthly_savings_usd=round(monthly_saving, 2),
                    waste_percentage=round(waste_pct, 1),
                    reason=f"p95 actual {cpu_act:.2f} cores / {mem_act:.1f} Mi vs request",
                    priority=priority,
                )
            )
            total_savings += monthly_saving

        recommendations.sort(key=lambda r: r.monthly_savings_usd, reverse=True)
        top = recommendations[: command.top_n]

        report = RightsizingReport(
            recommendations=top,
            total_monthly_savings_usd=round(total_savings, 2),
            skipped_count=skipped,
        )
        return EstimateRightsizingSavingsResponse(
            report=report, metrics_server_available=metrics_available
        )
