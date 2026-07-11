"""MCP tool: report_critical_vulnerabilities — critical CVEs in business
language (affected services, oldest unresolved, remediation guidance)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.report_critical_vulnerabilities.report_critical_vulnerabilities_command import (  # noqa: E501
    ReportCriticalVulnerabilitiesCommand,
)
from hexawyn.application.use_case.report_critical_vulnerabilities.report_critical_vulnerabilities_use_case import (  # noqa: E501
    ReportCriticalVulnerabilitiesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP

    from hexawyn.domain.models.critical_cve import CveSummary


def report_critical_vulnerabilities() -> dict[str, object]:
    from hexawyn.application.service.report_critical_vulnerabilities_service import (
        ReportCriticalVulnerabilitiesService,
    )
    from hexawyn.mcp.server import build_critical_cve_adapter

    try:
        adapter = build_critical_cve_adapter()
        service = ReportCriticalVulnerabilitiesService(cve_port=adapter)
        use_case = ReportCriticalVulnerabilitiesUseCase(service=service)
        response = use_case.execute(ReportCriticalVulnerabilitiesCommand())
        r = response.result
        return {
            "period_label": r.period_label,
            "total_critical_cves": r.total_critical_cves,
            "affected_service_count": r.affected_service_count,
            "oldest_unresolved_days": r.oldest_unresolved_days,
            "total_images_scanned": r.total_images_scanned,
            "cves": [_serialize_cve(cve) for cve in r.cves],
            "has_data": r.has_data,
            "warning": r.warning,
            "error": None,
        }
    except Exception as exc:
        return {
            "period_label": "Dernier scan",
            "total_critical_cves": 0,
            "affected_service_count": 0,
            "oldest_unresolved_days": 0,
            "total_images_scanned": 0,
            "cves": [],
            "has_data": False,
            "warning": "",
            "error": str(exc),
        }


def _serialize_cve(cve: CveSummary) -> dict[str, object]:
    return {
        "business_service_name": cve.business_service_name,
        "severity": cve.severity,
        "count": cve.count,
        "oldest_unresolved_days": cve.oldest_unresolved_days,
    }


def register(mcp: FastMCP) -> None:
    mcp.tool()(report_critical_vulnerabilities)
