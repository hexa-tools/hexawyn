from hexawyn.domain.models.semantic import CheckerVerdict, SemanticCheckResult


class TestCheckerVerdict:
    def test_class_attributes_are_strings(self):
        assert CheckerVerdict.PASS == "PASS"
        assert CheckerVerdict.FAIL == "FAIL"
        assert CheckerVerdict.BLOCKED == "BLOCKED"
        assert CheckerVerdict.DEGRADED == "DEGRADED"

    def test_isinstance_of_str(self):
        assert isinstance(CheckerVerdict.PASS, str)
        assert isinstance(CheckerVerdict.FAIL, str)


class TestSemanticCheckResult:
    def test_defaults(self):
        result = SemanticCheckResult(
            verdict=CheckerVerdict.PASS, score=0.95, reason="All checks passed"
        )
        assert result.verdict == "PASS"
        assert result.score == 0.95  # noqa: PLR2004
        assert result.retry_count == 0
        assert result.max_retries == 3  # noqa: PLR2004

    def test_fail_verdict(self):
        result = SemanticCheckResult(
            verdict=CheckerVerdict.FAIL,
            score=0.3,
            reason="Inconsistency found",
            retry_count=2,
        )
        assert result.verdict == "FAIL"
        assert result.retry_count == 2  # noqa: PLR2004

    def test_blocked_verdict(self):
        result = SemanticCheckResult(
            verdict=CheckerVerdict.BLOCKED,
            score=0.0,
            reason="Mutation blocked",
            max_retries=0,
        )
        assert result.verdict == "BLOCKED"
        assert result.max_retries == 0

    def test_is_dataclass(self):
        r1 = SemanticCheckResult(verdict="PASS", score=1.0, reason="ok")
        r2 = SemanticCheckResult(verdict="PASS", score=1.0, reason="ok")
        assert r1 == r2
