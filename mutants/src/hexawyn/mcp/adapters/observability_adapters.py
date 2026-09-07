from __future__ import annotations

import os

from hexawyn.application.ports.driven.cross_namespace_traffic_port import (
    CrossNamespaceTrafficPort,
)
from hexawyn.application.ports.driven.deployment_latency_comparison_port import (
    DeploymentLatencyComparisonPort,
)
from hexawyn.application.ports.driven.error_attribution_port import ErrorAttributionPort
from hexawyn.application.ports.driven.error_budget_port import ErrorBudgetPort
from hexawyn.application.ports.driven.latency_percentile_port import LatencyPercentilePort
from hexawyn.application.ports.driven.log_search_port import LogSearchPort
from hexawyn.application.ports.driven.metric_correlation_port import MetricCorrelationPort
from hexawyn.application.ports.driven.metrics_query_port import MetricsQueryPort
from hexawyn.application.ports.driven.namespace_events_port import NamespaceEventsPort
from hexawyn.application.ports.driven.namespace_overview_port import NamespaceOverviewPort
from hexawyn.application.ports.driven.pod_log_watch_port import PodLogWatchPort
from hexawyn.application.ports.driven.pod_logs_port import PodLogsPort
from hexawyn.application.ports.driven.pod_metrics_baseline_port import (
    PodMetricsBaselinePort,
)
from hexawyn.application.ports.driven.redundant_call_detection_port import (
    RedundantCallDetectionPort,
)
from hexawyn.application.ports.driven.service_dependency_graph_port import (
    ServiceDependencyGraphPort,
)
from hexawyn.application.ports.driven.slo_breach_prediction_port import (
    SLOBreachPredictionPort,
)
from hexawyn.application.ports.driven.slow_trace_search_port import SlowTraceSearchPort
from hexawyn.application.ports.driven.span_bottleneck_port import SpanBottleneckPort
from hexawyn.application.ports.driven.trace_event_correlation_port import (
    TraceEventCorrelationPort,
)
from hexawyn.application.ports.driven.trace_log_correlation_port import (
    TraceLogCorrelationPort,
)
from hexawyn.application.ports.driven.trace_query_port import TraceQueryPort
from hexawyn.mcp.adapters.cluster_adapters import build_k8s_adapter
from hexawyn.mcp.providers.detector import (
    _current_cluster_context,
    _is_aws_eks_context,
    _is_azure_aks_context,
    _is_datadog_enabled,
    _is_gcp_gke_context,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


def build_span_bottleneck_adapter() -> SpanBottleneckPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.otel_span_breakdown_adapter import (
        OTelSpanBreakdownAdapter,
    )

    return OTelSpanBreakdownAdapter()


def build_latency_percentile_adapter() -> LatencyPercentilePort:
    from hexawyn.infrastructure.adapters.secondary.gitops.otel_latency_adapter import (
        OTelPrometheusLatencyAdapter,
    )

    return OTelPrometheusLatencyAdapter()


def build_metric_correlation_adapter() -> MetricCorrelationPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.otel_correlation_adapter import (
        OTelPrometheusCorrelationAdapter,
    )

    return OTelPrometheusCorrelationAdapter()
mutants_x_build_metrics_query_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_metrics_query_adapter__mutmut)
def build_metrics_query_adapter() -> MetricsQueryPort:
    context = _current_cluster_context()
    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.infrastructure.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=os.environ.get("AZURE_MONITOR_PROMETHEUS_URL", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return PrometheusHTTPAdapter(
        endpoint=prometheus_url, token=os.environ.get("PROMETHEUS_TOKEN") or None
    )


def x_build_metrics_query_adapter__mutmut_orig() -> MetricsQueryPort:
    context = _current_cluster_context()
    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.infrastructure.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=os.environ.get("AZURE_MONITOR_PROMETHEUS_URL", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return PrometheusHTTPAdapter(
        endpoint=prometheus_url, token=os.environ.get("PROMETHEUS_TOKEN") or None
    )


def x_build_metrics_query_adapter__mutmut_1() -> MetricsQueryPort:
    context = None
    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.infrastructure.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=os.environ.get("AZURE_MONITOR_PROMETHEUS_URL", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return PrometheusHTTPAdapter(
        endpoint=prometheus_url, token=os.environ.get("PROMETHEUS_TOKEN") or None
    )


def x_build_metrics_query_adapter__mutmut_2() -> MetricsQueryPort:
    context = _current_cluster_context()
    if _is_gcp_gke_context(None):
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.infrastructure.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=os.environ.get("AZURE_MONITOR_PROMETHEUS_URL", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return PrometheusHTTPAdapter(
        endpoint=prometheus_url, token=os.environ.get("PROMETHEUS_TOKEN") or None
    )


def x_build_metrics_query_adapter__mutmut_3() -> MetricsQueryPort:
    context = _current_cluster_context()
    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.infrastructure.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=None)

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=os.environ.get("AZURE_MONITOR_PROMETHEUS_URL", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return PrometheusHTTPAdapter(
        endpoint=prometheus_url, token=os.environ.get("PROMETHEUS_TOKEN") or None
    )


def x_build_metrics_query_adapter__mutmut_4() -> MetricsQueryPort:
    context = _current_cluster_context()
    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.infrastructure.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=GCPGKEAdapter(context).project_id and "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=os.environ.get("AZURE_MONITOR_PROMETHEUS_URL", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return PrometheusHTTPAdapter(
        endpoint=prometheus_url, token=os.environ.get("PROMETHEUS_TOKEN") or None
    )


def x_build_metrics_query_adapter__mutmut_5() -> MetricsQueryPort:
    context = _current_cluster_context()
    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.infrastructure.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=GCPGKEAdapter(None).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=os.environ.get("AZURE_MONITOR_PROMETHEUS_URL", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return PrometheusHTTPAdapter(
        endpoint=prometheus_url, token=os.environ.get("PROMETHEUS_TOKEN") or None
    )


def x_build_metrics_query_adapter__mutmut_6() -> MetricsQueryPort:
    context = _current_cluster_context()
    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.infrastructure.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=GCPGKEAdapter(context).project_id or "XXXX")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=os.environ.get("AZURE_MONITOR_PROMETHEUS_URL", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return PrometheusHTTPAdapter(
        endpoint=prometheus_url, token=os.environ.get("PROMETHEUS_TOKEN") or None
    )


def x_build_metrics_query_adapter__mutmut_7() -> MetricsQueryPort:
    context = _current_cluster_context()
    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.infrastructure.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(None):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=os.environ.get("AZURE_MONITOR_PROMETHEUS_URL", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return PrometheusHTTPAdapter(
        endpoint=prometheus_url, token=os.environ.get("PROMETHEUS_TOKEN") or None
    )


def x_build_metrics_query_adapter__mutmut_8() -> MetricsQueryPort:
    context = _current_cluster_context()
    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.infrastructure.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=None
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return PrometheusHTTPAdapter(
        endpoint=prometheus_url, token=os.environ.get("PROMETHEUS_TOKEN") or None
    )


def x_build_metrics_query_adapter__mutmut_9() -> MetricsQueryPort:
    context = _current_cluster_context()
    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.infrastructure.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=os.environ.get(None, "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return PrometheusHTTPAdapter(
        endpoint=prometheus_url, token=os.environ.get("PROMETHEUS_TOKEN") or None
    )


def x_build_metrics_query_adapter__mutmut_10() -> MetricsQueryPort:
    context = _current_cluster_context()
    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.infrastructure.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=os.environ.get("AZURE_MONITOR_PROMETHEUS_URL", None)
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return PrometheusHTTPAdapter(
        endpoint=prometheus_url, token=os.environ.get("PROMETHEUS_TOKEN") or None
    )


def x_build_metrics_query_adapter__mutmut_11() -> MetricsQueryPort:
    context = _current_cluster_context()
    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.infrastructure.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=os.environ.get("")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return PrometheusHTTPAdapter(
        endpoint=prometheus_url, token=os.environ.get("PROMETHEUS_TOKEN") or None
    )


def x_build_metrics_query_adapter__mutmut_12() -> MetricsQueryPort:
    context = _current_cluster_context()
    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.infrastructure.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=os.environ.get("AZURE_MONITOR_PROMETHEUS_URL", )
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return PrometheusHTTPAdapter(
        endpoint=prometheus_url, token=os.environ.get("PROMETHEUS_TOKEN") or None
    )


def x_build_metrics_query_adapter__mutmut_13() -> MetricsQueryPort:
    context = _current_cluster_context()
    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.infrastructure.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=os.environ.get("XXAZURE_MONITOR_PROMETHEUS_URLXX", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return PrometheusHTTPAdapter(
        endpoint=prometheus_url, token=os.environ.get("PROMETHEUS_TOKEN") or None
    )


def x_build_metrics_query_adapter__mutmut_14() -> MetricsQueryPort:
    context = _current_cluster_context()
    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.infrastructure.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=os.environ.get("azure_monitor_prometheus_url", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return PrometheusHTTPAdapter(
        endpoint=prometheus_url, token=os.environ.get("PROMETHEUS_TOKEN") or None
    )


def x_build_metrics_query_adapter__mutmut_15() -> MetricsQueryPort:
    context = _current_cluster_context()
    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.infrastructure.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=os.environ.get("AZURE_MONITOR_PROMETHEUS_URL", "XXXX")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return PrometheusHTTPAdapter(
        endpoint=prometheus_url, token=os.environ.get("PROMETHEUS_TOKEN") or None
    )


def x_build_metrics_query_adapter__mutmut_16() -> MetricsQueryPort:
    context = _current_cluster_context()
    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.infrastructure.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=os.environ.get("AZURE_MONITOR_PROMETHEUS_URL", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = None
    return PrometheusHTTPAdapter(
        endpoint=prometheus_url, token=os.environ.get("PROMETHEUS_TOKEN") or None
    )


def x_build_metrics_query_adapter__mutmut_17() -> MetricsQueryPort:
    context = _current_cluster_context()
    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.infrastructure.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=os.environ.get("AZURE_MONITOR_PROMETHEUS_URL", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get(None, "")
    return PrometheusHTTPAdapter(
        endpoint=prometheus_url, token=os.environ.get("PROMETHEUS_TOKEN") or None
    )


def x_build_metrics_query_adapter__mutmut_18() -> MetricsQueryPort:
    context = _current_cluster_context()
    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.infrastructure.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=os.environ.get("AZURE_MONITOR_PROMETHEUS_URL", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get("PROMETHEUS_URL", None)
    return PrometheusHTTPAdapter(
        endpoint=prometheus_url, token=os.environ.get("PROMETHEUS_TOKEN") or None
    )


def x_build_metrics_query_adapter__mutmut_19() -> MetricsQueryPort:
    context = _current_cluster_context()
    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.infrastructure.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=os.environ.get("AZURE_MONITOR_PROMETHEUS_URL", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get("")
    return PrometheusHTTPAdapter(
        endpoint=prometheus_url, token=os.environ.get("PROMETHEUS_TOKEN") or None
    )


def x_build_metrics_query_adapter__mutmut_20() -> MetricsQueryPort:
    context = _current_cluster_context()
    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.infrastructure.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=os.environ.get("AZURE_MONITOR_PROMETHEUS_URL", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get("PROMETHEUS_URL", )
    return PrometheusHTTPAdapter(
        endpoint=prometheus_url, token=os.environ.get("PROMETHEUS_TOKEN") or None
    )


def x_build_metrics_query_adapter__mutmut_21() -> MetricsQueryPort:
    context = _current_cluster_context()
    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.infrastructure.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=os.environ.get("AZURE_MONITOR_PROMETHEUS_URL", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get("XXPROMETHEUS_URLXX", "")
    return PrometheusHTTPAdapter(
        endpoint=prometheus_url, token=os.environ.get("PROMETHEUS_TOKEN") or None
    )


def x_build_metrics_query_adapter__mutmut_22() -> MetricsQueryPort:
    context = _current_cluster_context()
    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.infrastructure.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=os.environ.get("AZURE_MONITOR_PROMETHEUS_URL", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get("prometheus_url", "")
    return PrometheusHTTPAdapter(
        endpoint=prometheus_url, token=os.environ.get("PROMETHEUS_TOKEN") or None
    )


def x_build_metrics_query_adapter__mutmut_23() -> MetricsQueryPort:
    context = _current_cluster_context()
    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.infrastructure.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=os.environ.get("AZURE_MONITOR_PROMETHEUS_URL", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get("PROMETHEUS_URL", "XXXX")
    return PrometheusHTTPAdapter(
        endpoint=prometheus_url, token=os.environ.get("PROMETHEUS_TOKEN") or None
    )


def x_build_metrics_query_adapter__mutmut_24() -> MetricsQueryPort:
    context = _current_cluster_context()
    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.infrastructure.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=os.environ.get("AZURE_MONITOR_PROMETHEUS_URL", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return PrometheusHTTPAdapter(
        endpoint=None, token=os.environ.get("PROMETHEUS_TOKEN") or None
    )


def x_build_metrics_query_adapter__mutmut_25() -> MetricsQueryPort:
    context = _current_cluster_context()
    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.infrastructure.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=os.environ.get("AZURE_MONITOR_PROMETHEUS_URL", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return PrometheusHTTPAdapter(
        endpoint=prometheus_url, token=None
    )


def x_build_metrics_query_adapter__mutmut_26() -> MetricsQueryPort:
    context = _current_cluster_context()
    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.infrastructure.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=os.environ.get("AZURE_MONITOR_PROMETHEUS_URL", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return PrometheusHTTPAdapter(
        token=os.environ.get("PROMETHEUS_TOKEN") or None
    )


def x_build_metrics_query_adapter__mutmut_27() -> MetricsQueryPort:
    context = _current_cluster_context()
    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.infrastructure.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=os.environ.get("AZURE_MONITOR_PROMETHEUS_URL", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return PrometheusHTTPAdapter(
        endpoint=prometheus_url, )


def x_build_metrics_query_adapter__mutmut_28() -> MetricsQueryPort:
    context = _current_cluster_context()
    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.infrastructure.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=os.environ.get("AZURE_MONITOR_PROMETHEUS_URL", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return PrometheusHTTPAdapter(
        endpoint=prometheus_url, token=os.environ.get("PROMETHEUS_TOKEN") and None
    )


def x_build_metrics_query_adapter__mutmut_29() -> MetricsQueryPort:
    context = _current_cluster_context()
    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.infrastructure.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=os.environ.get("AZURE_MONITOR_PROMETHEUS_URL", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return PrometheusHTTPAdapter(
        endpoint=prometheus_url, token=os.environ.get(None) or None
    )


def x_build_metrics_query_adapter__mutmut_30() -> MetricsQueryPort:
    context = _current_cluster_context()
    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.infrastructure.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=os.environ.get("AZURE_MONITOR_PROMETHEUS_URL", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return PrometheusHTTPAdapter(
        endpoint=prometheus_url, token=os.environ.get("XXPROMETHEUS_TOKENXX") or None
    )


def x_build_metrics_query_adapter__mutmut_31() -> MetricsQueryPort:
    context = _current_cluster_context()
    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.infrastructure.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=os.environ.get("AZURE_MONITOR_PROMETHEUS_URL", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return PrometheusHTTPAdapter(
        endpoint=prometheus_url, token=os.environ.get("prometheus_token") or None
    )

mutants_x_build_metrics_query_adapter__mutmut['_mutmut_orig'] = x_build_metrics_query_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_metrics_query_adapter__mutmut['x_build_metrics_query_adapter__mutmut_1'] = x_build_metrics_query_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_metrics_query_adapter__mutmut['x_build_metrics_query_adapter__mutmut_2'] = x_build_metrics_query_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_metrics_query_adapter__mutmut['x_build_metrics_query_adapter__mutmut_3'] = x_build_metrics_query_adapter__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_metrics_query_adapter__mutmut['x_build_metrics_query_adapter__mutmut_4'] = x_build_metrics_query_adapter__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_metrics_query_adapter__mutmut['x_build_metrics_query_adapter__mutmut_5'] = x_build_metrics_query_adapter__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_metrics_query_adapter__mutmut['x_build_metrics_query_adapter__mutmut_6'] = x_build_metrics_query_adapter__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_metrics_query_adapter__mutmut['x_build_metrics_query_adapter__mutmut_7'] = x_build_metrics_query_adapter__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_metrics_query_adapter__mutmut['x_build_metrics_query_adapter__mutmut_8'] = x_build_metrics_query_adapter__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_metrics_query_adapter__mutmut['x_build_metrics_query_adapter__mutmut_9'] = x_build_metrics_query_adapter__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_metrics_query_adapter__mutmut['x_build_metrics_query_adapter__mutmut_10'] = x_build_metrics_query_adapter__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_metrics_query_adapter__mutmut['x_build_metrics_query_adapter__mutmut_11'] = x_build_metrics_query_adapter__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_metrics_query_adapter__mutmut['x_build_metrics_query_adapter__mutmut_12'] = x_build_metrics_query_adapter__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_metrics_query_adapter__mutmut['x_build_metrics_query_adapter__mutmut_13'] = x_build_metrics_query_adapter__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_metrics_query_adapter__mutmut['x_build_metrics_query_adapter__mutmut_14'] = x_build_metrics_query_adapter__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_metrics_query_adapter__mutmut['x_build_metrics_query_adapter__mutmut_15'] = x_build_metrics_query_adapter__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_metrics_query_adapter__mutmut['x_build_metrics_query_adapter__mutmut_16'] = x_build_metrics_query_adapter__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_metrics_query_adapter__mutmut['x_build_metrics_query_adapter__mutmut_17'] = x_build_metrics_query_adapter__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_metrics_query_adapter__mutmut['x_build_metrics_query_adapter__mutmut_18'] = x_build_metrics_query_adapter__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_metrics_query_adapter__mutmut['x_build_metrics_query_adapter__mutmut_19'] = x_build_metrics_query_adapter__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_metrics_query_adapter__mutmut['x_build_metrics_query_adapter__mutmut_20'] = x_build_metrics_query_adapter__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_metrics_query_adapter__mutmut['x_build_metrics_query_adapter__mutmut_21'] = x_build_metrics_query_adapter__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_metrics_query_adapter__mutmut['x_build_metrics_query_adapter__mutmut_22'] = x_build_metrics_query_adapter__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_metrics_query_adapter__mutmut['x_build_metrics_query_adapter__mutmut_23'] = x_build_metrics_query_adapter__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_metrics_query_adapter__mutmut['x_build_metrics_query_adapter__mutmut_24'] = x_build_metrics_query_adapter__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_metrics_query_adapter__mutmut['x_build_metrics_query_adapter__mutmut_25'] = x_build_metrics_query_adapter__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_metrics_query_adapter__mutmut['x_build_metrics_query_adapter__mutmut_26'] = x_build_metrics_query_adapter__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_metrics_query_adapter__mutmut['x_build_metrics_query_adapter__mutmut_27'] = x_build_metrics_query_adapter__mutmut_27 # type: ignore # mutmut generated
mutants_x_build_metrics_query_adapter__mutmut['x_build_metrics_query_adapter__mutmut_28'] = x_build_metrics_query_adapter__mutmut_28 # type: ignore # mutmut generated
mutants_x_build_metrics_query_adapter__mutmut['x_build_metrics_query_adapter__mutmut_29'] = x_build_metrics_query_adapter__mutmut_29 # type: ignore # mutmut generated
mutants_x_build_metrics_query_adapter__mutmut['x_build_metrics_query_adapter__mutmut_30'] = x_build_metrics_query_adapter__mutmut_30 # type: ignore # mutmut generated
mutants_x_build_metrics_query_adapter__mutmut['x_build_metrics_query_adapter__mutmut_31'] = x_build_metrics_query_adapter__mutmut_31 # type: ignore # mutmut generated


def build_cross_namespace_traffic_adapter() -> CrossNamespaceTrafficPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.otel_cross_namespace_traffic_adapter import (  # noqa: E501
        OTelCrossNamespaceTrafficAdapter,
    )

    return OTelCrossNamespaceTrafficAdapter()


def build_trace_log_correlation_adapter() -> TraceLogCorrelationPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.otel_trace_log_adapter import (
        OTelTraceLogAdapter,
    )

    return OTelTraceLogAdapter()


def build_service_dependency_graph_adapter() -> ServiceDependencyGraphPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.otel_dependency_graph_adapter import (
        OTelDependencyGraphAdapter,
    )

    return OTelDependencyGraphAdapter()


def build_trace_event_correlation_adapter() -> TraceEventCorrelationPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_event_adapter import (
        KubernetesEventAdapter,
    )

    return KubernetesEventAdapter()
mutants_x_build_trace_query_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_trace_query_adapter__mutmut)
def build_trace_query_adapter() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def x_build_trace_query_adapter__mutmut_orig() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def x_build_trace_query_adapter__mutmut_1() -> TraceQueryPort:
    context = None
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def x_build_trace_query_adapter__mutmut_2() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(None):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def x_build_trace_query_adapter__mutmut_3() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = None
        return DatadogTracesAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def x_build_trace_query_adapter__mutmut_4() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            key=None, app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def x_build_trace_query_adapter__mutmut_5() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            key=config["key"], app_key=None, site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def x_build_trace_query_adapter__mutmut_6() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            key=config["key"], app_key=config["app_key"], site=None
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def x_build_trace_query_adapter__mutmut_7() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def x_build_trace_query_adapter__mutmut_8() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            key=config["key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def x_build_trace_query_adapter__mutmut_9() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            key=config["key"], app_key=config["app_key"], )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def x_build_trace_query_adapter__mutmut_10() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            key=config["XXkeyXX"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def x_build_trace_query_adapter__mutmut_11() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            key=config["KEY"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def x_build_trace_query_adapter__mutmut_12() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            key=config["key"], app_key=config["XXapp_keyXX"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def x_build_trace_query_adapter__mutmut_13() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            key=config["key"], app_key=config["APP_KEY"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def x_build_trace_query_adapter__mutmut_14() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            key=config["key"], app_key=config["app_key"], site=config["XXsiteXX"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def x_build_trace_query_adapter__mutmut_15() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            key=config["key"], app_key=config["app_key"], site=config["SITE"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def x_build_trace_query_adapter__mutmut_16() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(None):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def x_build_trace_query_adapter__mutmut_17() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=None)

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def x_build_trace_query_adapter__mutmut_18() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(None).region)

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def x_build_trace_query_adapter__mutmut_19() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

    if _is_gcp_gke_context(None):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def x_build_trace_query_adapter__mutmut_20() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=None)

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def x_build_trace_query_adapter__mutmut_21() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(context).project_id and "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def x_build_trace_query_adapter__mutmut_22() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(None).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def x_build_trace_query_adapter__mutmut_23() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(context).project_id or "XXXX")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def x_build_trace_query_adapter__mutmut_24() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(None):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def x_build_trace_query_adapter__mutmut_25() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=None
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def x_build_trace_query_adapter__mutmut_26() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get(None, "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def x_build_trace_query_adapter__mutmut_27() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", None)
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def x_build_trace_query_adapter__mutmut_28() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get("")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def x_build_trace_query_adapter__mutmut_29() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", )
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def x_build_trace_query_adapter__mutmut_30() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get("XXAZURE_LOG_ANALYTICS_WORKSPACE_IDXX", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def x_build_trace_query_adapter__mutmut_31() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get("azure_log_analytics_workspace_id", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def x_build_trace_query_adapter__mutmut_32() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.infrastructure.adapters.secondary.aws.xray_trace_adapter import (
            AWSXRayTraceAdapter,
        )

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "XXXX")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()

mutants_x_build_trace_query_adapter__mutmut['_mutmut_orig'] = x_build_trace_query_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_trace_query_adapter__mutmut['x_build_trace_query_adapter__mutmut_1'] = x_build_trace_query_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_trace_query_adapter__mutmut['x_build_trace_query_adapter__mutmut_2'] = x_build_trace_query_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_trace_query_adapter__mutmut['x_build_trace_query_adapter__mutmut_3'] = x_build_trace_query_adapter__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_trace_query_adapter__mutmut['x_build_trace_query_adapter__mutmut_4'] = x_build_trace_query_adapter__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_trace_query_adapter__mutmut['x_build_trace_query_adapter__mutmut_5'] = x_build_trace_query_adapter__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_trace_query_adapter__mutmut['x_build_trace_query_adapter__mutmut_6'] = x_build_trace_query_adapter__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_trace_query_adapter__mutmut['x_build_trace_query_adapter__mutmut_7'] = x_build_trace_query_adapter__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_trace_query_adapter__mutmut['x_build_trace_query_adapter__mutmut_8'] = x_build_trace_query_adapter__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_trace_query_adapter__mutmut['x_build_trace_query_adapter__mutmut_9'] = x_build_trace_query_adapter__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_trace_query_adapter__mutmut['x_build_trace_query_adapter__mutmut_10'] = x_build_trace_query_adapter__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_trace_query_adapter__mutmut['x_build_trace_query_adapter__mutmut_11'] = x_build_trace_query_adapter__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_trace_query_adapter__mutmut['x_build_trace_query_adapter__mutmut_12'] = x_build_trace_query_adapter__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_trace_query_adapter__mutmut['x_build_trace_query_adapter__mutmut_13'] = x_build_trace_query_adapter__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_trace_query_adapter__mutmut['x_build_trace_query_adapter__mutmut_14'] = x_build_trace_query_adapter__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_trace_query_adapter__mutmut['x_build_trace_query_adapter__mutmut_15'] = x_build_trace_query_adapter__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_trace_query_adapter__mutmut['x_build_trace_query_adapter__mutmut_16'] = x_build_trace_query_adapter__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_trace_query_adapter__mutmut['x_build_trace_query_adapter__mutmut_17'] = x_build_trace_query_adapter__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_trace_query_adapter__mutmut['x_build_trace_query_adapter__mutmut_18'] = x_build_trace_query_adapter__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_trace_query_adapter__mutmut['x_build_trace_query_adapter__mutmut_19'] = x_build_trace_query_adapter__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_trace_query_adapter__mutmut['x_build_trace_query_adapter__mutmut_20'] = x_build_trace_query_adapter__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_trace_query_adapter__mutmut['x_build_trace_query_adapter__mutmut_21'] = x_build_trace_query_adapter__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_trace_query_adapter__mutmut['x_build_trace_query_adapter__mutmut_22'] = x_build_trace_query_adapter__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_trace_query_adapter__mutmut['x_build_trace_query_adapter__mutmut_23'] = x_build_trace_query_adapter__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_trace_query_adapter__mutmut['x_build_trace_query_adapter__mutmut_24'] = x_build_trace_query_adapter__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_trace_query_adapter__mutmut['x_build_trace_query_adapter__mutmut_25'] = x_build_trace_query_adapter__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_trace_query_adapter__mutmut['x_build_trace_query_adapter__mutmut_26'] = x_build_trace_query_adapter__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_trace_query_adapter__mutmut['x_build_trace_query_adapter__mutmut_27'] = x_build_trace_query_adapter__mutmut_27 # type: ignore # mutmut generated
mutants_x_build_trace_query_adapter__mutmut['x_build_trace_query_adapter__mutmut_28'] = x_build_trace_query_adapter__mutmut_28 # type: ignore # mutmut generated
mutants_x_build_trace_query_adapter__mutmut['x_build_trace_query_adapter__mutmut_29'] = x_build_trace_query_adapter__mutmut_29 # type: ignore # mutmut generated
mutants_x_build_trace_query_adapter__mutmut['x_build_trace_query_adapter__mutmut_30'] = x_build_trace_query_adapter__mutmut_30 # type: ignore # mutmut generated
mutants_x_build_trace_query_adapter__mutmut['x_build_trace_query_adapter__mutmut_31'] = x_build_trace_query_adapter__mutmut_31 # type: ignore # mutmut generated
mutants_x_build_trace_query_adapter__mutmut['x_build_trace_query_adapter__mutmut_32'] = x_build_trace_query_adapter__mutmut_32 # type: ignore # mutmut generated


def build_slow_trace_search_adapter() -> SlowTraceSearchPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.otel_pod_trace_adapter import (
        OTelPodTraceAdapter,
    )

    return OTelPodTraceAdapter()


def build_deployment_latency_comparison_adapter() -> DeploymentLatencyComparisonPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.otel_deployment_comparison_adapter import (  # noqa: E501
        OTelDeploymentComparisonAdapter,
    )

    return OTelDeploymentComparisonAdapter()


def build_redundant_call_detection_adapter() -> RedundantCallDetectionPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.otel_redundant_call_adapter import (
        OTelRedundantCallAdapter,
    )

    return OTelRedundantCallAdapter()


def build_error_attribution_adapter() -> ErrorAttributionPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.otel_error_attribution_adapter import (
        OTelErrorAttributionAdapter,
    )

    return OTelErrorAttributionAdapter()


def build_slo_breach_prediction_adapter() -> SLOBreachPredictionPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.otel_slo_prediction_adapter import (
        OTelSLOPredictionAdapter,
    )

    return OTelSLOPredictionAdapter()


def build_pod_logs_adapter() -> PodLogsPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_logs_adapter import (
        KubernetesPodLogsAdapter,
    )

    return KubernetesPodLogsAdapter()
mutants_x_build_log_search_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_log_search_adapter__mutmut)
def build_log_search_adapter() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_orig() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_1() -> LogSearchPort:
    context = None
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_2() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(None):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_3() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = None
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_4() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=None, app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_5() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=None, site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_6() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=None)

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_7() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_8() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_9() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], )

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_10() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["XXkeyXX"], app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_11() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["KEY"], app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_12() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["XXapp_keyXX"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_13() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["APP_KEY"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_14() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=config["XXsiteXX"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_15() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=config["SITE"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_16() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(None):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_17() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=None,
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_18() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=None,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_19() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_20() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_21() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] and context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_22() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["XXclusterXX"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_23() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["CLUSTER"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_24() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["XXnameXX"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_25() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["NAME"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_26() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(None).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_27() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(None):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_28() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=None)

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_29() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id and "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_30() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(None).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_31() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "XXXX")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_32() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(None):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_33() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=None
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_34() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get(None, "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_35() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", None)
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_36() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_37() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", )
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_38() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("XXAZURE_LOG_ANALYTICS_WORKSPACE_IDXX", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_39() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("azure_log_analytics_workspace_id", "")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def x_build_log_search_adapter__mutmut_40() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.infrastructure.adapters.secondary.datadog.datadog_logs_adapter import (
            DatadogLogsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.infrastructure.adapters.secondary.aws.cloudwatch_logs_adapter import (
            CloudWatchLogsAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.infrastructure.adapters.secondary.gcp.cloud_logging_adapter import (
            GCPCloudLoggingAdapter,
        )
        from hexawyn.infrastructure.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.infrastructure.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "XXXX")
        )

    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()

mutants_x_build_log_search_adapter__mutmut['_mutmut_orig'] = x_build_log_search_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_1'] = x_build_log_search_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_2'] = x_build_log_search_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_3'] = x_build_log_search_adapter__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_4'] = x_build_log_search_adapter__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_5'] = x_build_log_search_adapter__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_6'] = x_build_log_search_adapter__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_7'] = x_build_log_search_adapter__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_8'] = x_build_log_search_adapter__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_9'] = x_build_log_search_adapter__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_10'] = x_build_log_search_adapter__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_11'] = x_build_log_search_adapter__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_12'] = x_build_log_search_adapter__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_13'] = x_build_log_search_adapter__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_14'] = x_build_log_search_adapter__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_15'] = x_build_log_search_adapter__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_16'] = x_build_log_search_adapter__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_17'] = x_build_log_search_adapter__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_18'] = x_build_log_search_adapter__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_19'] = x_build_log_search_adapter__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_20'] = x_build_log_search_adapter__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_21'] = x_build_log_search_adapter__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_22'] = x_build_log_search_adapter__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_23'] = x_build_log_search_adapter__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_24'] = x_build_log_search_adapter__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_25'] = x_build_log_search_adapter__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_26'] = x_build_log_search_adapter__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_27'] = x_build_log_search_adapter__mutmut_27 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_28'] = x_build_log_search_adapter__mutmut_28 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_29'] = x_build_log_search_adapter__mutmut_29 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_30'] = x_build_log_search_adapter__mutmut_30 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_31'] = x_build_log_search_adapter__mutmut_31 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_32'] = x_build_log_search_adapter__mutmut_32 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_33'] = x_build_log_search_adapter__mutmut_33 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_34'] = x_build_log_search_adapter__mutmut_34 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_35'] = x_build_log_search_adapter__mutmut_35 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_36'] = x_build_log_search_adapter__mutmut_36 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_37'] = x_build_log_search_adapter__mutmut_37 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_38'] = x_build_log_search_adapter__mutmut_38 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_39'] = x_build_log_search_adapter__mutmut_39 # type: ignore # mutmut generated
mutants_x_build_log_search_adapter__mutmut['x_build_log_search_adapter__mutmut_40'] = x_build_log_search_adapter__mutmut_40 # type: ignore # mutmut generated
mutants_x_build_pod_metrics_baseline_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_pod_metrics_baseline_adapter__mutmut)
def build_pod_metrics_baseline_adapter() -> PodMetricsBaselinePort:
    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_pod_metrics_baseline_adapter import (  # noqa: E501
        PrometheusPodMetricsBaselineAdapter,
    )

    return PrometheusPodMetricsBaselineAdapter(
        metrics_query_port=build_metrics_query_adapter(), k8s_port=build_k8s_adapter()
    )


def x_build_pod_metrics_baseline_adapter__mutmut_orig() -> PodMetricsBaselinePort:
    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_pod_metrics_baseline_adapter import (  # noqa: E501
        PrometheusPodMetricsBaselineAdapter,
    )

    return PrometheusPodMetricsBaselineAdapter(
        metrics_query_port=build_metrics_query_adapter(), k8s_port=build_k8s_adapter()
    )


def x_build_pod_metrics_baseline_adapter__mutmut_1() -> PodMetricsBaselinePort:
    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_pod_metrics_baseline_adapter import (  # noqa: E501
        PrometheusPodMetricsBaselineAdapter,
    )

    return PrometheusPodMetricsBaselineAdapter(
        metrics_query_port=None, k8s_port=build_k8s_adapter()
    )


def x_build_pod_metrics_baseline_adapter__mutmut_2() -> PodMetricsBaselinePort:
    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_pod_metrics_baseline_adapter import (  # noqa: E501
        PrometheusPodMetricsBaselineAdapter,
    )

    return PrometheusPodMetricsBaselineAdapter(
        metrics_query_port=build_metrics_query_adapter(), k8s_port=None
    )


def x_build_pod_metrics_baseline_adapter__mutmut_3() -> PodMetricsBaselinePort:
    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_pod_metrics_baseline_adapter import (  # noqa: E501
        PrometheusPodMetricsBaselineAdapter,
    )

    return PrometheusPodMetricsBaselineAdapter(
        k8s_port=build_k8s_adapter()
    )


def x_build_pod_metrics_baseline_adapter__mutmut_4() -> PodMetricsBaselinePort:
    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_pod_metrics_baseline_adapter import (  # noqa: E501
        PrometheusPodMetricsBaselineAdapter,
    )

    return PrometheusPodMetricsBaselineAdapter(
        metrics_query_port=build_metrics_query_adapter(), )

mutants_x_build_pod_metrics_baseline_adapter__mutmut['_mutmut_orig'] = x_build_pod_metrics_baseline_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_pod_metrics_baseline_adapter__mutmut['x_build_pod_metrics_baseline_adapter__mutmut_1'] = x_build_pod_metrics_baseline_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_pod_metrics_baseline_adapter__mutmut['x_build_pod_metrics_baseline_adapter__mutmut_2'] = x_build_pod_metrics_baseline_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_pod_metrics_baseline_adapter__mutmut['x_build_pod_metrics_baseline_adapter__mutmut_3'] = x_build_pod_metrics_baseline_adapter__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_pod_metrics_baseline_adapter__mutmut['x_build_pod_metrics_baseline_adapter__mutmut_4'] = x_build_pod_metrics_baseline_adapter__mutmut_4 # type: ignore # mutmut generated


def build_namespace_events_adapter() -> NamespaceEventsPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_namespace_events_adapter import (  # noqa: E501
        KubernetesNamespaceEventsAdapter,
    )

    return KubernetesNamespaceEventsAdapter()


def build_namespace_overview_adapter() -> NamespaceOverviewPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_namespace_adapter import (
        KubernetesNamespaceAdapter,
    )

    return KubernetesNamespaceAdapter()


def build_pod_log_watch_adapter() -> PodLogWatchPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.kubernetes_pod_log_watch_adapter import (
        KubernetesPodLogWatchAdapter,
    )

    return KubernetesPodLogWatchAdapter()
mutants_x_build_error_budget_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_error_budget_adapter__mutmut)
def build_error_budget_adapter() -> ErrorBudgetPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_error_budget_adapter import (
        PrometheusErrorBudgetAdapter,
    )

    return PrometheusErrorBudgetAdapter(metrics_query_port=build_metrics_query_adapter())


def x_build_error_budget_adapter__mutmut_orig() -> ErrorBudgetPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_error_budget_adapter import (
        PrometheusErrorBudgetAdapter,
    )

    return PrometheusErrorBudgetAdapter(metrics_query_port=build_metrics_query_adapter())


def x_build_error_budget_adapter__mutmut_1() -> ErrorBudgetPort:
    from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_error_budget_adapter import (
        PrometheusErrorBudgetAdapter,
    )

    return PrometheusErrorBudgetAdapter(metrics_query_port=None)

mutants_x_build_error_budget_adapter__mutmut['_mutmut_orig'] = x_build_error_budget_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_error_budget_adapter__mutmut['x_build_error_budget_adapter__mutmut_1'] = x_build_error_budget_adapter__mutmut_1 # type: ignore # mutmut generated
