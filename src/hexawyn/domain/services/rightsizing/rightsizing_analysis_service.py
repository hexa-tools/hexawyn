from __future__ import annotations

from hexawyn.domain.models.rightsizing import (
    RightsizingRecommendation,
    RightsizingReport,
    RightsizingType,
)

# Detection thresholds (from ticket)
_OVER_CPU_THRESHOLD = 0.30
_OVER_RAM_THRESHOLD = 0.40
_UNDER_RAM_THRESHOLD = 0.85
_MINIMUM_SAVINGS_USD = 5.0

# Headroom added to recommendations
_OVER_HEADROOM = 1.3
_UNDER_HEADROOM = 2.0
_MIN_CPU_CORES = 0.1
_MIN_MEMORY_MI = 128.0

# Cloud pricing constants (USD — generic on-demand)
_CPU_COST_PER_CORE_MONTH = 21.6  # ~$0.030/vCPU-hour × 720h
_MEM_COST_PER_GIB_MONTH = 2.88  # ~$0.004/GiB-hour × 720h

# Priority thresholds (absolute USD savings per month)
_PRIORITY_HIGH_USD = 50.0
_PRIORITY_MEDIUM_USD = 20.0


class RightsizingAnalysisService:
    """Pure domain service — no infra deps, no try/catch."""

    def analyze(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped += 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(recommendations, key=lambda r: r.monthly_savings_usd, reverse=True)[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 0)

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=skipped,
            total_monthly_savings_usd=total_savings,
        )


def _analyze_workload(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def _classify(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def _recommend_cpu(cpu_req: float, cpu_actual: float | None) -> float:
    """Only reduce CPU if it is genuinely over-provisioned."""
    if cpu_actual is not None and cpu_req > 0 and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD:
        return max(cpu_actual * _OVER_HEADROOM, _MIN_CPU_CORES)
    return cpu_req


def _recommend_memory(
    rtype: RightsizingType,
    mem_req: float,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return mem_req * _UNDER_HEADROOM
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req < _OVER_RAM_THRESHOLD:
        return max(mem_actual * _OVER_HEADROOM, _MIN_MEMORY_MI)
    return mem_req


def _compute_savings(
    cpu_req: float,
    rec_cpu: float,
    mem_req: float,
    rec_mem: float,
) -> float:
    cpu_saved = (cpu_req - rec_cpu) * _CPU_COST_PER_CORE_MONTH
    mem_saved_gib = (mem_req - rec_mem) / 1024.0
    mem_saved = mem_saved_gib * _MEM_COST_PER_GIB_MONTH
    return round(cpu_saved + mem_saved, 2)


def _waste_percentage(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.OVER_PROVISIONED:
        cpu_waste = (
            (1.0 - cpu_actual / cpu_req) * 100.0 if cpu_req > 0 and cpu_actual is not None else 0.0
        )
        mem_waste = (
            (1.0 - mem_actual / mem_req) * 100.0 if mem_req > 0 and mem_actual is not None else 0.0
        )
        return round(max(cpu_waste, mem_waste), 1)
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return round(
            mem_actual / mem_req * 100.0 if mem_req > 0 and mem_actual is not None else 0.0, 1
        )
    return 0.0


def _priority(savings: float) -> str:
    amount = abs(savings)
    if amount > _PRIORITY_HIGH_USD:
        return "high"
    if amount > _PRIORITY_MEDIUM_USD:
        return "medium"
    return "low"


def _as_float_or_none(value: object) -> float | None:
    if value is None:
        return None
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return None
