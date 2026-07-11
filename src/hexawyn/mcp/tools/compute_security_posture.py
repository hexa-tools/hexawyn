"""MCP tool: compute_security_posture — board-level security compliance score
aggregating TLS, RBAC, Pod Security, image scanning and secret rotation."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hexawyn.application.ports.driving.compute_security_posture.compute_security_posture_command import (  # noqa: E501
    ComputeSecurityPostureCommand,
)
from hexawyn.application.use_case.compute_security_posture.compute_security_posture_use_case import (  # noqa: E501
    ComputeSecurityPostureUseCase,
)

if TYPE_CHECKING:
    from fastmcp import FastMCP

    from hexawyn.domain.models.security_posture import CategoryScore, WorkloadCompliance


def compute_security_posture(previous_score_pct: float | None = None) -> dict[str, object]:
    """Compute the overall security compliance posture across all workloads.

    Returns the overall compliance score (%), a per-category breakdown (TLS,
    RBAC, Pod Security, image scanning, secret rotation), a priority-ordered
    remediation list, and the quarter-over-quarter trend when a previous score
    is provided. Categories without a defined policy are reported as such —
    never silently counted as compliant.
    """
    from hexawyn.application.service.compute_security_posture_service import (
        ComputeSecurityPostureService,
    )
    from hexawyn.mcp.server import build_security_posture_adapter

    try:
        adapter = build_security_posture_adapter()
        service = ComputeSecurityPostureService(posture_port=adapter)
        use_case = ComputeSecurityPostureUseCase(service=service)
        response = use_case.execute(
            ComputeSecurityPostureCommand(previous_score_pct=previous_score_pct)
        )
        report = response.result
        return {
            "overall_score_pct": report.overall_score_pct,
            "trend": report.trend,
            "previous_score_pct": report.previous_score_pct,
            "partial": report.partial,
            "warning": report.warning,
            "categories": [_serialize_category(category) for category in report.categories],
            "remediation_order": [
                _serialize_finding(finding) for finding in report.remediation_order
            ],
            "error": None,
        }
    except Exception as exc:
        return {
            "overall_score_pct": 0.0,
            "trend": "stable",
            "previous_score_pct": previous_score_pct,
            "partial": False,
            "warning": "",
            "categories": [],
            "remediation_order": [],
            "error": str(exc),
        }


def _serialize_category(category: CategoryScore) -> dict[str, object]:
    return {
        "category": category.category,
        "total": category.total,
        "compliant": category.compliant,
        "non_compliant": category.non_compliant,
        "exempt": category.exempt,
        "score_pct": category.score_pct,
        "policy_defined": category.policy_defined,
        "non_compliant_workloads": [
            _serialize_finding(finding) for finding in category.non_compliant_workloads
        ],
    }


def _serialize_finding(finding: WorkloadCompliance) -> dict[str, object]:
    return {
        "workload": finding.workload,
        "namespace": finding.namespace,
        "category": finding.category,
        "status": finding.status,
        "remediation_priority": finding.remediation_priority,
        "detail": finding.detail,
    }


def register(mcp: FastMCP) -> None:
    mcp.tool()(compute_security_posture)
