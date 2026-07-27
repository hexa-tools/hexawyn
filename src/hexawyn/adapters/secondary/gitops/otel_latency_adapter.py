from __future__ import annotations

from hexawyn.adapters.secondary.gitops.otel_http_client import query_prometheus_instant
from hexawyn.application.ports.driven.latency_percentile_port import LatencyPercentilePort
from hexawyn.domain.models.p99_latency import LatencyPercentileRequest, LatencyPercentiles


class OTelPrometheusLatencyAdapter(LatencyPercentilePort):
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
