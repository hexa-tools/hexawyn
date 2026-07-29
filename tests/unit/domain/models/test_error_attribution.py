from __future__ import annotations

from hexawyn.domain.models.error_attribution import (
    ErrorAttributionRequest,
    ErrorAttributionResult,
    ServiceErrorCount,
)


class TestServiceErrorCount:
    def test_create(self) -> None:
        sec = ServiceErrorCount(service_name="auth-service", error_count=1012, percentage=81.6)
        assert sec.service_name == "auth-service"
        assert sec.error_count == 1012  # noqa: PLR2004


class TestErrorAttributionResult:
    def test_pareto_culprit(self) -> None:
        errors = [
            ("auth-service", 1012),
            ("payment-service", 180),
            ("checkout-service", 48),
        ]
        raw = [{"service": s, "count": c} for s, c in errors]
        result = ErrorAttributionResult.compute(
            request=ErrorAttributionRequest(gateway="api-gateway"),
            raw_errors=raw,
        )
        assert result.total_errors == 1240  # noqa: PLR2004
        assert len(result.attribution) == 3  # noqa: PLR2004
        assert result.attribution[0].service_name == "auth-service"
        assert result.pareto_culprit == "auth-service"

    def test_no_errors(self) -> None:
        result = ErrorAttributionResult.compute(
            request=ErrorAttributionRequest(gateway="api-gateway"),
            raw_errors=[],
        )
        assert result.total_errors == 0
        assert result.attribution == []

    def test_no_pareto(self) -> None:
        raw = [
            {"service": "auth-service", "count": 40},
            {"service": "payment-service", "count": 35},
            {"service": "checkout-service", "count": 30},
        ]
        result = ErrorAttributionResult.compute(
            request=ErrorAttributionRequest(gateway="api-gateway"),
            raw_errors=raw,
        )
        assert result.pareto_culprit is None
