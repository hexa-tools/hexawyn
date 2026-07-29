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


def build_span_bottleneck_adapter() -> SpanBottleneckPort:
    from hexawyn.adapters.secondary.gitops.otel_span_breakdown_adapter import (
        OTelSpanBreakdownAdapter,
    )

    return OTelSpanBreakdownAdapter()


def build_latency_percentile_adapter() -> LatencyPercentilePort:
    from hexawyn.adapters.secondary.gitops.otel_latency_adapter import (
        OTelPrometheusLatencyAdapter,
    )

    return OTelPrometheusLatencyAdapter()


def build_metric_correlation_adapter() -> MetricCorrelationPort:
    from hexawyn.adapters.secondary.gitops.otel_correlation_adapter import (
        OTelPrometheusCorrelationAdapter,
    )

    return OTelPrometheusCorrelationAdapter()


def build_metrics_query_adapter() -> MetricsQueryPort:
    context = _current_cluster_context()
    if _is_gcp_gke_context(context):
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter
        from hexawyn.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )

        return GCPManagedPrometheusAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        return AzureMonitorMetricsAdapter(
            endpoint=os.environ.get("AZURE_MONITOR_PROMETHEUS_URL", "")
        )

    from hexawyn.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return PrometheusHTTPAdapter(
        endpoint=prometheus_url, token=os.environ.get("PROMETHEUS_TOKEN") or None
    )


def build_cross_namespace_traffic_adapter() -> CrossNamespaceTrafficPort:
    from hexawyn.adapters.secondary.gitops.otel_cross_namespace_traffic_adapter import (
        OTelCrossNamespaceTrafficAdapter,
    )

    return OTelCrossNamespaceTrafficAdapter()


def build_trace_log_correlation_adapter() -> TraceLogCorrelationPort:
    from hexawyn.adapters.secondary.gitops.otel_trace_log_adapter import (
        OTelTraceLogAdapter,
    )

    return OTelTraceLogAdapter()


def build_service_dependency_graph_adapter() -> ServiceDependencyGraphPort:
    from hexawyn.adapters.secondary.gitops.otel_dependency_graph_adapter import (
        OTelDependencyGraphAdapter,
    )

    return OTelDependencyGraphAdapter()


def build_trace_event_correlation_adapter() -> TraceEventCorrelationPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_event_adapter import (
        KubernetesEventAdapter,
    )

    return KubernetesEventAdapter()


def build_trace_query_adapter() -> TraceQueryPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogTracesAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

    if _is_aws_eks_context(context):
        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.adapters.secondary.aws.xray_trace_adapter import AWSXRayTraceAdapter

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

    if _is_gcp_gke_context(context):
        from hexawyn.adapters.secondary.gcp.cloud_trace_adapter import GCPCloudTraceAdapter
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudTraceAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        return AzureMonitorTracesAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter

    return OTelHTTPAdapter()


def build_slow_trace_search_adapter() -> SlowTraceSearchPort:
    from hexawyn.adapters.secondary.gitops.otel_pod_trace_adapter import (
        OTelPodTraceAdapter,
    )

    return OTelPodTraceAdapter()


def build_deployment_latency_comparison_adapter() -> DeploymentLatencyComparisonPort:
    from hexawyn.adapters.secondary.gitops.otel_deployment_comparison_adapter import (
        OTelDeploymentComparisonAdapter,
    )

    return OTelDeploymentComparisonAdapter()


def build_redundant_call_detection_adapter() -> RedundantCallDetectionPort:
    from hexawyn.adapters.secondary.gitops.otel_redundant_call_adapter import (
        OTelRedundantCallAdapter,
    )

    return OTelRedundantCallAdapter()


def build_error_attribution_adapter() -> ErrorAttributionPort:
    from hexawyn.adapters.secondary.gitops.otel_error_attribution_adapter import (
        OTelErrorAttributionAdapter,
    )

    return OTelErrorAttributionAdapter()


def build_slo_breach_prediction_adapter() -> SLOBreachPredictionPort:
    from hexawyn.adapters.secondary.gitops.otel_slo_prediction_adapter import (
        OTelSLOPredictionAdapter,
    )

    return OTelSLOPredictionAdapter()


def build_pod_logs_adapter() -> PodLogsPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_pod_logs_adapter import (
        KubernetesPodLogsAdapter,
    )

    return KubernetesPodLogsAdapter()


def build_log_search_adapter() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.adapters.secondary.datadog.datadog_logs_adapter import DatadogLogsAdapter
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogLogsAdapter(key=config["key"], app_key=config["app_key"], site=config["site"])

    if _is_aws_eks_context(context):
        from hexawyn.adapters.secondary.aws.cloudwatch_logs_adapter import CloudWatchLogsAdapter
        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
        )

    if _is_gcp_gke_context(context):
        from hexawyn.adapters.secondary.gcp.cloud_logging_adapter import GCPCloudLoggingAdapter
        from hexawyn.adapters.secondary.gcp.gke_adapter import GCPGKEAdapter

        return GCPCloudLoggingAdapter(project_id=GCPGKEAdapter(context).project_id or "")

    if _is_azure_aks_context(context):
        from hexawyn.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        return AzureLogAnalyticsAdapter(
            workspace_id=os.environ.get("AZURE_LOG_ANALYTICS_WORKSPACE_ID", "")
        )

    from hexawyn.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
        KubernetesPodLogSearchAdapter,
    )

    return KubernetesPodLogSearchAdapter()


def build_pod_metrics_baseline_adapter() -> PodMetricsBaselinePort:
    from hexawyn.adapters.secondary.gitops.prometheus_pod_metrics_baseline_adapter import (
        PrometheusPodMetricsBaselineAdapter,
    )

    return PrometheusPodMetricsBaselineAdapter(
        metrics_query_port=build_metrics_query_adapter(), k8s_port=build_k8s_adapter()
    )


def build_namespace_events_adapter() -> NamespaceEventsPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_namespace_events_adapter import (
        KubernetesNamespaceEventsAdapter,
    )

    return KubernetesNamespaceEventsAdapter()


def build_namespace_overview_adapter() -> NamespaceOverviewPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_namespace_adapter import (
        KubernetesNamespaceAdapter,
    )

    return KubernetesNamespaceAdapter()


def build_pod_log_watch_adapter() -> PodLogWatchPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_pod_log_watch_adapter import (
        KubernetesPodLogWatchAdapter,
    )

    return KubernetesPodLogWatchAdapter()


def build_error_budget_adapter() -> ErrorBudgetPort:
    from hexawyn.adapters.secondary.gitops.prometheus_error_budget_adapter import (
        PrometheusErrorBudgetAdapter,
    )

    return PrometheusErrorBudgetAdapter(metrics_query_port=build_metrics_query_adapter())
