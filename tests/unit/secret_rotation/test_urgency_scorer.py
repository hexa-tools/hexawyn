"""Unit tests for compute_urgency_score / sort_by_urgency. Checker case 5:
urgency_score must be a deterministic function of (risk_level, age_days),
never an inconsistent standalone number."""

from __future__ import annotations

from hexawyn.domain.models.secret_rotation import StaleSecretFinding


def _finding(name: str, urgency_score: int) -> StaleSecretFinding:
    return StaleSecretFinding(
        name=name,
        namespace="production",
        secret_type="Opaque",
        age_days=100,
        last_modified="2026-01-01",
        referenced_by=[],
        risk_level="critical",
        urgency_score=urgency_score,
        note=None,
    )


class TestComputeUrgencyScore:
    def test_ticket_test_data_exact_reproduction(self) -> None:
        """Test Data: age_days=180, risk=critical -> urgency_score=95."""
        from hexawyn.domain.services.secret_rotation.urgency_scorer import compute_urgency_score

        score = compute_urgency_score(risk_level="critical", age_days=180)

        assert score == 95

    def test_medium_risk_lower_base_than_critical(self) -> None:
        from hexawyn.domain.services.secret_rotation.urgency_scorer import compute_urgency_score

        critical_score = compute_urgency_score(risk_level="critical", age_days=0)
        medium_score = compute_urgency_score(risk_level="medium", age_days=0)

        assert critical_score > medium_score

    def test_low_risk_lower_base_than_medium(self) -> None:
        from hexawyn.domain.services.secret_rotation.urgency_scorer import compute_urgency_score

        medium_score = compute_urgency_score(risk_level="medium", age_days=0)
        low_score = compute_urgency_score(risk_level="low", age_days=0)

        assert medium_score > low_score

    def test_score_increases_with_age(self) -> None:
        from hexawyn.domain.services.secret_rotation.urgency_scorer import compute_urgency_score

        older_score = compute_urgency_score(risk_level="critical", age_days=200)
        younger_score = compute_urgency_score(risk_level="critical", age_days=100)

        assert older_score > younger_score

    def test_score_never_exceeds_100(self) -> None:
        from hexawyn.domain.services.secret_rotation.urgency_scorer import compute_urgency_score

        score = compute_urgency_score(risk_level="critical", age_days=100_000)

        assert score == 100


class TestSortByUrgency:
    def test_tc5_sorts_highest_urgency_first(self) -> None:
        from hexawyn.domain.services.secret_rotation.urgency_scorer import sort_by_urgency

        low = _finding("low-urgency", 20)
        high = _finding("high-urgency", 95)
        medium = _finding("medium-urgency", 50)

        result = sort_by_urgency([low, medium, high])

        assert result == [high, medium, low]

    def test_ties_broken_alphabetically_by_name(self) -> None:
        from hexawyn.domain.services.secret_rotation.urgency_scorer import sort_by_urgency

        b = _finding("b-secret", 50)
        a = _finding("a-secret", 50)

        result = sort_by_urgency([b, a])

        assert result == [a, b]
