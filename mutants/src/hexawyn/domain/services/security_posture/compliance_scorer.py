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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_score_category__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_score_category__mutmut)
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


def x_score_category__mutmut_orig(
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


def x_score_category__mutmut_1(
    category: str,
    records: list[WorkloadComplianceRaw],
    policy_defined: bool,
) -> CategoryScore:
    """Score one compliance category.

    Exempt workloads are excluded from the denominator (neither compliant nor
    non-compliant). A category with no defined policy scores 0% and is flagged
    ``policy_defined=False`` — never silently counted as compliant.
    """
    exempt = None
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


def x_score_category__mutmut_2(
    category: str,
    records: list[WorkloadComplianceRaw],
    policy_defined: bool,
) -> CategoryScore:
    """Score one compliance category.

    Exempt workloads are excluded from the denominator (neither compliant nor
    non-compliant). A category with no defined policy scores 0% and is flagged
    ``policy_defined=False`` — never silently counted as compliant.
    """
    exempt = [record for record in records if record["XXexemptXX"]]
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


def x_score_category__mutmut_3(
    category: str,
    records: list[WorkloadComplianceRaw],
    policy_defined: bool,
) -> CategoryScore:
    """Score one compliance category.

    Exempt workloads are excluded from the denominator (neither compliant nor
    non-compliant). A category with no defined policy scores 0% and is flagged
    ``policy_defined=False`` — never silently counted as compliant.
    """
    exempt = [record for record in records if record["EXEMPT"]]
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


def x_score_category__mutmut_4(
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
    evaluated = None
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


def x_score_category__mutmut_5(
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
    evaluated = [record for record in records if record["exempt"]]
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


def x_score_category__mutmut_6(
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
    evaluated = [record for record in records if not record["XXexemptXX"]]
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


def x_score_category__mutmut_7(
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
    evaluated = [record for record in records if not record["EXEMPT"]]
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


def x_score_category__mutmut_8(
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
    compliant = None
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


def x_score_category__mutmut_9(
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
    compliant = [record for record in evaluated if record["XXcompliantXX"]]
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


def x_score_category__mutmut_10(
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
    compliant = [record for record in evaluated if record["COMPLIANT"]]
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


def x_score_category__mutmut_11(
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
    non_compliant = None

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


def x_score_category__mutmut_12(
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
    non_compliant = [record for record in evaluated if record["compliant"]]

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


def x_score_category__mutmut_13(
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
    non_compliant = [record for record in evaluated if not record["XXcompliantXX"]]

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


def x_score_category__mutmut_14(
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
    non_compliant = [record for record in evaluated if not record["COMPLIANT"]]

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


def x_score_category__mutmut_15(
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
        category=None,
        total=len(evaluated),
        compliant=len(compliant),
        non_compliant=len(non_compliant),
        exempt=len(exempt),
        score_pct=_category_score_pct(policy_defined, len(compliant), len(evaluated)),
        policy_defined=policy_defined,
        non_compliant_workloads=[_to_finding(record, category) for record in non_compliant],
    )


def x_score_category__mutmut_16(
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
        total=None,
        compliant=len(compliant),
        non_compliant=len(non_compliant),
        exempt=len(exempt),
        score_pct=_category_score_pct(policy_defined, len(compliant), len(evaluated)),
        policy_defined=policy_defined,
        non_compliant_workloads=[_to_finding(record, category) for record in non_compliant],
    )


def x_score_category__mutmut_17(
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
        compliant=None,
        non_compliant=len(non_compliant),
        exempt=len(exempt),
        score_pct=_category_score_pct(policy_defined, len(compliant), len(evaluated)),
        policy_defined=policy_defined,
        non_compliant_workloads=[_to_finding(record, category) for record in non_compliant],
    )


def x_score_category__mutmut_18(
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
        non_compliant=None,
        exempt=len(exempt),
        score_pct=_category_score_pct(policy_defined, len(compliant), len(evaluated)),
        policy_defined=policy_defined,
        non_compliant_workloads=[_to_finding(record, category) for record in non_compliant],
    )


def x_score_category__mutmut_19(
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
        exempt=None,
        score_pct=_category_score_pct(policy_defined, len(compliant), len(evaluated)),
        policy_defined=policy_defined,
        non_compliant_workloads=[_to_finding(record, category) for record in non_compliant],
    )


def x_score_category__mutmut_20(
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
        score_pct=None,
        policy_defined=policy_defined,
        non_compliant_workloads=[_to_finding(record, category) for record in non_compliant],
    )


def x_score_category__mutmut_21(
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
        policy_defined=None,
        non_compliant_workloads=[_to_finding(record, category) for record in non_compliant],
    )


def x_score_category__mutmut_22(
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
        non_compliant_workloads=None,
    )


def x_score_category__mutmut_23(
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
        total=len(evaluated),
        compliant=len(compliant),
        non_compliant=len(non_compliant),
        exempt=len(exempt),
        score_pct=_category_score_pct(policy_defined, len(compliant), len(evaluated)),
        policy_defined=policy_defined,
        non_compliant_workloads=[_to_finding(record, category) for record in non_compliant],
    )


def x_score_category__mutmut_24(
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
        compliant=len(compliant),
        non_compliant=len(non_compliant),
        exempt=len(exempt),
        score_pct=_category_score_pct(policy_defined, len(compliant), len(evaluated)),
        policy_defined=policy_defined,
        non_compliant_workloads=[_to_finding(record, category) for record in non_compliant],
    )


def x_score_category__mutmut_25(
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
        non_compliant=len(non_compliant),
        exempt=len(exempt),
        score_pct=_category_score_pct(policy_defined, len(compliant), len(evaluated)),
        policy_defined=policy_defined,
        non_compliant_workloads=[_to_finding(record, category) for record in non_compliant],
    )


def x_score_category__mutmut_26(
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
        exempt=len(exempt),
        score_pct=_category_score_pct(policy_defined, len(compliant), len(evaluated)),
        policy_defined=policy_defined,
        non_compliant_workloads=[_to_finding(record, category) for record in non_compliant],
    )


def x_score_category__mutmut_27(
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
        score_pct=_category_score_pct(policy_defined, len(compliant), len(evaluated)),
        policy_defined=policy_defined,
        non_compliant_workloads=[_to_finding(record, category) for record in non_compliant],
    )


def x_score_category__mutmut_28(
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
        policy_defined=policy_defined,
        non_compliant_workloads=[_to_finding(record, category) for record in non_compliant],
    )


def x_score_category__mutmut_29(
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
        non_compliant_workloads=[_to_finding(record, category) for record in non_compliant],
    )


def x_score_category__mutmut_30(
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
        )


def x_score_category__mutmut_31(
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
        score_pct=_category_score_pct(None, len(compliant), len(evaluated)),
        policy_defined=policy_defined,
        non_compliant_workloads=[_to_finding(record, category) for record in non_compliant],
    )


def x_score_category__mutmut_32(
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
        score_pct=_category_score_pct(policy_defined, None, len(evaluated)),
        policy_defined=policy_defined,
        non_compliant_workloads=[_to_finding(record, category) for record in non_compliant],
    )


def x_score_category__mutmut_33(
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
        score_pct=_category_score_pct(policy_defined, len(compliant), None),
        policy_defined=policy_defined,
        non_compliant_workloads=[_to_finding(record, category) for record in non_compliant],
    )


def x_score_category__mutmut_34(
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
        score_pct=_category_score_pct(len(compliant), len(evaluated)),
        policy_defined=policy_defined,
        non_compliant_workloads=[_to_finding(record, category) for record in non_compliant],
    )


def x_score_category__mutmut_35(
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
        score_pct=_category_score_pct(policy_defined, len(evaluated)),
        policy_defined=policy_defined,
        non_compliant_workloads=[_to_finding(record, category) for record in non_compliant],
    )


def x_score_category__mutmut_36(
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
        score_pct=_category_score_pct(policy_defined, len(compliant), ),
        policy_defined=policy_defined,
        non_compliant_workloads=[_to_finding(record, category) for record in non_compliant],
    )


def x_score_category__mutmut_37(
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
        non_compliant_workloads=[_to_finding(None, category) for record in non_compliant],
    )


def x_score_category__mutmut_38(
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
        non_compliant_workloads=[_to_finding(record, None) for record in non_compliant],
    )


def x_score_category__mutmut_39(
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
        non_compliant_workloads=[_to_finding(category) for record in non_compliant],
    )


def x_score_category__mutmut_40(
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
        non_compliant_workloads=[_to_finding(record, ) for record in non_compliant],
    )

mutants_x_score_category__mutmut['_mutmut_orig'] = x_score_category__mutmut_orig # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_1'] = x_score_category__mutmut_1 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_2'] = x_score_category__mutmut_2 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_3'] = x_score_category__mutmut_3 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_4'] = x_score_category__mutmut_4 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_5'] = x_score_category__mutmut_5 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_6'] = x_score_category__mutmut_6 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_7'] = x_score_category__mutmut_7 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_8'] = x_score_category__mutmut_8 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_9'] = x_score_category__mutmut_9 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_10'] = x_score_category__mutmut_10 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_11'] = x_score_category__mutmut_11 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_12'] = x_score_category__mutmut_12 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_13'] = x_score_category__mutmut_13 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_14'] = x_score_category__mutmut_14 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_15'] = x_score_category__mutmut_15 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_16'] = x_score_category__mutmut_16 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_17'] = x_score_category__mutmut_17 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_18'] = x_score_category__mutmut_18 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_19'] = x_score_category__mutmut_19 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_20'] = x_score_category__mutmut_20 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_21'] = x_score_category__mutmut_21 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_22'] = x_score_category__mutmut_22 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_23'] = x_score_category__mutmut_23 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_24'] = x_score_category__mutmut_24 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_25'] = x_score_category__mutmut_25 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_26'] = x_score_category__mutmut_26 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_27'] = x_score_category__mutmut_27 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_28'] = x_score_category__mutmut_28 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_29'] = x_score_category__mutmut_29 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_30'] = x_score_category__mutmut_30 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_31'] = x_score_category__mutmut_31 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_32'] = x_score_category__mutmut_32 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_33'] = x_score_category__mutmut_33 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_34'] = x_score_category__mutmut_34 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_35'] = x_score_category__mutmut_35 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_36'] = x_score_category__mutmut_36 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_37'] = x_score_category__mutmut_37 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_38'] = x_score_category__mutmut_38 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_39'] = x_score_category__mutmut_39 # type: ignore # mutmut generated
mutants_x_score_category__mutmut['x_score_category__mutmut_40'] = x_score_category__mutmut_40 # type: ignore # mutmut generated
mutants_x_compute_overall_score__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_overall_score__mutmut)
def compute_overall_score(categories: list[CategoryScore]) -> float:
    """Overall score is the mean of the defined categories' scores.

    Categories without a defined policy are excluded from the mean; when no
    category has a defined policy the overall score is 0.0.
    """
    defined = [category for category in categories if category.policy_defined]
    if not defined:
        return 0.0
    return round(sum(category.score_pct for category in defined) / len(defined), 1)


def x_compute_overall_score__mutmut_orig(categories: list[CategoryScore]) -> float:
    """Overall score is the mean of the defined categories' scores.

    Categories without a defined policy are excluded from the mean; when no
    category has a defined policy the overall score is 0.0.
    """
    defined = [category for category in categories if category.policy_defined]
    if not defined:
        return 0.0
    return round(sum(category.score_pct for category in defined) / len(defined), 1)


def x_compute_overall_score__mutmut_1(categories: list[CategoryScore]) -> float:
    """Overall score is the mean of the defined categories' scores.

    Categories without a defined policy are excluded from the mean; when no
    category has a defined policy the overall score is 0.0.
    """
    defined = None
    if not defined:
        return 0.0
    return round(sum(category.score_pct for category in defined) / len(defined), 1)


def x_compute_overall_score__mutmut_2(categories: list[CategoryScore]) -> float:
    """Overall score is the mean of the defined categories' scores.

    Categories without a defined policy are excluded from the mean; when no
    category has a defined policy the overall score is 0.0.
    """
    defined = [category for category in categories if category.policy_defined]
    if defined:
        return 0.0
    return round(sum(category.score_pct for category in defined) / len(defined), 1)


def x_compute_overall_score__mutmut_3(categories: list[CategoryScore]) -> float:
    """Overall score is the mean of the defined categories' scores.

    Categories without a defined policy are excluded from the mean; when no
    category has a defined policy the overall score is 0.0.
    """
    defined = [category for category in categories if category.policy_defined]
    if not defined:
        return 1.0
    return round(sum(category.score_pct for category in defined) / len(defined), 1)


def x_compute_overall_score__mutmut_4(categories: list[CategoryScore]) -> float:
    """Overall score is the mean of the defined categories' scores.

    Categories without a defined policy are excluded from the mean; when no
    category has a defined policy the overall score is 0.0.
    """
    defined = [category for category in categories if category.policy_defined]
    if not defined:
        return 0.0
    return round(None, 1)


def x_compute_overall_score__mutmut_5(categories: list[CategoryScore]) -> float:
    """Overall score is the mean of the defined categories' scores.

    Categories without a defined policy are excluded from the mean; when no
    category has a defined policy the overall score is 0.0.
    """
    defined = [category for category in categories if category.policy_defined]
    if not defined:
        return 0.0
    return round(sum(category.score_pct for category in defined) / len(defined), None)


def x_compute_overall_score__mutmut_6(categories: list[CategoryScore]) -> float:
    """Overall score is the mean of the defined categories' scores.

    Categories without a defined policy are excluded from the mean; when no
    category has a defined policy the overall score is 0.0.
    """
    defined = [category for category in categories if category.policy_defined]
    if not defined:
        return 0.0
    return round(1)


def x_compute_overall_score__mutmut_7(categories: list[CategoryScore]) -> float:
    """Overall score is the mean of the defined categories' scores.

    Categories without a defined policy are excluded from the mean; when no
    category has a defined policy the overall score is 0.0.
    """
    defined = [category for category in categories if category.policy_defined]
    if not defined:
        return 0.0
    return round(sum(category.score_pct for category in defined) / len(defined), )


def x_compute_overall_score__mutmut_8(categories: list[CategoryScore]) -> float:
    """Overall score is the mean of the defined categories' scores.

    Categories without a defined policy are excluded from the mean; when no
    category has a defined policy the overall score is 0.0.
    """
    defined = [category for category in categories if category.policy_defined]
    if not defined:
        return 0.0
    return round(sum(category.score_pct for category in defined) * len(defined), 1)


def x_compute_overall_score__mutmut_9(categories: list[CategoryScore]) -> float:
    """Overall score is the mean of the defined categories' scores.

    Categories without a defined policy are excluded from the mean; when no
    category has a defined policy the overall score is 0.0.
    """
    defined = [category for category in categories if category.policy_defined]
    if not defined:
        return 0.0
    return round(sum(None) / len(defined), 1)


def x_compute_overall_score__mutmut_10(categories: list[CategoryScore]) -> float:
    """Overall score is the mean of the defined categories' scores.

    Categories without a defined policy are excluded from the mean; when no
    category has a defined policy the overall score is 0.0.
    """
    defined = [category for category in categories if category.policy_defined]
    if not defined:
        return 0.0
    return round(sum(category.score_pct for category in defined) / len(defined), 2)

mutants_x_compute_overall_score__mutmut['_mutmut_orig'] = x_compute_overall_score__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_overall_score__mutmut['x_compute_overall_score__mutmut_1'] = x_compute_overall_score__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_overall_score__mutmut['x_compute_overall_score__mutmut_2'] = x_compute_overall_score__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_overall_score__mutmut['x_compute_overall_score__mutmut_3'] = x_compute_overall_score__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_overall_score__mutmut['x_compute_overall_score__mutmut_4'] = x_compute_overall_score__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_overall_score__mutmut['x_compute_overall_score__mutmut_5'] = x_compute_overall_score__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_overall_score__mutmut['x_compute_overall_score__mutmut_6'] = x_compute_overall_score__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_overall_score__mutmut['x_compute_overall_score__mutmut_7'] = x_compute_overall_score__mutmut_7 # type: ignore # mutmut generated
mutants_x_compute_overall_score__mutmut['x_compute_overall_score__mutmut_8'] = x_compute_overall_score__mutmut_8 # type: ignore # mutmut generated
mutants_x_compute_overall_score__mutmut['x_compute_overall_score__mutmut_9'] = x_compute_overall_score__mutmut_9 # type: ignore # mutmut generated
mutants_x_compute_overall_score__mutmut['x_compute_overall_score__mutmut_10'] = x_compute_overall_score__mutmut_10 # type: ignore # mutmut generated
mutants_x__category_score_pct__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__category_score_pct__mutmut)
def _category_score_pct(policy_defined: bool, compliant: int, evaluated: int) -> float:
    if not policy_defined:
        return 0.0
    if evaluated == 0:
        return 100.0
    return round(compliant / evaluated * 100, 1)


def x__category_score_pct__mutmut_orig(policy_defined: bool, compliant: int, evaluated: int) -> float:
    if not policy_defined:
        return 0.0
    if evaluated == 0:
        return 100.0
    return round(compliant / evaluated * 100, 1)


def x__category_score_pct__mutmut_1(policy_defined: bool, compliant: int, evaluated: int) -> float:
    if policy_defined:
        return 0.0
    if evaluated == 0:
        return 100.0
    return round(compliant / evaluated * 100, 1)


def x__category_score_pct__mutmut_2(policy_defined: bool, compliant: int, evaluated: int) -> float:
    if not policy_defined:
        return 1.0
    if evaluated == 0:
        return 100.0
    return round(compliant / evaluated * 100, 1)


def x__category_score_pct__mutmut_3(policy_defined: bool, compliant: int, evaluated: int) -> float:
    if not policy_defined:
        return 0.0
    if evaluated != 0:
        return 100.0
    return round(compliant / evaluated * 100, 1)


def x__category_score_pct__mutmut_4(policy_defined: bool, compliant: int, evaluated: int) -> float:
    if not policy_defined:
        return 0.0
    if evaluated == 1:
        return 100.0
    return round(compliant / evaluated * 100, 1)


def x__category_score_pct__mutmut_5(policy_defined: bool, compliant: int, evaluated: int) -> float:
    if not policy_defined:
        return 0.0
    if evaluated == 0:
        return 101.0
    return round(compliant / evaluated * 100, 1)


def x__category_score_pct__mutmut_6(policy_defined: bool, compliant: int, evaluated: int) -> float:
    if not policy_defined:
        return 0.0
    if evaluated == 0:
        return 100.0
    return round(None, 1)


def x__category_score_pct__mutmut_7(policy_defined: bool, compliant: int, evaluated: int) -> float:
    if not policy_defined:
        return 0.0
    if evaluated == 0:
        return 100.0
    return round(compliant / evaluated * 100, None)


def x__category_score_pct__mutmut_8(policy_defined: bool, compliant: int, evaluated: int) -> float:
    if not policy_defined:
        return 0.0
    if evaluated == 0:
        return 100.0
    return round(1)


def x__category_score_pct__mutmut_9(policy_defined: bool, compliant: int, evaluated: int) -> float:
    if not policy_defined:
        return 0.0
    if evaluated == 0:
        return 100.0
    return round(compliant / evaluated * 100, )


def x__category_score_pct__mutmut_10(policy_defined: bool, compliant: int, evaluated: int) -> float:
    if not policy_defined:
        return 0.0
    if evaluated == 0:
        return 100.0
    return round(compliant / evaluated / 100, 1)


def x__category_score_pct__mutmut_11(policy_defined: bool, compliant: int, evaluated: int) -> float:
    if not policy_defined:
        return 0.0
    if evaluated == 0:
        return 100.0
    return round(compliant * evaluated * 100, 1)


def x__category_score_pct__mutmut_12(policy_defined: bool, compliant: int, evaluated: int) -> float:
    if not policy_defined:
        return 0.0
    if evaluated == 0:
        return 100.0
    return round(compliant / evaluated * 101, 1)


def x__category_score_pct__mutmut_13(policy_defined: bool, compliant: int, evaluated: int) -> float:
    if not policy_defined:
        return 0.0
    if evaluated == 0:
        return 100.0
    return round(compliant / evaluated * 100, 2)

mutants_x__category_score_pct__mutmut['_mutmut_orig'] = x__category_score_pct__mutmut_orig # type: ignore # mutmut generated
mutants_x__category_score_pct__mutmut['x__category_score_pct__mutmut_1'] = x__category_score_pct__mutmut_1 # type: ignore # mutmut generated
mutants_x__category_score_pct__mutmut['x__category_score_pct__mutmut_2'] = x__category_score_pct__mutmut_2 # type: ignore # mutmut generated
mutants_x__category_score_pct__mutmut['x__category_score_pct__mutmut_3'] = x__category_score_pct__mutmut_3 # type: ignore # mutmut generated
mutants_x__category_score_pct__mutmut['x__category_score_pct__mutmut_4'] = x__category_score_pct__mutmut_4 # type: ignore # mutmut generated
mutants_x__category_score_pct__mutmut['x__category_score_pct__mutmut_5'] = x__category_score_pct__mutmut_5 # type: ignore # mutmut generated
mutants_x__category_score_pct__mutmut['x__category_score_pct__mutmut_6'] = x__category_score_pct__mutmut_6 # type: ignore # mutmut generated
mutants_x__category_score_pct__mutmut['x__category_score_pct__mutmut_7'] = x__category_score_pct__mutmut_7 # type: ignore # mutmut generated
mutants_x__category_score_pct__mutmut['x__category_score_pct__mutmut_8'] = x__category_score_pct__mutmut_8 # type: ignore # mutmut generated
mutants_x__category_score_pct__mutmut['x__category_score_pct__mutmut_9'] = x__category_score_pct__mutmut_9 # type: ignore # mutmut generated
mutants_x__category_score_pct__mutmut['x__category_score_pct__mutmut_10'] = x__category_score_pct__mutmut_10 # type: ignore # mutmut generated
mutants_x__category_score_pct__mutmut['x__category_score_pct__mutmut_11'] = x__category_score_pct__mutmut_11 # type: ignore # mutmut generated
mutants_x__category_score_pct__mutmut['x__category_score_pct__mutmut_12'] = x__category_score_pct__mutmut_12 # type: ignore # mutmut generated
mutants_x__category_score_pct__mutmut['x__category_score_pct__mutmut_13'] = x__category_score_pct__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_finding__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_finding__mutmut)
def _to_finding(record: WorkloadComplianceRaw, category: str) -> WorkloadCompliance:
    return WorkloadCompliance(
        workload=record["workload"],
        namespace=record["namespace"],
        category=category,
        status="non_compliant",
        remediation_priority=_REMEDIATION_PRIORITY.get(category, _DEFAULT_PRIORITY),
        detail=record.get("detail", ""),
    )


def x__to_finding__mutmut_orig(record: WorkloadComplianceRaw, category: str) -> WorkloadCompliance:
    return WorkloadCompliance(
        workload=record["workload"],
        namespace=record["namespace"],
        category=category,
        status="non_compliant",
        remediation_priority=_REMEDIATION_PRIORITY.get(category, _DEFAULT_PRIORITY),
        detail=record.get("detail", ""),
    )


def x__to_finding__mutmut_1(record: WorkloadComplianceRaw, category: str) -> WorkloadCompliance:
    return WorkloadCompliance(
        workload=None,
        namespace=record["namespace"],
        category=category,
        status="non_compliant",
        remediation_priority=_REMEDIATION_PRIORITY.get(category, _DEFAULT_PRIORITY),
        detail=record.get("detail", ""),
    )


def x__to_finding__mutmut_2(record: WorkloadComplianceRaw, category: str) -> WorkloadCompliance:
    return WorkloadCompliance(
        workload=record["workload"],
        namespace=None,
        category=category,
        status="non_compliant",
        remediation_priority=_REMEDIATION_PRIORITY.get(category, _DEFAULT_PRIORITY),
        detail=record.get("detail", ""),
    )


def x__to_finding__mutmut_3(record: WorkloadComplianceRaw, category: str) -> WorkloadCompliance:
    return WorkloadCompliance(
        workload=record["workload"],
        namespace=record["namespace"],
        category=None,
        status="non_compliant",
        remediation_priority=_REMEDIATION_PRIORITY.get(category, _DEFAULT_PRIORITY),
        detail=record.get("detail", ""),
    )


def x__to_finding__mutmut_4(record: WorkloadComplianceRaw, category: str) -> WorkloadCompliance:
    return WorkloadCompliance(
        workload=record["workload"],
        namespace=record["namespace"],
        category=category,
        status=None,
        remediation_priority=_REMEDIATION_PRIORITY.get(category, _DEFAULT_PRIORITY),
        detail=record.get("detail", ""),
    )


def x__to_finding__mutmut_5(record: WorkloadComplianceRaw, category: str) -> WorkloadCompliance:
    return WorkloadCompliance(
        workload=record["workload"],
        namespace=record["namespace"],
        category=category,
        status="non_compliant",
        remediation_priority=None,
        detail=record.get("detail", ""),
    )


def x__to_finding__mutmut_6(record: WorkloadComplianceRaw, category: str) -> WorkloadCompliance:
    return WorkloadCompliance(
        workload=record["workload"],
        namespace=record["namespace"],
        category=category,
        status="non_compliant",
        remediation_priority=_REMEDIATION_PRIORITY.get(category, _DEFAULT_PRIORITY),
        detail=None,
    )


def x__to_finding__mutmut_7(record: WorkloadComplianceRaw, category: str) -> WorkloadCompliance:
    return WorkloadCompliance(
        namespace=record["namespace"],
        category=category,
        status="non_compliant",
        remediation_priority=_REMEDIATION_PRIORITY.get(category, _DEFAULT_PRIORITY),
        detail=record.get("detail", ""),
    )


def x__to_finding__mutmut_8(record: WorkloadComplianceRaw, category: str) -> WorkloadCompliance:
    return WorkloadCompliance(
        workload=record["workload"],
        category=category,
        status="non_compliant",
        remediation_priority=_REMEDIATION_PRIORITY.get(category, _DEFAULT_PRIORITY),
        detail=record.get("detail", ""),
    )


def x__to_finding__mutmut_9(record: WorkloadComplianceRaw, category: str) -> WorkloadCompliance:
    return WorkloadCompliance(
        workload=record["workload"],
        namespace=record["namespace"],
        status="non_compliant",
        remediation_priority=_REMEDIATION_PRIORITY.get(category, _DEFAULT_PRIORITY),
        detail=record.get("detail", ""),
    )


def x__to_finding__mutmut_10(record: WorkloadComplianceRaw, category: str) -> WorkloadCompliance:
    return WorkloadCompliance(
        workload=record["workload"],
        namespace=record["namespace"],
        category=category,
        remediation_priority=_REMEDIATION_PRIORITY.get(category, _DEFAULT_PRIORITY),
        detail=record.get("detail", ""),
    )


def x__to_finding__mutmut_11(record: WorkloadComplianceRaw, category: str) -> WorkloadCompliance:
    return WorkloadCompliance(
        workload=record["workload"],
        namespace=record["namespace"],
        category=category,
        status="non_compliant",
        detail=record.get("detail", ""),
    )


def x__to_finding__mutmut_12(record: WorkloadComplianceRaw, category: str) -> WorkloadCompliance:
    return WorkloadCompliance(
        workload=record["workload"],
        namespace=record["namespace"],
        category=category,
        status="non_compliant",
        remediation_priority=_REMEDIATION_PRIORITY.get(category, _DEFAULT_PRIORITY),
        )


def x__to_finding__mutmut_13(record: WorkloadComplianceRaw, category: str) -> WorkloadCompliance:
    return WorkloadCompliance(
        workload=record["XXworkloadXX"],
        namespace=record["namespace"],
        category=category,
        status="non_compliant",
        remediation_priority=_REMEDIATION_PRIORITY.get(category, _DEFAULT_PRIORITY),
        detail=record.get("detail", ""),
    )


def x__to_finding__mutmut_14(record: WorkloadComplianceRaw, category: str) -> WorkloadCompliance:
    return WorkloadCompliance(
        workload=record["WORKLOAD"],
        namespace=record["namespace"],
        category=category,
        status="non_compliant",
        remediation_priority=_REMEDIATION_PRIORITY.get(category, _DEFAULT_PRIORITY),
        detail=record.get("detail", ""),
    )


def x__to_finding__mutmut_15(record: WorkloadComplianceRaw, category: str) -> WorkloadCompliance:
    return WorkloadCompliance(
        workload=record["workload"],
        namespace=record["XXnamespaceXX"],
        category=category,
        status="non_compliant",
        remediation_priority=_REMEDIATION_PRIORITY.get(category, _DEFAULT_PRIORITY),
        detail=record.get("detail", ""),
    )


def x__to_finding__mutmut_16(record: WorkloadComplianceRaw, category: str) -> WorkloadCompliance:
    return WorkloadCompliance(
        workload=record["workload"],
        namespace=record["NAMESPACE"],
        category=category,
        status="non_compliant",
        remediation_priority=_REMEDIATION_PRIORITY.get(category, _DEFAULT_PRIORITY),
        detail=record.get("detail", ""),
    )


def x__to_finding__mutmut_17(record: WorkloadComplianceRaw, category: str) -> WorkloadCompliance:
    return WorkloadCompliance(
        workload=record["workload"],
        namespace=record["namespace"],
        category=category,
        status="XXnon_compliantXX",
        remediation_priority=_REMEDIATION_PRIORITY.get(category, _DEFAULT_PRIORITY),
        detail=record.get("detail", ""),
    )


def x__to_finding__mutmut_18(record: WorkloadComplianceRaw, category: str) -> WorkloadCompliance:
    return WorkloadCompliance(
        workload=record["workload"],
        namespace=record["namespace"],
        category=category,
        status="NON_COMPLIANT",
        remediation_priority=_REMEDIATION_PRIORITY.get(category, _DEFAULT_PRIORITY),
        detail=record.get("detail", ""),
    )


def x__to_finding__mutmut_19(record: WorkloadComplianceRaw, category: str) -> WorkloadCompliance:
    return WorkloadCompliance(
        workload=record["workload"],
        namespace=record["namespace"],
        category=category,
        status="non_compliant",
        remediation_priority=_REMEDIATION_PRIORITY.get(None, _DEFAULT_PRIORITY),
        detail=record.get("detail", ""),
    )


def x__to_finding__mutmut_20(record: WorkloadComplianceRaw, category: str) -> WorkloadCompliance:
    return WorkloadCompliance(
        workload=record["workload"],
        namespace=record["namespace"],
        category=category,
        status="non_compliant",
        remediation_priority=_REMEDIATION_PRIORITY.get(category, None),
        detail=record.get("detail", ""),
    )


def x__to_finding__mutmut_21(record: WorkloadComplianceRaw, category: str) -> WorkloadCompliance:
    return WorkloadCompliance(
        workload=record["workload"],
        namespace=record["namespace"],
        category=category,
        status="non_compliant",
        remediation_priority=_REMEDIATION_PRIORITY.get(_DEFAULT_PRIORITY),
        detail=record.get("detail", ""),
    )


def x__to_finding__mutmut_22(record: WorkloadComplianceRaw, category: str) -> WorkloadCompliance:
    return WorkloadCompliance(
        workload=record["workload"],
        namespace=record["namespace"],
        category=category,
        status="non_compliant",
        remediation_priority=_REMEDIATION_PRIORITY.get(category, ),
        detail=record.get("detail", ""),
    )


def x__to_finding__mutmut_23(record: WorkloadComplianceRaw, category: str) -> WorkloadCompliance:
    return WorkloadCompliance(
        workload=record["workload"],
        namespace=record["namespace"],
        category=category,
        status="non_compliant",
        remediation_priority=_REMEDIATION_PRIORITY.get(category, _DEFAULT_PRIORITY),
        detail=record.get(None, ""),
    )


def x__to_finding__mutmut_24(record: WorkloadComplianceRaw, category: str) -> WorkloadCompliance:
    return WorkloadCompliance(
        workload=record["workload"],
        namespace=record["namespace"],
        category=category,
        status="non_compliant",
        remediation_priority=_REMEDIATION_PRIORITY.get(category, _DEFAULT_PRIORITY),
        detail=record.get("detail", None),
    )


def x__to_finding__mutmut_25(record: WorkloadComplianceRaw, category: str) -> WorkloadCompliance:
    return WorkloadCompliance(
        workload=record["workload"],
        namespace=record["namespace"],
        category=category,
        status="non_compliant",
        remediation_priority=_REMEDIATION_PRIORITY.get(category, _DEFAULT_PRIORITY),
        detail=record.get(""),
    )


def x__to_finding__mutmut_26(record: WorkloadComplianceRaw, category: str) -> WorkloadCompliance:
    return WorkloadCompliance(
        workload=record["workload"],
        namespace=record["namespace"],
        category=category,
        status="non_compliant",
        remediation_priority=_REMEDIATION_PRIORITY.get(category, _DEFAULT_PRIORITY),
        detail=record.get("detail", ),
    )


def x__to_finding__mutmut_27(record: WorkloadComplianceRaw, category: str) -> WorkloadCompliance:
    return WorkloadCompliance(
        workload=record["workload"],
        namespace=record["namespace"],
        category=category,
        status="non_compliant",
        remediation_priority=_REMEDIATION_PRIORITY.get(category, _DEFAULT_PRIORITY),
        detail=record.get("XXdetailXX", ""),
    )


def x__to_finding__mutmut_28(record: WorkloadComplianceRaw, category: str) -> WorkloadCompliance:
    return WorkloadCompliance(
        workload=record["workload"],
        namespace=record["namespace"],
        category=category,
        status="non_compliant",
        remediation_priority=_REMEDIATION_PRIORITY.get(category, _DEFAULT_PRIORITY),
        detail=record.get("DETAIL", ""),
    )


def x__to_finding__mutmut_29(record: WorkloadComplianceRaw, category: str) -> WorkloadCompliance:
    return WorkloadCompliance(
        workload=record["workload"],
        namespace=record["namespace"],
        category=category,
        status="non_compliant",
        remediation_priority=_REMEDIATION_PRIORITY.get(category, _DEFAULT_PRIORITY),
        detail=record.get("detail", "XXXX"),
    )

mutants_x__to_finding__mutmut['_mutmut_orig'] = x__to_finding__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_finding__mutmut['x__to_finding__mutmut_1'] = x__to_finding__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_finding__mutmut['x__to_finding__mutmut_2'] = x__to_finding__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_finding__mutmut['x__to_finding__mutmut_3'] = x__to_finding__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_finding__mutmut['x__to_finding__mutmut_4'] = x__to_finding__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_finding__mutmut['x__to_finding__mutmut_5'] = x__to_finding__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_finding__mutmut['x__to_finding__mutmut_6'] = x__to_finding__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_finding__mutmut['x__to_finding__mutmut_7'] = x__to_finding__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_finding__mutmut['x__to_finding__mutmut_8'] = x__to_finding__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_finding__mutmut['x__to_finding__mutmut_9'] = x__to_finding__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_finding__mutmut['x__to_finding__mutmut_10'] = x__to_finding__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_finding__mutmut['x__to_finding__mutmut_11'] = x__to_finding__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_finding__mutmut['x__to_finding__mutmut_12'] = x__to_finding__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_finding__mutmut['x__to_finding__mutmut_13'] = x__to_finding__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_finding__mutmut['x__to_finding__mutmut_14'] = x__to_finding__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_finding__mutmut['x__to_finding__mutmut_15'] = x__to_finding__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_finding__mutmut['x__to_finding__mutmut_16'] = x__to_finding__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_finding__mutmut['x__to_finding__mutmut_17'] = x__to_finding__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_finding__mutmut['x__to_finding__mutmut_18'] = x__to_finding__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_finding__mutmut['x__to_finding__mutmut_19'] = x__to_finding__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_finding__mutmut['x__to_finding__mutmut_20'] = x__to_finding__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_finding__mutmut['x__to_finding__mutmut_21'] = x__to_finding__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_finding__mutmut['x__to_finding__mutmut_22'] = x__to_finding__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_finding__mutmut['x__to_finding__mutmut_23'] = x__to_finding__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_finding__mutmut['x__to_finding__mutmut_24'] = x__to_finding__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_finding__mutmut['x__to_finding__mutmut_25'] = x__to_finding__mutmut_25 # type: ignore # mutmut generated
mutants_x__to_finding__mutmut['x__to_finding__mutmut_26'] = x__to_finding__mutmut_26 # type: ignore # mutmut generated
mutants_x__to_finding__mutmut['x__to_finding__mutmut_27'] = x__to_finding__mutmut_27 # type: ignore # mutmut generated
mutants_x__to_finding__mutmut['x__to_finding__mutmut_28'] = x__to_finding__mutmut_28 # type: ignore # mutmut generated
mutants_x__to_finding__mutmut['x__to_finding__mutmut_29'] = x__to_finding__mutmut_29 # type: ignore # mutmut generated
