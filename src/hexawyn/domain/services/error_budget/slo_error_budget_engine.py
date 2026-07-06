from __future__ import annotations

from hexawyn.domain.models.error_budget import SLOErrorBudgetResult

_DEFAULT_SLO_TARGET = 0.995
_SLO_TARGET_EPSILON = 0.0001


class SLOErrorBudgetBurnRateEngine:
    """Pure domain service — no infra deps, no try/catch."""

    def compute(
        self,
        slo_target: float,
        rolling_window_days: int,
        raw_success_rate: dict[str, object],
    ) -> SLOErrorBudgetResult:
        effective_slo = slo_target if slo_target > 0.0 else _DEFAULT_SLO_TARGET
        window_minutes = rolling_window_days * 24.0 * 60.0
        error_budget_rate = 1.0 - effective_slo

        total_budget_minutes = round(error_budget_rate * window_minutes, 2)

        success_rate = _as_float(raw_success_rate.get("success_rate"))
        error_rate = _as_float(raw_success_rate.get("error_rate"))
        total_requests = _as_int(raw_success_rate.get("total_requests"))
        successful_requests = _as_int(raw_success_rate.get("successful_requests"))
        failed_requests = _as_int(raw_success_rate.get("failed_requests"))
        has_data = _as_bool(raw_success_rate.get("has_data"))
        observation_days = _as_float(raw_success_rate.get("observation_days"))

        if not has_data or total_requests == 0:
            return SLOErrorBudgetResult(
                service_name=str(raw_success_rate.get("service_name", "")),
                slo_target=effective_slo,
                rolling_window_days=rolling_window_days,
                total_budget_minutes=total_budget_minutes,
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

        divisor = max(error_budget_rate, _SLO_TARGET_EPSILON)
        burn_rate = round(error_rate / divisor, 2)

        observation_minutes = observation_days * 24.0 * 60.0
        consumed_minutes = round(error_rate * observation_minutes, 2)
        remaining_minutes = total_budget_minutes - consumed_minutes
        remaining_pct = round((remaining_minutes / total_budget_minutes) * 100.0, 2)

        time_to_exhaustion_days = _compute_exhaustion_time(
            remaining_minutes, error_rate, error_budget_rate
        )

        verdict, recommendation = _classify_verdict(burn_rate, remaining_pct)

        return SLOErrorBudgetResult(
            service_name=str(raw_success_rate.get("service_name", "")),
            slo_target=effective_slo,
            rolling_window_days=rolling_window_days,
            total_budget_minutes=total_budget_minutes,
            current_success_rate=success_rate,
            error_rate=error_rate,
            budget_consumed_minutes=consumed_minutes,
            budget_remaining_pct=remaining_pct,
            burn_rate=burn_rate,
            time_to_exhaustion_days=time_to_exhaustion_days,
            verdict=verdict,
            recommendation=recommendation,
            total_requests=total_requests,
            successful_requests=successful_requests,
            failed_requests=failed_requests,
        )


def _compute_exhaustion_time(
    remaining_minutes: float,
    error_rate: float,
    error_budget_rate: float,
) -> float | None:
    if remaining_minutes <= 0:
        return None
    excess_burn = error_rate - error_budget_rate
    if excess_burn <= 0:
        return None
    time_minutes = remaining_minutes / excess_burn
    return round(time_minutes / (24.0 * 60.0), 1)


def _classify_verdict(
    burn_rate: float,
    remaining_pct: float,
) -> tuple[str, str]:
    if remaining_pct <= 0:
        return (
            "budget_exhausted",
            f"Immediate action required: error rate {burn_rate}x above SLO allowance",
        )

    if burn_rate >= 1.0:
        return (
            "budget_at_risk",
            f"Budget burning at {burn_rate}x — review immediately",
        )

    if burn_rate == 0.0:
        return (
            "budget_safe",
            "No errors — budget fully intact",
        )

    return (
        "budget_accumulating",
        "Performance better than SLO — budget accumulating",
    )


def _as_float(value: object) -> float:
    if value is None:
        return 0.0
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def _as_int(value: object) -> int:
    if value is None:
        return 0
    try:
        return int(float(value))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def _as_bool(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    return bool(value)
