from __future__ import annotations

from hexawyn.application.ports.driven.cost_saving_estimation_port import CostSavingEstimationPort
from hexawyn.application.use_case.estimate_cost_saving.command import EstimateCostSavingCommand
from hexawyn.application.use_case.estimate_cost_saving.response import (
    CostSavingReport,
    EstimateCostSavingResponse,
    NamespaceSaving,
    SavingOpportunity,
)


class EstimateCostSavingUseCase:
    def __init__(self, port: CostSavingEstimationPort) -> None:
        self._port = port

    def execute(self, command: EstimateCostSavingCommand) -> EstimateCostSavingResponse:
        all_data = self._port.get_pod_resource_data()
        previous_total = self._port.get_previous_total_saving()

        cpu_price = command.cpu_per_core_per_hour_usd
        mem_price = command.memory_per_gb_per_hour_usd
        pricing_configured = cpu_price is not None and mem_price is not None
        hours_per_month = 730.0

        opportunities: list[SavingOpportunity] = []
        namespaces: dict[str, list[float]] = {}
        total_delta_cores = 0.0
        total_delta_mem = 0.0
        pods_analyzed = 0
        pods_excluded = 0

        for pod in all_data:
            cpu_req = pod.get("cpu_request_cores")
            mem_req = pod.get("memory_request_mi")
            cpu_p95 = pod.get("cpu_p95_cores")
            mem_p95 = pod.get("memory_p95_mi")
            hpa = pod.get("hpa_enabled", False)

            if cpu_req is None and mem_req is None:
                pods_excluded += 1
                continue

            pods_analyzed += 1

            cpu_req_val = cpu_req or 0.0
            mem_req_val = mem_req or 0.0
            cpu_p95_val = cpu_p95 or 0.0
            mem_p95_val = mem_p95 or 0.0

            delta_cores = max(0.0, cpu_req_val - cpu_p95_val)
            delta_mem = max(0.0, mem_req_val - mem_p95_val)

            if delta_cores <= 0 and delta_mem <= 0:
                continue

            rec_cpu = cpu_p95_val if cpu_req is not None else None
            rec_mem = mem_p95_val if mem_req is not None else None

            saving_usd: float | None = None
            if pricing_configured:
                saving_usd = (
                    delta_cores * (cpu_price or 0.0) * hours_per_month
                    + (delta_mem / 1024) * (mem_price or 0.0) * hours_per_month
                )

            caveats: list[str] = []
            if hpa:
                caveats.append("HPA adjusts replicas — savings depend on average replica count")
            bursty = (
                pod.get("cpu_max_cores") is not None
                and pod.get("cpu_p95_cores") is not None
                and (pod.get("cpu_max_cores") or 0) > (pod.get("cpu_p95_cores") or 0) * 1.5
            )

            opportunities.append(
                SavingOpportunity(
                    pod_name=pod["pod_name"],
                    namespace=pod["namespace"],
                    current_cpu_request=cpu_req_val,
                    recommended_cpu_request=rec_cpu,
                    current_memory_request_mi=mem_req_val,
                    recommended_memory_request_mi=rec_mem,
                    delta_cores=delta_cores,
                    delta_memory_mi=delta_mem,
                    monthly_saving_usd=round(saving_usd, 2) if saving_usd is not None else None,
                    hpa_enabled=hpa,
                    is_bursty=bursty,
                    caveats=caveats,
                )
            )

            total_delta_cores += delta_cores
            total_delta_mem += delta_mem
            ns = namespaces.setdefault(pod["namespace"], [0.0, 0.0, 0.0, 0])
            ns[0] += 1
            ns[1] += delta_cores
            ns[2] += delta_mem
            ns[3] += saving_usd or 0.0

        opportunities.sort(key=lambda o: o.monthly_saving_usd or 0.0, reverse=True)
        top = opportunities[: command.top_n]

        ns_savings = sorted(
            [
                NamespaceSaving(
                    namespace=ns,
                    pod_count=int(v[0]),
                    total_delta_cores=v[1],
                    total_delta_memory_mi=v[2],
                    total_monthly_saving_usd=round(v[3], 2) if v[3] > 0 else None,
                )
                for ns, v in namespaces.items()
            ],
            key=lambda n: n.total_monthly_saving_usd or 0.0,
            reverse=True,
        )

        total_saving = sum(o.monthly_saving_usd or 0.0 for o in opportunities)
        self._port.store_total_saving(total_saving)

        saving_trend: str | None = None
        if previous_total is not None and total_saving > 0:
            if total_saving > previous_total * 1.1:
                saving_trend = "increasing"
            elif total_saving < previous_total * 0.9:
                saving_trend = "decreasing"
            else:
                saving_trend = "stable"

        report = CostSavingReport(
            top_opportunities=top,
            namespace_savings=ns_savings[: command.top_n],
            total_monthly_saving_usd=round(total_saving, 2) if pricing_configured else None,
            total_delta_cores=round(total_delta_cores, 3),
            total_delta_memory_mi=round(total_delta_mem, 1),
            pods_analyzed=pods_analyzed,
            pods_excluded=pods_excluded,
            pricing_configured=pricing_configured,
        )
        return EstimateCostSavingResponse(
            report=report, previous_total_saving_usd=previous_total, saving_trend=saving_trend
        )
