"""MCP tool: compute_security_posture."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.use_case.security.compute_security_posture.command import (
    ComputeSecurityPostureCommand,
)
from hexawyn.application.use_case.security.compute_security_posture.compute_security_posture_use_case import (  # noqa: E501
    ComputeSecurityPostureUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP


def compute_security_posture() -> dict[str, object]:
    from hexawyn.mcp.server import build_optimization_roi_adapter

    try:
        use_case = ComputeSecurityPostureUseCase(port=build_optimization_roi_adapter())  # type: ignore
        response = use_case.execute(ComputeSecurityPostureCommand())
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "categories": [
                {
                    "name": c.category,
                    "score_pct": c.score_pct,
                    "compliant": c.compliant,
                    "non_compliant_count": len(c.non_compliant_workloads),
                }
                for c in report.categories
            ],
            "remediation_order": [
                {"resource": r.workload, "namespace": r.namespace, "category": r.category}
                for r in report.remediation_order
            ],
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "error": response.error,
        }
    except Exception as exc:
        return {
            "overall_score_pct": None,
            "categories": [],
            "remediation_order": [],
            "trend": "",
            "previous_score_pct": None,
            "partial": False,
            "warning": "",
            "error": str(exc),
        }


def register(mcp: FastMCP) -> None:
    mcp.tool()(compute_security_posture)
