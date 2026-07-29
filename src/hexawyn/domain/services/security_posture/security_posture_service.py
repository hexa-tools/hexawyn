from __future__ import annotations

from hexawyn.domain.models.security_posture import (
    CategoryScore,
    SecurityPostureReport,
    WorkloadCompliance,
    WorkloadComplianceRaw,
)
from hexawyn.domain.services.security_posture.compliance_scorer import (
    compute_overall_score,
    score_category,
)
from hexawyn.domain.services.security_posture.posture_trend import classify_trend

_ALL_CATEGORIES = ["tls", "rbac", "pod_security", "image_scanning", "secret_rotation"]
_PARTIAL_WARNING = (
    "Partial results: the compliance scan timed out before every workload was "
    "evaluated. Scores reflect the workloads that were checked."
)


class SecurityPostureService:
    """Domain service — aggregates per-workload compliance into a board-level
    security posture report: overall score, per-category breakdown, a
    priority-ordered remediation list, and a quarter-over-quarter trend."""

    def build_report(
        self,
        records: list[WorkloadComplianceRaw],
        defined_categories: list[str],
        partial: bool,
        previous_score_pct: float | None = None,
    ) -> SecurityPostureReport:
        categories = [
            score_category(
                category,
                [record for record in records if record["category"] == category],
                policy_defined=category in defined_categories,
            )
            for category in _ALL_CATEGORIES
        ]
        overall = compute_overall_score(categories)

        return SecurityPostureReport(
            overall_score_pct=overall,
            categories=categories,
            remediation_order=_remediation_order(categories),
            trend=classify_trend(overall, previous_score_pct),
            previous_score_pct=previous_score_pct,
            partial=partial,
            warning=_PARTIAL_WARNING if partial else "",
        )


def _remediation_order(categories: list[CategoryScore]) -> list[WorkloadCompliance]:
    findings: list[WorkloadCompliance] = []
    for category in categories:
        findings.extend(category.non_compliant_workloads)
    return sorted(findings, key=lambda finding: finding.remediation_priority)
