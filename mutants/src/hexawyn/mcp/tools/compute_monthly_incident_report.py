"""MCP tool: compute_monthly_incident_report — monthly incident summary report."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.finops.compute_monthly_incident_report.command import (
    ComputeMonthlyIncidentReportCommand,
)
from hexawyn.application.use_case.finops.compute_monthly_incident_report.compute_monthly_incident_report_use_case import (  # noqa: E501
    ComputeMonthlyIncidentReportUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_compute_monthly_incident_report__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_monthly_incident_report__mutmut)
def compute_monthly_incident_report(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_orig(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_1(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = None
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_2(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = None  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_3(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=None)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_4(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = None
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_5(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(None)
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_6(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=None))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_7(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = None
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_8(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "XXmonthXX": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_9(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "MONTH": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_10(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "XXtotal_countXX": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_11(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "TOTAL_COUNT": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_12(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "XXtotal_downtime_minutesXX": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_13(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "TOTAL_DOWNTIME_MINUTES": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_14(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "XXper_severityXX": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_15(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "PER_SEVERITY": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_16(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "XXcountXX": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_17(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "COUNT": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_18(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "XXdowntime_minutesXX": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_19(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "DOWNTIME_MINUTES": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_20(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "XXmost_impacted_servicesXX": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_21(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "MOST_IMPACTED_SERVICES": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_22(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "XXservice_nameXX": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_23(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "SERVICE_NAME": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_24(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "XXtotal_downtimeXX": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_25(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "TOTAL_DOWNTIME": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_26(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "XXincident_countXX": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_27(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "INCIDENT_COUNT": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_28(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "XXprevious_month_total_countXX": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_29(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "PREVIOUS_MONTH_TOTAL_COUNT": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_30(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "XXprevious_month_downtime_minutesXX": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_31(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "PREVIOUS_MONTH_DOWNTIME_MINUTES": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_32(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "XXincidents_decreasingXX": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_33(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "INCIDENTS_DECREASING": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_34(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "XXerrorXX": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_35(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "ERROR": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_36(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "XXmonthXX": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_37(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "MONTH": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_38(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month and "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_39(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "XXXX",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_40(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "XXtotal_countXX": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_41(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "TOTAL_COUNT": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_42(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 1,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_43(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "XXtotal_downtime_minutesXX": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_44(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "TOTAL_DOWNTIME_MINUTES": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_45(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 1,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_46(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "XXper_severityXX": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_47(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "PER_SEVERITY": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_48(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "XXmost_impacted_servicesXX": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_49(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "MOST_IMPACTED_SERVICES": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_50(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "XXprevious_month_total_countXX": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_51(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "PREVIOUS_MONTH_TOTAL_COUNT": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_52(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 1,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_53(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "XXprevious_month_downtime_minutesXX": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_54(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "PREVIOUS_MONTH_DOWNTIME_MINUTES": 0,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_55(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 1,
            "incidents_decreasing": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_56(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "XXincidents_decreasingXX": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_57(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "INCIDENTS_DECREASING": False,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_58(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": True,
            "error": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_59(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "XXerrorXX": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_60(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "ERROR": str(exc),
        }


def x_compute_monthly_incident_report__mutmut_61(month: str | None = None) -> dict[str, object]:
    """Monthly incident report: count, downtime, severity breakdown, most impacted services.

    Returns total incident count and downtime broken down by severity (P1/P2/P3),
    most impacted services ranked by downtime, and month-over-month comparison.

    Args:
        month: Month in YYYY-MM format. Defaults to current month.
    """
    from hexawyn.mcp.server import build_monthly_incident_adapter

    try:
        adapter = build_monthly_incident_adapter()
        use_case = ComputeMonthlyIncidentReportUseCase(port=adapter)  # type: ignore
        response = use_case.execute(ComputeMonthlyIncidentReportCommand(month=month))
        r = response.result
        return {
            "month": r.month,
            "total_count": r.total_count,
            "total_downtime_minutes": r.total_downtime_minutes,
            "per_severity": {
                sev: {
                    "count": b.count,
                    "downtime_minutes": b.downtime_minutes,
                }
                for sev, b in r.per_severity.items()
            },
            "most_impacted_services": [
                {
                    "service_name": svc.service_name,
                    "total_downtime": svc.total_downtime,
                    "incident_count": svc.incident_count,
                }
                for svc in r.most_impacted_services
            ],
            "previous_month_total_count": r.previous_month_total_count,
            "previous_month_downtime_minutes": r.previous_month_downtime_minutes,
            "incidents_decreasing": r.incidents_decreasing,
            "error": None,
        }
    except Exception as exc:
        return {
            "month": month or "",
            "total_count": 0,
            "total_downtime_minutes": 0,
            "per_severity": {},
            "most_impacted_services": [],
            "previous_month_total_count": 0,
            "previous_month_downtime_minutes": 0,
            "incidents_decreasing": False,
            "error": str(None),
        }

mutants_x_compute_monthly_incident_report__mutmut['_mutmut_orig'] = x_compute_monthly_incident_report__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_1'] = x_compute_monthly_incident_report__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_2'] = x_compute_monthly_incident_report__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_3'] = x_compute_monthly_incident_report__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_4'] = x_compute_monthly_incident_report__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_5'] = x_compute_monthly_incident_report__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_6'] = x_compute_monthly_incident_report__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_7'] = x_compute_monthly_incident_report__mutmut_7 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_8'] = x_compute_monthly_incident_report__mutmut_8 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_9'] = x_compute_monthly_incident_report__mutmut_9 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_10'] = x_compute_monthly_incident_report__mutmut_10 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_11'] = x_compute_monthly_incident_report__mutmut_11 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_12'] = x_compute_monthly_incident_report__mutmut_12 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_13'] = x_compute_monthly_incident_report__mutmut_13 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_14'] = x_compute_monthly_incident_report__mutmut_14 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_15'] = x_compute_monthly_incident_report__mutmut_15 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_16'] = x_compute_monthly_incident_report__mutmut_16 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_17'] = x_compute_monthly_incident_report__mutmut_17 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_18'] = x_compute_monthly_incident_report__mutmut_18 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_19'] = x_compute_monthly_incident_report__mutmut_19 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_20'] = x_compute_monthly_incident_report__mutmut_20 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_21'] = x_compute_monthly_incident_report__mutmut_21 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_22'] = x_compute_monthly_incident_report__mutmut_22 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_23'] = x_compute_monthly_incident_report__mutmut_23 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_24'] = x_compute_monthly_incident_report__mutmut_24 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_25'] = x_compute_monthly_incident_report__mutmut_25 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_26'] = x_compute_monthly_incident_report__mutmut_26 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_27'] = x_compute_monthly_incident_report__mutmut_27 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_28'] = x_compute_monthly_incident_report__mutmut_28 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_29'] = x_compute_monthly_incident_report__mutmut_29 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_30'] = x_compute_monthly_incident_report__mutmut_30 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_31'] = x_compute_monthly_incident_report__mutmut_31 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_32'] = x_compute_monthly_incident_report__mutmut_32 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_33'] = x_compute_monthly_incident_report__mutmut_33 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_34'] = x_compute_monthly_incident_report__mutmut_34 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_35'] = x_compute_monthly_incident_report__mutmut_35 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_36'] = x_compute_monthly_incident_report__mutmut_36 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_37'] = x_compute_monthly_incident_report__mutmut_37 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_38'] = x_compute_monthly_incident_report__mutmut_38 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_39'] = x_compute_monthly_incident_report__mutmut_39 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_40'] = x_compute_monthly_incident_report__mutmut_40 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_41'] = x_compute_monthly_incident_report__mutmut_41 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_42'] = x_compute_monthly_incident_report__mutmut_42 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_43'] = x_compute_monthly_incident_report__mutmut_43 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_44'] = x_compute_monthly_incident_report__mutmut_44 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_45'] = x_compute_monthly_incident_report__mutmut_45 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_46'] = x_compute_monthly_incident_report__mutmut_46 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_47'] = x_compute_monthly_incident_report__mutmut_47 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_48'] = x_compute_monthly_incident_report__mutmut_48 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_49'] = x_compute_monthly_incident_report__mutmut_49 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_50'] = x_compute_monthly_incident_report__mutmut_50 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_51'] = x_compute_monthly_incident_report__mutmut_51 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_52'] = x_compute_monthly_incident_report__mutmut_52 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_53'] = x_compute_monthly_incident_report__mutmut_53 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_54'] = x_compute_monthly_incident_report__mutmut_54 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_55'] = x_compute_monthly_incident_report__mutmut_55 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_56'] = x_compute_monthly_incident_report__mutmut_56 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_57'] = x_compute_monthly_incident_report__mutmut_57 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_58'] = x_compute_monthly_incident_report__mutmut_58 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_59'] = x_compute_monthly_incident_report__mutmut_59 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_60'] = x_compute_monthly_incident_report__mutmut_60 # type: ignore # mutmut generated
mutants_x_compute_monthly_incident_report__mutmut['x_compute_monthly_incident_report__mutmut_61'] = x_compute_monthly_incident_report__mutmut_61 # type: ignore # mutmut generated
mutants_x_register__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register__mutmut)
def register(mcp: FastMCP) -> None:
    mcp.tool()(compute_monthly_incident_report)


def x_register__mutmut_orig(mcp: FastMCP) -> None:
    mcp.tool()(compute_monthly_incident_report)


def x_register__mutmut_1(mcp: FastMCP) -> None:
    mcp.tool()(None)

mutants_x_register__mutmut['_mutmut_orig'] = x_register__mutmut_orig # type: ignore # mutmut generated
mutants_x_register__mutmut['x_register__mutmut_1'] = x_register__mutmut_1 # type: ignore # mutmut generated
