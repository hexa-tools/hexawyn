from __future__ import annotations

from hexawyn.application.ports.driven.error_budget_port import (
    ErrorBudgetPort,
    ServiceSuccessRateRawData,
)
from hexawyn.application.ports.driven.metrics_query_port import MetricsQueryPort


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁPrometheusErrorBudgetAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut: MutantDict = {}  # type: ignore


class PrometheusErrorBudgetAdapter(ErrorBudgetPort):
    @_mutmut_mutated(mutants_xǁPrometheusErrorBudgetAdapterǁ__init____mutmut)
    def __init__(self, metrics_query_port: MetricsQueryPort) -> None:
        self._metrics = metrics_query_port
    def xǁPrometheusErrorBudgetAdapterǁ__init____mutmut_orig(self, metrics_query_port: MetricsQueryPort) -> None:
        self._metrics = metrics_query_port
    def xǁPrometheusErrorBudgetAdapterǁ__init____mutmut_1(self, metrics_query_port: MetricsQueryPort) -> None:
        self._metrics = None

    @_mutmut_mutated(mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut)
    def fetch_success_rate(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_orig(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_1(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = None
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_2(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 / 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_3(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 / 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_4(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days / 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_5(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 25 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_6(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 61 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_7(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 61
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_8(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = None
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_9(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(None, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_10(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, None)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_11(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_12(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, )
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_13(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = None

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_14(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(None, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_15(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=None)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_16(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_17(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, )

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_18(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=16.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_19(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_20(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=None,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_21(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=None,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_22(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=None,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_23(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=None,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_24(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=None,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_25(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=None,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_26(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=None,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_27(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=None,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_28(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_29(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_30(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_31(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_32(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_33(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_34(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_35(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_36(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=1,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_37(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=1,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_38(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=1,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_39(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=1.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_40(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=1.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_41(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=True,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_42(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = None
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_43(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[1]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_44(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = None

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_45(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(None)

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_46(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["XXvalueXX"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_47(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["VALUE"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_48(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = None
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_49(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 + success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_50(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 2.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_51(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = None
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_52(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = None

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_53(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(None)

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_54(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(None))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_55(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get(None, 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_56(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", None)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_57(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get(0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_58(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", )))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_59(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get(None, {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_60(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", None).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_61(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get({}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_62(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", ).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_63(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("XXmetricXX", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_64(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("METRIC", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_65(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("XXtotal_requestsXX", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_66(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("TOTAL_REQUESTS", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_67(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 1)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_68(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw >= 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_69(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 1:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_70(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = None
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_71(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(None)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_72(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw / total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_73(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = None
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_74(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw + failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_75(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = None
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_76(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 1
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_77(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = None

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_78(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 1

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_79(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=None,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_80(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=None,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_81(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=None,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_82(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=None,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_83(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=None,
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_84(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=None,
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_85(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=None,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_86(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=None,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_87(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_88(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_89(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_90(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_91(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_92(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_93(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_94(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_95(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(None, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_96(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, None),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_97(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_98(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, ),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_99(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 7),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_100(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(None, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_101(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, None),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_102(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_103(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, ),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_104(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 7),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_105(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=False,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_106(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=None,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_107(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=None,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_108(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=None,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_109(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=None,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_110(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=None,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_111(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=None,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_112(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=None,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_113(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=None,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_114(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_115(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_116(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_117(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_118(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_119(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_120(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_121(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_122(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=1,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_123(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=1,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_124(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=1,
                success_rate=0.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_125(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=1.0,
                error_rate=0.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_126(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=1.0,
                has_data=False,
                observation_days=window_days,
            )

    def xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_127(self, service_name: str, window_days: int) -> ServiceSuccessRateRawData:
        try:
            window_seconds = window_days * 24 * 60 * 60
            promql = _build_success_rate_query(service_name, window_seconds)
            samples = self._metrics.instant_query(promql, timeout_seconds=15.0)

            if not samples:
                return ServiceSuccessRateRawData(
                    service_name=service_name,
                    total_requests=0,
                    successful_requests=0,
                    failed_requests=0,
                    success_rate=0.0,
                    error_rate=0.0,
                    has_data=False,
                    observation_days=window_days,
                )

            first = samples[0]
            success_rate = float(first["value"])

            error_rate_raw = 1.0 - success_rate
            observation_days = window_days
            total_requests_raw = int(float(first.get("metric", {}).get("total_requests", 0)))

            if total_requests_raw > 0:
                failed = int(error_rate_raw * total_requests_raw)
                successful = total_requests_raw - failed
            else:
                failed = 0
                successful = 0

            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=total_requests_raw,
                successful_requests=successful,
                failed_requests=failed,
                success_rate=round(success_rate, 6),
                error_rate=round(error_rate_raw, 6),
                has_data=True,
                observation_days=observation_days,
            )
        except Exception:
            return ServiceSuccessRateRawData(
                service_name=service_name,
                total_requests=0,
                successful_requests=0,
                failed_requests=0,
                success_rate=0.0,
                error_rate=0.0,
                has_data=True,
                observation_days=window_days,
            )

mutants_xǁPrometheusErrorBudgetAdapterǁ__init____mutmut['_mutmut_orig'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁ__init____mutmut['xǁPrometheusErrorBudgetAdapterǁ__init____mutmut_1'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['_mutmut_orig'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_1'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_2'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_3'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_4'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_5'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_6'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_7'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_8'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_9'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_10'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_11'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_12'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_13'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_13 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_14'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_14 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_15'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_15 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_16'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_16 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_17'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_17 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_18'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_18 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_19'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_19 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_20'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_20 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_21'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_21 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_22'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_22 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_23'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_23 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_24'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_24 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_25'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_25 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_26'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_26 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_27'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_27 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_28'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_28 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_29'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_29 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_30'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_30 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_31'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_31 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_32'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_32 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_33'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_33 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_34'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_34 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_35'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_35 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_36'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_36 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_37'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_37 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_38'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_38 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_39'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_39 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_40'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_40 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_41'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_41 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_42'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_42 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_43'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_43 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_44'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_44 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_45'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_45 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_46'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_46 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_47'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_47 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_48'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_48 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_49'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_49 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_50'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_50 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_51'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_51 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_52'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_52 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_53'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_53 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_54'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_54 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_55'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_55 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_56'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_56 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_57'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_57 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_58'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_58 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_59'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_59 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_60'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_60 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_61'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_61 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_62'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_62 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_63'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_63 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_64'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_64 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_65'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_65 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_66'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_66 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_67'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_67 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_68'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_68 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_69'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_69 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_70'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_70 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_71'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_71 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_72'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_72 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_73'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_73 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_74'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_74 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_75'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_75 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_76'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_76 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_77'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_77 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_78'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_78 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_79'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_79 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_80'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_80 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_81'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_81 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_82'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_82 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_83'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_83 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_84'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_84 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_85'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_85 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_86'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_86 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_87'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_87 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_88'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_88 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_89'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_89 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_90'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_90 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_91'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_91 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_92'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_92 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_93'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_93 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_94'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_94 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_95'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_95 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_96'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_96 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_97'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_97 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_98'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_98 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_99'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_99 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_100'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_100 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_101'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_101 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_102'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_102 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_103'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_103 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_104'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_104 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_105'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_105 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_106'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_106 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_107'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_107 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_108'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_108 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_109'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_109 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_110'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_110 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_111'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_111 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_112'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_112 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_113'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_113 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_114'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_114 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_115'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_115 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_116'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_116 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_117'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_117 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_118'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_118 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_119'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_119 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_120'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_120 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_121'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_121 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_122'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_122 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_123'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_123 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_124'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_124 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_125'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_125 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_126'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_126 # type: ignore # mutmut generated
mutants_xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut['xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_127'] = PrometheusErrorBudgetAdapter.xǁPrometheusErrorBudgetAdapterǁfetch_success_rate__mutmut_127 # type: ignore # mutmut generated


def _build_success_rate_query(service_name: str, window_seconds: int) -> str:
    return (
        f'sum(rate(http_requests_total{{service="{service_name}",'
        f'code!~"5.."}}[{window_seconds}s]))'
        f" / "
        f'sum(rate(http_requests_total{{service="{service_name}"}}'
        f"[{window_seconds}s]))"
    )
