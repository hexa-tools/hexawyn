"""MCP tool: report_critical_vulnerabilities."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.report_critical_vulnerabilities.command import (
    ReportCriticalVulnerabilitiesCommand,
)
from hexawyn.application.use_case.report_critical_vulnerabilities.report_critical_vulnerabilities_use_case import (
    ReportCriticalVulnerabilitiesUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def report_critical_vulnerabilities() -> dict[str, object]:
    from hexawyn.mcp.server import build_critical_cve_adapter

    try:
        use_case = ReportCriticalVulnerabilitiesUseCase(cve_port=build_critical_cve_adapter())
        _ = use_case.execute(ReportCriticalVulnerabilitiesCommand())
        return {"error": None}
    except Exception as exc:
        return {"error": str(exc)}


def register(mcp: FastMCP) -> None:
    mcp.tool()(report_critical_vulnerabilities)
