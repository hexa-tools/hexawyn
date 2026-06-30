from __future__ import annotations

from hexawyn.domain.models.cost_saving_estimation import (
    CostSavingReport,
    NamespaceSaving,
    PodSavingOpportunity,
)

_P95_BUFFER = 1.2
_OPTIMAL_RATIO = 0.9
_MIN_CPU_CORES = 0.01  # 10m minimum
_MIN_MEM_MI = 64.0  # 64Mi minimum
_HOURS_PER_MONTH = 24 * 30  # 720
_BURSTY_MAX_P95_RATIO = 2.5  # max/p95 > 2.5 → bursty workload


class RightSizingCostEstimationService:
    """Pure domain service — no infra deps, no try/catch."""

    def estimate(
        self,
        pods: list[dict[str, object]],
        top_n: int,
        cpu_price: float | None,
        mem_price: float | None,
    ) -> CostSavingReport:
        pricing_configured = cpu_price is not None or mem_price is not None
        opportunities: list[PodSavingOpportunity] = []
        pods_excluded = 0

        for pod in pods:
            result = _analyze_pod(pod, cpu_price, mem_price)
            if result is None:
                pods_excluded += 1
                continue
            opportunities.append(result)

        ranked = _rank_opportunities(opportunities, top_n)
        namespace_savings = _aggregate_by_namespace(opportunities)
        total_delta_cores = round(sum(o.delta_cores for o in opportunities), 3)
        total_delta_mi = round(sum(o.delta_memory_mi for o in opportunities), 1)

        total_usd: float | None = None
        if pricing_configured:
            total_usd = round(
                sum(
                    o.monthly_saving_usd for o in opportunities if o.monthly_saving_usd is not None
                ),
                2,
            )

        return CostSavingReport(
            top_opportunities=ranked,
            namespace_savings=sorted(
                namespace_savings, key=lambda n: n.total_monthly_saving_usd or 0.0, reverse=True
            ),
            total_monthly_saving_usd=total_usd,
            total_delta_cores=total_delta_cores,
            total_delta_memory_mi=total_delta_mi,
            pods_analyzed=len(opportunities),
            pods_excluded=pods_excluded,
            pricing_configured=pricing_configured,
        )


def _analyze_pod(
    pod: dict[str, object],
    cpu_price: float | None,
    mem_price: float | None,
) -> PodSavingOpportunity | None:
    cpu_req = _f(pod.get("cpu_request_cores"))
    mem_req = _f(pod.get("memory_request_mi"))
    cpu_limit = _f(pod.get("cpu_limit_cores"))
    mem_limit = _f(pod.get("memory_limit_mi"))

    # Effective request: use limit when request is absent
    eff_cpu = cpu_req if cpu_req is not None else cpu_limit
    eff_mem = mem_req if mem_req is not None else mem_limit

    if eff_cpu is None and eff_mem is None:
        return None  # no request/limit → can't compute delta

    cpu_p95 = _f(pod.get("cpu_p95_cores"))
    mem_p95 = _f(pod.get("memory_p95_mi"))
    cpu_max = _f(pod.get("cpu_max_cores"))

    if cpu_p95 is None and mem_p95 is None:
        return None  # no actual usage data → can't right-size

    if _is_optimal(eff_cpu, eff_mem, cpu_p95, mem_p95):
        return None  # already well-sized → excluded

    rec_cpu = _recommended(eff_cpu, cpu_p95)
    rec_mem = _recommended(eff_mem, mem_p95)

    delta_cores = round(max(0.0, (eff_cpu or 0.0) - (rec_cpu or eff_cpu or 0.0)), 3)
    delta_mi = round(max(0.0, (eff_mem or 0.0) - (rec_mem or eff_mem or 0.0)), 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores * (cpu_price or 0.0) * _HOURS_PER_MONTH
        mem_saving = (delta_mi / 1024.0) * (mem_price or 0.0) * _HOURS_PER_MONTH
        monthly_usd = round(cpu_saving + mem_saving, 2)

    hpa_enabled = bool(pod.get("hpa_enabled"))
    is_bursty = _bursty(cpu_p95, cpu_max)

    caveats: list[str] = []
    if hpa_enabled:
        hpa_min = pod.get("hpa_min_replicas")
        caveats.append(
            f"HPA enabled (min_replicas={hpa_min}): right-size applies per-pod, "
            "adjust HPA min_replicas separately"
        )
    if is_bursty:
        caveats.append(
            "Bursty workload detected: right-sizing based on 7d p95 may cause OOM under peak"
        )

    return PodSavingOpportunity(
        pod_name=str(pod.get("pod_name", "")),
        namespace=str(pod.get("namespace", "")),
        current_cpu_request=eff_cpu,
        recommended_cpu_request=rec_cpu,
        current_memory_request_mi=eff_mem,
        recommended_memory_request_mi=rec_mem,
        delta_cores=delta_cores,
        delta_memory_mi=delta_mi,
        monthly_saving_usd=monthly_usd,
        hpa_enabled=hpa_enabled,
        is_bursty=is_bursty,
        caveats=caveats,
    )


def _is_optimal(
    eff_cpu: float | None,
    eff_mem: float | None,
    cpu_p95: float | None,
    mem_p95: float | None,
) -> bool:
    ratios: list[float] = []
    if eff_cpu is not None and eff_cpu > 0 and cpu_p95 is not None:
        ratios.append(cpu_p95 / eff_cpu)
    if eff_mem is not None and eff_mem > 0 and mem_p95 is not None:
        ratios.append(mem_p95 / eff_mem)
    return bool(ratios) and all(r >= _OPTIMAL_RATIO for r in ratios)


def _recommended(request: float | None, p95: float | None) -> float | None:
    if p95 is None or request is None:
        return request
    rec = p95 * _P95_BUFFER
    if request > 0.1:  # CPU vs memory threshold
        return round(max(rec, _MIN_CPU_CORES), 3)
    return round(max(rec, _MIN_MEM_MI), 1)


def _bursty(cpu_p95: float | None, cpu_max: float | None) -> bool:
    if cpu_p95 is None or cpu_max is None or cpu_p95 <= 0:
        return False
    return cpu_max / cpu_p95 > _BURSTY_MAX_P95_RATIO


def _rank_opportunities(
    opportunities: list[PodSavingOpportunity], top_n: int
) -> list[PodSavingOpportunity]:
    return sorted(
        opportunities,
        key=lambda o: o.monthly_saving_usd if o.monthly_saving_usd is not None else 0.0,
        reverse=True,
    )[:top_n]


class _NsAccumulator:
    def __init__(self) -> None:
        self.pod_count: int = 0
        self.delta_cores: float = 0.0
        self.delta_mi: float = 0.0
        self.usd: float = 0.0
        self.has_usd: bool = False


def _aggregate_by_namespace(
    opportunities: list[PodSavingOpportunity],
) -> list[NamespaceSaving]:
    ns_map: dict[str, _NsAccumulator] = {}
    for o in opportunities:
        if o.namespace not in ns_map:
            ns_map[o.namespace] = _NsAccumulator()
        acc = ns_map[o.namespace]
        acc.pod_count += 1
        acc.delta_cores += o.delta_cores
        acc.delta_mi += o.delta_memory_mi
        if o.monthly_saving_usd is not None:
            acc.usd += o.monthly_saving_usd
            acc.has_usd = True

    return [
        NamespaceSaving(
            namespace=ns,
            pod_count=acc.pod_count,
            total_delta_cores=round(acc.delta_cores, 3),
            total_delta_memory_mi=round(acc.delta_mi, 1),
            total_monthly_saving_usd=round(acc.usd, 2) if acc.has_usd else None,
        )
        for ns, acc in ns_map.items()
    ]


def _f(value: object) -> float | None:
    if value is None:
        return None
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return None
