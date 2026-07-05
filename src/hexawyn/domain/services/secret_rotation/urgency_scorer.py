from __future__ import annotations

from hexawyn.domain.models.secret_rotation import RiskLevel, StaleSecretFinding

_RISK_BASE_SCORE: dict[RiskLevel, int] = {"critical": 50, "medium": 30, "low": 10}
_AGE_DIVISOR = 4
_MAX_SCORE = 100
_MIN_SCORE = 0


def compute_urgency_score(risk_level: RiskLevel, age_days: int) -> int:
    score = _RISK_BASE_SCORE[risk_level] + age_days // _AGE_DIVISOR
    return min(_MAX_SCORE, max(_MIN_SCORE, score))


def sort_by_urgency(findings: list[StaleSecretFinding]) -> list[StaleSecretFinding]:
    return sorted(findings, key=lambda finding: (-finding.urgency_score, finding.name))
