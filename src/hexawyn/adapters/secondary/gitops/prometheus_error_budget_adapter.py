from __future__ import annotations

from hexawyn.application.ports.driven.error_budget_port import (
    ErrorBudgetPort,
    ServiceSuccessRateRawData,
)
from hexawyn.application.ports.driven.metrics_query_port import MetricsQueryPort


class PrometheusErrorBudgetAdapter(ErrorBudgetPort):
    def __init__(self, metrics_query_port: MetricsQueryPort) -> None:
        self._metrics = metrics_query_port

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


def _build_success_rate_query(service_name: str, window_seconds: int) -> str:
    return (
        f'sum(rate(http_requests_total{{service="{service_name}",'
        f'code!~"5.."}}[{window_seconds}s]))'
        f" / "
        f'sum(rate(http_requests_total{{service="{service_name}"}}'
        f"[{window_seconds}s]))"
    )
