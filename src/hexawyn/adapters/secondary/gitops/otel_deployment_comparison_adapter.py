from __future__ import annotations

from hexawyn.adapters.secondary.gitops.otel_http_client import query_prometheus_instant
from hexawyn.application.ports.driven.deployment_latency_comparison_port import (
    DeploymentLatencyComparisonPort,
)
from hexawyn.domain.models.deployment_latency import (
    DeploymentComparisonRequest,
    WindowLatency,
)


class OTelDeploymentComparisonAdapter(DeploymentLatencyComparisonPort):
    def fetch_pre_deploy_latency(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        try:
            p50_q = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m]))'  # noqa: E501
            p95_q = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m]))'  # noqa: E501
            p99_q = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m]))'  # noqa: E501
            count_q = f'rate(http_request_duration_seconds_count{{service="{request.service_name}"}}[30m])'  # noqa: E501

            p50 = query_prometheus_instant(p50_q)
            p95 = query_prometheus_instant(p95_q)
            p99 = query_prometheus_instant(p99_q)
            count = query_prometheus_instant(count_q)

            return WindowLatency(
                p50_ms=round(p50[0]["value"] * 1000.0, 2) if p50 else 0.0,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def fetch_post_deploy_latency(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        try:
            p50_q = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m] offset 30m))'  # noqa: E501
            p95_q = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m] offset 30m))'  # noqa: E501
            p99_q = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m] offset 30m))'  # noqa: E501
            count_q = f'rate(http_request_duration_seconds_count{{service="{request.service_name}"}}[30m])'  # noqa: E501

            p50 = query_prometheus_instant(p50_q)
            p95 = query_prometheus_instant(p95_q)
            p99 = query_prometheus_instant(p99_q)
            count = query_prometheus_instant(count_q)

            return WindowLatency(
                p50_ms=round(p50[0]["value"] * 1000.0, 2) if p50 else 0.0,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
