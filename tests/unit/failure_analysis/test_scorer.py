"""Unit tests for the RCA scorer."""

import pytest
from hexawyn.domain.models.scoring import RcaScoringConfig
from hexawyn.domain.services.failure_analysis.scorer import RcaScorer


class TestRcaScorerConfidence:
    def test_max_confidence_when_all_factors_present(self) -> None:
        scorer = RcaScorer()
        score = scorer.calculate_confidence(
            logs_analyzed=True,
            root_cause_found=True,
            timeline_available=True,
        )
        assert score.value == pytest.approx(1.0)
        assert score.label == "high"

    def test_base_confidence_when_no_factors(self) -> None:
        scorer = RcaScorer()
        score = scorer.calculate_confidence(
            logs_analyzed=False,
            root_cause_found=False,
            timeline_available=False,
        )
        assert score.value == 0.5
        assert score.label == "medium"

    def test_partial_factors(self) -> None:
        scorer = RcaScorer()
        score = scorer.calculate_confidence(
            logs_analyzed=True,
            root_cause_found=False,
            timeline_available=True,
        )
        assert 0.5 < score.value < 1.0

    def test_never_exceeds_max(self) -> None:
        scorer = RcaScorer()
        score = scorer.calculate_confidence(
            logs_analyzed=True,
            root_cause_found=True,
            timeline_available=True,
        )
        assert score.value <= scorer.config.max_confidence

    def test_custom_config_affects_score(self) -> None:
        config = RcaScoringConfig(
            base_confidence=0.3,
            logs_analyzed_weight=0.4,
        )
        scorer = RcaScorer(config)
        score = scorer.calculate_confidence(
            logs_analyzed=True,
            root_cause_found=False,
            timeline_available=False,
        )
        assert score.value == 0.7

    def test_labels_map_correctly(self) -> None:
        scorer = RcaScorer()
        low = scorer.calculate_confidence(False, False, False)
        medium = scorer.calculate_confidence(True, False, False)
        high = scorer.calculate_confidence(True, True, True)
        assert low.label == "medium"
        assert medium.label == "medium"
        assert high.label == "high"


class TestRcaScorerImpact:
    def test_base_impact_when_no_factors(self) -> None:
        scorer = RcaScorer()
        score = scorer.calculate_impact(
            affected_tasks=0,
            related_incidents=0,
            timeline_events=0,
        )
        assert score.value == 5.0

    def test_impact_increases_with_affected_tasks(self) -> None:
        scorer = RcaScorer()
        no_tasks = scorer.calculate_impact(0, 0, 0)
        with_tasks = scorer.calculate_impact(4, 0, 0)
        assert with_tasks.value > no_tasks.value

    def test_impact_increases_with_related_incidents(self) -> None:
        scorer = RcaScorer()
        no_related = scorer.calculate_impact(0, 0, 0)
        with_related = scorer.calculate_impact(0, 3, 0)
        assert with_related.value > no_related.value

    def test_impact_capped_at_max(self) -> None:
        scorer = RcaScorer()
        score = scorer.calculate_impact(
            affected_tasks=100,
            related_incidents=100,
            timeline_events=100,
        )
        assert score.value <= scorer.config.max_impact

    def test_impact_never_below_min(self) -> None:
        scorer = RcaScorer(config=RcaScoringConfig(base_impact=1.0, min_impact=1.0))
        score = scorer.calculate_impact(0, 0, 0)
        assert score.value >= scorer.config.min_impact

    def test_labels_map_correctly(self) -> None:
        scorer = RcaScorer()
        low = scorer.calculate_impact(0, 0, 0)
        high = scorer.calculate_impact(10, 5, 8)
        assert low.label == "medium"
        assert high.label == "critical"


class TestRcaScorerCombined:
    def test_assess_severity_combines_confidence_and_impact(self) -> None:
        scorer = RcaScorer()
        result = scorer.assess_severity(
            logs_analyzed=True,
            root_cause_found=True,
            timeline_available=True,
            affected_tasks=3,
            related_incidents=2,
            timeline_events=5,
        )
        assert "confidence" in result
        assert "impact" in result
        assert "overall_severity" in result
        assert "priority" in result

    def test_critical_severity_for_high_scores(self) -> None:
        scorer = RcaScorer()
        result = scorer.assess_severity(
            logs_analyzed=True,
            root_cause_found=True,
            timeline_available=True,
            affected_tasks=10,
            related_incidents=8,
            timeline_events=20,
        )
        assert result["overall_severity"] == "critical"
        assert result["priority"] == "P1"

    def test_low_severity_for_minimal_inputs(self) -> None:
        scorer = RcaScorer()
        result = scorer.assess_severity(
            logs_analyzed=False,
            root_cause_found=False,
            timeline_available=False,
            affected_tasks=0,
            related_incidents=0,
            timeline_events=0,
        )
        assert result["overall_severity"] == "medium"
        assert result["priority"] == "P3"
