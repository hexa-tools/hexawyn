"""Unit tests for RCA scoring domain models."""

import dataclasses

from hexawyn.domain.models.scoring import (
    FailureImpactScore,
    RcaConfidenceScore,
    RcaScoringConfig,
)


class TestRcaScoringConfig:
    def test_defaults(self) -> None:
        config = RcaScoringConfig()
        assert config.base_confidence == 0.5
        assert config.logs_analyzed_weight == 0.2
        assert config.root_cause_found_weight == 0.2
        assert config.timeline_available_weight == 0.1
        assert config.max_confidence == 1.0
        assert config.base_impact == 5.0
        assert config.affected_task_weight == 0.5
        assert config.related_incident_weight == 1.0
        assert config.timeline_event_weight == 0.2
        assert config.max_impact == 10.0
        assert config.min_impact == 1.0

    def test_custom_config(self) -> None:
        config = RcaScoringConfig(
            base_confidence=0.6,
            max_confidence=0.95,
            base_impact=3.0,
            max_impact=8.0,
        )
        assert config.base_confidence == 0.6
        assert config.base_impact == 3.0

    def test_is_dataclass(self) -> None:
        assert dataclasses.is_dataclass(RcaScoringConfig)


class TestRcaConfidenceScore:
    def test_defaults(self) -> None:
        score = RcaConfidenceScore()
        assert score.value == 0.0
        assert score.label == "unknown"
        assert score.factors == {}

    def test_full_construction(self) -> None:
        score = RcaConfidenceScore(
            value=0.85,
            label="high",
            factors={"logs": 0.2, "root_cause": 0.15},
        )
        assert score.value == 0.85
        assert score.label == "high"
        assert score.factors["logs"] == 0.2

    def test_is_dataclass(self) -> None:
        assert dataclasses.is_dataclass(RcaConfidenceScore)


class TestFailureImpactScore:
    def test_defaults(self) -> None:
        score = FailureImpactScore()
        assert score.value == 0.0
        assert score.label == "unknown"
        assert score.affected_components == 0

    def test_full_construction(self) -> None:
        score = FailureImpactScore(
            value=8.5,
            label="critical",
            affected_components=3,
            cascade_risk="high",
        )
        assert score.value == 8.5
        assert score.label == "critical"
        assert score.affected_components == 3
        assert score.cascade_risk == "high"

    def test_is_dataclass(self) -> None:
        assert dataclasses.is_dataclass(FailureImpactScore)
