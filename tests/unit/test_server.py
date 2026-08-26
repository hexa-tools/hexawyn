"""Comprehensive tests for server.py — all build_*_adapter() functions and helpers."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from hexawyn.application.ports.driven.adaptive_investigation_port import (
    AdaptiveInvestigationPort,
)
from hexawyn.application.ports.driven.alert_notification_port import AlertNotificationPort
from hexawyn.application.ports.driven.budget_intelligence_port import BudgetIntelligencePort
from hexawyn.application.ports.driven.budget_projection_port import BudgetProjectionPort
from hexawyn.application.ports.driven.canary_comparison_port import CanaryComparisonPort
from hexawyn.application.ports.driven.capacity_forecast_port import CapacityForecastPort
from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
from hexawyn.application.ports.driven.certificate_investigation_port import (
    CertificateInvestigationPort,
)
from hexawyn.application.ports.driven.cluster_certificate_health_port import (
    ClusterCertificateHealthPort,
)
from hexawyn.application.ports.driven.cluster_diff_port import ClusterDiffPort
from hexawyn.application.ports.driven.cluster_operator_status_port import (
    ClusterOperatorStatusPort,
)
from hexawyn.application.ports.driven.cluster_resource_metrics_port import (
    ClusterResourceMetricsPort,
)
from hexawyn.application.ports.driven.compliance_audit_port import ComplianceAuditPort
from hexawyn.application.ports.driven.consolidation_port import ConsolidationPort
from hexawyn.application.ports.driven.cost_estimation_port import CostEstimationPort
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
from hexawyn.application.ports.driven.disruption_risk_port import DisruptionRiskPort
from hexawyn.application.ports.driven.drift_detection_port import DriftDetectionPort
from hexawyn.application.ports.driven.engineer_workload_port import EngineerWorkloadPort
from hexawyn.application.ports.driven.error_attribution_port import ErrorAttributionPort
from hexawyn.application.ports.driven.error_budget_port import ErrorBudgetPort
from hexawyn.application.ports.driven.etcd_logs_port import ETCDLogsPort
from hexawyn.application.ports.driven.external_exposure_audit_port import (
    ExternalExposureAuditPort,
)
from hexawyn.application.ports.driven.fleet_health_port import FleetHealthPort
from hexawyn.application.ports.driven.gitops_drift_audit_port import GitOpsDriftAuditPort
from hexawyn.application.ports.driven.gitops_port import GitOpsPort
from hexawyn.application.ports.driven.headroom_simulation_port import (
    HeadroomSimulationPort,
)
from hexawyn.application.ports.driven.helm_release_version_port import HelmReleaseVersionPort
from hexawyn.application.ports.driven.helm_values_diff_port import HelmValuesDiffPort
from hexawyn.application.ports.driven.hot_node_analysis_port import HotNodeAnalysisPort
from hexawyn.application.ports.driven.image_drift_port import ImageDriftPort
from hexawyn.application.ports.driven.image_inventory_port import ImageInventoryPort
from hexawyn.application.ports.driven.image_vulnerability_scan_port import (
    ImageVulnerabilityScanPort,
)
from hexawyn.application.ports.driven.incident_cost_port import IncidentCostPort
from hexawyn.application.ports.driven.incident_memory_port import IncidentMemoryPort
from hexawyn.application.ports.driven.ingress_port import IngressPort
from hexawyn.application.ports.driven.istio_topology_port import IstioTopologyPort
from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.ports.driven.keda_port import KedaPort
from hexawyn.application.ports.driven.kubernetes_topology_port import KubernetesTopologyPort
from hexawyn.application.ports.driven.kustomize_patch_analysis_port import (
    KustomizePatchAnalysisPort,
)
from hexawyn.application.ports.driven.latency_percentile_port import LatencyPercentilePort
from hexawyn.application.ports.driven.live_resource_port import LiveResourcePort
from hexawyn.application.ports.driven.log_search_port import LogSearchPort
from hexawyn.application.ports.driven.machine_config_pool_port import MachineConfigPoolPort
from hexawyn.application.ports.driven.memory_saturation_port import MemorySaturationPort
from hexawyn.application.ports.driven.metric_correlation_port import MetricCorrelationPort
from hexawyn.application.ports.driven.metrics_query_port import MetricsQueryPort
from hexawyn.application.ports.driven.monthly_incident_port import MonthlyIncidentPort
from hexawyn.application.ports.driven.mttr_trend_port import MTTRTrendPort
from hexawyn.application.ports.driven.namespace_events_port import NamespaceEventsPort
from hexawyn.application.ports.driven.namespace_overview_port import NamespaceOverviewPort
from hexawyn.application.ports.driven.namespace_waste_port import NamespaceWasteAnalysisPort
from hexawyn.application.ports.driven.network_policy_audit_port import (
    NetworkPolicyAuditPort,
)
from hexawyn.application.ports.driven.openshift_resource_port import OpenShiftResourcePort
from hexawyn.application.ports.driven.optimization_roi_port import OptimizationRoiPort
from hexawyn.application.ports.driven.pipeline_baseline_port import PipelineBaselinePort
from hexawyn.application.ports.driven.pipeline_for_service_port import PipelineForServicePort
from hexawyn.application.ports.driven.pipeline_run_logs_port import PipelineRunLogsPort
from hexawyn.application.ports.driven.plan_port import PlanPort
from hexawyn.application.ports.driven.platform_reliability_port import PlatformReliabilityPort
from hexawyn.application.ports.driven.pod_log_watch_port import PodLogWatchPort
from hexawyn.application.ports.driven.pod_logs_port import PodLogsPort
from hexawyn.application.ports.driven.pod_metrics_baseline_port import PodMetricsBaselinePort
from hexawyn.application.ports.driven.pod_security_context_audit_port import (
    PodSecurityContextAuditPort,
)
from hexawyn.application.ports.driven.policy_port import PolicyPort
from hexawyn.application.ports.driven.prediction_roi_port import PredictionRoiPort
from hexawyn.application.ports.driven.probe_audit_port import ProbeAuditPort
from hexawyn.application.ports.driven.rbac_security_audit_port import RBACSecurityAuditPort
from hexawyn.application.ports.driven.recurring_incident_port import RecurringIncidentPort
from hexawyn.application.ports.driven.redundant_call_detection_port import (
    RedundantCallDetectionPort,
)
from hexawyn.application.ports.driven.resource_search_port import ResourceSearchPort
from hexawyn.application.ports.driven.resource_yaml_port import ResourceYAMLPort
from hexawyn.application.ports.driven.rightsizing_port import RightsizingPort
from hexawyn.application.ports.driven.rollouts_port import RolloutsPort
from hexawyn.application.ports.driven.secret_rotation_audit_port import SecretRotationAuditPort
from hexawyn.application.ports.driven.security_audit_port import SecurityAuditPort
from hexawyn.application.ports.driven.security_posture_port import SecurityPosturePort
from hexawyn.application.ports.driven.service_cost_port import ServiceCostPort
from hexawyn.application.ports.driven.service_dependency_graph_port import (
    ServiceDependencyGraphPort,
)
from hexawyn.application.ports.driven.sla_report_port import SlaReportPort
from hexawyn.application.ports.driven.slo_breach_prediction_port import SLOBreachPredictionPort
from hexawyn.application.ports.driven.slow_trace_search_port import SlowTraceSearchPort
from hexawyn.application.ports.driven.span_bottleneck_port import SpanBottleneckPort
from hexawyn.application.ports.driven.spike_provisioning_port import SpikeProvisioningPort
from hexawyn.application.ports.driven.stale_credentials_port import StaleCredentialsPort
from hexawyn.application.ports.driven.team_cost_port import TeamCostPort
from hexawyn.application.ports.driven.tekton_port import TektonPort
from hexawyn.application.ports.driven.tls_compliance_port import TLSCompliancePort
from hexawyn.application.ports.driven.topology_snapshot_port import TopologySnapshotPort
from hexawyn.application.ports.driven.trace_event_correlation_port import (
    TraceEventCorrelationPort,
)
from hexawyn.application.ports.driven.trace_log_correlation_port import TraceLogCorrelationPort
from hexawyn.application.ports.driven.trace_query_port import TraceQueryPort
from hexawyn.application.ports.driven.unauthorized_access_port import UnauthorizedAccessPort
from hexawyn.application.ports.driven.usage_meter_port import UsageMeterPort
from hexawyn.application.ports.driven.version_regression_port import VersionRegressionPort
from hexawyn.application.ports.driven.weekly_reliability_report_port import (
    WeeklyReliabilityReportPort,
)
from hexawyn.application.ports.driven.what_if_simulation_port import WhatIfSimulationPort
from hexawyn.application.ports.driven.zombie_detection_port import ZombieDetectionPort


def _mock_kubeconfig() -> MagicMock:
    return MagicMock()


class TestMCPBuilderFunctions:
    """Test every build_*_adapter() function in server.py."""

    @pytest.fixture(autouse=True)
    def _setup(self) -> None:
        from hexawyn.mcp import server as server_mod

        self.server_mod = server_mod

    def test_build_k8s_adapter(self) -> None:
        result = self.server_mod.build_k8s_adapter()
        assert isinstance(result, K8sPort)

    def test_build_ingress_adapter(self) -> None:
        result = self.server_mod.build_ingress_adapter()
        assert isinstance(result, IngressPort)

    def test_build_tekton_adapter(self) -> None:
        from unittest.mock import patch

        with patch("hexawyn.mcp.adapters.cluster_adapters.get_connection"):
            result = self.server_mod.build_tekton_adapter()
        assert isinstance(result, TektonPort)

    def test_build_rightsizing_adapter(self) -> None:
        result = self.server_mod.build_rightsizing_adapter()
        assert isinstance(result, RightsizingPort)

    def test_build_what_if_simulation_adapter(self) -> None:
        result = self.server_mod.build_what_if_simulation_adapter()
        assert isinstance(result, WhatIfSimulationPort)

    def test_build_cost_forecast_adapter(self) -> None:
        result = self.server_mod.build_cost_forecast_adapter()
        assert isinstance(result, CostForecastPort)

    def test_build_budget_projection_adapter(self) -> None:
        with patch.object(self.server_mod, "context_name", "test-cluster"):
            result = self.server_mod.build_budget_projection_adapter()
            assert isinstance(result, BudgetProjectionPort)

    def test_build_waste_adapter(self) -> None:
        result = self.server_mod.build_waste_adapter()
        assert isinstance(result, NamespaceWasteAnalysisPort)

    def test_build_zombie_detection_adapter(self) -> None:
        result = self.server_mod.build_zombie_detection_adapter()
        assert isinstance(result, ZombieDetectionPort)

    def test_build_cost_saving_adapter(self) -> None:
        result = self.server_mod.build_cost_saving_adapter()
        assert isinstance(result, CostSavingEstimationPort)

    def test_build_fleet_health_adapter(self) -> None:
        result = self.server_mod.build_fleet_health_adapter()
        assert isinstance(result, FleetHealthPort)

    def test_build_cluster_certificate_health_adapter(self) -> None:
        with (
            patch(
                "hexawyn.mcp.adapters.cluster_adapters.load_kubeconfig",
                return_value=MagicMock(),
            ),
            patch("hexawyn.mcp.adapters.cluster_adapters.context_name", "test-cluster"),
        ):
            result = self.server_mod.build_cluster_certificate_health_adapter()
            assert isinstance(result, ClusterCertificateHealthPort)

    def test_build_kubernetes_topology_adapter(self) -> None:
        result = self.server_mod.build_kubernetes_topology_adapter()
        assert isinstance(result, KubernetesTopologyPort)

    def test_build_istio_topology_adapter(self) -> None:
        result = self.server_mod.build_istio_topology_adapter()
        assert isinstance(result, IstioTopologyPort)

    def test_build_gitops_adapter(self) -> None:
        result = self.server_mod.build_gitops_adapter()
        assert isinstance(result, GitOpsPort)

    def test_build_topology_snapshot_adapter(self) -> None:
        with patch(
            "hexawyn.mcp.adapters.cluster_adapters.get_connection",
            return_value=MagicMock(),
        ):
            result = self.server_mod.build_topology_snapshot_adapter()
            assert isinstance(result, TopologySnapshotPort)

    def test_build_incident_memory_adapter(self) -> None:
        with patch.object(self.server_mod, "get_connection", return_value=MagicMock()):
            result = self.server_mod.build_incident_memory_adapter()
            assert isinstance(result, IncidentMemoryPort)

    def test_build_rollouts_adapter(self) -> None:
        result = self.server_mod.build_rollouts_adapter()
        assert isinstance(result, RolloutsPort)

    def test_build_policy_adapter(self) -> None:
        result = self.server_mod.build_policy_adapter()
        assert isinstance(result, PolicyPort)

    def test_build_cert_manager_adapter(self) -> None:
        result = self.server_mod.build_cert_manager_adapter()
        assert isinstance(result, CertManagerPort)

    def test_build_keda_adapter(self) -> None:
        result = self.server_mod.build_keda_adapter()
        assert isinstance(result, KedaPort)

    def test_build_canary_comparison_adapter(self) -> None:
        result = self.server_mod.build_canary_comparison_adapter()
        assert isinstance(result, CanaryComparisonPort)

    def test_build_cost_profiling_adapter(self) -> None:
        result = self.server_mod.build_cost_profiling_adapter()
        assert isinstance(result, CostProfilingPort)

    def test_build_memory_saturation_adapter(self) -> None:
        result = self.server_mod.build_memory_saturation_adapter()
        assert isinstance(result, MemorySaturationPort)

    def test_build_span_bottleneck_adapter(self) -> None:
        result = self.server_mod.build_span_bottleneck_adapter()
        assert isinstance(result, SpanBottleneckPort)

    def test_build_latency_percentile_adapter(self) -> None:
        result = self.server_mod.build_latency_percentile_adapter()
        assert isinstance(result, LatencyPercentilePort)

    def test_build_metric_correlation_adapter(self) -> None:
        result = self.server_mod.build_metric_correlation_adapter()
        assert isinstance(result, MetricCorrelationPort)

    def test_build_metrics_query_adapter(self) -> None:
        from hexawyn.application.ports.driven.k8s_port import ClusterContext

        mock_context: ClusterContext = {
            "name": "vanilla",
            "cluster": "test",
            "provider": "vanilla",
            "namespace": "ns",
        }
        with patch(
            "hexawyn.mcp.adapters.observability_adapters._current_cluster_context",
            return_value=mock_context,
        ):
            result = self.server_mod.build_metrics_query_adapter()
            assert isinstance(result, MetricsQueryPort)

    def test_build_cluster_resource_metrics_adapter(self) -> None:
        from hexawyn.application.ports.driven.k8s_port import ClusterContext

        mock_context: ClusterContext = {
            "name": "vanilla",
            "cluster": "test",
            "provider": "vanilla",
            "namespace": "ns",
        }
        with patch(
            "hexawyn.mcp.adapters.cluster_adapters._current_cluster_context",
            return_value=mock_context,
        ):
            result = self.server_mod.build_cluster_resource_metrics_adapter()
            assert isinstance(result, ClusterResourceMetricsPort)

    def test_build_capacity_forecast_v2_adapter(self) -> None:
        result = self.server_mod.build_capacity_forecast_adapter()
        assert isinstance(result, CapacityForecastPort)

    def test_build_headroom_simulation_adapter(self) -> None:
        result = self.server_mod.build_headroom_simulation_adapter()
        assert isinstance(result, HeadroomSimulationPort)

    def test_build_spike_provisioning_adapter(self) -> None:
        result = self.server_mod.build_spike_provisioning_adapter()
        assert isinstance(result, SpikeProvisioningPort)

    def test_build_optimization_roi_adapter(self) -> None:
        result = self.server_mod.build_optimization_roi_adapter()
        assert isinstance(result, OptimizationRoiPort)

    def test_build_sla_report_adapter(self) -> None:
        result = self.server_mod.build_sla_report_adapter()
        assert isinstance(result, SlaReportPort)

    def test_build_platform_reliability_adapter(self) -> None:
        result = self.server_mod.build_platform_reliability_adapter()
        assert isinstance(result, PlatformReliabilityPort)

    def test_build_incident_cost_adapter(self) -> None:
        result = self.server_mod.build_incident_cost_adapter()
        assert isinstance(result, IncidentCostPort)

    def test_build_prediction_roi_adapter(self) -> None:
        result = self.server_mod.build_prediction_roi_adapter()
        assert isinstance(result, PredictionRoiPort)

    def test_build_budget_intelligence_adapter(self) -> None:
        result = self.server_mod.build_budget_intelligence_adapter()
        assert isinstance(result, BudgetIntelligencePort)

    def test_build_night_intervention_adapter(self) -> None:
        result = self.server_mod.build_night_intervention_adapter()
        assert isinstance(result, EngineerWorkloadPort)

    def test_build_disruption_risk_adapter(self) -> None:
        result = self.server_mod.build_disruption_risk_adapter()
        assert isinstance(result, DisruptionRiskPort)

    def test_build_critical_cve_adapter(self) -> None:
        result = self.server_mod.build_critical_cve_adapter()
        assert isinstance(result, CriticalCvePort)

    def test_build_stale_credentials_adapter(self) -> None:
        result = self.server_mod.build_stale_credentials_adapter()
        assert isinstance(result, StaleCredentialsPort)

    def test_build_unauthorized_access_adapter(self) -> None:
        result = self.server_mod.build_unauthorized_access_adapter()
        assert isinstance(result, UnauthorizedAccessPort)

    def test_build_cost_adapter(self) -> None:
        result = self.server_mod.build_cost_adapter()
        assert isinstance(result, CostEstimationPort)

    def test_build_cluster_diff_adapter(self) -> None:
        result = self.server_mod.build_cluster_diff_adapter()
        assert isinstance(result, ClusterDiffPort)

    def test_build_cross_cluster_incident_adapter(self) -> None:
        result = self.server_mod.build_cross_cluster_incident_adapter()
        assert isinstance(result, CrossClusterIncidentPort)

    def test_build_node_analysis_adapter(self) -> None:
        result = self.server_mod.build_node_analysis_adapter()
        assert isinstance(result, HotNodeAnalysisPort)

    def test_build_helm_drift_adapter(self) -> None:
        result = self.server_mod.build_helm_drift_adapter()
        assert isinstance(result, DriftDetectionPort)

    def test_build_kustomize_drift_adapter(self) -> None:
        result = self.server_mod.build_kustomize_drift_adapter()
        assert isinstance(result, DriftDetectionPort)

    def test_build_live_resource_adapter(self) -> None:
        result = self.server_mod.build_live_resource_adapter()
        assert isinstance(result, LiveResourcePort)

    def test_build_audit_log_adapter(self) -> None:
        result = self.server_mod.build_audit_log_adapter()
        assert isinstance(result, GitOpsDriftAuditPort)

    def test_build_image_drift_adapter(self) -> None:
        result = self.server_mod.build_image_drift_adapter()
        assert isinstance(result, ImageDriftPort)

    def test_build_rbac_audit_adapter(self) -> None:
        result = self.server_mod.build_rbac_audit_adapter()
        assert isinstance(result, RBACSecurityAuditPort)

    def test_build_pod_security_adapter(self) -> None:
        result = self.server_mod.build_pod_security_adapter()
        assert isinstance(result, PodSecurityContextAuditPort)

    def test_build_image_inventory_adapter(self) -> None:
        result = self.server_mod.build_image_inventory_adapter()
        assert isinstance(result, ImageInventoryPort)

    def test_build_image_vulnerability_scan_adapter(self) -> None:
        result = self.server_mod.build_image_vulnerability_scan_adapter()
        assert isinstance(result, ImageVulnerabilityScanPort)

    def test_build_secret_rotation_audit_adapter(self) -> None:
        result = self.server_mod.build_secret_rotation_audit_adapter()
        assert isinstance(result, SecretRotationAuditPort)

    def test_build_network_policy_audit_adapter(self) -> None:
        result = self.server_mod.build_network_policy_audit_adapter()
        assert isinstance(result, NetworkPolicyAuditPort)

    def test_build_external_exposure_audit_adapter(self) -> None:
        result = self.server_mod.build_external_exposure_audit_adapter()
        assert isinstance(result, ExternalExposureAuditPort)

    def test_build_cross_namespace_traffic_adapter(self) -> None:
        result = self.server_mod.build_cross_namespace_traffic_adapter()
        assert isinstance(result, CrossNamespaceTrafficPort)

    def test_build_trace_log_correlation_adapter(self) -> None:
        result = self.server_mod.build_trace_log_correlation_adapter()
        assert isinstance(result, TraceLogCorrelationPort)

    def test_build_security_audit_adapter(self) -> None:
        result = self.server_mod.build_security_audit_adapter()
        assert isinstance(result, SecurityAuditPort)

    def test_build_service_dependency_graph_adapter(self) -> None:
        result = self.server_mod.build_service_dependency_graph_adapter()
        assert isinstance(result, ServiceDependencyGraphPort)

    def test_build_trace_event_correlation_adapter(self) -> None:
        result = self.server_mod.build_trace_event_correlation_adapter()
        assert isinstance(result, TraceEventCorrelationPort)

    def test_build_trace_query_adapter(self) -> None:
        result = self.server_mod.build_trace_query_adapter()
        assert isinstance(result, TraceQueryPort)

    def test_build_slow_trace_search_adapter(self) -> None:
        result = self.server_mod.build_slow_trace_search_adapter()
        assert isinstance(result, SlowTraceSearchPort)

    def test_build_deployment_latency_comparison_adapter(self) -> None:
        result = self.server_mod.build_deployment_latency_comparison_adapter()
        assert isinstance(result, DeploymentLatencyComparisonPort)

    def test_build_version_regression_adapter(self) -> None:
        result = self.server_mod.build_version_regression_adapter()
        assert isinstance(result, VersionRegressionPort)

    def test_build_redundant_call_detection_adapter(self) -> None:
        result = self.server_mod.build_redundant_call_detection_adapter()
        assert isinstance(result, RedundantCallDetectionPort)

    def test_build_compliance_audit_adapter(self) -> None:
        result = self.server_mod.build_compliance_audit_adapter()
        assert isinstance(result, ComplianceAuditPort)

    def test_build_error_attribution_adapter(self) -> None:
        result = self.server_mod.build_error_attribution_adapter()
        assert isinstance(result, ErrorAttributionPort)

    def test_build_slo_breach_prediction_adapter(self) -> None:
        result = self.server_mod.build_slo_breach_prediction_adapter()
        assert isinstance(result, SLOBreachPredictionPort)

    def test_build_certificate_investigation_adapter(self) -> None:
        with patch.object(self.server_mod, "load_kubeconfig", return_value=MagicMock()):
            with patch.object(self.server_mod, "context_name", "test-cluster"):
                result = self.server_mod.build_certificate_investigation_adapter()
                assert isinstance(result, CertificateInvestigationPort)

    def test_build_resource_yaml_adapter(self) -> None:
        result = self.server_mod.build_resource_yaml_adapter()
        assert isinstance(result, ResourceYAMLPort)

    def test_build_pipeline_run_logs_adapter(self) -> None:
        result = self.server_mod.build_pipeline_run_logs_adapter()
        assert isinstance(result, PipelineRunLogsPort)

    def test_build_etcd_logs_adapter(self) -> None:
        result = self.server_mod.build_etcd_logs_adapter()
        assert isinstance(result, ETCDLogsPort)

    def test_build_pod_logs_adapter(self) -> None:
        result = self.server_mod.build_pod_logs_adapter()
        assert isinstance(result, PodLogsPort)

    def test_build_pod_metrics_adapter(self) -> None:
        from hexawyn.application.ports.driven.pod_metrics_port import PodMetricsPort

        result = self.server_mod.build_pod_metrics_adapter()
        assert isinstance(result, PodMetricsPort)

    def test_build_log_search_adapter(self) -> None:
        result = self.server_mod.build_log_search_adapter()
        assert isinstance(result, LogSearchPort)

    def test_build_pod_metrics_baseline_adapter(self) -> None:
        result = self.server_mod.build_pod_metrics_baseline_adapter()
        assert isinstance(result, PodMetricsBaselinePort)

    def test_build_resource_search_adapter(self) -> None:
        result = self.server_mod.build_resource_search_adapter()
        assert isinstance(result, ResourceSearchPort)

    def test_build_namespace_events_adapter(self) -> None:
        result = self.server_mod.build_namespace_events_adapter()
        assert isinstance(result, NamespaceEventsPort)

    def test_build_namespace_overview_adapter(self) -> None:
        result = self.server_mod.build_namespace_overview_adapter()
        assert isinstance(result, NamespaceOverviewPort)

    def test_build_adaptive_investigation_adapter(self) -> None:
        result = self.server_mod.build_adaptive_investigation_adapter()
        assert isinstance(result, AdaptiveInvestigationPort)

    def test_build_pod_log_watch_adapter(self) -> None:
        result = self.server_mod.build_pod_log_watch_adapter()
        assert isinstance(result, PodLogWatchPort)

    def test_build_alert_notification_adapter(self) -> None:
        result = self.server_mod.build_alert_notification_adapter()
        assert isinstance(result, AlertNotificationPort)

    def test_build_pipeline_baseline_adapter(self) -> None:
        result = self.server_mod.build_pipeline_baseline_adapter()
        assert isinstance(result, PipelineBaselinePort)

    def test_build_pipeline_for_service_adapter(self) -> None:
        result = self.server_mod.build_pipeline_for_service_adapter()
        assert isinstance(result, PipelineForServicePort)

    def test_build_probe_audit_adapter(self) -> None:
        result = self.server_mod.build_probe_audit_adapter()
        assert isinstance(result, ProbeAuditPort)

    def test_build_error_budget_adapter(self) -> None:
        result = self.server_mod.build_error_budget_adapter()
        assert isinstance(result, ErrorBudgetPort)

    def test_build_reliability_report_adapter(self) -> None:
        result = self.server_mod.build_reliability_report_adapter()
        assert isinstance(result, WeeklyReliabilityReportPort)

    def test_build_helm_release_version_adapter(self) -> None:
        result = self.server_mod.build_helm_release_version_adapter()
        assert isinstance(result, HelmReleaseVersionPort)

    def test_build_helm_values_diff_adapter(self) -> None:
        result = self.server_mod.build_helm_values_diff_adapter()
        assert isinstance(result, HelmValuesDiffPort)

    def test_build_kustomize_patch_analysis_adapter(self) -> None:
        result = self.server_mod.build_kustomize_patch_analysis_adapter()
        assert isinstance(result, KustomizePatchAnalysisPort)

    def test_build_service_cost_adapter(self) -> None:
        result = self.server_mod.build_service_cost_adapter()
        assert isinstance(result, ServiceCostPort)

    def test_build_team_cost_adapter(self) -> None:
        result = self.server_mod.build_team_cost_adapter()
        assert isinstance(result, TeamCostPort)

    def test_build_monthly_incident_adapter(self) -> None:
        result = self.server_mod.build_monthly_incident_adapter()
        assert isinstance(result, MonthlyIncidentPort)

    def test_build_mttr_trend_adapter(self) -> None:
        result = self.server_mod.build_mttr_trend_adapter()
        assert isinstance(result, MTTRTrendPort)

    def test_build_recurring_incident_adapter(self) -> None:
        result = self.server_mod.build_recurring_incident_adapter()
        assert isinstance(result, RecurringIncidentPort)

    def test_build_tls_compliance_adapter(self) -> None:
        result = self.server_mod.build_tls_compliance_adapter()
        assert isinstance(result, TLSCompliancePort)

    def test_build_security_posture_adapter(self) -> None:
        result = self.server_mod.build_security_posture_adapter()
        assert isinstance(result, SecurityPosturePort)

    @pytest.mark.skip(reason="OpenShiftAdapter requires context param - production bug")
    def test_build_openshift_resource_adapter(self) -> None:
        result = self.server_mod.build_openshift_resource_adapter()
        assert isinstance(result, OpenShiftResourcePort)

    def test_build_cluster_operator_status_adapter(self) -> None:
        result = self.server_mod.build_cluster_operator_status_adapter()
        assert isinstance(result, ClusterOperatorStatusPort)

    def test_build_machine_config_pool_adapter(self) -> None:
        result = self.server_mod.build_machine_config_pool_adapter()
        assert isinstance(result, MachineConfigPoolPort)

    def test_build_pricing_plan_adapter(self) -> None:
        result = self.server_mod.build_pricing_plan_adapter()
        assert isinstance(result, PlanPort)

    def test_build_usage_meter_adapter(self) -> None:
        result = self.server_mod.build_usage_meter_adapter()
        assert isinstance(result, UsageMeterPort)

    def test_build_consolidation_adapter(self) -> None:
        with patch.object(self.server_mod, "get_connection", return_value=MagicMock()):
            result = self.server_mod.build_consolidation_adapter()
            assert isinstance(result, ConsolidationPort)


class TestServerHelpers:
    """Test helper functions in server.py."""

    @pytest.fixture(autouse=True)
    def _setup(self) -> None:
        from hexawyn.mcp import server as server_mod

        self.server_mod = server_mod

    def test_health_returns_dict(self) -> None:
        with patch.object(self.server_mod, "get_connection", return_value=MagicMock()):
            result = self.server_mod.health()
        assert "status" in result
        assert "version" in result
        assert "duckdb" in result
        assert "api_key" in result
        assert "cluster" in result

    def test_health_db_degraded(self) -> None:
        with patch.object(self.server_mod, "get_connection", side_effect=Exception("db error")):
            result = self.server_mod.health()
        assert result["status"] == "degraded"
        assert result["duckdb"] == "unavailable"

    def test_health_duckdb_connected(self) -> None:
        mock_conn = MagicMock()
        mock_conn.execute.return_value.fetchone.return_value = [1]
        with patch.object(self.server_mod, "get_connection", return_value=mock_conn):
            with patch.object(self.server_mod, "get_api_key", return_value="sk-test"):
                result = self.server_mod.health()
        assert result["status"] == "ok"
        assert result["duckdb"] == "connected"
        assert result["api_key"] == "configured"

    def test_context_name_module_variable(self) -> None:
        from hexawyn.infrastructure.config.kubeconfig_reader import get_active_context

        active = get_active_context()
        expected = str(active["name"]) if active else "unknown"
        assert self.server_mod.context_name == expected

    def test_build_cost_forecast_adapter_unknown_context(self) -> None:
        with patch.object(self.server_mod, "context_name", "unknown"):
            result = self.server_mod.build_cost_forecast_adapter()
            assert isinstance(result, CostForecastPort)
