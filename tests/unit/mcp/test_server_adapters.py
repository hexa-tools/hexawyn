"""Unit tests for all build_*_adapter() factories in mcp/server.py.

Per AGENTS.md: every build_*_adapter() MUST have a corresponding test.
"""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestMCPServerAdapterFactories:
    def test_build_k8s_adapter_returns_k8sport(self) -> None:
        from hexawyn.application.ports.driven.k8s_port import K8sPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_k8s_adapter

            result = build_k8s_adapter()

            assert isinstance(result, K8sPort)

    def test_build_tekton_adapter_returns_tektonport(self) -> None:
        from hexawyn.application.ports.driven.tekton_port import TektonPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_tekton_adapter

            result = build_tekton_adapter()

            assert isinstance(result, TektonPort)

    def test_build_rightsizing_adapter_returns_rightsizingport(self) -> None:
        from hexawyn.application.ports.driven.rightsizing_port import RightsizingPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_rightsizing_adapter

            result = build_rightsizing_adapter()

            assert isinstance(result, RightsizingPort)

    def test_build_what_if_simulation_adapter_returns_whatifsimulationport(self) -> None:
        from hexawyn.application.ports.driven.what_if_simulation_port import WhatIfSimulationPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_what_if_simulation_adapter

            result = build_what_if_simulation_adapter()

            assert isinstance(result, WhatIfSimulationPort)

    def test_build_cost_forecast_adapter_returns_costforecastport(self) -> None:
        from hexawyn.application.ports.driven.cost_forecast_port import CostForecastPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_cost_forecast_adapter

            result = build_cost_forecast_adapter()

            assert isinstance(result, CostForecastPort)

    def test_build_budget_projection_adapter_returns_budgetprojectionport(self) -> None:
        from hexawyn.application.ports.driven.budget_projection_port import BudgetProjectionPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_budget_projection_adapter

            result = build_budget_projection_adapter()

            assert isinstance(result, BudgetProjectionPort)

    def test_build_waste_adapter_returns_namespacewasteanalysisport(self) -> None:
        from hexawyn.application.ports.driven.namespace_waste_port import NamespaceWasteAnalysisPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_waste_adapter

            result = build_waste_adapter()

            assert isinstance(result, NamespaceWasteAnalysisPort)

    def test_build_zombie_detection_adapter_returns_zombiedetectionport(self) -> None:
        from hexawyn.application.ports.driven.zombie_detection_port import ZombieDetectionPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_zombie_detection_adapter

            result = build_zombie_detection_adapter()

            assert isinstance(result, ZombieDetectionPort)

    def test_build_cost_saving_adapter_returns_costsavingestimationport(self) -> None:
        from hexawyn.application.ports.driven.cost_saving_estimation_port import (
            CostSavingEstimationPort,
        )

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_cost_saving_adapter

            result = build_cost_saving_adapter()

            assert isinstance(result, CostSavingEstimationPort)

    def test_build_fleet_health_adapter_returns_fleethealthport(self) -> None:
        from hexawyn.application.ports.driven.fleet_health_port import FleetHealthPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_fleet_health_adapter

            result = build_fleet_health_adapter()

            assert isinstance(result, FleetHealthPort)

    def test_build_kubernetes_topology_adapter_returns_kubernetestopologyport(self) -> None:
        from hexawyn.application.ports.driven.kubernetes_topology_port import KubernetesTopologyPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_kubernetes_topology_adapter

            result = build_kubernetes_topology_adapter()

            assert isinstance(result, KubernetesTopologyPort)

    def test_build_istio_topology_adapter_returns_istiotopologyport(self) -> None:
        from hexawyn.application.ports.driven.istio_topology_port import IstioTopologyPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_istio_topology_adapter

            result = build_istio_topology_adapter()

            assert isinstance(result, IstioTopologyPort)

    def test_build_gitops_adapter_returns_gitopsport(self) -> None:
        from hexawyn.application.ports.driven.gitops_port import GitOpsPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_gitops_adapter

            result = build_gitops_adapter()

            assert isinstance(result, GitOpsPort)

    def test_build_topology_snapshot_adapter_returns_topologysnapshotport(self) -> None:
        from hexawyn.application.ports.driven.topology_snapshot_port import TopologySnapshotPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_topology_snapshot_adapter

            result = build_topology_snapshot_adapter()

            assert isinstance(result, TopologySnapshotPort)

    def test_build_incident_memory_adapter_returns_incidentmemoryport(self) -> None:
        from hexawyn.application.ports.driven.incident_memory_port import IncidentMemoryPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_incident_memory_adapter

            result = build_incident_memory_adapter()

            assert isinstance(result, IncidentMemoryPort)

    def test_build_rollouts_adapter_returns_rolloutsport(self) -> None:
        from hexawyn.application.ports.driven.rollouts_port import RolloutsPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_rollouts_adapter

            result = build_rollouts_adapter()

            assert isinstance(result, RolloutsPort)

    def test_build_policy_adapter_returns_policyport(self) -> None:
        from hexawyn.application.ports.driven.policy_port import PolicyPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_policy_adapter

            result = build_policy_adapter()

            assert isinstance(result, PolicyPort)

    def test_build_cert_manager_adapter_returns_certmanagerport(self) -> None:
        from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_cert_manager_adapter

            result = build_cert_manager_adapter()

            assert isinstance(result, CertManagerPort)

    def test_build_keda_adapter_returns_kedaport(self) -> None:
        from hexawyn.application.ports.driven.keda_port import KedaPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_keda_adapter

            result = build_keda_adapter()

            assert isinstance(result, KedaPort)

    def test_build_canary_comparison_adapter_returns_canarycomparisonport(self) -> None:
        from hexawyn.application.ports.driven.canary_comparison_port import CanaryComparisonPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_canary_comparison_adapter

            result = build_canary_comparison_adapter()

            assert isinstance(result, CanaryComparisonPort)

    def test_build_cost_profiling_adapter_returns_costprofilingport(self) -> None:
        from hexawyn.application.ports.driven.cost_profiling_port import CostProfilingPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_cost_profiling_adapter

            result = build_cost_profiling_adapter()

            assert isinstance(result, CostProfilingPort)

    def test_build_memory_saturation_adapter_returns_memorysaturationport(self) -> None:
        from hexawyn.application.ports.driven.memory_saturation_port import MemorySaturationPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_memory_saturation_adapter

            result = build_memory_saturation_adapter()

            assert isinstance(result, MemorySaturationPort)

    def test_build_span_bottleneck_adapter_returns_spanbottleneckport(self) -> None:
        from hexawyn.application.ports.driven.span_bottleneck_port import SpanBottleneckPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_span_bottleneck_adapter

            result = build_span_bottleneck_adapter()

            assert isinstance(result, SpanBottleneckPort)

    def test_build_latency_percentile_adapter_returns_latencypercentileport(self) -> None:
        from hexawyn.application.ports.driven.latency_percentile_port import LatencyPercentilePort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_latency_percentile_adapter

            result = build_latency_percentile_adapter()

            assert isinstance(result, LatencyPercentilePort)

    def test_build_metric_correlation_adapter_returns_metriccorrelationport(self) -> None:
        from hexawyn.application.ports.driven.metric_correlation_port import MetricCorrelationPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_metric_correlation_adapter

            result = build_metric_correlation_adapter()

            assert isinstance(result, MetricCorrelationPort)

    def test_build_metrics_query_adapter_returns_metricsqueryport(self) -> None:
        from hexawyn.application.ports.driven.metrics_query_port import MetricsQueryPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_metrics_query_adapter

            result = build_metrics_query_adapter()

            assert isinstance(result, MetricsQueryPort)

    def test_build_cluster_resource_metrics_adapter_returns_clusterresourcemetricsport(
        self,
    ) -> None:
        from hexawyn.application.ports.driven.cluster_resource_metrics_port import (
            ClusterResourceMetricsPort,
        )

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_cluster_resource_metrics_adapter

            result = build_cluster_resource_metrics_adapter()

            assert isinstance(result, ClusterResourceMetricsPort)

    def test_build_capacity_forecast_adapter_returns_capacityforecastport(self) -> None:
        from hexawyn.application.ports.driven.capacity_forecast_port import CapacityForecastPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_capacity_forecast_adapter

            result = build_capacity_forecast_adapter()

            assert isinstance(result, CapacityForecastPort)

    def test_build_headroom_simulation_adapter_returns_headroomsimulationport(self) -> None:
        from hexawyn.application.ports.driven.headroom_simulation_port import HeadroomSimulationPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_headroom_simulation_adapter

            result = build_headroom_simulation_adapter()

            assert isinstance(result, HeadroomSimulationPort)

    def test_build_spike_provisioning_adapter_returns_spikeprovisioningport(self) -> None:
        from hexawyn.application.ports.driven.spike_provisioning_port import SpikeProvisioningPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_spike_provisioning_adapter

            result = build_spike_provisioning_adapter()

            assert isinstance(result, SpikeProvisioningPort)

    def test_build_optimization_roi_adapter_returns_optimizationroiport(self) -> None:
        from hexawyn.application.ports.driven.optimization_roi_port import OptimizationRoiPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_optimization_roi_adapter

            result = build_optimization_roi_adapter()

            assert isinstance(result, OptimizationRoiPort)

    def test_build_sla_report_adapter_returns_slareportport(self) -> None:
        from hexawyn.application.ports.driven.sla_report_port import SlaReportPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_sla_report_adapter

            result = build_sla_report_adapter()

            assert isinstance(result, SlaReportPort)

    def test_build_platform_reliability_adapter_returns_platformreliabilityport(self) -> None:
        from hexawyn.application.ports.driven.platform_reliability_port import (
            PlatformReliabilityPort,
        )

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_platform_reliability_adapter

            result = build_platform_reliability_adapter()

            assert isinstance(result, PlatformReliabilityPort)

    def test_build_incident_cost_adapter_returns_incidentcostport(self) -> None:
        from hexawyn.application.ports.driven.incident_cost_port import IncidentCostPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_incident_cost_adapter

            result = build_incident_cost_adapter()

            assert isinstance(result, IncidentCostPort)

    def test_build_prediction_roi_adapter_returns_predictionroiport(self) -> None:
        from hexawyn.application.ports.driven.prediction_roi_port import PredictionRoiPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_prediction_roi_adapter

            result = build_prediction_roi_adapter()

            assert isinstance(result, PredictionRoiPort)

    def test_build_budget_intelligence_adapter_returns_budgetintelligenceport(self) -> None:
        from hexawyn.application.ports.driven.budget_intelligence_port import BudgetIntelligencePort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_budget_intelligence_adapter

            result = build_budget_intelligence_adapter()

            assert isinstance(result, BudgetIntelligencePort)

    def test_build_night_intervention_adapter_returns_engineerworkloadport(self) -> None:
        from hexawyn.application.ports.driven.engineer_workload_port import EngineerWorkloadPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_night_intervention_adapter

            result = build_night_intervention_adapter()

            assert isinstance(result, EngineerWorkloadPort)

    def test_build_disruption_risk_adapter_returns_disruptionriskport(self) -> None:
        from hexawyn.application.ports.driven.disruption_risk_port import DisruptionRiskPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_disruption_risk_adapter

            result = build_disruption_risk_adapter()

            assert isinstance(result, DisruptionRiskPort)

    def test_build_critical_cve_adapter_returns_criticalcveport(self) -> None:
        from hexawyn.application.ports.driven.critical_cve_port import CriticalCvePort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_critical_cve_adapter

            result = build_critical_cve_adapter()

            assert isinstance(result, CriticalCvePort)

    def test_build_stale_credentials_adapter_returns_stalecredentialsport(self) -> None:
        from hexawyn.application.ports.driven.stale_credentials_port import StaleCredentialsPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_stale_credentials_adapter

            result = build_stale_credentials_adapter()

            assert isinstance(result, StaleCredentialsPort)

    def test_build_unauthorized_access_adapter_returns_unauthorizedaccessport(self) -> None:
        from hexawyn.application.ports.driven.unauthorized_access_port import UnauthorizedAccessPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_unauthorized_access_adapter

            result = build_unauthorized_access_adapter()

            assert isinstance(result, UnauthorizedAccessPort)

    def test_build_cost_adapter_returns_costestimationport(self) -> None:
        from hexawyn.application.ports.driven.cost_estimation_port import CostEstimationPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_cost_adapter

            result = build_cost_adapter()

            assert isinstance(result, CostEstimationPort)

    def test_build_cluster_diff_adapter_returns_clusterdiffport(self) -> None:
        from hexawyn.application.ports.driven.cluster_diff_port import ClusterDiffPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_cluster_diff_adapter

            result = build_cluster_diff_adapter()

            assert isinstance(result, ClusterDiffPort)

    def test_build_cross_cluster_incident_adapter_returns_crossclusterincidentport(self) -> None:
        from hexawyn.application.ports.driven.cross_cluster_incident_port import (
            CrossClusterIncidentPort,
        )

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_cross_cluster_incident_adapter

            result = build_cross_cluster_incident_adapter()

            assert isinstance(result, CrossClusterIncidentPort)

    def test_build_node_analysis_adapter_returns_hotnodeanalysisport(self) -> None:
        from hexawyn.application.ports.driven.hot_node_analysis_port import HotNodeAnalysisPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_node_analysis_adapter

            result = build_node_analysis_adapter()

            assert isinstance(result, HotNodeAnalysisPort)

    def test_build_helm_drift_adapter_returns_driftdetectionport(self) -> None:
        from hexawyn.application.ports.driven.drift_detection_port import DriftDetectionPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_helm_drift_adapter

            result = build_helm_drift_adapter()

            assert isinstance(result, DriftDetectionPort)

    def test_build_kustomize_drift_adapter_returns_driftdetectionport(self) -> None:
        from hexawyn.application.ports.driven.drift_detection_port import DriftDetectionPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_kustomize_drift_adapter

            result = build_kustomize_drift_adapter()

            assert isinstance(result, DriftDetectionPort)

    def test_build_live_resource_adapter_returns_liveresourceport(self) -> None:
        from hexawyn.application.ports.driven.live_resource_port import LiveResourcePort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_live_resource_adapter

            result = build_live_resource_adapter()

            assert isinstance(result, LiveResourcePort)

    def test_build_audit_log_adapter_returns_gitopsdriftauditport(self) -> None:
        from hexawyn.application.ports.driven.gitops_drift_audit_port import GitOpsDriftAuditPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_audit_log_adapter

            result = build_audit_log_adapter()

            assert isinstance(result, GitOpsDriftAuditPort)

    def test_build_image_drift_adapter_returns_imagedriftport(self) -> None:
        from hexawyn.application.ports.driven.image_drift_port import ImageDriftPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_image_drift_adapter

            result = build_image_drift_adapter()

            assert isinstance(result, ImageDriftPort)

    def test_build_rbac_audit_adapter_returns_rbacsecurityauditport(self) -> None:
        from hexawyn.application.ports.driven.rbac_security_audit_port import RBACSecurityAuditPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_rbac_audit_adapter

            result = build_rbac_audit_adapter()

            assert isinstance(result, RBACSecurityAuditPort)

    def test_build_pod_security_adapter_returns_podsecuritycontextauditport(self) -> None:
        from hexawyn.application.ports.driven.pod_security_context_audit_port import (
            PodSecurityContextAuditPort,
        )

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_pod_security_adapter

            result = build_pod_security_adapter()

            assert isinstance(result, PodSecurityContextAuditPort)

    def test_build_image_inventory_adapter_returns_imageinventoryport(self) -> None:
        from hexawyn.application.ports.driven.image_inventory_port import ImageInventoryPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_image_inventory_adapter

            result = build_image_inventory_adapter()

            assert isinstance(result, ImageInventoryPort)

    def test_build_image_vulnerability_scan_adapter_returns_imagevulnerabilityscanport(
        self,
    ) -> None:
        from hexawyn.application.ports.driven.image_vulnerability_scan_port import (
            ImageVulnerabilityScanPort,
        )

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_image_vulnerability_scan_adapter

            result = build_image_vulnerability_scan_adapter()

            assert isinstance(result, ImageVulnerabilityScanPort)

    def test_build_secret_rotation_audit_adapter_returns_secretrotationauditport(self) -> None:
        from hexawyn.application.ports.driven.secret_rotation_audit_port import (
            SecretRotationAuditPort,
        )

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_secret_rotation_audit_adapter

            result = build_secret_rotation_audit_adapter()

            assert isinstance(result, SecretRotationAuditPort)

    def test_build_network_policy_audit_adapter_returns_networkpolicyauditport(self) -> None:
        from hexawyn.application.ports.driven.network_policy_audit_port import (
            NetworkPolicyAuditPort,
        )

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_network_policy_audit_adapter

            result = build_network_policy_audit_adapter()

            assert isinstance(result, NetworkPolicyAuditPort)

    def test_build_external_exposure_audit_adapter_returns_externalexposureauditport(self) -> None:
        from hexawyn.application.ports.driven.external_exposure_audit_port import (
            ExternalExposureAuditPort,
        )

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_external_exposure_audit_adapter

            result = build_external_exposure_audit_adapter()

            assert isinstance(result, ExternalExposureAuditPort)

    def test_build_cross_namespace_traffic_adapter_returns_crossnamespacetrafficport(self) -> None:
        from hexawyn.application.ports.driven.cross_namespace_traffic_port import (
            CrossNamespaceTrafficPort,
        )

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_cross_namespace_traffic_adapter

            result = build_cross_namespace_traffic_adapter()

            assert isinstance(result, CrossNamespaceTrafficPort)

    def test_build_trace_log_correlation_adapter_returns_tracelogcorrelationport(self) -> None:
        from hexawyn.application.ports.driven.trace_log_correlation_port import (
            TraceLogCorrelationPort,
        )

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_trace_log_correlation_adapter

            result = build_trace_log_correlation_adapter()

            assert isinstance(result, TraceLogCorrelationPort)

    def test_build_security_audit_adapter_returns_securityauditport(self) -> None:
        from hexawyn.application.ports.driven.security_audit_port import SecurityAuditPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_security_audit_adapter

            result = build_security_audit_adapter()

            assert isinstance(result, SecurityAuditPort)

    def test_build_service_dependency_graph_adapter_returns_servicedependencygraphport(
        self,
    ) -> None:
        from hexawyn.application.ports.driven.service_dependency_graph_port import (
            ServiceDependencyGraphPort,
        )

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_service_dependency_graph_adapter

            result = build_service_dependency_graph_adapter()

            assert isinstance(result, ServiceDependencyGraphPort)

    def test_build_trace_event_correlation_adapter_returns_traceeventcorrelationport(self) -> None:
        from hexawyn.application.ports.driven.trace_event_correlation_port import (
            TraceEventCorrelationPort,
        )

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_trace_event_correlation_adapter

            result = build_trace_event_correlation_adapter()

            assert isinstance(result, TraceEventCorrelationPort)

    def test_build_trace_query_adapter_returns_tracequeryport(self) -> None:
        from hexawyn.application.ports.driven.trace_query_port import TraceQueryPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_trace_query_adapter

            result = build_trace_query_adapter()

            assert isinstance(result, TraceQueryPort)

    def test_build_slow_trace_search_adapter_returns_slowtracesearchport(self) -> None:
        from hexawyn.application.ports.driven.slow_trace_search_port import SlowTraceSearchPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_slow_trace_search_adapter

            result = build_slow_trace_search_adapter()

            assert isinstance(result, SlowTraceSearchPort)

    def test_build_deployment_latency_comparison_adapter_returns_deploymentlatencycomparisonport(
        self,
    ) -> None:
        from hexawyn.application.ports.driven.deployment_latency_comparison_port import (
            DeploymentLatencyComparisonPort,
        )

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_deployment_latency_comparison_adapter

            result = build_deployment_latency_comparison_adapter()

            assert isinstance(result, DeploymentLatencyComparisonPort)

    def test_build_version_regression_adapter_returns_versionregressionport(self) -> None:
        from hexawyn.application.ports.driven.version_regression_port import VersionRegressionPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_version_regression_adapter

            result = build_version_regression_adapter()

            assert isinstance(result, VersionRegressionPort)

    def test_build_redundant_call_detection_adapter_returns_redundantcalldetectionport(
        self,
    ) -> None:
        from hexawyn.application.ports.driven.redundant_call_detection_port import (
            RedundantCallDetectionPort,
        )

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_redundant_call_detection_adapter

            result = build_redundant_call_detection_adapter()

            assert isinstance(result, RedundantCallDetectionPort)

    def test_build_compliance_audit_adapter_returns_complianceauditport(self) -> None:
        from hexawyn.application.ports.driven.compliance_audit_port import ComplianceAuditPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_compliance_audit_adapter

            result = build_compliance_audit_adapter()

            assert isinstance(result, ComplianceAuditPort)

    def test_build_error_attribution_adapter_returns_errorattributionport(self) -> None:
        from hexawyn.application.ports.driven.error_attribution_port import ErrorAttributionPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_error_attribution_adapter

            result = build_error_attribution_adapter()

            assert isinstance(result, ErrorAttributionPort)

    def test_build_slo_breach_prediction_adapter_returns_slobreachpredictionport(self) -> None:
        from hexawyn.application.ports.driven.slo_breach_prediction_port import (
            SLOBreachPredictionPort,
        )

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_slo_breach_prediction_adapter

            result = build_slo_breach_prediction_adapter()

            assert isinstance(result, SLOBreachPredictionPort)

    def test_build_certificate_investigation_adapter_returns_certificateinvestigationport(
        self,
    ) -> None:
        from hexawyn.application.ports.driven.certificate_investigation_port import (
            CertificateInvestigationPort,
        )

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_certificate_investigation_adapter

            result = build_certificate_investigation_adapter()

            assert isinstance(result, CertificateInvestigationPort)

    def test_build_resource_yaml_adapter_returns_resourceyamlport(self) -> None:
        from hexawyn.application.ports.driven.resource_yaml_port import ResourceYAMLPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_resource_yaml_adapter

            result = build_resource_yaml_adapter()

            assert isinstance(result, ResourceYAMLPort)

    def test_build_pipeline_run_logs_adapter_returns_pipelinerunlogsport(self) -> None:
        from hexawyn.application.ports.driven.pipeline_run_logs_port import PipelineRunLogsPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_pipeline_run_logs_adapter

            result = build_pipeline_run_logs_adapter()

            assert isinstance(result, PipelineRunLogsPort)

    def test_build_etcd_logs_adapter_returns_etcdlogsport(self) -> None:
        from hexawyn.application.ports.driven.etcd_logs_port import ETCDLogsPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_etcd_logs_adapter

            result = build_etcd_logs_adapter()

            assert isinstance(result, ETCDLogsPort)

    def test_build_pod_logs_adapter_returns_podlogsport(self) -> None:
        from hexawyn.application.ports.driven.pod_logs_port import PodLogsPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_pod_logs_adapter

            result = build_pod_logs_adapter()

            assert isinstance(result, PodLogsPort)

    def test_build_log_search_adapter_returns_logsearchport(self) -> None:
        from hexawyn.application.ports.driven.log_search_port import LogSearchPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_log_search_adapter

            result = build_log_search_adapter()

            assert isinstance(result, LogSearchPort)

    def test_build_pod_metrics_baseline_adapter_returns_podmetricsbaselineport(self) -> None:
        from hexawyn.application.ports.driven.pod_metrics_baseline_port import (
            PodMetricsBaselinePort,
        )

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_pod_metrics_baseline_adapter

            result = build_pod_metrics_baseline_adapter()

            assert isinstance(result, PodMetricsBaselinePort)

    def test_build_resource_search_adapter_returns_resourcesearchport(self) -> None:
        from hexawyn.application.ports.driven.resource_search_port import ResourceSearchPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_resource_search_adapter

            result = build_resource_search_adapter()

            assert isinstance(result, ResourceSearchPort)

    def test_build_namespace_events_adapter_returns_namespaceeventsport(self) -> None:
        from hexawyn.application.ports.driven.namespace_events_port import NamespaceEventsPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_namespace_events_adapter

            result = build_namespace_events_adapter()

            assert isinstance(result, NamespaceEventsPort)

    def test_build_namespace_overview_adapter_returns_namespaceoverviewport(self) -> None:
        from hexawyn.application.ports.driven.namespace_overview_port import NamespaceOverviewPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_namespace_overview_adapter

            result = build_namespace_overview_adapter()

            assert isinstance(result, NamespaceOverviewPort)

    def test_build_adaptive_investigation_adapter_returns_adaptiveinvestigationport(self) -> None:
        from hexawyn.application.ports.driven.adaptive_investigation_port import (
            AdaptiveInvestigationPort,
        )

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_adaptive_investigation_adapter

            result = build_adaptive_investigation_adapter()

            assert isinstance(result, AdaptiveInvestigationPort)

    def test_build_pod_log_watch_adapter_returns_podlogwatchport(self) -> None:
        from hexawyn.application.ports.driven.pod_log_watch_port import PodLogWatchPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_pod_log_watch_adapter

            result = build_pod_log_watch_adapter()

            assert isinstance(result, PodLogWatchPort)

    def test_build_alert_notification_adapter_returns_alertnotificationport(self) -> None:
        from hexawyn.application.ports.driven.alert_notification_port import AlertNotificationPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_alert_notification_adapter

            result = build_alert_notification_adapter()

            assert isinstance(result, AlertNotificationPort)

    def test_build_pipeline_for_service_adapter_returns_pipelineforserviceport(self) -> None:
        from hexawyn.application.ports.driven.pipeline_for_service_port import (
            PipelineForServicePort,
        )

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_pipeline_for_service_adapter

            result = build_pipeline_for_service_adapter()

            assert isinstance(result, PipelineForServicePort)

    def test_build_probe_audit_adapter_returns_probeauditport(self) -> None:
        from hexawyn.application.ports.driven.probe_audit_port import ProbeAuditPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_probe_audit_adapter

            result = build_probe_audit_adapter()

            assert isinstance(result, ProbeAuditPort)

    def test_build_error_budget_adapter_returns_errorbudgetport(self) -> None:
        from hexawyn.application.ports.driven.error_budget_port import ErrorBudgetPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_error_budget_adapter

            result = build_error_budget_adapter()

            assert isinstance(result, ErrorBudgetPort)

    def test_build_reliability_report_adapter_returns_weeklyreliabilityreportport(self) -> None:
        from hexawyn.application.ports.driven.weekly_reliability_report_port import (
            WeeklyReliabilityReportPort,
        )

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_reliability_report_adapter

            result = build_reliability_report_adapter()

            assert isinstance(result, WeeklyReliabilityReportPort)

    def test_build_helm_release_version_adapter_returns_helmreleaseversionport(self) -> None:
        from hexawyn.application.ports.driven.helm_release_version_port import (
            HelmReleaseVersionPort,
        )

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_helm_release_version_adapter

            result = build_helm_release_version_adapter()

            assert isinstance(result, HelmReleaseVersionPort)

    def test_build_helm_values_diff_adapter_returns_helmvaluesdiffport(self) -> None:
        from hexawyn.application.ports.driven.helm_values_diff_port import HelmValuesDiffPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_helm_values_diff_adapter

            result = build_helm_values_diff_adapter()

            assert isinstance(result, HelmValuesDiffPort)

    def test_build_kustomize_patch_analysis_adapter_returns_kustomizepatchanalysisport(
        self,
    ) -> None:
        from hexawyn.application.ports.driven.kustomize_patch_analysis_port import (
            KustomizePatchAnalysisPort,
        )

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_kustomize_patch_analysis_adapter

            result = build_kustomize_patch_analysis_adapter()

            assert isinstance(result, KustomizePatchAnalysisPort)

    def test_build_service_cost_adapter_returns_servicecostport(self) -> None:
        from hexawyn.application.ports.driven.service_cost_port import ServiceCostPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_service_cost_adapter

            result = build_service_cost_adapter()

            assert isinstance(result, ServiceCostPort)

    def test_build_team_cost_adapter_returns_teamcostport(self) -> None:
        from hexawyn.application.ports.driven.team_cost_port import TeamCostPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_team_cost_adapter

            result = build_team_cost_adapter()

            assert isinstance(result, TeamCostPort)

    def test_build_monthly_incident_adapter_returns_monthlyincidentport(self) -> None:
        from hexawyn.application.ports.driven.monthly_incident_port import MonthlyIncidentPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_monthly_incident_adapter

            result = build_monthly_incident_adapter()

            assert isinstance(result, MonthlyIncidentPort)

    def test_build_mttr_trend_adapter_returns_mttrtrendport(self) -> None:
        from hexawyn.application.ports.driven.mttr_trend_port import MTTRTrendPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_mttr_trend_adapter

            result = build_mttr_trend_adapter()

            assert isinstance(result, MTTRTrendPort)

    def test_build_recurring_incident_adapter_returns_recurringincidentport(self) -> None:
        from hexawyn.application.ports.driven.recurring_incident_port import RecurringIncidentPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_recurring_incident_adapter

            result = build_recurring_incident_adapter()

            assert isinstance(result, RecurringIncidentPort)

    def test_build_tls_compliance_adapter_returns_tlscomplianceport(self) -> None:
        from hexawyn.application.ports.driven.tls_compliance_port import TLSCompliancePort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_tls_compliance_adapter

            result = build_tls_compliance_adapter()

            assert isinstance(result, TLSCompliancePort)

    def test_build_security_posture_adapter_returns_securitypostureport(self) -> None:
        from hexawyn.application.ports.driven.security_posture_port import SecurityPosturePort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_security_posture_adapter

            result = build_security_posture_adapter()

            assert isinstance(result, SecurityPosturePort)

    def test_build_cluster_operator_status_adapter_returns_clusteroperatorstatusport(self) -> None:
        from hexawyn.application.ports.driven.cluster_operator_status_port import (
            ClusterOperatorStatusPort,
        )

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_cluster_operator_status_adapter

            result = build_cluster_operator_status_adapter()

            assert isinstance(result, ClusterOperatorStatusPort)

    def test_build_machine_config_pool_adapter_returns_machineconfigpoolport(self) -> None:
        from hexawyn.application.ports.driven.machine_config_pool_port import MachineConfigPoolPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_machine_config_pool_adapter

            result = build_machine_config_pool_adapter()

            assert isinstance(result, MachineConfigPoolPort)

    def test_build_pricing_plan_adapter_returns_planport(self) -> None:
        from hexawyn.application.ports.driven.plan_port import PlanPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_pricing_plan_adapter

            result = build_pricing_plan_adapter()

            assert isinstance(result, PlanPort)

    def test_build_usage_meter_adapter_returns_usagemeterport(self) -> None:
        from hexawyn.application.ports.driven.usage_meter_port import UsageMeterPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_usage_meter_adapter

            result = build_usage_meter_adapter()

            assert isinstance(result, UsageMeterPort)

    def test_build_consolidation_adapter_returns_consolidationport(self) -> None:
        from hexawyn.application.ports.driven.consolidation_port import ConsolidationPort

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            from hexawyn.mcp.server import build_consolidation_adapter

            result = build_consolidation_adapter()

            assert isinstance(result, ConsolidationPort)
