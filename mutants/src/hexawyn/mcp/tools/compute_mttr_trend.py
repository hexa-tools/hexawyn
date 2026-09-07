"""MCP tool: compute_mttr_trend — MTTR trend over last 3 months."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.workloads.compute_mttr_trend.command import (
    ComputeMTTRTrendCommand,
)
from hexawyn.application.use_case.workloads.compute_mttr_trend.compute_mttr_trend_use_case import (
    ComputeMTTRTrendUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_compute_mttr_trend__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_mttr_trend__mutmut)
def compute_mttr_trend(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_orig(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_1(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = None
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_2(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = None
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_3(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=None)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_4(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = None
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_5(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(None)
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_6(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=None))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_7(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months and []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_8(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = None
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_9(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "XXtrendXX": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_10(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "TREND": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_11(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "XXrecommendationXX": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_12(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "RECOMMENDATION": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_13(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "XXper_monthXX": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_14(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "PER_MONTH": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_15(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "XXmttr_minutesXX": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_16(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "MTTR_MINUTES": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_17(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "XXcountXX": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_18(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "COUNT": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_19(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "XXdowntime_totalXX": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_20(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "DOWNTIME_TOTAL": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_21(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "XXslowest_incidentsXX": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_22(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "SLOWEST_INCIDENTS": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_23(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "XXincident_idXX": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_24(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "INCIDENT_ID": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_25(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "XXservice_nameXX": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_26(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "SERVICE_NAME": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_27(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "XXseverityXX": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_28(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "SEVERITY": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_29(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "XXdowntime_minutesXX": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_30(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "DOWNTIME_MINUTES": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_31(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "XXerrorXX": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_32(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "ERROR": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_33(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "XXtrendXX": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_34(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "TREND": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_35(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "XXerrorXX",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_36(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "ERROR",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_37(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "XXrecommendationXX": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_38(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "RECOMMENDATION": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_39(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "XXXX",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_40(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "XXper_monthXX": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_41(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "PER_MONTH": {},
            "slowest_incidents": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_42(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "XXslowest_incidentsXX": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_43(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "SLOWEST_INCIDENTS": [],
            "error": str(exc),
        }


def x_compute_mttr_trend__mutmut_44(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "XXerrorXX": str(exc),
        }


def x_compute_mttr_trend__mutmut_45(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "ERROR": str(exc),
        }


def x_compute_mttr_trend__mutmut_46(months: list[str] | None = None) -> dict[str, object]:
    """Track Mean Time To Recovery (MTTR) trend over the last 3 months.

    Returns MTTR per month broken down by severity (P1/P2/P3),
    trend indicator (improving/degrading/stable), top 3 slowest incidents,
    and benchark comparison against industry standards.

    Args:
        months: List of months in YYYY-MM format. Defaults to last 3 months.
    """
    from hexawyn.mcp.server import build_mttr_trend_adapter

    try:
        adapter = build_mttr_trend_adapter()
        use_case = ComputeMTTRTrendUseCase(mttr_port=adapter)
        response = use_case.execute(ComputeMTTRTrendCommand(months=months or []))
        r = response.result
        return {
            "trend": r.trend,
            "recommendation": r.recommendation,
            "per_month": {
                m: {
                    sev: {
                        "mttr_minutes": s.mttr_minutes,
                        "count": s.count,
                        "downtime_total": s.downtime_total,
                    }
                    for sev, s in data.items()
                }
                for m, data in r.per_month.items()
            },
            "slowest_incidents": [
                {
                    "incident_id": i.incident_id,
                    "service_name": i.service_name,
                    "severity": i.severity,
                    "downtime_minutes": i.downtime_minutes,
                }
                for i in r.slowest_incidents
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "trend": "error",
            "recommendation": "",
            "per_month": {},
            "slowest_incidents": [],
            "error": str(None),
        }

mutants_x_compute_mttr_trend__mutmut['_mutmut_orig'] = x_compute_mttr_trend__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_1'] = x_compute_mttr_trend__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_2'] = x_compute_mttr_trend__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_3'] = x_compute_mttr_trend__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_4'] = x_compute_mttr_trend__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_5'] = x_compute_mttr_trend__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_6'] = x_compute_mttr_trend__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_7'] = x_compute_mttr_trend__mutmut_7 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_8'] = x_compute_mttr_trend__mutmut_8 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_9'] = x_compute_mttr_trend__mutmut_9 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_10'] = x_compute_mttr_trend__mutmut_10 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_11'] = x_compute_mttr_trend__mutmut_11 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_12'] = x_compute_mttr_trend__mutmut_12 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_13'] = x_compute_mttr_trend__mutmut_13 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_14'] = x_compute_mttr_trend__mutmut_14 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_15'] = x_compute_mttr_trend__mutmut_15 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_16'] = x_compute_mttr_trend__mutmut_16 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_17'] = x_compute_mttr_trend__mutmut_17 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_18'] = x_compute_mttr_trend__mutmut_18 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_19'] = x_compute_mttr_trend__mutmut_19 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_20'] = x_compute_mttr_trend__mutmut_20 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_21'] = x_compute_mttr_trend__mutmut_21 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_22'] = x_compute_mttr_trend__mutmut_22 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_23'] = x_compute_mttr_trend__mutmut_23 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_24'] = x_compute_mttr_trend__mutmut_24 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_25'] = x_compute_mttr_trend__mutmut_25 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_26'] = x_compute_mttr_trend__mutmut_26 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_27'] = x_compute_mttr_trend__mutmut_27 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_28'] = x_compute_mttr_trend__mutmut_28 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_29'] = x_compute_mttr_trend__mutmut_29 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_30'] = x_compute_mttr_trend__mutmut_30 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_31'] = x_compute_mttr_trend__mutmut_31 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_32'] = x_compute_mttr_trend__mutmut_32 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_33'] = x_compute_mttr_trend__mutmut_33 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_34'] = x_compute_mttr_trend__mutmut_34 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_35'] = x_compute_mttr_trend__mutmut_35 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_36'] = x_compute_mttr_trend__mutmut_36 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_37'] = x_compute_mttr_trend__mutmut_37 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_38'] = x_compute_mttr_trend__mutmut_38 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_39'] = x_compute_mttr_trend__mutmut_39 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_40'] = x_compute_mttr_trend__mutmut_40 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_41'] = x_compute_mttr_trend__mutmut_41 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_42'] = x_compute_mttr_trend__mutmut_42 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_43'] = x_compute_mttr_trend__mutmut_43 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_44'] = x_compute_mttr_trend__mutmut_44 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_45'] = x_compute_mttr_trend__mutmut_45 # type: ignore # mutmut generated
mutants_x_compute_mttr_trend__mutmut['x_compute_mttr_trend__mutmut_46'] = x_compute_mttr_trend__mutmut_46 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(compute_mttr_trend)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(compute_mttr_trend)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
