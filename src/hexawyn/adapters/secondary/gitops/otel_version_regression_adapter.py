from __future__ import annotations

from hexawyn.adapters.secondary.gitops.otel_http_client import query_prometheus_instant
from hexawyn.application.ports.driven.version_regression_port import (
    VersionRegressionPort,
)
from hexawyn.domain.models.version_regression import (
    VersionComparisonRequest,
    VersionMetrics,
)


class OTelVersionRegressionAdapter(VersionRegressionPort):
    def fetch_baseline_metrics(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="unknown",
                p50_ms=0.0,
                p95_ms=0.0,
                p99_ms=0.0,
                error_rate_pct=0.0,
                request_count=0,
            )

        try:
            p50_q = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[5m]))'  # noqa: E501
            p99_q = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[5m]))'  # noqa: E501
            count_q = (
                f'rate(http_request_duration_seconds_count{{service="{request.service_name}"}}[5m])'  # noqa: E501
            )

            p50 = query_prometheus_instant(p50_q)
            p99 = query_prometheus_instant(p99_q)
            count = query_prometheus_instant(count_q)

            return VersionMetrics(
                version=request.baseline_version or "baseline",  # type: ignore
                request_count=int(count[0]["value"]) if count else 0,
                p50_ms=round(p50[0]["value"] * 1000.0, 2) if p50 else 0.0,
                p95_ms=0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                error_rate_pct=0.0,
            )
        except Exception:
            return VersionMetrics(
                version="unknown",
                p50_ms=0.0,
                p95_ms=0.0,
                p99_ms=0.0,
                error_rate_pct=0.0,
                request_count=0,
            )

    def fetch_current_metrics(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="unknown",
                p50_ms=0.0,
                p95_ms=0.0,
                p99_ms=0.0,
                error_rate_pct=0.0,
                request_count=0,
            )

        try:
            p50_q = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[5m]) offset 5m)'  # noqa: E501
            p99_q = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[5m]) offset 5m)'  # noqa: E501
            count_q = (
                f'rate(http_request_duration_seconds_count{{service="{request.service_name}"}}[5m])'  # noqa: E501
            )

            p50 = query_prometheus_instant(p50_q)
            p99 = query_prometheus_instant(p99_q)
            count = query_prometheus_instant(count_q)

            return VersionMetrics(
                version=request.current_version or "current",  # type: ignore
                request_count=int(count[0]["value"]) if count else 0,
                p50_ms=round(p50[0]["value"] * 1000.0, 2) if p50 else 0.0,
                p95_ms=0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                error_rate_pct=0.0,
            )
        except Exception:
            return VersionMetrics(
                version="unknown",
                p50_ms=0.0,
                p95_ms=0.0,
                p99_ms=0.0,
                error_rate_pct=0.0,
                request_count=0,
            )
