import pytest
from hexawyn.domain.models.error_budget import SLOErrorBudgetResult
from hexawyn.domain.services.error_budget.slo_error_budget_engine import (
    SLOErrorBudgetBurnRateEngine,
    _as_bool,
    _as_float,
    _as_int,
    _classify_verdict,
    _compute_exhaustion_time,
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


class TestFullResultPropagation:
    def test_full_result_fields_round_trip_exact_values(self) -> None:
        engine = SLOErrorBudgetBurnRateEngine()
        raw: dict[str, object] = {
            "service_name": "svc-payments",
            "success_rate": 0.998867,
            "error_rate": 0.001133,
            "total_requests": 100000,
            "successful_requests": 99887,
            "failed_requests": 113,
            "has_data": True,
            "observation_days": 7,
        }

        result = engine.compute(
            slo_target=0.999,
            rolling_window_days=30,
            raw_success_rate=raw,
        )

        assert result == SLOErrorBudgetResult(
            service_name="svc-payments",
            slo_target=0.999,
            rolling_window_days=30,
            total_budget_minutes=43.2,
            current_success_rate=0.998867,
            error_rate=0.001133,
            budget_consumed_minutes=11.42,
            budget_remaining_pct=73.56,
            burn_rate=1.13,
            time_to_exhaustion_days=165.9,
            verdict="budget_at_risk",
            recommendation="Budget burning at 1.13x — review immediately",
            total_requests=100000,
            successful_requests=99887,
            failed_requests=113,
        )

    def test_result_propagates_service_name_when_present(self) -> None:
        engine = SLOErrorBudgetBurnRateEngine()
        raw = _raw_data(service_name="checkout-api")

        result = engine.compute(
            slo_target=0.999,
            rolling_window_days=30,
            raw_success_rate=raw,
        )

        assert result.service_name == "checkout-api"

    def test_missing_service_name_defaults_to_empty_string(self) -> None:
        engine = SLOErrorBudgetBurnRateEngine()
        raw = _raw_data(service_name="")
        raw.pop("service_name")

        result = engine.compute(
            slo_target=0.999,
            rolling_window_days=30,
            raw_success_rate=raw,
        )

        assert result.service_name == ""

    def test_no_data_result_full_equality(self) -> None:
        engine = SLOErrorBudgetBurnRateEngine()
        raw: dict[str, object] = {
            "service_name": "svc-empty",
            "success_rate": 0.0,
            "error_rate": 0.0,
            "total_requests": 0,
            "successful_requests": 0,
            "failed_requests": 0,
            "has_data": False,
            "observation_days": 7,
        }

        result = engine.compute(
            slo_target=0.999,
            rolling_window_days=30,
            raw_success_rate=raw,
        )

        assert result == SLOErrorBudgetResult(
            service_name="svc-empty",
            slo_target=0.999,
            rolling_window_days=30,
            total_budget_minutes=43.2,
            current_success_rate=0.0,
            error_rate=0.0,
            budget_consumed_minutes=0.0,
            budget_remaining_pct=100.0,
            burn_rate=0.0,
            time_to_exhaustion_days=None,
            verdict="no_data",
            recommendation="No traffic data available for this service",
            total_requests=0,
            successful_requests=0,
            failed_requests=0,
        )

    def test_no_data_missing_service_name_uses_empty_string(self) -> None:
        engine = SLOErrorBudgetBurnRateEngine()
        raw: dict[str, object] = {
            "error_rate": 0.0,
            "total_requests": 0,
            "has_data": False,
            "observation_days": 7,
        }

        result = engine.compute(
            slo_target=0.999,
            rolling_window_days=30,
            raw_success_rate=raw,
        )

        assert result.service_name == ""
        assert result.verdict == "no_data"

    def test_total_budget_rounds_to_two_decimals(self) -> None:
        engine = SLOErrorBudgetBurnRateEngine()
        raw = _raw_data()

        result = engine.compute(
            slo_target=0.999883,
            rolling_window_days=1,
            raw_success_rate=raw,
        )

        assert result.total_budget_minutes == 0.17  # noqa: PLR2004

    def test_no_data_respects_non_default_slo_and_window(self) -> None:
        engine = SLOErrorBudgetBurnRateEngine()
        raw: dict[str, object] = {
            "service_name": "svc-empty",
            "has_data": False,
            "observation_days": 7,
        }

        result = engine.compute(
            slo_target=0.995,
            rolling_window_days=7,
            raw_success_rate=raw,
        )

        assert result.slo_target == 0.995  # noqa: PLR2004
        assert result.rolling_window_days == 7  # noqa: PLR2004
        assert result.total_budget_minutes == 50.4  # noqa: PLR2004
        assert result.verdict == "no_data"


class TestExhaustionHelperDiscriminators:
    def test_remaining_zero_returns_none(self) -> None:
        assert _compute_exhaustion_time(0.0, 0.002, 0.001) is None

    def test_error_rate_below_budget_returns_none(self) -> None:
        assert _compute_exhaustion_time(100.0, 0.0005, 0.001) is None

    def test_excess_exactly_zero_returns_none(self) -> None:
        assert _compute_exhaustion_time(100.0, 0.001, 0.001) is None

    def test_single_day_remaining_one_minute_excess(self) -> None:
        result = _compute_exhaustion_time(1.0, 0.002, 0.001)
        assert result == 0.7  # noqa: PLR2004

    def test_fractional_day_rounds_to_one_decimal(self) -> None:
        result = _compute_exhaustion_time(1.8144, 0.002, 0.001)
        assert result == 1.3  # noqa: PLR2004

    def test_large_remaining_scales_linearly(self) -> None:
        result = _compute_exhaustion_time(181.44, 0.002, 0.001)
        assert result == 126.0  # noqa: PLR2004

    def test_excess_slightly_above_budget_computes_days(self) -> None:
        result = _compute_exhaustion_time(43.2, 0.002, 0.001)
        assert result == 30.0  # noqa: PLR2004


class TestClassifyVerdictDiscriminators:
    def test_zero_percent_remaining_exhausted(self) -> None:
        verdict, recommendation = _classify_verdict(2.0, 0.0)
        assert verdict == "budget_exhausted"
        assert recommendation == ("Immediate action required: error rate 2.0x above SLO allowance")

    def test_one_percent_remaining_accumulating_low_burn(self) -> None:
        verdict, _ = _classify_verdict(0.5, 1.0)
        assert verdict == "budget_accumulating"

    def test_burn_rate_exactly_one_at_risk(self) -> None:
        verdict, _ = _classify_verdict(1.0, 50.0)
        assert verdict == "budget_at_risk"

    def test_zero_burn_safe_exact_message(self) -> None:
        verdict, recommendation = _classify_verdict(0.0, 50.0)
        assert verdict == "budget_safe"
        assert recommendation == "No errors — budget fully intact"

    def test_low_burn_accumulating_exact_message(self) -> None:
        verdict, recommendation = _classify_verdict(0.5, 50.0)
        assert verdict == "budget_accumulating"
        assert recommendation == "Performance better than SLO — budget accumulating"

    def test_burn_above_one_exhausted_recommendation_format(self) -> None:
        verdict, recommendation = _classify_verdict(3.5, -10.0)
        assert verdict == "budget_exhausted"
        assert recommendation == ("Immediate action required: error rate 3.5x above SLO allowance")
