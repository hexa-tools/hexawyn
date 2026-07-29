"""RED → GREEN — Layer 1: SLO Error Budget domain models."""

from hexawyn.domain.models.error_budget import SLOErrorBudgetRequest, SLOErrorBudgetResult


class TestSLOErrorBudgetRequest:
    def test_holds_service_and_slo(self) -> None:
        req = SLOErrorBudgetRequest(
            service_name="payment-service",
            slo_target=0.999,
            rolling_window_days=30,
        )
        assert req.service_name == "payment-service"
        assert req.slo_target == 0.999  # noqa: PLR2004
        assert req.rolling_window_days == 30  # noqa: PLR2004

    def test_is_frozen(self) -> None:
        import pytest

        req = SLOErrorBudgetRequest(service_name="svc", slo_target=0.99, rolling_window_days=30)
        with pytest.raises(Exception):
            req.slo_target = 0.999  # type: ignore[misc]


class TestSLOErrorBudgetResult:
    def test_default_values(self) -> None:
        result = SLOErrorBudgetResult()
        assert result.service_name == ""
        assert result.slo_target == 0.999  # noqa: PLR2004
        assert result.total_budget_minutes == 0.0
        assert result.verdict == "budget_safe"

    def test_full_result_construction(self) -> None:
        result = SLOErrorBudgetResult(
            service_name="payment-service",
            slo_target=0.999,
            rolling_window_days=30,
            total_budget_minutes=43.2,
            current_success_rate=0.995,
            error_rate=0.005,
            budget_consumed_minutes=216.0,
            budget_remaining_pct=-400.0,
            burn_rate=5.0,
            time_to_exhaustion_days=None,
            verdict="budget_exhausted",
            recommendation="Immediate action required",
            total_requests=100000,
            successful_requests=99500,
            failed_requests=500,
        )
        assert result.service_name == "payment-service"
        assert result.burn_rate == 5.0  # noqa: PLR2004
        assert result.verdict == "budget_exhausted"
        assert result.total_requests == 100000  # noqa: PLR2004
