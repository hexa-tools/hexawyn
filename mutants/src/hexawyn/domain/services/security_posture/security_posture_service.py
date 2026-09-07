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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut: MutantDict = {}  # type: ignore


class SecurityPostureService:
    """Domain service — aggregates per-workload compliance into a board-level
    security posture report: overall score, per-category breakdown, a
    priority-ordered remediation list, and a quarter-over-quarter trend."""

    @_mutmut_mutated(mutants_xǁSecurityPostureServiceǁbuild_report__mutmut)
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

    def xǁSecurityPostureServiceǁbuild_report__mutmut_orig(
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

    def xǁSecurityPostureServiceǁbuild_report__mutmut_1(
        self,
        records: list[WorkloadComplianceRaw],
        defined_categories: list[str],
        partial: bool,
        previous_score_pct: float | None = None,
    ) -> SecurityPostureReport:
        categories = None
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

    def xǁSecurityPostureServiceǁbuild_report__mutmut_2(
        self,
        records: list[WorkloadComplianceRaw],
        defined_categories: list[str],
        partial: bool,
        previous_score_pct: float | None = None,
    ) -> SecurityPostureReport:
        categories = [
            score_category(
                None,
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

    def xǁSecurityPostureServiceǁbuild_report__mutmut_3(
        self,
        records: list[WorkloadComplianceRaw],
        defined_categories: list[str],
        partial: bool,
        previous_score_pct: float | None = None,
    ) -> SecurityPostureReport:
        categories = [
            score_category(
                category,
                None,
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

    def xǁSecurityPostureServiceǁbuild_report__mutmut_4(
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
                policy_defined=None,
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

    def xǁSecurityPostureServiceǁbuild_report__mutmut_5(
        self,
        records: list[WorkloadComplianceRaw],
        defined_categories: list[str],
        partial: bool,
        previous_score_pct: float | None = None,
    ) -> SecurityPostureReport:
        categories = [
            score_category(
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

    def xǁSecurityPostureServiceǁbuild_report__mutmut_6(
        self,
        records: list[WorkloadComplianceRaw],
        defined_categories: list[str],
        partial: bool,
        previous_score_pct: float | None = None,
    ) -> SecurityPostureReport:
        categories = [
            score_category(
                category,
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

    def xǁSecurityPostureServiceǁbuild_report__mutmut_7(
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

    def xǁSecurityPostureServiceǁbuild_report__mutmut_8(
        self,
        records: list[WorkloadComplianceRaw],
        defined_categories: list[str],
        partial: bool,
        previous_score_pct: float | None = None,
    ) -> SecurityPostureReport:
        categories = [
            score_category(
                category,
                [record for record in records if record["XXcategoryXX"] == category],
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

    def xǁSecurityPostureServiceǁbuild_report__mutmut_9(
        self,
        records: list[WorkloadComplianceRaw],
        defined_categories: list[str],
        partial: bool,
        previous_score_pct: float | None = None,
    ) -> SecurityPostureReport:
        categories = [
            score_category(
                category,
                [record for record in records if record["CATEGORY"] == category],
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

    def xǁSecurityPostureServiceǁbuild_report__mutmut_10(
        self,
        records: list[WorkloadComplianceRaw],
        defined_categories: list[str],
        partial: bool,
        previous_score_pct: float | None = None,
    ) -> SecurityPostureReport:
        categories = [
            score_category(
                category,
                [record for record in records if record["category"] != category],
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

    def xǁSecurityPostureServiceǁbuild_report__mutmut_11(
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
                policy_defined=category not in defined_categories,
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

    def xǁSecurityPostureServiceǁbuild_report__mutmut_12(
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
        overall = None

        return SecurityPostureReport(
            overall_score_pct=overall,
            categories=categories,
            remediation_order=_remediation_order(categories),
            trend=classify_trend(overall, previous_score_pct),
            previous_score_pct=previous_score_pct,
            partial=partial,
            warning=_PARTIAL_WARNING if partial else "",
        )

    def xǁSecurityPostureServiceǁbuild_report__mutmut_13(
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
        overall = compute_overall_score(None)

        return SecurityPostureReport(
            overall_score_pct=overall,
            categories=categories,
            remediation_order=_remediation_order(categories),
            trend=classify_trend(overall, previous_score_pct),
            previous_score_pct=previous_score_pct,
            partial=partial,
            warning=_PARTIAL_WARNING if partial else "",
        )

    def xǁSecurityPostureServiceǁbuild_report__mutmut_14(
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
            overall_score_pct=None,
            categories=categories,
            remediation_order=_remediation_order(categories),
            trend=classify_trend(overall, previous_score_pct),
            previous_score_pct=previous_score_pct,
            partial=partial,
            warning=_PARTIAL_WARNING if partial else "",
        )

    def xǁSecurityPostureServiceǁbuild_report__mutmut_15(
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
            categories=None,
            remediation_order=_remediation_order(categories),
            trend=classify_trend(overall, previous_score_pct),
            previous_score_pct=previous_score_pct,
            partial=partial,
            warning=_PARTIAL_WARNING if partial else "",
        )

    def xǁSecurityPostureServiceǁbuild_report__mutmut_16(
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
            remediation_order=None,
            trend=classify_trend(overall, previous_score_pct),
            previous_score_pct=previous_score_pct,
            partial=partial,
            warning=_PARTIAL_WARNING if partial else "",
        )

    def xǁSecurityPostureServiceǁbuild_report__mutmut_17(
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
            trend=None,
            previous_score_pct=previous_score_pct,
            partial=partial,
            warning=_PARTIAL_WARNING if partial else "",
        )

    def xǁSecurityPostureServiceǁbuild_report__mutmut_18(
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
            previous_score_pct=None,
            partial=partial,
            warning=_PARTIAL_WARNING if partial else "",
        )

    def xǁSecurityPostureServiceǁbuild_report__mutmut_19(
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
            partial=None,
            warning=_PARTIAL_WARNING if partial else "",
        )

    def xǁSecurityPostureServiceǁbuild_report__mutmut_20(
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
            warning=None,
        )

    def xǁSecurityPostureServiceǁbuild_report__mutmut_21(
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
            categories=categories,
            remediation_order=_remediation_order(categories),
            trend=classify_trend(overall, previous_score_pct),
            previous_score_pct=previous_score_pct,
            partial=partial,
            warning=_PARTIAL_WARNING if partial else "",
        )

    def xǁSecurityPostureServiceǁbuild_report__mutmut_22(
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
            remediation_order=_remediation_order(categories),
            trend=classify_trend(overall, previous_score_pct),
            previous_score_pct=previous_score_pct,
            partial=partial,
            warning=_PARTIAL_WARNING if partial else "",
        )

    def xǁSecurityPostureServiceǁbuild_report__mutmut_23(
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
            trend=classify_trend(overall, previous_score_pct),
            previous_score_pct=previous_score_pct,
            partial=partial,
            warning=_PARTIAL_WARNING if partial else "",
        )

    def xǁSecurityPostureServiceǁbuild_report__mutmut_24(
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
            previous_score_pct=previous_score_pct,
            partial=partial,
            warning=_PARTIAL_WARNING if partial else "",
        )

    def xǁSecurityPostureServiceǁbuild_report__mutmut_25(
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
            partial=partial,
            warning=_PARTIAL_WARNING if partial else "",
        )

    def xǁSecurityPostureServiceǁbuild_report__mutmut_26(
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
            warning=_PARTIAL_WARNING if partial else "",
        )

    def xǁSecurityPostureServiceǁbuild_report__mutmut_27(
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
            )

    def xǁSecurityPostureServiceǁbuild_report__mutmut_28(
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
            remediation_order=_remediation_order(None),
            trend=classify_trend(overall, previous_score_pct),
            previous_score_pct=previous_score_pct,
            partial=partial,
            warning=_PARTIAL_WARNING if partial else "",
        )

    def xǁSecurityPostureServiceǁbuild_report__mutmut_29(
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
            trend=classify_trend(None, previous_score_pct),
            previous_score_pct=previous_score_pct,
            partial=partial,
            warning=_PARTIAL_WARNING if partial else "",
        )

    def xǁSecurityPostureServiceǁbuild_report__mutmut_30(
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
            trend=classify_trend(overall, None),
            previous_score_pct=previous_score_pct,
            partial=partial,
            warning=_PARTIAL_WARNING if partial else "",
        )

    def xǁSecurityPostureServiceǁbuild_report__mutmut_31(
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
            trend=classify_trend(previous_score_pct),
            previous_score_pct=previous_score_pct,
            partial=partial,
            warning=_PARTIAL_WARNING if partial else "",
        )

    def xǁSecurityPostureServiceǁbuild_report__mutmut_32(
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
            trend=classify_trend(overall, ),
            previous_score_pct=previous_score_pct,
            partial=partial,
            warning=_PARTIAL_WARNING if partial else "",
        )

    def xǁSecurityPostureServiceǁbuild_report__mutmut_33(
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
            warning=_PARTIAL_WARNING if partial else "XXXX",
        )

mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['_mutmut_orig'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['xǁSecurityPostureServiceǁbuild_report__mutmut_1'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['xǁSecurityPostureServiceǁbuild_report__mutmut_2'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['xǁSecurityPostureServiceǁbuild_report__mutmut_3'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['xǁSecurityPostureServiceǁbuild_report__mutmut_4'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['xǁSecurityPostureServiceǁbuild_report__mutmut_5'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['xǁSecurityPostureServiceǁbuild_report__mutmut_6'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_6 # type: ignore # mutmut generated
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['xǁSecurityPostureServiceǁbuild_report__mutmut_7'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_7 # type: ignore # mutmut generated
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['xǁSecurityPostureServiceǁbuild_report__mutmut_8'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_8 # type: ignore # mutmut generated
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['xǁSecurityPostureServiceǁbuild_report__mutmut_9'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_9 # type: ignore # mutmut generated
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['xǁSecurityPostureServiceǁbuild_report__mutmut_10'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_10 # type: ignore # mutmut generated
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['xǁSecurityPostureServiceǁbuild_report__mutmut_11'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_11 # type: ignore # mutmut generated
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['xǁSecurityPostureServiceǁbuild_report__mutmut_12'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_12 # type: ignore # mutmut generated
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['xǁSecurityPostureServiceǁbuild_report__mutmut_13'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_13 # type: ignore # mutmut generated
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['xǁSecurityPostureServiceǁbuild_report__mutmut_14'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_14 # type: ignore # mutmut generated
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['xǁSecurityPostureServiceǁbuild_report__mutmut_15'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_15 # type: ignore # mutmut generated
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['xǁSecurityPostureServiceǁbuild_report__mutmut_16'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_16 # type: ignore # mutmut generated
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['xǁSecurityPostureServiceǁbuild_report__mutmut_17'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_17 # type: ignore # mutmut generated
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['xǁSecurityPostureServiceǁbuild_report__mutmut_18'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_18 # type: ignore # mutmut generated
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['xǁSecurityPostureServiceǁbuild_report__mutmut_19'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_19 # type: ignore # mutmut generated
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['xǁSecurityPostureServiceǁbuild_report__mutmut_20'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_20 # type: ignore # mutmut generated
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['xǁSecurityPostureServiceǁbuild_report__mutmut_21'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_21 # type: ignore # mutmut generated
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['xǁSecurityPostureServiceǁbuild_report__mutmut_22'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_22 # type: ignore # mutmut generated
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['xǁSecurityPostureServiceǁbuild_report__mutmut_23'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_23 # type: ignore # mutmut generated
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['xǁSecurityPostureServiceǁbuild_report__mutmut_24'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_24 # type: ignore # mutmut generated
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['xǁSecurityPostureServiceǁbuild_report__mutmut_25'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_25 # type: ignore # mutmut generated
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['xǁSecurityPostureServiceǁbuild_report__mutmut_26'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_26 # type: ignore # mutmut generated
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['xǁSecurityPostureServiceǁbuild_report__mutmut_27'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_27 # type: ignore # mutmut generated
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['xǁSecurityPostureServiceǁbuild_report__mutmut_28'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_28 # type: ignore # mutmut generated
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['xǁSecurityPostureServiceǁbuild_report__mutmut_29'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_29 # type: ignore # mutmut generated
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['xǁSecurityPostureServiceǁbuild_report__mutmut_30'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_30 # type: ignore # mutmut generated
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['xǁSecurityPostureServiceǁbuild_report__mutmut_31'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_31 # type: ignore # mutmut generated
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['xǁSecurityPostureServiceǁbuild_report__mutmut_32'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_32 # type: ignore # mutmut generated
mutants_xǁSecurityPostureServiceǁbuild_report__mutmut['xǁSecurityPostureServiceǁbuild_report__mutmut_33'] = SecurityPostureService.xǁSecurityPostureServiceǁbuild_report__mutmut_33 # type: ignore # mutmut generated
mutants_x__remediation_order__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__remediation_order__mutmut)
def _remediation_order(categories: list[CategoryScore]) -> list[WorkloadCompliance]:
    findings: list[WorkloadCompliance] = []
    for category in categories:
        findings.extend(category.non_compliant_workloads)
    return sorted(findings, key=lambda finding: finding.remediation_priority)


def x__remediation_order__mutmut_orig(categories: list[CategoryScore]) -> list[WorkloadCompliance]:
    findings: list[WorkloadCompliance] = []
    for category in categories:
        findings.extend(category.non_compliant_workloads)
    return sorted(findings, key=lambda finding: finding.remediation_priority)


def x__remediation_order__mutmut_1(categories: list[CategoryScore]) -> list[WorkloadCompliance]:
    findings: list[WorkloadCompliance] = None
    for category in categories:
        findings.extend(category.non_compliant_workloads)
    return sorted(findings, key=lambda finding: finding.remediation_priority)


def x__remediation_order__mutmut_2(categories: list[CategoryScore]) -> list[WorkloadCompliance]:
    findings: list[WorkloadCompliance] = []
    for category in categories:
        findings.extend(None)
    return sorted(findings, key=lambda finding: finding.remediation_priority)


def x__remediation_order__mutmut_3(categories: list[CategoryScore]) -> list[WorkloadCompliance]:
    findings: list[WorkloadCompliance] = []
    for category in categories:
        findings.extend(category.non_compliant_workloads)
    return sorted(None, key=lambda finding: finding.remediation_priority)


def x__remediation_order__mutmut_4(categories: list[CategoryScore]) -> list[WorkloadCompliance]:
    findings: list[WorkloadCompliance] = []
    for category in categories:
        findings.extend(category.non_compliant_workloads)
    return sorted(findings, key=None)


def x__remediation_order__mutmut_5(categories: list[CategoryScore]) -> list[WorkloadCompliance]:
    findings: list[WorkloadCompliance] = []
    for category in categories:
        findings.extend(category.non_compliant_workloads)
    return sorted(key=lambda finding: finding.remediation_priority)


def x__remediation_order__mutmut_6(categories: list[CategoryScore]) -> list[WorkloadCompliance]:
    findings: list[WorkloadCompliance] = []
    for category in categories:
        findings.extend(category.non_compliant_workloads)
    return sorted(findings, )


def x__remediation_order__mutmut_7(categories: list[CategoryScore]) -> list[WorkloadCompliance]:
    findings: list[WorkloadCompliance] = []
    for category in categories:
        findings.extend(category.non_compliant_workloads)
    return sorted(findings, key=lambda finding: None)

mutants_x__remediation_order__mutmut['_mutmut_orig'] = x__remediation_order__mutmut_orig # type: ignore # mutmut generated
mutants_x__remediation_order__mutmut['x__remediation_order__mutmut_1'] = x__remediation_order__mutmut_1 # type: ignore # mutmut generated
mutants_x__remediation_order__mutmut['x__remediation_order__mutmut_2'] = x__remediation_order__mutmut_2 # type: ignore # mutmut generated
mutants_x__remediation_order__mutmut['x__remediation_order__mutmut_3'] = x__remediation_order__mutmut_3 # type: ignore # mutmut generated
mutants_x__remediation_order__mutmut['x__remediation_order__mutmut_4'] = x__remediation_order__mutmut_4 # type: ignore # mutmut generated
mutants_x__remediation_order__mutmut['x__remediation_order__mutmut_5'] = x__remediation_order__mutmut_5 # type: ignore # mutmut generated
mutants_x__remediation_order__mutmut['x__remediation_order__mutmut_6'] = x__remediation_order__mutmut_6 # type: ignore # mutmut generated
mutants_x__remediation_order__mutmut['x__remediation_order__mutmut_7'] = x__remediation_order__mutmut_7 # type: ignore # mutmut generated
