from __future__ import annotations

from hexawyn.domain.models.security_posture import (
    CategoryScore,
    WorkloadCompliance,
    WorkloadComplianceRaw,
)

_REMEDIATION_PRIORITY: dict[str, int] = {
    "image_scanning": 1,
    "rbac": 2,
    "secret_rotation": 3,
    "pod_security": 4,
    "tls": 5,
}
_DEFAULT_PRIORITY = 9


def score_category(
    category: str,
    records: list[WorkloadComplianceRaw],
    policy_defined: bool,
) -> CategoryScore:
    """Score one compliance category.

    Exempt workloads are excluded from the denominator (neither compliant nor
    non-compliant). A category with no defined policy scores 0% and is flagged
    ``policy_defined=False`` — never silently counted as compliant.
    """
    exempt = [record for record in records if record["exempt"]]
    evaluated = [record for record in records if not record["exempt"]]
    compliant = [record for record in evaluated if record["compliant"]]
    non_compliant = [record for record in evaluated if not record["compliant"]]

    return CategoryScore(
        category=category,
        total=len(evaluated),
        compliant=len(compliant),
        non_compliant=len(non_compliant),
        exempt=len(exempt),
        score_pct=_category_score_pct(policy_defined, len(compliant), len(evaluated)),
        policy_defined=policy_defined,
        non_compliant_workloads=[_to_finding(record, category) for record in non_compliant],
    )


def compute_overall_score(categories: list[CategoryScore]) -> float:
    """Overall score is the mean of the defined categories' scores.

    Categories without a defined policy are excluded from the mean; when no
    category has a defined policy the overall score is 0.0.
    """
    defined = [category for category in categories if category.policy_defined]
    if not defined:
        return 0.0
    return round(sum(category.score_pct for category in defined) / len(defined), 1)


def _category_score_pct(policy_defined: bool, compliant: int, evaluated: int) -> float:
    if not policy_defined:
        return 0.0
    if evaluated == 0:
        return 100.0
    return round(compliant / evaluated * 100, 1)


def _to_finding(record: WorkloadComplianceRaw, category: str) -> WorkloadCompliance:
    return WorkloadCompliance(
        workload=record["workload"],
        namespace=record["namespace"],
        category=category,
        status="non_compliant",
        remediation_priority=_REMEDIATION_PRIORITY.get(category, _DEFAULT_PRIORITY),
        detail=record.get("detail", ""),
    )
