from __future__ import annotations

from hexawyn.application.ports.driven.version_regression_port import (
    VersionRegressionPort,
)
from hexawyn.domain.models.version_regression import (
    VersionComparisonRequest,
    VersionMetrics,
)
from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_client import (
    query_prometheus_instant,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut: MutantDict = {}  # type: ignore
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut: MutantDict = {}  # type: ignore


class OTelVersionRegressionAdapter(VersionRegressionPort):
    @_mutmut_mutated(mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut)
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_orig(self, request: VersionComparisonRequest) -> VersionMetrics:
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_1(self, request: VersionComparisonRequest) -> VersionMetrics:
        if request.service_name:
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_2(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version=None,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_3(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="unknown",
                p50_ms=None,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_4(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="unknown",
                p50_ms=0.0,
                p95_ms=None,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_5(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="unknown",
                p50_ms=0.0,
                p95_ms=0.0,
                p99_ms=None,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_6(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="unknown",
                p50_ms=0.0,
                p95_ms=0.0,
                p99_ms=0.0,
                error_rate_pct=None,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_7(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="unknown",
                p50_ms=0.0,
                p95_ms=0.0,
                p99_ms=0.0,
                error_rate_pct=0.0,
                request_count=None,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_8(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_9(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="unknown",
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_10(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="unknown",
                p50_ms=0.0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_11(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="unknown",
                p50_ms=0.0,
                p95_ms=0.0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_12(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="unknown",
                p50_ms=0.0,
                p95_ms=0.0,
                p99_ms=0.0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_13(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="unknown",
                p50_ms=0.0,
                p95_ms=0.0,
                p99_ms=0.0,
                error_rate_pct=0.0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_14(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="XXunknownXX",
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_15(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="UNKNOWN",
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_16(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="unknown",
                p50_ms=1.0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_17(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="unknown",
                p50_ms=0.0,
                p95_ms=1.0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_18(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="unknown",
                p50_ms=0.0,
                p95_ms=0.0,
                p99_ms=1.0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_19(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="unknown",
                p50_ms=0.0,
                p95_ms=0.0,
                p99_ms=0.0,
                error_rate_pct=1.0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_20(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="unknown",
                p50_ms=0.0,
                p95_ms=0.0,
                p99_ms=0.0,
                error_rate_pct=0.0,
                request_count=1,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_21(self, request: VersionComparisonRequest) -> VersionMetrics:
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
            p50_q = None  # noqa: E501
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_22(self, request: VersionComparisonRequest) -> VersionMetrics:
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
            p99_q = None  # noqa: E501
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_23(self, request: VersionComparisonRequest) -> VersionMetrics:
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
            count_q = None

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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_24(self, request: VersionComparisonRequest) -> VersionMetrics:
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

            p50 = None
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_25(self, request: VersionComparisonRequest) -> VersionMetrics:
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

            p50 = query_prometheus_instant(None)
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_26(self, request: VersionComparisonRequest) -> VersionMetrics:
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
            p99 = None
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_27(self, request: VersionComparisonRequest) -> VersionMetrics:
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
            p99 = query_prometheus_instant(None)
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_28(self, request: VersionComparisonRequest) -> VersionMetrics:
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
            count = None

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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_29(self, request: VersionComparisonRequest) -> VersionMetrics:
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
            count = query_prometheus_instant(None)

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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_30(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                version=None,  # type: ignore
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_31(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                request_count=None,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_32(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p50_ms=None,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_33(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p95_ms=None,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_34(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p99_ms=None,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_35(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                error_rate_pct=None,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_36(self, request: VersionComparisonRequest) -> VersionMetrics:
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_37(self, request: VersionComparisonRequest) -> VersionMetrics:
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_38(self, request: VersionComparisonRequest) -> VersionMetrics:
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_39(self, request: VersionComparisonRequest) -> VersionMetrics:
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_40(self, request: VersionComparisonRequest) -> VersionMetrics:
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_41(self, request: VersionComparisonRequest) -> VersionMetrics:
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_42(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                version=request.baseline_version and "baseline",  # type: ignore
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_43(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                version=request.baseline_version or "XXbaselineXX",  # type: ignore
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_44(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                version=request.baseline_version or "BASELINE",  # type: ignore
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_45(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                request_count=int(None) if count else 0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_46(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                request_count=int(count[1]["value"]) if count else 0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_47(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                request_count=int(count[0]["XXvalueXX"]) if count else 0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_48(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                request_count=int(count[0]["VALUE"]) if count else 0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_49(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                request_count=int(count[0]["value"]) if count else 1,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_50(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p50_ms=round(None, 2) if p50 else 0.0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_51(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p50_ms=round(p50[0]["value"] * 1000.0, None) if p50 else 0.0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_52(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p50_ms=round(2) if p50 else 0.0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_53(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p50_ms=round(p50[0]["value"] * 1000.0, ) if p50 else 0.0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_54(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p50_ms=round(p50[0]["value"] / 1000.0, 2) if p50 else 0.0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_55(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p50_ms=round(p50[1]["value"] * 1000.0, 2) if p50 else 0.0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_56(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p50_ms=round(p50[0]["XXvalueXX"] * 1000.0, 2) if p50 else 0.0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_57(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p50_ms=round(p50[0]["VALUE"] * 1000.0, 2) if p50 else 0.0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_58(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p50_ms=round(p50[0]["value"] * 1001.0, 2) if p50 else 0.0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_59(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p50_ms=round(p50[0]["value"] * 1000.0, 3) if p50 else 0.0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_60(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p50_ms=round(p50[0]["value"] * 1000.0, 2) if p50 else 1.0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_61(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p95_ms=1.0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_62(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p99_ms=round(None, 2) if p99 else 0.0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_63(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p99_ms=round(p99[0]["value"] * 1000.0, None) if p99 else 0.0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_64(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p99_ms=round(2) if p99 else 0.0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_65(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p99_ms=round(p99[0]["value"] * 1000.0, ) if p99 else 0.0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_66(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p99_ms=round(p99[0]["value"] / 1000.0, 2) if p99 else 0.0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_67(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p99_ms=round(p99[1]["value"] * 1000.0, 2) if p99 else 0.0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_68(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p99_ms=round(p99[0]["XXvalueXX"] * 1000.0, 2) if p99 else 0.0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_69(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p99_ms=round(p99[0]["VALUE"] * 1000.0, 2) if p99 else 0.0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_70(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p99_ms=round(p99[0]["value"] * 1001.0, 2) if p99 else 0.0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_71(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p99_ms=round(p99[0]["value"] * 1000.0, 3) if p99 else 0.0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_72(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 1.0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_73(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                error_rate_pct=1.0,
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
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_74(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                version=None,
                p50_ms=0.0,
                p95_ms=0.0,
                p99_ms=0.0,
                error_rate_pct=0.0,
                request_count=0,
            )
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_75(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p50_ms=None,
                p95_ms=0.0,
                p99_ms=0.0,
                error_rate_pct=0.0,
                request_count=0,
            )
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_76(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p95_ms=None,
                p99_ms=0.0,
                error_rate_pct=0.0,
                request_count=0,
            )
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_77(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p99_ms=None,
                error_rate_pct=0.0,
                request_count=0,
            )
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_78(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                error_rate_pct=None,
                request_count=0,
            )
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_79(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                request_count=None,
            )
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_80(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p50_ms=0.0,
                p95_ms=0.0,
                p99_ms=0.0,
                error_rate_pct=0.0,
                request_count=0,
            )
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_81(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p95_ms=0.0,
                p99_ms=0.0,
                error_rate_pct=0.0,
                request_count=0,
            )
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_82(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p99_ms=0.0,
                error_rate_pct=0.0,
                request_count=0,
            )
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_83(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                error_rate_pct=0.0,
                request_count=0,
            )
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_84(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                request_count=0,
            )
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_85(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                )
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_86(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                version="XXunknownXX",
                p50_ms=0.0,
                p95_ms=0.0,
                p99_ms=0.0,
                error_rate_pct=0.0,
                request_count=0,
            )
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_87(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                version="UNKNOWN",
                p50_ms=0.0,
                p95_ms=0.0,
                p99_ms=0.0,
                error_rate_pct=0.0,
                request_count=0,
            )
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_88(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p50_ms=1.0,
                p95_ms=0.0,
                p99_ms=0.0,
                error_rate_pct=0.0,
                request_count=0,
            )
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_89(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p95_ms=1.0,
                p99_ms=0.0,
                error_rate_pct=0.0,
                request_count=0,
            )
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_90(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p99_ms=1.0,
                error_rate_pct=0.0,
                request_count=0,
            )
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_91(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                error_rate_pct=1.0,
                request_count=0,
            )
    def xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_92(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                request_count=1,
            )

    @_mutmut_mutated(mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut)
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_orig(self, request: VersionComparisonRequest) -> VersionMetrics:
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_1(self, request: VersionComparisonRequest) -> VersionMetrics:
        if request.service_name:
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_2(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version=None,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_3(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="unknown",
                p50_ms=None,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_4(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="unknown",
                p50_ms=0.0,
                p95_ms=None,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_5(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="unknown",
                p50_ms=0.0,
                p95_ms=0.0,
                p99_ms=None,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_6(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="unknown",
                p50_ms=0.0,
                p95_ms=0.0,
                p99_ms=0.0,
                error_rate_pct=None,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_7(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="unknown",
                p50_ms=0.0,
                p95_ms=0.0,
                p99_ms=0.0,
                error_rate_pct=0.0,
                request_count=None,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_8(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_9(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="unknown",
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_10(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="unknown",
                p50_ms=0.0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_11(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="unknown",
                p50_ms=0.0,
                p95_ms=0.0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_12(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="unknown",
                p50_ms=0.0,
                p95_ms=0.0,
                p99_ms=0.0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_13(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="unknown",
                p50_ms=0.0,
                p95_ms=0.0,
                p99_ms=0.0,
                error_rate_pct=0.0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_14(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="XXunknownXX",
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_15(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="UNKNOWN",
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_16(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="unknown",
                p50_ms=1.0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_17(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="unknown",
                p50_ms=0.0,
                p95_ms=1.0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_18(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="unknown",
                p50_ms=0.0,
                p95_ms=0.0,
                p99_ms=1.0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_19(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="unknown",
                p50_ms=0.0,
                p95_ms=0.0,
                p99_ms=0.0,
                error_rate_pct=1.0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_20(self, request: VersionComparisonRequest) -> VersionMetrics:
        if not request.service_name:
            return VersionMetrics(
                version="unknown",
                p50_ms=0.0,
                p95_ms=0.0,
                p99_ms=0.0,
                error_rate_pct=0.0,
                request_count=1,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_21(self, request: VersionComparisonRequest) -> VersionMetrics:
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
            p50_q = None  # noqa: E501
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_22(self, request: VersionComparisonRequest) -> VersionMetrics:
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
            p99_q = None  # noqa: E501
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_23(self, request: VersionComparisonRequest) -> VersionMetrics:
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
            count_q = None

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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_24(self, request: VersionComparisonRequest) -> VersionMetrics:
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

            p50 = None
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_25(self, request: VersionComparisonRequest) -> VersionMetrics:
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

            p50 = query_prometheus_instant(None)
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_26(self, request: VersionComparisonRequest) -> VersionMetrics:
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
            p99 = None
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_27(self, request: VersionComparisonRequest) -> VersionMetrics:
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
            p99 = query_prometheus_instant(None)
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_28(self, request: VersionComparisonRequest) -> VersionMetrics:
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
            count = None

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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_29(self, request: VersionComparisonRequest) -> VersionMetrics:
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
            count = query_prometheus_instant(None)

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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_30(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                version=None,  # type: ignore
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_31(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                request_count=None,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_32(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p50_ms=None,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_33(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p95_ms=None,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_34(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p99_ms=None,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_35(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                error_rate_pct=None,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_36(self, request: VersionComparisonRequest) -> VersionMetrics:
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_37(self, request: VersionComparisonRequest) -> VersionMetrics:
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_38(self, request: VersionComparisonRequest) -> VersionMetrics:
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_39(self, request: VersionComparisonRequest) -> VersionMetrics:
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_40(self, request: VersionComparisonRequest) -> VersionMetrics:
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_41(self, request: VersionComparisonRequest) -> VersionMetrics:
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_42(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                version=request.current_version and "current",  # type: ignore
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_43(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                version=request.current_version or "XXcurrentXX",  # type: ignore
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_44(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                version=request.current_version or "CURRENT",  # type: ignore
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_45(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                request_count=int(None) if count else 0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_46(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                request_count=int(count[1]["value"]) if count else 0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_47(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                request_count=int(count[0]["XXvalueXX"]) if count else 0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_48(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                request_count=int(count[0]["VALUE"]) if count else 0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_49(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                request_count=int(count[0]["value"]) if count else 1,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_50(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p50_ms=round(None, 2) if p50 else 0.0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_51(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p50_ms=round(p50[0]["value"] * 1000.0, None) if p50 else 0.0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_52(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p50_ms=round(2) if p50 else 0.0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_53(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p50_ms=round(p50[0]["value"] * 1000.0, ) if p50 else 0.0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_54(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p50_ms=round(p50[0]["value"] / 1000.0, 2) if p50 else 0.0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_55(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p50_ms=round(p50[1]["value"] * 1000.0, 2) if p50 else 0.0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_56(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p50_ms=round(p50[0]["XXvalueXX"] * 1000.0, 2) if p50 else 0.0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_57(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p50_ms=round(p50[0]["VALUE"] * 1000.0, 2) if p50 else 0.0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_58(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p50_ms=round(p50[0]["value"] * 1001.0, 2) if p50 else 0.0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_59(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p50_ms=round(p50[0]["value"] * 1000.0, 3) if p50 else 0.0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_60(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p50_ms=round(p50[0]["value"] * 1000.0, 2) if p50 else 1.0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_61(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p95_ms=1.0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_62(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p99_ms=round(None, 2) if p99 else 0.0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_63(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p99_ms=round(p99[0]["value"] * 1000.0, None) if p99 else 0.0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_64(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p99_ms=round(2) if p99 else 0.0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_65(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p99_ms=round(p99[0]["value"] * 1000.0, ) if p99 else 0.0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_66(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p99_ms=round(p99[0]["value"] / 1000.0, 2) if p99 else 0.0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_67(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p99_ms=round(p99[1]["value"] * 1000.0, 2) if p99 else 0.0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_68(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p99_ms=round(p99[0]["XXvalueXX"] * 1000.0, 2) if p99 else 0.0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_69(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p99_ms=round(p99[0]["VALUE"] * 1000.0, 2) if p99 else 0.0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_70(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p99_ms=round(p99[0]["value"] * 1001.0, 2) if p99 else 0.0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_71(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p99_ms=round(p99[0]["value"] * 1000.0, 3) if p99 else 0.0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_72(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 1.0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_73(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                error_rate_pct=1.0,
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

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_74(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                version=None,
                p50_ms=0.0,
                p95_ms=0.0,
                p99_ms=0.0,
                error_rate_pct=0.0,
                request_count=0,
            )

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_75(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p50_ms=None,
                p95_ms=0.0,
                p99_ms=0.0,
                error_rate_pct=0.0,
                request_count=0,
            )

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_76(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p95_ms=None,
                p99_ms=0.0,
                error_rate_pct=0.0,
                request_count=0,
            )

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_77(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p99_ms=None,
                error_rate_pct=0.0,
                request_count=0,
            )

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_78(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                error_rate_pct=None,
                request_count=0,
            )

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_79(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                request_count=None,
            )

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_80(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p50_ms=0.0,
                p95_ms=0.0,
                p99_ms=0.0,
                error_rate_pct=0.0,
                request_count=0,
            )

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_81(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p95_ms=0.0,
                p99_ms=0.0,
                error_rate_pct=0.0,
                request_count=0,
            )

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_82(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p99_ms=0.0,
                error_rate_pct=0.0,
                request_count=0,
            )

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_83(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                error_rate_pct=0.0,
                request_count=0,
            )

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_84(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                request_count=0,
            )

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_85(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                )

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_86(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                version="XXunknownXX",
                p50_ms=0.0,
                p95_ms=0.0,
                p99_ms=0.0,
                error_rate_pct=0.0,
                request_count=0,
            )

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_87(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                version="UNKNOWN",
                p50_ms=0.0,
                p95_ms=0.0,
                p99_ms=0.0,
                error_rate_pct=0.0,
                request_count=0,
            )

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_88(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p50_ms=1.0,
                p95_ms=0.0,
                p99_ms=0.0,
                error_rate_pct=0.0,
                request_count=0,
            )

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_89(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p95_ms=1.0,
                p99_ms=0.0,
                error_rate_pct=0.0,
                request_count=0,
            )

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_90(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                p99_ms=1.0,
                error_rate_pct=0.0,
                request_count=0,
            )

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_91(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                error_rate_pct=1.0,
                request_count=0,
            )

    def xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_92(self, request: VersionComparisonRequest) -> VersionMetrics:
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
                request_count=1,
            )

mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['_mutmut_orig'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_1'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_2'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_3'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_4'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_5'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_6'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_7'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_8'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_9'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_10'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_10 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_11'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_11 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_12'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_12 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_13'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_13 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_14'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_14 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_15'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_15 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_16'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_16 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_17'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_17 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_18'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_18 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_19'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_19 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_20'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_20 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_21'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_21 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_22'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_22 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_23'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_23 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_24'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_24 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_25'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_25 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_26'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_26 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_27'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_27 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_28'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_28 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_29'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_29 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_30'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_30 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_31'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_31 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_32'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_32 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_33'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_33 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_34'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_34 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_35'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_35 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_36'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_36 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_37'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_37 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_38'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_38 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_39'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_39 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_40'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_40 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_41'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_41 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_42'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_42 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_43'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_43 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_44'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_44 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_45'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_45 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_46'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_46 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_47'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_47 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_48'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_48 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_49'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_49 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_50'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_50 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_51'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_51 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_52'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_52 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_53'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_53 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_54'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_54 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_55'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_55 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_56'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_56 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_57'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_57 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_58'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_58 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_59'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_59 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_60'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_60 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_61'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_61 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_62'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_62 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_63'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_63 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_64'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_64 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_65'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_65 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_66'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_66 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_67'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_67 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_68'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_68 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_69'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_69 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_70'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_70 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_71'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_71 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_72'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_72 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_73'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_73 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_74'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_74 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_75'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_75 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_76'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_76 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_77'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_77 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_78'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_78 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_79'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_79 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_80'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_80 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_81'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_81 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_82'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_82 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_83'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_83 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_84'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_84 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_85'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_85 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_86'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_86 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_87'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_87 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_88'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_88 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_89'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_89 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_90'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_90 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_91'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_91 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_92'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_baseline_metrics__mutmut_92 # type: ignore # mutmut generated

mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['_mutmut_orig'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_1'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_2'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_3'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_4'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_5'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_6'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_7'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_8'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_9'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_10'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_10 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_11'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_11 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_12'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_12 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_13'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_13 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_14'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_14 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_15'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_15 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_16'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_16 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_17'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_17 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_18'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_18 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_19'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_19 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_20'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_20 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_21'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_21 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_22'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_22 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_23'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_23 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_24'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_24 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_25'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_25 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_26'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_26 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_27'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_27 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_28'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_28 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_29'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_29 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_30'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_30 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_31'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_31 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_32'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_32 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_33'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_33 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_34'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_34 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_35'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_35 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_36'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_36 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_37'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_37 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_38'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_38 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_39'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_39 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_40'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_40 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_41'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_41 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_42'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_42 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_43'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_43 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_44'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_44 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_45'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_45 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_46'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_46 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_47'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_47 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_48'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_48 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_49'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_49 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_50'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_50 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_51'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_51 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_52'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_52 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_53'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_53 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_54'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_54 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_55'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_55 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_56'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_56 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_57'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_57 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_58'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_58 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_59'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_59 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_60'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_60 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_61'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_61 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_62'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_62 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_63'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_63 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_64'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_64 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_65'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_65 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_66'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_66 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_67'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_67 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_68'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_68 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_69'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_69 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_70'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_70 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_71'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_71 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_72'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_72 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_73'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_73 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_74'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_74 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_75'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_75 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_76'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_76 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_77'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_77 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_78'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_78 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_79'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_79 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_80'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_80 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_81'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_81 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_82'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_82 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_83'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_83 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_84'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_84 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_85'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_85 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_86'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_86 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_87'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_87 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_88'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_88 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_89'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_89 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_90'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_90 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_91'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_91 # type: ignore # mutmut generated
mutants_xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut['xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_92'] = OTelVersionRegressionAdapter.xǁOTelVersionRegressionAdapterǁfetch_current_metrics__mutmut_92 # type: ignore # mutmut generated
