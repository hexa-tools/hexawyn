from dataclasses import dataclass, field


@dataclass(frozen=True)
class RcaScoringConfig:
    """Configurable weights and thresholds for RCA scoring.

    All weights are additive — the final score is clamped between
    min and max bounds. Modify this config to tune scoring behavior.
    """

    base_confidence: float = 0.5
    logs_analyzed_weight: float = 0.2
    root_cause_found_weight: float = 0.2
    timeline_available_weight: float = 0.1
    max_confidence: float = 1.0

    base_impact: float = 5.0
    affected_task_weight: float = 0.5
    related_incident_weight: float = 1.0
    timeline_event_weight: float = 0.2
    max_impact: float = 10.0
    min_impact: float = 1.0


@dataclass
class RcaConfidenceScore:
    """Confidence score for a root cause analysis."""

    value: float = 0.0
    label: str = "unknown"
    factors: dict[str, float] = field(default_factory=dict)


@dataclass
class FailureImpactScore:
    """Impact score of a failure on the system."""

    value: float = 0.0
    label: str = "unknown"
    affected_components: int = 0
    cascade_risk: str = "none"
