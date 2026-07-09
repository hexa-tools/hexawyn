from __future__ import annotations

import os
from typing import TYPE_CHECKING

from fastmcp import FastMCP

from hexawyn.domain.errors import ClusterUnreachableError
from hexawyn.infrastructure.config.cache_manager import get_cache_stats
from hexawyn.infrastructure.config.config_manager import get_api_key
from hexawyn.infrastructure.config.kubeconfig_reader import (
    get_active_context,
    load_kubeconfig,
    validate_connection,
)
from hexawyn.infrastructure.memory.duckdb_client import get_connection

if TYPE_CHECKING:
    from hexawyn.application.ports.driven.adaptive_investigation_port import (
        AdaptiveInvestigationPort,
    )
    from hexawyn.application.ports.driven.alert_notification_port import (
        AlertNotificationPort,
    )
    from hexawyn.application.ports.driven.canary_comparison_port import (
        CanaryComparisonPort,
    )
    from hexawyn.application.ports.driven.capacity_forecast_port import (
        CapacityForecastPort,
    )
    from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
    from hexawyn.application.ports.driven.certificate_investigation_port import (
        CertificateInvestigationPort,
    )
    from hexawyn.application.ports.driven.cluster_resource_metrics_port import (
        ClusterResourceMetricsPort,
    )
    from hexawyn.application.ports.driven.compliance_audit_port import (
        ComplianceAuditPort,
    )
    from hexawyn.application.ports.driven.cost_forecast_port import CostForecastPort
    from hexawyn.application.ports.driven.cost_profiling_port import CostProfilingPort
    from hexawyn.application.ports.driven.cost_saving_estimation_port import (
        CostSavingEstimationPort,
    )
    from hexawyn.application.ports.driven.cross_namespace_traffic_port import (
        CrossNamespaceTrafficPort,
    )
    from hexawyn.application.ports.driven.deployment_latency_comparison_port import (
        DeploymentLatencyComparisonPort,
    )
    from hexawyn.application.ports.driven.drift_detection_port import DriftDetectionPort
    from hexawyn.application.ports.driven.error_attribution_port import (
        ErrorAttributionPort,
    )
    from hexawyn.application.ports.driven.error_budget_port import ErrorBudgetPort
    from hexawyn.application.ports.driven.etcd_logs_port import ETCDLogsPort
    from hexawyn.application.ports.driven.external_exposure_audit_port import (
        ExternalExposureAuditPort,
    )
    from hexawyn.application.ports.driven.fleet_health_port import FleetHealthPort
    from hexawyn.application.ports.driven.gitops_drift_audit_port import (
        GitOpsDriftAuditPort,
    )
    from hexawyn.application.ports.driven.gitops_port import GitOpsPort
    from hexawyn.application.ports.driven.headroom_simulation_port import (
        HeadroomSimulationPort,
    )
    from hexawyn.application.ports.driven.helm_release_version_port import (
        HelmReleaseVersionPort,
    )
    from hexawyn.application.ports.driven.hot_node_analysis_port import (
        HotNodeAnalysisPort,
    )
    from hexawyn.application.ports.driven.image_drift_port import ImageDriftPort
    from hexawyn.application.ports.driven.image_inventory_port import ImageInventoryPort
    from hexawyn.application.ports.driven.image_vulnerability_scan_port import (
        ImageVulnerabilityScanPort,
    )
    from hexawyn.application.ports.driven.istio_topology_port import IstioTopologyPort
    from hexawyn.application.ports.driven.k8s_port import ClusterContext, K8sPort
    from hexawyn.application.ports.driven.keda_port import KedaPort
    from hexawyn.application.ports.driven.kubernetes_topology_port import (
        KubernetesTopologyPort,
    )
    from hexawyn.application.ports.driven.kustomize_patch_analysis_port import (
        KustomizePatchAnalysisPort,
    )
    from hexawyn.application.ports.driven.latency_percentile_port import (
        LatencyPercentilePort,
    )
    from hexawyn.application.ports.driven.live_resource_port import LiveResourcePort
    from hexawyn.application.ports.driven.log_search_port import LogSearchPort
    from hexawyn.application.ports.driven.memory_saturation_port import (
        MemorySaturationPort,
    )
    from hexawyn.application.ports.driven.metric_correlation_port import (
        MetricCorrelationPort,
    )
    from hexawyn.application.ports.driven.metrics_query_port import MetricsQueryPort
    from hexawyn.application.ports.driven.monthly_incident_port import (
        MonthlyIncidentPort,
    )
    from hexawyn.application.ports.driven.mttr_trend_port import MTTRTrendPort
    from hexawyn.application.ports.driven.namespace_events_port import (
        NamespaceEventsPort,
    )
    from hexawyn.application.ports.driven.namespace_overview_port import (
        NamespaceOverviewPort,
    )
    from hexawyn.application.ports.driven.namespace_waste_port import (
        NamespaceWasteAnalysisPort,
    )
    from hexawyn.application.ports.driven.network_policy_audit_port import (
        NetworkPolicyAuditPort,
    )
    from hexawyn.application.ports.driven.pipeline_for_service_port import (
        PipelineForServicePort,
    )
    from hexawyn.application.ports.driven.pipeline_run_logs_port import (
        PipelineRunLogsPort,
    )
    from hexawyn.application.ports.driven.pod_log_watch_port import PodLogWatchPort
    from hexawyn.application.ports.driven.pod_logs_port import PodLogsPort
    from hexawyn.application.ports.driven.pod_metrics_baseline_port import (
        PodMetricsBaselinePort,
    )
    from hexawyn.application.ports.driven.pod_security_context_audit_port import (
        PodSecurityContextAuditPort,
    )
    from hexawyn.application.ports.driven.policy_port import PolicyPort
    from hexawyn.application.ports.driven.probe_audit_port import ProbeAuditPort
    from hexawyn.application.ports.driven.rbac_security_audit_port import (
        RBACSecurityAuditPort,
    )
    from hexawyn.application.ports.driven.recurring_incident_port import (
        RecurringIncidentPort,
    )
    from hexawyn.application.ports.driven.redundant_call_detection_port import (
        RedundantCallDetectionPort,
    )
    from hexawyn.application.ports.driven.resource_search_port import ResourceSearchPort
    from hexawyn.application.ports.driven.resource_yaml_port import ResourceYAMLPort
    from hexawyn.application.ports.driven.rightsizing_port import RightsizingPort
    from hexawyn.application.ports.driven.rollouts_port import RolloutsPort
    from hexawyn.application.ports.driven.secret_rotation_audit_port import (
        SecretRotationAuditPort,
    )
    from hexawyn.application.ports.driven.security_audit_port import SecurityAuditPort
    from hexawyn.application.ports.driven.service_cost_port import ServiceCostPort
    from hexawyn.application.ports.driven.service_dependency_graph_port import (
        ServiceDependencyGraphPort,
    )
    from hexawyn.application.ports.driven.slo_breach_prediction_port import (
        SLOBreachPredictionPort,
    )
    from hexawyn.application.ports.driven.slow_trace_search_port import (
        SlowTraceSearchPort,
    )
    from hexawyn.application.ports.driven.span_bottleneck_port import (
        SpanBottleneckPort,
    )
    from hexawyn.application.ports.driven.team_cost_port import TeamCostPort
    from hexawyn.application.ports.driven.tekton_port import TektonPort
    from hexawyn.application.ports.driven.tls_compliance_port import (
        TLSCompliancePort,
    )
    from hexawyn.application.ports.driven.topology_snapshot_port import (
        TopologySnapshotPort,
    )
    from hexawyn.application.ports.driven.trace_event_correlation_port import (
        TraceEventCorrelationPort,
    )
    from hexawyn.application.ports.driven.trace_log_correlation_port import (
        TraceLogCorrelationPort,
    )
    from hexawyn.application.ports.driven.trace_query_port import TraceQueryPort
    from hexawyn.application.ports.driven.version_regression_port import (
        VersionRegressionPort,
    )
    from hexawyn.application.ports.driven.weekly_reliability_report_port import (
        WeeklyReliabilityReportPort,
    )
    from hexawyn.application.ports.driven.what_if_simulation_port import (
        WhatIfSimulationPort,
    )
    from hexawyn.application.ports.driven.zombie_detection_port import (
        ZombieDetectionPort,
    )

# Initialize FastMCP server
mcp = FastMCP(
    name="hexawyn",
    version="0.1.0b0",
    instructions="AI-powered Kubernetes diagnostic agent",
)

# ── Startup kubeconfig validation ─────────────────────────
_k8s_api = None
_cluster_status: dict[str, str] = {"status": "not_initialized"}

context_name = "unknown"

try:
    _k8s_api = load_kubeconfig()
    active_ctx = get_active_context()
    context_name = str(active_ctx["name"]) if active_ctx else "unknown"
    _cluster_status = validate_connection(_k8s_api, context_name)
except ClusterUnreachableError as e:
    _cluster_status = {
        "status": "no_kubeconfig",
        "error": str(e),
    }
    print("[hexawyn] \u26a0\ufe0f  No kubeconfig found — starting in degraded mode")


def build_k8s_adapter() -> K8sPort:
    from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def build_tekton_adapter() -> TektonPort:
    from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def build_rightsizing_adapter() -> RightsizingPort:
    from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def build_what_if_simulation_adapter() -> WhatIfSimulationPort:
    from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def build_cost_forecast_adapter() -> CostForecastPort:
    from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def build_waste_adapter() -> NamespaceWasteAnalysisPort:
    from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=prometheus_url)


def build_zombie_detection_adapter() -> ZombieDetectionPort:
    from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def build_cost_saving_adapter() -> CostSavingEstimationPort:
    from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return VanillaAdapter(cluster_name=context or "default", prometheus_url=prometheus_url)


def build_fleet_health_adapter() -> FleetHealthPort:
    from hexawyn.adapters.secondary.fleet_health_adapter import FleetHealthAdapter

    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return FleetHealthAdapter(prometheus_url=prometheus_url)


def build_kubernetes_topology_adapter() -> KubernetesTopologyPort:
    from hexawyn.adapters.secondary.kubernetes_topology_adapter import (
        KubernetesTopologyAdapter,
    )

    context = context_name if context_name != "unknown" else None
    return KubernetesTopologyAdapter(cluster_name=context or "default")


def build_istio_topology_adapter() -> IstioTopologyPort:
    from hexawyn.adapters.secondary.istio_topology_adapter import IstioTopologyAdapter

    return IstioTopologyAdapter()


def build_gitops_adapter() -> GitOpsPort:
    from hexawyn.adapters.secondary.gitops.gitops_detector import GitOpsDetector

    return GitOpsDetector()


def build_topology_snapshot_adapter() -> TopologySnapshotPort:
    from hexawyn.infrastructure.memory.topology_snapshot_repository import (
        TopologySnapshotRepository,
    )

    return TopologySnapshotRepository(conn=get_connection())


def build_rollouts_adapter() -> RolloutsPort:
    from hexawyn.adapters.secondary.gitops.argo_rollouts_detector import (
        ArgoRolloutsDetector,
    )

    return ArgoRolloutsDetector()


def build_policy_adapter() -> PolicyPort:
    from hexawyn.adapters.secondary.gitops.policy_detector import PolicyDetector

    return PolicyDetector()


def build_cert_manager_adapter() -> CertManagerPort:
    from hexawyn.adapters.secondary.gitops.cert_manager_detector import (
        CertManagerDetector,
    )

    return CertManagerDetector()


def build_keda_adapter() -> KedaPort:
    from hexawyn.adapters.secondary.gitops.keda_detector import KedaDetector

    return KedaDetector()


def build_canary_comparison_adapter() -> CanaryComparisonPort:
    from hexawyn.adapters.secondary.gitops.otel_canary_comparison_adapter import (
        OTelCanaryComparisonAdapter,
    )

    return OTelCanaryComparisonAdapter()


def build_cost_profiling_adapter() -> CostProfilingPort:
    from hexawyn.adapters.secondary.gitops.otel_cost_profiling_adapter import (
        OTelCostProfilingAdapter,
    )

    return OTelCostProfilingAdapter()


def build_memory_saturation_adapter() -> MemorySaturationPort:
    from hexawyn.adapters.secondary.gitops.prometheus_memory_adapter import (
        PrometheusMemoryAdapter,
    )

    return PrometheusMemoryAdapter()


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
    from hexawyn.adapters.secondary.gitops.prometheus_http_adapter import (
        PrometheusHTTPAdapter,
    )

    prometheus_url = os.environ.get("PROMETHEUS_URL", "")
    return PrometheusHTTPAdapter(
        endpoint=prometheus_url, token=os.environ.get("PROMETHEUS_TOKEN") or None
    )


def build_cluster_resource_metrics_adapter() -> ClusterResourceMetricsPort:
    """Provider-aware cluster resource metrics.

    On AWS EKS (boto3 installed + EKS context) uses CloudWatch Container
    Insights; otherwise falls back to Prometheus (PromQL).
    """
    context = _current_cluster_context()
    if _is_aws_eks_context(context):
        from hexawyn.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )
        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchClusterResourceMetricsAdapter(
            cluster_name=context["name"], region=AWSEKSAdapter(context).region
        )

    from hexawyn.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (
        PrometheusClusterResourceMetricsAdapter,
    )

    return PrometheusClusterResourceMetricsAdapter(metrics_query_port=build_metrics_query_adapter())


def _current_cluster_context() -> ClusterContext:
    name = context_name if context_name != "unknown" else "default"
    return {"name": name, "cluster": name, "provider": "unknown", "namespace": "default"}


def _is_aws_eks_context(context: ClusterContext) -> bool:
    from hexawyn.adapters.secondary.aws.aws_eks_provider import AWSEKSProvider
    from hexawyn.infrastructure.config.stack_config import get_stack_override

    override = get_stack_override(context["name"])
    if override == "aws":
        return True
    if override == "vanilla":
        return False

    try:
        return AWSEKSProvider.supports(context)
    except Exception:
        return False


def build_capacity_forecast_adapter() -> CapacityForecastPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_capacity_forecast_adapter import (
        KubernetesCapacityForecastAdapter,
    )

    return KubernetesCapacityForecastAdapter()


def build_headroom_simulation_adapter() -> HeadroomSimulationPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_headroom_simulation_adapter import (
        KubernetesHeadroomSimulationAdapter,
    )

    return KubernetesHeadroomSimulationAdapter()


def build_node_analysis_adapter() -> HotNodeAnalysisPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_node_analysis_adapter import (
        KubernetesNodeAnalysisAdapter,
    )

    return KubernetesNodeAnalysisAdapter()


def build_helm_drift_adapter() -> DriftDetectionPort:
    from hexawyn.adapters.secondary.gitops.helm_drift_adapter import HelmDriftAdapter

    return HelmDriftAdapter()


def build_kustomize_drift_adapter() -> DriftDetectionPort:
    from hexawyn.adapters.secondary.gitops.kustomize_drift_adapter import (
        KustomizeDriftAdapter,
    )

    return KustomizeDriftAdapter()


def build_live_resource_adapter() -> LiveResourcePort:
    from hexawyn.adapters.secondary.gitops.kubernetes_live_resource_adapter import (
        KubernetesLiveResourceAdapter,
    )

    return KubernetesLiveResourceAdapter()


def build_audit_log_adapter() -> GitOpsDriftAuditPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_audit_log_adapter import (
        KubernetesAuditLogAdapter,
    )

    return KubernetesAuditLogAdapter()


def build_image_drift_adapter() -> ImageDriftPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_image_drift_adapter import (
        KubernetesImageDriftAdapter,
    )

    return KubernetesImageDriftAdapter()


def build_rbac_audit_adapter() -> RBACSecurityAuditPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_rbac_adapter import (
        KubernetesRBACAdapter,
    )

    return KubernetesRBACAdapter()


def build_pod_security_adapter() -> PodSecurityContextAuditPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_pod_security_adapter import (
        KubernetesPodSecurityAdapter,
    )

    return KubernetesPodSecurityAdapter()


def build_image_inventory_adapter() -> ImageInventoryPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_image_inventory_adapter import (
        KubernetesImageInventoryAdapter,
    )

    return KubernetesImageInventoryAdapter()


def build_image_vulnerability_scan_adapter() -> ImageVulnerabilityScanPort:
    from hexawyn.adapters.secondary.gitops.trivy_cve_scan_adapter import TrivyCVEScanAdapter

    return TrivyCVEScanAdapter()


def build_secret_rotation_audit_adapter() -> SecretRotationAuditPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_secret_audit_adapter import (
        KubernetesSecretAuditAdapter,
    )

    return KubernetesSecretAuditAdapter()


def build_network_policy_audit_adapter() -> NetworkPolicyAuditPort:
    from hexawyn.adapters.secondary.kubernetes_network_policy_adapter import (
        KubernetesNetworkPolicyAdapter,
    )

    return KubernetesNetworkPolicyAdapter()


def build_external_exposure_audit_adapter() -> ExternalExposureAuditPort:
    from hexawyn.adapters.secondary.kubernetes_external_exposure_adapter import (
        KubernetesExternalExposureAdapter,
    )

    return KubernetesExternalExposureAdapter()


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


def build_security_audit_adapter() -> SecurityAuditPort:
    from hexawyn.adapters.secondary.gitops.otel_security_audit_adapter import (
        OTelSecurityAuditAdapter,
    )

    return OTelSecurityAuditAdapter()


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
    if _is_aws_eks_context(context):
        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter
        from hexawyn.adapters.secondary.aws.xray_trace_adapter import AWSXRayTraceAdapter

        return AWSXRayTraceAdapter(region=AWSEKSAdapter(context).region)

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


def build_version_regression_adapter() -> VersionRegressionPort:
    from hexawyn.adapters.secondary.gitops.otel_version_regression_adapter import (
        OTelVersionRegressionAdapter,
    )

    return OTelVersionRegressionAdapter()


def build_redundant_call_detection_adapter() -> RedundantCallDetectionPort:
    from hexawyn.adapters.secondary.gitops.otel_redundant_call_adapter import (
        OTelRedundantCallAdapter,
    )

    return OTelRedundantCallAdapter()


def build_compliance_audit_adapter() -> ComplianceAuditPort:
    from hexawyn.adapters.secondary.gitops.otel_compliance_audit_adapter import (
        OTelComplianceAuditAdapter,
    )

    return OTelComplianceAuditAdapter()


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


def build_certificate_investigation_adapter() -> CertificateInvestigationPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_certificate_adapter import (
        KubernetesCertificateAdapter,
    )

    return KubernetesCertificateAdapter()


def build_resource_yaml_adapter() -> ResourceYAMLPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_resource_yaml_adapter import (
        KubernetesResourceYAMLAdapter,
    )

    return KubernetesResourceYAMLAdapter()


def build_pipeline_run_logs_adapter() -> PipelineRunLogsPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_pipeline_run_logs_adapter import (
        KubernetesPipelineRunLogsAdapter,
    )

    return KubernetesPipelineRunLogsAdapter()


def build_etcd_logs_adapter() -> ETCDLogsPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_etcd_logs_adapter import (
        KubernetesETCDLogsAdapter,
    )

    return KubernetesETCDLogsAdapter()


def build_pod_logs_adapter() -> PodLogsPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_pod_logs_adapter import (
        KubernetesPodLogsAdapter,
    )

    return KubernetesPodLogsAdapter()


def build_log_search_adapter() -> LogSearchPort:
    context = _current_cluster_context()
    if _is_aws_eks_context(context):
        from hexawyn.adapters.secondary.aws.cloudwatch_logs_adapter import CloudWatchLogsAdapter
        from hexawyn.adapters.secondary.aws.eks_adapter import AWSEKSAdapter

        return CloudWatchLogsAdapter(
            cluster_name=context["cluster"] or context["name"],
            region=AWSEKSAdapter(context).region,
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


def build_resource_search_adapter() -> ResourceSearchPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_label_search_adapter import (
        KubernetesLabelSearchAdapter,
    )

    return KubernetesLabelSearchAdapter()


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


def build_adaptive_investigation_adapter() -> AdaptiveInvestigationPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_adaptive_investigation_adapter import (
        KubernetesAdaptiveInvestigationAdapter,
    )

    return KubernetesAdaptiveInvestigationAdapter()


def build_pod_log_watch_adapter() -> PodLogWatchPort:
    from hexawyn.adapters.secondary.gitops.kubernetes_pod_log_watch_adapter import (
        KubernetesPodLogWatchAdapter,
    )

    return KubernetesPodLogWatchAdapter()


def build_alert_notification_adapter() -> AlertNotificationPort:
    from hexawyn.adapters.secondary.slack.slack_alert_adapter import SlackAlertAdapter

    return SlackAlertAdapter()


def build_pipeline_for_service_adapter() -> PipelineForServicePort:
    from hexawyn.adapters.secondary.gitops.kubernetes_pipeline_for_service_adapter import (
        KubernetesPipelineForServiceAdapter,
    )

    return KubernetesPipelineForServiceAdapter()


def build_probe_audit_adapter() -> ProbeAuditPort:
    from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter

    context = context_name if context_name != "unknown" else None
    return VanillaAdapter(cluster_name=context or "default")


def build_error_budget_adapter() -> ErrorBudgetPort:
    from hexawyn.adapters.secondary.gitops.prometheus_error_budget_adapter import (
        PrometheusErrorBudgetAdapter,
    )

    return PrometheusErrorBudgetAdapter(metrics_query_port=build_metrics_query_adapter())


def build_reliability_report_adapter() -> WeeklyReliabilityReportPort:
    from hexawyn.adapters.secondary.gitops.prometheus_reliability_adapter import (
        PrometheusReliabilityAdapter,
    )

    return PrometheusReliabilityAdapter(metrics_query_port=build_metrics_query_adapter())


def build_helm_release_version_adapter() -> HelmReleaseVersionPort:
    from hexawyn.adapters.secondary.gitops.helm_release_version_adapter import (
        HelmReleaseVersionAdapter,
    )

    return HelmReleaseVersionAdapter()


def build_kustomize_patch_analysis_adapter() -> KustomizePatchAnalysisPort:
    from hexawyn.adapters.secondary.gitops.kustomize_patch_adapter import (
        KustomizeCLIPatchAdapter,
    )

    return KustomizeCLIPatchAdapter()


def build_service_cost_adapter() -> ServiceCostPort:
    from hexawyn.adapters.secondary.gitops.service_cost_prometheus_adapter import (
        ServiceCostPrometheusAdapter,
    )

    return ServiceCostPrometheusAdapter()


def build_team_cost_adapter() -> TeamCostPort:
    from hexawyn.adapters.secondary.gitops.team_cost_kubernetes_adapter import (
        TeamCostKubernetesAdapter,
    )

    return TeamCostKubernetesAdapter()


def build_monthly_incident_adapter() -> MonthlyIncidentPort:
    from hexawyn.adapters.secondary.gitops.monthly_incident_adapter import (
        MonthlyIncidentAdapter,
    )

    return MonthlyIncidentAdapter()


def build_mttr_trend_adapter() -> MTTRTrendPort:
    from hexawyn.adapters.secondary.gitops.mttr_trend_adapter import (
        MTTRTrendAdapter,
    )

    return MTTRTrendAdapter()


def build_recurring_incident_adapter() -> RecurringIncidentPort:
    from hexawyn.adapters.secondary.gitops.recurring_incident_adapter import (
        RecurringIncidentAdapter,
    )

    return RecurringIncidentAdapter()


def build_tls_compliance_adapter() -> TLSCompliancePort:
    from hexawyn.adapters.secondary.gitops.tls_compliance_adapter import (
        TLSComplianceAdapter,
    )

    return TLSComplianceAdapter()


def register_tools(server: FastMCP) -> None:
    """Auto-discover and register all MCP tools from mcp/tools/ modules."""
    import importlib
    from pathlib import Path

    tools_dir = Path(__file__).parent / "tools"
    for module_path in sorted(tools_dir.glob("*.py")):
        module_name = module_path.stem
        if module_name.startswith("_"):
            continue
        try:
            mod = importlib.import_module(f"hexawyn.mcp.tools.{module_name}")
            register_fn = getattr(mod, "register", None)
            if callable(register_fn):
                register_fn(server)
        except Exception:
            pass


@mcp.tool()
def health() -> dict[str, str]:
    """
    Health check endpoint — used by Docker, CI, and Marketplace readiness probes.
    Returns status, version, DuckDB connectivity, API key status, and cluster connectivity.
    """
    db_ok = False
    try:
        conn = get_connection()
        conn.execute("SELECT 1").fetchone()
        db_ok = True
    except Exception:
        db_ok = False

    api_key_ok = get_api_key() is not None
    cache_stats = get_cache_stats()
    slack_configured = bool(os.environ.get("HEXAWYN_SLACK_WEBHOOK_URL"))

    return {
        "status": "ok" if db_ok else "degraded",
        "version": "0.1.0b0",
        "duckdb": "connected" if db_ok else "unavailable",
        "api_key": "configured" if api_key_ok else "missing",
        "cluster": _cluster_status.get("status", "unknown"),
        "context": _cluster_status.get("context", "none"),
        "cache_l1_size": str(cache_stats["l1_size"]),
        "cache_l1_ttl": str(cache_stats["l1_ttl_seconds"]),
        "slack": "configured" if slack_configured else "not_configured",
    }


# ── Register all tools ──────────────────────────────────────
register_tools(mcp)


if __name__ == "__main__":  # pragma: no cover
    port = int(os.environ.get("HEXAWYN_PORT", "8000"))
    mcp.run(host="0.0.0.0", port=port)
