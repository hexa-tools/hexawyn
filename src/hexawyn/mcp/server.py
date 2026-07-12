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
    from collections.abc import Callable

    from hexawyn.application.ports.driven.adaptive_investigation_port import (
        AdaptiveInvestigationPort,
    )
    from hexawyn.application.ports.driven.alert_notification_port import (
        AlertNotificationPort,
    )
    from hexawyn.application.ports.driven.budget_intelligence_port import (
        BudgetIntelligencePort,
    )
    from hexawyn.application.ports.driven.budget_projection_port import (
        BudgetProjectionPort,
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
    from hexawyn.application.ports.driven.cluster_diff_port import ClusterDiffPort
    from hexawyn.application.ports.driven.cluster_operator_status_port import (
        ClusterOperatorStatusPort,
    )
    from hexawyn.application.ports.driven.cluster_resource_metrics_port import (
        ClusterResourceMetricsPort,
    )
    from hexawyn.application.ports.driven.compliance_audit_port import (
        ComplianceAuditPort,
    )
    from hexawyn.application.ports.driven.cost_estimation_port import (
        CostEstimationPort,
    )
    from hexawyn.application.ports.driven.cost_forecast_port import CostForecastPort
    from hexawyn.application.ports.driven.cost_profiling_port import CostProfilingPort
    from hexawyn.application.ports.driven.cost_saving_estimation_port import (
        CostSavingEstimationPort,
    )
    from hexawyn.application.ports.driven.critical_cve_port import CriticalCvePort
    from hexawyn.application.ports.driven.cross_cluster_incident_port import (
        CrossClusterIncidentPort,
    )
    from hexawyn.application.ports.driven.cross_namespace_traffic_port import (
        CrossNamespaceTrafficPort,
    )
    from hexawyn.application.ports.driven.deployment_latency_comparison_port import (
        DeploymentLatencyComparisonPort,
    )
    from hexawyn.application.ports.driven.disruption_risk_port import (
        DisruptionRiskPort,
    )
    from hexawyn.application.ports.driven.drift_detection_port import DriftDetectionPort
    from hexawyn.application.ports.driven.engineer_workload_port import (
        EngineerWorkloadPort,
    )
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
    from hexawyn.application.ports.driven.helm_values_diff_port import (
        HelmValuesDiffPort,
    )
    from hexawyn.application.ports.driven.hot_node_analysis_port import (
        HotNodeAnalysisPort,
    )
    from hexawyn.application.ports.driven.image_drift_port import ImageDriftPort
    from hexawyn.application.ports.driven.image_inventory_port import ImageInventoryPort
    from hexawyn.application.ports.driven.image_vulnerability_scan_port import (
        ImageVulnerabilityScanPort,
    )
    from hexawyn.application.ports.driven.incident_cost_port import IncidentCostPort
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
    from hexawyn.application.ports.driven.machine_config_pool_port import (
        MachineConfigPoolPort,
    )
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
    from hexawyn.application.ports.driven.optimization_roi_port import (
        OptimizationRoiPort,
    )
    from hexawyn.application.ports.driven.pipeline_for_service_port import (
        PipelineForServicePort,
    )
    from hexawyn.application.ports.driven.pipeline_run_logs_port import (
        PipelineRunLogsPort,
    )
    from hexawyn.application.ports.driven.platform_reliability_port import (
        PlatformReliabilityPort,
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
    from hexawyn.application.ports.driven.prediction_roi_port import (
        PredictionRoiPort,
    )
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
    from hexawyn.application.ports.driven.security_posture_port import (
        SecurityPosturePort,
    )
    from hexawyn.application.ports.driven.service_cost_port import ServiceCostPort
    from hexawyn.application.ports.driven.service_dependency_graph_port import (
        ServiceDependencyGraphPort,
    )
    from hexawyn.application.ports.driven.sla_report_port import SlaReportPort
    from hexawyn.application.ports.driven.slo_breach_prediction_port import (
        SLOBreachPredictionPort,
    )
    from hexawyn.application.ports.driven.slow_trace_search_port import (
        SlowTraceSearchPort,
    )
    from hexawyn.application.ports.driven.span_bottleneck_port import (
        SpanBottleneckPort,
    )
    from hexawyn.application.ports.driven.spike_provisioning_port import (
        SpikeProvisioningPort,
    )
    from hexawyn.application.ports.driven.stale_credentials_port import (
        StaleCredentialsPort,
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
    from hexawyn.application.ports.driven.unauthorized_access_port import (
        UnauthorizedAccessPort,
    )
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


def build_budget_projection_adapter() -> BudgetProjectionPort:
    from hexawyn.adapters.secondary.gitops.budget_projection_adapter import (
        BudgetProjectionAdapter,
    )

    return BudgetProjectionAdapter(cost_forecast_port=build_cost_forecast_adapter())


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


def _is_gcp_gke_context(context: ClusterContext) -> bool:
    from hexawyn.adapters.secondary.gcp.gcp_gke_provider import GCPGKEProvider

    return _detect_provider(context, "gcp", GCPGKEProvider.supports)


def _is_azure_aks_context(context: ClusterContext) -> bool:
    from hexawyn.adapters.secondary.azure.azure_aks_provider import AzureAKSProvider

    return _detect_provider(context, "azure", AzureAKSProvider.supports)


def build_cluster_resource_metrics_adapter() -> ClusterResourceMetricsPort:
    """Provider-aware cluster resource metrics.

    On AWS EKS (boto3 installed + EKS context) uses CloudWatch Container
    Insights; otherwise falls back to Prometheus (PromQL).
    """
    context = _current_cluster_context()
    if _is_datadog_enabled(context):
        from hexawyn.adapters.secondary.datadog.datadog_metrics_adapter import (
            DatadogClusterResourceMetricsAdapter,
        )
        from hexawyn.infrastructure.config.datadog_config import get_datadog_config

        config = get_datadog_config()
        return DatadogClusterResourceMetricsAdapter(
            key=config["key"], app_key=config["app_key"], site=config["site"]
        )

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


def _is_datadog_enabled(context: ClusterContext) -> bool:
    from hexawyn.infrastructure.config.datadog_config import is_datadog_configured
    from hexawyn.infrastructure.config.stack_config import get_stack_override

    override = get_stack_override(context["name"])
    if override is not None:
        return override == "datadog"
    return is_datadog_configured()


def _current_cluster_context() -> ClusterContext:
    name = context_name if context_name != "unknown" else "default"
    return {"name": name, "cluster": name, "provider": "unknown", "namespace": "default"}


def _is_aws_eks_context(context: ClusterContext) -> bool:
    from hexawyn.adapters.secondary.aws.aws_eks_provider import AWSEKSProvider

    return _detect_provider(context, "aws", AWSEKSProvider.supports)


def _detect_provider(
    context: ClusterContext,
    provider_key: str,
    supports: Callable[[ClusterContext], bool],
) -> bool:
    """Resolve whether a cloud provider applies to the context.

    An explicit stack override wins over auto-detection; otherwise the
    provider's own `supports()` is used (failures are swallowed as False).
    """
    from hexawyn.infrastructure.config.stack_config import get_stack_override

    override = get_stack_override(context["name"])
    if override is not None:
        return override == provider_key

    try:
        return supports(context)
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


def build_spike_provisioning_adapter() -> SpikeProvisioningPort:
    from hexawyn.adapters.secondary.gitops.spike_provisioning_adapter import (
        SpikeProvisioningAdapter,
    )

    return SpikeProvisioningAdapter(
        headroom_port=build_headroom_simulation_adapter(),
        current_cpu_used_cores=0.0,
        current_memory_used_gb=0.0,
    )


def build_optimization_roi_adapter() -> OptimizationRoiPort:
    from hexawyn.adapters.secondary.gitops.optimization_roi_adapter import (
        OptimizationRoiAdapter,
    )
    from hexawyn.adapters.secondary.gitops.optimization_roi_source import (
        EmptySprintRoiSource,
    )

    return OptimizationRoiAdapter(source=EmptySprintRoiSource())


def build_sla_report_adapter() -> SlaReportPort:
    from hexawyn.adapters.secondary.gitops.sla_report_adapter import SlaReportAdapter
    from hexawyn.adapters.secondary.gitops.sla_report_source import (
        EmptyQuarterSlaSource,
    )

    return SlaReportAdapter(source=EmptyQuarterSlaSource())


def build_platform_reliability_adapter() -> PlatformReliabilityPort:
    from hexawyn.adapters.secondary.gitops.platform_reliability_adapter import (
        PlatformReliabilityAdapter,
    )
    from hexawyn.adapters.secondary.gitops.platform_reliability_source import (
        EmptyReliabilityDataSource,
    )

    return PlatformReliabilityAdapter(source=EmptyReliabilityDataSource())


def build_incident_cost_adapter() -> IncidentCostPort:
    from hexawyn.adapters.secondary.gitops.incident_cost_adapter import (
        IncidentCostAdapter,
    )
    from hexawyn.adapters.secondary.gitops.incident_cost_source import (
        ConfigIncidentCostSource,
    )

    return IncidentCostAdapter(source=ConfigIncidentCostSource())


def build_prediction_roi_adapter() -> PredictionRoiPort:
    from hexawyn.adapters.secondary.gitops.prediction_roi_adapter import (
        PredictionRoiAdapter,
    )
    from hexawyn.adapters.secondary.gitops.prediction_roi_source import (
        ConfigPredictionRoiSource,
    )

    return PredictionRoiAdapter(source=ConfigPredictionRoiSource())


def build_budget_intelligence_adapter() -> BudgetIntelligencePort:
    from hexawyn.adapters.secondary.gitops.budget_intelligence_adapter import (
        BudgetIntelligenceAdapter,
    )
    from hexawyn.adapters.secondary.gitops.budget_intelligence_source import (
        ConfigBudgetIntelligenceSource,
    )

    return BudgetIntelligenceAdapter(source=ConfigBudgetIntelligenceSource())


def build_night_intervention_adapter() -> EngineerWorkloadPort:
    from hexawyn.adapters.secondary.gitops.night_intervention_adapter import (
        NightInterventionAdapter,
    )
    from hexawyn.adapters.secondary.gitops.night_intervention_source import (
        EmptyNightInterventionSource,
    )

    return NightInterventionAdapter(source=EmptyNightInterventionSource())


def build_disruption_risk_adapter() -> DisruptionRiskPort:
    from hexawyn.adapters.secondary.gitops.disruption_risk_adapter import (
        DisruptionRiskAdapter,
    )
    from hexawyn.adapters.secondary.gitops.disruption_risk_source import (
        EmptyDisruptionRiskSource,
    )

    return DisruptionRiskAdapter(source=EmptyDisruptionRiskSource())


def build_critical_cve_adapter() -> CriticalCvePort:
    from hexawyn.adapters.secondary.gitops.critical_cve_adapter import (
        CriticalCveAdapter,
    )
    from hexawyn.adapters.secondary.gitops.critical_cve_source import (
        EmptyCriticalCveSource,
    )

    return CriticalCveAdapter(source=EmptyCriticalCveSource())


def build_stale_credentials_adapter() -> StaleCredentialsPort:
    from hexawyn.adapters.secondary.gitops.stale_credentials_adapter import (
        StaleCredentialsAdapter,
    )
    from hexawyn.adapters.secondary.gitops.stale_credentials_source import (
        EmptyStaleCredentialsSource,
    )

    return StaleCredentialsAdapter(source=EmptyStaleCredentialsSource())


def build_unauthorized_access_adapter() -> UnauthorizedAccessPort:
    from hexawyn.adapters.secondary.gitops.unauthorized_access_adapter import (
        UnauthorizedAccessAdapter,
    )
    from hexawyn.adapters.secondary.gitops.unauthorized_access_source import (
        EmptyUnauthorizedAccessSource,
    )

    return UnauthorizedAccessAdapter(source=EmptyUnauthorizedAccessSource())


def build_cost_adapter() -> CostEstimationPort:
    """Select the cost adapter based on the detected cloud provider."""

    provider = context_name or ""
    provider_lower = provider.lower()

    if "eks" in provider_lower or provider_lower == "aws":
        from hexawyn.adapters.secondary.aws.aws_cost_adapter import AWSCostAdapter

        return AWSCostAdapter(region="us-east-1")
    if "aks" in provider_lower or provider_lower == "azure":
        from hexawyn.adapters.secondary.azure.azure_cost_adapter import AzureCostAdapter

        return AzureCostAdapter(subscription_id="unknown")
    if "gke" in provider_lower or provider_lower == "gcp":
        from hexawyn.adapters.secondary.gcp.gcp_cost_adapter import GCPCostAdapter

        return GCPCostAdapter(project_id="unknown")

    from hexawyn.adapters.secondary.vanilla.vanilla_cost_adapter import VanillaCostAdapter

    return VanillaCostAdapter()


def build_cluster_diff_adapter() -> ClusterDiffPort:
    from hexawyn.adapters.secondary.gitops.cluster_diff_adapter import (
        ClusterDiffAdapter,
    )
    from hexawyn.adapters.secondary.gitops.cluster_diff_source import (
        EmptyClusterInventorySource,
    )

    return ClusterDiffAdapter(source=EmptyClusterInventorySource())


def build_cross_cluster_incident_adapter() -> CrossClusterIncidentPort:
    from hexawyn.adapters.secondary.gitops.cross_cluster_incident_adapter import (
        CrossClusterIncidentAdapter,
    )
    from hexawyn.adapters.secondary.gitops.cross_cluster_incident_source import (
        EmptyFailureSignatureSource,
    )

    return CrossClusterIncidentAdapter(source=EmptyFailureSignatureSource())


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


def build_helm_values_diff_adapter() -> HelmValuesDiffPort:
    from hexawyn.adapters.secondary.gitops.helm_values_adapter import (
        HelmValuesAdapter,
    )

    return HelmValuesAdapter()


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


def build_security_posture_adapter() -> SecurityPosturePort:
    from hexawyn.adapters.secondary.security_posture.category_providers import (
        PodSecurityProvider,
        TLSComplianceProvider,
    )
    from hexawyn.adapters.secondary.security_posture.security_posture_adapter import (
        ComplianceCategoryProvider,
        SecurityPostureAdapter,
    )
    from hexawyn.application.service.audit_tls_compliance_service import (
        AuditTLSComplianceService,
    )
    from hexawyn.application.service.pod_security_standards_audit_service import (
        PodSecurityStandardsAuditService,
    )

    providers: list[ComplianceCategoryProvider] = [
        TLSComplianceProvider(
            service=AuditTLSComplianceService(tls_port=build_tls_compliance_adapter())
        ),
        PodSecurityProvider(
            service=PodSecurityStandardsAuditService(pod_security_port=build_pod_security_adapter())
        ),
    ]
    return SecurityPostureAdapter(providers=providers)


def build_cluster_operator_status_adapter() -> ClusterOperatorStatusPort:
    from hexawyn.adapters.secondary.openshift.openshift_cluster_operator_adapter import (
        OpenShiftClusterOperatorAdapter,
    )

    return OpenShiftClusterOperatorAdapter()


def build_machine_config_pool_adapter() -> MachineConfigPoolPort:
    from hexawyn.adapters.secondary.openshift.openshift_machine_config_adapter import (
        OpenShiftMachineConfigAdapter,
    )

    return OpenShiftMachineConfigAdapter()


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
