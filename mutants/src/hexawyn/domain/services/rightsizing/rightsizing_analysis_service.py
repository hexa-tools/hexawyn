from __future__ import annotations

from hexawyn.domain.models.rightsizing import (
    RightsizingRecommendation,
    RightsizingReport,
    RightsizingType,
)

# Detection thresholds (from ticket)
_OVER_CPU_THRESHOLD = 0.30
_OVER_RAM_THRESHOLD = 0.40
_UNDER_RAM_THRESHOLD = 0.85
_MINIMUM_SAVINGS_USD = 5.0

# Headroom added to recommendations
_OVER_HEADROOM = 1.3
_UNDER_HEADROOM = 2.0
_MIN_CPU_CORES = 0.1
_MIN_MEMORY_MI = 128.0

# Cloud pricing constants (USD — generic on-demand)
_CPU_COST_PER_CORE_MONTH = 21.6  # ~$0.030/vCPU-hour × 720h
_MEM_COST_PER_GIB_MONTH = 2.88  # ~$0.004/GiB-hour × 720h

# Priority thresholds (absolute USD savings per month)
_PRIORITY_HIGH_USD = 50.0
_PRIORITY_MEDIUM_USD = 20.0


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut: MutantDict = {}  # type: ignore


class RightsizingAnalysisService:
    """Pure domain service — no infra deps, no try/catch."""

    @_mutmut_mutated(mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut)
    def analyze(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped += 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(recommendations, key=lambda r: r.monthly_savings_usd, reverse=True)[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 0)

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=skipped,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_orig(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped += 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(recommendations, key=lambda r: r.monthly_savings_usd, reverse=True)[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 0)

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=skipped,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_1(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = None
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped += 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(recommendations, key=lambda r: r.monthly_savings_usd, reverse=True)[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 0)

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=skipped,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_2(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = None

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped += 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(recommendations, key=lambda r: r.monthly_savings_usd, reverse=True)[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 0)

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=skipped,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_3(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 1

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped += 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(recommendations, key=lambda r: r.monthly_savings_usd, reverse=True)[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 0)

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=skipped,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_4(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = None
            if rec is None:
                skipped += 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(recommendations, key=lambda r: r.monthly_savings_usd, reverse=True)[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 0)

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=skipped,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_5(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(None)
            if rec is None:
                skipped += 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(recommendations, key=lambda r: r.monthly_savings_usd, reverse=True)[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 0)

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=skipped,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_6(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is not None:
                skipped += 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(recommendations, key=lambda r: r.monthly_savings_usd, reverse=True)[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 0)

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=skipped,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_7(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped = 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(recommendations, key=lambda r: r.monthly_savings_usd, reverse=True)[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 0)

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=skipped,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_8(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped -= 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(recommendations, key=lambda r: r.monthly_savings_usd, reverse=True)[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 0)

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=skipped,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_9(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped += 2
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(recommendations, key=lambda r: r.monthly_savings_usd, reverse=True)[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 0)

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=skipped,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_10(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped += 1
                break
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(recommendations, key=lambda r: r.monthly_savings_usd, reverse=True)[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 0)

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=skipped,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_11(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped += 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED or rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(recommendations, key=lambda r: r.monthly_savings_usd, reverse=True)[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 0)

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=skipped,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_12(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped += 1
                continue
            if (
                rec.rightsizing_type != RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(recommendations, key=lambda r: r.monthly_savings_usd, reverse=True)[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 0)

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=skipped,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_13(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped += 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd <= _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(recommendations, key=lambda r: r.monthly_savings_usd, reverse=True)[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 0)

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=skipped,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_14(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped += 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                break
            recommendations.append(rec)

        ranked = sorted(recommendations, key=lambda r: r.monthly_savings_usd, reverse=True)[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 0)

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=skipped,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_15(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped += 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(None)

        ranked = sorted(recommendations, key=lambda r: r.monthly_savings_usd, reverse=True)[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 0)

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=skipped,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_16(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped += 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = None
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 0)

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=skipped,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_17(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped += 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(None, key=lambda r: r.monthly_savings_usd, reverse=True)[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 0)

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=skipped,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_18(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped += 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(recommendations, key=None, reverse=True)[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 0)

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=skipped,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_19(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped += 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(recommendations, key=lambda r: r.monthly_savings_usd, reverse=None)[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 0)

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=skipped,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_20(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped += 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(key=lambda r: r.monthly_savings_usd, reverse=True)[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 0)

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=skipped,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_21(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped += 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(recommendations, reverse=True)[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 0)

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=skipped,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_22(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped += 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(recommendations, key=lambda r: r.monthly_savings_usd, )[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 0)

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=skipped,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_23(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped += 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(recommendations, key=lambda r: None, reverse=True)[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 0)

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=skipped,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_24(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped += 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(recommendations, key=lambda r: r.monthly_savings_usd, reverse=False)[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 0)

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=skipped,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_25(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped += 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(recommendations, key=lambda r: r.monthly_savings_usd, reverse=True)[:top_n]
        total_savings = None

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=skipped,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_26(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped += 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(recommendations, key=lambda r: r.monthly_savings_usd, reverse=True)[:top_n]
        total_savings = sum(None)

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=skipped,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_27(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped += 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(recommendations, key=lambda r: r.monthly_savings_usd, reverse=True)[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd >= 0)

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=skipped,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_28(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped += 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(recommendations, key=lambda r: r.monthly_savings_usd, reverse=True)[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 1)

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=skipped,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_29(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped += 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(recommendations, key=lambda r: r.monthly_savings_usd, reverse=True)[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 0)

        return RightsizingReport(
            recommendations=None,
            skipped_count=skipped,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_30(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped += 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(recommendations, key=lambda r: r.monthly_savings_usd, reverse=True)[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 0)

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=None,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_31(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped += 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(recommendations, key=lambda r: r.monthly_savings_usd, reverse=True)[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 0)

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=skipped,
            total_monthly_savings_usd=None,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_32(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped += 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(recommendations, key=lambda r: r.monthly_savings_usd, reverse=True)[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 0)

        return RightsizingReport(
            skipped_count=skipped,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_33(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped += 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(recommendations, key=lambda r: r.monthly_savings_usd, reverse=True)[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 0)

        return RightsizingReport(
            recommendations=ranked,
            total_monthly_savings_usd=total_savings,
        )

    def xǁRightsizingAnalysisServiceǁanalyze__mutmut_34(
        self,
        raw_data: list[dict[str, object]],
        top_n: int,
    ) -> RightsizingReport:
        recommendations: list[RightsizingRecommendation] = []
        skipped = 0

        for item in raw_data:
            rec = _analyze_workload(item)
            if rec is None:
                skipped += 1
                continue
            if (
                rec.rightsizing_type == RightsizingType.OVER_PROVISIONED
                and rec.monthly_savings_usd < _MINIMUM_SAVINGS_USD
            ):
                continue
            recommendations.append(rec)

        ranked = sorted(recommendations, key=lambda r: r.monthly_savings_usd, reverse=True)[:top_n]
        total_savings = sum(r.monthly_savings_usd for r in ranked if r.monthly_savings_usd > 0)

        return RightsizingReport(
            recommendations=ranked,
            skipped_count=skipped,
            )

mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['_mutmut_orig'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_1'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_2'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_3'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_4'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_5'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_6'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_7'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_8'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_9'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_10'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_11'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_12'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_12 # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_13'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_13 # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_14'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_14 # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_15'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_15 # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_16'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_16 # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_17'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_17 # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_18'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_18 # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_19'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_19 # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_20'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_20 # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_21'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_21 # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_22'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_22 # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_23'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_23 # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_24'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_24 # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_25'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_25 # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_26'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_26 # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_27'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_27 # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_28'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_28 # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_29'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_29 # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_30'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_30 # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_31'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_31 # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_32'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_32 # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_33'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_33 # type: ignore # mutmut generated
mutants_xǁRightsizingAnalysisServiceǁanalyze__mutmut['xǁRightsizingAnalysisServiceǁanalyze__mutmut_34'] = RightsizingAnalysisService.xǁRightsizingAnalysisServiceǁanalyze__mutmut_34 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__analyze_workload__mutmut)
def _analyze_workload(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_orig(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_1(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = None
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_2(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(None)
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_3(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get(None))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_4(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("XXcpu_actual_coresXX"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_5(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("CPU_ACTUAL_CORES"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_6(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = None

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_7(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(None)

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_8(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get(None))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_9(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("XXmemory_actual_miXX"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_10(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("MEMORY_ACTUAL_MI"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_11(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None or mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_12(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is not None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_13(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is not None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_14(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = None  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_15(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(None)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_16(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") and 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_17(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get(None) or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_18(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("XXcpu_requested_coresXX") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_19(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("CPU_REQUESTED_CORES") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_20(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 1.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_21(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = None  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_22(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(None)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_23(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") and 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_24(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get(None) or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_25(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("XXmemory_requested_miXX") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_26(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("MEMORY_REQUESTED_MI") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_27(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 1.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_28(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = None
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_29(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(None, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_30(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, None, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_31(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, None, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_32(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, None)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_33(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_34(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_35(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_36(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, )
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_37(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type != RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_38(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = None
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_39(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(None, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_40(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, None)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_41(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_42(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, )
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_43(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = None
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_44(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(None, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_45(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, None, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_46(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, None)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_47(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_48(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_49(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, )
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_50(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = None
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_51(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(None, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_52(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, None, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_53(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, None, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_54(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, None)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_55(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_56(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_57(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_58(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, )
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_59(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = None

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_60(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(None, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_61(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, None, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_62(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, None, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_63(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, None, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_64(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, None)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_65(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_66(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_67(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_68(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_69(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, )

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_70(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=None,
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_71(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=None,
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_72(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=None,
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_73(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=None,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_74(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=None,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_75(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=None,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_76(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=None,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_77(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=None,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_78(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=None,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_79(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=None,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_80(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=None,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_81(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=None,
    )


def x__analyze_workload__mutmut_82(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_83(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_84(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_85(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_86(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_87(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_88(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_89(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_90(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_91(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_92(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_93(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        )


def x__analyze_workload__mutmut_94(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(None),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_95(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get(None, "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_96(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", None)),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_97(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_98(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", )),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_99(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("XXresource_nameXX", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_100(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("RESOURCE_NAME", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_101(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "XXXX")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_102(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(None),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_103(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get(None, "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_104(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", None)),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_105(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_106(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", )),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_107(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("XXnamespaceXX", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_108(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("NAMESPACE", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_109(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "XXXX")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_110(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(None),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_111(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get(None, "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_112(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", None)),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_113(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_114(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", )),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_115(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("XXkindXX", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_116(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("KIND", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_117(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "XXDeploymentXX")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_118(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_119(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "DEPLOYMENT")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(savings),
    )


def x__analyze_workload__mutmut_120(item: dict[str, object]) -> RightsizingRecommendation | None:
    cpu_actual = _as_float_or_none(item.get("cpu_actual_cores"))
    mem_actual = _as_float_or_none(item.get("memory_actual_mi"))

    if cpu_actual is None and mem_actual is None:
        return None

    cpu_req = float(item.get("cpu_requested_cores") or 0.0)  # type: ignore[arg-type]
    mem_req = float(item.get("memory_requested_mi") or 0.0)  # type: ignore[arg-type]

    rightsizing_type, reason = _classify(cpu_req, mem_req, cpu_actual, mem_actual)
    if rightsizing_type == RightsizingType.OPTIMAL:
        return None

    rec_cpu = _recommend_cpu(cpu_req, cpu_actual)
    rec_mem = _recommend_memory(rightsizing_type, mem_req, mem_actual)
    savings = _compute_savings(cpu_req, rec_cpu, mem_req, rec_mem)
    waste_pct = _waste_percentage(rightsizing_type, cpu_req, mem_req, cpu_actual, mem_actual)

    return RightsizingRecommendation(
        resource_name=str(item.get("resource_name", "")),
        namespace=str(item.get("namespace", "")),
        kind=str(item.get("kind", "Deployment")),
        rightsizing_type=rightsizing_type,
        current_cpu_cores=cpu_req,
        recommended_cpu_cores=rec_cpu,
        current_memory_mi=mem_req,
        recommended_memory_mi=rec_mem,
        monthly_savings_usd=savings,
        waste_percentage=waste_pct,
        reason=reason,
        priority=_priority(None),
    )

mutants_x__analyze_workload__mutmut['_mutmut_orig'] = x__analyze_workload__mutmut_orig # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_1'] = x__analyze_workload__mutmut_1 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_2'] = x__analyze_workload__mutmut_2 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_3'] = x__analyze_workload__mutmut_3 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_4'] = x__analyze_workload__mutmut_4 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_5'] = x__analyze_workload__mutmut_5 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_6'] = x__analyze_workload__mutmut_6 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_7'] = x__analyze_workload__mutmut_7 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_8'] = x__analyze_workload__mutmut_8 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_9'] = x__analyze_workload__mutmut_9 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_10'] = x__analyze_workload__mutmut_10 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_11'] = x__analyze_workload__mutmut_11 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_12'] = x__analyze_workload__mutmut_12 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_13'] = x__analyze_workload__mutmut_13 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_14'] = x__analyze_workload__mutmut_14 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_15'] = x__analyze_workload__mutmut_15 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_16'] = x__analyze_workload__mutmut_16 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_17'] = x__analyze_workload__mutmut_17 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_18'] = x__analyze_workload__mutmut_18 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_19'] = x__analyze_workload__mutmut_19 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_20'] = x__analyze_workload__mutmut_20 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_21'] = x__analyze_workload__mutmut_21 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_22'] = x__analyze_workload__mutmut_22 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_23'] = x__analyze_workload__mutmut_23 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_24'] = x__analyze_workload__mutmut_24 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_25'] = x__analyze_workload__mutmut_25 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_26'] = x__analyze_workload__mutmut_26 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_27'] = x__analyze_workload__mutmut_27 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_28'] = x__analyze_workload__mutmut_28 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_29'] = x__analyze_workload__mutmut_29 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_30'] = x__analyze_workload__mutmut_30 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_31'] = x__analyze_workload__mutmut_31 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_32'] = x__analyze_workload__mutmut_32 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_33'] = x__analyze_workload__mutmut_33 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_34'] = x__analyze_workload__mutmut_34 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_35'] = x__analyze_workload__mutmut_35 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_36'] = x__analyze_workload__mutmut_36 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_37'] = x__analyze_workload__mutmut_37 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_38'] = x__analyze_workload__mutmut_38 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_39'] = x__analyze_workload__mutmut_39 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_40'] = x__analyze_workload__mutmut_40 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_41'] = x__analyze_workload__mutmut_41 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_42'] = x__analyze_workload__mutmut_42 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_43'] = x__analyze_workload__mutmut_43 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_44'] = x__analyze_workload__mutmut_44 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_45'] = x__analyze_workload__mutmut_45 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_46'] = x__analyze_workload__mutmut_46 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_47'] = x__analyze_workload__mutmut_47 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_48'] = x__analyze_workload__mutmut_48 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_49'] = x__analyze_workload__mutmut_49 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_50'] = x__analyze_workload__mutmut_50 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_51'] = x__analyze_workload__mutmut_51 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_52'] = x__analyze_workload__mutmut_52 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_53'] = x__analyze_workload__mutmut_53 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_54'] = x__analyze_workload__mutmut_54 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_55'] = x__analyze_workload__mutmut_55 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_56'] = x__analyze_workload__mutmut_56 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_57'] = x__analyze_workload__mutmut_57 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_58'] = x__analyze_workload__mutmut_58 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_59'] = x__analyze_workload__mutmut_59 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_60'] = x__analyze_workload__mutmut_60 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_61'] = x__analyze_workload__mutmut_61 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_62'] = x__analyze_workload__mutmut_62 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_63'] = x__analyze_workload__mutmut_63 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_64'] = x__analyze_workload__mutmut_64 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_65'] = x__analyze_workload__mutmut_65 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_66'] = x__analyze_workload__mutmut_66 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_67'] = x__analyze_workload__mutmut_67 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_68'] = x__analyze_workload__mutmut_68 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_69'] = x__analyze_workload__mutmut_69 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_70'] = x__analyze_workload__mutmut_70 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_71'] = x__analyze_workload__mutmut_71 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_72'] = x__analyze_workload__mutmut_72 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_73'] = x__analyze_workload__mutmut_73 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_74'] = x__analyze_workload__mutmut_74 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_75'] = x__analyze_workload__mutmut_75 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_76'] = x__analyze_workload__mutmut_76 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_77'] = x__analyze_workload__mutmut_77 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_78'] = x__analyze_workload__mutmut_78 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_79'] = x__analyze_workload__mutmut_79 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_80'] = x__analyze_workload__mutmut_80 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_81'] = x__analyze_workload__mutmut_81 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_82'] = x__analyze_workload__mutmut_82 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_83'] = x__analyze_workload__mutmut_83 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_84'] = x__analyze_workload__mutmut_84 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_85'] = x__analyze_workload__mutmut_85 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_86'] = x__analyze_workload__mutmut_86 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_87'] = x__analyze_workload__mutmut_87 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_88'] = x__analyze_workload__mutmut_88 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_89'] = x__analyze_workload__mutmut_89 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_90'] = x__analyze_workload__mutmut_90 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_91'] = x__analyze_workload__mutmut_91 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_92'] = x__analyze_workload__mutmut_92 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_93'] = x__analyze_workload__mutmut_93 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_94'] = x__analyze_workload__mutmut_94 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_95'] = x__analyze_workload__mutmut_95 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_96'] = x__analyze_workload__mutmut_96 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_97'] = x__analyze_workload__mutmut_97 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_98'] = x__analyze_workload__mutmut_98 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_99'] = x__analyze_workload__mutmut_99 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_100'] = x__analyze_workload__mutmut_100 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_101'] = x__analyze_workload__mutmut_101 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_102'] = x__analyze_workload__mutmut_102 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_103'] = x__analyze_workload__mutmut_103 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_104'] = x__analyze_workload__mutmut_104 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_105'] = x__analyze_workload__mutmut_105 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_106'] = x__analyze_workload__mutmut_106 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_107'] = x__analyze_workload__mutmut_107 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_108'] = x__analyze_workload__mutmut_108 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_109'] = x__analyze_workload__mutmut_109 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_110'] = x__analyze_workload__mutmut_110 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_111'] = x__analyze_workload__mutmut_111 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_112'] = x__analyze_workload__mutmut_112 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_113'] = x__analyze_workload__mutmut_113 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_114'] = x__analyze_workload__mutmut_114 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_115'] = x__analyze_workload__mutmut_115 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_116'] = x__analyze_workload__mutmut_116 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_117'] = x__analyze_workload__mutmut_117 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_118'] = x__analyze_workload__mutmut_118 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_119'] = x__analyze_workload__mutmut_119 # type: ignore # mutmut generated
mutants_x__analyze_workload__mutmut['x__analyze_workload__mutmut_120'] = x__analyze_workload__mutmut_120 # type: ignore # mutmut generated
mutants_x__classify__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__classify__mutmut)
def _classify(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_orig(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_1(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 or mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_2(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None or mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_3(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_4(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req >= 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_5(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 1 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_6(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual * mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_7(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req >= _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_8(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = None
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_9(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(None, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_10(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, None)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_11(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_12(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, )
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_13(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req / 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_14(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual * mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_15(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 101, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_16(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 2)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_17(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = None
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_18(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None or cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_19(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 or cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_20(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req >= 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_21(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 1 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_22(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_23(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual * cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_24(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req <= _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_25(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = None

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_26(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None or mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_27(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 or mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_28(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req >= 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_29(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 1 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_30(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_31(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual * mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_32(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req <= _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_33(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu and over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_34(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = None
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_35(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu or cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_36(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_37(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(None)
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_38(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(None, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_39(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, None)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_40(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_41(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, )}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_42(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req / 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_43(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual * cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_44(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 101, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_45(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 2)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_46(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem or mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_47(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_48(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(None)
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_49(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(None, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_50(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, None)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_51(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_52(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, )}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_53(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req / 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_54(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual * mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_55(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 101, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_56(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 2)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_57(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(None)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_58(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, "XX · XX".join(parts)

    return RightsizingType.OPTIMAL, ""


def x__classify__mutmut_59(
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> tuple[RightsizingType, str]:
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req > _UNDER_RAM_THRESHOLD:
        pct = round(mem_actual / mem_req * 100, 1)
        return RightsizingType.UNDER_PROVISIONED, f"RAM usage {pct}% of requests — OOM risk"

    over_cpu = cpu_req > 0 and cpu_actual is not None and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD
    over_mem = mem_req > 0 and mem_actual is not None and mem_actual / mem_req < _OVER_RAM_THRESHOLD

    if over_cpu or over_mem:
        parts: list[str] = []
        if over_cpu and cpu_actual is not None:
            parts.append(f"CPU usage {round(cpu_actual / cpu_req * 100, 1)}% of requests")
        if over_mem and mem_actual is not None:
            parts.append(f"RAM usage {round(mem_actual / mem_req * 100, 1)}% of requests")
        return RightsizingType.OVER_PROVISIONED, " · ".join(parts)

    return RightsizingType.OPTIMAL, "XXXX"

mutants_x__classify__mutmut['_mutmut_orig'] = x__classify__mutmut_orig # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_1'] = x__classify__mutmut_1 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_2'] = x__classify__mutmut_2 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_3'] = x__classify__mutmut_3 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_4'] = x__classify__mutmut_4 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_5'] = x__classify__mutmut_5 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_6'] = x__classify__mutmut_6 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_7'] = x__classify__mutmut_7 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_8'] = x__classify__mutmut_8 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_9'] = x__classify__mutmut_9 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_10'] = x__classify__mutmut_10 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_11'] = x__classify__mutmut_11 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_12'] = x__classify__mutmut_12 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_13'] = x__classify__mutmut_13 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_14'] = x__classify__mutmut_14 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_15'] = x__classify__mutmut_15 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_16'] = x__classify__mutmut_16 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_17'] = x__classify__mutmut_17 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_18'] = x__classify__mutmut_18 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_19'] = x__classify__mutmut_19 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_20'] = x__classify__mutmut_20 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_21'] = x__classify__mutmut_21 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_22'] = x__classify__mutmut_22 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_23'] = x__classify__mutmut_23 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_24'] = x__classify__mutmut_24 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_25'] = x__classify__mutmut_25 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_26'] = x__classify__mutmut_26 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_27'] = x__classify__mutmut_27 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_28'] = x__classify__mutmut_28 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_29'] = x__classify__mutmut_29 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_30'] = x__classify__mutmut_30 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_31'] = x__classify__mutmut_31 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_32'] = x__classify__mutmut_32 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_33'] = x__classify__mutmut_33 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_34'] = x__classify__mutmut_34 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_35'] = x__classify__mutmut_35 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_36'] = x__classify__mutmut_36 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_37'] = x__classify__mutmut_37 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_38'] = x__classify__mutmut_38 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_39'] = x__classify__mutmut_39 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_40'] = x__classify__mutmut_40 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_41'] = x__classify__mutmut_41 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_42'] = x__classify__mutmut_42 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_43'] = x__classify__mutmut_43 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_44'] = x__classify__mutmut_44 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_45'] = x__classify__mutmut_45 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_46'] = x__classify__mutmut_46 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_47'] = x__classify__mutmut_47 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_48'] = x__classify__mutmut_48 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_49'] = x__classify__mutmut_49 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_50'] = x__classify__mutmut_50 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_51'] = x__classify__mutmut_51 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_52'] = x__classify__mutmut_52 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_53'] = x__classify__mutmut_53 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_54'] = x__classify__mutmut_54 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_55'] = x__classify__mutmut_55 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_56'] = x__classify__mutmut_56 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_57'] = x__classify__mutmut_57 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_58'] = x__classify__mutmut_58 # type: ignore # mutmut generated
mutants_x__classify__mutmut['x__classify__mutmut_59'] = x__classify__mutmut_59 # type: ignore # mutmut generated
mutants_x__recommend_cpu__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__recommend_cpu__mutmut)
def _recommend_cpu(cpu_req: float, cpu_actual: float | None) -> float:
    """Only reduce CPU if it is genuinely over-provisioned."""
    if cpu_actual is not None and cpu_req > 0 and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD:
        return max(cpu_actual * _OVER_HEADROOM, _MIN_CPU_CORES)
    return cpu_req


def x__recommend_cpu__mutmut_orig(cpu_req: float, cpu_actual: float | None) -> float:
    """Only reduce CPU if it is genuinely over-provisioned."""
    if cpu_actual is not None and cpu_req > 0 and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD:
        return max(cpu_actual * _OVER_HEADROOM, _MIN_CPU_CORES)
    return cpu_req


def x__recommend_cpu__mutmut_1(cpu_req: float, cpu_actual: float | None) -> float:
    """Only reduce CPU if it is genuinely over-provisioned."""
    if cpu_actual is not None and cpu_req > 0 or cpu_actual / cpu_req < _OVER_CPU_THRESHOLD:
        return max(cpu_actual * _OVER_HEADROOM, _MIN_CPU_CORES)
    return cpu_req


def x__recommend_cpu__mutmut_2(cpu_req: float, cpu_actual: float | None) -> float:
    """Only reduce CPU if it is genuinely over-provisioned."""
    if cpu_actual is not None or cpu_req > 0 and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD:
        return max(cpu_actual * _OVER_HEADROOM, _MIN_CPU_CORES)
    return cpu_req


def x__recommend_cpu__mutmut_3(cpu_req: float, cpu_actual: float | None) -> float:
    """Only reduce CPU if it is genuinely over-provisioned."""
    if cpu_actual is None and cpu_req > 0 and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD:
        return max(cpu_actual * _OVER_HEADROOM, _MIN_CPU_CORES)
    return cpu_req


def x__recommend_cpu__mutmut_4(cpu_req: float, cpu_actual: float | None) -> float:
    """Only reduce CPU if it is genuinely over-provisioned."""
    if cpu_actual is not None and cpu_req >= 0 and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD:
        return max(cpu_actual * _OVER_HEADROOM, _MIN_CPU_CORES)
    return cpu_req


def x__recommend_cpu__mutmut_5(cpu_req: float, cpu_actual: float | None) -> float:
    """Only reduce CPU if it is genuinely over-provisioned."""
    if cpu_actual is not None and cpu_req > 1 and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD:
        return max(cpu_actual * _OVER_HEADROOM, _MIN_CPU_CORES)
    return cpu_req


def x__recommend_cpu__mutmut_6(cpu_req: float, cpu_actual: float | None) -> float:
    """Only reduce CPU if it is genuinely over-provisioned."""
    if cpu_actual is not None and cpu_req > 0 and cpu_actual * cpu_req < _OVER_CPU_THRESHOLD:
        return max(cpu_actual * _OVER_HEADROOM, _MIN_CPU_CORES)
    return cpu_req


def x__recommend_cpu__mutmut_7(cpu_req: float, cpu_actual: float | None) -> float:
    """Only reduce CPU if it is genuinely over-provisioned."""
    if cpu_actual is not None and cpu_req > 0 and cpu_actual / cpu_req <= _OVER_CPU_THRESHOLD:
        return max(cpu_actual * _OVER_HEADROOM, _MIN_CPU_CORES)
    return cpu_req


def x__recommend_cpu__mutmut_8(cpu_req: float, cpu_actual: float | None) -> float:
    """Only reduce CPU if it is genuinely over-provisioned."""
    if cpu_actual is not None and cpu_req > 0 and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD:
        return max(None, _MIN_CPU_CORES)
    return cpu_req


def x__recommend_cpu__mutmut_9(cpu_req: float, cpu_actual: float | None) -> float:
    """Only reduce CPU if it is genuinely over-provisioned."""
    if cpu_actual is not None and cpu_req > 0 and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD:
        return max(cpu_actual * _OVER_HEADROOM, None)
    return cpu_req


def x__recommend_cpu__mutmut_10(cpu_req: float, cpu_actual: float | None) -> float:
    """Only reduce CPU if it is genuinely over-provisioned."""
    if cpu_actual is not None and cpu_req > 0 and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD:
        return max(_MIN_CPU_CORES)
    return cpu_req


def x__recommend_cpu__mutmut_11(cpu_req: float, cpu_actual: float | None) -> float:
    """Only reduce CPU if it is genuinely over-provisioned."""
    if cpu_actual is not None and cpu_req > 0 and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD:
        return max(cpu_actual * _OVER_HEADROOM, )
    return cpu_req


def x__recommend_cpu__mutmut_12(cpu_req: float, cpu_actual: float | None) -> float:
    """Only reduce CPU if it is genuinely over-provisioned."""
    if cpu_actual is not None and cpu_req > 0 and cpu_actual / cpu_req < _OVER_CPU_THRESHOLD:
        return max(cpu_actual / _OVER_HEADROOM, _MIN_CPU_CORES)
    return cpu_req

mutants_x__recommend_cpu__mutmut['_mutmut_orig'] = x__recommend_cpu__mutmut_orig # type: ignore # mutmut generated
mutants_x__recommend_cpu__mutmut['x__recommend_cpu__mutmut_1'] = x__recommend_cpu__mutmut_1 # type: ignore # mutmut generated
mutants_x__recommend_cpu__mutmut['x__recommend_cpu__mutmut_2'] = x__recommend_cpu__mutmut_2 # type: ignore # mutmut generated
mutants_x__recommend_cpu__mutmut['x__recommend_cpu__mutmut_3'] = x__recommend_cpu__mutmut_3 # type: ignore # mutmut generated
mutants_x__recommend_cpu__mutmut['x__recommend_cpu__mutmut_4'] = x__recommend_cpu__mutmut_4 # type: ignore # mutmut generated
mutants_x__recommend_cpu__mutmut['x__recommend_cpu__mutmut_5'] = x__recommend_cpu__mutmut_5 # type: ignore # mutmut generated
mutants_x__recommend_cpu__mutmut['x__recommend_cpu__mutmut_6'] = x__recommend_cpu__mutmut_6 # type: ignore # mutmut generated
mutants_x__recommend_cpu__mutmut['x__recommend_cpu__mutmut_7'] = x__recommend_cpu__mutmut_7 # type: ignore # mutmut generated
mutants_x__recommend_cpu__mutmut['x__recommend_cpu__mutmut_8'] = x__recommend_cpu__mutmut_8 # type: ignore # mutmut generated
mutants_x__recommend_cpu__mutmut['x__recommend_cpu__mutmut_9'] = x__recommend_cpu__mutmut_9 # type: ignore # mutmut generated
mutants_x__recommend_cpu__mutmut['x__recommend_cpu__mutmut_10'] = x__recommend_cpu__mutmut_10 # type: ignore # mutmut generated
mutants_x__recommend_cpu__mutmut['x__recommend_cpu__mutmut_11'] = x__recommend_cpu__mutmut_11 # type: ignore # mutmut generated
mutants_x__recommend_cpu__mutmut['x__recommend_cpu__mutmut_12'] = x__recommend_cpu__mutmut_12 # type: ignore # mutmut generated
mutants_x__recommend_memory__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__recommend_memory__mutmut)
def _recommend_memory(
    rtype: RightsizingType,
    mem_req: float,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return mem_req * _UNDER_HEADROOM
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req < _OVER_RAM_THRESHOLD:
        return max(mem_actual * _OVER_HEADROOM, _MIN_MEMORY_MI)
    return mem_req


def x__recommend_memory__mutmut_orig(
    rtype: RightsizingType,
    mem_req: float,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return mem_req * _UNDER_HEADROOM
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req < _OVER_RAM_THRESHOLD:
        return max(mem_actual * _OVER_HEADROOM, _MIN_MEMORY_MI)
    return mem_req


def x__recommend_memory__mutmut_1(
    rtype: RightsizingType,
    mem_req: float,
    mem_actual: float | None,
) -> float:
    if rtype != RightsizingType.UNDER_PROVISIONED:
        return mem_req * _UNDER_HEADROOM
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req < _OVER_RAM_THRESHOLD:
        return max(mem_actual * _OVER_HEADROOM, _MIN_MEMORY_MI)
    return mem_req


def x__recommend_memory__mutmut_2(
    rtype: RightsizingType,
    mem_req: float,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return mem_req / _UNDER_HEADROOM
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req < _OVER_RAM_THRESHOLD:
        return max(mem_actual * _OVER_HEADROOM, _MIN_MEMORY_MI)
    return mem_req


def x__recommend_memory__mutmut_3(
    rtype: RightsizingType,
    mem_req: float,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return mem_req * _UNDER_HEADROOM
    if mem_actual is not None and mem_req > 0 or mem_actual / mem_req < _OVER_RAM_THRESHOLD:
        return max(mem_actual * _OVER_HEADROOM, _MIN_MEMORY_MI)
    return mem_req


def x__recommend_memory__mutmut_4(
    rtype: RightsizingType,
    mem_req: float,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return mem_req * _UNDER_HEADROOM
    if mem_actual is not None or mem_req > 0 and mem_actual / mem_req < _OVER_RAM_THRESHOLD:
        return max(mem_actual * _OVER_HEADROOM, _MIN_MEMORY_MI)
    return mem_req


def x__recommend_memory__mutmut_5(
    rtype: RightsizingType,
    mem_req: float,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return mem_req * _UNDER_HEADROOM
    if mem_actual is None and mem_req > 0 and mem_actual / mem_req < _OVER_RAM_THRESHOLD:
        return max(mem_actual * _OVER_HEADROOM, _MIN_MEMORY_MI)
    return mem_req


def x__recommend_memory__mutmut_6(
    rtype: RightsizingType,
    mem_req: float,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return mem_req * _UNDER_HEADROOM
    if mem_actual is not None and mem_req >= 0 and mem_actual / mem_req < _OVER_RAM_THRESHOLD:
        return max(mem_actual * _OVER_HEADROOM, _MIN_MEMORY_MI)
    return mem_req


def x__recommend_memory__mutmut_7(
    rtype: RightsizingType,
    mem_req: float,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return mem_req * _UNDER_HEADROOM
    if mem_actual is not None and mem_req > 1 and mem_actual / mem_req < _OVER_RAM_THRESHOLD:
        return max(mem_actual * _OVER_HEADROOM, _MIN_MEMORY_MI)
    return mem_req


def x__recommend_memory__mutmut_8(
    rtype: RightsizingType,
    mem_req: float,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return mem_req * _UNDER_HEADROOM
    if mem_actual is not None and mem_req > 0 and mem_actual * mem_req < _OVER_RAM_THRESHOLD:
        return max(mem_actual * _OVER_HEADROOM, _MIN_MEMORY_MI)
    return mem_req


def x__recommend_memory__mutmut_9(
    rtype: RightsizingType,
    mem_req: float,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return mem_req * _UNDER_HEADROOM
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req <= _OVER_RAM_THRESHOLD:
        return max(mem_actual * _OVER_HEADROOM, _MIN_MEMORY_MI)
    return mem_req


def x__recommend_memory__mutmut_10(
    rtype: RightsizingType,
    mem_req: float,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return mem_req * _UNDER_HEADROOM
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req < _OVER_RAM_THRESHOLD:
        return max(None, _MIN_MEMORY_MI)
    return mem_req


def x__recommend_memory__mutmut_11(
    rtype: RightsizingType,
    mem_req: float,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return mem_req * _UNDER_HEADROOM
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req < _OVER_RAM_THRESHOLD:
        return max(mem_actual * _OVER_HEADROOM, None)
    return mem_req


def x__recommend_memory__mutmut_12(
    rtype: RightsizingType,
    mem_req: float,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return mem_req * _UNDER_HEADROOM
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req < _OVER_RAM_THRESHOLD:
        return max(_MIN_MEMORY_MI)
    return mem_req


def x__recommend_memory__mutmut_13(
    rtype: RightsizingType,
    mem_req: float,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return mem_req * _UNDER_HEADROOM
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req < _OVER_RAM_THRESHOLD:
        return max(mem_actual * _OVER_HEADROOM, )
    return mem_req


def x__recommend_memory__mutmut_14(
    rtype: RightsizingType,
    mem_req: float,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return mem_req * _UNDER_HEADROOM
    if mem_actual is not None and mem_req > 0 and mem_actual / mem_req < _OVER_RAM_THRESHOLD:
        return max(mem_actual / _OVER_HEADROOM, _MIN_MEMORY_MI)
    return mem_req

mutants_x__recommend_memory__mutmut['_mutmut_orig'] = x__recommend_memory__mutmut_orig # type: ignore # mutmut generated
mutants_x__recommend_memory__mutmut['x__recommend_memory__mutmut_1'] = x__recommend_memory__mutmut_1 # type: ignore # mutmut generated
mutants_x__recommend_memory__mutmut['x__recommend_memory__mutmut_2'] = x__recommend_memory__mutmut_2 # type: ignore # mutmut generated
mutants_x__recommend_memory__mutmut['x__recommend_memory__mutmut_3'] = x__recommend_memory__mutmut_3 # type: ignore # mutmut generated
mutants_x__recommend_memory__mutmut['x__recommend_memory__mutmut_4'] = x__recommend_memory__mutmut_4 # type: ignore # mutmut generated
mutants_x__recommend_memory__mutmut['x__recommend_memory__mutmut_5'] = x__recommend_memory__mutmut_5 # type: ignore # mutmut generated
mutants_x__recommend_memory__mutmut['x__recommend_memory__mutmut_6'] = x__recommend_memory__mutmut_6 # type: ignore # mutmut generated
mutants_x__recommend_memory__mutmut['x__recommend_memory__mutmut_7'] = x__recommend_memory__mutmut_7 # type: ignore # mutmut generated
mutants_x__recommend_memory__mutmut['x__recommend_memory__mutmut_8'] = x__recommend_memory__mutmut_8 # type: ignore # mutmut generated
mutants_x__recommend_memory__mutmut['x__recommend_memory__mutmut_9'] = x__recommend_memory__mutmut_9 # type: ignore # mutmut generated
mutants_x__recommend_memory__mutmut['x__recommend_memory__mutmut_10'] = x__recommend_memory__mutmut_10 # type: ignore # mutmut generated
mutants_x__recommend_memory__mutmut['x__recommend_memory__mutmut_11'] = x__recommend_memory__mutmut_11 # type: ignore # mutmut generated
mutants_x__recommend_memory__mutmut['x__recommend_memory__mutmut_12'] = x__recommend_memory__mutmut_12 # type: ignore # mutmut generated
mutants_x__recommend_memory__mutmut['x__recommend_memory__mutmut_13'] = x__recommend_memory__mutmut_13 # type: ignore # mutmut generated
mutants_x__recommend_memory__mutmut['x__recommend_memory__mutmut_14'] = x__recommend_memory__mutmut_14 # type: ignore # mutmut generated
mutants_x__compute_savings__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__compute_savings__mutmut)
def _compute_savings(
    cpu_req: float,
    rec_cpu: float,
    mem_req: float,
    rec_mem: float,
) -> float:
    cpu_saved = (cpu_req - rec_cpu) * _CPU_COST_PER_CORE_MONTH
    mem_saved_gib = (mem_req - rec_mem) / 1024.0
    mem_saved = mem_saved_gib * _MEM_COST_PER_GIB_MONTH
    return round(cpu_saved + mem_saved, 2)


def x__compute_savings__mutmut_orig(
    cpu_req: float,
    rec_cpu: float,
    mem_req: float,
    rec_mem: float,
) -> float:
    cpu_saved = (cpu_req - rec_cpu) * _CPU_COST_PER_CORE_MONTH
    mem_saved_gib = (mem_req - rec_mem) / 1024.0
    mem_saved = mem_saved_gib * _MEM_COST_PER_GIB_MONTH
    return round(cpu_saved + mem_saved, 2)


def x__compute_savings__mutmut_1(
    cpu_req: float,
    rec_cpu: float,
    mem_req: float,
    rec_mem: float,
) -> float:
    cpu_saved = None
    mem_saved_gib = (mem_req - rec_mem) / 1024.0
    mem_saved = mem_saved_gib * _MEM_COST_PER_GIB_MONTH
    return round(cpu_saved + mem_saved, 2)


def x__compute_savings__mutmut_2(
    cpu_req: float,
    rec_cpu: float,
    mem_req: float,
    rec_mem: float,
) -> float:
    cpu_saved = (cpu_req - rec_cpu) / _CPU_COST_PER_CORE_MONTH
    mem_saved_gib = (mem_req - rec_mem) / 1024.0
    mem_saved = mem_saved_gib * _MEM_COST_PER_GIB_MONTH
    return round(cpu_saved + mem_saved, 2)


def x__compute_savings__mutmut_3(
    cpu_req: float,
    rec_cpu: float,
    mem_req: float,
    rec_mem: float,
) -> float:
    cpu_saved = (cpu_req + rec_cpu) * _CPU_COST_PER_CORE_MONTH
    mem_saved_gib = (mem_req - rec_mem) / 1024.0
    mem_saved = mem_saved_gib * _MEM_COST_PER_GIB_MONTH
    return round(cpu_saved + mem_saved, 2)


def x__compute_savings__mutmut_4(
    cpu_req: float,
    rec_cpu: float,
    mem_req: float,
    rec_mem: float,
) -> float:
    cpu_saved = (cpu_req - rec_cpu) * _CPU_COST_PER_CORE_MONTH
    mem_saved_gib = None
    mem_saved = mem_saved_gib * _MEM_COST_PER_GIB_MONTH
    return round(cpu_saved + mem_saved, 2)


def x__compute_savings__mutmut_5(
    cpu_req: float,
    rec_cpu: float,
    mem_req: float,
    rec_mem: float,
) -> float:
    cpu_saved = (cpu_req - rec_cpu) * _CPU_COST_PER_CORE_MONTH
    mem_saved_gib = (mem_req - rec_mem) * 1024.0
    mem_saved = mem_saved_gib * _MEM_COST_PER_GIB_MONTH
    return round(cpu_saved + mem_saved, 2)


def x__compute_savings__mutmut_6(
    cpu_req: float,
    rec_cpu: float,
    mem_req: float,
    rec_mem: float,
) -> float:
    cpu_saved = (cpu_req - rec_cpu) * _CPU_COST_PER_CORE_MONTH
    mem_saved_gib = (mem_req + rec_mem) / 1024.0
    mem_saved = mem_saved_gib * _MEM_COST_PER_GIB_MONTH
    return round(cpu_saved + mem_saved, 2)


def x__compute_savings__mutmut_7(
    cpu_req: float,
    rec_cpu: float,
    mem_req: float,
    rec_mem: float,
) -> float:
    cpu_saved = (cpu_req - rec_cpu) * _CPU_COST_PER_CORE_MONTH
    mem_saved_gib = (mem_req - rec_mem) / 1025.0
    mem_saved = mem_saved_gib * _MEM_COST_PER_GIB_MONTH
    return round(cpu_saved + mem_saved, 2)


def x__compute_savings__mutmut_8(
    cpu_req: float,
    rec_cpu: float,
    mem_req: float,
    rec_mem: float,
) -> float:
    cpu_saved = (cpu_req - rec_cpu) * _CPU_COST_PER_CORE_MONTH
    mem_saved_gib = (mem_req - rec_mem) / 1024.0
    mem_saved = None
    return round(cpu_saved + mem_saved, 2)


def x__compute_savings__mutmut_9(
    cpu_req: float,
    rec_cpu: float,
    mem_req: float,
    rec_mem: float,
) -> float:
    cpu_saved = (cpu_req - rec_cpu) * _CPU_COST_PER_CORE_MONTH
    mem_saved_gib = (mem_req - rec_mem) / 1024.0
    mem_saved = mem_saved_gib / _MEM_COST_PER_GIB_MONTH
    return round(cpu_saved + mem_saved, 2)


def x__compute_savings__mutmut_10(
    cpu_req: float,
    rec_cpu: float,
    mem_req: float,
    rec_mem: float,
) -> float:
    cpu_saved = (cpu_req - rec_cpu) * _CPU_COST_PER_CORE_MONTH
    mem_saved_gib = (mem_req - rec_mem) / 1024.0
    mem_saved = mem_saved_gib * _MEM_COST_PER_GIB_MONTH
    return round(None, 2)


def x__compute_savings__mutmut_11(
    cpu_req: float,
    rec_cpu: float,
    mem_req: float,
    rec_mem: float,
) -> float:
    cpu_saved = (cpu_req - rec_cpu) * _CPU_COST_PER_CORE_MONTH
    mem_saved_gib = (mem_req - rec_mem) / 1024.0
    mem_saved = mem_saved_gib * _MEM_COST_PER_GIB_MONTH
    return round(cpu_saved + mem_saved, None)


def x__compute_savings__mutmut_12(
    cpu_req: float,
    rec_cpu: float,
    mem_req: float,
    rec_mem: float,
) -> float:
    cpu_saved = (cpu_req - rec_cpu) * _CPU_COST_PER_CORE_MONTH
    mem_saved_gib = (mem_req - rec_mem) / 1024.0
    mem_saved = mem_saved_gib * _MEM_COST_PER_GIB_MONTH
    return round(2)


def x__compute_savings__mutmut_13(
    cpu_req: float,
    rec_cpu: float,
    mem_req: float,
    rec_mem: float,
) -> float:
    cpu_saved = (cpu_req - rec_cpu) * _CPU_COST_PER_CORE_MONTH
    mem_saved_gib = (mem_req - rec_mem) / 1024.0
    mem_saved = mem_saved_gib * _MEM_COST_PER_GIB_MONTH
    return round(cpu_saved + mem_saved, )


def x__compute_savings__mutmut_14(
    cpu_req: float,
    rec_cpu: float,
    mem_req: float,
    rec_mem: float,
) -> float:
    cpu_saved = (cpu_req - rec_cpu) * _CPU_COST_PER_CORE_MONTH
    mem_saved_gib = (mem_req - rec_mem) / 1024.0
    mem_saved = mem_saved_gib * _MEM_COST_PER_GIB_MONTH
    return round(cpu_saved - mem_saved, 2)


def x__compute_savings__mutmut_15(
    cpu_req: float,
    rec_cpu: float,
    mem_req: float,
    rec_mem: float,
) -> float:
    cpu_saved = (cpu_req - rec_cpu) * _CPU_COST_PER_CORE_MONTH
    mem_saved_gib = (mem_req - rec_mem) / 1024.0
    mem_saved = mem_saved_gib * _MEM_COST_PER_GIB_MONTH
    return round(cpu_saved + mem_saved, 3)

mutants_x__compute_savings__mutmut['_mutmut_orig'] = x__compute_savings__mutmut_orig # type: ignore # mutmut generated
mutants_x__compute_savings__mutmut['x__compute_savings__mutmut_1'] = x__compute_savings__mutmut_1 # type: ignore # mutmut generated
mutants_x__compute_savings__mutmut['x__compute_savings__mutmut_2'] = x__compute_savings__mutmut_2 # type: ignore # mutmut generated
mutants_x__compute_savings__mutmut['x__compute_savings__mutmut_3'] = x__compute_savings__mutmut_3 # type: ignore # mutmut generated
mutants_x__compute_savings__mutmut['x__compute_savings__mutmut_4'] = x__compute_savings__mutmut_4 # type: ignore # mutmut generated
mutants_x__compute_savings__mutmut['x__compute_savings__mutmut_5'] = x__compute_savings__mutmut_5 # type: ignore # mutmut generated
mutants_x__compute_savings__mutmut['x__compute_savings__mutmut_6'] = x__compute_savings__mutmut_6 # type: ignore # mutmut generated
mutants_x__compute_savings__mutmut['x__compute_savings__mutmut_7'] = x__compute_savings__mutmut_7 # type: ignore # mutmut generated
mutants_x__compute_savings__mutmut['x__compute_savings__mutmut_8'] = x__compute_savings__mutmut_8 # type: ignore # mutmut generated
mutants_x__compute_savings__mutmut['x__compute_savings__mutmut_9'] = x__compute_savings__mutmut_9 # type: ignore # mutmut generated
mutants_x__compute_savings__mutmut['x__compute_savings__mutmut_10'] = x__compute_savings__mutmut_10 # type: ignore # mutmut generated
mutants_x__compute_savings__mutmut['x__compute_savings__mutmut_11'] = x__compute_savings__mutmut_11 # type: ignore # mutmut generated
mutants_x__compute_savings__mutmut['x__compute_savings__mutmut_12'] = x__compute_savings__mutmut_12 # type: ignore # mutmut generated
mutants_x__compute_savings__mutmut['x__compute_savings__mutmut_13'] = x__compute_savings__mutmut_13 # type: ignore # mutmut generated
mutants_x__compute_savings__mutmut['x__compute_savings__mutmut_14'] = x__compute_savings__mutmut_14 # type: ignore # mutmut generated
mutants_x__compute_savings__mutmut['x__compute_savings__mutmut_15'] = x__compute_savings__mutmut_15 # type: ignore # mutmut generated
mutants_x__waste_percentage__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__waste_percentage__mutmut)
def _waste_percentage(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.OVER_PROVISIONED:
        cpu_waste = _over_waste(cpu_actual, cpu_req)
        mem_waste = _over_waste(mem_actual, mem_req)
        return round(max(cpu_waste, mem_waste), 1)
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return round(_under_waste(mem_actual, mem_req), 1)
    return 0.0


def x__waste_percentage__mutmut_orig(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.OVER_PROVISIONED:
        cpu_waste = _over_waste(cpu_actual, cpu_req)
        mem_waste = _over_waste(mem_actual, mem_req)
        return round(max(cpu_waste, mem_waste), 1)
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return round(_under_waste(mem_actual, mem_req), 1)
    return 0.0


def x__waste_percentage__mutmut_1(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype != RightsizingType.OVER_PROVISIONED:
        cpu_waste = _over_waste(cpu_actual, cpu_req)
        mem_waste = _over_waste(mem_actual, mem_req)
        return round(max(cpu_waste, mem_waste), 1)
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return round(_under_waste(mem_actual, mem_req), 1)
    return 0.0


def x__waste_percentage__mutmut_2(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.OVER_PROVISIONED:
        cpu_waste = None
        mem_waste = _over_waste(mem_actual, mem_req)
        return round(max(cpu_waste, mem_waste), 1)
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return round(_under_waste(mem_actual, mem_req), 1)
    return 0.0


def x__waste_percentage__mutmut_3(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.OVER_PROVISIONED:
        cpu_waste = _over_waste(None, cpu_req)
        mem_waste = _over_waste(mem_actual, mem_req)
        return round(max(cpu_waste, mem_waste), 1)
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return round(_under_waste(mem_actual, mem_req), 1)
    return 0.0


def x__waste_percentage__mutmut_4(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.OVER_PROVISIONED:
        cpu_waste = _over_waste(cpu_actual, None)
        mem_waste = _over_waste(mem_actual, mem_req)
        return round(max(cpu_waste, mem_waste), 1)
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return round(_under_waste(mem_actual, mem_req), 1)
    return 0.0


def x__waste_percentage__mutmut_5(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.OVER_PROVISIONED:
        cpu_waste = _over_waste(cpu_req)
        mem_waste = _over_waste(mem_actual, mem_req)
        return round(max(cpu_waste, mem_waste), 1)
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return round(_under_waste(mem_actual, mem_req), 1)
    return 0.0


def x__waste_percentage__mutmut_6(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.OVER_PROVISIONED:
        cpu_waste = _over_waste(cpu_actual, )
        mem_waste = _over_waste(mem_actual, mem_req)
        return round(max(cpu_waste, mem_waste), 1)
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return round(_under_waste(mem_actual, mem_req), 1)
    return 0.0


def x__waste_percentage__mutmut_7(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.OVER_PROVISIONED:
        cpu_waste = _over_waste(cpu_actual, cpu_req)
        mem_waste = None
        return round(max(cpu_waste, mem_waste), 1)
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return round(_under_waste(mem_actual, mem_req), 1)
    return 0.0


def x__waste_percentage__mutmut_8(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.OVER_PROVISIONED:
        cpu_waste = _over_waste(cpu_actual, cpu_req)
        mem_waste = _over_waste(None, mem_req)
        return round(max(cpu_waste, mem_waste), 1)
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return round(_under_waste(mem_actual, mem_req), 1)
    return 0.0


def x__waste_percentage__mutmut_9(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.OVER_PROVISIONED:
        cpu_waste = _over_waste(cpu_actual, cpu_req)
        mem_waste = _over_waste(mem_actual, None)
        return round(max(cpu_waste, mem_waste), 1)
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return round(_under_waste(mem_actual, mem_req), 1)
    return 0.0


def x__waste_percentage__mutmut_10(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.OVER_PROVISIONED:
        cpu_waste = _over_waste(cpu_actual, cpu_req)
        mem_waste = _over_waste(mem_req)
        return round(max(cpu_waste, mem_waste), 1)
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return round(_under_waste(mem_actual, mem_req), 1)
    return 0.0


def x__waste_percentage__mutmut_11(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.OVER_PROVISIONED:
        cpu_waste = _over_waste(cpu_actual, cpu_req)
        mem_waste = _over_waste(mem_actual, )
        return round(max(cpu_waste, mem_waste), 1)
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return round(_under_waste(mem_actual, mem_req), 1)
    return 0.0


def x__waste_percentage__mutmut_12(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.OVER_PROVISIONED:
        cpu_waste = _over_waste(cpu_actual, cpu_req)
        mem_waste = _over_waste(mem_actual, mem_req)
        return round(None, 1)
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return round(_under_waste(mem_actual, mem_req), 1)
    return 0.0


def x__waste_percentage__mutmut_13(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.OVER_PROVISIONED:
        cpu_waste = _over_waste(cpu_actual, cpu_req)
        mem_waste = _over_waste(mem_actual, mem_req)
        return round(max(cpu_waste, mem_waste), None)
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return round(_under_waste(mem_actual, mem_req), 1)
    return 0.0


def x__waste_percentage__mutmut_14(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.OVER_PROVISIONED:
        cpu_waste = _over_waste(cpu_actual, cpu_req)
        mem_waste = _over_waste(mem_actual, mem_req)
        return round(1)
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return round(_under_waste(mem_actual, mem_req), 1)
    return 0.0


def x__waste_percentage__mutmut_15(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.OVER_PROVISIONED:
        cpu_waste = _over_waste(cpu_actual, cpu_req)
        mem_waste = _over_waste(mem_actual, mem_req)
        return round(max(cpu_waste, mem_waste), )
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return round(_under_waste(mem_actual, mem_req), 1)
    return 0.0


def x__waste_percentage__mutmut_16(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.OVER_PROVISIONED:
        cpu_waste = _over_waste(cpu_actual, cpu_req)
        mem_waste = _over_waste(mem_actual, mem_req)
        return round(max(None, mem_waste), 1)
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return round(_under_waste(mem_actual, mem_req), 1)
    return 0.0


def x__waste_percentage__mutmut_17(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.OVER_PROVISIONED:
        cpu_waste = _over_waste(cpu_actual, cpu_req)
        mem_waste = _over_waste(mem_actual, mem_req)
        return round(max(cpu_waste, None), 1)
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return round(_under_waste(mem_actual, mem_req), 1)
    return 0.0


def x__waste_percentage__mutmut_18(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.OVER_PROVISIONED:
        cpu_waste = _over_waste(cpu_actual, cpu_req)
        mem_waste = _over_waste(mem_actual, mem_req)
        return round(max(mem_waste), 1)
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return round(_under_waste(mem_actual, mem_req), 1)
    return 0.0


def x__waste_percentage__mutmut_19(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.OVER_PROVISIONED:
        cpu_waste = _over_waste(cpu_actual, cpu_req)
        mem_waste = _over_waste(mem_actual, mem_req)
        return round(max(cpu_waste, ), 1)
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return round(_under_waste(mem_actual, mem_req), 1)
    return 0.0


def x__waste_percentage__mutmut_20(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.OVER_PROVISIONED:
        cpu_waste = _over_waste(cpu_actual, cpu_req)
        mem_waste = _over_waste(mem_actual, mem_req)
        return round(max(cpu_waste, mem_waste), 2)
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return round(_under_waste(mem_actual, mem_req), 1)
    return 0.0


def x__waste_percentage__mutmut_21(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.OVER_PROVISIONED:
        cpu_waste = _over_waste(cpu_actual, cpu_req)
        mem_waste = _over_waste(mem_actual, mem_req)
        return round(max(cpu_waste, mem_waste), 1)
    if rtype != RightsizingType.UNDER_PROVISIONED:
        return round(_under_waste(mem_actual, mem_req), 1)
    return 0.0


def x__waste_percentage__mutmut_22(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.OVER_PROVISIONED:
        cpu_waste = _over_waste(cpu_actual, cpu_req)
        mem_waste = _over_waste(mem_actual, mem_req)
        return round(max(cpu_waste, mem_waste), 1)
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return round(None, 1)
    return 0.0


def x__waste_percentage__mutmut_23(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.OVER_PROVISIONED:
        cpu_waste = _over_waste(cpu_actual, cpu_req)
        mem_waste = _over_waste(mem_actual, mem_req)
        return round(max(cpu_waste, mem_waste), 1)
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return round(_under_waste(mem_actual, mem_req), None)
    return 0.0


def x__waste_percentage__mutmut_24(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.OVER_PROVISIONED:
        cpu_waste = _over_waste(cpu_actual, cpu_req)
        mem_waste = _over_waste(mem_actual, mem_req)
        return round(max(cpu_waste, mem_waste), 1)
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return round(1)
    return 0.0


def x__waste_percentage__mutmut_25(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.OVER_PROVISIONED:
        cpu_waste = _over_waste(cpu_actual, cpu_req)
        mem_waste = _over_waste(mem_actual, mem_req)
        return round(max(cpu_waste, mem_waste), 1)
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return round(_under_waste(mem_actual, mem_req), )
    return 0.0


def x__waste_percentage__mutmut_26(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.OVER_PROVISIONED:
        cpu_waste = _over_waste(cpu_actual, cpu_req)
        mem_waste = _over_waste(mem_actual, mem_req)
        return round(max(cpu_waste, mem_waste), 1)
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return round(_under_waste(None, mem_req), 1)
    return 0.0


def x__waste_percentage__mutmut_27(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.OVER_PROVISIONED:
        cpu_waste = _over_waste(cpu_actual, cpu_req)
        mem_waste = _over_waste(mem_actual, mem_req)
        return round(max(cpu_waste, mem_waste), 1)
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return round(_under_waste(mem_actual, None), 1)
    return 0.0


def x__waste_percentage__mutmut_28(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.OVER_PROVISIONED:
        cpu_waste = _over_waste(cpu_actual, cpu_req)
        mem_waste = _over_waste(mem_actual, mem_req)
        return round(max(cpu_waste, mem_waste), 1)
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return round(_under_waste(mem_req), 1)
    return 0.0


def x__waste_percentage__mutmut_29(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.OVER_PROVISIONED:
        cpu_waste = _over_waste(cpu_actual, cpu_req)
        mem_waste = _over_waste(mem_actual, mem_req)
        return round(max(cpu_waste, mem_waste), 1)
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return round(_under_waste(mem_actual, ), 1)
    return 0.0


def x__waste_percentage__mutmut_30(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.OVER_PROVISIONED:
        cpu_waste = _over_waste(cpu_actual, cpu_req)
        mem_waste = _over_waste(mem_actual, mem_req)
        return round(max(cpu_waste, mem_waste), 1)
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return round(_under_waste(mem_actual, mem_req), 2)
    return 0.0


def x__waste_percentage__mutmut_31(
    rtype: RightsizingType,
    cpu_req: float,
    mem_req: float,
    cpu_actual: float | None,
    mem_actual: float | None,
) -> float:
    if rtype == RightsizingType.OVER_PROVISIONED:
        cpu_waste = _over_waste(cpu_actual, cpu_req)
        mem_waste = _over_waste(mem_actual, mem_req)
        return round(max(cpu_waste, mem_waste), 1)
    if rtype == RightsizingType.UNDER_PROVISIONED:
        return round(_under_waste(mem_actual, mem_req), 1)
    return 1.0

mutants_x__waste_percentage__mutmut['_mutmut_orig'] = x__waste_percentage__mutmut_orig # type: ignore # mutmut generated
mutants_x__waste_percentage__mutmut['x__waste_percentage__mutmut_1'] = x__waste_percentage__mutmut_1 # type: ignore # mutmut generated
mutants_x__waste_percentage__mutmut['x__waste_percentage__mutmut_2'] = x__waste_percentage__mutmut_2 # type: ignore # mutmut generated
mutants_x__waste_percentage__mutmut['x__waste_percentage__mutmut_3'] = x__waste_percentage__mutmut_3 # type: ignore # mutmut generated
mutants_x__waste_percentage__mutmut['x__waste_percentage__mutmut_4'] = x__waste_percentage__mutmut_4 # type: ignore # mutmut generated
mutants_x__waste_percentage__mutmut['x__waste_percentage__mutmut_5'] = x__waste_percentage__mutmut_5 # type: ignore # mutmut generated
mutants_x__waste_percentage__mutmut['x__waste_percentage__mutmut_6'] = x__waste_percentage__mutmut_6 # type: ignore # mutmut generated
mutants_x__waste_percentage__mutmut['x__waste_percentage__mutmut_7'] = x__waste_percentage__mutmut_7 # type: ignore # mutmut generated
mutants_x__waste_percentage__mutmut['x__waste_percentage__mutmut_8'] = x__waste_percentage__mutmut_8 # type: ignore # mutmut generated
mutants_x__waste_percentage__mutmut['x__waste_percentage__mutmut_9'] = x__waste_percentage__mutmut_9 # type: ignore # mutmut generated
mutants_x__waste_percentage__mutmut['x__waste_percentage__mutmut_10'] = x__waste_percentage__mutmut_10 # type: ignore # mutmut generated
mutants_x__waste_percentage__mutmut['x__waste_percentage__mutmut_11'] = x__waste_percentage__mutmut_11 # type: ignore # mutmut generated
mutants_x__waste_percentage__mutmut['x__waste_percentage__mutmut_12'] = x__waste_percentage__mutmut_12 # type: ignore # mutmut generated
mutants_x__waste_percentage__mutmut['x__waste_percentage__mutmut_13'] = x__waste_percentage__mutmut_13 # type: ignore # mutmut generated
mutants_x__waste_percentage__mutmut['x__waste_percentage__mutmut_14'] = x__waste_percentage__mutmut_14 # type: ignore # mutmut generated
mutants_x__waste_percentage__mutmut['x__waste_percentage__mutmut_15'] = x__waste_percentage__mutmut_15 # type: ignore # mutmut generated
mutants_x__waste_percentage__mutmut['x__waste_percentage__mutmut_16'] = x__waste_percentage__mutmut_16 # type: ignore # mutmut generated
mutants_x__waste_percentage__mutmut['x__waste_percentage__mutmut_17'] = x__waste_percentage__mutmut_17 # type: ignore # mutmut generated
mutants_x__waste_percentage__mutmut['x__waste_percentage__mutmut_18'] = x__waste_percentage__mutmut_18 # type: ignore # mutmut generated
mutants_x__waste_percentage__mutmut['x__waste_percentage__mutmut_19'] = x__waste_percentage__mutmut_19 # type: ignore # mutmut generated
mutants_x__waste_percentage__mutmut['x__waste_percentage__mutmut_20'] = x__waste_percentage__mutmut_20 # type: ignore # mutmut generated
mutants_x__waste_percentage__mutmut['x__waste_percentage__mutmut_21'] = x__waste_percentage__mutmut_21 # type: ignore # mutmut generated
mutants_x__waste_percentage__mutmut['x__waste_percentage__mutmut_22'] = x__waste_percentage__mutmut_22 # type: ignore # mutmut generated
mutants_x__waste_percentage__mutmut['x__waste_percentage__mutmut_23'] = x__waste_percentage__mutmut_23 # type: ignore # mutmut generated
mutants_x__waste_percentage__mutmut['x__waste_percentage__mutmut_24'] = x__waste_percentage__mutmut_24 # type: ignore # mutmut generated
mutants_x__waste_percentage__mutmut['x__waste_percentage__mutmut_25'] = x__waste_percentage__mutmut_25 # type: ignore # mutmut generated
mutants_x__waste_percentage__mutmut['x__waste_percentage__mutmut_26'] = x__waste_percentage__mutmut_26 # type: ignore # mutmut generated
mutants_x__waste_percentage__mutmut['x__waste_percentage__mutmut_27'] = x__waste_percentage__mutmut_27 # type: ignore # mutmut generated
mutants_x__waste_percentage__mutmut['x__waste_percentage__mutmut_28'] = x__waste_percentage__mutmut_28 # type: ignore # mutmut generated
mutants_x__waste_percentage__mutmut['x__waste_percentage__mutmut_29'] = x__waste_percentage__mutmut_29 # type: ignore # mutmut generated
mutants_x__waste_percentage__mutmut['x__waste_percentage__mutmut_30'] = x__waste_percentage__mutmut_30 # type: ignore # mutmut generated
mutants_x__waste_percentage__mutmut['x__waste_percentage__mutmut_31'] = x__waste_percentage__mutmut_31 # type: ignore # mutmut generated
mutants_x__over_waste__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__over_waste__mutmut)
def _over_waste(actual: float | None, request: float) -> float:
    if request <= 0 or actual is None:
        return 0.0
    return (1.0 - actual / request) * 100.0


def x__over_waste__mutmut_orig(actual: float | None, request: float) -> float:
    if request <= 0 or actual is None:
        return 0.0
    return (1.0 - actual / request) * 100.0


def x__over_waste__mutmut_1(actual: float | None, request: float) -> float:
    if request <= 0 and actual is None:
        return 0.0
    return (1.0 - actual / request) * 100.0


def x__over_waste__mutmut_2(actual: float | None, request: float) -> float:
    if request < 0 or actual is None:
        return 0.0
    return (1.0 - actual / request) * 100.0


def x__over_waste__mutmut_3(actual: float | None, request: float) -> float:
    if request <= 1 or actual is None:
        return 0.0
    return (1.0 - actual / request) * 100.0


def x__over_waste__mutmut_4(actual: float | None, request: float) -> float:
    if request <= 0 or actual is not None:
        return 0.0
    return (1.0 - actual / request) * 100.0


def x__over_waste__mutmut_5(actual: float | None, request: float) -> float:
    if request <= 0 or actual is None:
        return 1.0
    return (1.0 - actual / request) * 100.0


def x__over_waste__mutmut_6(actual: float | None, request: float) -> float:
    if request <= 0 or actual is None:
        return 0.0
    return (1.0 - actual / request) / 100.0


def x__over_waste__mutmut_7(actual: float | None, request: float) -> float:
    if request <= 0 or actual is None:
        return 0.0
    return (1.0 + actual / request) * 100.0


def x__over_waste__mutmut_8(actual: float | None, request: float) -> float:
    if request <= 0 or actual is None:
        return 0.0
    return (2.0 - actual / request) * 100.0


def x__over_waste__mutmut_9(actual: float | None, request: float) -> float:
    if request <= 0 or actual is None:
        return 0.0
    return (1.0 - actual * request) * 100.0


def x__over_waste__mutmut_10(actual: float | None, request: float) -> float:
    if request <= 0 or actual is None:
        return 0.0
    return (1.0 - actual / request) * 101.0

mutants_x__over_waste__mutmut['_mutmut_orig'] = x__over_waste__mutmut_orig # type: ignore # mutmut generated
mutants_x__over_waste__mutmut['x__over_waste__mutmut_1'] = x__over_waste__mutmut_1 # type: ignore # mutmut generated
mutants_x__over_waste__mutmut['x__over_waste__mutmut_2'] = x__over_waste__mutmut_2 # type: ignore # mutmut generated
mutants_x__over_waste__mutmut['x__over_waste__mutmut_3'] = x__over_waste__mutmut_3 # type: ignore # mutmut generated
mutants_x__over_waste__mutmut['x__over_waste__mutmut_4'] = x__over_waste__mutmut_4 # type: ignore # mutmut generated
mutants_x__over_waste__mutmut['x__over_waste__mutmut_5'] = x__over_waste__mutmut_5 # type: ignore # mutmut generated
mutants_x__over_waste__mutmut['x__over_waste__mutmut_6'] = x__over_waste__mutmut_6 # type: ignore # mutmut generated
mutants_x__over_waste__mutmut['x__over_waste__mutmut_7'] = x__over_waste__mutmut_7 # type: ignore # mutmut generated
mutants_x__over_waste__mutmut['x__over_waste__mutmut_8'] = x__over_waste__mutmut_8 # type: ignore # mutmut generated
mutants_x__over_waste__mutmut['x__over_waste__mutmut_9'] = x__over_waste__mutmut_9 # type: ignore # mutmut generated
mutants_x__over_waste__mutmut['x__over_waste__mutmut_10'] = x__over_waste__mutmut_10 # type: ignore # mutmut generated
mutants_x__under_waste__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__under_waste__mutmut)
def _under_waste(actual: float | None, request: float) -> float:
    if request <= 0 or actual is None:
        return 0.0
    return actual / request * 100.0


def x__under_waste__mutmut_orig(actual: float | None, request: float) -> float:
    if request <= 0 or actual is None:
        return 0.0
    return actual / request * 100.0


def x__under_waste__mutmut_1(actual: float | None, request: float) -> float:
    if request <= 0 and actual is None:
        return 0.0
    return actual / request * 100.0


def x__under_waste__mutmut_2(actual: float | None, request: float) -> float:
    if request < 0 or actual is None:
        return 0.0
    return actual / request * 100.0


def x__under_waste__mutmut_3(actual: float | None, request: float) -> float:
    if request <= 1 or actual is None:
        return 0.0
    return actual / request * 100.0


def x__under_waste__mutmut_4(actual: float | None, request: float) -> float:
    if request <= 0 or actual is not None:
        return 0.0
    return actual / request * 100.0


def x__under_waste__mutmut_5(actual: float | None, request: float) -> float:
    if request <= 0 or actual is None:
        return 1.0
    return actual / request * 100.0


def x__under_waste__mutmut_6(actual: float | None, request: float) -> float:
    if request <= 0 or actual is None:
        return 0.0
    return actual / request / 100.0


def x__under_waste__mutmut_7(actual: float | None, request: float) -> float:
    if request <= 0 or actual is None:
        return 0.0
    return actual * request * 100.0


def x__under_waste__mutmut_8(actual: float | None, request: float) -> float:
    if request <= 0 or actual is None:
        return 0.0
    return actual / request * 101.0

mutants_x__under_waste__mutmut['_mutmut_orig'] = x__under_waste__mutmut_orig # type: ignore # mutmut generated
mutants_x__under_waste__mutmut['x__under_waste__mutmut_1'] = x__under_waste__mutmut_1 # type: ignore # mutmut generated
mutants_x__under_waste__mutmut['x__under_waste__mutmut_2'] = x__under_waste__mutmut_2 # type: ignore # mutmut generated
mutants_x__under_waste__mutmut['x__under_waste__mutmut_3'] = x__under_waste__mutmut_3 # type: ignore # mutmut generated
mutants_x__under_waste__mutmut['x__under_waste__mutmut_4'] = x__under_waste__mutmut_4 # type: ignore # mutmut generated
mutants_x__under_waste__mutmut['x__under_waste__mutmut_5'] = x__under_waste__mutmut_5 # type: ignore # mutmut generated
mutants_x__under_waste__mutmut['x__under_waste__mutmut_6'] = x__under_waste__mutmut_6 # type: ignore # mutmut generated
mutants_x__under_waste__mutmut['x__under_waste__mutmut_7'] = x__under_waste__mutmut_7 # type: ignore # mutmut generated
mutants_x__under_waste__mutmut['x__under_waste__mutmut_8'] = x__under_waste__mutmut_8 # type: ignore # mutmut generated
mutants_x__priority__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__priority__mutmut)
def _priority(savings: float) -> str:
    amount = abs(savings)
    if amount > _PRIORITY_HIGH_USD:
        return "high"
    if amount > _PRIORITY_MEDIUM_USD:
        return "medium"
    return "low"


def x__priority__mutmut_orig(savings: float) -> str:
    amount = abs(savings)
    if amount > _PRIORITY_HIGH_USD:
        return "high"
    if amount > _PRIORITY_MEDIUM_USD:
        return "medium"
    return "low"


def x__priority__mutmut_1(savings: float) -> str:
    amount = None
    if amount > _PRIORITY_HIGH_USD:
        return "high"
    if amount > _PRIORITY_MEDIUM_USD:
        return "medium"
    return "low"


def x__priority__mutmut_2(savings: float) -> str:
    amount = abs(None)
    if amount > _PRIORITY_HIGH_USD:
        return "high"
    if amount > _PRIORITY_MEDIUM_USD:
        return "medium"
    return "low"


def x__priority__mutmut_3(savings: float) -> str:
    amount = abs(savings)
    if amount >= _PRIORITY_HIGH_USD:
        return "high"
    if amount > _PRIORITY_MEDIUM_USD:
        return "medium"
    return "low"


def x__priority__mutmut_4(savings: float) -> str:
    amount = abs(savings)
    if amount > _PRIORITY_HIGH_USD:
        return "XXhighXX"
    if amount > _PRIORITY_MEDIUM_USD:
        return "medium"
    return "low"


def x__priority__mutmut_5(savings: float) -> str:
    amount = abs(savings)
    if amount > _PRIORITY_HIGH_USD:
        return "HIGH"
    if amount > _PRIORITY_MEDIUM_USD:
        return "medium"
    return "low"


def x__priority__mutmut_6(savings: float) -> str:
    amount = abs(savings)
    if amount > _PRIORITY_HIGH_USD:
        return "high"
    if amount >= _PRIORITY_MEDIUM_USD:
        return "medium"
    return "low"


def x__priority__mutmut_7(savings: float) -> str:
    amount = abs(savings)
    if amount > _PRIORITY_HIGH_USD:
        return "high"
    if amount > _PRIORITY_MEDIUM_USD:
        return "XXmediumXX"
    return "low"


def x__priority__mutmut_8(savings: float) -> str:
    amount = abs(savings)
    if amount > _PRIORITY_HIGH_USD:
        return "high"
    if amount > _PRIORITY_MEDIUM_USD:
        return "MEDIUM"
    return "low"


def x__priority__mutmut_9(savings: float) -> str:
    amount = abs(savings)
    if amount > _PRIORITY_HIGH_USD:
        return "high"
    if amount > _PRIORITY_MEDIUM_USD:
        return "medium"
    return "XXlowXX"


def x__priority__mutmut_10(savings: float) -> str:
    amount = abs(savings)
    if amount > _PRIORITY_HIGH_USD:
        return "high"
    if amount > _PRIORITY_MEDIUM_USD:
        return "medium"
    return "LOW"

mutants_x__priority__mutmut['_mutmut_orig'] = x__priority__mutmut_orig # type: ignore # mutmut generated
mutants_x__priority__mutmut['x__priority__mutmut_1'] = x__priority__mutmut_1 # type: ignore # mutmut generated
mutants_x__priority__mutmut['x__priority__mutmut_2'] = x__priority__mutmut_2 # type: ignore # mutmut generated
mutants_x__priority__mutmut['x__priority__mutmut_3'] = x__priority__mutmut_3 # type: ignore # mutmut generated
mutants_x__priority__mutmut['x__priority__mutmut_4'] = x__priority__mutmut_4 # type: ignore # mutmut generated
mutants_x__priority__mutmut['x__priority__mutmut_5'] = x__priority__mutmut_5 # type: ignore # mutmut generated
mutants_x__priority__mutmut['x__priority__mutmut_6'] = x__priority__mutmut_6 # type: ignore # mutmut generated
mutants_x__priority__mutmut['x__priority__mutmut_7'] = x__priority__mutmut_7 # type: ignore # mutmut generated
mutants_x__priority__mutmut['x__priority__mutmut_8'] = x__priority__mutmut_8 # type: ignore # mutmut generated
mutants_x__priority__mutmut['x__priority__mutmut_9'] = x__priority__mutmut_9 # type: ignore # mutmut generated
mutants_x__priority__mutmut['x__priority__mutmut_10'] = x__priority__mutmut_10 # type: ignore # mutmut generated
mutants_x__as_float_or_none__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__as_float_or_none__mutmut)
def _as_float_or_none(value: object) -> float | None:
    if value is None:
        return None
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return None


def x__as_float_or_none__mutmut_orig(value: object) -> float | None:
    if value is None:
        return None
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return None


def x__as_float_or_none__mutmut_1(value: object) -> float | None:
    if value is not None:
        return None
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return None


def x__as_float_or_none__mutmut_2(value: object) -> float | None:
    if value is None:
        return None
    try:
        return float(None)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return None

mutants_x__as_float_or_none__mutmut['_mutmut_orig'] = x__as_float_or_none__mutmut_orig # type: ignore # mutmut generated
mutants_x__as_float_or_none__mutmut['x__as_float_or_none__mutmut_1'] = x__as_float_or_none__mutmut_1 # type: ignore # mutmut generated
mutants_x__as_float_or_none__mutmut['x__as_float_or_none__mutmut_2'] = x__as_float_or_none__mutmut_2 # type: ignore # mutmut generated
