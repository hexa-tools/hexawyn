from __future__ import annotations

from hexawyn.domain.models.error_budget import SLOErrorBudgetResult

_DEFAULT_SLO_TARGET = 0.995
_SLO_TARGET_EPSILON = 0.0001


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut: MutantDict = {}  # type: ignore


class SLOErrorBudgetBurnRateEngine:
    """Pure domain service — no infra deps, no try/catch."""

    @_mutmut_mutated(mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut)
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_orig(
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_1(
        self,
        slo_target: float,
        rolling_window_days: int,
        raw_success_rate: dict[str, object],
    ) -> SLOErrorBudgetResult:
        effective_slo = None
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_2(
        self,
        slo_target: float,
        rolling_window_days: int,
        raw_success_rate: dict[str, object],
    ) -> SLOErrorBudgetResult:
        effective_slo = slo_target if slo_target >= 0.0 else _DEFAULT_SLO_TARGET
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_3(
        self,
        slo_target: float,
        rolling_window_days: int,
        raw_success_rate: dict[str, object],
    ) -> SLOErrorBudgetResult:
        effective_slo = slo_target if slo_target > 1.0 else _DEFAULT_SLO_TARGET
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_4(
        self,
        slo_target: float,
        rolling_window_days: int,
        raw_success_rate: dict[str, object],
    ) -> SLOErrorBudgetResult:
        effective_slo = slo_target if slo_target > 0.0 else _DEFAULT_SLO_TARGET
        window_minutes = None
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_5(
        self,
        slo_target: float,
        rolling_window_days: int,
        raw_success_rate: dict[str, object],
    ) -> SLOErrorBudgetResult:
        effective_slo = slo_target if slo_target > 0.0 else _DEFAULT_SLO_TARGET
        window_minutes = rolling_window_days * 24.0 / 60.0
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_6(
        self,
        slo_target: float,
        rolling_window_days: int,
        raw_success_rate: dict[str, object],
    ) -> SLOErrorBudgetResult:
        effective_slo = slo_target if slo_target > 0.0 else _DEFAULT_SLO_TARGET
        window_minutes = rolling_window_days / 24.0 * 60.0
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_7(
        self,
        slo_target: float,
        rolling_window_days: int,
        raw_success_rate: dict[str, object],
    ) -> SLOErrorBudgetResult:
        effective_slo = slo_target if slo_target > 0.0 else _DEFAULT_SLO_TARGET
        window_minutes = rolling_window_days * 25.0 * 60.0
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_8(
        self,
        slo_target: float,
        rolling_window_days: int,
        raw_success_rate: dict[str, object],
    ) -> SLOErrorBudgetResult:
        effective_slo = slo_target if slo_target > 0.0 else _DEFAULT_SLO_TARGET
        window_minutes = rolling_window_days * 24.0 * 61.0
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_9(
        self,
        slo_target: float,
        rolling_window_days: int,
        raw_success_rate: dict[str, object],
    ) -> SLOErrorBudgetResult:
        effective_slo = slo_target if slo_target > 0.0 else _DEFAULT_SLO_TARGET
        window_minutes = rolling_window_days * 24.0 * 60.0
        error_budget_rate = None

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_10(
        self,
        slo_target: float,
        rolling_window_days: int,
        raw_success_rate: dict[str, object],
    ) -> SLOErrorBudgetResult:
        effective_slo = slo_target if slo_target > 0.0 else _DEFAULT_SLO_TARGET
        window_minutes = rolling_window_days * 24.0 * 60.0
        error_budget_rate = 1.0 + effective_slo

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_11(
        self,
        slo_target: float,
        rolling_window_days: int,
        raw_success_rate: dict[str, object],
    ) -> SLOErrorBudgetResult:
        effective_slo = slo_target if slo_target > 0.0 else _DEFAULT_SLO_TARGET
        window_minutes = rolling_window_days * 24.0 * 60.0
        error_budget_rate = 2.0 - effective_slo

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_12(
        self,
        slo_target: float,
        rolling_window_days: int,
        raw_success_rate: dict[str, object],
    ) -> SLOErrorBudgetResult:
        effective_slo = slo_target if slo_target > 0.0 else _DEFAULT_SLO_TARGET
        window_minutes = rolling_window_days * 24.0 * 60.0
        error_budget_rate = 1.0 - effective_slo

        total_budget_minutes = None

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_13(
        self,
        slo_target: float,
        rolling_window_days: int,
        raw_success_rate: dict[str, object],
    ) -> SLOErrorBudgetResult:
        effective_slo = slo_target if slo_target > 0.0 else _DEFAULT_SLO_TARGET
        window_minutes = rolling_window_days * 24.0 * 60.0
        error_budget_rate = 1.0 - effective_slo

        total_budget_minutes = round(None, 2)

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_14(
        self,
        slo_target: float,
        rolling_window_days: int,
        raw_success_rate: dict[str, object],
    ) -> SLOErrorBudgetResult:
        effective_slo = slo_target if slo_target > 0.0 else _DEFAULT_SLO_TARGET
        window_minutes = rolling_window_days * 24.0 * 60.0
        error_budget_rate = 1.0 - effective_slo

        total_budget_minutes = round(error_budget_rate * window_minutes, None)

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_15(
        self,
        slo_target: float,
        rolling_window_days: int,
        raw_success_rate: dict[str, object],
    ) -> SLOErrorBudgetResult:
        effective_slo = slo_target if slo_target > 0.0 else _DEFAULT_SLO_TARGET
        window_minutes = rolling_window_days * 24.0 * 60.0
        error_budget_rate = 1.0 - effective_slo

        total_budget_minutes = round(2)

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_16(
        self,
        slo_target: float,
        rolling_window_days: int,
        raw_success_rate: dict[str, object],
    ) -> SLOErrorBudgetResult:
        effective_slo = slo_target if slo_target > 0.0 else _DEFAULT_SLO_TARGET
        window_minutes = rolling_window_days * 24.0 * 60.0
        error_budget_rate = 1.0 - effective_slo

        total_budget_minutes = round(error_budget_rate * window_minutes, )

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_17(
        self,
        slo_target: float,
        rolling_window_days: int,
        raw_success_rate: dict[str, object],
    ) -> SLOErrorBudgetResult:
        effective_slo = slo_target if slo_target > 0.0 else _DEFAULT_SLO_TARGET
        window_minutes = rolling_window_days * 24.0 * 60.0
        error_budget_rate = 1.0 - effective_slo

        total_budget_minutes = round(error_budget_rate / window_minutes, 2)

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_18(
        self,
        slo_target: float,
        rolling_window_days: int,
        raw_success_rate: dict[str, object],
    ) -> SLOErrorBudgetResult:
        effective_slo = slo_target if slo_target > 0.0 else _DEFAULT_SLO_TARGET
        window_minutes = rolling_window_days * 24.0 * 60.0
        error_budget_rate = 1.0 - effective_slo

        total_budget_minutes = round(error_budget_rate * window_minutes, 3)

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_19(
        self,
        slo_target: float,
        rolling_window_days: int,
        raw_success_rate: dict[str, object],
    ) -> SLOErrorBudgetResult:
        effective_slo = slo_target if slo_target > 0.0 else _DEFAULT_SLO_TARGET
        window_minutes = rolling_window_days * 24.0 * 60.0
        error_budget_rate = 1.0 - effective_slo

        total_budget_minutes = round(error_budget_rate * window_minutes, 2)

        success_rate = None
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_20(
        self,
        slo_target: float,
        rolling_window_days: int,
        raw_success_rate: dict[str, object],
    ) -> SLOErrorBudgetResult:
        effective_slo = slo_target if slo_target > 0.0 else _DEFAULT_SLO_TARGET
        window_minutes = rolling_window_days * 24.0 * 60.0
        error_budget_rate = 1.0 - effective_slo

        total_budget_minutes = round(error_budget_rate * window_minutes, 2)

        success_rate = _as_float(None)
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_21(
        self,
        slo_target: float,
        rolling_window_days: int,
        raw_success_rate: dict[str, object],
    ) -> SLOErrorBudgetResult:
        effective_slo = slo_target if slo_target > 0.0 else _DEFAULT_SLO_TARGET
        window_minutes = rolling_window_days * 24.0 * 60.0
        error_budget_rate = 1.0 - effective_slo

        total_budget_minutes = round(error_budget_rate * window_minutes, 2)

        success_rate = _as_float(raw_success_rate.get(None))
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_22(
        self,
        slo_target: float,
        rolling_window_days: int,
        raw_success_rate: dict[str, object],
    ) -> SLOErrorBudgetResult:
        effective_slo = slo_target if slo_target > 0.0 else _DEFAULT_SLO_TARGET
        window_minutes = rolling_window_days * 24.0 * 60.0
        error_budget_rate = 1.0 - effective_slo

        total_budget_minutes = round(error_budget_rate * window_minutes, 2)

        success_rate = _as_float(raw_success_rate.get("XXsuccess_rateXX"))
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_23(
        self,
        slo_target: float,
        rolling_window_days: int,
        raw_success_rate: dict[str, object],
    ) -> SLOErrorBudgetResult:
        effective_slo = slo_target if slo_target > 0.0 else _DEFAULT_SLO_TARGET
        window_minutes = rolling_window_days * 24.0 * 60.0
        error_budget_rate = 1.0 - effective_slo

        total_budget_minutes = round(error_budget_rate * window_minutes, 2)

        success_rate = _as_float(raw_success_rate.get("SUCCESS_RATE"))
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_24(
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
        error_rate = None
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_25(
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
        error_rate = _as_float(None)
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_26(
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
        error_rate = _as_float(raw_success_rate.get(None))
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_27(
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
        error_rate = _as_float(raw_success_rate.get("XXerror_rateXX"))
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_28(
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
        error_rate = _as_float(raw_success_rate.get("ERROR_RATE"))
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_29(
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
        total_requests = None
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_30(
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
        total_requests = _as_int(None)
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_31(
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
        total_requests = _as_int(raw_success_rate.get(None))
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_32(
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
        total_requests = _as_int(raw_success_rate.get("XXtotal_requestsXX"))
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_33(
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
        total_requests = _as_int(raw_success_rate.get("TOTAL_REQUESTS"))
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_34(
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
        successful_requests = None
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_35(
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
        successful_requests = _as_int(None)
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_36(
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
        successful_requests = _as_int(raw_success_rate.get(None))
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_37(
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
        successful_requests = _as_int(raw_success_rate.get("XXsuccessful_requestsXX"))
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_38(
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
        successful_requests = _as_int(raw_success_rate.get("SUCCESSFUL_REQUESTS"))
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_39(
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
        failed_requests = None
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_40(
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
        failed_requests = _as_int(None)
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_41(
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
        failed_requests = _as_int(raw_success_rate.get(None))
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_42(
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
        failed_requests = _as_int(raw_success_rate.get("XXfailed_requestsXX"))
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_43(
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
        failed_requests = _as_int(raw_success_rate.get("FAILED_REQUESTS"))
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_44(
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
        has_data = None
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_45(
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
        has_data = _as_bool(None)
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_46(
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
        has_data = _as_bool(raw_success_rate.get(None))
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_47(
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
        has_data = _as_bool(raw_success_rate.get("XXhas_dataXX"))
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_48(
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
        has_data = _as_bool(raw_success_rate.get("HAS_DATA"))
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_49(
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
        observation_days = None

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_50(
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
        observation_days = _as_float(None)

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_51(
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
        observation_days = _as_float(raw_success_rate.get(None))

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_52(
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
        observation_days = _as_float(raw_success_rate.get("XXobservation_daysXX"))

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_53(
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
        observation_days = _as_float(raw_success_rate.get("OBSERVATION_DAYS"))

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_54(
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

        if not has_data and total_requests == 0:
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_55(
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

        if has_data or total_requests == 0:
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_56(
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

        if not has_data or total_requests != 0:
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_57(
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

        if not has_data or total_requests == 1:
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_58(
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
                service_name=None,
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_59(
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
                slo_target=None,
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_60(
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
                rolling_window_days=None,
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_61(
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
                total_budget_minutes=None,
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_62(
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
                current_success_rate=None,
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_63(
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
                error_rate=None,
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_64(
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
                budget_consumed_minutes=None,
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_65(
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
                budget_remaining_pct=None,
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_66(
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
                burn_rate=None,
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_67(
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
                verdict=None,
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_68(
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
                recommendation=None,
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_69(
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
                total_requests=None,
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_70(
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
                successful_requests=None,
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_71(
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
                failed_requests=None,
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_72(
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_73(
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_74(
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_75(
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_76(
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_77(
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_78(
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_79(
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_80(
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_81(
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_82(
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_83(
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_84(
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_85(
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_86(
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_87(
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
                service_name=str(None),
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_88(
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
                service_name=str(raw_success_rate.get(None, "")),
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_89(
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
                service_name=str(raw_success_rate.get("service_name", None)),
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_90(
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
                service_name=str(raw_success_rate.get("")),
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_91(
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
                service_name=str(raw_success_rate.get("service_name", )),
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_92(
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
                service_name=str(raw_success_rate.get("XXservice_nameXX", "")),
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_93(
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
                service_name=str(raw_success_rate.get("SERVICE_NAME", "")),
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_94(
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
                service_name=str(raw_success_rate.get("service_name", "XXXX")),
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_95(
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
                current_success_rate=1.0,
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_96(
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
                error_rate=1.0,
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_97(
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
                budget_consumed_minutes=1.0,
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_98(
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
                budget_remaining_pct=101.0,
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_99(
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
                burn_rate=1.0,
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_100(
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
                verdict="XXno_dataXX",
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_101(
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
                verdict="NO_DATA",
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_102(
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
                recommendation="XXNo traffic data available for this serviceXX",
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_103(
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
                recommendation="no traffic data available for this service",
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_104(
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
                recommendation="NO TRAFFIC DATA AVAILABLE FOR THIS SERVICE",
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_105(
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
                total_requests=1,
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_106(
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
                successful_requests=1,
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_107(
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
                failed_requests=1,
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_108(
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

        divisor = None
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_109(
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

        divisor = max(None, _SLO_TARGET_EPSILON)
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_110(
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

        divisor = max(error_budget_rate, None)
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_111(
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

        divisor = max(_SLO_TARGET_EPSILON)
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_112(
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

        divisor = max(error_budget_rate, )
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_113(
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
        burn_rate = None

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_114(
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
        burn_rate = round(None, 2)

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_115(
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
        burn_rate = round(error_rate / divisor, None)

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_116(
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
        burn_rate = round(2)

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_117(
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
        burn_rate = round(error_rate / divisor, )

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_118(
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
        burn_rate = round(error_rate * divisor, 2)

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_119(
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
        burn_rate = round(error_rate / divisor, 3)

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_120(
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

        observation_minutes = None
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_121(
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

        observation_minutes = observation_days * 24.0 / 60.0
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_122(
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

        observation_minutes = observation_days / 24.0 * 60.0
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_123(
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

        observation_minutes = observation_days * 25.0 * 60.0
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_124(
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

        observation_minutes = observation_days * 24.0 * 61.0
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_125(
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
        consumed_minutes = None
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_126(
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
        consumed_minutes = round(None, 2)
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_127(
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
        consumed_minutes = round(error_rate * observation_minutes, None)
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_128(
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
        consumed_minutes = round(2)
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_129(
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
        consumed_minutes = round(error_rate * observation_minutes, )
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_130(
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
        consumed_minutes = round(error_rate / observation_minutes, 2)
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_131(
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
        consumed_minutes = round(error_rate * observation_minutes, 3)
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_132(
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
        remaining_minutes = None
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_133(
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
        remaining_minutes = total_budget_minutes + consumed_minutes
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_134(
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
        remaining_pct = None

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_135(
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
        remaining_pct = round(None, 2)

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_136(
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
        remaining_pct = round((remaining_minutes / total_budget_minutes) * 100.0, None)

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_137(
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
        remaining_pct = round(2)

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_138(
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
        remaining_pct = round((remaining_minutes / total_budget_minutes) * 100.0, )

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_139(
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
        remaining_pct = round((remaining_minutes / total_budget_minutes) / 100.0, 2)

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_140(
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
        remaining_pct = round((remaining_minutes * total_budget_minutes) * 100.0, 2)

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_141(
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
        remaining_pct = round((remaining_minutes / total_budget_minutes) * 101.0, 2)

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_142(
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
        remaining_pct = round((remaining_minutes / total_budget_minutes) * 100.0, 3)

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_143(
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

        time_to_exhaustion_days = None

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_144(
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
            None, error_rate, error_budget_rate
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_145(
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
            remaining_minutes, None, error_budget_rate
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_146(
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
            remaining_minutes, error_rate, None
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_147(
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
            error_rate, error_budget_rate
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_148(
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
            remaining_minutes, error_budget_rate
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_149(
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
            remaining_minutes, error_rate, )

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_150(
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

        verdict, recommendation = None

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_151(
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

        verdict, recommendation = _classify_verdict(None, remaining_pct)

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_152(
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

        verdict, recommendation = _classify_verdict(burn_rate, None)

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_153(
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

        verdict, recommendation = _classify_verdict(remaining_pct)

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_154(
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

        verdict, recommendation = _classify_verdict(burn_rate, )

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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_155(
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
            service_name=None,
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_156(
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
            slo_target=None,
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_157(
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
            rolling_window_days=None,
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_158(
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
            total_budget_minutes=None,
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_159(
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
            current_success_rate=None,
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_160(
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
            error_rate=None,
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_161(
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
            budget_consumed_minutes=None,
            budget_remaining_pct=remaining_pct,
            burn_rate=burn_rate,
            time_to_exhaustion_days=time_to_exhaustion_days,
            verdict=verdict,
            recommendation=recommendation,
            total_requests=total_requests,
            successful_requests=successful_requests,
            failed_requests=failed_requests,
        )

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_162(
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
            budget_remaining_pct=None,
            burn_rate=burn_rate,
            time_to_exhaustion_days=time_to_exhaustion_days,
            verdict=verdict,
            recommendation=recommendation,
            total_requests=total_requests,
            successful_requests=successful_requests,
            failed_requests=failed_requests,
        )

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_163(
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
            burn_rate=None,
            time_to_exhaustion_days=time_to_exhaustion_days,
            verdict=verdict,
            recommendation=recommendation,
            total_requests=total_requests,
            successful_requests=successful_requests,
            failed_requests=failed_requests,
        )

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_164(
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
            time_to_exhaustion_days=None,
            verdict=verdict,
            recommendation=recommendation,
            total_requests=total_requests,
            successful_requests=successful_requests,
            failed_requests=failed_requests,
        )

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_165(
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
            verdict=None,
            recommendation=recommendation,
            total_requests=total_requests,
            successful_requests=successful_requests,
            failed_requests=failed_requests,
        )

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_166(
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
            recommendation=None,
            total_requests=total_requests,
            successful_requests=successful_requests,
            failed_requests=failed_requests,
        )

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_167(
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
            total_requests=None,
            successful_requests=successful_requests,
            failed_requests=failed_requests,
        )

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_168(
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
            successful_requests=None,
            failed_requests=failed_requests,
        )

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_169(
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
            failed_requests=None,
        )

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_170(
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_171(
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_172(
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_173(
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_174(
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_175(
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_176(
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
            budget_remaining_pct=remaining_pct,
            burn_rate=burn_rate,
            time_to_exhaustion_days=time_to_exhaustion_days,
            verdict=verdict,
            recommendation=recommendation,
            total_requests=total_requests,
            successful_requests=successful_requests,
            failed_requests=failed_requests,
        )

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_177(
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
            burn_rate=burn_rate,
            time_to_exhaustion_days=time_to_exhaustion_days,
            verdict=verdict,
            recommendation=recommendation,
            total_requests=total_requests,
            successful_requests=successful_requests,
            failed_requests=failed_requests,
        )

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_178(
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
            time_to_exhaustion_days=time_to_exhaustion_days,
            verdict=verdict,
            recommendation=recommendation,
            total_requests=total_requests,
            successful_requests=successful_requests,
            failed_requests=failed_requests,
        )

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_179(
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
            verdict=verdict,
            recommendation=recommendation,
            total_requests=total_requests,
            successful_requests=successful_requests,
            failed_requests=failed_requests,
        )

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_180(
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
            recommendation=recommendation,
            total_requests=total_requests,
            successful_requests=successful_requests,
            failed_requests=failed_requests,
        )

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_181(
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
            total_requests=total_requests,
            successful_requests=successful_requests,
            failed_requests=failed_requests,
        )

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_182(
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
            successful_requests=successful_requests,
            failed_requests=failed_requests,
        )

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_183(
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
            failed_requests=failed_requests,
        )

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_184(
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
            )

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_185(
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
            service_name=str(None),
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_186(
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
            service_name=str(raw_success_rate.get(None, "")),
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_187(
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
            service_name=str(raw_success_rate.get("service_name", None)),
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_188(
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
            service_name=str(raw_success_rate.get("")),
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_189(
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
            service_name=str(raw_success_rate.get("service_name", )),
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_190(
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
            service_name=str(raw_success_rate.get("XXservice_nameXX", "")),
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_191(
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
            service_name=str(raw_success_rate.get("SERVICE_NAME", "")),
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

    def xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_192(
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
            service_name=str(raw_success_rate.get("service_name", "XXXX")),
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

mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['_mutmut_orig'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_1'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_2'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_3'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_4'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_5'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_6'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_7'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_8'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_9'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_10'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_11'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_12'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_13'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_14'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_15'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_16'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_17'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_18'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_19'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_20'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_21'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_22'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_23'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_24'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_25'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_26'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_27'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_28'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_29'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_30'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_31'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_32'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_33'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_34'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_35'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_36'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_37'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_38'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_39'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_39 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_40'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_40 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_41'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_41 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_42'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_42 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_43'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_43 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_44'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_44 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_45'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_45 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_46'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_46 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_47'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_47 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_48'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_48 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_49'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_49 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_50'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_50 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_51'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_51 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_52'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_52 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_53'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_53 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_54'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_54 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_55'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_55 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_56'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_56 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_57'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_57 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_58'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_58 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_59'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_59 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_60'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_60 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_61'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_61 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_62'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_62 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_63'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_63 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_64'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_64 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_65'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_65 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_66'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_66 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_67'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_67 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_68'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_68 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_69'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_69 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_70'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_70 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_71'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_71 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_72'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_72 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_73'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_73 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_74'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_74 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_75'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_75 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_76'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_76 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_77'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_77 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_78'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_78 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_79'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_79 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_80'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_80 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_81'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_81 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_82'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_82 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_83'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_83 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_84'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_84 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_85'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_85 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_86'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_86 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_87'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_87 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_88'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_88 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_89'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_89 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_90'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_90 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_91'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_91 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_92'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_92 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_93'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_93 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_94'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_94 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_95'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_95 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_96'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_96 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_97'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_97 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_98'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_98 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_99'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_99 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_100'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_100 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_101'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_101 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_102'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_102 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_103'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_103 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_104'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_104 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_105'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_105 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_106'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_106 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_107'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_107 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_108'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_108 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_109'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_109 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_110'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_110 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_111'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_111 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_112'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_112 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_113'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_113 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_114'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_114 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_115'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_115 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_116'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_116 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_117'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_117 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_118'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_118 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_119'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_119 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_120'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_120 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_121'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_121 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_122'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_122 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_123'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_123 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_124'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_124 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_125'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_125 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_126'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_126 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_127'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_127 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_128'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_128 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_129'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_129 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_130'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_130 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_131'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_131 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_132'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_132 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_133'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_133 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_134'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_134 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_135'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_135 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_136'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_136 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_137'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_137 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_138'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_138 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_139'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_139 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_140'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_140 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_141'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_141 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_142'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_142 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_143'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_143 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_144'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_144 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_145'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_145 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_146'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_146 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_147'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_147 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_148'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_148 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_149'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_149 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_150'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_150 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_151'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_151 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_152'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_152 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_153'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_153 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_154'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_154 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_155'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_155 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_156'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_156 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_157'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_157 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_158'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_158 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_159'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_159 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_160'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_160 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_161'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_161 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_162'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_162 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_163'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_163 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_164'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_164 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_165'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_165 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_166'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_166 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_167'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_167 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_168'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_168 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_169'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_169 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_170'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_170 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_171'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_171 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_172'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_172 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_173'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_173 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_174'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_174 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_175'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_175 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_176'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_176 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_177'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_177 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_178'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_178 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_179'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_179 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_180'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_180 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_181'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_181 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_182'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_182 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_183'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_183 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_184'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_184 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_185'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_185 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_186'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_186 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_187'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_187 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_188'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_188 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_189'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_189 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_190'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_190 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_191'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_191 # type: ignore # mutmut generated
mutants_xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut['xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_192'] = SLOErrorBudgetBurnRateEngine.xǁSLOErrorBudgetBurnRateEngineǁcompute__mutmut_192 # type: ignore # mutmut generated
mutants_x__compute_exhaustion_time__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__compute_exhaustion_time__mutmut)
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


def x__compute_exhaustion_time__mutmut_orig(
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


def x__compute_exhaustion_time__mutmut_1(
    remaining_minutes: float,
    error_rate: float,
    error_budget_rate: float,
) -> float | None:
    if remaining_minutes < 0:
        return None
    excess_burn = error_rate - error_budget_rate
    if excess_burn <= 0:
        return None
    time_minutes = remaining_minutes / excess_burn
    return round(time_minutes / (24.0 * 60.0), 1)


def x__compute_exhaustion_time__mutmut_2(
    remaining_minutes: float,
    error_rate: float,
    error_budget_rate: float,
) -> float | None:
    if remaining_minutes <= 1:
        return None
    excess_burn = error_rate - error_budget_rate
    if excess_burn <= 0:
        return None
    time_minutes = remaining_minutes / excess_burn
    return round(time_minutes / (24.0 * 60.0), 1)


def x__compute_exhaustion_time__mutmut_3(
    remaining_minutes: float,
    error_rate: float,
    error_budget_rate: float,
) -> float | None:
    if remaining_minutes <= 0:
        return None
    excess_burn = None
    if excess_burn <= 0:
        return None
    time_minutes = remaining_minutes / excess_burn
    return round(time_minutes / (24.0 * 60.0), 1)


def x__compute_exhaustion_time__mutmut_4(
    remaining_minutes: float,
    error_rate: float,
    error_budget_rate: float,
) -> float | None:
    if remaining_minutes <= 0:
        return None
    excess_burn = error_rate + error_budget_rate
    if excess_burn <= 0:
        return None
    time_minutes = remaining_minutes / excess_burn
    return round(time_minutes / (24.0 * 60.0), 1)


def x__compute_exhaustion_time__mutmut_5(
    remaining_minutes: float,
    error_rate: float,
    error_budget_rate: float,
) -> float | None:
    if remaining_minutes <= 0:
        return None
    excess_burn = error_rate - error_budget_rate
    if excess_burn < 0:
        return None
    time_minutes = remaining_minutes / excess_burn
    return round(time_minutes / (24.0 * 60.0), 1)


def x__compute_exhaustion_time__mutmut_6(
    remaining_minutes: float,
    error_rate: float,
    error_budget_rate: float,
) -> float | None:
    if remaining_minutes <= 0:
        return None
    excess_burn = error_rate - error_budget_rate
    if excess_burn <= 1:
        return None
    time_minutes = remaining_minutes / excess_burn
    return round(time_minutes / (24.0 * 60.0), 1)


def x__compute_exhaustion_time__mutmut_7(
    remaining_minutes: float,
    error_rate: float,
    error_budget_rate: float,
) -> float | None:
    if remaining_minutes <= 0:
        return None
    excess_burn = error_rate - error_budget_rate
    if excess_burn <= 0:
        return None
    time_minutes = None
    return round(time_minutes / (24.0 * 60.0), 1)


def x__compute_exhaustion_time__mutmut_8(
    remaining_minutes: float,
    error_rate: float,
    error_budget_rate: float,
) -> float | None:
    if remaining_minutes <= 0:
        return None
    excess_burn = error_rate - error_budget_rate
    if excess_burn <= 0:
        return None
    time_minutes = remaining_minutes * excess_burn
    return round(time_minutes / (24.0 * 60.0), 1)


def x__compute_exhaustion_time__mutmut_9(
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
    return round(None, 1)


def x__compute_exhaustion_time__mutmut_10(
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
    return round(time_minutes / (24.0 * 60.0), None)


def x__compute_exhaustion_time__mutmut_11(
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
    return round(1)


def x__compute_exhaustion_time__mutmut_12(
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
    return round(time_minutes / (24.0 * 60.0), )


def x__compute_exhaustion_time__mutmut_13(
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
    return round(time_minutes * (24.0 * 60.0), 1)


def x__compute_exhaustion_time__mutmut_14(
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
    return round(time_minutes / (24.0 / 60.0), 1)


def x__compute_exhaustion_time__mutmut_15(
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
    return round(time_minutes / (25.0 * 60.0), 1)


def x__compute_exhaustion_time__mutmut_16(
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
    return round(time_minutes / (24.0 * 61.0), 1)


def x__compute_exhaustion_time__mutmut_17(
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
    return round(time_minutes / (24.0 * 60.0), 2)

mutants_x__compute_exhaustion_time__mutmut['_mutmut_orig'] = x__compute_exhaustion_time__mutmut_orig # type: ignore # mutmut generated
mutants_x__compute_exhaustion_time__mutmut['x__compute_exhaustion_time__mutmut_1'] = x__compute_exhaustion_time__mutmut_1 # type: ignore # mutmut generated
mutants_x__compute_exhaustion_time__mutmut['x__compute_exhaustion_time__mutmut_2'] = x__compute_exhaustion_time__mutmut_2 # type: ignore # mutmut generated
mutants_x__compute_exhaustion_time__mutmut['x__compute_exhaustion_time__mutmut_3'] = x__compute_exhaustion_time__mutmut_3 # type: ignore # mutmut generated
mutants_x__compute_exhaustion_time__mutmut['x__compute_exhaustion_time__mutmut_4'] = x__compute_exhaustion_time__mutmut_4 # type: ignore # mutmut generated
mutants_x__compute_exhaustion_time__mutmut['x__compute_exhaustion_time__mutmut_5'] = x__compute_exhaustion_time__mutmut_5 # type: ignore # mutmut generated
mutants_x__compute_exhaustion_time__mutmut['x__compute_exhaustion_time__mutmut_6'] = x__compute_exhaustion_time__mutmut_6 # type: ignore # mutmut generated
mutants_x__compute_exhaustion_time__mutmut['x__compute_exhaustion_time__mutmut_7'] = x__compute_exhaustion_time__mutmut_7 # type: ignore # mutmut generated
mutants_x__compute_exhaustion_time__mutmut['x__compute_exhaustion_time__mutmut_8'] = x__compute_exhaustion_time__mutmut_8 # type: ignore # mutmut generated
mutants_x__compute_exhaustion_time__mutmut['x__compute_exhaustion_time__mutmut_9'] = x__compute_exhaustion_time__mutmut_9 # type: ignore # mutmut generated
mutants_x__compute_exhaustion_time__mutmut['x__compute_exhaustion_time__mutmut_10'] = x__compute_exhaustion_time__mutmut_10 # type: ignore # mutmut generated
mutants_x__compute_exhaustion_time__mutmut['x__compute_exhaustion_time__mutmut_11'] = x__compute_exhaustion_time__mutmut_11 # type: ignore # mutmut generated
mutants_x__compute_exhaustion_time__mutmut['x__compute_exhaustion_time__mutmut_12'] = x__compute_exhaustion_time__mutmut_12 # type: ignore # mutmut generated
mutants_x__compute_exhaustion_time__mutmut['x__compute_exhaustion_time__mutmut_13'] = x__compute_exhaustion_time__mutmut_13 # type: ignore # mutmut generated
mutants_x__compute_exhaustion_time__mutmut['x__compute_exhaustion_time__mutmut_14'] = x__compute_exhaustion_time__mutmut_14 # type: ignore # mutmut generated
mutants_x__compute_exhaustion_time__mutmut['x__compute_exhaustion_time__mutmut_15'] = x__compute_exhaustion_time__mutmut_15 # type: ignore # mutmut generated
mutants_x__compute_exhaustion_time__mutmut['x__compute_exhaustion_time__mutmut_16'] = x__compute_exhaustion_time__mutmut_16 # type: ignore # mutmut generated
mutants_x__compute_exhaustion_time__mutmut['x__compute_exhaustion_time__mutmut_17'] = x__compute_exhaustion_time__mutmut_17 # type: ignore # mutmut generated
mutants_x__classify_verdict__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__classify_verdict__mutmut)
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


def x__classify_verdict__mutmut_orig(
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


def x__classify_verdict__mutmut_1(
    burn_rate: float,
    remaining_pct: float,
) -> tuple[str, str]:
    if remaining_pct < 0:
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


def x__classify_verdict__mutmut_2(
    burn_rate: float,
    remaining_pct: float,
) -> tuple[str, str]:
    if remaining_pct <= 1:
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


def x__classify_verdict__mutmut_3(
    burn_rate: float,
    remaining_pct: float,
) -> tuple[str, str]:
    if remaining_pct <= 0:
        return (
            "XXbudget_exhaustedXX",
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


def x__classify_verdict__mutmut_4(
    burn_rate: float,
    remaining_pct: float,
) -> tuple[str, str]:
    if remaining_pct <= 0:
        return (
            "BUDGET_EXHAUSTED",
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


def x__classify_verdict__mutmut_5(
    burn_rate: float,
    remaining_pct: float,
) -> tuple[str, str]:
    if remaining_pct <= 0:
        return (
            "budget_exhausted",
            f"Immediate action required: error rate {burn_rate}x above SLO allowance",
        )

    if burn_rate > 1.0:
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


def x__classify_verdict__mutmut_6(
    burn_rate: float,
    remaining_pct: float,
) -> tuple[str, str]:
    if remaining_pct <= 0:
        return (
            "budget_exhausted",
            f"Immediate action required: error rate {burn_rate}x above SLO allowance",
        )

    if burn_rate >= 2.0:
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


def x__classify_verdict__mutmut_7(
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
            "XXbudget_at_riskXX",
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


def x__classify_verdict__mutmut_8(
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
            "BUDGET_AT_RISK",
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


def x__classify_verdict__mutmut_9(
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

    if burn_rate != 0.0:
        return (
            "budget_safe",
            "No errors — budget fully intact",
        )

    return (
        "budget_accumulating",
        "Performance better than SLO — budget accumulating",
    )


def x__classify_verdict__mutmut_10(
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

    if burn_rate == 1.0:
        return (
            "budget_safe",
            "No errors — budget fully intact",
        )

    return (
        "budget_accumulating",
        "Performance better than SLO — budget accumulating",
    )


def x__classify_verdict__mutmut_11(
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
            "XXbudget_safeXX",
            "No errors — budget fully intact",
        )

    return (
        "budget_accumulating",
        "Performance better than SLO — budget accumulating",
    )


def x__classify_verdict__mutmut_12(
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
            "BUDGET_SAFE",
            "No errors — budget fully intact",
        )

    return (
        "budget_accumulating",
        "Performance better than SLO — budget accumulating",
    )


def x__classify_verdict__mutmut_13(
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
            "XXNo errors — budget fully intactXX",
        )

    return (
        "budget_accumulating",
        "Performance better than SLO — budget accumulating",
    )


def x__classify_verdict__mutmut_14(
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
            "no errors — budget fully intact",
        )

    return (
        "budget_accumulating",
        "Performance better than SLO — budget accumulating",
    )


def x__classify_verdict__mutmut_15(
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
            "NO ERRORS — BUDGET FULLY INTACT",
        )

    return (
        "budget_accumulating",
        "Performance better than SLO — budget accumulating",
    )


def x__classify_verdict__mutmut_16(
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
        "XXbudget_accumulatingXX",
        "Performance better than SLO — budget accumulating",
    )


def x__classify_verdict__mutmut_17(
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
        "BUDGET_ACCUMULATING",
        "Performance better than SLO — budget accumulating",
    )


def x__classify_verdict__mutmut_18(
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
        "XXPerformance better than SLO — budget accumulatingXX",
    )


def x__classify_verdict__mutmut_19(
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
        "performance better than slo — budget accumulating",
    )


def x__classify_verdict__mutmut_20(
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
        "PERFORMANCE BETTER THAN SLO — BUDGET ACCUMULATING",
    )

mutants_x__classify_verdict__mutmut['_mutmut_orig'] = x__classify_verdict__mutmut_orig # type: ignore # mutmut generated
mutants_x__classify_verdict__mutmut['x__classify_verdict__mutmut_1'] = x__classify_verdict__mutmut_1 # type: ignore # mutmut generated
mutants_x__classify_verdict__mutmut['x__classify_verdict__mutmut_2'] = x__classify_verdict__mutmut_2 # type: ignore # mutmut generated
mutants_x__classify_verdict__mutmut['x__classify_verdict__mutmut_3'] = x__classify_verdict__mutmut_3 # type: ignore # mutmut generated
mutants_x__classify_verdict__mutmut['x__classify_verdict__mutmut_4'] = x__classify_verdict__mutmut_4 # type: ignore # mutmut generated
mutants_x__classify_verdict__mutmut['x__classify_verdict__mutmut_5'] = x__classify_verdict__mutmut_5 # type: ignore # mutmut generated
mutants_x__classify_verdict__mutmut['x__classify_verdict__mutmut_6'] = x__classify_verdict__mutmut_6 # type: ignore # mutmut generated
mutants_x__classify_verdict__mutmut['x__classify_verdict__mutmut_7'] = x__classify_verdict__mutmut_7 # type: ignore # mutmut generated
mutants_x__classify_verdict__mutmut['x__classify_verdict__mutmut_8'] = x__classify_verdict__mutmut_8 # type: ignore # mutmut generated
mutants_x__classify_verdict__mutmut['x__classify_verdict__mutmut_9'] = x__classify_verdict__mutmut_9 # type: ignore # mutmut generated
mutants_x__classify_verdict__mutmut['x__classify_verdict__mutmut_10'] = x__classify_verdict__mutmut_10 # type: ignore # mutmut generated
mutants_x__classify_verdict__mutmut['x__classify_verdict__mutmut_11'] = x__classify_verdict__mutmut_11 # type: ignore # mutmut generated
mutants_x__classify_verdict__mutmut['x__classify_verdict__mutmut_12'] = x__classify_verdict__mutmut_12 # type: ignore # mutmut generated
mutants_x__classify_verdict__mutmut['x__classify_verdict__mutmut_13'] = x__classify_verdict__mutmut_13 # type: ignore # mutmut generated
mutants_x__classify_verdict__mutmut['x__classify_verdict__mutmut_14'] = x__classify_verdict__mutmut_14 # type: ignore # mutmut generated
mutants_x__classify_verdict__mutmut['x__classify_verdict__mutmut_15'] = x__classify_verdict__mutmut_15 # type: ignore # mutmut generated
mutants_x__classify_verdict__mutmut['x__classify_verdict__mutmut_16'] = x__classify_verdict__mutmut_16 # type: ignore # mutmut generated
mutants_x__classify_verdict__mutmut['x__classify_verdict__mutmut_17'] = x__classify_verdict__mutmut_17 # type: ignore # mutmut generated
mutants_x__classify_verdict__mutmut['x__classify_verdict__mutmut_18'] = x__classify_verdict__mutmut_18 # type: ignore # mutmut generated
mutants_x__classify_verdict__mutmut['x__classify_verdict__mutmut_19'] = x__classify_verdict__mutmut_19 # type: ignore # mutmut generated
mutants_x__classify_verdict__mutmut['x__classify_verdict__mutmut_20'] = x__classify_verdict__mutmut_20 # type: ignore # mutmut generated
mutants_x__as_float__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__as_float__mutmut)
def _as_float(value: object) -> float:
    if value is None:
        return 0.0
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def x__as_float__mutmut_orig(value: object) -> float:
    if value is None:
        return 0.0
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def x__as_float__mutmut_1(value: object) -> float:
    if value is not None:
        return 0.0
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def x__as_float__mutmut_2(value: object) -> float:
    if value is None:
        return 1.0
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def x__as_float__mutmut_3(value: object) -> float:
    if value is None:
        return 0.0
    try:
        return float(None)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


def x__as_float__mutmut_4(value: object) -> float:
    if value is None:
        return 0.0
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 1.0

mutants_x__as_float__mutmut['_mutmut_orig'] = x__as_float__mutmut_orig # type: ignore # mutmut generated
mutants_x__as_float__mutmut['x__as_float__mutmut_1'] = x__as_float__mutmut_1 # type: ignore # mutmut generated
mutants_x__as_float__mutmut['x__as_float__mutmut_2'] = x__as_float__mutmut_2 # type: ignore # mutmut generated
mutants_x__as_float__mutmut['x__as_float__mutmut_3'] = x__as_float__mutmut_3 # type: ignore # mutmut generated
mutants_x__as_float__mutmut['x__as_float__mutmut_4'] = x__as_float__mutmut_4 # type: ignore # mutmut generated
mutants_x__as_int__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__as_int__mutmut)
def _as_int(value: object) -> int:
    if value is None:
        return 0
    try:
        return int(float(value))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def x__as_int__mutmut_orig(value: object) -> int:
    if value is None:
        return 0
    try:
        return int(float(value))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def x__as_int__mutmut_1(value: object) -> int:
    if value is not None:
        return 0
    try:
        return int(float(value))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def x__as_int__mutmut_2(value: object) -> int:
    if value is None:
        return 1
    try:
        return int(float(value))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def x__as_int__mutmut_3(value: object) -> int:
    if value is None:
        return 0
    try:
        return int(None)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def x__as_int__mutmut_4(value: object) -> int:
    if value is None:
        return 0
    try:
        return int(float(None))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def x__as_int__mutmut_5(value: object) -> int:
    if value is None:
        return 0
    try:
        return int(float(value))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 1

mutants_x__as_int__mutmut['_mutmut_orig'] = x__as_int__mutmut_orig # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_1'] = x__as_int__mutmut_1 # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_2'] = x__as_int__mutmut_2 # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_3'] = x__as_int__mutmut_3 # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_4'] = x__as_int__mutmut_4 # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_5'] = x__as_int__mutmut_5 # type: ignore # mutmut generated
mutants_x__as_bool__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__as_bool__mutmut)
def _as_bool(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    return bool(value)


def x__as_bool__mutmut_orig(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    return bool(value)


def x__as_bool__mutmut_1(value: object) -> bool:
    if value is not None:
        return False
    if isinstance(value, bool):
        return value
    return bool(value)


def x__as_bool__mutmut_2(value: object) -> bool:
    if value is None:
        return True
    if isinstance(value, bool):
        return value
    return bool(value)


def x__as_bool__mutmut_3(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    return bool(None)

mutants_x__as_bool__mutmut['_mutmut_orig'] = x__as_bool__mutmut_orig # type: ignore # mutmut generated
mutants_x__as_bool__mutmut['x__as_bool__mutmut_1'] = x__as_bool__mutmut_1 # type: ignore # mutmut generated
mutants_x__as_bool__mutmut['x__as_bool__mutmut_2'] = x__as_bool__mutmut_2 # type: ignore # mutmut generated
mutants_x__as_bool__mutmut['x__as_bool__mutmut_3'] = x__as_bool__mutmut_3 # type: ignore # mutmut generated
