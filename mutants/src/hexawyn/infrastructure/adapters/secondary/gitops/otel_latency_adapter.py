from __future__ import annotations

from hexawyn.application.ports.driven.latency_percentile_port import LatencyPercentilePort
from hexawyn.domain.models.p99_latency import LatencyPercentileRequest, LatencyPercentiles
from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_client import (
    query_prometheus_instant,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut: MutantDict = {}  # type: ignore


class OTelPrometheusLatencyAdapter(LatencyPercentilePort):
    @_mutmut_mutated(mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut)
    def fetch_percentiles(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_orig(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_1(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_2(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=None, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_3(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=None, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_4(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=None, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_5(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=None)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_6(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_7(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_8(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_9(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, )

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_10(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=1.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_11(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=1.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_12(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=1.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_13(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=1)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_14(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = None
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_15(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(None, "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_16(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", None)
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_17(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace("_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_18(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", )
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_19(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace(None, "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_20(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", None).replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_21(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_22(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", ).replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_23(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("XX/XX", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_24(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "XX_XX").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_25(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace("XX.XX", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_26(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "XX_XX")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_27(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = None  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_28(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = None  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_29(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = None  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_30(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = None

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_31(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = None
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_32(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(None)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_33(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = None
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_34(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(None)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_35(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = None
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_36(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(None)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_37(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = None

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_38(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(None)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_39(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = None
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_40(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] / 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_41(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[1]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_42(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["XXvalueXX"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_43(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["VALUE"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_44(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1001.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_45(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 1.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_46(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = None
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_47(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] / 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_48(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[1]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_49(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["XXvalueXX"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_50(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["VALUE"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_51(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1001.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_52(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 1.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_53(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = None
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_54(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] / 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_55(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[1]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_56(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["XXvalueXX"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_57(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["VALUE"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_58(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1001.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_59(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 1.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_60(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = None

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_61(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(None) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_62(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[1]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_63(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["XXvalueXX"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_64(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["VALUE"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_65(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 1

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_66(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=None,
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_67(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=None,
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_68(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=None,
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_69(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=None,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_70(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_71(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_72(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_73(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_74(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(None, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_75(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, None),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_76(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_77(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, ),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_78(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 3),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_79(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(None, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_80(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, None),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_81(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_82(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, ),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_83(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 3),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_84(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(None, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_85(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, None),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_86(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_87(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, ),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_88(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 3),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_89(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=None, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_90(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=None, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_91(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=None, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_92(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=None)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_93(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_94(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_95(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_96(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, )
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_97(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=1.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_98(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=1.0, p99_ms=0.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_99(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=1.0, sample_count=0)
    def xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_100(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        if not request.endpoint:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        endpoint_label = request.endpoint.replace("/", "_").replace(".", "_")
        p50_query = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p95_query = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        p99_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{endpoint="{endpoint_label}"}}[5m]))'  # noqa: E501
        count_query = (
            f'rate(http_request_duration_seconds_count{{endpoint="{endpoint_label}"}}[5m])'  # noqa: E501
        )

        try:
            p50_metrics = query_prometheus_instant(p50_query)
            p95_metrics = query_prometheus_instant(p95_query)
            p99_metrics = query_prometheus_instant(p99_query)
            count_metrics = query_prometheus_instant(count_query)

            p50_ms = (p50_metrics[0]["value"] * 1000.0) if p50_metrics else 0.0
            p95_ms = (p95_metrics[0]["value"] * 1000.0) if p95_metrics else 0.0
            p99_ms = (p99_metrics[0]["value"] * 1000.0) if p99_metrics else 0.0
            sample_count = int(count_metrics[0]["value"]) if count_metrics else 0

            return LatencyPercentiles(
                p50_ms=round(p50_ms, 2),
                p95_ms=round(p95_ms, 2),
                p99_ms=round(p99_ms, 2),
                sample_count=sample_count,
            )
        except Exception:
            return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=1)

mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['_mutmut_orig'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_1'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_2'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_3'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_4'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_5'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_6'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_7'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_8'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_9'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_10'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_10 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_11'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_11 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_12'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_12 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_13'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_13 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_14'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_14 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_15'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_15 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_16'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_16 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_17'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_17 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_18'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_18 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_19'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_19 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_20'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_20 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_21'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_21 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_22'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_22 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_23'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_23 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_24'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_24 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_25'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_25 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_26'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_26 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_27'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_27 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_28'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_28 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_29'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_29 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_30'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_30 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_31'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_31 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_32'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_32 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_33'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_33 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_34'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_34 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_35'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_35 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_36'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_36 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_37'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_37 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_38'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_38 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_39'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_39 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_40'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_40 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_41'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_41 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_42'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_42 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_43'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_43 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_44'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_44 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_45'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_45 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_46'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_46 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_47'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_47 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_48'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_48 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_49'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_49 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_50'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_50 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_51'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_51 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_52'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_52 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_53'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_53 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_54'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_54 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_55'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_55 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_56'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_56 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_57'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_57 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_58'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_58 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_59'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_59 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_60'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_60 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_61'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_61 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_62'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_62 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_63'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_63 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_64'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_64 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_65'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_65 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_66'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_66 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_67'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_67 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_68'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_68 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_69'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_69 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_70'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_70 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_71'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_71 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_72'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_72 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_73'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_73 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_74'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_74 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_75'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_75 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_76'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_76 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_77'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_77 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_78'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_78 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_79'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_79 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_80'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_80 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_81'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_81 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_82'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_82 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_83'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_83 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_84'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_84 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_85'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_85 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_86'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_86 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_87'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_87 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_88'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_88 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_89'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_89 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_90'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_90 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_91'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_91 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_92'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_92 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_93'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_93 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_94'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_94 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_95'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_95 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_96'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_96 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_97'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_97 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_98'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_98 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_99'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_99 # type: ignore # mutmut generated
mutants_xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut['xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_100'] = OTelPrometheusLatencyAdapter.xǁOTelPrometheusLatencyAdapterǁfetch_percentiles__mutmut_100 # type: ignore # mutmut generated
