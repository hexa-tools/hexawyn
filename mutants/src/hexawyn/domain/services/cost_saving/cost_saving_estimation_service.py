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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut: MutantDict = {}  # type: ignore


class RightSizingCostEstimationService:
    """Pure domain service — no infra deps, no try/catch."""

    @_mutmut_mutated(mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut)
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_orig(
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_1(
        self,
        pods: list[dict[str, object]],
        top_n: int,
        cpu_price: float | None,
        mem_price: float | None,
    ) -> CostSavingReport:
        pricing_configured = None
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_2(
        self,
        pods: list[dict[str, object]],
        top_n: int,
        cpu_price: float | None,
        mem_price: float | None,
    ) -> CostSavingReport:
        pricing_configured = cpu_price is not None and mem_price is not None
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_3(
        self,
        pods: list[dict[str, object]],
        top_n: int,
        cpu_price: float | None,
        mem_price: float | None,
    ) -> CostSavingReport:
        pricing_configured = cpu_price is None or mem_price is not None
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_4(
        self,
        pods: list[dict[str, object]],
        top_n: int,
        cpu_price: float | None,
        mem_price: float | None,
    ) -> CostSavingReport:
        pricing_configured = cpu_price is not None or mem_price is None
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_5(
        self,
        pods: list[dict[str, object]],
        top_n: int,
        cpu_price: float | None,
        mem_price: float | None,
    ) -> CostSavingReport:
        pricing_configured = cpu_price is not None or mem_price is not None
        opportunities: list[PodSavingOpportunity] = None
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_6(
        self,
        pods: list[dict[str, object]],
        top_n: int,
        cpu_price: float | None,
        mem_price: float | None,
    ) -> CostSavingReport:
        pricing_configured = cpu_price is not None or mem_price is not None
        opportunities: list[PodSavingOpportunity] = []
        pods_excluded = None

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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_7(
        self,
        pods: list[dict[str, object]],
        top_n: int,
        cpu_price: float | None,
        mem_price: float | None,
    ) -> CostSavingReport:
        pricing_configured = cpu_price is not None or mem_price is not None
        opportunities: list[PodSavingOpportunity] = []
        pods_excluded = 1

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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_8(
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
            result = None
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_9(
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
            result = _analyze_pod(None, cpu_price, mem_price)
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_10(
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
            result = _analyze_pod(pod, None, mem_price)
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_11(
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
            result = _analyze_pod(pod, cpu_price, None)
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_12(
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
            result = _analyze_pod(cpu_price, mem_price)
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_13(
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
            result = _analyze_pod(pod, mem_price)
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_14(
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
            result = _analyze_pod(pod, cpu_price, )
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_15(
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
            if result is not None:
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_16(
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
                pods_excluded = 1
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_17(
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
                pods_excluded -= 1
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_18(
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
                pods_excluded += 2
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_19(
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
                break
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_20(
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
            opportunities.append(None)

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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_21(
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

        ranked = None
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_22(
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

        ranked = _rank_opportunities(None, top_n)
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_23(
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

        ranked = _rank_opportunities(opportunities, None)
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_24(
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

        ranked = _rank_opportunities(top_n)
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_25(
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

        ranked = _rank_opportunities(opportunities, )
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_26(
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
        namespace_savings = None
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_27(
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
        namespace_savings = _aggregate_by_namespace(None)
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_28(
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
        total_delta_cores = None
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_29(
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
        total_delta_cores = round(None, 3)
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_30(
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
        total_delta_cores = round(sum(o.delta_cores for o in opportunities), None)
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_31(
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
        total_delta_cores = round(3)
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_32(
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
        total_delta_cores = round(sum(o.delta_cores for o in opportunities), )
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_33(
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
        total_delta_cores = round(sum(None), 3)
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_34(
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
        total_delta_cores = round(sum(o.delta_cores for o in opportunities), 4)
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_35(
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
        total_delta_mi = None

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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_36(
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
        total_delta_mi = round(None, 1)

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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_37(
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
        total_delta_mi = round(sum(o.delta_memory_mi for o in opportunities), None)

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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_38(
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
        total_delta_mi = round(1)

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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_39(
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
        total_delta_mi = round(sum(o.delta_memory_mi for o in opportunities), )

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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_40(
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
        total_delta_mi = round(sum(None), 1)

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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_41(
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
        total_delta_mi = round(sum(o.delta_memory_mi for o in opportunities), 2)

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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_42(
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

        total_usd: float | None = ""
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_43(
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
            total_usd = None

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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_44(
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
                None,
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_45(
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
                None,
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_46(
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_47(
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_48(
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
                    None
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_49(
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
                    o.monthly_saving_usd for o in opportunities if o.monthly_saving_usd is None
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_50(
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
                3,
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_51(
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
            top_opportunities=None,
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_52(
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
            namespace_savings=None,
            total_monthly_saving_usd=total_usd,
            total_delta_cores=total_delta_cores,
            total_delta_memory_mi=total_delta_mi,
            pods_analyzed=len(opportunities),
            pods_excluded=pods_excluded,
            pricing_configured=pricing_configured,
        )

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_53(
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
            total_monthly_saving_usd=None,
            total_delta_cores=total_delta_cores,
            total_delta_memory_mi=total_delta_mi,
            pods_analyzed=len(opportunities),
            pods_excluded=pods_excluded,
            pricing_configured=pricing_configured,
        )

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_54(
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
            total_delta_cores=None,
            total_delta_memory_mi=total_delta_mi,
            pods_analyzed=len(opportunities),
            pods_excluded=pods_excluded,
            pricing_configured=pricing_configured,
        )

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_55(
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
            total_delta_memory_mi=None,
            pods_analyzed=len(opportunities),
            pods_excluded=pods_excluded,
            pricing_configured=pricing_configured,
        )

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_56(
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
            pods_analyzed=None,
            pods_excluded=pods_excluded,
            pricing_configured=pricing_configured,
        )

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_57(
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
            pods_excluded=None,
            pricing_configured=pricing_configured,
        )

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_58(
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
            pricing_configured=None,
        )

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_59(
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

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_60(
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
            total_monthly_saving_usd=total_usd,
            total_delta_cores=total_delta_cores,
            total_delta_memory_mi=total_delta_mi,
            pods_analyzed=len(opportunities),
            pods_excluded=pods_excluded,
            pricing_configured=pricing_configured,
        )

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_61(
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
            total_delta_cores=total_delta_cores,
            total_delta_memory_mi=total_delta_mi,
            pods_analyzed=len(opportunities),
            pods_excluded=pods_excluded,
            pricing_configured=pricing_configured,
        )

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_62(
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
            total_delta_memory_mi=total_delta_mi,
            pods_analyzed=len(opportunities),
            pods_excluded=pods_excluded,
            pricing_configured=pricing_configured,
        )

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_63(
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
            pods_analyzed=len(opportunities),
            pods_excluded=pods_excluded,
            pricing_configured=pricing_configured,
        )

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_64(
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
            pods_excluded=pods_excluded,
            pricing_configured=pricing_configured,
        )

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_65(
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
            pricing_configured=pricing_configured,
        )

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_66(
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
            )

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_67(
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
                None, key=lambda n: n.total_monthly_saving_usd or 0.0, reverse=True
            ),
            total_monthly_saving_usd=total_usd,
            total_delta_cores=total_delta_cores,
            total_delta_memory_mi=total_delta_mi,
            pods_analyzed=len(opportunities),
            pods_excluded=pods_excluded,
            pricing_configured=pricing_configured,
        )

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_68(
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
                namespace_savings, key=None, reverse=True
            ),
            total_monthly_saving_usd=total_usd,
            total_delta_cores=total_delta_cores,
            total_delta_memory_mi=total_delta_mi,
            pods_analyzed=len(opportunities),
            pods_excluded=pods_excluded,
            pricing_configured=pricing_configured,
        )

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_69(
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
                namespace_savings, key=lambda n: n.total_monthly_saving_usd or 0.0, reverse=None
            ),
            total_monthly_saving_usd=total_usd,
            total_delta_cores=total_delta_cores,
            total_delta_memory_mi=total_delta_mi,
            pods_analyzed=len(opportunities),
            pods_excluded=pods_excluded,
            pricing_configured=pricing_configured,
        )

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_70(
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
                key=lambda n: n.total_monthly_saving_usd or 0.0, reverse=True
            ),
            total_monthly_saving_usd=total_usd,
            total_delta_cores=total_delta_cores,
            total_delta_memory_mi=total_delta_mi,
            pods_analyzed=len(opportunities),
            pods_excluded=pods_excluded,
            pricing_configured=pricing_configured,
        )

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_71(
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
                namespace_savings, reverse=True
            ),
            total_monthly_saving_usd=total_usd,
            total_delta_cores=total_delta_cores,
            total_delta_memory_mi=total_delta_mi,
            pods_analyzed=len(opportunities),
            pods_excluded=pods_excluded,
            pricing_configured=pricing_configured,
        )

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_72(
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
                namespace_savings, key=lambda n: n.total_monthly_saving_usd or 0.0, ),
            total_monthly_saving_usd=total_usd,
            total_delta_cores=total_delta_cores,
            total_delta_memory_mi=total_delta_mi,
            pods_analyzed=len(opportunities),
            pods_excluded=pods_excluded,
            pricing_configured=pricing_configured,
        )

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_73(
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
                namespace_savings, key=lambda n: None, reverse=True
            ),
            total_monthly_saving_usd=total_usd,
            total_delta_cores=total_delta_cores,
            total_delta_memory_mi=total_delta_mi,
            pods_analyzed=len(opportunities),
            pods_excluded=pods_excluded,
            pricing_configured=pricing_configured,
        )

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_74(
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
                namespace_savings, key=lambda n: n.total_monthly_saving_usd and 0.0, reverse=True
            ),
            total_monthly_saving_usd=total_usd,
            total_delta_cores=total_delta_cores,
            total_delta_memory_mi=total_delta_mi,
            pods_analyzed=len(opportunities),
            pods_excluded=pods_excluded,
            pricing_configured=pricing_configured,
        )

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_75(
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
                namespace_savings, key=lambda n: n.total_monthly_saving_usd or 1.0, reverse=True
            ),
            total_monthly_saving_usd=total_usd,
            total_delta_cores=total_delta_cores,
            total_delta_memory_mi=total_delta_mi,
            pods_analyzed=len(opportunities),
            pods_excluded=pods_excluded,
            pricing_configured=pricing_configured,
        )

    def xǁRightSizingCostEstimationServiceǁestimate__mutmut_76(
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
                namespace_savings, key=lambda n: n.total_monthly_saving_usd or 0.0, reverse=False
            ),
            total_monthly_saving_usd=total_usd,
            total_delta_cores=total_delta_cores,
            total_delta_memory_mi=total_delta_mi,
            pods_analyzed=len(opportunities),
            pods_excluded=pods_excluded,
            pricing_configured=pricing_configured,
        )

mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['_mutmut_orig'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_1'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_2'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_3'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_4'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_5'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_6'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_7'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_8'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_9'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_10'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_11'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_12'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_12 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_13'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_13 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_14'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_14 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_15'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_15 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_16'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_16 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_17'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_17 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_18'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_18 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_19'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_19 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_20'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_20 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_21'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_21 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_22'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_22 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_23'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_23 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_24'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_24 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_25'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_25 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_26'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_26 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_27'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_27 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_28'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_28 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_29'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_29 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_30'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_30 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_31'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_31 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_32'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_32 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_33'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_33 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_34'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_34 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_35'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_35 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_36'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_36 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_37'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_37 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_38'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_38 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_39'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_39 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_40'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_40 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_41'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_41 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_42'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_42 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_43'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_43 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_44'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_44 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_45'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_45 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_46'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_46 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_47'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_47 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_48'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_48 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_49'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_49 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_50'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_50 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_51'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_51 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_52'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_52 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_53'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_53 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_54'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_54 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_55'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_55 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_56'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_56 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_57'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_57 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_58'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_58 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_59'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_59 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_60'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_60 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_61'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_61 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_62'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_62 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_63'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_63 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_64'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_64 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_65'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_65 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_66'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_66 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_67'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_67 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_68'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_68 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_69'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_69 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_70'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_70 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_71'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_71 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_72'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_72 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_73'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_73 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_74'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_74 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_75'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_75 # type: ignore # mutmut generated
mutants_xǁRightSizingCostEstimationServiceǁestimate__mutmut['xǁRightSizingCostEstimationServiceǁestimate__mutmut_76'] = RightSizingCostEstimationService.xǁRightSizingCostEstimationServiceǁestimate__mutmut_76 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__analyze_pod__mutmut)
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_orig(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_1(
    pod: dict[str, object],
    cpu_price: float | None,
    mem_price: float | None,
) -> PodSavingOpportunity | None:
    cpu_req = None
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_2(
    pod: dict[str, object],
    cpu_price: float | None,
    mem_price: float | None,
) -> PodSavingOpportunity | None:
    cpu_req = _f(None)
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_3(
    pod: dict[str, object],
    cpu_price: float | None,
    mem_price: float | None,
) -> PodSavingOpportunity | None:
    cpu_req = _f(pod.get(None))
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_4(
    pod: dict[str, object],
    cpu_price: float | None,
    mem_price: float | None,
) -> PodSavingOpportunity | None:
    cpu_req = _f(pod.get("XXcpu_request_coresXX"))
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_5(
    pod: dict[str, object],
    cpu_price: float | None,
    mem_price: float | None,
) -> PodSavingOpportunity | None:
    cpu_req = _f(pod.get("CPU_REQUEST_CORES"))
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_6(
    pod: dict[str, object],
    cpu_price: float | None,
    mem_price: float | None,
) -> PodSavingOpportunity | None:
    cpu_req = _f(pod.get("cpu_request_cores"))
    mem_req = None
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_7(
    pod: dict[str, object],
    cpu_price: float | None,
    mem_price: float | None,
) -> PodSavingOpportunity | None:
    cpu_req = _f(pod.get("cpu_request_cores"))
    mem_req = _f(None)
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_8(
    pod: dict[str, object],
    cpu_price: float | None,
    mem_price: float | None,
) -> PodSavingOpportunity | None:
    cpu_req = _f(pod.get("cpu_request_cores"))
    mem_req = _f(pod.get(None))
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_9(
    pod: dict[str, object],
    cpu_price: float | None,
    mem_price: float | None,
) -> PodSavingOpportunity | None:
    cpu_req = _f(pod.get("cpu_request_cores"))
    mem_req = _f(pod.get("XXmemory_request_miXX"))
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_10(
    pod: dict[str, object],
    cpu_price: float | None,
    mem_price: float | None,
) -> PodSavingOpportunity | None:
    cpu_req = _f(pod.get("cpu_request_cores"))
    mem_req = _f(pod.get("MEMORY_REQUEST_MI"))
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_11(
    pod: dict[str, object],
    cpu_price: float | None,
    mem_price: float | None,
) -> PodSavingOpportunity | None:
    cpu_req = _f(pod.get("cpu_request_cores"))
    mem_req = _f(pod.get("memory_request_mi"))
    cpu_limit = None
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_12(
    pod: dict[str, object],
    cpu_price: float | None,
    mem_price: float | None,
) -> PodSavingOpportunity | None:
    cpu_req = _f(pod.get("cpu_request_cores"))
    mem_req = _f(pod.get("memory_request_mi"))
    cpu_limit = _f(None)
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_13(
    pod: dict[str, object],
    cpu_price: float | None,
    mem_price: float | None,
) -> PodSavingOpportunity | None:
    cpu_req = _f(pod.get("cpu_request_cores"))
    mem_req = _f(pod.get("memory_request_mi"))
    cpu_limit = _f(pod.get(None))
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_14(
    pod: dict[str, object],
    cpu_price: float | None,
    mem_price: float | None,
) -> PodSavingOpportunity | None:
    cpu_req = _f(pod.get("cpu_request_cores"))
    mem_req = _f(pod.get("memory_request_mi"))
    cpu_limit = _f(pod.get("XXcpu_limit_coresXX"))
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_15(
    pod: dict[str, object],
    cpu_price: float | None,
    mem_price: float | None,
) -> PodSavingOpportunity | None:
    cpu_req = _f(pod.get("cpu_request_cores"))
    mem_req = _f(pod.get("memory_request_mi"))
    cpu_limit = _f(pod.get("CPU_LIMIT_CORES"))
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_16(
    pod: dict[str, object],
    cpu_price: float | None,
    mem_price: float | None,
) -> PodSavingOpportunity | None:
    cpu_req = _f(pod.get("cpu_request_cores"))
    mem_req = _f(pod.get("memory_request_mi"))
    cpu_limit = _f(pod.get("cpu_limit_cores"))
    mem_limit = None

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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_17(
    pod: dict[str, object],
    cpu_price: float | None,
    mem_price: float | None,
) -> PodSavingOpportunity | None:
    cpu_req = _f(pod.get("cpu_request_cores"))
    mem_req = _f(pod.get("memory_request_mi"))
    cpu_limit = _f(pod.get("cpu_limit_cores"))
    mem_limit = _f(None)

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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_18(
    pod: dict[str, object],
    cpu_price: float | None,
    mem_price: float | None,
) -> PodSavingOpportunity | None:
    cpu_req = _f(pod.get("cpu_request_cores"))
    mem_req = _f(pod.get("memory_request_mi"))
    cpu_limit = _f(pod.get("cpu_limit_cores"))
    mem_limit = _f(pod.get(None))

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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_19(
    pod: dict[str, object],
    cpu_price: float | None,
    mem_price: float | None,
) -> PodSavingOpportunity | None:
    cpu_req = _f(pod.get("cpu_request_cores"))
    mem_req = _f(pod.get("memory_request_mi"))
    cpu_limit = _f(pod.get("cpu_limit_cores"))
    mem_limit = _f(pod.get("XXmemory_limit_miXX"))

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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_20(
    pod: dict[str, object],
    cpu_price: float | None,
    mem_price: float | None,
) -> PodSavingOpportunity | None:
    cpu_req = _f(pod.get("cpu_request_cores"))
    mem_req = _f(pod.get("memory_request_mi"))
    cpu_limit = _f(pod.get("cpu_limit_cores"))
    mem_limit = _f(pod.get("MEMORY_LIMIT_MI"))

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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_21(
    pod: dict[str, object],
    cpu_price: float | None,
    mem_price: float | None,
) -> PodSavingOpportunity | None:
    cpu_req = _f(pod.get("cpu_request_cores"))
    mem_req = _f(pod.get("memory_request_mi"))
    cpu_limit = _f(pod.get("cpu_limit_cores"))
    mem_limit = _f(pod.get("memory_limit_mi"))

    # Effective request: use limit when request is absent
    eff_cpu = None
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_22(
    pod: dict[str, object],
    cpu_price: float | None,
    mem_price: float | None,
) -> PodSavingOpportunity | None:
    cpu_req = _f(pod.get("cpu_request_cores"))
    mem_req = _f(pod.get("memory_request_mi"))
    cpu_limit = _f(pod.get("cpu_limit_cores"))
    mem_limit = _f(pod.get("memory_limit_mi"))

    # Effective request: use limit when request is absent
    eff_cpu = cpu_req if cpu_req is None else cpu_limit
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_23(
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
    eff_mem = None

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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_24(
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
    eff_mem = mem_req if mem_req is None else mem_limit

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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_25(
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

    if eff_cpu is None or eff_mem is None:
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_26(
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

    if eff_cpu is not None and eff_mem is None:
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_27(
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

    if eff_cpu is None and eff_mem is not None:
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_28(
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

    cpu_p95 = None
    mem_p95 = _f(pod.get("memory_p95_mi"))
    cpu_max = _f(pod.get("cpu_max_cores"))

    if cpu_p95 is None and mem_p95 is None:
        return None  # no actual usage data → can't right-size

    if _is_optimal(eff_cpu, eff_mem, cpu_p95, mem_p95):
        return None  # already well-sized → excluded

    rec_cpu = _recommended(eff_cpu, cpu_p95)
    rec_mem = _recommended(eff_mem, mem_p95)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_29(
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

    cpu_p95 = _f(None)
    mem_p95 = _f(pod.get("memory_p95_mi"))
    cpu_max = _f(pod.get("cpu_max_cores"))

    if cpu_p95 is None and mem_p95 is None:
        return None  # no actual usage data → can't right-size

    if _is_optimal(eff_cpu, eff_mem, cpu_p95, mem_p95):
        return None  # already well-sized → excluded

    rec_cpu = _recommended(eff_cpu, cpu_p95)
    rec_mem = _recommended(eff_mem, mem_p95)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_30(
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

    cpu_p95 = _f(pod.get(None))
    mem_p95 = _f(pod.get("memory_p95_mi"))
    cpu_max = _f(pod.get("cpu_max_cores"))

    if cpu_p95 is None and mem_p95 is None:
        return None  # no actual usage data → can't right-size

    if _is_optimal(eff_cpu, eff_mem, cpu_p95, mem_p95):
        return None  # already well-sized → excluded

    rec_cpu = _recommended(eff_cpu, cpu_p95)
    rec_mem = _recommended(eff_mem, mem_p95)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_31(
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

    cpu_p95 = _f(pod.get("XXcpu_p95_coresXX"))
    mem_p95 = _f(pod.get("memory_p95_mi"))
    cpu_max = _f(pod.get("cpu_max_cores"))

    if cpu_p95 is None and mem_p95 is None:
        return None  # no actual usage data → can't right-size

    if _is_optimal(eff_cpu, eff_mem, cpu_p95, mem_p95):
        return None  # already well-sized → excluded

    rec_cpu = _recommended(eff_cpu, cpu_p95)
    rec_mem = _recommended(eff_mem, mem_p95)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_32(
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

    cpu_p95 = _f(pod.get("CPU_P95_CORES"))
    mem_p95 = _f(pod.get("memory_p95_mi"))
    cpu_max = _f(pod.get("cpu_max_cores"))

    if cpu_p95 is None and mem_p95 is None:
        return None  # no actual usage data → can't right-size

    if _is_optimal(eff_cpu, eff_mem, cpu_p95, mem_p95):
        return None  # already well-sized → excluded

    rec_cpu = _recommended(eff_cpu, cpu_p95)
    rec_mem = _recommended(eff_mem, mem_p95)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_33(
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
    mem_p95 = None
    cpu_max = _f(pod.get("cpu_max_cores"))

    if cpu_p95 is None and mem_p95 is None:
        return None  # no actual usage data → can't right-size

    if _is_optimal(eff_cpu, eff_mem, cpu_p95, mem_p95):
        return None  # already well-sized → excluded

    rec_cpu = _recommended(eff_cpu, cpu_p95)
    rec_mem = _recommended(eff_mem, mem_p95)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_34(
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
    mem_p95 = _f(None)
    cpu_max = _f(pod.get("cpu_max_cores"))

    if cpu_p95 is None and mem_p95 is None:
        return None  # no actual usage data → can't right-size

    if _is_optimal(eff_cpu, eff_mem, cpu_p95, mem_p95):
        return None  # already well-sized → excluded

    rec_cpu = _recommended(eff_cpu, cpu_p95)
    rec_mem = _recommended(eff_mem, mem_p95)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_35(
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
    mem_p95 = _f(pod.get(None))
    cpu_max = _f(pod.get("cpu_max_cores"))

    if cpu_p95 is None and mem_p95 is None:
        return None  # no actual usage data → can't right-size

    if _is_optimal(eff_cpu, eff_mem, cpu_p95, mem_p95):
        return None  # already well-sized → excluded

    rec_cpu = _recommended(eff_cpu, cpu_p95)
    rec_mem = _recommended(eff_mem, mem_p95)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_36(
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
    mem_p95 = _f(pod.get("XXmemory_p95_miXX"))
    cpu_max = _f(pod.get("cpu_max_cores"))

    if cpu_p95 is None and mem_p95 is None:
        return None  # no actual usage data → can't right-size

    if _is_optimal(eff_cpu, eff_mem, cpu_p95, mem_p95):
        return None  # already well-sized → excluded

    rec_cpu = _recommended(eff_cpu, cpu_p95)
    rec_mem = _recommended(eff_mem, mem_p95)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_37(
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
    mem_p95 = _f(pod.get("MEMORY_P95_MI"))
    cpu_max = _f(pod.get("cpu_max_cores"))

    if cpu_p95 is None and mem_p95 is None:
        return None  # no actual usage data → can't right-size

    if _is_optimal(eff_cpu, eff_mem, cpu_p95, mem_p95):
        return None  # already well-sized → excluded

    rec_cpu = _recommended(eff_cpu, cpu_p95)
    rec_mem = _recommended(eff_mem, mem_p95)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_38(
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
    cpu_max = None

    if cpu_p95 is None and mem_p95 is None:
        return None  # no actual usage data → can't right-size

    if _is_optimal(eff_cpu, eff_mem, cpu_p95, mem_p95):
        return None  # already well-sized → excluded

    rec_cpu = _recommended(eff_cpu, cpu_p95)
    rec_mem = _recommended(eff_mem, mem_p95)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_39(
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
    cpu_max = _f(None)

    if cpu_p95 is None and mem_p95 is None:
        return None  # no actual usage data → can't right-size

    if _is_optimal(eff_cpu, eff_mem, cpu_p95, mem_p95):
        return None  # already well-sized → excluded

    rec_cpu = _recommended(eff_cpu, cpu_p95)
    rec_mem = _recommended(eff_mem, mem_p95)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_40(
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
    cpu_max = _f(pod.get(None))

    if cpu_p95 is None and mem_p95 is None:
        return None  # no actual usage data → can't right-size

    if _is_optimal(eff_cpu, eff_mem, cpu_p95, mem_p95):
        return None  # already well-sized → excluded

    rec_cpu = _recommended(eff_cpu, cpu_p95)
    rec_mem = _recommended(eff_mem, mem_p95)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_41(
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
    cpu_max = _f(pod.get("XXcpu_max_coresXX"))

    if cpu_p95 is None and mem_p95 is None:
        return None  # no actual usage data → can't right-size

    if _is_optimal(eff_cpu, eff_mem, cpu_p95, mem_p95):
        return None  # already well-sized → excluded

    rec_cpu = _recommended(eff_cpu, cpu_p95)
    rec_mem = _recommended(eff_mem, mem_p95)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_42(
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
    cpu_max = _f(pod.get("CPU_MAX_CORES"))

    if cpu_p95 is None and mem_p95 is None:
        return None  # no actual usage data → can't right-size

    if _is_optimal(eff_cpu, eff_mem, cpu_p95, mem_p95):
        return None  # already well-sized → excluded

    rec_cpu = _recommended(eff_cpu, cpu_p95)
    rec_mem = _recommended(eff_mem, mem_p95)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_43(
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

    if cpu_p95 is None or mem_p95 is None:
        return None  # no actual usage data → can't right-size

    if _is_optimal(eff_cpu, eff_mem, cpu_p95, mem_p95):
        return None  # already well-sized → excluded

    rec_cpu = _recommended(eff_cpu, cpu_p95)
    rec_mem = _recommended(eff_mem, mem_p95)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_44(
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

    if cpu_p95 is not None and mem_p95 is None:
        return None  # no actual usage data → can't right-size

    if _is_optimal(eff_cpu, eff_mem, cpu_p95, mem_p95):
        return None  # already well-sized → excluded

    rec_cpu = _recommended(eff_cpu, cpu_p95)
    rec_mem = _recommended(eff_mem, mem_p95)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_45(
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

    if cpu_p95 is None and mem_p95 is not None:
        return None  # no actual usage data → can't right-size

    if _is_optimal(eff_cpu, eff_mem, cpu_p95, mem_p95):
        return None  # already well-sized → excluded

    rec_cpu = _recommended(eff_cpu, cpu_p95)
    rec_mem = _recommended(eff_mem, mem_p95)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_46(
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

    if _is_optimal(None, eff_mem, cpu_p95, mem_p95):
        return None  # already well-sized → excluded

    rec_cpu = _recommended(eff_cpu, cpu_p95)
    rec_mem = _recommended(eff_mem, mem_p95)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_47(
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

    if _is_optimal(eff_cpu, None, cpu_p95, mem_p95):
        return None  # already well-sized → excluded

    rec_cpu = _recommended(eff_cpu, cpu_p95)
    rec_mem = _recommended(eff_mem, mem_p95)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_48(
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

    if _is_optimal(eff_cpu, eff_mem, None, mem_p95):
        return None  # already well-sized → excluded

    rec_cpu = _recommended(eff_cpu, cpu_p95)
    rec_mem = _recommended(eff_mem, mem_p95)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_49(
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

    if _is_optimal(eff_cpu, eff_mem, cpu_p95, None):
        return None  # already well-sized → excluded

    rec_cpu = _recommended(eff_cpu, cpu_p95)
    rec_mem = _recommended(eff_mem, mem_p95)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_50(
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

    if _is_optimal(eff_mem, cpu_p95, mem_p95):
        return None  # already well-sized → excluded

    rec_cpu = _recommended(eff_cpu, cpu_p95)
    rec_mem = _recommended(eff_mem, mem_p95)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_51(
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

    if _is_optimal(eff_cpu, cpu_p95, mem_p95):
        return None  # already well-sized → excluded

    rec_cpu = _recommended(eff_cpu, cpu_p95)
    rec_mem = _recommended(eff_mem, mem_p95)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_52(
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

    if _is_optimal(eff_cpu, eff_mem, mem_p95):
        return None  # already well-sized → excluded

    rec_cpu = _recommended(eff_cpu, cpu_p95)
    rec_mem = _recommended(eff_mem, mem_p95)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_53(
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

    if _is_optimal(eff_cpu, eff_mem, cpu_p95, ):
        return None  # already well-sized → excluded

    rec_cpu = _recommended(eff_cpu, cpu_p95)
    rec_mem = _recommended(eff_mem, mem_p95)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_54(
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

    rec_cpu = None
    rec_mem = _recommended(eff_mem, mem_p95)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_55(
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

    rec_cpu = _recommended(None, cpu_p95)
    rec_mem = _recommended(eff_mem, mem_p95)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_56(
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

    rec_cpu = _recommended(eff_cpu, None)
    rec_mem = _recommended(eff_mem, mem_p95)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_57(
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

    rec_cpu = _recommended(cpu_p95)
    rec_mem = _recommended(eff_mem, mem_p95)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_58(
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

    rec_cpu = _recommended(eff_cpu, )
    rec_mem = _recommended(eff_mem, mem_p95)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_59(
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
    rec_mem = None

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_60(
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
    rec_mem = _recommended(None, mem_p95)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_61(
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
    rec_mem = _recommended(eff_mem, None)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_62(
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
    rec_mem = _recommended(mem_p95)

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_63(
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
    rec_mem = _recommended(eff_mem, )

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_64(
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

    delta_cores = None
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_65(
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

    delta_cores = _delta(None, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_66(
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

    delta_cores = _delta(eff_cpu, None, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_67(
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

    delta_cores = _delta(eff_cpu, rec_cpu, None)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_68(
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

    delta_cores = _delta(rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_69(
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

    delta_cores = _delta(eff_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_70(
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

    delta_cores = _delta(eff_cpu, rec_cpu, )
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_71(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 4)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_72(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = None

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


def x__analyze_pod__mutmut_73(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(None, rec_mem, 1)

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


def x__analyze_pod__mutmut_74(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, None, 1)

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


def x__analyze_pod__mutmut_75(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, None)

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


def x__analyze_pod__mutmut_76(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(rec_mem, 1)

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


def x__analyze_pod__mutmut_77(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, 1)

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


def x__analyze_pod__mutmut_78(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, )

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


def x__analyze_pod__mutmut_79(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 2)

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


def x__analyze_pod__mutmut_80(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = ""
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


def x__analyze_pod__mutmut_81(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None and mem_price is not None:
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


def x__analyze_pod__mutmut_82(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is None or mem_price is not None:
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


def x__analyze_pod__mutmut_83(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is None:
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


def x__analyze_pod__mutmut_84(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = None
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


def x__analyze_pod__mutmut_85(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores * (cpu_price or 0.0) / _HOURS_PER_MONTH
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


def x__analyze_pod__mutmut_86(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores / (cpu_price or 0.0) * _HOURS_PER_MONTH
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


def x__analyze_pod__mutmut_87(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores * (cpu_price and 0.0) * _HOURS_PER_MONTH
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


def x__analyze_pod__mutmut_88(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores * (cpu_price or 1.0) * _HOURS_PER_MONTH
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


def x__analyze_pod__mutmut_89(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores * (cpu_price or 0.0) * _HOURS_PER_MONTH
        mem_saving = None
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


def x__analyze_pod__mutmut_90(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores * (cpu_price or 0.0) * _HOURS_PER_MONTH
        mem_saving = (delta_mi / 1024.0) * (mem_price or 0.0) / _HOURS_PER_MONTH
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


def x__analyze_pod__mutmut_91(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores * (cpu_price or 0.0) * _HOURS_PER_MONTH
        mem_saving = (delta_mi / 1024.0) / (mem_price or 0.0) * _HOURS_PER_MONTH
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


def x__analyze_pod__mutmut_92(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores * (cpu_price or 0.0) * _HOURS_PER_MONTH
        mem_saving = (delta_mi * 1024.0) * (mem_price or 0.0) * _HOURS_PER_MONTH
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


def x__analyze_pod__mutmut_93(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores * (cpu_price or 0.0) * _HOURS_PER_MONTH
        mem_saving = (delta_mi / 1025.0) * (mem_price or 0.0) * _HOURS_PER_MONTH
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


def x__analyze_pod__mutmut_94(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores * (cpu_price or 0.0) * _HOURS_PER_MONTH
        mem_saving = (delta_mi / 1024.0) * (mem_price and 0.0) * _HOURS_PER_MONTH
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


def x__analyze_pod__mutmut_95(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores * (cpu_price or 0.0) * _HOURS_PER_MONTH
        mem_saving = (delta_mi / 1024.0) * (mem_price or 1.0) * _HOURS_PER_MONTH
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


def x__analyze_pod__mutmut_96(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores * (cpu_price or 0.0) * _HOURS_PER_MONTH
        mem_saving = (delta_mi / 1024.0) * (mem_price or 0.0) * _HOURS_PER_MONTH
        monthly_usd = None

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


def x__analyze_pod__mutmut_97(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores * (cpu_price or 0.0) * _HOURS_PER_MONTH
        mem_saving = (delta_mi / 1024.0) * (mem_price or 0.0) * _HOURS_PER_MONTH
        monthly_usd = round(None, 2)

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


def x__analyze_pod__mutmut_98(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores * (cpu_price or 0.0) * _HOURS_PER_MONTH
        mem_saving = (delta_mi / 1024.0) * (mem_price or 0.0) * _HOURS_PER_MONTH
        monthly_usd = round(cpu_saving + mem_saving, None)

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


def x__analyze_pod__mutmut_99(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores * (cpu_price or 0.0) * _HOURS_PER_MONTH
        mem_saving = (delta_mi / 1024.0) * (mem_price or 0.0) * _HOURS_PER_MONTH
        monthly_usd = round(2)

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


def x__analyze_pod__mutmut_100(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores * (cpu_price or 0.0) * _HOURS_PER_MONTH
        mem_saving = (delta_mi / 1024.0) * (mem_price or 0.0) * _HOURS_PER_MONTH
        monthly_usd = round(cpu_saving + mem_saving, )

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


def x__analyze_pod__mutmut_101(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores * (cpu_price or 0.0) * _HOURS_PER_MONTH
        mem_saving = (delta_mi / 1024.0) * (mem_price or 0.0) * _HOURS_PER_MONTH
        monthly_usd = round(cpu_saving - mem_saving, 2)

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


def x__analyze_pod__mutmut_102(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores * (cpu_price or 0.0) * _HOURS_PER_MONTH
        mem_saving = (delta_mi / 1024.0) * (mem_price or 0.0) * _HOURS_PER_MONTH
        monthly_usd = round(cpu_saving + mem_saving, 3)

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


def x__analyze_pod__mutmut_103(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores * (cpu_price or 0.0) * _HOURS_PER_MONTH
        mem_saving = (delta_mi / 1024.0) * (mem_price or 0.0) * _HOURS_PER_MONTH
        monthly_usd = round(cpu_saving + mem_saving, 2)

    hpa_enabled = None
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


def x__analyze_pod__mutmut_104(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores * (cpu_price or 0.0) * _HOURS_PER_MONTH
        mem_saving = (delta_mi / 1024.0) * (mem_price or 0.0) * _HOURS_PER_MONTH
        monthly_usd = round(cpu_saving + mem_saving, 2)

    hpa_enabled = bool(None)
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


def x__analyze_pod__mutmut_105(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores * (cpu_price or 0.0) * _HOURS_PER_MONTH
        mem_saving = (delta_mi / 1024.0) * (mem_price or 0.0) * _HOURS_PER_MONTH
        monthly_usd = round(cpu_saving + mem_saving, 2)

    hpa_enabled = bool(pod.get(None))
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


def x__analyze_pod__mutmut_106(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores * (cpu_price or 0.0) * _HOURS_PER_MONTH
        mem_saving = (delta_mi / 1024.0) * (mem_price or 0.0) * _HOURS_PER_MONTH
        monthly_usd = round(cpu_saving + mem_saving, 2)

    hpa_enabled = bool(pod.get("XXhpa_enabledXX"))
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


def x__analyze_pod__mutmut_107(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores * (cpu_price or 0.0) * _HOURS_PER_MONTH
        mem_saving = (delta_mi / 1024.0) * (mem_price or 0.0) * _HOURS_PER_MONTH
        monthly_usd = round(cpu_saving + mem_saving, 2)

    hpa_enabled = bool(pod.get("HPA_ENABLED"))
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


def x__analyze_pod__mutmut_108(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores * (cpu_price or 0.0) * _HOURS_PER_MONTH
        mem_saving = (delta_mi / 1024.0) * (mem_price or 0.0) * _HOURS_PER_MONTH
        monthly_usd = round(cpu_saving + mem_saving, 2)

    hpa_enabled = bool(pod.get("hpa_enabled"))
    is_bursty = None

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


def x__analyze_pod__mutmut_109(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores * (cpu_price or 0.0) * _HOURS_PER_MONTH
        mem_saving = (delta_mi / 1024.0) * (mem_price or 0.0) * _HOURS_PER_MONTH
        monthly_usd = round(cpu_saving + mem_saving, 2)

    hpa_enabled = bool(pod.get("hpa_enabled"))
    is_bursty = _bursty(None, cpu_max)

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


def x__analyze_pod__mutmut_110(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores * (cpu_price or 0.0) * _HOURS_PER_MONTH
        mem_saving = (delta_mi / 1024.0) * (mem_price or 0.0) * _HOURS_PER_MONTH
        monthly_usd = round(cpu_saving + mem_saving, 2)

    hpa_enabled = bool(pod.get("hpa_enabled"))
    is_bursty = _bursty(cpu_p95, None)

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


def x__analyze_pod__mutmut_111(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores * (cpu_price or 0.0) * _HOURS_PER_MONTH
        mem_saving = (delta_mi / 1024.0) * (mem_price or 0.0) * _HOURS_PER_MONTH
        monthly_usd = round(cpu_saving + mem_saving, 2)

    hpa_enabled = bool(pod.get("hpa_enabled"))
    is_bursty = _bursty(cpu_max)

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


def x__analyze_pod__mutmut_112(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores * (cpu_price or 0.0) * _HOURS_PER_MONTH
        mem_saving = (delta_mi / 1024.0) * (mem_price or 0.0) * _HOURS_PER_MONTH
        monthly_usd = round(cpu_saving + mem_saving, 2)

    hpa_enabled = bool(pod.get("hpa_enabled"))
    is_bursty = _bursty(cpu_p95, )

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


def x__analyze_pod__mutmut_113(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores * (cpu_price or 0.0) * _HOURS_PER_MONTH
        mem_saving = (delta_mi / 1024.0) * (mem_price or 0.0) * _HOURS_PER_MONTH
        monthly_usd = round(cpu_saving + mem_saving, 2)

    hpa_enabled = bool(pod.get("hpa_enabled"))
    is_bursty = _bursty(cpu_p95, cpu_max)

    caveats: list[str] = None
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


def x__analyze_pod__mutmut_114(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores * (cpu_price or 0.0) * _HOURS_PER_MONTH
        mem_saving = (delta_mi / 1024.0) * (mem_price or 0.0) * _HOURS_PER_MONTH
        monthly_usd = round(cpu_saving + mem_saving, 2)

    hpa_enabled = bool(pod.get("hpa_enabled"))
    is_bursty = _bursty(cpu_p95, cpu_max)

    caveats: list[str] = []
    if hpa_enabled:
        hpa_min = None
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


def x__analyze_pod__mutmut_115(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores * (cpu_price or 0.0) * _HOURS_PER_MONTH
        mem_saving = (delta_mi / 1024.0) * (mem_price or 0.0) * _HOURS_PER_MONTH
        monthly_usd = round(cpu_saving + mem_saving, 2)

    hpa_enabled = bool(pod.get("hpa_enabled"))
    is_bursty = _bursty(cpu_p95, cpu_max)

    caveats: list[str] = []
    if hpa_enabled:
        hpa_min = pod.get(None)
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


def x__analyze_pod__mutmut_116(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores * (cpu_price or 0.0) * _HOURS_PER_MONTH
        mem_saving = (delta_mi / 1024.0) * (mem_price or 0.0) * _HOURS_PER_MONTH
        monthly_usd = round(cpu_saving + mem_saving, 2)

    hpa_enabled = bool(pod.get("hpa_enabled"))
    is_bursty = _bursty(cpu_p95, cpu_max)

    caveats: list[str] = []
    if hpa_enabled:
        hpa_min = pod.get("XXhpa_min_replicasXX")
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


def x__analyze_pod__mutmut_117(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

    monthly_usd: float | None = None
    if cpu_price is not None or mem_price is not None:
        cpu_saving = delta_cores * (cpu_price or 0.0) * _HOURS_PER_MONTH
        mem_saving = (delta_mi / 1024.0) * (mem_price or 0.0) * _HOURS_PER_MONTH
        monthly_usd = round(cpu_saving + mem_saving, 2)

    hpa_enabled = bool(pod.get("hpa_enabled"))
    is_bursty = _bursty(cpu_p95, cpu_max)

    caveats: list[str] = []
    if hpa_enabled:
        hpa_min = pod.get("HPA_MIN_REPLICAS")
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


def x__analyze_pod__mutmut_118(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
            None
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


def x__analyze_pod__mutmut_119(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
            "XXadjust HPA min_replicas separatelyXX"
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


def x__analyze_pod__mutmut_120(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
            "adjust hpa min_replicas separately"
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


def x__analyze_pod__mutmut_121(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
            "ADJUST HPA MIN_REPLICAS SEPARATELY"
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


def x__analyze_pod__mutmut_122(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
            None
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


def x__analyze_pod__mutmut_123(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
            "XXBursty workload detected: right-sizing based on 7d p95 may cause OOM under peakXX"
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


def x__analyze_pod__mutmut_124(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
            "bursty workload detected: right-sizing based on 7d p95 may cause oom under peak"
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


def x__analyze_pod__mutmut_125(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
            "BURSTY WORKLOAD DETECTED: RIGHT-SIZING BASED ON 7D P95 MAY CAUSE OOM UNDER PEAK"
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


def x__analyze_pod__mutmut_126(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        pod_name=None,
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


def x__analyze_pod__mutmut_127(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        namespace=None,
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


def x__analyze_pod__mutmut_128(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        current_cpu_request=None,
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


def x__analyze_pod__mutmut_129(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        recommended_cpu_request=None,
        current_memory_request_mi=eff_mem,
        recommended_memory_request_mi=rec_mem,
        delta_cores=delta_cores,
        delta_memory_mi=delta_mi,
        monthly_saving_usd=monthly_usd,
        hpa_enabled=hpa_enabled,
        is_bursty=is_bursty,
        caveats=caveats,
    )


def x__analyze_pod__mutmut_130(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        current_memory_request_mi=None,
        recommended_memory_request_mi=rec_mem,
        delta_cores=delta_cores,
        delta_memory_mi=delta_mi,
        monthly_saving_usd=monthly_usd,
        hpa_enabled=hpa_enabled,
        is_bursty=is_bursty,
        caveats=caveats,
    )


def x__analyze_pod__mutmut_131(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        recommended_memory_request_mi=None,
        delta_cores=delta_cores,
        delta_memory_mi=delta_mi,
        monthly_saving_usd=monthly_usd,
        hpa_enabled=hpa_enabled,
        is_bursty=is_bursty,
        caveats=caveats,
    )


def x__analyze_pod__mutmut_132(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        delta_cores=None,
        delta_memory_mi=delta_mi,
        monthly_saving_usd=monthly_usd,
        hpa_enabled=hpa_enabled,
        is_bursty=is_bursty,
        caveats=caveats,
    )


def x__analyze_pod__mutmut_133(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        delta_memory_mi=None,
        monthly_saving_usd=monthly_usd,
        hpa_enabled=hpa_enabled,
        is_bursty=is_bursty,
        caveats=caveats,
    )


def x__analyze_pod__mutmut_134(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        monthly_saving_usd=None,
        hpa_enabled=hpa_enabled,
        is_bursty=is_bursty,
        caveats=caveats,
    )


def x__analyze_pod__mutmut_135(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        hpa_enabled=None,
        is_bursty=is_bursty,
        caveats=caveats,
    )


def x__analyze_pod__mutmut_136(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        is_bursty=None,
        caveats=caveats,
    )


def x__analyze_pod__mutmut_137(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        caveats=None,
    )


def x__analyze_pod__mutmut_138(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_139(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_140(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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


def x__analyze_pod__mutmut_141(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        current_memory_request_mi=eff_mem,
        recommended_memory_request_mi=rec_mem,
        delta_cores=delta_cores,
        delta_memory_mi=delta_mi,
        monthly_saving_usd=monthly_usd,
        hpa_enabled=hpa_enabled,
        is_bursty=is_bursty,
        caveats=caveats,
    )


def x__analyze_pod__mutmut_142(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        recommended_memory_request_mi=rec_mem,
        delta_cores=delta_cores,
        delta_memory_mi=delta_mi,
        monthly_saving_usd=monthly_usd,
        hpa_enabled=hpa_enabled,
        is_bursty=is_bursty,
        caveats=caveats,
    )


def x__analyze_pod__mutmut_143(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        delta_cores=delta_cores,
        delta_memory_mi=delta_mi,
        monthly_saving_usd=monthly_usd,
        hpa_enabled=hpa_enabled,
        is_bursty=is_bursty,
        caveats=caveats,
    )


def x__analyze_pod__mutmut_144(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        delta_memory_mi=delta_mi,
        monthly_saving_usd=monthly_usd,
        hpa_enabled=hpa_enabled,
        is_bursty=is_bursty,
        caveats=caveats,
    )


def x__analyze_pod__mutmut_145(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        monthly_saving_usd=monthly_usd,
        hpa_enabled=hpa_enabled,
        is_bursty=is_bursty,
        caveats=caveats,
    )


def x__analyze_pod__mutmut_146(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        hpa_enabled=hpa_enabled,
        is_bursty=is_bursty,
        caveats=caveats,
    )


def x__analyze_pod__mutmut_147(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        is_bursty=is_bursty,
        caveats=caveats,
    )


def x__analyze_pod__mutmut_148(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        caveats=caveats,
    )


def x__analyze_pod__mutmut_149(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        )


def x__analyze_pod__mutmut_150(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        pod_name=str(None),
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


def x__analyze_pod__mutmut_151(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        pod_name=str(pod.get(None, "")),
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


def x__analyze_pod__mutmut_152(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        pod_name=str(pod.get("pod_name", None)),
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


def x__analyze_pod__mutmut_153(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        pod_name=str(pod.get("")),
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


def x__analyze_pod__mutmut_154(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        pod_name=str(pod.get("pod_name", )),
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


def x__analyze_pod__mutmut_155(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        pod_name=str(pod.get("XXpod_nameXX", "")),
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


def x__analyze_pod__mutmut_156(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        pod_name=str(pod.get("POD_NAME", "")),
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


def x__analyze_pod__mutmut_157(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        pod_name=str(pod.get("pod_name", "XXXX")),
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


def x__analyze_pod__mutmut_158(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        namespace=str(None),
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


def x__analyze_pod__mutmut_159(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        namespace=str(pod.get(None, "")),
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


def x__analyze_pod__mutmut_160(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        namespace=str(pod.get("namespace", None)),
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


def x__analyze_pod__mutmut_161(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        namespace=str(pod.get("")),
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


def x__analyze_pod__mutmut_162(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        namespace=str(pod.get("namespace", )),
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


def x__analyze_pod__mutmut_163(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        namespace=str(pod.get("XXnamespaceXX", "")),
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


def x__analyze_pod__mutmut_164(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        namespace=str(pod.get("NAMESPACE", "")),
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


def x__analyze_pod__mutmut_165(
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

    delta_cores = _delta(eff_cpu, rec_cpu, 3)
    delta_mi = _delta(eff_mem, rec_mem, 1)

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
        namespace=str(pod.get("namespace", "XXXX")),
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

mutants_x__analyze_pod__mutmut['_mutmut_orig'] = x__analyze_pod__mutmut_orig # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_1'] = x__analyze_pod__mutmut_1 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_2'] = x__analyze_pod__mutmut_2 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_3'] = x__analyze_pod__mutmut_3 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_4'] = x__analyze_pod__mutmut_4 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_5'] = x__analyze_pod__mutmut_5 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_6'] = x__analyze_pod__mutmut_6 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_7'] = x__analyze_pod__mutmut_7 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_8'] = x__analyze_pod__mutmut_8 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_9'] = x__analyze_pod__mutmut_9 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_10'] = x__analyze_pod__mutmut_10 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_11'] = x__analyze_pod__mutmut_11 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_12'] = x__analyze_pod__mutmut_12 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_13'] = x__analyze_pod__mutmut_13 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_14'] = x__analyze_pod__mutmut_14 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_15'] = x__analyze_pod__mutmut_15 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_16'] = x__analyze_pod__mutmut_16 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_17'] = x__analyze_pod__mutmut_17 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_18'] = x__analyze_pod__mutmut_18 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_19'] = x__analyze_pod__mutmut_19 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_20'] = x__analyze_pod__mutmut_20 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_21'] = x__analyze_pod__mutmut_21 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_22'] = x__analyze_pod__mutmut_22 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_23'] = x__analyze_pod__mutmut_23 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_24'] = x__analyze_pod__mutmut_24 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_25'] = x__analyze_pod__mutmut_25 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_26'] = x__analyze_pod__mutmut_26 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_27'] = x__analyze_pod__mutmut_27 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_28'] = x__analyze_pod__mutmut_28 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_29'] = x__analyze_pod__mutmut_29 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_30'] = x__analyze_pod__mutmut_30 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_31'] = x__analyze_pod__mutmut_31 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_32'] = x__analyze_pod__mutmut_32 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_33'] = x__analyze_pod__mutmut_33 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_34'] = x__analyze_pod__mutmut_34 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_35'] = x__analyze_pod__mutmut_35 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_36'] = x__analyze_pod__mutmut_36 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_37'] = x__analyze_pod__mutmut_37 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_38'] = x__analyze_pod__mutmut_38 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_39'] = x__analyze_pod__mutmut_39 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_40'] = x__analyze_pod__mutmut_40 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_41'] = x__analyze_pod__mutmut_41 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_42'] = x__analyze_pod__mutmut_42 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_43'] = x__analyze_pod__mutmut_43 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_44'] = x__analyze_pod__mutmut_44 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_45'] = x__analyze_pod__mutmut_45 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_46'] = x__analyze_pod__mutmut_46 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_47'] = x__analyze_pod__mutmut_47 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_48'] = x__analyze_pod__mutmut_48 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_49'] = x__analyze_pod__mutmut_49 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_50'] = x__analyze_pod__mutmut_50 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_51'] = x__analyze_pod__mutmut_51 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_52'] = x__analyze_pod__mutmut_52 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_53'] = x__analyze_pod__mutmut_53 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_54'] = x__analyze_pod__mutmut_54 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_55'] = x__analyze_pod__mutmut_55 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_56'] = x__analyze_pod__mutmut_56 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_57'] = x__analyze_pod__mutmut_57 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_58'] = x__analyze_pod__mutmut_58 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_59'] = x__analyze_pod__mutmut_59 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_60'] = x__analyze_pod__mutmut_60 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_61'] = x__analyze_pod__mutmut_61 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_62'] = x__analyze_pod__mutmut_62 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_63'] = x__analyze_pod__mutmut_63 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_64'] = x__analyze_pod__mutmut_64 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_65'] = x__analyze_pod__mutmut_65 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_66'] = x__analyze_pod__mutmut_66 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_67'] = x__analyze_pod__mutmut_67 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_68'] = x__analyze_pod__mutmut_68 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_69'] = x__analyze_pod__mutmut_69 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_70'] = x__analyze_pod__mutmut_70 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_71'] = x__analyze_pod__mutmut_71 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_72'] = x__analyze_pod__mutmut_72 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_73'] = x__analyze_pod__mutmut_73 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_74'] = x__analyze_pod__mutmut_74 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_75'] = x__analyze_pod__mutmut_75 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_76'] = x__analyze_pod__mutmut_76 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_77'] = x__analyze_pod__mutmut_77 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_78'] = x__analyze_pod__mutmut_78 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_79'] = x__analyze_pod__mutmut_79 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_80'] = x__analyze_pod__mutmut_80 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_81'] = x__analyze_pod__mutmut_81 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_82'] = x__analyze_pod__mutmut_82 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_83'] = x__analyze_pod__mutmut_83 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_84'] = x__analyze_pod__mutmut_84 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_85'] = x__analyze_pod__mutmut_85 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_86'] = x__analyze_pod__mutmut_86 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_87'] = x__analyze_pod__mutmut_87 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_88'] = x__analyze_pod__mutmut_88 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_89'] = x__analyze_pod__mutmut_89 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_90'] = x__analyze_pod__mutmut_90 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_91'] = x__analyze_pod__mutmut_91 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_92'] = x__analyze_pod__mutmut_92 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_93'] = x__analyze_pod__mutmut_93 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_94'] = x__analyze_pod__mutmut_94 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_95'] = x__analyze_pod__mutmut_95 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_96'] = x__analyze_pod__mutmut_96 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_97'] = x__analyze_pod__mutmut_97 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_98'] = x__analyze_pod__mutmut_98 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_99'] = x__analyze_pod__mutmut_99 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_100'] = x__analyze_pod__mutmut_100 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_101'] = x__analyze_pod__mutmut_101 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_102'] = x__analyze_pod__mutmut_102 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_103'] = x__analyze_pod__mutmut_103 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_104'] = x__analyze_pod__mutmut_104 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_105'] = x__analyze_pod__mutmut_105 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_106'] = x__analyze_pod__mutmut_106 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_107'] = x__analyze_pod__mutmut_107 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_108'] = x__analyze_pod__mutmut_108 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_109'] = x__analyze_pod__mutmut_109 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_110'] = x__analyze_pod__mutmut_110 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_111'] = x__analyze_pod__mutmut_111 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_112'] = x__analyze_pod__mutmut_112 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_113'] = x__analyze_pod__mutmut_113 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_114'] = x__analyze_pod__mutmut_114 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_115'] = x__analyze_pod__mutmut_115 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_116'] = x__analyze_pod__mutmut_116 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_117'] = x__analyze_pod__mutmut_117 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_118'] = x__analyze_pod__mutmut_118 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_119'] = x__analyze_pod__mutmut_119 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_120'] = x__analyze_pod__mutmut_120 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_121'] = x__analyze_pod__mutmut_121 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_122'] = x__analyze_pod__mutmut_122 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_123'] = x__analyze_pod__mutmut_123 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_124'] = x__analyze_pod__mutmut_124 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_125'] = x__analyze_pod__mutmut_125 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_126'] = x__analyze_pod__mutmut_126 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_127'] = x__analyze_pod__mutmut_127 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_128'] = x__analyze_pod__mutmut_128 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_129'] = x__analyze_pod__mutmut_129 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_130'] = x__analyze_pod__mutmut_130 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_131'] = x__analyze_pod__mutmut_131 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_132'] = x__analyze_pod__mutmut_132 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_133'] = x__analyze_pod__mutmut_133 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_134'] = x__analyze_pod__mutmut_134 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_135'] = x__analyze_pod__mutmut_135 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_136'] = x__analyze_pod__mutmut_136 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_137'] = x__analyze_pod__mutmut_137 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_138'] = x__analyze_pod__mutmut_138 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_139'] = x__analyze_pod__mutmut_139 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_140'] = x__analyze_pod__mutmut_140 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_141'] = x__analyze_pod__mutmut_141 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_142'] = x__analyze_pod__mutmut_142 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_143'] = x__analyze_pod__mutmut_143 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_144'] = x__analyze_pod__mutmut_144 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_145'] = x__analyze_pod__mutmut_145 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_146'] = x__analyze_pod__mutmut_146 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_147'] = x__analyze_pod__mutmut_147 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_148'] = x__analyze_pod__mutmut_148 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_149'] = x__analyze_pod__mutmut_149 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_150'] = x__analyze_pod__mutmut_150 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_151'] = x__analyze_pod__mutmut_151 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_152'] = x__analyze_pod__mutmut_152 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_153'] = x__analyze_pod__mutmut_153 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_154'] = x__analyze_pod__mutmut_154 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_155'] = x__analyze_pod__mutmut_155 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_156'] = x__analyze_pod__mutmut_156 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_157'] = x__analyze_pod__mutmut_157 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_158'] = x__analyze_pod__mutmut_158 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_159'] = x__analyze_pod__mutmut_159 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_160'] = x__analyze_pod__mutmut_160 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_161'] = x__analyze_pod__mutmut_161 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_162'] = x__analyze_pod__mutmut_162 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_163'] = x__analyze_pod__mutmut_163 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_164'] = x__analyze_pod__mutmut_164 # type: ignore # mutmut generated
mutants_x__analyze_pod__mutmut['x__analyze_pod__mutmut_165'] = x__analyze_pod__mutmut_165 # type: ignore # mutmut generated
mutants_x__is_optimal__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__is_optimal__mutmut)
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


def x__is_optimal__mutmut_orig(
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


def x__is_optimal__mutmut_1(
    eff_cpu: float | None,
    eff_mem: float | None,
    cpu_p95: float | None,
    mem_p95: float | None,
) -> bool:
    ratios: list[float] = None
    if eff_cpu is not None and eff_cpu > 0 and cpu_p95 is not None:
        ratios.append(cpu_p95 / eff_cpu)
    if eff_mem is not None and eff_mem > 0 and mem_p95 is not None:
        ratios.append(mem_p95 / eff_mem)
    return bool(ratios) and all(r >= _OPTIMAL_RATIO for r in ratios)


def x__is_optimal__mutmut_2(
    eff_cpu: float | None,
    eff_mem: float | None,
    cpu_p95: float | None,
    mem_p95: float | None,
) -> bool:
    ratios: list[float] = []
    if eff_cpu is not None and eff_cpu > 0 or cpu_p95 is not None:
        ratios.append(cpu_p95 / eff_cpu)
    if eff_mem is not None and eff_mem > 0 and mem_p95 is not None:
        ratios.append(mem_p95 / eff_mem)
    return bool(ratios) and all(r >= _OPTIMAL_RATIO for r in ratios)


def x__is_optimal__mutmut_3(
    eff_cpu: float | None,
    eff_mem: float | None,
    cpu_p95: float | None,
    mem_p95: float | None,
) -> bool:
    ratios: list[float] = []
    if eff_cpu is not None or eff_cpu > 0 and cpu_p95 is not None:
        ratios.append(cpu_p95 / eff_cpu)
    if eff_mem is not None and eff_mem > 0 and mem_p95 is not None:
        ratios.append(mem_p95 / eff_mem)
    return bool(ratios) and all(r >= _OPTIMAL_RATIO for r in ratios)


def x__is_optimal__mutmut_4(
    eff_cpu: float | None,
    eff_mem: float | None,
    cpu_p95: float | None,
    mem_p95: float | None,
) -> bool:
    ratios: list[float] = []
    if eff_cpu is None and eff_cpu > 0 and cpu_p95 is not None:
        ratios.append(cpu_p95 / eff_cpu)
    if eff_mem is not None and eff_mem > 0 and mem_p95 is not None:
        ratios.append(mem_p95 / eff_mem)
    return bool(ratios) and all(r >= _OPTIMAL_RATIO for r in ratios)


def x__is_optimal__mutmut_5(
    eff_cpu: float | None,
    eff_mem: float | None,
    cpu_p95: float | None,
    mem_p95: float | None,
) -> bool:
    ratios: list[float] = []
    if eff_cpu is not None and eff_cpu >= 0 and cpu_p95 is not None:
        ratios.append(cpu_p95 / eff_cpu)
    if eff_mem is not None and eff_mem > 0 and mem_p95 is not None:
        ratios.append(mem_p95 / eff_mem)
    return bool(ratios) and all(r >= _OPTIMAL_RATIO for r in ratios)


def x__is_optimal__mutmut_6(
    eff_cpu: float | None,
    eff_mem: float | None,
    cpu_p95: float | None,
    mem_p95: float | None,
) -> bool:
    ratios: list[float] = []
    if eff_cpu is not None and eff_cpu > 1 and cpu_p95 is not None:
        ratios.append(cpu_p95 / eff_cpu)
    if eff_mem is not None and eff_mem > 0 and mem_p95 is not None:
        ratios.append(mem_p95 / eff_mem)
    return bool(ratios) and all(r >= _OPTIMAL_RATIO for r in ratios)


def x__is_optimal__mutmut_7(
    eff_cpu: float | None,
    eff_mem: float | None,
    cpu_p95: float | None,
    mem_p95: float | None,
) -> bool:
    ratios: list[float] = []
    if eff_cpu is not None and eff_cpu > 0 and cpu_p95 is None:
        ratios.append(cpu_p95 / eff_cpu)
    if eff_mem is not None and eff_mem > 0 and mem_p95 is not None:
        ratios.append(mem_p95 / eff_mem)
    return bool(ratios) and all(r >= _OPTIMAL_RATIO for r in ratios)


def x__is_optimal__mutmut_8(
    eff_cpu: float | None,
    eff_mem: float | None,
    cpu_p95: float | None,
    mem_p95: float | None,
) -> bool:
    ratios: list[float] = []
    if eff_cpu is not None and eff_cpu > 0 and cpu_p95 is not None:
        ratios.append(None)
    if eff_mem is not None and eff_mem > 0 and mem_p95 is not None:
        ratios.append(mem_p95 / eff_mem)
    return bool(ratios) and all(r >= _OPTIMAL_RATIO for r in ratios)


def x__is_optimal__mutmut_9(
    eff_cpu: float | None,
    eff_mem: float | None,
    cpu_p95: float | None,
    mem_p95: float | None,
) -> bool:
    ratios: list[float] = []
    if eff_cpu is not None and eff_cpu > 0 and cpu_p95 is not None:
        ratios.append(cpu_p95 * eff_cpu)
    if eff_mem is not None and eff_mem > 0 and mem_p95 is not None:
        ratios.append(mem_p95 / eff_mem)
    return bool(ratios) and all(r >= _OPTIMAL_RATIO for r in ratios)


def x__is_optimal__mutmut_10(
    eff_cpu: float | None,
    eff_mem: float | None,
    cpu_p95: float | None,
    mem_p95: float | None,
) -> bool:
    ratios: list[float] = []
    if eff_cpu is not None and eff_cpu > 0 and cpu_p95 is not None:
        ratios.append(cpu_p95 / eff_cpu)
    if eff_mem is not None and eff_mem > 0 or mem_p95 is not None:
        ratios.append(mem_p95 / eff_mem)
    return bool(ratios) and all(r >= _OPTIMAL_RATIO for r in ratios)


def x__is_optimal__mutmut_11(
    eff_cpu: float | None,
    eff_mem: float | None,
    cpu_p95: float | None,
    mem_p95: float | None,
) -> bool:
    ratios: list[float] = []
    if eff_cpu is not None and eff_cpu > 0 and cpu_p95 is not None:
        ratios.append(cpu_p95 / eff_cpu)
    if eff_mem is not None or eff_mem > 0 and mem_p95 is not None:
        ratios.append(mem_p95 / eff_mem)
    return bool(ratios) and all(r >= _OPTIMAL_RATIO for r in ratios)


def x__is_optimal__mutmut_12(
    eff_cpu: float | None,
    eff_mem: float | None,
    cpu_p95: float | None,
    mem_p95: float | None,
) -> bool:
    ratios: list[float] = []
    if eff_cpu is not None and eff_cpu > 0 and cpu_p95 is not None:
        ratios.append(cpu_p95 / eff_cpu)
    if eff_mem is None and eff_mem > 0 and mem_p95 is not None:
        ratios.append(mem_p95 / eff_mem)
    return bool(ratios) and all(r >= _OPTIMAL_RATIO for r in ratios)


def x__is_optimal__mutmut_13(
    eff_cpu: float | None,
    eff_mem: float | None,
    cpu_p95: float | None,
    mem_p95: float | None,
) -> bool:
    ratios: list[float] = []
    if eff_cpu is not None and eff_cpu > 0 and cpu_p95 is not None:
        ratios.append(cpu_p95 / eff_cpu)
    if eff_mem is not None and eff_mem >= 0 and mem_p95 is not None:
        ratios.append(mem_p95 / eff_mem)
    return bool(ratios) and all(r >= _OPTIMAL_RATIO for r in ratios)


def x__is_optimal__mutmut_14(
    eff_cpu: float | None,
    eff_mem: float | None,
    cpu_p95: float | None,
    mem_p95: float | None,
) -> bool:
    ratios: list[float] = []
    if eff_cpu is not None and eff_cpu > 0 and cpu_p95 is not None:
        ratios.append(cpu_p95 / eff_cpu)
    if eff_mem is not None and eff_mem > 1 and mem_p95 is not None:
        ratios.append(mem_p95 / eff_mem)
    return bool(ratios) and all(r >= _OPTIMAL_RATIO for r in ratios)


def x__is_optimal__mutmut_15(
    eff_cpu: float | None,
    eff_mem: float | None,
    cpu_p95: float | None,
    mem_p95: float | None,
) -> bool:
    ratios: list[float] = []
    if eff_cpu is not None and eff_cpu > 0 and cpu_p95 is not None:
        ratios.append(cpu_p95 / eff_cpu)
    if eff_mem is not None and eff_mem > 0 and mem_p95 is None:
        ratios.append(mem_p95 / eff_mem)
    return bool(ratios) and all(r >= _OPTIMAL_RATIO for r in ratios)


def x__is_optimal__mutmut_16(
    eff_cpu: float | None,
    eff_mem: float | None,
    cpu_p95: float | None,
    mem_p95: float | None,
) -> bool:
    ratios: list[float] = []
    if eff_cpu is not None and eff_cpu > 0 and cpu_p95 is not None:
        ratios.append(cpu_p95 / eff_cpu)
    if eff_mem is not None and eff_mem > 0 and mem_p95 is not None:
        ratios.append(None)
    return bool(ratios) and all(r >= _OPTIMAL_RATIO for r in ratios)


def x__is_optimal__mutmut_17(
    eff_cpu: float | None,
    eff_mem: float | None,
    cpu_p95: float | None,
    mem_p95: float | None,
) -> bool:
    ratios: list[float] = []
    if eff_cpu is not None and eff_cpu > 0 and cpu_p95 is not None:
        ratios.append(cpu_p95 / eff_cpu)
    if eff_mem is not None and eff_mem > 0 and mem_p95 is not None:
        ratios.append(mem_p95 * eff_mem)
    return bool(ratios) and all(r >= _OPTIMAL_RATIO for r in ratios)


def x__is_optimal__mutmut_18(
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
    return bool(ratios) or all(r >= _OPTIMAL_RATIO for r in ratios)


def x__is_optimal__mutmut_19(
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
    return bool(None) and all(r >= _OPTIMAL_RATIO for r in ratios)


def x__is_optimal__mutmut_20(
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
    return bool(ratios) and all(None)


def x__is_optimal__mutmut_21(
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
    return bool(ratios) and all(r > _OPTIMAL_RATIO for r in ratios)

mutants_x__is_optimal__mutmut['_mutmut_orig'] = x__is_optimal__mutmut_orig # type: ignore # mutmut generated
mutants_x__is_optimal__mutmut['x__is_optimal__mutmut_1'] = x__is_optimal__mutmut_1 # type: ignore # mutmut generated
mutants_x__is_optimal__mutmut['x__is_optimal__mutmut_2'] = x__is_optimal__mutmut_2 # type: ignore # mutmut generated
mutants_x__is_optimal__mutmut['x__is_optimal__mutmut_3'] = x__is_optimal__mutmut_3 # type: ignore # mutmut generated
mutants_x__is_optimal__mutmut['x__is_optimal__mutmut_4'] = x__is_optimal__mutmut_4 # type: ignore # mutmut generated
mutants_x__is_optimal__mutmut['x__is_optimal__mutmut_5'] = x__is_optimal__mutmut_5 # type: ignore # mutmut generated
mutants_x__is_optimal__mutmut['x__is_optimal__mutmut_6'] = x__is_optimal__mutmut_6 # type: ignore # mutmut generated
mutants_x__is_optimal__mutmut['x__is_optimal__mutmut_7'] = x__is_optimal__mutmut_7 # type: ignore # mutmut generated
mutants_x__is_optimal__mutmut['x__is_optimal__mutmut_8'] = x__is_optimal__mutmut_8 # type: ignore # mutmut generated
mutants_x__is_optimal__mutmut['x__is_optimal__mutmut_9'] = x__is_optimal__mutmut_9 # type: ignore # mutmut generated
mutants_x__is_optimal__mutmut['x__is_optimal__mutmut_10'] = x__is_optimal__mutmut_10 # type: ignore # mutmut generated
mutants_x__is_optimal__mutmut['x__is_optimal__mutmut_11'] = x__is_optimal__mutmut_11 # type: ignore # mutmut generated
mutants_x__is_optimal__mutmut['x__is_optimal__mutmut_12'] = x__is_optimal__mutmut_12 # type: ignore # mutmut generated
mutants_x__is_optimal__mutmut['x__is_optimal__mutmut_13'] = x__is_optimal__mutmut_13 # type: ignore # mutmut generated
mutants_x__is_optimal__mutmut['x__is_optimal__mutmut_14'] = x__is_optimal__mutmut_14 # type: ignore # mutmut generated
mutants_x__is_optimal__mutmut['x__is_optimal__mutmut_15'] = x__is_optimal__mutmut_15 # type: ignore # mutmut generated
mutants_x__is_optimal__mutmut['x__is_optimal__mutmut_16'] = x__is_optimal__mutmut_16 # type: ignore # mutmut generated
mutants_x__is_optimal__mutmut['x__is_optimal__mutmut_17'] = x__is_optimal__mutmut_17 # type: ignore # mutmut generated
mutants_x__is_optimal__mutmut['x__is_optimal__mutmut_18'] = x__is_optimal__mutmut_18 # type: ignore # mutmut generated
mutants_x__is_optimal__mutmut['x__is_optimal__mutmut_19'] = x__is_optimal__mutmut_19 # type: ignore # mutmut generated
mutants_x__is_optimal__mutmut['x__is_optimal__mutmut_20'] = x__is_optimal__mutmut_20 # type: ignore # mutmut generated
mutants_x__is_optimal__mutmut['x__is_optimal__mutmut_21'] = x__is_optimal__mutmut_21 # type: ignore # mutmut generated
mutants_x__recommended__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__recommended__mutmut)
def _recommended(request: float | None, p95: float | None) -> float | None:
    if p95 is None or request is None:
        return request
    rec = p95 * _P95_BUFFER
    if request > 0.1:  # CPU vs memory threshold  # noqa: PLR2004
        return round(max(rec, _MIN_CPU_CORES), 3)
    return round(max(rec, _MIN_MEM_MI), 1)


def x__recommended__mutmut_orig(request: float | None, p95: float | None) -> float | None:
    if p95 is None or request is None:
        return request
    rec = p95 * _P95_BUFFER
    if request > 0.1:  # CPU vs memory threshold  # noqa: PLR2004
        return round(max(rec, _MIN_CPU_CORES), 3)
    return round(max(rec, _MIN_MEM_MI), 1)


def x__recommended__mutmut_1(request: float | None, p95: float | None) -> float | None:
    if p95 is None and request is None:
        return request
    rec = p95 * _P95_BUFFER
    if request > 0.1:  # CPU vs memory threshold  # noqa: PLR2004
        return round(max(rec, _MIN_CPU_CORES), 3)
    return round(max(rec, _MIN_MEM_MI), 1)


def x__recommended__mutmut_2(request: float | None, p95: float | None) -> float | None:
    if p95 is not None or request is None:
        return request
    rec = p95 * _P95_BUFFER
    if request > 0.1:  # CPU vs memory threshold  # noqa: PLR2004
        return round(max(rec, _MIN_CPU_CORES), 3)
    return round(max(rec, _MIN_MEM_MI), 1)


def x__recommended__mutmut_3(request: float | None, p95: float | None) -> float | None:
    if p95 is None or request is not None:
        return request
    rec = p95 * _P95_BUFFER
    if request > 0.1:  # CPU vs memory threshold  # noqa: PLR2004
        return round(max(rec, _MIN_CPU_CORES), 3)
    return round(max(rec, _MIN_MEM_MI), 1)


def x__recommended__mutmut_4(request: float | None, p95: float | None) -> float | None:
    if p95 is None or request is None:
        return request
    rec = None
    if request > 0.1:  # CPU vs memory threshold  # noqa: PLR2004
        return round(max(rec, _MIN_CPU_CORES), 3)
    return round(max(rec, _MIN_MEM_MI), 1)


def x__recommended__mutmut_5(request: float | None, p95: float | None) -> float | None:
    if p95 is None or request is None:
        return request
    rec = p95 / _P95_BUFFER
    if request > 0.1:  # CPU vs memory threshold  # noqa: PLR2004
        return round(max(rec, _MIN_CPU_CORES), 3)
    return round(max(rec, _MIN_MEM_MI), 1)


def x__recommended__mutmut_6(request: float | None, p95: float | None) -> float | None:
    if p95 is None or request is None:
        return request
    rec = p95 * _P95_BUFFER
    if request >= 0.1:  # CPU vs memory threshold  # noqa: PLR2004
        return round(max(rec, _MIN_CPU_CORES), 3)
    return round(max(rec, _MIN_MEM_MI), 1)


def x__recommended__mutmut_7(request: float | None, p95: float | None) -> float | None:
    if p95 is None or request is None:
        return request
    rec = p95 * _P95_BUFFER
    if request > 1.1:  # CPU vs memory threshold  # noqa: PLR2004
        return round(max(rec, _MIN_CPU_CORES), 3)
    return round(max(rec, _MIN_MEM_MI), 1)


def x__recommended__mutmut_8(request: float | None, p95: float | None) -> float | None:
    if p95 is None or request is None:
        return request
    rec = p95 * _P95_BUFFER
    if request > 0.1:  # CPU vs memory threshold  # noqa: PLR2004
        return round(None, 3)
    return round(max(rec, _MIN_MEM_MI), 1)


def x__recommended__mutmut_9(request: float | None, p95: float | None) -> float | None:
    if p95 is None or request is None:
        return request
    rec = p95 * _P95_BUFFER
    if request > 0.1:  # CPU vs memory threshold  # noqa: PLR2004
        return round(max(rec, _MIN_CPU_CORES), None)
    return round(max(rec, _MIN_MEM_MI), 1)


def x__recommended__mutmut_10(request: float | None, p95: float | None) -> float | None:
    if p95 is None or request is None:
        return request
    rec = p95 * _P95_BUFFER
    if request > 0.1:  # CPU vs memory threshold  # noqa: PLR2004
        return round(3)
    return round(max(rec, _MIN_MEM_MI), 1)


def x__recommended__mutmut_11(request: float | None, p95: float | None) -> float | None:
    if p95 is None or request is None:
        return request
    rec = p95 * _P95_BUFFER
    if request > 0.1:  # CPU vs memory threshold  # noqa: PLR2004
        return round(max(rec, _MIN_CPU_CORES), )
    return round(max(rec, _MIN_MEM_MI), 1)


def x__recommended__mutmut_12(request: float | None, p95: float | None) -> float | None:
    if p95 is None or request is None:
        return request
    rec = p95 * _P95_BUFFER
    if request > 0.1:  # CPU vs memory threshold  # noqa: PLR2004
        return round(max(None, _MIN_CPU_CORES), 3)
    return round(max(rec, _MIN_MEM_MI), 1)


def x__recommended__mutmut_13(request: float | None, p95: float | None) -> float | None:
    if p95 is None or request is None:
        return request
    rec = p95 * _P95_BUFFER
    if request > 0.1:  # CPU vs memory threshold  # noqa: PLR2004
        return round(max(rec, None), 3)
    return round(max(rec, _MIN_MEM_MI), 1)


def x__recommended__mutmut_14(request: float | None, p95: float | None) -> float | None:
    if p95 is None or request is None:
        return request
    rec = p95 * _P95_BUFFER
    if request > 0.1:  # CPU vs memory threshold  # noqa: PLR2004
        return round(max(_MIN_CPU_CORES), 3)
    return round(max(rec, _MIN_MEM_MI), 1)


def x__recommended__mutmut_15(request: float | None, p95: float | None) -> float | None:
    if p95 is None or request is None:
        return request
    rec = p95 * _P95_BUFFER
    if request > 0.1:  # CPU vs memory threshold  # noqa: PLR2004
        return round(max(rec, ), 3)
    return round(max(rec, _MIN_MEM_MI), 1)


def x__recommended__mutmut_16(request: float | None, p95: float | None) -> float | None:
    if p95 is None or request is None:
        return request
    rec = p95 * _P95_BUFFER
    if request > 0.1:  # CPU vs memory threshold  # noqa: PLR2004
        return round(max(rec, _MIN_CPU_CORES), 4)
    return round(max(rec, _MIN_MEM_MI), 1)


def x__recommended__mutmut_17(request: float | None, p95: float | None) -> float | None:
    if p95 is None or request is None:
        return request
    rec = p95 * _P95_BUFFER
    if request > 0.1:  # CPU vs memory threshold  # noqa: PLR2004
        return round(max(rec, _MIN_CPU_CORES), 3)
    return round(None, 1)


def x__recommended__mutmut_18(request: float | None, p95: float | None) -> float | None:
    if p95 is None or request is None:
        return request
    rec = p95 * _P95_BUFFER
    if request > 0.1:  # CPU vs memory threshold  # noqa: PLR2004
        return round(max(rec, _MIN_CPU_CORES), 3)
    return round(max(rec, _MIN_MEM_MI), None)


def x__recommended__mutmut_19(request: float | None, p95: float | None) -> float | None:
    if p95 is None or request is None:
        return request
    rec = p95 * _P95_BUFFER
    if request > 0.1:  # CPU vs memory threshold  # noqa: PLR2004
        return round(max(rec, _MIN_CPU_CORES), 3)
    return round(1)


def x__recommended__mutmut_20(request: float | None, p95: float | None) -> float | None:
    if p95 is None or request is None:
        return request
    rec = p95 * _P95_BUFFER
    if request > 0.1:  # CPU vs memory threshold  # noqa: PLR2004
        return round(max(rec, _MIN_CPU_CORES), 3)
    return round(max(rec, _MIN_MEM_MI), )


def x__recommended__mutmut_21(request: float | None, p95: float | None) -> float | None:
    if p95 is None or request is None:
        return request
    rec = p95 * _P95_BUFFER
    if request > 0.1:  # CPU vs memory threshold  # noqa: PLR2004
        return round(max(rec, _MIN_CPU_CORES), 3)
    return round(max(None, _MIN_MEM_MI), 1)


def x__recommended__mutmut_22(request: float | None, p95: float | None) -> float | None:
    if p95 is None or request is None:
        return request
    rec = p95 * _P95_BUFFER
    if request > 0.1:  # CPU vs memory threshold  # noqa: PLR2004
        return round(max(rec, _MIN_CPU_CORES), 3)
    return round(max(rec, None), 1)


def x__recommended__mutmut_23(request: float | None, p95: float | None) -> float | None:
    if p95 is None or request is None:
        return request
    rec = p95 * _P95_BUFFER
    if request > 0.1:  # CPU vs memory threshold  # noqa: PLR2004
        return round(max(rec, _MIN_CPU_CORES), 3)
    return round(max(_MIN_MEM_MI), 1)


def x__recommended__mutmut_24(request: float | None, p95: float | None) -> float | None:
    if p95 is None or request is None:
        return request
    rec = p95 * _P95_BUFFER
    if request > 0.1:  # CPU vs memory threshold  # noqa: PLR2004
        return round(max(rec, _MIN_CPU_CORES), 3)
    return round(max(rec, ), 1)


def x__recommended__mutmut_25(request: float | None, p95: float | None) -> float | None:
    if p95 is None or request is None:
        return request
    rec = p95 * _P95_BUFFER
    if request > 0.1:  # CPU vs memory threshold  # noqa: PLR2004
        return round(max(rec, _MIN_CPU_CORES), 3)
    return round(max(rec, _MIN_MEM_MI), 2)

mutants_x__recommended__mutmut['_mutmut_orig'] = x__recommended__mutmut_orig # type: ignore # mutmut generated
mutants_x__recommended__mutmut['x__recommended__mutmut_1'] = x__recommended__mutmut_1 # type: ignore # mutmut generated
mutants_x__recommended__mutmut['x__recommended__mutmut_2'] = x__recommended__mutmut_2 # type: ignore # mutmut generated
mutants_x__recommended__mutmut['x__recommended__mutmut_3'] = x__recommended__mutmut_3 # type: ignore # mutmut generated
mutants_x__recommended__mutmut['x__recommended__mutmut_4'] = x__recommended__mutmut_4 # type: ignore # mutmut generated
mutants_x__recommended__mutmut['x__recommended__mutmut_5'] = x__recommended__mutmut_5 # type: ignore # mutmut generated
mutants_x__recommended__mutmut['x__recommended__mutmut_6'] = x__recommended__mutmut_6 # type: ignore # mutmut generated
mutants_x__recommended__mutmut['x__recommended__mutmut_7'] = x__recommended__mutmut_7 # type: ignore # mutmut generated
mutants_x__recommended__mutmut['x__recommended__mutmut_8'] = x__recommended__mutmut_8 # type: ignore # mutmut generated
mutants_x__recommended__mutmut['x__recommended__mutmut_9'] = x__recommended__mutmut_9 # type: ignore # mutmut generated
mutants_x__recommended__mutmut['x__recommended__mutmut_10'] = x__recommended__mutmut_10 # type: ignore # mutmut generated
mutants_x__recommended__mutmut['x__recommended__mutmut_11'] = x__recommended__mutmut_11 # type: ignore # mutmut generated
mutants_x__recommended__mutmut['x__recommended__mutmut_12'] = x__recommended__mutmut_12 # type: ignore # mutmut generated
mutants_x__recommended__mutmut['x__recommended__mutmut_13'] = x__recommended__mutmut_13 # type: ignore # mutmut generated
mutants_x__recommended__mutmut['x__recommended__mutmut_14'] = x__recommended__mutmut_14 # type: ignore # mutmut generated
mutants_x__recommended__mutmut['x__recommended__mutmut_15'] = x__recommended__mutmut_15 # type: ignore # mutmut generated
mutants_x__recommended__mutmut['x__recommended__mutmut_16'] = x__recommended__mutmut_16 # type: ignore # mutmut generated
mutants_x__recommended__mutmut['x__recommended__mutmut_17'] = x__recommended__mutmut_17 # type: ignore # mutmut generated
mutants_x__recommended__mutmut['x__recommended__mutmut_18'] = x__recommended__mutmut_18 # type: ignore # mutmut generated
mutants_x__recommended__mutmut['x__recommended__mutmut_19'] = x__recommended__mutmut_19 # type: ignore # mutmut generated
mutants_x__recommended__mutmut['x__recommended__mutmut_20'] = x__recommended__mutmut_20 # type: ignore # mutmut generated
mutants_x__recommended__mutmut['x__recommended__mutmut_21'] = x__recommended__mutmut_21 # type: ignore # mutmut generated
mutants_x__recommended__mutmut['x__recommended__mutmut_22'] = x__recommended__mutmut_22 # type: ignore # mutmut generated
mutants_x__recommended__mutmut['x__recommended__mutmut_23'] = x__recommended__mutmut_23 # type: ignore # mutmut generated
mutants_x__recommended__mutmut['x__recommended__mutmut_24'] = x__recommended__mutmut_24 # type: ignore # mutmut generated
mutants_x__recommended__mutmut['x__recommended__mutmut_25'] = x__recommended__mutmut_25 # type: ignore # mutmut generated
mutants_x__delta__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__delta__mutmut)
def _delta(eff: float | None, rec: float | None, digits: int) -> float:
    if eff is None:
        return 0.0
    return round(max(0.0, eff - (rec if rec is not None else eff)), digits)


def x__delta__mutmut_orig(eff: float | None, rec: float | None, digits: int) -> float:
    if eff is None:
        return 0.0
    return round(max(0.0, eff - (rec if rec is not None else eff)), digits)


def x__delta__mutmut_1(eff: float | None, rec: float | None, digits: int) -> float:
    if eff is not None:
        return 0.0
    return round(max(0.0, eff - (rec if rec is not None else eff)), digits)


def x__delta__mutmut_2(eff: float | None, rec: float | None, digits: int) -> float:
    if eff is None:
        return 1.0
    return round(max(0.0, eff - (rec if rec is not None else eff)), digits)


def x__delta__mutmut_3(eff: float | None, rec: float | None, digits: int) -> float:
    if eff is None:
        return 0.0
    return round(None, digits)


def x__delta__mutmut_4(eff: float | None, rec: float | None, digits: int) -> float:
    if eff is None:
        return 0.0
    return round(max(0.0, eff - (rec if rec is not None else eff)), None)


def x__delta__mutmut_5(eff: float | None, rec: float | None, digits: int) -> float:
    if eff is None:
        return 0.0
    return round(digits)


def x__delta__mutmut_6(eff: float | None, rec: float | None, digits: int) -> float:
    if eff is None:
        return 0.0
    return round(max(0.0, eff - (rec if rec is not None else eff)), )


def x__delta__mutmut_7(eff: float | None, rec: float | None, digits: int) -> float:
    if eff is None:
        return 0.0
    return round(max(None, eff - (rec if rec is not None else eff)), digits)


def x__delta__mutmut_8(eff: float | None, rec: float | None, digits: int) -> float:
    if eff is None:
        return 0.0
    return round(max(0.0, None), digits)


def x__delta__mutmut_9(eff: float | None, rec: float | None, digits: int) -> float:
    if eff is None:
        return 0.0
    return round(max(eff - (rec if rec is not None else eff)), digits)


def x__delta__mutmut_10(eff: float | None, rec: float | None, digits: int) -> float:
    if eff is None:
        return 0.0
    return round(max(0.0, ), digits)


def x__delta__mutmut_11(eff: float | None, rec: float | None, digits: int) -> float:
    if eff is None:
        return 0.0
    return round(max(1.0, eff - (rec if rec is not None else eff)), digits)


def x__delta__mutmut_12(eff: float | None, rec: float | None, digits: int) -> float:
    if eff is None:
        return 0.0
    return round(max(0.0, eff + (rec if rec is not None else eff)), digits)


def x__delta__mutmut_13(eff: float | None, rec: float | None, digits: int) -> float:
    if eff is None:
        return 0.0
    return round(max(0.0, eff - (rec if rec is None else eff)), digits)

mutants_x__delta__mutmut['_mutmut_orig'] = x__delta__mutmut_orig # type: ignore # mutmut generated
mutants_x__delta__mutmut['x__delta__mutmut_1'] = x__delta__mutmut_1 # type: ignore # mutmut generated
mutants_x__delta__mutmut['x__delta__mutmut_2'] = x__delta__mutmut_2 # type: ignore # mutmut generated
mutants_x__delta__mutmut['x__delta__mutmut_3'] = x__delta__mutmut_3 # type: ignore # mutmut generated
mutants_x__delta__mutmut['x__delta__mutmut_4'] = x__delta__mutmut_4 # type: ignore # mutmut generated
mutants_x__delta__mutmut['x__delta__mutmut_5'] = x__delta__mutmut_5 # type: ignore # mutmut generated
mutants_x__delta__mutmut['x__delta__mutmut_6'] = x__delta__mutmut_6 # type: ignore # mutmut generated
mutants_x__delta__mutmut['x__delta__mutmut_7'] = x__delta__mutmut_7 # type: ignore # mutmut generated
mutants_x__delta__mutmut['x__delta__mutmut_8'] = x__delta__mutmut_8 # type: ignore # mutmut generated
mutants_x__delta__mutmut['x__delta__mutmut_9'] = x__delta__mutmut_9 # type: ignore # mutmut generated
mutants_x__delta__mutmut['x__delta__mutmut_10'] = x__delta__mutmut_10 # type: ignore # mutmut generated
mutants_x__delta__mutmut['x__delta__mutmut_11'] = x__delta__mutmut_11 # type: ignore # mutmut generated
mutants_x__delta__mutmut['x__delta__mutmut_12'] = x__delta__mutmut_12 # type: ignore # mutmut generated
mutants_x__delta__mutmut['x__delta__mutmut_13'] = x__delta__mutmut_13 # type: ignore # mutmut generated
mutants_x__bursty__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__bursty__mutmut)
def _bursty(cpu_p95: float | None, cpu_max: float | None) -> bool:
    if cpu_p95 is None or cpu_max is None or cpu_p95 <= 0:
        return False
    return cpu_max / cpu_p95 > _BURSTY_MAX_P95_RATIO


def x__bursty__mutmut_orig(cpu_p95: float | None, cpu_max: float | None) -> bool:
    if cpu_p95 is None or cpu_max is None or cpu_p95 <= 0:
        return False
    return cpu_max / cpu_p95 > _BURSTY_MAX_P95_RATIO


def x__bursty__mutmut_1(cpu_p95: float | None, cpu_max: float | None) -> bool:
    if cpu_p95 is None or cpu_max is None and cpu_p95 <= 0:
        return False
    return cpu_max / cpu_p95 > _BURSTY_MAX_P95_RATIO


def x__bursty__mutmut_2(cpu_p95: float | None, cpu_max: float | None) -> bool:
    if cpu_p95 is None and cpu_max is None or cpu_p95 <= 0:
        return False
    return cpu_max / cpu_p95 > _BURSTY_MAX_P95_RATIO


def x__bursty__mutmut_3(cpu_p95: float | None, cpu_max: float | None) -> bool:
    if cpu_p95 is not None or cpu_max is None or cpu_p95 <= 0:
        return False
    return cpu_max / cpu_p95 > _BURSTY_MAX_P95_RATIO


def x__bursty__mutmut_4(cpu_p95: float | None, cpu_max: float | None) -> bool:
    if cpu_p95 is None or cpu_max is not None or cpu_p95 <= 0:
        return False
    return cpu_max / cpu_p95 > _BURSTY_MAX_P95_RATIO


def x__bursty__mutmut_5(cpu_p95: float | None, cpu_max: float | None) -> bool:
    if cpu_p95 is None or cpu_max is None or cpu_p95 < 0:
        return False
    return cpu_max / cpu_p95 > _BURSTY_MAX_P95_RATIO


def x__bursty__mutmut_6(cpu_p95: float | None, cpu_max: float | None) -> bool:
    if cpu_p95 is None or cpu_max is None or cpu_p95 <= 1:
        return False
    return cpu_max / cpu_p95 > _BURSTY_MAX_P95_RATIO


def x__bursty__mutmut_7(cpu_p95: float | None, cpu_max: float | None) -> bool:
    if cpu_p95 is None or cpu_max is None or cpu_p95 <= 0:
        return True
    return cpu_max / cpu_p95 > _BURSTY_MAX_P95_RATIO


def x__bursty__mutmut_8(cpu_p95: float | None, cpu_max: float | None) -> bool:
    if cpu_p95 is None or cpu_max is None or cpu_p95 <= 0:
        return False
    return cpu_max * cpu_p95 > _BURSTY_MAX_P95_RATIO


def x__bursty__mutmut_9(cpu_p95: float | None, cpu_max: float | None) -> bool:
    if cpu_p95 is None or cpu_max is None or cpu_p95 <= 0:
        return False
    return cpu_max / cpu_p95 >= _BURSTY_MAX_P95_RATIO

mutants_x__bursty__mutmut['_mutmut_orig'] = x__bursty__mutmut_orig # type: ignore # mutmut generated
mutants_x__bursty__mutmut['x__bursty__mutmut_1'] = x__bursty__mutmut_1 # type: ignore # mutmut generated
mutants_x__bursty__mutmut['x__bursty__mutmut_2'] = x__bursty__mutmut_2 # type: ignore # mutmut generated
mutants_x__bursty__mutmut['x__bursty__mutmut_3'] = x__bursty__mutmut_3 # type: ignore # mutmut generated
mutants_x__bursty__mutmut['x__bursty__mutmut_4'] = x__bursty__mutmut_4 # type: ignore # mutmut generated
mutants_x__bursty__mutmut['x__bursty__mutmut_5'] = x__bursty__mutmut_5 # type: ignore # mutmut generated
mutants_x__bursty__mutmut['x__bursty__mutmut_6'] = x__bursty__mutmut_6 # type: ignore # mutmut generated
mutants_x__bursty__mutmut['x__bursty__mutmut_7'] = x__bursty__mutmut_7 # type: ignore # mutmut generated
mutants_x__bursty__mutmut['x__bursty__mutmut_8'] = x__bursty__mutmut_8 # type: ignore # mutmut generated
mutants_x__bursty__mutmut['x__bursty__mutmut_9'] = x__bursty__mutmut_9 # type: ignore # mutmut generated
mutants_x__rank_opportunities__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__rank_opportunities__mutmut)
def _rank_opportunities(
    opportunities: list[PodSavingOpportunity], top_n: int
) -> list[PodSavingOpportunity]:
    return sorted(
        opportunities,
        key=lambda o: o.monthly_saving_usd if o.monthly_saving_usd is not None else 0.0,
        reverse=True,
    )[:top_n]


def x__rank_opportunities__mutmut_orig(
    opportunities: list[PodSavingOpportunity], top_n: int
) -> list[PodSavingOpportunity]:
    return sorted(
        opportunities,
        key=lambda o: o.monthly_saving_usd if o.monthly_saving_usd is not None else 0.0,
        reverse=True,
    )[:top_n]


def x__rank_opportunities__mutmut_1(
    opportunities: list[PodSavingOpportunity], top_n: int
) -> list[PodSavingOpportunity]:
    return sorted(
        None,
        key=lambda o: o.monthly_saving_usd if o.monthly_saving_usd is not None else 0.0,
        reverse=True,
    )[:top_n]


def x__rank_opportunities__mutmut_2(
    opportunities: list[PodSavingOpportunity], top_n: int
) -> list[PodSavingOpportunity]:
    return sorted(
        opportunities,
        key=None,
        reverse=True,
    )[:top_n]


def x__rank_opportunities__mutmut_3(
    opportunities: list[PodSavingOpportunity], top_n: int
) -> list[PodSavingOpportunity]:
    return sorted(
        opportunities,
        key=lambda o: o.monthly_saving_usd if o.monthly_saving_usd is not None else 0.0,
        reverse=None,
    )[:top_n]


def x__rank_opportunities__mutmut_4(
    opportunities: list[PodSavingOpportunity], top_n: int
) -> list[PodSavingOpportunity]:
    return sorted(
        key=lambda o: o.monthly_saving_usd if o.monthly_saving_usd is not None else 0.0,
        reverse=True,
    )[:top_n]


def x__rank_opportunities__mutmut_5(
    opportunities: list[PodSavingOpportunity], top_n: int
) -> list[PodSavingOpportunity]:
    return sorted(
        opportunities,
        reverse=True,
    )[:top_n]


def x__rank_opportunities__mutmut_6(
    opportunities: list[PodSavingOpportunity], top_n: int
) -> list[PodSavingOpportunity]:
    return sorted(
        opportunities,
        key=lambda o: o.monthly_saving_usd if o.monthly_saving_usd is not None else 0.0,
        )[:top_n]


def x__rank_opportunities__mutmut_7(
    opportunities: list[PodSavingOpportunity], top_n: int
) -> list[PodSavingOpportunity]:
    return sorted(
        opportunities,
        key=lambda o: None,
        reverse=True,
    )[:top_n]


def x__rank_opportunities__mutmut_8(
    opportunities: list[PodSavingOpportunity], top_n: int
) -> list[PodSavingOpportunity]:
    return sorted(
        opportunities,
        key=lambda o: o.monthly_saving_usd if o.monthly_saving_usd is None else 0.0,
        reverse=True,
    )[:top_n]


def x__rank_opportunities__mutmut_9(
    opportunities: list[PodSavingOpportunity], top_n: int
) -> list[PodSavingOpportunity]:
    return sorted(
        opportunities,
        key=lambda o: o.monthly_saving_usd if o.monthly_saving_usd is not None else 1.0,
        reverse=True,
    )[:top_n]


def x__rank_opportunities__mutmut_10(
    opportunities: list[PodSavingOpportunity], top_n: int
) -> list[PodSavingOpportunity]:
    return sorted(
        opportunities,
        key=lambda o: o.monthly_saving_usd if o.monthly_saving_usd is not None else 0.0,
        reverse=False,
    )[:top_n]

mutants_x__rank_opportunities__mutmut['_mutmut_orig'] = x__rank_opportunities__mutmut_orig # type: ignore # mutmut generated
mutants_x__rank_opportunities__mutmut['x__rank_opportunities__mutmut_1'] = x__rank_opportunities__mutmut_1 # type: ignore # mutmut generated
mutants_x__rank_opportunities__mutmut['x__rank_opportunities__mutmut_2'] = x__rank_opportunities__mutmut_2 # type: ignore # mutmut generated
mutants_x__rank_opportunities__mutmut['x__rank_opportunities__mutmut_3'] = x__rank_opportunities__mutmut_3 # type: ignore # mutmut generated
mutants_x__rank_opportunities__mutmut['x__rank_opportunities__mutmut_4'] = x__rank_opportunities__mutmut_4 # type: ignore # mutmut generated
mutants_x__rank_opportunities__mutmut['x__rank_opportunities__mutmut_5'] = x__rank_opportunities__mutmut_5 # type: ignore # mutmut generated
mutants_x__rank_opportunities__mutmut['x__rank_opportunities__mutmut_6'] = x__rank_opportunities__mutmut_6 # type: ignore # mutmut generated
mutants_x__rank_opportunities__mutmut['x__rank_opportunities__mutmut_7'] = x__rank_opportunities__mutmut_7 # type: ignore # mutmut generated
mutants_x__rank_opportunities__mutmut['x__rank_opportunities__mutmut_8'] = x__rank_opportunities__mutmut_8 # type: ignore # mutmut generated
mutants_x__rank_opportunities__mutmut['x__rank_opportunities__mutmut_9'] = x__rank_opportunities__mutmut_9 # type: ignore # mutmut generated
mutants_x__rank_opportunities__mutmut['x__rank_opportunities__mutmut_10'] = x__rank_opportunities__mutmut_10 # type: ignore # mutmut generated
mutants_xǁ_NsAccumulatorǁ__init____mutmut: MutantDict = {}  # type: ignore


class _NsAccumulator:
    @_mutmut_mutated(mutants_xǁ_NsAccumulatorǁ__init____mutmut)
    def __init__(self) -> None:
        self.pod_count: int = 0
        self.delta_cores: float = 0.0
        self.delta_mi: float = 0.0
        self.usd: float = 0.0
        self.has_usd: bool = False
    def xǁ_NsAccumulatorǁ__init____mutmut_orig(self) -> None:
        self.pod_count: int = 0
        self.delta_cores: float = 0.0
        self.delta_mi: float = 0.0
        self.usd: float = 0.0
        self.has_usd: bool = False
    def xǁ_NsAccumulatorǁ__init____mutmut_1(self) -> None:
        self.pod_count: int = None
        self.delta_cores: float = 0.0
        self.delta_mi: float = 0.0
        self.usd: float = 0.0
        self.has_usd: bool = False
    def xǁ_NsAccumulatorǁ__init____mutmut_2(self) -> None:
        self.pod_count: int = 1
        self.delta_cores: float = 0.0
        self.delta_mi: float = 0.0
        self.usd: float = 0.0
        self.has_usd: bool = False
    def xǁ_NsAccumulatorǁ__init____mutmut_3(self) -> None:
        self.pod_count: int = 0
        self.delta_cores: float = None
        self.delta_mi: float = 0.0
        self.usd: float = 0.0
        self.has_usd: bool = False
    def xǁ_NsAccumulatorǁ__init____mutmut_4(self) -> None:
        self.pod_count: int = 0
        self.delta_cores: float = 1.0
        self.delta_mi: float = 0.0
        self.usd: float = 0.0
        self.has_usd: bool = False
    def xǁ_NsAccumulatorǁ__init____mutmut_5(self) -> None:
        self.pod_count: int = 0
        self.delta_cores: float = 0.0
        self.delta_mi: float = None
        self.usd: float = 0.0
        self.has_usd: bool = False
    def xǁ_NsAccumulatorǁ__init____mutmut_6(self) -> None:
        self.pod_count: int = 0
        self.delta_cores: float = 0.0
        self.delta_mi: float = 1.0
        self.usd: float = 0.0
        self.has_usd: bool = False
    def xǁ_NsAccumulatorǁ__init____mutmut_7(self) -> None:
        self.pod_count: int = 0
        self.delta_cores: float = 0.0
        self.delta_mi: float = 0.0
        self.usd: float = None
        self.has_usd: bool = False
    def xǁ_NsAccumulatorǁ__init____mutmut_8(self) -> None:
        self.pod_count: int = 0
        self.delta_cores: float = 0.0
        self.delta_mi: float = 0.0
        self.usd: float = 1.0
        self.has_usd: bool = False
    def xǁ_NsAccumulatorǁ__init____mutmut_9(self) -> None:
        self.pod_count: int = 0
        self.delta_cores: float = 0.0
        self.delta_mi: float = 0.0
        self.usd: float = 0.0
        self.has_usd: bool = None
    def xǁ_NsAccumulatorǁ__init____mutmut_10(self) -> None:
        self.pod_count: int = 0
        self.delta_cores: float = 0.0
        self.delta_mi: float = 0.0
        self.usd: float = 0.0
        self.has_usd: bool = True

mutants_xǁ_NsAccumulatorǁ__init____mutmut['_mutmut_orig'] = _NsAccumulator.xǁ_NsAccumulatorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁ_NsAccumulatorǁ__init____mutmut['xǁ_NsAccumulatorǁ__init____mutmut_1'] = _NsAccumulator.xǁ_NsAccumulatorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁ_NsAccumulatorǁ__init____mutmut['xǁ_NsAccumulatorǁ__init____mutmut_2'] = _NsAccumulator.xǁ_NsAccumulatorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁ_NsAccumulatorǁ__init____mutmut['xǁ_NsAccumulatorǁ__init____mutmut_3'] = _NsAccumulator.xǁ_NsAccumulatorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁ_NsAccumulatorǁ__init____mutmut['xǁ_NsAccumulatorǁ__init____mutmut_4'] = _NsAccumulator.xǁ_NsAccumulatorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁ_NsAccumulatorǁ__init____mutmut['xǁ_NsAccumulatorǁ__init____mutmut_5'] = _NsAccumulator.xǁ_NsAccumulatorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁ_NsAccumulatorǁ__init____mutmut['xǁ_NsAccumulatorǁ__init____mutmut_6'] = _NsAccumulator.xǁ_NsAccumulatorǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁ_NsAccumulatorǁ__init____mutmut['xǁ_NsAccumulatorǁ__init____mutmut_7'] = _NsAccumulator.xǁ_NsAccumulatorǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁ_NsAccumulatorǁ__init____mutmut['xǁ_NsAccumulatorǁ__init____mutmut_8'] = _NsAccumulator.xǁ_NsAccumulatorǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁ_NsAccumulatorǁ__init____mutmut['xǁ_NsAccumulatorǁ__init____mutmut_9'] = _NsAccumulator.xǁ_NsAccumulatorǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁ_NsAccumulatorǁ__init____mutmut['xǁ_NsAccumulatorǁ__init____mutmut_10'] = _NsAccumulator.xǁ_NsAccumulatorǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__aggregate_by_namespace__mutmut)
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


def x__aggregate_by_namespace__mutmut_orig(
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


def x__aggregate_by_namespace__mutmut_1(
    opportunities: list[PodSavingOpportunity],
) -> list[NamespaceSaving]:
    ns_map: dict[str, _NsAccumulator] = None
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


def x__aggregate_by_namespace__mutmut_2(
    opportunities: list[PodSavingOpportunity],
) -> list[NamespaceSaving]:
    ns_map: dict[str, _NsAccumulator] = {}
    for o in opportunities:
        if o.namespace in ns_map:
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


def x__aggregate_by_namespace__mutmut_3(
    opportunities: list[PodSavingOpportunity],
) -> list[NamespaceSaving]:
    ns_map: dict[str, _NsAccumulator] = {}
    for o in opportunities:
        if o.namespace not in ns_map:
            ns_map[o.namespace] = None
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


def x__aggregate_by_namespace__mutmut_4(
    opportunities: list[PodSavingOpportunity],
) -> list[NamespaceSaving]:
    ns_map: dict[str, _NsAccumulator] = {}
    for o in opportunities:
        if o.namespace not in ns_map:
            ns_map[o.namespace] = _NsAccumulator()
        acc = None
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


def x__aggregate_by_namespace__mutmut_5(
    opportunities: list[PodSavingOpportunity],
) -> list[NamespaceSaving]:
    ns_map: dict[str, _NsAccumulator] = {}
    for o in opportunities:
        if o.namespace not in ns_map:
            ns_map[o.namespace] = _NsAccumulator()
        acc = ns_map[o.namespace]
        acc.pod_count = 1
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


def x__aggregate_by_namespace__mutmut_6(
    opportunities: list[PodSavingOpportunity],
) -> list[NamespaceSaving]:
    ns_map: dict[str, _NsAccumulator] = {}
    for o in opportunities:
        if o.namespace not in ns_map:
            ns_map[o.namespace] = _NsAccumulator()
        acc = ns_map[o.namespace]
        acc.pod_count -= 1
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


def x__aggregate_by_namespace__mutmut_7(
    opportunities: list[PodSavingOpportunity],
) -> list[NamespaceSaving]:
    ns_map: dict[str, _NsAccumulator] = {}
    for o in opportunities:
        if o.namespace not in ns_map:
            ns_map[o.namespace] = _NsAccumulator()
        acc = ns_map[o.namespace]
        acc.pod_count += 2
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


def x__aggregate_by_namespace__mutmut_8(
    opportunities: list[PodSavingOpportunity],
) -> list[NamespaceSaving]:
    ns_map: dict[str, _NsAccumulator] = {}
    for o in opportunities:
        if o.namespace not in ns_map:
            ns_map[o.namespace] = _NsAccumulator()
        acc = ns_map[o.namespace]
        acc.pod_count += 1
        acc.delta_cores = o.delta_cores
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


def x__aggregate_by_namespace__mutmut_9(
    opportunities: list[PodSavingOpportunity],
) -> list[NamespaceSaving]:
    ns_map: dict[str, _NsAccumulator] = {}
    for o in opportunities:
        if o.namespace not in ns_map:
            ns_map[o.namespace] = _NsAccumulator()
        acc = ns_map[o.namespace]
        acc.pod_count += 1
        acc.delta_cores -= o.delta_cores
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


def x__aggregate_by_namespace__mutmut_10(
    opportunities: list[PodSavingOpportunity],
) -> list[NamespaceSaving]:
    ns_map: dict[str, _NsAccumulator] = {}
    for o in opportunities:
        if o.namespace not in ns_map:
            ns_map[o.namespace] = _NsAccumulator()
        acc = ns_map[o.namespace]
        acc.pod_count += 1
        acc.delta_cores += o.delta_cores
        acc.delta_mi = o.delta_memory_mi
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


def x__aggregate_by_namespace__mutmut_11(
    opportunities: list[PodSavingOpportunity],
) -> list[NamespaceSaving]:
    ns_map: dict[str, _NsAccumulator] = {}
    for o in opportunities:
        if o.namespace not in ns_map:
            ns_map[o.namespace] = _NsAccumulator()
        acc = ns_map[o.namespace]
        acc.pod_count += 1
        acc.delta_cores += o.delta_cores
        acc.delta_mi -= o.delta_memory_mi
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


def x__aggregate_by_namespace__mutmut_12(
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
        if o.monthly_saving_usd is None:
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


def x__aggregate_by_namespace__mutmut_13(
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
            acc.usd = o.monthly_saving_usd
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


def x__aggregate_by_namespace__mutmut_14(
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
            acc.usd -= o.monthly_saving_usd
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


def x__aggregate_by_namespace__mutmut_15(
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
            acc.has_usd = None

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


def x__aggregate_by_namespace__mutmut_16(
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
            acc.has_usd = False

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


def x__aggregate_by_namespace__mutmut_17(
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
            namespace=None,
            pod_count=acc.pod_count,
            total_delta_cores=round(acc.delta_cores, 3),
            total_delta_memory_mi=round(acc.delta_mi, 1),
            total_monthly_saving_usd=round(acc.usd, 2) if acc.has_usd else None,
        )
        for ns, acc in ns_map.items()
    ]


def x__aggregate_by_namespace__mutmut_18(
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
            pod_count=None,
            total_delta_cores=round(acc.delta_cores, 3),
            total_delta_memory_mi=round(acc.delta_mi, 1),
            total_monthly_saving_usd=round(acc.usd, 2) if acc.has_usd else None,
        )
        for ns, acc in ns_map.items()
    ]


def x__aggregate_by_namespace__mutmut_19(
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
            total_delta_cores=None,
            total_delta_memory_mi=round(acc.delta_mi, 1),
            total_monthly_saving_usd=round(acc.usd, 2) if acc.has_usd else None,
        )
        for ns, acc in ns_map.items()
    ]


def x__aggregate_by_namespace__mutmut_20(
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
            total_delta_memory_mi=None,
            total_monthly_saving_usd=round(acc.usd, 2) if acc.has_usd else None,
        )
        for ns, acc in ns_map.items()
    ]


def x__aggregate_by_namespace__mutmut_21(
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
            total_monthly_saving_usd=None,
        )
        for ns, acc in ns_map.items()
    ]


def x__aggregate_by_namespace__mutmut_22(
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
            pod_count=acc.pod_count,
            total_delta_cores=round(acc.delta_cores, 3),
            total_delta_memory_mi=round(acc.delta_mi, 1),
            total_monthly_saving_usd=round(acc.usd, 2) if acc.has_usd else None,
        )
        for ns, acc in ns_map.items()
    ]


def x__aggregate_by_namespace__mutmut_23(
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
            total_delta_cores=round(acc.delta_cores, 3),
            total_delta_memory_mi=round(acc.delta_mi, 1),
            total_monthly_saving_usd=round(acc.usd, 2) if acc.has_usd else None,
        )
        for ns, acc in ns_map.items()
    ]


def x__aggregate_by_namespace__mutmut_24(
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
            total_delta_memory_mi=round(acc.delta_mi, 1),
            total_monthly_saving_usd=round(acc.usd, 2) if acc.has_usd else None,
        )
        for ns, acc in ns_map.items()
    ]


def x__aggregate_by_namespace__mutmut_25(
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
            total_monthly_saving_usd=round(acc.usd, 2) if acc.has_usd else None,
        )
        for ns, acc in ns_map.items()
    ]


def x__aggregate_by_namespace__mutmut_26(
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
            )
        for ns, acc in ns_map.items()
    ]


def x__aggregate_by_namespace__mutmut_27(
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
            total_delta_cores=round(None, 3),
            total_delta_memory_mi=round(acc.delta_mi, 1),
            total_monthly_saving_usd=round(acc.usd, 2) if acc.has_usd else None,
        )
        for ns, acc in ns_map.items()
    ]


def x__aggregate_by_namespace__mutmut_28(
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
            total_delta_cores=round(acc.delta_cores, None),
            total_delta_memory_mi=round(acc.delta_mi, 1),
            total_monthly_saving_usd=round(acc.usd, 2) if acc.has_usd else None,
        )
        for ns, acc in ns_map.items()
    ]


def x__aggregate_by_namespace__mutmut_29(
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
            total_delta_cores=round(3),
            total_delta_memory_mi=round(acc.delta_mi, 1),
            total_monthly_saving_usd=round(acc.usd, 2) if acc.has_usd else None,
        )
        for ns, acc in ns_map.items()
    ]


def x__aggregate_by_namespace__mutmut_30(
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
            total_delta_cores=round(acc.delta_cores, ),
            total_delta_memory_mi=round(acc.delta_mi, 1),
            total_monthly_saving_usd=round(acc.usd, 2) if acc.has_usd else None,
        )
        for ns, acc in ns_map.items()
    ]


def x__aggregate_by_namespace__mutmut_31(
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
            total_delta_cores=round(acc.delta_cores, 4),
            total_delta_memory_mi=round(acc.delta_mi, 1),
            total_monthly_saving_usd=round(acc.usd, 2) if acc.has_usd else None,
        )
        for ns, acc in ns_map.items()
    ]


def x__aggregate_by_namespace__mutmut_32(
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
            total_delta_memory_mi=round(None, 1),
            total_monthly_saving_usd=round(acc.usd, 2) if acc.has_usd else None,
        )
        for ns, acc in ns_map.items()
    ]


def x__aggregate_by_namespace__mutmut_33(
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
            total_delta_memory_mi=round(acc.delta_mi, None),
            total_monthly_saving_usd=round(acc.usd, 2) if acc.has_usd else None,
        )
        for ns, acc in ns_map.items()
    ]


def x__aggregate_by_namespace__mutmut_34(
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
            total_delta_memory_mi=round(1),
            total_monthly_saving_usd=round(acc.usd, 2) if acc.has_usd else None,
        )
        for ns, acc in ns_map.items()
    ]


def x__aggregate_by_namespace__mutmut_35(
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
            total_delta_memory_mi=round(acc.delta_mi, ),
            total_monthly_saving_usd=round(acc.usd, 2) if acc.has_usd else None,
        )
        for ns, acc in ns_map.items()
    ]


def x__aggregate_by_namespace__mutmut_36(
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
            total_delta_memory_mi=round(acc.delta_mi, 2),
            total_monthly_saving_usd=round(acc.usd, 2) if acc.has_usd else None,
        )
        for ns, acc in ns_map.items()
    ]


def x__aggregate_by_namespace__mutmut_37(
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
            total_monthly_saving_usd=round(None, 2) if acc.has_usd else None,
        )
        for ns, acc in ns_map.items()
    ]


def x__aggregate_by_namespace__mutmut_38(
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
            total_monthly_saving_usd=round(acc.usd, None) if acc.has_usd else None,
        )
        for ns, acc in ns_map.items()
    ]


def x__aggregate_by_namespace__mutmut_39(
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
            total_monthly_saving_usd=round(2) if acc.has_usd else None,
        )
        for ns, acc in ns_map.items()
    ]


def x__aggregate_by_namespace__mutmut_40(
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
            total_monthly_saving_usd=round(acc.usd, ) if acc.has_usd else None,
        )
        for ns, acc in ns_map.items()
    ]


def x__aggregate_by_namespace__mutmut_41(
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
            total_monthly_saving_usd=round(acc.usd, 3) if acc.has_usd else None,
        )
        for ns, acc in ns_map.items()
    ]

mutants_x__aggregate_by_namespace__mutmut['_mutmut_orig'] = x__aggregate_by_namespace__mutmut_orig # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_1'] = x__aggregate_by_namespace__mutmut_1 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_2'] = x__aggregate_by_namespace__mutmut_2 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_3'] = x__aggregate_by_namespace__mutmut_3 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_4'] = x__aggregate_by_namespace__mutmut_4 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_5'] = x__aggregate_by_namespace__mutmut_5 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_6'] = x__aggregate_by_namespace__mutmut_6 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_7'] = x__aggregate_by_namespace__mutmut_7 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_8'] = x__aggregate_by_namespace__mutmut_8 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_9'] = x__aggregate_by_namespace__mutmut_9 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_10'] = x__aggregate_by_namespace__mutmut_10 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_11'] = x__aggregate_by_namespace__mutmut_11 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_12'] = x__aggregate_by_namespace__mutmut_12 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_13'] = x__aggregate_by_namespace__mutmut_13 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_14'] = x__aggregate_by_namespace__mutmut_14 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_15'] = x__aggregate_by_namespace__mutmut_15 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_16'] = x__aggregate_by_namespace__mutmut_16 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_17'] = x__aggregate_by_namespace__mutmut_17 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_18'] = x__aggregate_by_namespace__mutmut_18 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_19'] = x__aggregate_by_namespace__mutmut_19 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_20'] = x__aggregate_by_namespace__mutmut_20 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_21'] = x__aggregate_by_namespace__mutmut_21 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_22'] = x__aggregate_by_namespace__mutmut_22 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_23'] = x__aggregate_by_namespace__mutmut_23 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_24'] = x__aggregate_by_namespace__mutmut_24 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_25'] = x__aggregate_by_namespace__mutmut_25 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_26'] = x__aggregate_by_namespace__mutmut_26 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_27'] = x__aggregate_by_namespace__mutmut_27 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_28'] = x__aggregate_by_namespace__mutmut_28 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_29'] = x__aggregate_by_namespace__mutmut_29 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_30'] = x__aggregate_by_namespace__mutmut_30 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_31'] = x__aggregate_by_namespace__mutmut_31 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_32'] = x__aggregate_by_namespace__mutmut_32 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_33'] = x__aggregate_by_namespace__mutmut_33 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_34'] = x__aggregate_by_namespace__mutmut_34 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_35'] = x__aggregate_by_namespace__mutmut_35 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_36'] = x__aggregate_by_namespace__mutmut_36 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_37'] = x__aggregate_by_namespace__mutmut_37 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_38'] = x__aggregate_by_namespace__mutmut_38 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_39'] = x__aggregate_by_namespace__mutmut_39 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_40'] = x__aggregate_by_namespace__mutmut_40 # type: ignore # mutmut generated
mutants_x__aggregate_by_namespace__mutmut['x__aggregate_by_namespace__mutmut_41'] = x__aggregate_by_namespace__mutmut_41 # type: ignore # mutmut generated
mutants_x__f__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__f__mutmut)
def _f(value: object) -> float | None:
    if value is None:
        return None
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return None


def x__f__mutmut_orig(value: object) -> float | None:
    if value is None:
        return None
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return None


def x__f__mutmut_1(value: object) -> float | None:
    if value is not None:
        return None
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return None


def x__f__mutmut_2(value: object) -> float | None:
    if value is None:
        return None
    try:
        return float(None)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return None

mutants_x__f__mutmut['_mutmut_orig'] = x__f__mutmut_orig # type: ignore # mutmut generated
mutants_x__f__mutmut['x__f__mutmut_1'] = x__f__mutmut_1 # type: ignore # mutmut generated
mutants_x__f__mutmut['x__f__mutmut_2'] = x__f__mutmut_2 # type: ignore # mutmut generated


_SIGNIFICANT_TREND_PCT = 0.10
mutants_x_compute_trend__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_trend__mutmut)
def compute_trend(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "stable"


def x_compute_trend__mutmut_orig(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "stable"


def x_compute_trend__mutmut_1(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None and previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "stable"


def x_compute_trend__mutmut_2(previous: float | None, current: float | None) -> str | None:
    if previous is None and current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "stable"


def x_compute_trend__mutmut_3(previous: float | None, current: float | None) -> str | None:
    if previous is not None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "stable"


def x_compute_trend__mutmut_4(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is not None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "stable"


def x_compute_trend__mutmut_5(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous != 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "stable"


def x_compute_trend__mutmut_6(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 1:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "stable"


def x_compute_trend__mutmut_7(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = None
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "stable"


def x_compute_trend__mutmut_8(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) * previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "stable"


def x_compute_trend__mutmut_9(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current + previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "stable"


def x_compute_trend__mutmut_10(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct >= _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "stable"


def x_compute_trend__mutmut_11(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "XXincreasingXX"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "stable"


def x_compute_trend__mutmut_12(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "INCREASING"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "stable"


def x_compute_trend__mutmut_13(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct <= -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "stable"


def x_compute_trend__mutmut_14(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < +_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "stable"


def x_compute_trend__mutmut_15(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "XXdecreasingXX"
    return "stable"


def x_compute_trend__mutmut_16(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "DECREASING"
    return "stable"


def x_compute_trend__mutmut_17(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "XXstableXX"


def x_compute_trend__mutmut_18(previous: float | None, current: float | None) -> str | None:
    if previous is None or current is None or previous == 0:
        return None
    delta_pct = (current - previous) / previous
    if delta_pct > _SIGNIFICANT_TREND_PCT:
        return "increasing"
    if delta_pct < -_SIGNIFICANT_TREND_PCT:
        return "decreasing"
    return "STABLE"

mutants_x_compute_trend__mutmut['_mutmut_orig'] = x_compute_trend__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_trend__mutmut['x_compute_trend__mutmut_1'] = x_compute_trend__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_trend__mutmut['x_compute_trend__mutmut_2'] = x_compute_trend__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_trend__mutmut['x_compute_trend__mutmut_3'] = x_compute_trend__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_trend__mutmut['x_compute_trend__mutmut_4'] = x_compute_trend__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_trend__mutmut['x_compute_trend__mutmut_5'] = x_compute_trend__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_trend__mutmut['x_compute_trend__mutmut_6'] = x_compute_trend__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_trend__mutmut['x_compute_trend__mutmut_7'] = x_compute_trend__mutmut_7 # type: ignore # mutmut generated
mutants_x_compute_trend__mutmut['x_compute_trend__mutmut_8'] = x_compute_trend__mutmut_8 # type: ignore # mutmut generated
mutants_x_compute_trend__mutmut['x_compute_trend__mutmut_9'] = x_compute_trend__mutmut_9 # type: ignore # mutmut generated
mutants_x_compute_trend__mutmut['x_compute_trend__mutmut_10'] = x_compute_trend__mutmut_10 # type: ignore # mutmut generated
mutants_x_compute_trend__mutmut['x_compute_trend__mutmut_11'] = x_compute_trend__mutmut_11 # type: ignore # mutmut generated
mutants_x_compute_trend__mutmut['x_compute_trend__mutmut_12'] = x_compute_trend__mutmut_12 # type: ignore # mutmut generated
mutants_x_compute_trend__mutmut['x_compute_trend__mutmut_13'] = x_compute_trend__mutmut_13 # type: ignore # mutmut generated
mutants_x_compute_trend__mutmut['x_compute_trend__mutmut_14'] = x_compute_trend__mutmut_14 # type: ignore # mutmut generated
mutants_x_compute_trend__mutmut['x_compute_trend__mutmut_15'] = x_compute_trend__mutmut_15 # type: ignore # mutmut generated
mutants_x_compute_trend__mutmut['x_compute_trend__mutmut_16'] = x_compute_trend__mutmut_16 # type: ignore # mutmut generated
mutants_x_compute_trend__mutmut['x_compute_trend__mutmut_17'] = x_compute_trend__mutmut_17 # type: ignore # mutmut generated
mutants_x_compute_trend__mutmut['x_compute_trend__mutmut_18'] = x_compute_trend__mutmut_18 # type: ignore # mutmut generated
