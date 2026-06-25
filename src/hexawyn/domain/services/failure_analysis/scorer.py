from hexawyn.domain.models.constants import ScoringConstants
from hexawyn.domain.models.scoring import (
    FailureImpactScore,
    RcaConfidenceScore,
    RcaScoringConfig,
)

_scoring = ScoringConstants()


class RcaScorer:
    """Calculates confidence and impact scores for root cause analysis.

    Uses config-driven additive scoring with min/max clamping.
    Weights are defined in RcaScoringConfig — no hardcoded magic numbers.
    """

    def __init__(self, config: RcaScoringConfig | None = None) -> None:
        self.config = config or RcaScoringConfig()

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

    def assess_severity(
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

    @staticmethod
    def _confidence_label(value: float) -> str:
        if value >= _scoring.confidence_high_threshold:
            return "high"
        if value >= _scoring.confidence_medium_threshold:
            return "medium"
        return "low"

    @staticmethod
    def _impact_label(value: float) -> str:
        if value >= _scoring.impact_critical_threshold:
            return "critical"
        if value >= _scoring.impact_high_threshold:
            return "high"
        if value >= _scoring.impact_medium_threshold:
            return "medium"
        return "low"

    @staticmethod
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
    def _overall_severity(combined: float) -> str:
        if combined >= _scoring.severity_critical_threshold:
            return "critical"
        if combined >= _scoring.severity_high_threshold:
            return "high"
        if combined >= _scoring.severity_medium_threshold:
            return "medium"
        return "low"

    @staticmethod
    def _priority(combined: float) -> str:
        if combined >= _scoring.severity_critical_threshold:
            return "P1"
        if combined >= _scoring.severity_high_threshold:
            return "P2"
        if combined >= _scoring.severity_medium_threshold:
            return "P3"
        return "P4"
