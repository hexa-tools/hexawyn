from hexawyn.domain.models.constants import ScoringConstants
from hexawyn.domain.models.scoring import (
    FailureImpactScore,
    RcaConfidenceScore,
    RcaScoringConfig,
)

_scoring = ScoringConstants()


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁRcaScorerǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁRcaScorerǁcalculate_confidence__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRcaScorerǁcalculate_impact__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRcaScorerǁassess_severity__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRcaScorerǁ_confidence_label__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRcaScorerǁ_impact_label__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRcaScorerǁ_cascade_risk__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRcaScorerǁ_overall_severity__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRcaScorerǁ_priority__mutmut: MutantDict = {}  # type: ignore


class RcaScorer:
    """Calculates confidence and impact scores for root cause analysis.

    Uses config-driven additive scoring with min/max clamping.
    Weights are defined in RcaScoringConfig — no hardcoded magic numbers.
    """

    @_mutmut_mutated(mutants_xǁRcaScorerǁ__init____mutmut)
    def __init__(self, config: RcaScoringConfig | None = None) -> None:
        self.config = config or RcaScoringConfig()

    def xǁRcaScorerǁ__init____mutmut_orig(self, config: RcaScoringConfig | None = None) -> None:
        self.config = config or RcaScoringConfig()

    def xǁRcaScorerǁ__init____mutmut_1(self, config: RcaScoringConfig | None = None) -> None:
        self.config = None

    def xǁRcaScorerǁ__init____mutmut_2(self, config: RcaScoringConfig | None = None) -> None:
        self.config = config and RcaScoringConfig()

    @_mutmut_mutated(mutants_xǁRcaScorerǁcalculate_confidence__mutmut)
    def calculate_confidence(
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
    ) -> RcaConfidenceScore:
        factors: dict[str, float] = {}
        score = self.config.base_confidence

        if logs_analyzed:
            factors["logs_analyzed"] = self.config.logs_analyzed_weight
            score += self.config.logs_analyzed_weight

        if root_cause_found:
            factors["root_cause_found"] = self.config.root_cause_found_weight
            score += self.config.root_cause_found_weight

        if timeline_available:
            factors["timeline_available"] = self.config.timeline_available_weight
            score += self.config.timeline_available_weight

        value = min(score, self.config.max_confidence)
        label = self._confidence_label(value)

        return RcaConfidenceScore(value=value, label=label, factors=factors)

    def xǁRcaScorerǁcalculate_confidence__mutmut_orig(
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
    ) -> RcaConfidenceScore:
        factors: dict[str, float] = {}
        score = self.config.base_confidence

        if logs_analyzed:
            factors["logs_analyzed"] = self.config.logs_analyzed_weight
            score += self.config.logs_analyzed_weight

        if root_cause_found:
            factors["root_cause_found"] = self.config.root_cause_found_weight
            score += self.config.root_cause_found_weight

        if timeline_available:
            factors["timeline_available"] = self.config.timeline_available_weight
            score += self.config.timeline_available_weight

        value = min(score, self.config.max_confidence)
        label = self._confidence_label(value)

        return RcaConfidenceScore(value=value, label=label, factors=factors)

    def xǁRcaScorerǁcalculate_confidence__mutmut_1(
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
    ) -> RcaConfidenceScore:
        factors: dict[str, float] = None
        score = self.config.base_confidence

        if logs_analyzed:
            factors["logs_analyzed"] = self.config.logs_analyzed_weight
            score += self.config.logs_analyzed_weight

        if root_cause_found:
            factors["root_cause_found"] = self.config.root_cause_found_weight
            score += self.config.root_cause_found_weight

        if timeline_available:
            factors["timeline_available"] = self.config.timeline_available_weight
            score += self.config.timeline_available_weight

        value = min(score, self.config.max_confidence)
        label = self._confidence_label(value)

        return RcaConfidenceScore(value=value, label=label, factors=factors)

    def xǁRcaScorerǁcalculate_confidence__mutmut_2(
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
    ) -> RcaConfidenceScore:
        factors: dict[str, float] = {}
        score = None

        if logs_analyzed:
            factors["logs_analyzed"] = self.config.logs_analyzed_weight
            score += self.config.logs_analyzed_weight

        if root_cause_found:
            factors["root_cause_found"] = self.config.root_cause_found_weight
            score += self.config.root_cause_found_weight

        if timeline_available:
            factors["timeline_available"] = self.config.timeline_available_weight
            score += self.config.timeline_available_weight

        value = min(score, self.config.max_confidence)
        label = self._confidence_label(value)

        return RcaConfidenceScore(value=value, label=label, factors=factors)

    def xǁRcaScorerǁcalculate_confidence__mutmut_3(
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
    ) -> RcaConfidenceScore:
        factors: dict[str, float] = {}
        score = self.config.base_confidence

        if logs_analyzed:
            factors["logs_analyzed"] = None
            score += self.config.logs_analyzed_weight

        if root_cause_found:
            factors["root_cause_found"] = self.config.root_cause_found_weight
            score += self.config.root_cause_found_weight

        if timeline_available:
            factors["timeline_available"] = self.config.timeline_available_weight
            score += self.config.timeline_available_weight

        value = min(score, self.config.max_confidence)
        label = self._confidence_label(value)

        return RcaConfidenceScore(value=value, label=label, factors=factors)

    def xǁRcaScorerǁcalculate_confidence__mutmut_4(
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
    ) -> RcaConfidenceScore:
        factors: dict[str, float] = {}
        score = self.config.base_confidence

        if logs_analyzed:
            factors["XXlogs_analyzedXX"] = self.config.logs_analyzed_weight
            score += self.config.logs_analyzed_weight

        if root_cause_found:
            factors["root_cause_found"] = self.config.root_cause_found_weight
            score += self.config.root_cause_found_weight

        if timeline_available:
            factors["timeline_available"] = self.config.timeline_available_weight
            score += self.config.timeline_available_weight

        value = min(score, self.config.max_confidence)
        label = self._confidence_label(value)

        return RcaConfidenceScore(value=value, label=label, factors=factors)

    def xǁRcaScorerǁcalculate_confidence__mutmut_5(
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
    ) -> RcaConfidenceScore:
        factors: dict[str, float] = {}
        score = self.config.base_confidence

        if logs_analyzed:
            factors["LOGS_ANALYZED"] = self.config.logs_analyzed_weight
            score += self.config.logs_analyzed_weight

        if root_cause_found:
            factors["root_cause_found"] = self.config.root_cause_found_weight
            score += self.config.root_cause_found_weight

        if timeline_available:
            factors["timeline_available"] = self.config.timeline_available_weight
            score += self.config.timeline_available_weight

        value = min(score, self.config.max_confidence)
        label = self._confidence_label(value)

        return RcaConfidenceScore(value=value, label=label, factors=factors)

    def xǁRcaScorerǁcalculate_confidence__mutmut_6(
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
    ) -> RcaConfidenceScore:
        factors: dict[str, float] = {}
        score = self.config.base_confidence

        if logs_analyzed:
            factors["logs_analyzed"] = self.config.logs_analyzed_weight
            score = self.config.logs_analyzed_weight

        if root_cause_found:
            factors["root_cause_found"] = self.config.root_cause_found_weight
            score += self.config.root_cause_found_weight

        if timeline_available:
            factors["timeline_available"] = self.config.timeline_available_weight
            score += self.config.timeline_available_weight

        value = min(score, self.config.max_confidence)
        label = self._confidence_label(value)

        return RcaConfidenceScore(value=value, label=label, factors=factors)

    def xǁRcaScorerǁcalculate_confidence__mutmut_7(
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
    ) -> RcaConfidenceScore:
        factors: dict[str, float] = {}
        score = self.config.base_confidence

        if logs_analyzed:
            factors["logs_analyzed"] = self.config.logs_analyzed_weight
            score -= self.config.logs_analyzed_weight

        if root_cause_found:
            factors["root_cause_found"] = self.config.root_cause_found_weight
            score += self.config.root_cause_found_weight

        if timeline_available:
            factors["timeline_available"] = self.config.timeline_available_weight
            score += self.config.timeline_available_weight

        value = min(score, self.config.max_confidence)
        label = self._confidence_label(value)

        return RcaConfidenceScore(value=value, label=label, factors=factors)

    def xǁRcaScorerǁcalculate_confidence__mutmut_8(
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
    ) -> RcaConfidenceScore:
        factors: dict[str, float] = {}
        score = self.config.base_confidence

        if logs_analyzed:
            factors["logs_analyzed"] = self.config.logs_analyzed_weight
            score += self.config.logs_analyzed_weight

        if root_cause_found:
            factors["root_cause_found"] = None
            score += self.config.root_cause_found_weight

        if timeline_available:
            factors["timeline_available"] = self.config.timeline_available_weight
            score += self.config.timeline_available_weight

        value = min(score, self.config.max_confidence)
        label = self._confidence_label(value)

        return RcaConfidenceScore(value=value, label=label, factors=factors)

    def xǁRcaScorerǁcalculate_confidence__mutmut_9(
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
    ) -> RcaConfidenceScore:
        factors: dict[str, float] = {}
        score = self.config.base_confidence

        if logs_analyzed:
            factors["logs_analyzed"] = self.config.logs_analyzed_weight
            score += self.config.logs_analyzed_weight

        if root_cause_found:
            factors["XXroot_cause_foundXX"] = self.config.root_cause_found_weight
            score += self.config.root_cause_found_weight

        if timeline_available:
            factors["timeline_available"] = self.config.timeline_available_weight
            score += self.config.timeline_available_weight

        value = min(score, self.config.max_confidence)
        label = self._confidence_label(value)

        return RcaConfidenceScore(value=value, label=label, factors=factors)

    def xǁRcaScorerǁcalculate_confidence__mutmut_10(
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
    ) -> RcaConfidenceScore:
        factors: dict[str, float] = {}
        score = self.config.base_confidence

        if logs_analyzed:
            factors["logs_analyzed"] = self.config.logs_analyzed_weight
            score += self.config.logs_analyzed_weight

        if root_cause_found:
            factors["ROOT_CAUSE_FOUND"] = self.config.root_cause_found_weight
            score += self.config.root_cause_found_weight

        if timeline_available:
            factors["timeline_available"] = self.config.timeline_available_weight
            score += self.config.timeline_available_weight

        value = min(score, self.config.max_confidence)
        label = self._confidence_label(value)

        return RcaConfidenceScore(value=value, label=label, factors=factors)

    def xǁRcaScorerǁcalculate_confidence__mutmut_11(
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
    ) -> RcaConfidenceScore:
        factors: dict[str, float] = {}
        score = self.config.base_confidence

        if logs_analyzed:
            factors["logs_analyzed"] = self.config.logs_analyzed_weight
            score += self.config.logs_analyzed_weight

        if root_cause_found:
            factors["root_cause_found"] = self.config.root_cause_found_weight
            score = self.config.root_cause_found_weight

        if timeline_available:
            factors["timeline_available"] = self.config.timeline_available_weight
            score += self.config.timeline_available_weight

        value = min(score, self.config.max_confidence)
        label = self._confidence_label(value)

        return RcaConfidenceScore(value=value, label=label, factors=factors)

    def xǁRcaScorerǁcalculate_confidence__mutmut_12(
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
    ) -> RcaConfidenceScore:
        factors: dict[str, float] = {}
        score = self.config.base_confidence

        if logs_analyzed:
            factors["logs_analyzed"] = self.config.logs_analyzed_weight
            score += self.config.logs_analyzed_weight

        if root_cause_found:
            factors["root_cause_found"] = self.config.root_cause_found_weight
            score -= self.config.root_cause_found_weight

        if timeline_available:
            factors["timeline_available"] = self.config.timeline_available_weight
            score += self.config.timeline_available_weight

        value = min(score, self.config.max_confidence)
        label = self._confidence_label(value)

        return RcaConfidenceScore(value=value, label=label, factors=factors)

    def xǁRcaScorerǁcalculate_confidence__mutmut_13(
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
    ) -> RcaConfidenceScore:
        factors: dict[str, float] = {}
        score = self.config.base_confidence

        if logs_analyzed:
            factors["logs_analyzed"] = self.config.logs_analyzed_weight
            score += self.config.logs_analyzed_weight

        if root_cause_found:
            factors["root_cause_found"] = self.config.root_cause_found_weight
            score += self.config.root_cause_found_weight

        if timeline_available:
            factors["timeline_available"] = None
            score += self.config.timeline_available_weight

        value = min(score, self.config.max_confidence)
        label = self._confidence_label(value)

        return RcaConfidenceScore(value=value, label=label, factors=factors)

    def xǁRcaScorerǁcalculate_confidence__mutmut_14(
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
    ) -> RcaConfidenceScore:
        factors: dict[str, float] = {}
        score = self.config.base_confidence

        if logs_analyzed:
            factors["logs_analyzed"] = self.config.logs_analyzed_weight
            score += self.config.logs_analyzed_weight

        if root_cause_found:
            factors["root_cause_found"] = self.config.root_cause_found_weight
            score += self.config.root_cause_found_weight

        if timeline_available:
            factors["XXtimeline_availableXX"] = self.config.timeline_available_weight
            score += self.config.timeline_available_weight

        value = min(score, self.config.max_confidence)
        label = self._confidence_label(value)

        return RcaConfidenceScore(value=value, label=label, factors=factors)

    def xǁRcaScorerǁcalculate_confidence__mutmut_15(
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
    ) -> RcaConfidenceScore:
        factors: dict[str, float] = {}
        score = self.config.base_confidence

        if logs_analyzed:
            factors["logs_analyzed"] = self.config.logs_analyzed_weight
            score += self.config.logs_analyzed_weight

        if root_cause_found:
            factors["root_cause_found"] = self.config.root_cause_found_weight
            score += self.config.root_cause_found_weight

        if timeline_available:
            factors["TIMELINE_AVAILABLE"] = self.config.timeline_available_weight
            score += self.config.timeline_available_weight

        value = min(score, self.config.max_confidence)
        label = self._confidence_label(value)

        return RcaConfidenceScore(value=value, label=label, factors=factors)

    def xǁRcaScorerǁcalculate_confidence__mutmut_16(
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
    ) -> RcaConfidenceScore:
        factors: dict[str, float] = {}
        score = self.config.base_confidence

        if logs_analyzed:
            factors["logs_analyzed"] = self.config.logs_analyzed_weight
            score += self.config.logs_analyzed_weight

        if root_cause_found:
            factors["root_cause_found"] = self.config.root_cause_found_weight
            score += self.config.root_cause_found_weight

        if timeline_available:
            factors["timeline_available"] = self.config.timeline_available_weight
            score = self.config.timeline_available_weight

        value = min(score, self.config.max_confidence)
        label = self._confidence_label(value)

        return RcaConfidenceScore(value=value, label=label, factors=factors)

    def xǁRcaScorerǁcalculate_confidence__mutmut_17(
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
    ) -> RcaConfidenceScore:
        factors: dict[str, float] = {}
        score = self.config.base_confidence

        if logs_analyzed:
            factors["logs_analyzed"] = self.config.logs_analyzed_weight
            score += self.config.logs_analyzed_weight

        if root_cause_found:
            factors["root_cause_found"] = self.config.root_cause_found_weight
            score += self.config.root_cause_found_weight

        if timeline_available:
            factors["timeline_available"] = self.config.timeline_available_weight
            score -= self.config.timeline_available_weight

        value = min(score, self.config.max_confidence)
        label = self._confidence_label(value)

        return RcaConfidenceScore(value=value, label=label, factors=factors)

    def xǁRcaScorerǁcalculate_confidence__mutmut_18(
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
    ) -> RcaConfidenceScore:
        factors: dict[str, float] = {}
        score = self.config.base_confidence

        if logs_analyzed:
            factors["logs_analyzed"] = self.config.logs_analyzed_weight
            score += self.config.logs_analyzed_weight

        if root_cause_found:
            factors["root_cause_found"] = self.config.root_cause_found_weight
            score += self.config.root_cause_found_weight

        if timeline_available:
            factors["timeline_available"] = self.config.timeline_available_weight
            score += self.config.timeline_available_weight

        value = None
        label = self._confidence_label(value)

        return RcaConfidenceScore(value=value, label=label, factors=factors)

    def xǁRcaScorerǁcalculate_confidence__mutmut_19(
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
    ) -> RcaConfidenceScore:
        factors: dict[str, float] = {}
        score = self.config.base_confidence

        if logs_analyzed:
            factors["logs_analyzed"] = self.config.logs_analyzed_weight
            score += self.config.logs_analyzed_weight

        if root_cause_found:
            factors["root_cause_found"] = self.config.root_cause_found_weight
            score += self.config.root_cause_found_weight

        if timeline_available:
            factors["timeline_available"] = self.config.timeline_available_weight
            score += self.config.timeline_available_weight

        value = min(None, self.config.max_confidence)
        label = self._confidence_label(value)

        return RcaConfidenceScore(value=value, label=label, factors=factors)

    def xǁRcaScorerǁcalculate_confidence__mutmut_20(
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
    ) -> RcaConfidenceScore:
        factors: dict[str, float] = {}
        score = self.config.base_confidence

        if logs_analyzed:
            factors["logs_analyzed"] = self.config.logs_analyzed_weight
            score += self.config.logs_analyzed_weight

        if root_cause_found:
            factors["root_cause_found"] = self.config.root_cause_found_weight
            score += self.config.root_cause_found_weight

        if timeline_available:
            factors["timeline_available"] = self.config.timeline_available_weight
            score += self.config.timeline_available_weight

        value = min(score, None)
        label = self._confidence_label(value)

        return RcaConfidenceScore(value=value, label=label, factors=factors)

    def xǁRcaScorerǁcalculate_confidence__mutmut_21(
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
    ) -> RcaConfidenceScore:
        factors: dict[str, float] = {}
        score = self.config.base_confidence

        if logs_analyzed:
            factors["logs_analyzed"] = self.config.logs_analyzed_weight
            score += self.config.logs_analyzed_weight

        if root_cause_found:
            factors["root_cause_found"] = self.config.root_cause_found_weight
            score += self.config.root_cause_found_weight

        if timeline_available:
            factors["timeline_available"] = self.config.timeline_available_weight
            score += self.config.timeline_available_weight

        value = min(self.config.max_confidence)
        label = self._confidence_label(value)

        return RcaConfidenceScore(value=value, label=label, factors=factors)

    def xǁRcaScorerǁcalculate_confidence__mutmut_22(
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
    ) -> RcaConfidenceScore:
        factors: dict[str, float] = {}
        score = self.config.base_confidence

        if logs_analyzed:
            factors["logs_analyzed"] = self.config.logs_analyzed_weight
            score += self.config.logs_analyzed_weight

        if root_cause_found:
            factors["root_cause_found"] = self.config.root_cause_found_weight
            score += self.config.root_cause_found_weight

        if timeline_available:
            factors["timeline_available"] = self.config.timeline_available_weight
            score += self.config.timeline_available_weight

        value = min(score, )
        label = self._confidence_label(value)

        return RcaConfidenceScore(value=value, label=label, factors=factors)

    def xǁRcaScorerǁcalculate_confidence__mutmut_23(
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
    ) -> RcaConfidenceScore:
        factors: dict[str, float] = {}
        score = self.config.base_confidence

        if logs_analyzed:
            factors["logs_analyzed"] = self.config.logs_analyzed_weight
            score += self.config.logs_analyzed_weight

        if root_cause_found:
            factors["root_cause_found"] = self.config.root_cause_found_weight
            score += self.config.root_cause_found_weight

        if timeline_available:
            factors["timeline_available"] = self.config.timeline_available_weight
            score += self.config.timeline_available_weight

        value = min(score, self.config.max_confidence)
        label = None

        return RcaConfidenceScore(value=value, label=label, factors=factors)

    def xǁRcaScorerǁcalculate_confidence__mutmut_24(
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
    ) -> RcaConfidenceScore:
        factors: dict[str, float] = {}
        score = self.config.base_confidence

        if logs_analyzed:
            factors["logs_analyzed"] = self.config.logs_analyzed_weight
            score += self.config.logs_analyzed_weight

        if root_cause_found:
            factors["root_cause_found"] = self.config.root_cause_found_weight
            score += self.config.root_cause_found_weight

        if timeline_available:
            factors["timeline_available"] = self.config.timeline_available_weight
            score += self.config.timeline_available_weight

        value = min(score, self.config.max_confidence)
        label = self._confidence_label(None)

        return RcaConfidenceScore(value=value, label=label, factors=factors)

    def xǁRcaScorerǁcalculate_confidence__mutmut_25(
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
    ) -> RcaConfidenceScore:
        factors: dict[str, float] = {}
        score = self.config.base_confidence

        if logs_analyzed:
            factors["logs_analyzed"] = self.config.logs_analyzed_weight
            score += self.config.logs_analyzed_weight

        if root_cause_found:
            factors["root_cause_found"] = self.config.root_cause_found_weight
            score += self.config.root_cause_found_weight

        if timeline_available:
            factors["timeline_available"] = self.config.timeline_available_weight
            score += self.config.timeline_available_weight

        value = min(score, self.config.max_confidence)
        label = self._confidence_label(value)

        return RcaConfidenceScore(value=None, label=label, factors=factors)

    def xǁRcaScorerǁcalculate_confidence__mutmut_26(
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
    ) -> RcaConfidenceScore:
        factors: dict[str, float] = {}
        score = self.config.base_confidence

        if logs_analyzed:
            factors["logs_analyzed"] = self.config.logs_analyzed_weight
            score += self.config.logs_analyzed_weight

        if root_cause_found:
            factors["root_cause_found"] = self.config.root_cause_found_weight
            score += self.config.root_cause_found_weight

        if timeline_available:
            factors["timeline_available"] = self.config.timeline_available_weight
            score += self.config.timeline_available_weight

        value = min(score, self.config.max_confidence)
        label = self._confidence_label(value)

        return RcaConfidenceScore(value=value, label=None, factors=factors)

    def xǁRcaScorerǁcalculate_confidence__mutmut_27(
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
    ) -> RcaConfidenceScore:
        factors: dict[str, float] = {}
        score = self.config.base_confidence

        if logs_analyzed:
            factors["logs_analyzed"] = self.config.logs_analyzed_weight
            score += self.config.logs_analyzed_weight

        if root_cause_found:
            factors["root_cause_found"] = self.config.root_cause_found_weight
            score += self.config.root_cause_found_weight

        if timeline_available:
            factors["timeline_available"] = self.config.timeline_available_weight
            score += self.config.timeline_available_weight

        value = min(score, self.config.max_confidence)
        label = self._confidence_label(value)

        return RcaConfidenceScore(value=value, label=label, factors=None)

    def xǁRcaScorerǁcalculate_confidence__mutmut_28(
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
    ) -> RcaConfidenceScore:
        factors: dict[str, float] = {}
        score = self.config.base_confidence

        if logs_analyzed:
            factors["logs_analyzed"] = self.config.logs_analyzed_weight
            score += self.config.logs_analyzed_weight

        if root_cause_found:
            factors["root_cause_found"] = self.config.root_cause_found_weight
            score += self.config.root_cause_found_weight

        if timeline_available:
            factors["timeline_available"] = self.config.timeline_available_weight
            score += self.config.timeline_available_weight

        value = min(score, self.config.max_confidence)
        label = self._confidence_label(value)

        return RcaConfidenceScore(label=label, factors=factors)

    def xǁRcaScorerǁcalculate_confidence__mutmut_29(
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
    ) -> RcaConfidenceScore:
        factors: dict[str, float] = {}
        score = self.config.base_confidence

        if logs_analyzed:
            factors["logs_analyzed"] = self.config.logs_analyzed_weight
            score += self.config.logs_analyzed_weight

        if root_cause_found:
            factors["root_cause_found"] = self.config.root_cause_found_weight
            score += self.config.root_cause_found_weight

        if timeline_available:
            factors["timeline_available"] = self.config.timeline_available_weight
            score += self.config.timeline_available_weight

        value = min(score, self.config.max_confidence)
        label = self._confidence_label(value)

        return RcaConfidenceScore(value=value, factors=factors)

    def xǁRcaScorerǁcalculate_confidence__mutmut_30(
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
    ) -> RcaConfidenceScore:
        factors: dict[str, float] = {}
        score = self.config.base_confidence

        if logs_analyzed:
            factors["logs_analyzed"] = self.config.logs_analyzed_weight
            score += self.config.logs_analyzed_weight

        if root_cause_found:
            factors["root_cause_found"] = self.config.root_cause_found_weight
            score += self.config.root_cause_found_weight

        if timeline_available:
            factors["timeline_available"] = self.config.timeline_available_weight
            score += self.config.timeline_available_weight

        value = min(score, self.config.max_confidence)
        label = self._confidence_label(value)

        return RcaConfidenceScore(value=value, label=label, )

    @_mutmut_mutated(mutants_xǁRcaScorerǁcalculate_impact__mutmut)
    def calculate_impact(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score += affected_tasks * self.config.affected_task_weight
        score += related_incidents * self.config.related_incident_weight
        score += timeline_events * self.config.timeline_event_weight

        value = max(
            self.config.min_impact,
            min(score, self.config.max_impact),
        )
        label = self._impact_label(value)
        cascade_risk = self._cascade_risk(affected_tasks, related_incidents)

        return FailureImpactScore(
            value=value,
            label=label,
            affected_components=affected_tasks,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_orig(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score += affected_tasks * self.config.affected_task_weight
        score += related_incidents * self.config.related_incident_weight
        score += timeline_events * self.config.timeline_event_weight

        value = max(
            self.config.min_impact,
            min(score, self.config.max_impact),
        )
        label = self._impact_label(value)
        cascade_risk = self._cascade_risk(affected_tasks, related_incidents)

        return FailureImpactScore(
            value=value,
            label=label,
            affected_components=affected_tasks,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_1(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = None
        score += affected_tasks * self.config.affected_task_weight
        score += related_incidents * self.config.related_incident_weight
        score += timeline_events * self.config.timeline_event_weight

        value = max(
            self.config.min_impact,
            min(score, self.config.max_impact),
        )
        label = self._impact_label(value)
        cascade_risk = self._cascade_risk(affected_tasks, related_incidents)

        return FailureImpactScore(
            value=value,
            label=label,
            affected_components=affected_tasks,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_2(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score = affected_tasks * self.config.affected_task_weight
        score += related_incidents * self.config.related_incident_weight
        score += timeline_events * self.config.timeline_event_weight

        value = max(
            self.config.min_impact,
            min(score, self.config.max_impact),
        )
        label = self._impact_label(value)
        cascade_risk = self._cascade_risk(affected_tasks, related_incidents)

        return FailureImpactScore(
            value=value,
            label=label,
            affected_components=affected_tasks,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_3(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score -= affected_tasks * self.config.affected_task_weight
        score += related_incidents * self.config.related_incident_weight
        score += timeline_events * self.config.timeline_event_weight

        value = max(
            self.config.min_impact,
            min(score, self.config.max_impact),
        )
        label = self._impact_label(value)
        cascade_risk = self._cascade_risk(affected_tasks, related_incidents)

        return FailureImpactScore(
            value=value,
            label=label,
            affected_components=affected_tasks,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_4(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score += affected_tasks / self.config.affected_task_weight
        score += related_incidents * self.config.related_incident_weight
        score += timeline_events * self.config.timeline_event_weight

        value = max(
            self.config.min_impact,
            min(score, self.config.max_impact),
        )
        label = self._impact_label(value)
        cascade_risk = self._cascade_risk(affected_tasks, related_incidents)

        return FailureImpactScore(
            value=value,
            label=label,
            affected_components=affected_tasks,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_5(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score += affected_tasks * self.config.affected_task_weight
        score = related_incidents * self.config.related_incident_weight
        score += timeline_events * self.config.timeline_event_weight

        value = max(
            self.config.min_impact,
            min(score, self.config.max_impact),
        )
        label = self._impact_label(value)
        cascade_risk = self._cascade_risk(affected_tasks, related_incidents)

        return FailureImpactScore(
            value=value,
            label=label,
            affected_components=affected_tasks,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_6(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score += affected_tasks * self.config.affected_task_weight
        score -= related_incidents * self.config.related_incident_weight
        score += timeline_events * self.config.timeline_event_weight

        value = max(
            self.config.min_impact,
            min(score, self.config.max_impact),
        )
        label = self._impact_label(value)
        cascade_risk = self._cascade_risk(affected_tasks, related_incidents)

        return FailureImpactScore(
            value=value,
            label=label,
            affected_components=affected_tasks,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_7(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score += affected_tasks * self.config.affected_task_weight
        score += related_incidents / self.config.related_incident_weight
        score += timeline_events * self.config.timeline_event_weight

        value = max(
            self.config.min_impact,
            min(score, self.config.max_impact),
        )
        label = self._impact_label(value)
        cascade_risk = self._cascade_risk(affected_tasks, related_incidents)

        return FailureImpactScore(
            value=value,
            label=label,
            affected_components=affected_tasks,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_8(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score += affected_tasks * self.config.affected_task_weight
        score += related_incidents * self.config.related_incident_weight
        score = timeline_events * self.config.timeline_event_weight

        value = max(
            self.config.min_impact,
            min(score, self.config.max_impact),
        )
        label = self._impact_label(value)
        cascade_risk = self._cascade_risk(affected_tasks, related_incidents)

        return FailureImpactScore(
            value=value,
            label=label,
            affected_components=affected_tasks,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_9(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score += affected_tasks * self.config.affected_task_weight
        score += related_incidents * self.config.related_incident_weight
        score -= timeline_events * self.config.timeline_event_weight

        value = max(
            self.config.min_impact,
            min(score, self.config.max_impact),
        )
        label = self._impact_label(value)
        cascade_risk = self._cascade_risk(affected_tasks, related_incidents)

        return FailureImpactScore(
            value=value,
            label=label,
            affected_components=affected_tasks,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_10(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score += affected_tasks * self.config.affected_task_weight
        score += related_incidents * self.config.related_incident_weight
        score += timeline_events / self.config.timeline_event_weight

        value = max(
            self.config.min_impact,
            min(score, self.config.max_impact),
        )
        label = self._impact_label(value)
        cascade_risk = self._cascade_risk(affected_tasks, related_incidents)

        return FailureImpactScore(
            value=value,
            label=label,
            affected_components=affected_tasks,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_11(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score += affected_tasks * self.config.affected_task_weight
        score += related_incidents * self.config.related_incident_weight
        score += timeline_events * self.config.timeline_event_weight

        value = None
        label = self._impact_label(value)
        cascade_risk = self._cascade_risk(affected_tasks, related_incidents)

        return FailureImpactScore(
            value=value,
            label=label,
            affected_components=affected_tasks,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_12(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score += affected_tasks * self.config.affected_task_weight
        score += related_incidents * self.config.related_incident_weight
        score += timeline_events * self.config.timeline_event_weight

        value = max(
            None,
            min(score, self.config.max_impact),
        )
        label = self._impact_label(value)
        cascade_risk = self._cascade_risk(affected_tasks, related_incidents)

        return FailureImpactScore(
            value=value,
            label=label,
            affected_components=affected_tasks,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_13(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score += affected_tasks * self.config.affected_task_weight
        score += related_incidents * self.config.related_incident_weight
        score += timeline_events * self.config.timeline_event_weight

        value = max(
            self.config.min_impact,
            None,
        )
        label = self._impact_label(value)
        cascade_risk = self._cascade_risk(affected_tasks, related_incidents)

        return FailureImpactScore(
            value=value,
            label=label,
            affected_components=affected_tasks,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_14(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score += affected_tasks * self.config.affected_task_weight
        score += related_incidents * self.config.related_incident_weight
        score += timeline_events * self.config.timeline_event_weight

        value = max(
            min(score, self.config.max_impact),
        )
        label = self._impact_label(value)
        cascade_risk = self._cascade_risk(affected_tasks, related_incidents)

        return FailureImpactScore(
            value=value,
            label=label,
            affected_components=affected_tasks,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_15(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score += affected_tasks * self.config.affected_task_weight
        score += related_incidents * self.config.related_incident_weight
        score += timeline_events * self.config.timeline_event_weight

        value = max(
            self.config.min_impact,
            )
        label = self._impact_label(value)
        cascade_risk = self._cascade_risk(affected_tasks, related_incidents)

        return FailureImpactScore(
            value=value,
            label=label,
            affected_components=affected_tasks,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_16(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score += affected_tasks * self.config.affected_task_weight
        score += related_incidents * self.config.related_incident_weight
        score += timeline_events * self.config.timeline_event_weight

        value = max(
            self.config.min_impact,
            min(None, self.config.max_impact),
        )
        label = self._impact_label(value)
        cascade_risk = self._cascade_risk(affected_tasks, related_incidents)

        return FailureImpactScore(
            value=value,
            label=label,
            affected_components=affected_tasks,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_17(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score += affected_tasks * self.config.affected_task_weight
        score += related_incidents * self.config.related_incident_weight
        score += timeline_events * self.config.timeline_event_weight

        value = max(
            self.config.min_impact,
            min(score, None),
        )
        label = self._impact_label(value)
        cascade_risk = self._cascade_risk(affected_tasks, related_incidents)

        return FailureImpactScore(
            value=value,
            label=label,
            affected_components=affected_tasks,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_18(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score += affected_tasks * self.config.affected_task_weight
        score += related_incidents * self.config.related_incident_weight
        score += timeline_events * self.config.timeline_event_weight

        value = max(
            self.config.min_impact,
            min(self.config.max_impact),
        )
        label = self._impact_label(value)
        cascade_risk = self._cascade_risk(affected_tasks, related_incidents)

        return FailureImpactScore(
            value=value,
            label=label,
            affected_components=affected_tasks,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_19(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score += affected_tasks * self.config.affected_task_weight
        score += related_incidents * self.config.related_incident_weight
        score += timeline_events * self.config.timeline_event_weight

        value = max(
            self.config.min_impact,
            min(score, ),
        )
        label = self._impact_label(value)
        cascade_risk = self._cascade_risk(affected_tasks, related_incidents)

        return FailureImpactScore(
            value=value,
            label=label,
            affected_components=affected_tasks,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_20(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score += affected_tasks * self.config.affected_task_weight
        score += related_incidents * self.config.related_incident_weight
        score += timeline_events * self.config.timeline_event_weight

        value = max(
            self.config.min_impact,
            min(score, self.config.max_impact),
        )
        label = None
        cascade_risk = self._cascade_risk(affected_tasks, related_incidents)

        return FailureImpactScore(
            value=value,
            label=label,
            affected_components=affected_tasks,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_21(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score += affected_tasks * self.config.affected_task_weight
        score += related_incidents * self.config.related_incident_weight
        score += timeline_events * self.config.timeline_event_weight

        value = max(
            self.config.min_impact,
            min(score, self.config.max_impact),
        )
        label = self._impact_label(None)
        cascade_risk = self._cascade_risk(affected_tasks, related_incidents)

        return FailureImpactScore(
            value=value,
            label=label,
            affected_components=affected_tasks,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_22(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score += affected_tasks * self.config.affected_task_weight
        score += related_incidents * self.config.related_incident_weight
        score += timeline_events * self.config.timeline_event_weight

        value = max(
            self.config.min_impact,
            min(score, self.config.max_impact),
        )
        label = self._impact_label(value)
        cascade_risk = None

        return FailureImpactScore(
            value=value,
            label=label,
            affected_components=affected_tasks,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_23(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score += affected_tasks * self.config.affected_task_weight
        score += related_incidents * self.config.related_incident_weight
        score += timeline_events * self.config.timeline_event_weight

        value = max(
            self.config.min_impact,
            min(score, self.config.max_impact),
        )
        label = self._impact_label(value)
        cascade_risk = self._cascade_risk(None, related_incidents)

        return FailureImpactScore(
            value=value,
            label=label,
            affected_components=affected_tasks,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_24(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score += affected_tasks * self.config.affected_task_weight
        score += related_incidents * self.config.related_incident_weight
        score += timeline_events * self.config.timeline_event_weight

        value = max(
            self.config.min_impact,
            min(score, self.config.max_impact),
        )
        label = self._impact_label(value)
        cascade_risk = self._cascade_risk(affected_tasks, None)

        return FailureImpactScore(
            value=value,
            label=label,
            affected_components=affected_tasks,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_25(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score += affected_tasks * self.config.affected_task_weight
        score += related_incidents * self.config.related_incident_weight
        score += timeline_events * self.config.timeline_event_weight

        value = max(
            self.config.min_impact,
            min(score, self.config.max_impact),
        )
        label = self._impact_label(value)
        cascade_risk = self._cascade_risk(related_incidents)

        return FailureImpactScore(
            value=value,
            label=label,
            affected_components=affected_tasks,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_26(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score += affected_tasks * self.config.affected_task_weight
        score += related_incidents * self.config.related_incident_weight
        score += timeline_events * self.config.timeline_event_weight

        value = max(
            self.config.min_impact,
            min(score, self.config.max_impact),
        )
        label = self._impact_label(value)
        cascade_risk = self._cascade_risk(affected_tasks, )

        return FailureImpactScore(
            value=value,
            label=label,
            affected_components=affected_tasks,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_27(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score += affected_tasks * self.config.affected_task_weight
        score += related_incidents * self.config.related_incident_weight
        score += timeline_events * self.config.timeline_event_weight

        value = max(
            self.config.min_impact,
            min(score, self.config.max_impact),
        )
        label = self._impact_label(value)
        cascade_risk = self._cascade_risk(affected_tasks, related_incidents)

        return FailureImpactScore(
            value=None,
            label=label,
            affected_components=affected_tasks,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_28(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score += affected_tasks * self.config.affected_task_weight
        score += related_incidents * self.config.related_incident_weight
        score += timeline_events * self.config.timeline_event_weight

        value = max(
            self.config.min_impact,
            min(score, self.config.max_impact),
        )
        label = self._impact_label(value)
        cascade_risk = self._cascade_risk(affected_tasks, related_incidents)

        return FailureImpactScore(
            value=value,
            label=None,
            affected_components=affected_tasks,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_29(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score += affected_tasks * self.config.affected_task_weight
        score += related_incidents * self.config.related_incident_weight
        score += timeline_events * self.config.timeline_event_weight

        value = max(
            self.config.min_impact,
            min(score, self.config.max_impact),
        )
        label = self._impact_label(value)
        cascade_risk = self._cascade_risk(affected_tasks, related_incidents)

        return FailureImpactScore(
            value=value,
            label=label,
            affected_components=None,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_30(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score += affected_tasks * self.config.affected_task_weight
        score += related_incidents * self.config.related_incident_weight
        score += timeline_events * self.config.timeline_event_weight

        value = max(
            self.config.min_impact,
            min(score, self.config.max_impact),
        )
        label = self._impact_label(value)
        cascade_risk = self._cascade_risk(affected_tasks, related_incidents)

        return FailureImpactScore(
            value=value,
            label=label,
            affected_components=affected_tasks,
            cascade_risk=None,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_31(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score += affected_tasks * self.config.affected_task_weight
        score += related_incidents * self.config.related_incident_weight
        score += timeline_events * self.config.timeline_event_weight

        value = max(
            self.config.min_impact,
            min(score, self.config.max_impact),
        )
        label = self._impact_label(value)
        cascade_risk = self._cascade_risk(affected_tasks, related_incidents)

        return FailureImpactScore(
            label=label,
            affected_components=affected_tasks,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_32(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score += affected_tasks * self.config.affected_task_weight
        score += related_incidents * self.config.related_incident_weight
        score += timeline_events * self.config.timeline_event_weight

        value = max(
            self.config.min_impact,
            min(score, self.config.max_impact),
        )
        label = self._impact_label(value)
        cascade_risk = self._cascade_risk(affected_tasks, related_incidents)

        return FailureImpactScore(
            value=value,
            affected_components=affected_tasks,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_33(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score += affected_tasks * self.config.affected_task_weight
        score += related_incidents * self.config.related_incident_weight
        score += timeline_events * self.config.timeline_event_weight

        value = max(
            self.config.min_impact,
            min(score, self.config.max_impact),
        )
        label = self._impact_label(value)
        cascade_risk = self._cascade_risk(affected_tasks, related_incidents)

        return FailureImpactScore(
            value=value,
            label=label,
            cascade_risk=cascade_risk,
        )

    def xǁRcaScorerǁcalculate_impact__mutmut_34(
        self,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> FailureImpactScore:
        score = self.config.base_impact
        score += affected_tasks * self.config.affected_task_weight
        score += related_incidents * self.config.related_incident_weight
        score += timeline_events * self.config.timeline_event_weight

        value = max(
            self.config.min_impact,
            min(score, self.config.max_impact),
        )
        label = self._impact_label(value)
        cascade_risk = self._cascade_risk(affected_tasks, related_incidents)

        return FailureImpactScore(
            value=value,
            label=label,
            affected_components=affected_tasks,
            )

    @_mutmut_mutated(mutants_xǁRcaScorerǁassess_severity__mutmut)
    def assess_severity(  # noqa: PLR0913
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> dict[str, str | float]:
        confidence = self.calculate_confidence(logs_analyzed, root_cause_found, timeline_available)
        impact = self.calculate_impact(affected_tasks, related_incidents, timeline_events)

        combined = (confidence.value * _scoring.combined_confidence_weight) + (
            (impact.value / self.config.max_impact) * _scoring.combined_impact_weight
        )
        overall = self._overall_severity(combined)
        priority = self._priority(combined)

        return {
            "confidence": confidence.value,
            "impact": impact.value,
            "overall_severity": overall,
            "priority": priority,
        }

    def xǁRcaScorerǁassess_severity__mutmut_orig(  # noqa: PLR0913
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> dict[str, str | float]:
        confidence = self.calculate_confidence(logs_analyzed, root_cause_found, timeline_available)
        impact = self.calculate_impact(affected_tasks, related_incidents, timeline_events)

        combined = (confidence.value * _scoring.combined_confidence_weight) + (
            (impact.value / self.config.max_impact) * _scoring.combined_impact_weight
        )
        overall = self._overall_severity(combined)
        priority = self._priority(combined)

        return {
            "confidence": confidence.value,
            "impact": impact.value,
            "overall_severity": overall,
            "priority": priority,
        }

    def xǁRcaScorerǁassess_severity__mutmut_1(  # noqa: PLR0913
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> dict[str, str | float]:
        confidence = None
        impact = self.calculate_impact(affected_tasks, related_incidents, timeline_events)

        combined = (confidence.value * _scoring.combined_confidence_weight) + (
            (impact.value / self.config.max_impact) * _scoring.combined_impact_weight
        )
        overall = self._overall_severity(combined)
        priority = self._priority(combined)

        return {
            "confidence": confidence.value,
            "impact": impact.value,
            "overall_severity": overall,
            "priority": priority,
        }

    def xǁRcaScorerǁassess_severity__mutmut_2(  # noqa: PLR0913
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> dict[str, str | float]:
        confidence = self.calculate_confidence(None, root_cause_found, timeline_available)
        impact = self.calculate_impact(affected_tasks, related_incidents, timeline_events)

        combined = (confidence.value * _scoring.combined_confidence_weight) + (
            (impact.value / self.config.max_impact) * _scoring.combined_impact_weight
        )
        overall = self._overall_severity(combined)
        priority = self._priority(combined)

        return {
            "confidence": confidence.value,
            "impact": impact.value,
            "overall_severity": overall,
            "priority": priority,
        }

    def xǁRcaScorerǁassess_severity__mutmut_3(  # noqa: PLR0913
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> dict[str, str | float]:
        confidence = self.calculate_confidence(logs_analyzed, None, timeline_available)
        impact = self.calculate_impact(affected_tasks, related_incidents, timeline_events)

        combined = (confidence.value * _scoring.combined_confidence_weight) + (
            (impact.value / self.config.max_impact) * _scoring.combined_impact_weight
        )
        overall = self._overall_severity(combined)
        priority = self._priority(combined)

        return {
            "confidence": confidence.value,
            "impact": impact.value,
            "overall_severity": overall,
            "priority": priority,
        }

    def xǁRcaScorerǁassess_severity__mutmut_4(  # noqa: PLR0913
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> dict[str, str | float]:
        confidence = self.calculate_confidence(logs_analyzed, root_cause_found, None)
        impact = self.calculate_impact(affected_tasks, related_incidents, timeline_events)

        combined = (confidence.value * _scoring.combined_confidence_weight) + (
            (impact.value / self.config.max_impact) * _scoring.combined_impact_weight
        )
        overall = self._overall_severity(combined)
        priority = self._priority(combined)

        return {
            "confidence": confidence.value,
            "impact": impact.value,
            "overall_severity": overall,
            "priority": priority,
        }

    def xǁRcaScorerǁassess_severity__mutmut_5(  # noqa: PLR0913
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> dict[str, str | float]:
        confidence = self.calculate_confidence(root_cause_found, timeline_available)
        impact = self.calculate_impact(affected_tasks, related_incidents, timeline_events)

        combined = (confidence.value * _scoring.combined_confidence_weight) + (
            (impact.value / self.config.max_impact) * _scoring.combined_impact_weight
        )
        overall = self._overall_severity(combined)
        priority = self._priority(combined)

        return {
            "confidence": confidence.value,
            "impact": impact.value,
            "overall_severity": overall,
            "priority": priority,
        }

    def xǁRcaScorerǁassess_severity__mutmut_6(  # noqa: PLR0913
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> dict[str, str | float]:
        confidence = self.calculate_confidence(logs_analyzed, timeline_available)
        impact = self.calculate_impact(affected_tasks, related_incidents, timeline_events)

        combined = (confidence.value * _scoring.combined_confidence_weight) + (
            (impact.value / self.config.max_impact) * _scoring.combined_impact_weight
        )
        overall = self._overall_severity(combined)
        priority = self._priority(combined)

        return {
            "confidence": confidence.value,
            "impact": impact.value,
            "overall_severity": overall,
            "priority": priority,
        }

    def xǁRcaScorerǁassess_severity__mutmut_7(  # noqa: PLR0913
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> dict[str, str | float]:
        confidence = self.calculate_confidence(logs_analyzed, root_cause_found, )
        impact = self.calculate_impact(affected_tasks, related_incidents, timeline_events)

        combined = (confidence.value * _scoring.combined_confidence_weight) + (
            (impact.value / self.config.max_impact) * _scoring.combined_impact_weight
        )
        overall = self._overall_severity(combined)
        priority = self._priority(combined)

        return {
            "confidence": confidence.value,
            "impact": impact.value,
            "overall_severity": overall,
            "priority": priority,
        }

    def xǁRcaScorerǁassess_severity__mutmut_8(  # noqa: PLR0913
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> dict[str, str | float]:
        confidence = self.calculate_confidence(logs_analyzed, root_cause_found, timeline_available)
        impact = None

        combined = (confidence.value * _scoring.combined_confidence_weight) + (
            (impact.value / self.config.max_impact) * _scoring.combined_impact_weight
        )
        overall = self._overall_severity(combined)
        priority = self._priority(combined)

        return {
            "confidence": confidence.value,
            "impact": impact.value,
            "overall_severity": overall,
            "priority": priority,
        }

    def xǁRcaScorerǁassess_severity__mutmut_9(  # noqa: PLR0913
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> dict[str, str | float]:
        confidence = self.calculate_confidence(logs_analyzed, root_cause_found, timeline_available)
        impact = self.calculate_impact(None, related_incidents, timeline_events)

        combined = (confidence.value * _scoring.combined_confidence_weight) + (
            (impact.value / self.config.max_impact) * _scoring.combined_impact_weight
        )
        overall = self._overall_severity(combined)
        priority = self._priority(combined)

        return {
            "confidence": confidence.value,
            "impact": impact.value,
            "overall_severity": overall,
            "priority": priority,
        }

    def xǁRcaScorerǁassess_severity__mutmut_10(  # noqa: PLR0913
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> dict[str, str | float]:
        confidence = self.calculate_confidence(logs_analyzed, root_cause_found, timeline_available)
        impact = self.calculate_impact(affected_tasks, None, timeline_events)

        combined = (confidence.value * _scoring.combined_confidence_weight) + (
            (impact.value / self.config.max_impact) * _scoring.combined_impact_weight
        )
        overall = self._overall_severity(combined)
        priority = self._priority(combined)

        return {
            "confidence": confidence.value,
            "impact": impact.value,
            "overall_severity": overall,
            "priority": priority,
        }

    def xǁRcaScorerǁassess_severity__mutmut_11(  # noqa: PLR0913
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> dict[str, str | float]:
        confidence = self.calculate_confidence(logs_analyzed, root_cause_found, timeline_available)
        impact = self.calculate_impact(affected_tasks, related_incidents, None)

        combined = (confidence.value * _scoring.combined_confidence_weight) + (
            (impact.value / self.config.max_impact) * _scoring.combined_impact_weight
        )
        overall = self._overall_severity(combined)
        priority = self._priority(combined)

        return {
            "confidence": confidence.value,
            "impact": impact.value,
            "overall_severity": overall,
            "priority": priority,
        }

    def xǁRcaScorerǁassess_severity__mutmut_12(  # noqa: PLR0913
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> dict[str, str | float]:
        confidence = self.calculate_confidence(logs_analyzed, root_cause_found, timeline_available)
        impact = self.calculate_impact(related_incidents, timeline_events)

        combined = (confidence.value * _scoring.combined_confidence_weight) + (
            (impact.value / self.config.max_impact) * _scoring.combined_impact_weight
        )
        overall = self._overall_severity(combined)
        priority = self._priority(combined)

        return {
            "confidence": confidence.value,
            "impact": impact.value,
            "overall_severity": overall,
            "priority": priority,
        }

    def xǁRcaScorerǁassess_severity__mutmut_13(  # noqa: PLR0913
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> dict[str, str | float]:
        confidence = self.calculate_confidence(logs_analyzed, root_cause_found, timeline_available)
        impact = self.calculate_impact(affected_tasks, timeline_events)

        combined = (confidence.value * _scoring.combined_confidence_weight) + (
            (impact.value / self.config.max_impact) * _scoring.combined_impact_weight
        )
        overall = self._overall_severity(combined)
        priority = self._priority(combined)

        return {
            "confidence": confidence.value,
            "impact": impact.value,
            "overall_severity": overall,
            "priority": priority,
        }

    def xǁRcaScorerǁassess_severity__mutmut_14(  # noqa: PLR0913
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> dict[str, str | float]:
        confidence = self.calculate_confidence(logs_analyzed, root_cause_found, timeline_available)
        impact = self.calculate_impact(affected_tasks, related_incidents, )

        combined = (confidence.value * _scoring.combined_confidence_weight) + (
            (impact.value / self.config.max_impact) * _scoring.combined_impact_weight
        )
        overall = self._overall_severity(combined)
        priority = self._priority(combined)

        return {
            "confidence": confidence.value,
            "impact": impact.value,
            "overall_severity": overall,
            "priority": priority,
        }

    def xǁRcaScorerǁassess_severity__mutmut_15(  # noqa: PLR0913
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> dict[str, str | float]:
        confidence = self.calculate_confidence(logs_analyzed, root_cause_found, timeline_available)
        impact = self.calculate_impact(affected_tasks, related_incidents, timeline_events)

        combined = None
        overall = self._overall_severity(combined)
        priority = self._priority(combined)

        return {
            "confidence": confidence.value,
            "impact": impact.value,
            "overall_severity": overall,
            "priority": priority,
        }

    def xǁRcaScorerǁassess_severity__mutmut_16(  # noqa: PLR0913
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> dict[str, str | float]:
        confidence = self.calculate_confidence(logs_analyzed, root_cause_found, timeline_available)
        impact = self.calculate_impact(affected_tasks, related_incidents, timeline_events)

        combined = (confidence.value * _scoring.combined_confidence_weight) - (
            (impact.value / self.config.max_impact) * _scoring.combined_impact_weight
        )
        overall = self._overall_severity(combined)
        priority = self._priority(combined)

        return {
            "confidence": confidence.value,
            "impact": impact.value,
            "overall_severity": overall,
            "priority": priority,
        }

    def xǁRcaScorerǁassess_severity__mutmut_17(  # noqa: PLR0913
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> dict[str, str | float]:
        confidence = self.calculate_confidence(logs_analyzed, root_cause_found, timeline_available)
        impact = self.calculate_impact(affected_tasks, related_incidents, timeline_events)

        combined = (confidence.value / _scoring.combined_confidence_weight) + (
            (impact.value / self.config.max_impact) * _scoring.combined_impact_weight
        )
        overall = self._overall_severity(combined)
        priority = self._priority(combined)

        return {
            "confidence": confidence.value,
            "impact": impact.value,
            "overall_severity": overall,
            "priority": priority,
        }

    def xǁRcaScorerǁassess_severity__mutmut_18(  # noqa: PLR0913
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> dict[str, str | float]:
        confidence = self.calculate_confidence(logs_analyzed, root_cause_found, timeline_available)
        impact = self.calculate_impact(affected_tasks, related_incidents, timeline_events)

        combined = (confidence.value * _scoring.combined_confidence_weight) + (
            (impact.value / self.config.max_impact) / _scoring.combined_impact_weight
        )
        overall = self._overall_severity(combined)
        priority = self._priority(combined)

        return {
            "confidence": confidence.value,
            "impact": impact.value,
            "overall_severity": overall,
            "priority": priority,
        }

    def xǁRcaScorerǁassess_severity__mutmut_19(  # noqa: PLR0913
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> dict[str, str | float]:
        confidence = self.calculate_confidence(logs_analyzed, root_cause_found, timeline_available)
        impact = self.calculate_impact(affected_tasks, related_incidents, timeline_events)

        combined = (confidence.value * _scoring.combined_confidence_weight) + (
            (impact.value * self.config.max_impact) * _scoring.combined_impact_weight
        )
        overall = self._overall_severity(combined)
        priority = self._priority(combined)

        return {
            "confidence": confidence.value,
            "impact": impact.value,
            "overall_severity": overall,
            "priority": priority,
        }

    def xǁRcaScorerǁassess_severity__mutmut_20(  # noqa: PLR0913
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> dict[str, str | float]:
        confidence = self.calculate_confidence(logs_analyzed, root_cause_found, timeline_available)
        impact = self.calculate_impact(affected_tasks, related_incidents, timeline_events)

        combined = (confidence.value * _scoring.combined_confidence_weight) + (
            (impact.value / self.config.max_impact) * _scoring.combined_impact_weight
        )
        overall = None
        priority = self._priority(combined)

        return {
            "confidence": confidence.value,
            "impact": impact.value,
            "overall_severity": overall,
            "priority": priority,
        }

    def xǁRcaScorerǁassess_severity__mutmut_21(  # noqa: PLR0913
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> dict[str, str | float]:
        confidence = self.calculate_confidence(logs_analyzed, root_cause_found, timeline_available)
        impact = self.calculate_impact(affected_tasks, related_incidents, timeline_events)

        combined = (confidence.value * _scoring.combined_confidence_weight) + (
            (impact.value / self.config.max_impact) * _scoring.combined_impact_weight
        )
        overall = self._overall_severity(None)
        priority = self._priority(combined)

        return {
            "confidence": confidence.value,
            "impact": impact.value,
            "overall_severity": overall,
            "priority": priority,
        }

    def xǁRcaScorerǁassess_severity__mutmut_22(  # noqa: PLR0913
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> dict[str, str | float]:
        confidence = self.calculate_confidence(logs_analyzed, root_cause_found, timeline_available)
        impact = self.calculate_impact(affected_tasks, related_incidents, timeline_events)

        combined = (confidence.value * _scoring.combined_confidence_weight) + (
            (impact.value / self.config.max_impact) * _scoring.combined_impact_weight
        )
        overall = self._overall_severity(combined)
        priority = None

        return {
            "confidence": confidence.value,
            "impact": impact.value,
            "overall_severity": overall,
            "priority": priority,
        }

    def xǁRcaScorerǁassess_severity__mutmut_23(  # noqa: PLR0913
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> dict[str, str | float]:
        confidence = self.calculate_confidence(logs_analyzed, root_cause_found, timeline_available)
        impact = self.calculate_impact(affected_tasks, related_incidents, timeline_events)

        combined = (confidence.value * _scoring.combined_confidence_weight) + (
            (impact.value / self.config.max_impact) * _scoring.combined_impact_weight
        )
        overall = self._overall_severity(combined)
        priority = self._priority(None)

        return {
            "confidence": confidence.value,
            "impact": impact.value,
            "overall_severity": overall,
            "priority": priority,
        }

    def xǁRcaScorerǁassess_severity__mutmut_24(  # noqa: PLR0913
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> dict[str, str | float]:
        confidence = self.calculate_confidence(logs_analyzed, root_cause_found, timeline_available)
        impact = self.calculate_impact(affected_tasks, related_incidents, timeline_events)

        combined = (confidence.value * _scoring.combined_confidence_weight) + (
            (impact.value / self.config.max_impact) * _scoring.combined_impact_weight
        )
        overall = self._overall_severity(combined)
        priority = self._priority(combined)

        return {
            "XXconfidenceXX": confidence.value,
            "impact": impact.value,
            "overall_severity": overall,
            "priority": priority,
        }

    def xǁRcaScorerǁassess_severity__mutmut_25(  # noqa: PLR0913
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> dict[str, str | float]:
        confidence = self.calculate_confidence(logs_analyzed, root_cause_found, timeline_available)
        impact = self.calculate_impact(affected_tasks, related_incidents, timeline_events)

        combined = (confidence.value * _scoring.combined_confidence_weight) + (
            (impact.value / self.config.max_impact) * _scoring.combined_impact_weight
        )
        overall = self._overall_severity(combined)
        priority = self._priority(combined)

        return {
            "CONFIDENCE": confidence.value,
            "impact": impact.value,
            "overall_severity": overall,
            "priority": priority,
        }

    def xǁRcaScorerǁassess_severity__mutmut_26(  # noqa: PLR0913
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> dict[str, str | float]:
        confidence = self.calculate_confidence(logs_analyzed, root_cause_found, timeline_available)
        impact = self.calculate_impact(affected_tasks, related_incidents, timeline_events)

        combined = (confidence.value * _scoring.combined_confidence_weight) + (
            (impact.value / self.config.max_impact) * _scoring.combined_impact_weight
        )
        overall = self._overall_severity(combined)
        priority = self._priority(combined)

        return {
            "confidence": confidence.value,
            "XXimpactXX": impact.value,
            "overall_severity": overall,
            "priority": priority,
        }

    def xǁRcaScorerǁassess_severity__mutmut_27(  # noqa: PLR0913
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> dict[str, str | float]:
        confidence = self.calculate_confidence(logs_analyzed, root_cause_found, timeline_available)
        impact = self.calculate_impact(affected_tasks, related_incidents, timeline_events)

        combined = (confidence.value * _scoring.combined_confidence_weight) + (
            (impact.value / self.config.max_impact) * _scoring.combined_impact_weight
        )
        overall = self._overall_severity(combined)
        priority = self._priority(combined)

        return {
            "confidence": confidence.value,
            "IMPACT": impact.value,
            "overall_severity": overall,
            "priority": priority,
        }

    def xǁRcaScorerǁassess_severity__mutmut_28(  # noqa: PLR0913
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> dict[str, str | float]:
        confidence = self.calculate_confidence(logs_analyzed, root_cause_found, timeline_available)
        impact = self.calculate_impact(affected_tasks, related_incidents, timeline_events)

        combined = (confidence.value * _scoring.combined_confidence_weight) + (
            (impact.value / self.config.max_impact) * _scoring.combined_impact_weight
        )
        overall = self._overall_severity(combined)
        priority = self._priority(combined)

        return {
            "confidence": confidence.value,
            "impact": impact.value,
            "XXoverall_severityXX": overall,
            "priority": priority,
        }

    def xǁRcaScorerǁassess_severity__mutmut_29(  # noqa: PLR0913
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> dict[str, str | float]:
        confidence = self.calculate_confidence(logs_analyzed, root_cause_found, timeline_available)
        impact = self.calculate_impact(affected_tasks, related_incidents, timeline_events)

        combined = (confidence.value * _scoring.combined_confidence_weight) + (
            (impact.value / self.config.max_impact) * _scoring.combined_impact_weight
        )
        overall = self._overall_severity(combined)
        priority = self._priority(combined)

        return {
            "confidence": confidence.value,
            "impact": impact.value,
            "OVERALL_SEVERITY": overall,
            "priority": priority,
        }

    def xǁRcaScorerǁassess_severity__mutmut_30(  # noqa: PLR0913
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> dict[str, str | float]:
        confidence = self.calculate_confidence(logs_analyzed, root_cause_found, timeline_available)
        impact = self.calculate_impact(affected_tasks, related_incidents, timeline_events)

        combined = (confidence.value * _scoring.combined_confidence_weight) + (
            (impact.value / self.config.max_impact) * _scoring.combined_impact_weight
        )
        overall = self._overall_severity(combined)
        priority = self._priority(combined)

        return {
            "confidence": confidence.value,
            "impact": impact.value,
            "overall_severity": overall,
            "XXpriorityXX": priority,
        }

    def xǁRcaScorerǁassess_severity__mutmut_31(  # noqa: PLR0913
        self,
        logs_analyzed: bool,
        root_cause_found: bool,
        timeline_available: bool,
        affected_tasks: int,
        related_incidents: int,
        timeline_events: int,
    ) -> dict[str, str | float]:
        confidence = self.calculate_confidence(logs_analyzed, root_cause_found, timeline_available)
        impact = self.calculate_impact(affected_tasks, related_incidents, timeline_events)

        combined = (confidence.value * _scoring.combined_confidence_weight) + (
            (impact.value / self.config.max_impact) * _scoring.combined_impact_weight
        )
        overall = self._overall_severity(combined)
        priority = self._priority(combined)

        return {
            "confidence": confidence.value,
            "impact": impact.value,
            "overall_severity": overall,
            "PRIORITY": priority,
        }

    @staticmethod
    @_mutmut_mutated(mutants_xǁRcaScorerǁ_confidence_label__mutmut)
    def _confidence_label(value: float) -> str:
        if value >= _scoring.confidence_high_threshold:
            return "high"
        if value >= _scoring.confidence_medium_threshold:
            return "medium"
        return "low"

    @staticmethod
    def xǁRcaScorerǁ_confidence_label__mutmut_orig(value: float) -> str:
        if value >= _scoring.confidence_high_threshold:
            return "high"
        if value >= _scoring.confidence_medium_threshold:
            return "medium"
        return "low"

    @staticmethod
    def xǁRcaScorerǁ_confidence_label__mutmut_1(value: float) -> str:
        if value > _scoring.confidence_high_threshold:
            return "high"
        if value >= _scoring.confidence_medium_threshold:
            return "medium"
        return "low"

    @staticmethod
    def xǁRcaScorerǁ_confidence_label__mutmut_2(value: float) -> str:
        if value >= _scoring.confidence_high_threshold:
            return "XXhighXX"
        if value >= _scoring.confidence_medium_threshold:
            return "medium"
        return "low"

    @staticmethod
    def xǁRcaScorerǁ_confidence_label__mutmut_3(value: float) -> str:
        if value >= _scoring.confidence_high_threshold:
            return "HIGH"
        if value >= _scoring.confidence_medium_threshold:
            return "medium"
        return "low"

    @staticmethod
    def xǁRcaScorerǁ_confidence_label__mutmut_4(value: float) -> str:
        if value >= _scoring.confidence_high_threshold:
            return "high"
        if value > _scoring.confidence_medium_threshold:
            return "medium"
        return "low"

    @staticmethod
    def xǁRcaScorerǁ_confidence_label__mutmut_5(value: float) -> str:
        if value >= _scoring.confidence_high_threshold:
            return "high"
        if value >= _scoring.confidence_medium_threshold:
            return "XXmediumXX"
        return "low"

    @staticmethod
    def xǁRcaScorerǁ_confidence_label__mutmut_6(value: float) -> str:
        if value >= _scoring.confidence_high_threshold:
            return "high"
        if value >= _scoring.confidence_medium_threshold:
            return "MEDIUM"
        return "low"

    @staticmethod
    def xǁRcaScorerǁ_confidence_label__mutmut_7(value: float) -> str:
        if value >= _scoring.confidence_high_threshold:
            return "high"
        if value >= _scoring.confidence_medium_threshold:
            return "medium"
        return "XXlowXX"

    @staticmethod
    def xǁRcaScorerǁ_confidence_label__mutmut_8(value: float) -> str:
        if value >= _scoring.confidence_high_threshold:
            return "high"
        if value >= _scoring.confidence_medium_threshold:
            return "medium"
        return "LOW"

    @staticmethod
    @_mutmut_mutated(mutants_xǁRcaScorerǁ_impact_label__mutmut)
    def _impact_label(value: float) -> str:
        if value >= _scoring.impact_critical_threshold:
            return "critical"
        if value >= _scoring.impact_high_threshold:
            return "high"
        if value >= _scoring.impact_medium_threshold:
            return "medium"
        return "low"

    @staticmethod
    def xǁRcaScorerǁ_impact_label__mutmut_orig(value: float) -> str:
        if value >= _scoring.impact_critical_threshold:
            return "critical"
        if value >= _scoring.impact_high_threshold:
            return "high"
        if value >= _scoring.impact_medium_threshold:
            return "medium"
        return "low"

    @staticmethod
    def xǁRcaScorerǁ_impact_label__mutmut_1(value: float) -> str:
        if value > _scoring.impact_critical_threshold:
            return "critical"
        if value >= _scoring.impact_high_threshold:
            return "high"
        if value >= _scoring.impact_medium_threshold:
            return "medium"
        return "low"

    @staticmethod
    def xǁRcaScorerǁ_impact_label__mutmut_2(value: float) -> str:
        if value >= _scoring.impact_critical_threshold:
            return "XXcriticalXX"
        if value >= _scoring.impact_high_threshold:
            return "high"
        if value >= _scoring.impact_medium_threshold:
            return "medium"
        return "low"

    @staticmethod
    def xǁRcaScorerǁ_impact_label__mutmut_3(value: float) -> str:
        if value >= _scoring.impact_critical_threshold:
            return "CRITICAL"
        if value >= _scoring.impact_high_threshold:
            return "high"
        if value >= _scoring.impact_medium_threshold:
            return "medium"
        return "low"

    @staticmethod
    def xǁRcaScorerǁ_impact_label__mutmut_4(value: float) -> str:
        if value >= _scoring.impact_critical_threshold:
            return "critical"
        if value > _scoring.impact_high_threshold:
            return "high"
        if value >= _scoring.impact_medium_threshold:
            return "medium"
        return "low"

    @staticmethod
    def xǁRcaScorerǁ_impact_label__mutmut_5(value: float) -> str:
        if value >= _scoring.impact_critical_threshold:
            return "critical"
        if value >= _scoring.impact_high_threshold:
            return "XXhighXX"
        if value >= _scoring.impact_medium_threshold:
            return "medium"
        return "low"

    @staticmethod
    def xǁRcaScorerǁ_impact_label__mutmut_6(value: float) -> str:
        if value >= _scoring.impact_critical_threshold:
            return "critical"
        if value >= _scoring.impact_high_threshold:
            return "HIGH"
        if value >= _scoring.impact_medium_threshold:
            return "medium"
        return "low"

    @staticmethod
    def xǁRcaScorerǁ_impact_label__mutmut_7(value: float) -> str:
        if value >= _scoring.impact_critical_threshold:
            return "critical"
        if value >= _scoring.impact_high_threshold:
            return "high"
        if value > _scoring.impact_medium_threshold:
            return "medium"
        return "low"

    @staticmethod
    def xǁRcaScorerǁ_impact_label__mutmut_8(value: float) -> str:
        if value >= _scoring.impact_critical_threshold:
            return "critical"
        if value >= _scoring.impact_high_threshold:
            return "high"
        if value >= _scoring.impact_medium_threshold:
            return "XXmediumXX"
        return "low"

    @staticmethod
    def xǁRcaScorerǁ_impact_label__mutmut_9(value: float) -> str:
        if value >= _scoring.impact_critical_threshold:
            return "critical"
        if value >= _scoring.impact_high_threshold:
            return "high"
        if value >= _scoring.impact_medium_threshold:
            return "MEDIUM"
        return "low"

    @staticmethod
    def xǁRcaScorerǁ_impact_label__mutmut_10(value: float) -> str:
        if value >= _scoring.impact_critical_threshold:
            return "critical"
        if value >= _scoring.impact_high_threshold:
            return "high"
        if value >= _scoring.impact_medium_threshold:
            return "medium"
        return "XXlowXX"

    @staticmethod
    def xǁRcaScorerǁ_impact_label__mutmut_11(value: float) -> str:
        if value >= _scoring.impact_critical_threshold:
            return "critical"
        if value >= _scoring.impact_high_threshold:
            return "high"
        if value >= _scoring.impact_medium_threshold:
            return "medium"
        return "LOW"

    @staticmethod
    @_mutmut_mutated(mutants_xǁRcaScorerǁ_cascade_risk__mutmut)
    def _cascade_risk(affected_tasks: int, related_incidents: int) -> str:
        total = affected_tasks + related_incidents
        if total >= _scoring.cascade_high_threshold:
            return "high"
        if total >= _scoring.cascade_medium_threshold:
            return "medium"
        if total > 0:
            return "low"
        return "none"

    @staticmethod
    def xǁRcaScorerǁ_cascade_risk__mutmut_orig(affected_tasks: int, related_incidents: int) -> str:
        total = affected_tasks + related_incidents
        if total >= _scoring.cascade_high_threshold:
            return "high"
        if total >= _scoring.cascade_medium_threshold:
            return "medium"
        if total > 0:
            return "low"
        return "none"

    @staticmethod
    def xǁRcaScorerǁ_cascade_risk__mutmut_1(affected_tasks: int, related_incidents: int) -> str:
        total = None
        if total >= _scoring.cascade_high_threshold:
            return "high"
        if total >= _scoring.cascade_medium_threshold:
            return "medium"
        if total > 0:
            return "low"
        return "none"

    @staticmethod
    def xǁRcaScorerǁ_cascade_risk__mutmut_2(affected_tasks: int, related_incidents: int) -> str:
        total = affected_tasks - related_incidents
        if total >= _scoring.cascade_high_threshold:
            return "high"
        if total >= _scoring.cascade_medium_threshold:
            return "medium"
        if total > 0:
            return "low"
        return "none"

    @staticmethod
    def xǁRcaScorerǁ_cascade_risk__mutmut_3(affected_tasks: int, related_incidents: int) -> str:
        total = affected_tasks + related_incidents
        if total > _scoring.cascade_high_threshold:
            return "high"
        if total >= _scoring.cascade_medium_threshold:
            return "medium"
        if total > 0:
            return "low"
        return "none"

    @staticmethod
    def xǁRcaScorerǁ_cascade_risk__mutmut_4(affected_tasks: int, related_incidents: int) -> str:
        total = affected_tasks + related_incidents
        if total >= _scoring.cascade_high_threshold:
            return "XXhighXX"
        if total >= _scoring.cascade_medium_threshold:
            return "medium"
        if total > 0:
            return "low"
        return "none"

    @staticmethod
    def xǁRcaScorerǁ_cascade_risk__mutmut_5(affected_tasks: int, related_incidents: int) -> str:
        total = affected_tasks + related_incidents
        if total >= _scoring.cascade_high_threshold:
            return "HIGH"
        if total >= _scoring.cascade_medium_threshold:
            return "medium"
        if total > 0:
            return "low"
        return "none"

    @staticmethod
    def xǁRcaScorerǁ_cascade_risk__mutmut_6(affected_tasks: int, related_incidents: int) -> str:
        total = affected_tasks + related_incidents
        if total >= _scoring.cascade_high_threshold:
            return "high"
        if total > _scoring.cascade_medium_threshold:
            return "medium"
        if total > 0:
            return "low"
        return "none"

    @staticmethod
    def xǁRcaScorerǁ_cascade_risk__mutmut_7(affected_tasks: int, related_incidents: int) -> str:
        total = affected_tasks + related_incidents
        if total >= _scoring.cascade_high_threshold:
            return "high"
        if total >= _scoring.cascade_medium_threshold:
            return "XXmediumXX"
        if total > 0:
            return "low"
        return "none"

    @staticmethod
    def xǁRcaScorerǁ_cascade_risk__mutmut_8(affected_tasks: int, related_incidents: int) -> str:
        total = affected_tasks + related_incidents
        if total >= _scoring.cascade_high_threshold:
            return "high"
        if total >= _scoring.cascade_medium_threshold:
            return "MEDIUM"
        if total > 0:
            return "low"
        return "none"

    @staticmethod
    def xǁRcaScorerǁ_cascade_risk__mutmut_9(affected_tasks: int, related_incidents: int) -> str:
        total = affected_tasks + related_incidents
        if total >= _scoring.cascade_high_threshold:
            return "high"
        if total >= _scoring.cascade_medium_threshold:
            return "medium"
        if total >= 0:
            return "low"
        return "none"

    @staticmethod
    def xǁRcaScorerǁ_cascade_risk__mutmut_10(affected_tasks: int, related_incidents: int) -> str:
        total = affected_tasks + related_incidents
        if total >= _scoring.cascade_high_threshold:
            return "high"
        if total >= _scoring.cascade_medium_threshold:
            return "medium"
        if total > 1:
            return "low"
        return "none"

    @staticmethod
    def xǁRcaScorerǁ_cascade_risk__mutmut_11(affected_tasks: int, related_incidents: int) -> str:
        total = affected_tasks + related_incidents
        if total >= _scoring.cascade_high_threshold:
            return "high"
        if total >= _scoring.cascade_medium_threshold:
            return "medium"
        if total > 0:
            return "XXlowXX"
        return "none"

    @staticmethod
    def xǁRcaScorerǁ_cascade_risk__mutmut_12(affected_tasks: int, related_incidents: int) -> str:
        total = affected_tasks + related_incidents
        if total >= _scoring.cascade_high_threshold:
            return "high"
        if total >= _scoring.cascade_medium_threshold:
            return "medium"
        if total > 0:
            return "LOW"
        return "none"

    @staticmethod
    def xǁRcaScorerǁ_cascade_risk__mutmut_13(affected_tasks: int, related_incidents: int) -> str:
        total = affected_tasks + related_incidents
        if total >= _scoring.cascade_high_threshold:
            return "high"
        if total >= _scoring.cascade_medium_threshold:
            return "medium"
        if total > 0:
            return "low"
        return "XXnoneXX"

    @staticmethod
    def xǁRcaScorerǁ_cascade_risk__mutmut_14(affected_tasks: int, related_incidents: int) -> str:
        total = affected_tasks + related_incidents
        if total >= _scoring.cascade_high_threshold:
            return "high"
        if total >= _scoring.cascade_medium_threshold:
            return "medium"
        if total > 0:
            return "low"
        return "NONE"

    @staticmethod
    @_mutmut_mutated(mutants_xǁRcaScorerǁ_overall_severity__mutmut)
    def _overall_severity(combined: float) -> str:
        if combined >= _scoring.severity_critical_threshold:
            return "critical"
        if combined >= _scoring.severity_high_threshold:
            return "high"
        if combined >= _scoring.severity_medium_threshold:
            return "medium"
        return "low"

    @staticmethod
    def xǁRcaScorerǁ_overall_severity__mutmut_orig(combined: float) -> str:
        if combined >= _scoring.severity_critical_threshold:
            return "critical"
        if combined >= _scoring.severity_high_threshold:
            return "high"
        if combined >= _scoring.severity_medium_threshold:
            return "medium"
        return "low"

    @staticmethod
    def xǁRcaScorerǁ_overall_severity__mutmut_1(combined: float) -> str:
        if combined > _scoring.severity_critical_threshold:
            return "critical"
        if combined >= _scoring.severity_high_threshold:
            return "high"
        if combined >= _scoring.severity_medium_threshold:
            return "medium"
        return "low"

    @staticmethod
    def xǁRcaScorerǁ_overall_severity__mutmut_2(combined: float) -> str:
        if combined >= _scoring.severity_critical_threshold:
            return "XXcriticalXX"
        if combined >= _scoring.severity_high_threshold:
            return "high"
        if combined >= _scoring.severity_medium_threshold:
            return "medium"
        return "low"

    @staticmethod
    def xǁRcaScorerǁ_overall_severity__mutmut_3(combined: float) -> str:
        if combined >= _scoring.severity_critical_threshold:
            return "CRITICAL"
        if combined >= _scoring.severity_high_threshold:
            return "high"
        if combined >= _scoring.severity_medium_threshold:
            return "medium"
        return "low"

    @staticmethod
    def xǁRcaScorerǁ_overall_severity__mutmut_4(combined: float) -> str:
        if combined >= _scoring.severity_critical_threshold:
            return "critical"
        if combined > _scoring.severity_high_threshold:
            return "high"
        if combined >= _scoring.severity_medium_threshold:
            return "medium"
        return "low"

    @staticmethod
    def xǁRcaScorerǁ_overall_severity__mutmut_5(combined: float) -> str:
        if combined >= _scoring.severity_critical_threshold:
            return "critical"
        if combined >= _scoring.severity_high_threshold:
            return "XXhighXX"
        if combined >= _scoring.severity_medium_threshold:
            return "medium"
        return "low"

    @staticmethod
    def xǁRcaScorerǁ_overall_severity__mutmut_6(combined: float) -> str:
        if combined >= _scoring.severity_critical_threshold:
            return "critical"
        if combined >= _scoring.severity_high_threshold:
            return "HIGH"
        if combined >= _scoring.severity_medium_threshold:
            return "medium"
        return "low"

    @staticmethod
    def xǁRcaScorerǁ_overall_severity__mutmut_7(combined: float) -> str:
        if combined >= _scoring.severity_critical_threshold:
            return "critical"
        if combined >= _scoring.severity_high_threshold:
            return "high"
        if combined > _scoring.severity_medium_threshold:
            return "medium"
        return "low"

    @staticmethod
    def xǁRcaScorerǁ_overall_severity__mutmut_8(combined: float) -> str:
        if combined >= _scoring.severity_critical_threshold:
            return "critical"
        if combined >= _scoring.severity_high_threshold:
            return "high"
        if combined >= _scoring.severity_medium_threshold:
            return "XXmediumXX"
        return "low"

    @staticmethod
    def xǁRcaScorerǁ_overall_severity__mutmut_9(combined: float) -> str:
        if combined >= _scoring.severity_critical_threshold:
            return "critical"
        if combined >= _scoring.severity_high_threshold:
            return "high"
        if combined >= _scoring.severity_medium_threshold:
            return "MEDIUM"
        return "low"

    @staticmethod
    def xǁRcaScorerǁ_overall_severity__mutmut_10(combined: float) -> str:
        if combined >= _scoring.severity_critical_threshold:
            return "critical"
        if combined >= _scoring.severity_high_threshold:
            return "high"
        if combined >= _scoring.severity_medium_threshold:
            return "medium"
        return "XXlowXX"

    @staticmethod
    def xǁRcaScorerǁ_overall_severity__mutmut_11(combined: float) -> str:
        if combined >= _scoring.severity_critical_threshold:
            return "critical"
        if combined >= _scoring.severity_high_threshold:
            return "high"
        if combined >= _scoring.severity_medium_threshold:
            return "medium"
        return "LOW"

    @staticmethod
    @_mutmut_mutated(mutants_xǁRcaScorerǁ_priority__mutmut)
    def _priority(combined: float) -> str:
        if combined >= _scoring.severity_critical_threshold:
            return "P1"
        if combined >= _scoring.severity_high_threshold:
            return "P2"
        if combined >= _scoring.severity_medium_threshold:
            return "P3"
        return "P4"

    @staticmethod
    def xǁRcaScorerǁ_priority__mutmut_orig(combined: float) -> str:
        if combined >= _scoring.severity_critical_threshold:
            return "P1"
        if combined >= _scoring.severity_high_threshold:
            return "P2"
        if combined >= _scoring.severity_medium_threshold:
            return "P3"
        return "P4"

    @staticmethod
    def xǁRcaScorerǁ_priority__mutmut_1(combined: float) -> str:
        if combined > _scoring.severity_critical_threshold:
            return "P1"
        if combined >= _scoring.severity_high_threshold:
            return "P2"
        if combined >= _scoring.severity_medium_threshold:
            return "P3"
        return "P4"

    @staticmethod
    def xǁRcaScorerǁ_priority__mutmut_2(combined: float) -> str:
        if combined >= _scoring.severity_critical_threshold:
            return "XXP1XX"
        if combined >= _scoring.severity_high_threshold:
            return "P2"
        if combined >= _scoring.severity_medium_threshold:
            return "P3"
        return "P4"

    @staticmethod
    def xǁRcaScorerǁ_priority__mutmut_3(combined: float) -> str:
        if combined >= _scoring.severity_critical_threshold:
            return "p1"
        if combined >= _scoring.severity_high_threshold:
            return "P2"
        if combined >= _scoring.severity_medium_threshold:
            return "P3"
        return "P4"

    @staticmethod
    def xǁRcaScorerǁ_priority__mutmut_4(combined: float) -> str:
        if combined >= _scoring.severity_critical_threshold:
            return "P1"
        if combined > _scoring.severity_high_threshold:
            return "P2"
        if combined >= _scoring.severity_medium_threshold:
            return "P3"
        return "P4"

    @staticmethod
    def xǁRcaScorerǁ_priority__mutmut_5(combined: float) -> str:
        if combined >= _scoring.severity_critical_threshold:
            return "P1"
        if combined >= _scoring.severity_high_threshold:
            return "XXP2XX"
        if combined >= _scoring.severity_medium_threshold:
            return "P3"
        return "P4"

    @staticmethod
    def xǁRcaScorerǁ_priority__mutmut_6(combined: float) -> str:
        if combined >= _scoring.severity_critical_threshold:
            return "P1"
        if combined >= _scoring.severity_high_threshold:
            return "p2"
        if combined >= _scoring.severity_medium_threshold:
            return "P3"
        return "P4"

    @staticmethod
    def xǁRcaScorerǁ_priority__mutmut_7(combined: float) -> str:
        if combined >= _scoring.severity_critical_threshold:
            return "P1"
        if combined >= _scoring.severity_high_threshold:
            return "P2"
        if combined > _scoring.severity_medium_threshold:
            return "P3"
        return "P4"

    @staticmethod
    def xǁRcaScorerǁ_priority__mutmut_8(combined: float) -> str:
        if combined >= _scoring.severity_critical_threshold:
            return "P1"
        if combined >= _scoring.severity_high_threshold:
            return "P2"
        if combined >= _scoring.severity_medium_threshold:
            return "XXP3XX"
        return "P4"

    @staticmethod
    def xǁRcaScorerǁ_priority__mutmut_9(combined: float) -> str:
        if combined >= _scoring.severity_critical_threshold:
            return "P1"
        if combined >= _scoring.severity_high_threshold:
            return "P2"
        if combined >= _scoring.severity_medium_threshold:
            return "p3"
        return "P4"

    @staticmethod
    def xǁRcaScorerǁ_priority__mutmut_10(combined: float) -> str:
        if combined >= _scoring.severity_critical_threshold:
            return "P1"
        if combined >= _scoring.severity_high_threshold:
            return "P2"
        if combined >= _scoring.severity_medium_threshold:
            return "P3"
        return "XXP4XX"

    @staticmethod
    def xǁRcaScorerǁ_priority__mutmut_11(combined: float) -> str:
        if combined >= _scoring.severity_critical_threshold:
            return "P1"
        if combined >= _scoring.severity_high_threshold:
            return "P2"
        if combined >= _scoring.severity_medium_threshold:
            return "P3"
        return "p4"

mutants_xǁRcaScorerǁ__init____mutmut['_mutmut_orig'] = RcaScorer.xǁRcaScorerǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ__init____mutmut['xǁRcaScorerǁ__init____mutmut_1'] = RcaScorer.xǁRcaScorerǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ__init____mutmut['xǁRcaScorerǁ__init____mutmut_2'] = RcaScorer.xǁRcaScorerǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁRcaScorerǁcalculate_confidence__mutmut['_mutmut_orig'] = RcaScorer.xǁRcaScorerǁcalculate_confidence__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_confidence__mutmut['xǁRcaScorerǁcalculate_confidence__mutmut_1'] = RcaScorer.xǁRcaScorerǁcalculate_confidence__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_confidence__mutmut['xǁRcaScorerǁcalculate_confidence__mutmut_2'] = RcaScorer.xǁRcaScorerǁcalculate_confidence__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_confidence__mutmut['xǁRcaScorerǁcalculate_confidence__mutmut_3'] = RcaScorer.xǁRcaScorerǁcalculate_confidence__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_confidence__mutmut['xǁRcaScorerǁcalculate_confidence__mutmut_4'] = RcaScorer.xǁRcaScorerǁcalculate_confidence__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_confidence__mutmut['xǁRcaScorerǁcalculate_confidence__mutmut_5'] = RcaScorer.xǁRcaScorerǁcalculate_confidence__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_confidence__mutmut['xǁRcaScorerǁcalculate_confidence__mutmut_6'] = RcaScorer.xǁRcaScorerǁcalculate_confidence__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_confidence__mutmut['xǁRcaScorerǁcalculate_confidence__mutmut_7'] = RcaScorer.xǁRcaScorerǁcalculate_confidence__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_confidence__mutmut['xǁRcaScorerǁcalculate_confidence__mutmut_8'] = RcaScorer.xǁRcaScorerǁcalculate_confidence__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_confidence__mutmut['xǁRcaScorerǁcalculate_confidence__mutmut_9'] = RcaScorer.xǁRcaScorerǁcalculate_confidence__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_confidence__mutmut['xǁRcaScorerǁcalculate_confidence__mutmut_10'] = RcaScorer.xǁRcaScorerǁcalculate_confidence__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_confidence__mutmut['xǁRcaScorerǁcalculate_confidence__mutmut_11'] = RcaScorer.xǁRcaScorerǁcalculate_confidence__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_confidence__mutmut['xǁRcaScorerǁcalculate_confidence__mutmut_12'] = RcaScorer.xǁRcaScorerǁcalculate_confidence__mutmut_12 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_confidence__mutmut['xǁRcaScorerǁcalculate_confidence__mutmut_13'] = RcaScorer.xǁRcaScorerǁcalculate_confidence__mutmut_13 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_confidence__mutmut['xǁRcaScorerǁcalculate_confidence__mutmut_14'] = RcaScorer.xǁRcaScorerǁcalculate_confidence__mutmut_14 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_confidence__mutmut['xǁRcaScorerǁcalculate_confidence__mutmut_15'] = RcaScorer.xǁRcaScorerǁcalculate_confidence__mutmut_15 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_confidence__mutmut['xǁRcaScorerǁcalculate_confidence__mutmut_16'] = RcaScorer.xǁRcaScorerǁcalculate_confidence__mutmut_16 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_confidence__mutmut['xǁRcaScorerǁcalculate_confidence__mutmut_17'] = RcaScorer.xǁRcaScorerǁcalculate_confidence__mutmut_17 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_confidence__mutmut['xǁRcaScorerǁcalculate_confidence__mutmut_18'] = RcaScorer.xǁRcaScorerǁcalculate_confidence__mutmut_18 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_confidence__mutmut['xǁRcaScorerǁcalculate_confidence__mutmut_19'] = RcaScorer.xǁRcaScorerǁcalculate_confidence__mutmut_19 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_confidence__mutmut['xǁRcaScorerǁcalculate_confidence__mutmut_20'] = RcaScorer.xǁRcaScorerǁcalculate_confidence__mutmut_20 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_confidence__mutmut['xǁRcaScorerǁcalculate_confidence__mutmut_21'] = RcaScorer.xǁRcaScorerǁcalculate_confidence__mutmut_21 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_confidence__mutmut['xǁRcaScorerǁcalculate_confidence__mutmut_22'] = RcaScorer.xǁRcaScorerǁcalculate_confidence__mutmut_22 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_confidence__mutmut['xǁRcaScorerǁcalculate_confidence__mutmut_23'] = RcaScorer.xǁRcaScorerǁcalculate_confidence__mutmut_23 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_confidence__mutmut['xǁRcaScorerǁcalculate_confidence__mutmut_24'] = RcaScorer.xǁRcaScorerǁcalculate_confidence__mutmut_24 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_confidence__mutmut['xǁRcaScorerǁcalculate_confidence__mutmut_25'] = RcaScorer.xǁRcaScorerǁcalculate_confidence__mutmut_25 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_confidence__mutmut['xǁRcaScorerǁcalculate_confidence__mutmut_26'] = RcaScorer.xǁRcaScorerǁcalculate_confidence__mutmut_26 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_confidence__mutmut['xǁRcaScorerǁcalculate_confidence__mutmut_27'] = RcaScorer.xǁRcaScorerǁcalculate_confidence__mutmut_27 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_confidence__mutmut['xǁRcaScorerǁcalculate_confidence__mutmut_28'] = RcaScorer.xǁRcaScorerǁcalculate_confidence__mutmut_28 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_confidence__mutmut['xǁRcaScorerǁcalculate_confidence__mutmut_29'] = RcaScorer.xǁRcaScorerǁcalculate_confidence__mutmut_29 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_confidence__mutmut['xǁRcaScorerǁcalculate_confidence__mutmut_30'] = RcaScorer.xǁRcaScorerǁcalculate_confidence__mutmut_30 # type: ignore # mutmut generated

mutants_xǁRcaScorerǁcalculate_impact__mutmut['_mutmut_orig'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_1'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_2'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_3'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_4'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_5'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_6'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_7'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_8'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_9'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_10'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_11'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_12'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_12 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_13'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_13 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_14'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_14 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_15'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_15 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_16'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_16 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_17'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_17 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_18'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_18 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_19'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_19 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_20'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_20 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_21'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_21 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_22'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_22 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_23'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_23 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_24'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_24 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_25'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_25 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_26'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_26 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_27'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_27 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_28'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_28 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_29'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_29 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_30'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_30 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_31'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_31 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_32'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_32 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_33'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_33 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁcalculate_impact__mutmut['xǁRcaScorerǁcalculate_impact__mutmut_34'] = RcaScorer.xǁRcaScorerǁcalculate_impact__mutmut_34 # type: ignore # mutmut generated

mutants_xǁRcaScorerǁassess_severity__mutmut['_mutmut_orig'] = RcaScorer.xǁRcaScorerǁassess_severity__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRcaScorerǁassess_severity__mutmut['xǁRcaScorerǁassess_severity__mutmut_1'] = RcaScorer.xǁRcaScorerǁassess_severity__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁassess_severity__mutmut['xǁRcaScorerǁassess_severity__mutmut_2'] = RcaScorer.xǁRcaScorerǁassess_severity__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁassess_severity__mutmut['xǁRcaScorerǁassess_severity__mutmut_3'] = RcaScorer.xǁRcaScorerǁassess_severity__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁassess_severity__mutmut['xǁRcaScorerǁassess_severity__mutmut_4'] = RcaScorer.xǁRcaScorerǁassess_severity__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁassess_severity__mutmut['xǁRcaScorerǁassess_severity__mutmut_5'] = RcaScorer.xǁRcaScorerǁassess_severity__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁassess_severity__mutmut['xǁRcaScorerǁassess_severity__mutmut_6'] = RcaScorer.xǁRcaScorerǁassess_severity__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁassess_severity__mutmut['xǁRcaScorerǁassess_severity__mutmut_7'] = RcaScorer.xǁRcaScorerǁassess_severity__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁassess_severity__mutmut['xǁRcaScorerǁassess_severity__mutmut_8'] = RcaScorer.xǁRcaScorerǁassess_severity__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁassess_severity__mutmut['xǁRcaScorerǁassess_severity__mutmut_9'] = RcaScorer.xǁRcaScorerǁassess_severity__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁassess_severity__mutmut['xǁRcaScorerǁassess_severity__mutmut_10'] = RcaScorer.xǁRcaScorerǁassess_severity__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁassess_severity__mutmut['xǁRcaScorerǁassess_severity__mutmut_11'] = RcaScorer.xǁRcaScorerǁassess_severity__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁassess_severity__mutmut['xǁRcaScorerǁassess_severity__mutmut_12'] = RcaScorer.xǁRcaScorerǁassess_severity__mutmut_12 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁassess_severity__mutmut['xǁRcaScorerǁassess_severity__mutmut_13'] = RcaScorer.xǁRcaScorerǁassess_severity__mutmut_13 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁassess_severity__mutmut['xǁRcaScorerǁassess_severity__mutmut_14'] = RcaScorer.xǁRcaScorerǁassess_severity__mutmut_14 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁassess_severity__mutmut['xǁRcaScorerǁassess_severity__mutmut_15'] = RcaScorer.xǁRcaScorerǁassess_severity__mutmut_15 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁassess_severity__mutmut['xǁRcaScorerǁassess_severity__mutmut_16'] = RcaScorer.xǁRcaScorerǁassess_severity__mutmut_16 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁassess_severity__mutmut['xǁRcaScorerǁassess_severity__mutmut_17'] = RcaScorer.xǁRcaScorerǁassess_severity__mutmut_17 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁassess_severity__mutmut['xǁRcaScorerǁassess_severity__mutmut_18'] = RcaScorer.xǁRcaScorerǁassess_severity__mutmut_18 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁassess_severity__mutmut['xǁRcaScorerǁassess_severity__mutmut_19'] = RcaScorer.xǁRcaScorerǁassess_severity__mutmut_19 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁassess_severity__mutmut['xǁRcaScorerǁassess_severity__mutmut_20'] = RcaScorer.xǁRcaScorerǁassess_severity__mutmut_20 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁassess_severity__mutmut['xǁRcaScorerǁassess_severity__mutmut_21'] = RcaScorer.xǁRcaScorerǁassess_severity__mutmut_21 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁassess_severity__mutmut['xǁRcaScorerǁassess_severity__mutmut_22'] = RcaScorer.xǁRcaScorerǁassess_severity__mutmut_22 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁassess_severity__mutmut['xǁRcaScorerǁassess_severity__mutmut_23'] = RcaScorer.xǁRcaScorerǁassess_severity__mutmut_23 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁassess_severity__mutmut['xǁRcaScorerǁassess_severity__mutmut_24'] = RcaScorer.xǁRcaScorerǁassess_severity__mutmut_24 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁassess_severity__mutmut['xǁRcaScorerǁassess_severity__mutmut_25'] = RcaScorer.xǁRcaScorerǁassess_severity__mutmut_25 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁassess_severity__mutmut['xǁRcaScorerǁassess_severity__mutmut_26'] = RcaScorer.xǁRcaScorerǁassess_severity__mutmut_26 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁassess_severity__mutmut['xǁRcaScorerǁassess_severity__mutmut_27'] = RcaScorer.xǁRcaScorerǁassess_severity__mutmut_27 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁassess_severity__mutmut['xǁRcaScorerǁassess_severity__mutmut_28'] = RcaScorer.xǁRcaScorerǁassess_severity__mutmut_28 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁassess_severity__mutmut['xǁRcaScorerǁassess_severity__mutmut_29'] = RcaScorer.xǁRcaScorerǁassess_severity__mutmut_29 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁassess_severity__mutmut['xǁRcaScorerǁassess_severity__mutmut_30'] = RcaScorer.xǁRcaScorerǁassess_severity__mutmut_30 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁassess_severity__mutmut['xǁRcaScorerǁassess_severity__mutmut_31'] = RcaScorer.xǁRcaScorerǁassess_severity__mutmut_31 # type: ignore # mutmut generated

mutants_xǁRcaScorerǁ_confidence_label__mutmut['_mutmut_orig'] = RcaScorer.xǁRcaScorerǁ_confidence_label__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_confidence_label__mutmut['xǁRcaScorerǁ_confidence_label__mutmut_1'] = RcaScorer.xǁRcaScorerǁ_confidence_label__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_confidence_label__mutmut['xǁRcaScorerǁ_confidence_label__mutmut_2'] = RcaScorer.xǁRcaScorerǁ_confidence_label__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_confidence_label__mutmut['xǁRcaScorerǁ_confidence_label__mutmut_3'] = RcaScorer.xǁRcaScorerǁ_confidence_label__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_confidence_label__mutmut['xǁRcaScorerǁ_confidence_label__mutmut_4'] = RcaScorer.xǁRcaScorerǁ_confidence_label__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_confidence_label__mutmut['xǁRcaScorerǁ_confidence_label__mutmut_5'] = RcaScorer.xǁRcaScorerǁ_confidence_label__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_confidence_label__mutmut['xǁRcaScorerǁ_confidence_label__mutmut_6'] = RcaScorer.xǁRcaScorerǁ_confidence_label__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_confidence_label__mutmut['xǁRcaScorerǁ_confidence_label__mutmut_7'] = RcaScorer.xǁRcaScorerǁ_confidence_label__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_confidence_label__mutmut['xǁRcaScorerǁ_confidence_label__mutmut_8'] = RcaScorer.xǁRcaScorerǁ_confidence_label__mutmut_8 # type: ignore # mutmut generated

mutants_xǁRcaScorerǁ_impact_label__mutmut['_mutmut_orig'] = RcaScorer.xǁRcaScorerǁ_impact_label__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_impact_label__mutmut['xǁRcaScorerǁ_impact_label__mutmut_1'] = RcaScorer.xǁRcaScorerǁ_impact_label__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_impact_label__mutmut['xǁRcaScorerǁ_impact_label__mutmut_2'] = RcaScorer.xǁRcaScorerǁ_impact_label__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_impact_label__mutmut['xǁRcaScorerǁ_impact_label__mutmut_3'] = RcaScorer.xǁRcaScorerǁ_impact_label__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_impact_label__mutmut['xǁRcaScorerǁ_impact_label__mutmut_4'] = RcaScorer.xǁRcaScorerǁ_impact_label__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_impact_label__mutmut['xǁRcaScorerǁ_impact_label__mutmut_5'] = RcaScorer.xǁRcaScorerǁ_impact_label__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_impact_label__mutmut['xǁRcaScorerǁ_impact_label__mutmut_6'] = RcaScorer.xǁRcaScorerǁ_impact_label__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_impact_label__mutmut['xǁRcaScorerǁ_impact_label__mutmut_7'] = RcaScorer.xǁRcaScorerǁ_impact_label__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_impact_label__mutmut['xǁRcaScorerǁ_impact_label__mutmut_8'] = RcaScorer.xǁRcaScorerǁ_impact_label__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_impact_label__mutmut['xǁRcaScorerǁ_impact_label__mutmut_9'] = RcaScorer.xǁRcaScorerǁ_impact_label__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_impact_label__mutmut['xǁRcaScorerǁ_impact_label__mutmut_10'] = RcaScorer.xǁRcaScorerǁ_impact_label__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_impact_label__mutmut['xǁRcaScorerǁ_impact_label__mutmut_11'] = RcaScorer.xǁRcaScorerǁ_impact_label__mutmut_11 # type: ignore # mutmut generated

mutants_xǁRcaScorerǁ_cascade_risk__mutmut['_mutmut_orig'] = RcaScorer.xǁRcaScorerǁ_cascade_risk__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_cascade_risk__mutmut['xǁRcaScorerǁ_cascade_risk__mutmut_1'] = RcaScorer.xǁRcaScorerǁ_cascade_risk__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_cascade_risk__mutmut['xǁRcaScorerǁ_cascade_risk__mutmut_2'] = RcaScorer.xǁRcaScorerǁ_cascade_risk__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_cascade_risk__mutmut['xǁRcaScorerǁ_cascade_risk__mutmut_3'] = RcaScorer.xǁRcaScorerǁ_cascade_risk__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_cascade_risk__mutmut['xǁRcaScorerǁ_cascade_risk__mutmut_4'] = RcaScorer.xǁRcaScorerǁ_cascade_risk__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_cascade_risk__mutmut['xǁRcaScorerǁ_cascade_risk__mutmut_5'] = RcaScorer.xǁRcaScorerǁ_cascade_risk__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_cascade_risk__mutmut['xǁRcaScorerǁ_cascade_risk__mutmut_6'] = RcaScorer.xǁRcaScorerǁ_cascade_risk__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_cascade_risk__mutmut['xǁRcaScorerǁ_cascade_risk__mutmut_7'] = RcaScorer.xǁRcaScorerǁ_cascade_risk__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_cascade_risk__mutmut['xǁRcaScorerǁ_cascade_risk__mutmut_8'] = RcaScorer.xǁRcaScorerǁ_cascade_risk__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_cascade_risk__mutmut['xǁRcaScorerǁ_cascade_risk__mutmut_9'] = RcaScorer.xǁRcaScorerǁ_cascade_risk__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_cascade_risk__mutmut['xǁRcaScorerǁ_cascade_risk__mutmut_10'] = RcaScorer.xǁRcaScorerǁ_cascade_risk__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_cascade_risk__mutmut['xǁRcaScorerǁ_cascade_risk__mutmut_11'] = RcaScorer.xǁRcaScorerǁ_cascade_risk__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_cascade_risk__mutmut['xǁRcaScorerǁ_cascade_risk__mutmut_12'] = RcaScorer.xǁRcaScorerǁ_cascade_risk__mutmut_12 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_cascade_risk__mutmut['xǁRcaScorerǁ_cascade_risk__mutmut_13'] = RcaScorer.xǁRcaScorerǁ_cascade_risk__mutmut_13 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_cascade_risk__mutmut['xǁRcaScorerǁ_cascade_risk__mutmut_14'] = RcaScorer.xǁRcaScorerǁ_cascade_risk__mutmut_14 # type: ignore # mutmut generated

mutants_xǁRcaScorerǁ_overall_severity__mutmut['_mutmut_orig'] = RcaScorer.xǁRcaScorerǁ_overall_severity__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_overall_severity__mutmut['xǁRcaScorerǁ_overall_severity__mutmut_1'] = RcaScorer.xǁRcaScorerǁ_overall_severity__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_overall_severity__mutmut['xǁRcaScorerǁ_overall_severity__mutmut_2'] = RcaScorer.xǁRcaScorerǁ_overall_severity__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_overall_severity__mutmut['xǁRcaScorerǁ_overall_severity__mutmut_3'] = RcaScorer.xǁRcaScorerǁ_overall_severity__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_overall_severity__mutmut['xǁRcaScorerǁ_overall_severity__mutmut_4'] = RcaScorer.xǁRcaScorerǁ_overall_severity__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_overall_severity__mutmut['xǁRcaScorerǁ_overall_severity__mutmut_5'] = RcaScorer.xǁRcaScorerǁ_overall_severity__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_overall_severity__mutmut['xǁRcaScorerǁ_overall_severity__mutmut_6'] = RcaScorer.xǁRcaScorerǁ_overall_severity__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_overall_severity__mutmut['xǁRcaScorerǁ_overall_severity__mutmut_7'] = RcaScorer.xǁRcaScorerǁ_overall_severity__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_overall_severity__mutmut['xǁRcaScorerǁ_overall_severity__mutmut_8'] = RcaScorer.xǁRcaScorerǁ_overall_severity__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_overall_severity__mutmut['xǁRcaScorerǁ_overall_severity__mutmut_9'] = RcaScorer.xǁRcaScorerǁ_overall_severity__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_overall_severity__mutmut['xǁRcaScorerǁ_overall_severity__mutmut_10'] = RcaScorer.xǁRcaScorerǁ_overall_severity__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_overall_severity__mutmut['xǁRcaScorerǁ_overall_severity__mutmut_11'] = RcaScorer.xǁRcaScorerǁ_overall_severity__mutmut_11 # type: ignore # mutmut generated

mutants_xǁRcaScorerǁ_priority__mutmut['_mutmut_orig'] = RcaScorer.xǁRcaScorerǁ_priority__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_priority__mutmut['xǁRcaScorerǁ_priority__mutmut_1'] = RcaScorer.xǁRcaScorerǁ_priority__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_priority__mutmut['xǁRcaScorerǁ_priority__mutmut_2'] = RcaScorer.xǁRcaScorerǁ_priority__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_priority__mutmut['xǁRcaScorerǁ_priority__mutmut_3'] = RcaScorer.xǁRcaScorerǁ_priority__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_priority__mutmut['xǁRcaScorerǁ_priority__mutmut_4'] = RcaScorer.xǁRcaScorerǁ_priority__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_priority__mutmut['xǁRcaScorerǁ_priority__mutmut_5'] = RcaScorer.xǁRcaScorerǁ_priority__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_priority__mutmut['xǁRcaScorerǁ_priority__mutmut_6'] = RcaScorer.xǁRcaScorerǁ_priority__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_priority__mutmut['xǁRcaScorerǁ_priority__mutmut_7'] = RcaScorer.xǁRcaScorerǁ_priority__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_priority__mutmut['xǁRcaScorerǁ_priority__mutmut_8'] = RcaScorer.xǁRcaScorerǁ_priority__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_priority__mutmut['xǁRcaScorerǁ_priority__mutmut_9'] = RcaScorer.xǁRcaScorerǁ_priority__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_priority__mutmut['xǁRcaScorerǁ_priority__mutmut_10'] = RcaScorer.xǁRcaScorerǁ_priority__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRcaScorerǁ_priority__mutmut['xǁRcaScorerǁ_priority__mutmut_11'] = RcaScorer.xǁRcaScorerǁ_priority__mutmut_11 # type: ignore # mutmut generated
