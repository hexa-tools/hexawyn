import pytest
from hexawyn.domain.services.error_budget.slo_error_budget_engine import (
    SLOErrorBudgetBurnRateEngine,
    _as_bool,
    _as_float,
    _as_int,
)


def _raw_data(
    service_name: str = "payment-service",
    total_requests: int = 100000,
    successful_requests: int = 99500,
    has_data: bool = True,
    observation_days: int = 30,
) -> dict[str, object]:
    return {
        "service_name": service_name,
        "total_requests": total_requests,
        "successful_requests": successful_requests,
        "failed_requests": total_requests - successful_requests,
        "success_rate": successful_requests / total_requests if total_requests > 0 else 0.0,
        "error_rate": 1.0 - (successful_requests / total_requests) if total_requests > 0 else 0.0,
        "has_data": has_data,
        "observation_days": observation_days,
    }


class TestErrorBudgetCalculation:
    def test_slo_999_budget_is_0_1_percent_of_window(self) -> None:
        engine = SLOErrorBudgetBurnRateEngine()

        result = engine.compute(
            slo_target=0.999,
            rolling_window_days=30,
            raw_success_rate=_raw_data(),
        )

        assert result.total_budget_minutes == 43.2  # noqa: PLR2004
        assert result.slo_target == 0.999  # noqa: PLR2004

    def test_slo_995_budget_is_0_5_percent_of_window(self) -> None:
        engine = SLOErrorBudgetBurnRateEngine()

        result = engine.compute(
            slo_target=0.995,
            rolling_window_days=30,
            raw_success_rate=_raw_data(),
        )

        assert result.total_budget_minutes == 216.0  # noqa: PLR2004


class TestBurnRateComputation:
    def test_burn_rate_5x_when_burning_fast(self) -> None:
        engine = SLOErrorBudgetBurnRateEngine()
        raw = _raw_data(successful_requests=99500, total_requests=100000)

        result = engine.compute(
            slo_target=0.999,
            rolling_window_days=30,
            raw_success_rate=raw,
        )

        assert result.burn_rate == 5.0  # noqa: PLR2004

    def test_burn_rate_1x_when_exactly_at_slo(self) -> None:
        engine = SLOErrorBudgetBurnRateEngine()
        raw = _raw_data(successful_requests=99900, total_requests=100000)

        result = engine.compute(
            slo_target=0.999,
            rolling_window_days=30,
            raw_success_rate=raw,
        )

        assert result.burn_rate == 1.0

    def test_burn_rate_below_1_when_better_than_slo(self) -> None:
        engine = SLOErrorBudgetBurnRateEngine()
        raw = _raw_data(successful_requests=99950, total_requests=100000)

        result = engine.compute(
            slo_target=0.999,
            rolling_window_days=30,
            raw_success_rate=raw,
        )

        assert result.burn_rate == 0.5  # noqa: PLR2004

    def test_burn_rate_zero_when_no_errors(self) -> None:
        engine = SLOErrorBudgetBurnRateEngine()
        raw = _raw_data(successful_requests=100000, total_requests=100000)

        result = engine.compute(
            slo_target=0.999,
            rolling_window_days=30,
            raw_success_rate=raw,
        )

        assert result.burn_rate == 0.0


class TestBudgetConsumedAndRemaining:
    def test_budget_already_exhausted_negative_remaining(self) -> None:
        engine = SLOErrorBudgetBurnRateEngine()
        raw = _raw_data(successful_requests=99500, total_requests=100000)

        result = engine.compute(
            slo_target=0.999,
            rolling_window_days=30,
            raw_success_rate=raw,
        )

        assert result.budget_consumed_minutes == 216.0  # noqa: PLR2004
        assert result.budget_remaining_pct == -400.0  # noqa: PLR2004

    def test_budget_fully_intact(self) -> None:
        engine = SLOErrorBudgetBurnRateEngine()
        raw = _raw_data(successful_requests=100000, total_requests=100000)

        result = engine.compute(
            slo_target=0.999,
            rolling_window_days=30,
            raw_success_rate=raw,
        )

        assert result.budget_consumed_minutes == 0.0
        assert result.budget_remaining_pct == 100.0  # noqa: PLR2004


class TestTimeToExhaustion:
    def test_exhaustion_already_happened(self) -> None:
        engine = SLOErrorBudgetBurnRateEngine()
        raw = _raw_data(successful_requests=99500, total_requests=100000)

        result = engine.compute(
            slo_target=0.999,
            rolling_window_days=30,
            raw_success_rate=raw,
        )

        assert result.time_to_exhaustion_days is None
        assert result.verdict == "budget_exhausted"

    def test_at_risk_with_partial_window_observation(self) -> None:
        engine = SLOErrorBudgetBurnRateEngine()
        raw = _raw_data(
            successful_requests=99890,
            total_requests=100000,
            observation_days=7,
        )

        result = engine.compute(
            slo_target=0.999,
            rolling_window_days=30,
            raw_success_rate=raw,
        )

        assert result.burn_rate == pytest.approx(1.1)
        assert result.budget_remaining_pct > 0
        assert result.time_to_exhaustion_days is not None
        assert result.verdict == "budget_at_risk"

    def test_no_exhaustion_when_better_than_slo(self) -> None:
        engine = SLOErrorBudgetBurnRateEngine()
        raw = _raw_data(successful_requests=99950, total_requests=100000)

        result = engine.compute(
            slo_target=0.999,
            rolling_window_days=30,
            raw_success_rate=raw,
        )

        assert result.verdict == "budget_accumulating"


class TestVerdictClassification:
    def test_budget_exhausted_verdict(self) -> None:
        engine = SLOErrorBudgetBurnRateEngine()
        raw = _raw_data(successful_requests=99500, total_requests=100000)

        result = engine.compute(
            slo_target=0.999,
            rolling_window_days=30,
            raw_success_rate=raw,
        )

        assert result.verdict == "budget_exhausted"
        assert "Immediate action required" in result.recommendation

    def test_budget_barely_below_slo_at_risk(self) -> None:
        engine = SLOErrorBudgetBurnRateEngine()
        raw = _raw_data(
            successful_requests=99890,
            total_requests=100000,
            observation_days=7,
        )

        result = engine.compute(
            slo_target=0.999,
            rolling_window_days=30,
            raw_success_rate=raw,
        )

        assert result.verdict == "budget_at_risk"

    def test_budget_accumulating_verdict(self) -> None:
        engine = SLOErrorBudgetBurnRateEngine()
        raw = _raw_data(successful_requests=99950, total_requests=100000)

        result = engine.compute(
            slo_target=0.999,
            rolling_window_days=30,
            raw_success_rate=raw,
        )

        assert result.verdict == "budget_accumulating"

    def test_no_data_verdict(self) -> None:
        engine = SLOErrorBudgetBurnRateEngine()
        raw = _raw_data(total_requests=0, successful_requests=0)

        result = engine.compute(
            slo_target=0.999,
            rolling_window_days=30,
            raw_success_rate=raw,
        )

        assert result.verdict == "no_data"


class TestDefaultSLO:
    def test_default_slo_995_when_not_configured(self) -> None:
        engine = SLOErrorBudgetBurnRateEngine()
        raw = _raw_data(successful_requests=100000, total_requests=100000)

        result = engine.compute(
            slo_target=0.0,
            rolling_window_days=30,
            raw_success_rate=raw,
        )

        assert result.slo_target == 0.995  # noqa: PLR2004
        assert result.verdict == "budget_safe"


class TestEdgeCases:
    def test_zero_requests_in_window_budget_not_consumed(self) -> None:
        engine = SLOErrorBudgetBurnRateEngine()
        raw = _raw_data(total_requests=0, successful_requests=0)

        result = engine.compute(
            slo_target=0.999,
            rolling_window_days=30,
            raw_success_rate=raw,
        )

        assert result.verdict == "no_data"
        assert result.budget_consumed_minutes == 0.0
        assert result.burn_rate == 0.0
        assert "No traffic data available" in result.recommendation

    def test_very_short_window_computed(self) -> None:
        engine = SLOErrorBudgetBurnRateEngine()
        raw = _raw_data(successful_requests=9950, total_requests=10000)

        result = engine.compute(
            slo_target=0.999,
            rolling_window_days=1,
            raw_success_rate=raw,
        )

        assert result.rolling_window_days == 1
        assert result.total_budget_minutes == 1.44  # noqa: PLR2004

    def test_perfect_success_rate_budget_safe(self) -> None:
        engine = SLOErrorBudgetBurnRateEngine()
        raw = _raw_data(successful_requests=100000, total_requests=100000)

        result = engine.compute(
            slo_target=0.999,
            rolling_window_days=30,
            raw_success_rate=raw,
        )

        assert result.verdict == "budget_safe"
        assert result.burn_rate == 0.0
        assert result.budget_remaining_pct == 100.0  # noqa: PLR2004


class TestHelperFunctions:
    def test_as_float_none_returns_zero(self) -> None:
        assert _as_float(None) == 0.0

    def test_as_float_list_returns_zero(self) -> None:
        assert _as_float([1, 2, 3]) == 0.0

    def test_as_float_string_returns_zero(self) -> None:
        assert _as_float("not-a-number") == 0.0

    def test_as_int_none_returns_zero(self) -> None:
        assert _as_int(None) == 0

    def test_as_int_list_returns_zero(self) -> None:
        assert _as_int([1, 2]) == 0

    def test_as_int_float_truncated(self) -> None:
        assert _as_int(3.9) == 3  # noqa: PLR2004

    def test_as_bool_none_returns_false(self) -> None:
        assert _as_bool(None) is False

    def test_as_bool_true_returns_true(self) -> None:
        assert _as_bool(True) is True

    def test_as_bool_non_empty_string_returns_true(self) -> None:
        assert _as_bool("yes") is True
