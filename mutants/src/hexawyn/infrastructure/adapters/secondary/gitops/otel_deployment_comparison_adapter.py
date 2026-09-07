from __future__ import annotations

from hexawyn.application.ports.driven.deployment_latency_comparison_port import (
    DeploymentLatencyComparisonPort,
)
from hexawyn.domain.models.deployment_latency import (
    DeploymentComparisonRequest,
    WindowLatency,
)
from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_client import (
    query_prometheus_instant,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut: MutantDict = {}  # type: ignore
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut: MutantDict = {}  # type: ignore


class OTelDeploymentComparisonAdapter(DeploymentLatencyComparisonPort):
    @_mutmut_mutated(mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut)
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
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_orig(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_1(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if request.service_name:
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
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_2(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=None, p95_ms=0.0, p99_ms=0.0, sample_count=0)

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
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_3(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=None, p99_ms=0.0, sample_count=0)

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
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_4(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=None, sample_count=0)

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
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_5(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=None)

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
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_6(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p95_ms=0.0, p99_ms=0.0, sample_count=0)

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
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_7(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p99_ms=0.0, sample_count=0)

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
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_8(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, sample_count=0)

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
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_9(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, )

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
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_10(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=1.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

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
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_11(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=1.0, p99_ms=0.0, sample_count=0)

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
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_12(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=1.0, sample_count=0)

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
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_13(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=1)

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
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_14(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        try:
            p50_q = None  # noqa: E501
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
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_15(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        try:
            p50_q = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m]))'  # noqa: E501
            p95_q = None  # noqa: E501
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
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_16(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        try:
            p50_q = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m]))'  # noqa: E501
            p95_q = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m]))'  # noqa: E501
            p99_q = None  # noqa: E501
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
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_17(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        try:
            p50_q = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m]))'  # noqa: E501
            p95_q = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m]))'  # noqa: E501
            p99_q = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m]))'  # noqa: E501
            count_q = None  # noqa: E501

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
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_18(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        try:
            p50_q = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m]))'  # noqa: E501
            p95_q = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m]))'  # noqa: E501
            p99_q = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m]))'  # noqa: E501
            count_q = f'rate(http_request_duration_seconds_count{{service="{request.service_name}"}}[30m])'  # noqa: E501

            p50 = None
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
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_19(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        try:
            p50_q = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m]))'  # noqa: E501
            p95_q = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m]))'  # noqa: E501
            p99_q = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m]))'  # noqa: E501
            count_q = f'rate(http_request_duration_seconds_count{{service="{request.service_name}"}}[30m])'  # noqa: E501

            p50 = query_prometheus_instant(None)
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
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_20(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        try:
            p50_q = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m]))'  # noqa: E501
            p95_q = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m]))'  # noqa: E501
            p99_q = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m]))'  # noqa: E501
            count_q = f'rate(http_request_duration_seconds_count{{service="{request.service_name}"}}[30m])'  # noqa: E501

            p50 = query_prometheus_instant(p50_q)
            p95 = None
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
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_21(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        try:
            p50_q = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m]))'  # noqa: E501
            p95_q = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m]))'  # noqa: E501
            p99_q = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m]))'  # noqa: E501
            count_q = f'rate(http_request_duration_seconds_count{{service="{request.service_name}"}}[30m])'  # noqa: E501

            p50 = query_prometheus_instant(p50_q)
            p95 = query_prometheus_instant(None)
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
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_22(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        try:
            p50_q = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m]))'  # noqa: E501
            p95_q = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m]))'  # noqa: E501
            p99_q = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m]))'  # noqa: E501
            count_q = f'rate(http_request_duration_seconds_count{{service="{request.service_name}"}}[30m])'  # noqa: E501

            p50 = query_prometheus_instant(p50_q)
            p95 = query_prometheus_instant(p95_q)
            p99 = None
            count = query_prometheus_instant(count_q)

            return WindowLatency(
                p50_ms=round(p50[0]["value"] * 1000.0, 2) if p50 else 0.0,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_23(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        try:
            p50_q = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m]))'  # noqa: E501
            p95_q = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m]))'  # noqa: E501
            p99_q = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m]))'  # noqa: E501
            count_q = f'rate(http_request_duration_seconds_count{{service="{request.service_name}"}}[30m])'  # noqa: E501

            p50 = query_prometheus_instant(p50_q)
            p95 = query_prometheus_instant(p95_q)
            p99 = query_prometheus_instant(None)
            count = query_prometheus_instant(count_q)

            return WindowLatency(
                p50_ms=round(p50[0]["value"] * 1000.0, 2) if p50 else 0.0,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_24(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
            count = None

            return WindowLatency(
                p50_ms=round(p50[0]["value"] * 1000.0, 2) if p50 else 0.0,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_25(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
            count = query_prometheus_instant(None)

            return WindowLatency(
                p50_ms=round(p50[0]["value"] * 1000.0, 2) if p50 else 0.0,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_26(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p50_ms=None,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_27(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p95_ms=None,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_28(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p99_ms=None,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_29(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                sample_count=None,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_30(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_31(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_32(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_33(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_34(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p50_ms=round(None, 2) if p50 else 0.0,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_35(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p50_ms=round(p50[0]["value"] * 1000.0, None) if p50 else 0.0,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_36(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p50_ms=round(2) if p50 else 0.0,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_37(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p50_ms=round(p50[0]["value"] * 1000.0, ) if p50 else 0.0,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_38(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p50_ms=round(p50[0]["value"] / 1000.0, 2) if p50 else 0.0,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_39(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p50_ms=round(p50[1]["value"] * 1000.0, 2) if p50 else 0.0,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_40(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p50_ms=round(p50[0]["XXvalueXX"] * 1000.0, 2) if p50 else 0.0,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_41(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p50_ms=round(p50[0]["VALUE"] * 1000.0, 2) if p50 else 0.0,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_42(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p50_ms=round(p50[0]["value"] * 1001.0, 2) if p50 else 0.0,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_43(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p50_ms=round(p50[0]["value"] * 1000.0, 3) if p50 else 0.0,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_44(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p50_ms=round(p50[0]["value"] * 1000.0, 2) if p50 else 1.0,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_45(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p95_ms=round(None, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_46(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p95_ms=round(p95[0]["value"] * 1000.0, None) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_47(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p95_ms=round(2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_48(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p95_ms=round(p95[0]["value"] * 1000.0, ) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_49(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p95_ms=round(p95[0]["value"] / 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_50(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p95_ms=round(p95[1]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_51(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p95_ms=round(p95[0]["XXvalueXX"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_52(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p95_ms=round(p95[0]["VALUE"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_53(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p95_ms=round(p95[0]["value"] * 1001.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_54(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p95_ms=round(p95[0]["value"] * 1000.0, 3) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_55(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 1.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_56(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p99_ms=round(None, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_57(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p99_ms=round(p99[0]["value"] * 1000.0, None) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_58(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p99_ms=round(2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_59(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p99_ms=round(p99[0]["value"] * 1000.0, ) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_60(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p99_ms=round(p99[0]["value"] / 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_61(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p99_ms=round(p99[1]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_62(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p99_ms=round(p99[0]["XXvalueXX"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_63(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p99_ms=round(p99[0]["VALUE"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_64(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p99_ms=round(p99[0]["value"] * 1001.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_65(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p99_ms=round(p99[0]["value"] * 1000.0, 3) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_66(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 1.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_67(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                sample_count=int(None) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_68(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                sample_count=int(count[1]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_69(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                sample_count=int(count[0]["XXvalueXX"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_70(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                sample_count=int(count[0]["VALUE"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_71(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                sample_count=int(count[0]["value"]) if count else 1,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_72(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
            return WindowLatency(p50_ms=None, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_73(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
            return WindowLatency(p50_ms=0.0, p95_ms=None, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_74(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=None, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_75(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=None)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_76(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
            return WindowLatency(p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_77(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
            return WindowLatency(p50_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_78(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_79(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, )
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_80(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
            return WindowLatency(p50_ms=1.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_81(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
            return WindowLatency(p50_ms=0.0, p95_ms=1.0, p99_ms=0.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_82(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=1.0, sample_count=0)
    def xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_83(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=1)

    @_mutmut_mutated(mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut)
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

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_orig(self, request: DeploymentComparisonRequest) -> WindowLatency:
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

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_1(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if request.service_name:
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

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_2(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=None, p95_ms=0.0, p99_ms=0.0, sample_count=0)

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

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_3(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=None, p99_ms=0.0, sample_count=0)

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

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_4(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=None, sample_count=0)

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

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_5(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=None)

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

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_6(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p95_ms=0.0, p99_ms=0.0, sample_count=0)

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

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_7(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p99_ms=0.0, sample_count=0)

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

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_8(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, sample_count=0)

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

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_9(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, )

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

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_10(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=1.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

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

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_11(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=1.0, p99_ms=0.0, sample_count=0)

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

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_12(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=1.0, sample_count=0)

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

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_13(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=1)

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

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_14(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        try:
            p50_q = None  # noqa: E501
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

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_15(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        try:
            p50_q = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m] offset 30m))'  # noqa: E501
            p95_q = None  # noqa: E501
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

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_16(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        try:
            p50_q = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m] offset 30m))'  # noqa: E501
            p95_q = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m] offset 30m))'  # noqa: E501
            p99_q = None  # noqa: E501
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

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_17(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        try:
            p50_q = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m] offset 30m))'  # noqa: E501
            p95_q = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m] offset 30m))'  # noqa: E501
            p99_q = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m] offset 30m))'  # noqa: E501
            count_q = None  # noqa: E501

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

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_18(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        try:
            p50_q = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m] offset 30m))'  # noqa: E501
            p95_q = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m] offset 30m))'  # noqa: E501
            p99_q = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m] offset 30m))'  # noqa: E501
            count_q = f'rate(http_request_duration_seconds_count{{service="{request.service_name}"}}[30m])'  # noqa: E501

            p50 = None
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

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_19(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        try:
            p50_q = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m] offset 30m))'  # noqa: E501
            p95_q = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m] offset 30m))'  # noqa: E501
            p99_q = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m] offset 30m))'  # noqa: E501
            count_q = f'rate(http_request_duration_seconds_count{{service="{request.service_name}"}}[30m])'  # noqa: E501

            p50 = query_prometheus_instant(None)
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

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_20(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        try:
            p50_q = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m] offset 30m))'  # noqa: E501
            p95_q = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m] offset 30m))'  # noqa: E501
            p99_q = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m] offset 30m))'  # noqa: E501
            count_q = f'rate(http_request_duration_seconds_count{{service="{request.service_name}"}}[30m])'  # noqa: E501

            p50 = query_prometheus_instant(p50_q)
            p95 = None
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

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_21(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        try:
            p50_q = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m] offset 30m))'  # noqa: E501
            p95_q = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m] offset 30m))'  # noqa: E501
            p99_q = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m] offset 30m))'  # noqa: E501
            count_q = f'rate(http_request_duration_seconds_count{{service="{request.service_name}"}}[30m])'  # noqa: E501

            p50 = query_prometheus_instant(p50_q)
            p95 = query_prometheus_instant(None)
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

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_22(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        try:
            p50_q = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m] offset 30m))'  # noqa: E501
            p95_q = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m] offset 30m))'  # noqa: E501
            p99_q = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m] offset 30m))'  # noqa: E501
            count_q = f'rate(http_request_duration_seconds_count{{service="{request.service_name}"}}[30m])'  # noqa: E501

            p50 = query_prometheus_instant(p50_q)
            p95 = query_prometheus_instant(p95_q)
            p99 = None
            count = query_prometheus_instant(count_q)

            return WindowLatency(
                p50_ms=round(p50[0]["value"] * 1000.0, 2) if p50 else 0.0,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_23(self, request: DeploymentComparisonRequest) -> WindowLatency:
        if not request.service_name:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

        try:
            p50_q = f'histogram_quantile(0.50, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m] offset 30m))'  # noqa: E501
            p95_q = f'histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m] offset 30m))'  # noqa: E501
            p99_q = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{service="{request.service_name}"}}[30m] offset 30m))'  # noqa: E501
            count_q = f'rate(http_request_duration_seconds_count{{service="{request.service_name}"}}[30m])'  # noqa: E501

            p50 = query_prometheus_instant(p50_q)
            p95 = query_prometheus_instant(p95_q)
            p99 = query_prometheus_instant(None)
            count = query_prometheus_instant(count_q)

            return WindowLatency(
                p50_ms=round(p50[0]["value"] * 1000.0, 2) if p50 else 0.0,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_24(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
            count = None

            return WindowLatency(
                p50_ms=round(p50[0]["value"] * 1000.0, 2) if p50 else 0.0,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_25(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
            count = query_prometheus_instant(None)

            return WindowLatency(
                p50_ms=round(p50[0]["value"] * 1000.0, 2) if p50 else 0.0,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_26(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p50_ms=None,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_27(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p95_ms=None,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_28(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p99_ms=None,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_29(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                sample_count=None,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_30(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_31(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_32(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_33(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_34(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p50_ms=round(None, 2) if p50 else 0.0,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_35(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p50_ms=round(p50[0]["value"] * 1000.0, None) if p50 else 0.0,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_36(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p50_ms=round(2) if p50 else 0.0,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_37(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p50_ms=round(p50[0]["value"] * 1000.0, ) if p50 else 0.0,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_38(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p50_ms=round(p50[0]["value"] / 1000.0, 2) if p50 else 0.0,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_39(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p50_ms=round(p50[1]["value"] * 1000.0, 2) if p50 else 0.0,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_40(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p50_ms=round(p50[0]["XXvalueXX"] * 1000.0, 2) if p50 else 0.0,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_41(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p50_ms=round(p50[0]["VALUE"] * 1000.0, 2) if p50 else 0.0,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_42(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p50_ms=round(p50[0]["value"] * 1001.0, 2) if p50 else 0.0,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_43(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p50_ms=round(p50[0]["value"] * 1000.0, 3) if p50 else 0.0,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_44(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p50_ms=round(p50[0]["value"] * 1000.0, 2) if p50 else 1.0,
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_45(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p95_ms=round(None, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_46(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p95_ms=round(p95[0]["value"] * 1000.0, None) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_47(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p95_ms=round(2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_48(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p95_ms=round(p95[0]["value"] * 1000.0, ) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_49(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p95_ms=round(p95[0]["value"] / 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_50(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p95_ms=round(p95[1]["value"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_51(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p95_ms=round(p95[0]["XXvalueXX"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_52(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p95_ms=round(p95[0]["VALUE"] * 1000.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_53(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p95_ms=round(p95[0]["value"] * 1001.0, 2) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_54(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p95_ms=round(p95[0]["value"] * 1000.0, 3) if p95 else 0.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_55(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p95_ms=round(p95[0]["value"] * 1000.0, 2) if p95 else 1.0,
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_56(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p99_ms=round(None, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_57(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p99_ms=round(p99[0]["value"] * 1000.0, None) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_58(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p99_ms=round(2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_59(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p99_ms=round(p99[0]["value"] * 1000.0, ) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_60(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p99_ms=round(p99[0]["value"] / 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_61(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p99_ms=round(p99[1]["value"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_62(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p99_ms=round(p99[0]["XXvalueXX"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_63(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p99_ms=round(p99[0]["VALUE"] * 1000.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_64(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p99_ms=round(p99[0]["value"] * 1001.0, 2) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_65(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p99_ms=round(p99[0]["value"] * 1000.0, 3) if p99 else 0.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_66(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                p99_ms=round(p99[0]["value"] * 1000.0, 2) if p99 else 1.0,
                sample_count=int(count[0]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_67(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                sample_count=int(None) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_68(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                sample_count=int(count[1]["value"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_69(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                sample_count=int(count[0]["XXvalueXX"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_70(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                sample_count=int(count[0]["VALUE"]) if count else 0,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_71(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
                sample_count=int(count[0]["value"]) if count else 1,
            )
        except Exception:
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_72(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
            return WindowLatency(p50_ms=None, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_73(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
            return WindowLatency(p50_ms=0.0, p95_ms=None, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_74(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=None, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_75(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=None)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_76(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
            return WindowLatency(p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_77(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
            return WindowLatency(p50_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_78(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_79(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, )

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_80(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
            return WindowLatency(p50_ms=1.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_81(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
            return WindowLatency(p50_ms=0.0, p95_ms=1.0, p99_ms=0.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_82(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=1.0, sample_count=0)

    def xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_83(self, request: DeploymentComparisonRequest) -> WindowLatency:
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
            return WindowLatency(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=1)

mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['_mutmut_orig'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_1'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_2'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_3'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_4'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_5'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_6'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_7'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_8'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_9'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_10'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_10 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_11'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_11 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_12'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_12 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_13'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_13 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_14'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_14 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_15'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_15 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_16'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_16 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_17'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_17 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_18'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_18 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_19'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_19 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_20'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_20 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_21'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_21 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_22'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_22 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_23'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_23 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_24'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_24 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_25'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_25 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_26'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_26 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_27'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_27 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_28'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_28 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_29'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_29 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_30'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_30 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_31'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_31 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_32'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_32 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_33'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_33 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_34'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_34 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_35'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_35 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_36'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_36 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_37'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_37 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_38'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_38 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_39'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_39 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_40'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_40 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_41'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_41 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_42'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_42 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_43'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_43 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_44'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_44 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_45'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_45 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_46'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_46 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_47'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_47 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_48'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_48 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_49'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_49 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_50'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_50 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_51'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_51 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_52'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_52 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_53'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_53 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_54'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_54 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_55'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_55 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_56'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_56 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_57'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_57 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_58'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_58 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_59'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_59 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_60'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_60 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_61'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_61 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_62'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_62 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_63'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_63 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_64'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_64 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_65'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_65 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_66'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_66 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_67'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_67 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_68'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_68 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_69'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_69 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_70'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_70 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_71'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_71 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_72'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_72 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_73'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_73 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_74'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_74 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_75'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_75 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_76'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_76 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_77'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_77 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_78'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_78 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_79'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_79 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_80'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_80 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_81'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_81 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_82'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_82 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_83'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_pre_deploy_latency__mutmut_83 # type: ignore # mutmut generated

mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['_mutmut_orig'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_1'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_2'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_3'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_4'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_5'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_6'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_7'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_8'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_9'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_10'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_10 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_11'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_11 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_12'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_12 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_13'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_13 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_14'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_14 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_15'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_15 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_16'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_16 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_17'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_17 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_18'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_18 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_19'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_19 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_20'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_20 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_21'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_21 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_22'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_22 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_23'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_23 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_24'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_24 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_25'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_25 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_26'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_26 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_27'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_27 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_28'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_28 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_29'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_29 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_30'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_30 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_31'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_31 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_32'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_32 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_33'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_33 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_34'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_34 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_35'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_35 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_36'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_36 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_37'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_37 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_38'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_38 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_39'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_39 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_40'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_40 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_41'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_41 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_42'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_42 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_43'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_43 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_44'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_44 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_45'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_45 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_46'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_46 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_47'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_47 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_48'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_48 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_49'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_49 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_50'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_50 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_51'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_51 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_52'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_52 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_53'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_53 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_54'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_54 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_55'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_55 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_56'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_56 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_57'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_57 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_58'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_58 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_59'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_59 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_60'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_60 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_61'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_61 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_62'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_62 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_63'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_63 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_64'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_64 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_65'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_65 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_66'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_66 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_67'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_67 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_68'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_68 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_69'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_69 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_70'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_70 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_71'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_71 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_72'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_72 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_73'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_73 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_74'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_74 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_75'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_75 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_76'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_76 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_77'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_77 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_78'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_78 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_79'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_79 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_80'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_80 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_81'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_81 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_82'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_82 # type: ignore # mutmut generated
mutants_xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut['xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_83'] = OTelDeploymentComparisonAdapter.xǁOTelDeploymentComparisonAdapterǁfetch_post_deploy_latency__mutmut_83 # type: ignore # mutmut generated
