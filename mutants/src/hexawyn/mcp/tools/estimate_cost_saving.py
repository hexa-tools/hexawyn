"""MCP tool: estimate_cost_saving — FinOps pod-level right-sizing cost savings."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.finops.estimate_cost_saving.command import (
    EstimateCostSavingCommand,
)
from hexawyn.application.use_case.finops.estimate_cost_saving.estimate_cost_saving_use_case import (
    EstimateCostSavingUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_estimate_cost_saving__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_estimate_cost_saving__mutmut)
def estimate_cost_saving(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_orig(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_1(
    top_n: int = 11,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_2(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = None
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_3(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = None  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_4(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=None)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_5(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = None
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_6(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            None
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_7(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=None,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_8(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=None,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_9(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=None,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_10(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_11(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_12(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_13(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = None
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_14(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "XXtop_opportunitiesXX": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_15(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "TOP_OPPORTUNITIES": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_16(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "XXpodXX": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_17(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "POD": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_18(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "XXnamespaceXX": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_19(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "NAMESPACE": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_20(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "XXcurrent_cpu_requestXX": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_21(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "CURRENT_CPU_REQUEST": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_22(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "XXrecommended_cpu_requestXX": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_23(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "RECOMMENDED_CPU_REQUEST": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_24(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(None, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_25(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, None)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_26(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_27(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, )
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_28(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 4)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_29(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_30(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "XXcurrent_memory_request_miXX": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_31(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "CURRENT_MEMORY_REQUEST_MI": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_32(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "XXrecommended_memory_request_miXX": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_33(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "RECOMMENDED_MEMORY_REQUEST_MI": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_34(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(None, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_35(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, None)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_36(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_37(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, )
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_38(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 2)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_39(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_40(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "XXdelta_coresXX": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_41(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "DELTA_CORES": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_42(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(None, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_43(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, None),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_44(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_45(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, ),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_46(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 4),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_47(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "XXdelta_memory_miXX": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_48(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "DELTA_MEMORY_MI": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_49(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(None, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_50(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, None),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_51(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_52(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, ),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_53(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 2),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_54(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "XXmonthly_saving_usdXX": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_55(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "MONTHLY_SAVING_USD": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_56(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(None, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_57(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, None) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_58(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_59(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, ) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_60(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 3) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_61(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_62(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "XXhpa_enabledXX": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_63(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "HPA_ENABLED": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_64(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "XXis_burstyXX": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_65(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "IS_BURSTY": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_66(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "XXcaveatsXX": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_67(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "CAVEATS": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_68(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "XXnamespace_savingsXX": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_69(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "NAMESPACE_SAVINGS": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_70(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "XXnamespaceXX": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_71(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "NAMESPACE": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_72(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "XXpod_countXX": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_73(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "POD_COUNT": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_74(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "XXtotal_delta_coresXX": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_75(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "TOTAL_DELTA_CORES": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_76(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(None, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_77(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, None),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_78(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_79(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, ),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_80(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 4),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_81(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "XXtotal_delta_memory_miXX": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_82(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "TOTAL_DELTA_MEMORY_MI": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_83(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(None, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_84(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, None),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_85(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_86(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, ),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_87(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 2),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_88(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "XXtotal_monthly_saving_usdXX": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_89(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "TOTAL_MONTHLY_SAVING_USD": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_90(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(None, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_91(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, None)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_92(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_93(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, )
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_94(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 3)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_95(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_96(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "XXtotal_monthly_saving_usdXX": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_97(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "TOTAL_MONTHLY_SAVING_USD": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_98(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(None, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_99(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, None)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_100(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_101(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, )
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_102(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 3)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_103(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_104(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "XXtotal_delta_coresXX": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_105(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "TOTAL_DELTA_CORES": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_106(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(None, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_107(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, None),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_108(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_109(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, ),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_110(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 4),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_111(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "XXtotal_delta_memory_miXX": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_112(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "TOTAL_DELTA_MEMORY_MI": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_113(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(None, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_114(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, None),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_115(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_116(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, ),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_117(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 2),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_118(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "XXpods_analyzedXX": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_119(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "PODS_ANALYZED": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_120(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "XXpods_excludedXX": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_121(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "PODS_EXCLUDED": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_122(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "XXpricing_configuredXX": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_123(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "PRICING_CONFIGURED": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_124(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "XXprevious_total_saving_usdXX": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_125(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "PREVIOUS_TOTAL_SAVING_USD": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_126(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "XXsaving_trendXX": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_127(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "SAVING_TREND": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_128(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "XXerrorXX": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_129(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "ERROR": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_130(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "XXtop_opportunitiesXX": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_131(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "TOP_OPPORTUNITIES": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_132(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "XXnamespace_savingsXX": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_133(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "NAMESPACE_SAVINGS": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_134(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "XXtotal_monthly_saving_usdXX": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_135(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "TOTAL_MONTHLY_SAVING_USD": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_136(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "XXtotal_delta_coresXX": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_137(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "TOTAL_DELTA_CORES": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_138(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 1.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_139(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "XXtotal_delta_memory_miXX": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_140(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "TOTAL_DELTA_MEMORY_MI": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_141(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 1.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_142(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "XXpods_analyzedXX": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_143(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "PODS_ANALYZED": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_144(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 1,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_145(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "XXpods_excludedXX": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_146(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "PODS_EXCLUDED": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_147(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 1,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_148(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "XXpricing_configuredXX": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_149(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "PRICING_CONFIGURED": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_150(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": True,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_151(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "XXprevious_total_saving_usdXX": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_152(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "PREVIOUS_TOTAL_SAVING_USD": None,
            "saving_trend": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_153(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "XXsaving_trendXX": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_154(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "SAVING_TREND": None,
            "error": str(exc),
        }


def x_estimate_cost_saving__mutmut_155(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "XXerrorXX": str(exc),
        }


def x_estimate_cost_saving__mutmut_156(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "ERROR": str(exc),
        }


def x_estimate_cost_saving__mutmut_157(
    top_n: int = 10,
    cpu_per_core_per_hour_usd: float | None = None,
    memory_per_gb_per_hour_usd: float | None = None,
) -> dict[str, object]:
    """Estimate cloud cost savings from right-sizing over-provisioned pods to p95 actual usage.

    Args:
        top_n: Maximum saving opportunities to return, ranked by monthly savings (default: 10).
        cpu_per_core_per_hour_usd: CPU pricing in $/core/hour (e.g. 0.05). Omit for cores-only report.
        memory_per_gb_per_hour_usd: Memory pricing in $/GB/hour (e.g. 0.007). Omit for GB-only report.
    """  # noqa: E501
    from hexawyn.mcp.server import build_cost_saving_adapter

    try:
        adapter = build_cost_saving_adapter()
        use_case = EstimateCostSavingUseCase(port=adapter)  # type: ignore
        response = use_case.execute(  # type: ignore
            EstimateCostSavingCommand(
                top_n=top_n,
                cpu_per_core_per_hour_usd=cpu_per_core_per_hour_usd,
                memory_per_gb_per_hour_usd=memory_per_gb_per_hour_usd,
            )
        )
        report = response.report
        return {
            "top_opportunities": [
                {
                    "pod": o.pod_name,
                    "namespace": o.namespace,
                    "current_cpu_request": o.current_cpu_request,
                    "recommended_cpu_request": (
                        round(o.recommended_cpu_request, 3)
                        if o.recommended_cpu_request is not None
                        else None
                    ),
                    "current_memory_request_mi": o.current_memory_request_mi,
                    "recommended_memory_request_mi": (
                        round(o.recommended_memory_request_mi, 1)
                        if o.recommended_memory_request_mi is not None
                        else None
                    ),
                    "delta_cores": round(o.delta_cores, 3),
                    "delta_memory_mi": round(o.delta_memory_mi, 1),
                    "monthly_saving_usd": (
                        round(o.monthly_saving_usd, 2) if o.monthly_saving_usd is not None else None
                    ),
                    "hpa_enabled": o.hpa_enabled,
                    "is_bursty": o.is_bursty,
                    "caveats": o.caveats,
                }
                for o in report.top_opportunities
            ],
            "namespace_savings": [
                {
                    "namespace": ns.namespace,
                    "pod_count": ns.pod_count,
                    "total_delta_cores": round(ns.total_delta_cores, 3),
                    "total_delta_memory_mi": round(ns.total_delta_memory_mi, 1),
                    "total_monthly_saving_usd": (
                        round(ns.total_monthly_saving_usd, 2)
                        if ns.total_monthly_saving_usd is not None
                        else None
                    ),
                }
                for ns in report.namespace_savings
            ],
            "total_monthly_saving_usd": (
                round(report.total_monthly_saving_usd, 2)
                if report.total_monthly_saving_usd is not None
                else None
            ),
            "total_delta_cores": round(report.total_delta_cores, 3),
            "total_delta_memory_mi": round(report.total_delta_memory_mi, 1),
            "pods_analyzed": report.pods_analyzed,
            "pods_excluded": report.pods_excluded,
            "pricing_configured": report.pricing_configured,
            "previous_total_saving_usd": response.previous_total_saving_usd,
            "saving_trend": response.saving_trend,
            "error": None,
        }
    except Exception as exc:
        return {
            "top_opportunities": [],
            "namespace_savings": [],
            "total_monthly_saving_usd": None,
            "total_delta_cores": 0.0,
            "total_delta_memory_mi": 0.0,
            "pods_analyzed": 0,
            "pods_excluded": 0,
            "pricing_configured": False,
            "previous_total_saving_usd": None,
            "saving_trend": None,
            "error": str(None),
        }

mutants_x_estimate_cost_saving__mutmut['_mutmut_orig'] = x_estimate_cost_saving__mutmut_orig # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_1'] = x_estimate_cost_saving__mutmut_1 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_2'] = x_estimate_cost_saving__mutmut_2 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_3'] = x_estimate_cost_saving__mutmut_3 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_4'] = x_estimate_cost_saving__mutmut_4 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_5'] = x_estimate_cost_saving__mutmut_5 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_6'] = x_estimate_cost_saving__mutmut_6 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_7'] = x_estimate_cost_saving__mutmut_7 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_8'] = x_estimate_cost_saving__mutmut_8 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_9'] = x_estimate_cost_saving__mutmut_9 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_10'] = x_estimate_cost_saving__mutmut_10 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_11'] = x_estimate_cost_saving__mutmut_11 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_12'] = x_estimate_cost_saving__mutmut_12 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_13'] = x_estimate_cost_saving__mutmut_13 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_14'] = x_estimate_cost_saving__mutmut_14 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_15'] = x_estimate_cost_saving__mutmut_15 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_16'] = x_estimate_cost_saving__mutmut_16 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_17'] = x_estimate_cost_saving__mutmut_17 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_18'] = x_estimate_cost_saving__mutmut_18 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_19'] = x_estimate_cost_saving__mutmut_19 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_20'] = x_estimate_cost_saving__mutmut_20 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_21'] = x_estimate_cost_saving__mutmut_21 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_22'] = x_estimate_cost_saving__mutmut_22 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_23'] = x_estimate_cost_saving__mutmut_23 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_24'] = x_estimate_cost_saving__mutmut_24 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_25'] = x_estimate_cost_saving__mutmut_25 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_26'] = x_estimate_cost_saving__mutmut_26 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_27'] = x_estimate_cost_saving__mutmut_27 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_28'] = x_estimate_cost_saving__mutmut_28 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_29'] = x_estimate_cost_saving__mutmut_29 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_30'] = x_estimate_cost_saving__mutmut_30 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_31'] = x_estimate_cost_saving__mutmut_31 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_32'] = x_estimate_cost_saving__mutmut_32 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_33'] = x_estimate_cost_saving__mutmut_33 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_34'] = x_estimate_cost_saving__mutmut_34 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_35'] = x_estimate_cost_saving__mutmut_35 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_36'] = x_estimate_cost_saving__mutmut_36 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_37'] = x_estimate_cost_saving__mutmut_37 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_38'] = x_estimate_cost_saving__mutmut_38 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_39'] = x_estimate_cost_saving__mutmut_39 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_40'] = x_estimate_cost_saving__mutmut_40 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_41'] = x_estimate_cost_saving__mutmut_41 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_42'] = x_estimate_cost_saving__mutmut_42 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_43'] = x_estimate_cost_saving__mutmut_43 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_44'] = x_estimate_cost_saving__mutmut_44 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_45'] = x_estimate_cost_saving__mutmut_45 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_46'] = x_estimate_cost_saving__mutmut_46 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_47'] = x_estimate_cost_saving__mutmut_47 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_48'] = x_estimate_cost_saving__mutmut_48 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_49'] = x_estimate_cost_saving__mutmut_49 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_50'] = x_estimate_cost_saving__mutmut_50 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_51'] = x_estimate_cost_saving__mutmut_51 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_52'] = x_estimate_cost_saving__mutmut_52 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_53'] = x_estimate_cost_saving__mutmut_53 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_54'] = x_estimate_cost_saving__mutmut_54 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_55'] = x_estimate_cost_saving__mutmut_55 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_56'] = x_estimate_cost_saving__mutmut_56 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_57'] = x_estimate_cost_saving__mutmut_57 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_58'] = x_estimate_cost_saving__mutmut_58 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_59'] = x_estimate_cost_saving__mutmut_59 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_60'] = x_estimate_cost_saving__mutmut_60 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_61'] = x_estimate_cost_saving__mutmut_61 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_62'] = x_estimate_cost_saving__mutmut_62 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_63'] = x_estimate_cost_saving__mutmut_63 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_64'] = x_estimate_cost_saving__mutmut_64 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_65'] = x_estimate_cost_saving__mutmut_65 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_66'] = x_estimate_cost_saving__mutmut_66 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_67'] = x_estimate_cost_saving__mutmut_67 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_68'] = x_estimate_cost_saving__mutmut_68 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_69'] = x_estimate_cost_saving__mutmut_69 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_70'] = x_estimate_cost_saving__mutmut_70 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_71'] = x_estimate_cost_saving__mutmut_71 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_72'] = x_estimate_cost_saving__mutmut_72 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_73'] = x_estimate_cost_saving__mutmut_73 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_74'] = x_estimate_cost_saving__mutmut_74 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_75'] = x_estimate_cost_saving__mutmut_75 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_76'] = x_estimate_cost_saving__mutmut_76 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_77'] = x_estimate_cost_saving__mutmut_77 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_78'] = x_estimate_cost_saving__mutmut_78 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_79'] = x_estimate_cost_saving__mutmut_79 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_80'] = x_estimate_cost_saving__mutmut_80 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_81'] = x_estimate_cost_saving__mutmut_81 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_82'] = x_estimate_cost_saving__mutmut_82 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_83'] = x_estimate_cost_saving__mutmut_83 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_84'] = x_estimate_cost_saving__mutmut_84 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_85'] = x_estimate_cost_saving__mutmut_85 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_86'] = x_estimate_cost_saving__mutmut_86 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_87'] = x_estimate_cost_saving__mutmut_87 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_88'] = x_estimate_cost_saving__mutmut_88 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_89'] = x_estimate_cost_saving__mutmut_89 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_90'] = x_estimate_cost_saving__mutmut_90 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_91'] = x_estimate_cost_saving__mutmut_91 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_92'] = x_estimate_cost_saving__mutmut_92 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_93'] = x_estimate_cost_saving__mutmut_93 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_94'] = x_estimate_cost_saving__mutmut_94 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_95'] = x_estimate_cost_saving__mutmut_95 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_96'] = x_estimate_cost_saving__mutmut_96 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_97'] = x_estimate_cost_saving__mutmut_97 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_98'] = x_estimate_cost_saving__mutmut_98 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_99'] = x_estimate_cost_saving__mutmut_99 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_100'] = x_estimate_cost_saving__mutmut_100 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_101'] = x_estimate_cost_saving__mutmut_101 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_102'] = x_estimate_cost_saving__mutmut_102 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_103'] = x_estimate_cost_saving__mutmut_103 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_104'] = x_estimate_cost_saving__mutmut_104 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_105'] = x_estimate_cost_saving__mutmut_105 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_106'] = x_estimate_cost_saving__mutmut_106 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_107'] = x_estimate_cost_saving__mutmut_107 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_108'] = x_estimate_cost_saving__mutmut_108 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_109'] = x_estimate_cost_saving__mutmut_109 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_110'] = x_estimate_cost_saving__mutmut_110 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_111'] = x_estimate_cost_saving__mutmut_111 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_112'] = x_estimate_cost_saving__mutmut_112 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_113'] = x_estimate_cost_saving__mutmut_113 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_114'] = x_estimate_cost_saving__mutmut_114 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_115'] = x_estimate_cost_saving__mutmut_115 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_116'] = x_estimate_cost_saving__mutmut_116 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_117'] = x_estimate_cost_saving__mutmut_117 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_118'] = x_estimate_cost_saving__mutmut_118 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_119'] = x_estimate_cost_saving__mutmut_119 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_120'] = x_estimate_cost_saving__mutmut_120 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_121'] = x_estimate_cost_saving__mutmut_121 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_122'] = x_estimate_cost_saving__mutmut_122 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_123'] = x_estimate_cost_saving__mutmut_123 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_124'] = x_estimate_cost_saving__mutmut_124 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_125'] = x_estimate_cost_saving__mutmut_125 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_126'] = x_estimate_cost_saving__mutmut_126 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_127'] = x_estimate_cost_saving__mutmut_127 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_128'] = x_estimate_cost_saving__mutmut_128 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_129'] = x_estimate_cost_saving__mutmut_129 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_130'] = x_estimate_cost_saving__mutmut_130 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_131'] = x_estimate_cost_saving__mutmut_131 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_132'] = x_estimate_cost_saving__mutmut_132 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_133'] = x_estimate_cost_saving__mutmut_133 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_134'] = x_estimate_cost_saving__mutmut_134 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_135'] = x_estimate_cost_saving__mutmut_135 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_136'] = x_estimate_cost_saving__mutmut_136 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_137'] = x_estimate_cost_saving__mutmut_137 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_138'] = x_estimate_cost_saving__mutmut_138 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_139'] = x_estimate_cost_saving__mutmut_139 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_140'] = x_estimate_cost_saving__mutmut_140 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_141'] = x_estimate_cost_saving__mutmut_141 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_142'] = x_estimate_cost_saving__mutmut_142 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_143'] = x_estimate_cost_saving__mutmut_143 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_144'] = x_estimate_cost_saving__mutmut_144 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_145'] = x_estimate_cost_saving__mutmut_145 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_146'] = x_estimate_cost_saving__mutmut_146 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_147'] = x_estimate_cost_saving__mutmut_147 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_148'] = x_estimate_cost_saving__mutmut_148 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_149'] = x_estimate_cost_saving__mutmut_149 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_150'] = x_estimate_cost_saving__mutmut_150 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_151'] = x_estimate_cost_saving__mutmut_151 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_152'] = x_estimate_cost_saving__mutmut_152 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_153'] = x_estimate_cost_saving__mutmut_153 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_154'] = x_estimate_cost_saving__mutmut_154 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_155'] = x_estimate_cost_saving__mutmut_155 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_156'] = x_estimate_cost_saving__mutmut_156 # type: ignore # mutmut generated
mutants_x_estimate_cost_saving__mutmut['x_estimate_cost_saving__mutmut_157'] = x_estimate_cost_saving__mutmut_157 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(estimate_cost_saving)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(estimate_cost_saving)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
