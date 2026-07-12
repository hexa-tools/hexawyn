import asyncio
from unittest.mock import MagicMock, patch

from hexawyn.domain.errors import ClusterUnreachableError


class TestMCPHealthTool:
    def test_health_returns_status_ok_when_duckdb_connected(self):
        mock_conn = MagicMock()
        mock_conn.execute.return_value.fetchone.return_value = (1,)

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=mock_conn),
            patch("hexawyn.mcp.server.get_api_key", return_value="sk-ant-fake"),
            patch(
                "hexawyn.mcp.server._cluster_status",
                {"status": "connected", "context": "prod-eu"},
            ),
        ):
            from hexawyn.mcp.server import health

            result = health()
            assert result["status"] == "ok"
            assert result["duckdb"] == "connected"
            assert result["api_key"] == "configured"
            assert result["version"] == "0.1.0b0"
            assert result["cluster"] == "connected"
            assert result["context"] == "prod-eu"

    def test_health_returns_degraded_when_duckdb_fails(self):
        with (
            patch(
                "hexawyn.mcp.server.get_connection",
                side_effect=Exception("DB down"),
            ),
            patch("hexawyn.mcp.server.get_api_key", return_value="sk-ant-fake"),
            patch(
                "hexawyn.mcp.server._cluster_status",
                {"status": "connected", "context": "prod-eu"},
            ),
        ):
            from hexawyn.mcp.server import health

            result = health()
            assert result["status"] == "degraded"
            assert result["duckdb"] == "unavailable"
            assert result["cluster"] == "connected"

    def test_health_returns_missing_when_no_api_key(self):
        mock_conn = MagicMock()
        mock_conn.execute.return_value.fetchone.return_value = (1,)

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=mock_conn),
            patch("hexawyn.mcp.server.get_api_key", return_value=None),
            patch(
                "hexawyn.mcp.server._cluster_status",
                {"status": "no_kubeconfig", "error": "no config found"},
            ),
        ):
            from hexawyn.mcp.server import health

            result = health()
            assert result["api_key"] == "missing"
            assert result["cluster"] == "no_kubeconfig"
            assert result["context"] == "none"

    def test_health_returns_degraded_when_both_fail(self):
        with (
            patch(
                "hexawyn.mcp.server.get_connection",
                side_effect=Exception("DB down"),
            ),
            patch("hexawyn.mcp.server.get_api_key", return_value=None),
            patch(
                "hexawyn.mcp.server._cluster_status",
                {"status": "no_kubeconfig"},
            ),
        ):
            from hexawyn.mcp.server import health

            result = health()
            assert result["status"] == "degraded"
            assert result["duckdb"] == "unavailable"
            assert result["api_key"] == "missing"
            assert result["cluster"] == "no_kubeconfig"


class TestMCPServerStartupValidation:
    def test_cluster_status_no_kubeconfig_when_config_missing(self):
        import sys

        sys.modules.pop("hexawyn.mcp.server", None)
        sys.modules.pop("hexawyn.mcp", None)

        with patch(
            "hexawyn.infrastructure.config.kubeconfig_reader.load_kubeconfig",
            side_effect=ClusterUnreachableError("no kubeconfig"),
        ):
            import hexawyn.mcp.server as server_mod

            assert server_mod._cluster_status["status"] == "no_kubeconfig"

    def test_cluster_status_connected_when_config_found(self):
        import sys

        sys.modules.pop("hexawyn.mcp.server", None)
        sys.modules.pop("hexawyn.mcp", None)

        mock_api = MagicMock()
        with (
            patch(
                "hexawyn.infrastructure.config.kubeconfig_reader.load_kubeconfig",
                return_value=mock_api,
            ),
            patch(
                "hexawyn.infrastructure.config.kubeconfig_reader.get_active_context",
                return_value={"name": "prod-eu", "context": {"cluster": "cluster-eu"}},
            ),
            patch(
                "hexawyn.infrastructure.config.kubeconfig_reader.validate_connection",
                return_value={"status": "connected", "context": "prod-eu"},
            ),
        ):
            import hexawyn.mcp.server as server_mod

            assert server_mod._cluster_status["status"] == "connected"
            assert server_mod._cluster_status["context"] == "prod-eu"


class TestMCPServerInit:
    def test_mcp_server_has_correct_name_and_version(self):
        from hexawyn.mcp.server import mcp

        assert "hexawyn" in mcp.name.lower()
        assert mcp.version is not None

    def test_health_tool_is_registered(self):
        from hexawyn.mcp.server import mcp

        tools = asyncio.run(mcp.list_tools())
        tool_names = [tool.name for tool in tools]
        assert "health" in tool_names

    def test_list_namespaces_tool_is_registered(self) -> None:
        from hexawyn.mcp.server import mcp

        tools = asyncio.run(mcp.list_tools())
        tool_names = [tool.name for tool in tools]
        assert "list_namespaces" in tool_names


class TestMCPListNamespacesTool:
    def test_list_namespaces_returns_dict_with_namespaces_key(self) -> None:
        from hexawyn.adapters.secondary.mock.demo_adapter import DemoAdapter

        with patch(
            "hexawyn.mcp.server.build_k8s_adapter",
            return_value=DemoAdapter(scenario="aws_eks"),
        ):
            from hexawyn.mcp.tools.list_namespaces import list_namespaces

            result = list_namespaces()
            assert isinstance(result, dict)
            assert "namespaces" in result
            assert isinstance(result["namespaces"], list)

    def test_list_namespaces_items_have_expected_fields(self) -> None:
        from hexawyn.adapters.secondary.mock.demo_adapter import DemoAdapter

        with patch(
            "hexawyn.mcp.server.build_k8s_adapter",
            return_value=DemoAdapter(scenario="aws_eks"),
        ):
            from hexawyn.mcp.tools.list_namespaces import list_namespaces

            result = list_namespaces()
            for ns in result["namespaces"]:
                assert "name" in ns
                assert "status" in ns
                assert "age" in ns

    def test_list_namespaces_handles_no_cluster(self) -> None:
        from hexawyn.domain.errors import ClusterUnreachableError

        with patch(
            "hexawyn.mcp.server.build_k8s_adapter",
            side_effect=ClusterUnreachableError("no kubeconfig"),
        ):
            from hexawyn.mcp.tools.list_namespaces import list_namespaces

            result = list_namespaces()
            assert result["error"] is not None
            assert result["namespaces"] == []

    def test_list_pods_tool_is_registered(self) -> None:
        from hexawyn.mcp.server import mcp

        tools = asyncio.run(mcp.list_tools())
        tool_names = [tool.name for tool in tools]
        assert "list_pods" in tool_names

    def test_list_task_runs_tool_is_registered(self) -> None:
        from hexawyn.mcp.server import mcp

        tools = asyncio.run(mcp.list_tools())
        tool_names = [tool.name for tool in tools]
        assert "list_task_runs" in tool_names

    def test_build_tekton_adapter_returns_vanilla_adapter(self) -> None:
        from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
        from hexawyn.mcp.server import build_tekton_adapter

        result = build_tekton_adapter()
        assert isinstance(result, VanillaAdapter)

    def test_build_k8s_adapter_returns_vanilla_adapter(self) -> None:
        from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
        from hexawyn.mcp.server import build_k8s_adapter

        result = build_k8s_adapter()
        assert isinstance(result, VanillaAdapter)

    def test_build_waste_adapter_returns_namespace_waste_analysis_port(self) -> None:
        from hexawyn.application.ports.driven.namespace_waste_port import NamespaceWasteAnalysisPort
        from hexawyn.mcp.server import build_waste_adapter

        result = build_waste_adapter()
        assert isinstance(result, NamespaceWasteAnalysisPort)

    def test_build_waste_adapter_reads_prometheus_url_from_env(self) -> None:
        from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
        from hexawyn.mcp.server import build_waste_adapter

        with patch.dict("os.environ", {"PROMETHEUS_URL": "http://prom:9090"}):
            result = build_waste_adapter()

        assert isinstance(result, VanillaAdapter)
        assert result._prometheus_url == "http://prom:9090"

    def test_build_rightsizing_adapter_returns_rightsizing_port(self) -> None:
        from hexawyn.application.ports.driven.rightsizing_port import RightsizingPort
        from hexawyn.mcp.server import build_rightsizing_adapter

        result = build_rightsizing_adapter()

        assert isinstance(result, RightsizingPort)

    def test_build_cost_forecast_adapter_returns_cost_forecast_port(self) -> None:
        from hexawyn.application.ports.driven.cost_forecast_port import CostForecastPort
        from hexawyn.mcp.server import build_cost_forecast_adapter

        result = build_cost_forecast_adapter()

        assert isinstance(result, CostForecastPort)

    def test_build_budget_projection_adapter_returns_port(self) -> None:
        from hexawyn.application.ports.driven.budget_projection_port import (
            BudgetProjectionPort,
        )
        from hexawyn.mcp.server import build_budget_projection_adapter

        result = build_budget_projection_adapter()

        assert isinstance(result, BudgetProjectionPort)

    def test_build_spike_provisioning_adapter_returns_port(self) -> None:
        from hexawyn.application.ports.driven.spike_provisioning_port import (
            SpikeProvisioningPort,
        )
        from hexawyn.mcp.server import build_spike_provisioning_adapter

        result = build_spike_provisioning_adapter()

        assert isinstance(result, SpikeProvisioningPort)

    def test_build_optimization_roi_adapter_returns_port(self) -> None:
        from hexawyn.application.ports.driven.optimization_roi_port import (
            OptimizationRoiPort,
        )
        from hexawyn.mcp.server import build_optimization_roi_adapter

        result = build_optimization_roi_adapter()

        assert isinstance(result, OptimizationRoiPort)

    def test_build_sla_report_adapter_returns_port(self) -> None:
        from hexawyn.application.ports.driven.sla_report_port import SlaReportPort
        from hexawyn.mcp.server import build_sla_report_adapter

        result = build_sla_report_adapter()

        assert isinstance(result, SlaReportPort)

    def test_build_platform_reliability_adapter_returns_port(self) -> None:
        from hexawyn.application.ports.driven.platform_reliability_port import (
            PlatformReliabilityPort,
        )
        from hexawyn.mcp.server import build_platform_reliability_adapter

        result = build_platform_reliability_adapter()

        assert isinstance(result, PlatformReliabilityPort)

    def test_build_incident_cost_adapter_returns_port(self) -> None:
        from hexawyn.application.ports.driven.incident_cost_port import IncidentCostPort
        from hexawyn.mcp.server import build_incident_cost_adapter

        result = build_incident_cost_adapter()

        assert isinstance(result, IncidentCostPort)

    def test_build_prediction_roi_adapter_returns_port(self) -> None:
        from hexawyn.application.ports.driven.prediction_roi_port import (
            PredictionRoiPort,
        )
        from hexawyn.mcp.server import build_prediction_roi_adapter

        result = build_prediction_roi_adapter()

        assert isinstance(result, PredictionRoiPort)

    def test_build_budget_intelligence_adapter_returns_port(self) -> None:
        from hexawyn.application.ports.driven.budget_intelligence_port import (
            BudgetIntelligencePort,
        )
        from hexawyn.mcp.server import build_budget_intelligence_adapter

        result = build_budget_intelligence_adapter()

        assert isinstance(result, BudgetIntelligencePort)

    def test_build_night_intervention_adapter_returns_port(self) -> None:
        from hexawyn.application.ports.driven.engineer_workload_port import (
            EngineerWorkloadPort,
        )
        from hexawyn.mcp.server import build_night_intervention_adapter

        result = build_night_intervention_adapter()

        assert isinstance(result, EngineerWorkloadPort)

    def test_build_disruption_risk_adapter_returns_port(self) -> None:
        from hexawyn.application.ports.driven.disruption_risk_port import (
            DisruptionRiskPort,
        )
        from hexawyn.mcp.server import build_disruption_risk_adapter

        result = build_disruption_risk_adapter()

        assert isinstance(result, DisruptionRiskPort)

    def test_build_critical_cve_adapter_returns_port(self) -> None:
        from hexawyn.application.ports.driven.critical_cve_port import CriticalCvePort
        from hexawyn.mcp.server import build_critical_cve_adapter

        result = build_critical_cve_adapter()

        assert isinstance(result, CriticalCvePort)

    def test_build_stale_credentials_adapter_returns_port(self) -> None:
        from hexawyn.application.ports.driven.stale_credentials_port import (
            StaleCredentialsPort,
        )
        from hexawyn.mcp.server import build_stale_credentials_adapter

        result = build_stale_credentials_adapter()

        assert isinstance(result, StaleCredentialsPort)

    def test_build_unauthorized_access_adapter_returns_port(self) -> None:
        from hexawyn.application.ports.driven.unauthorized_access_port import (
            UnauthorizedAccessPort,
        )
        from hexawyn.mcp.server import build_unauthorized_access_adapter

        result = build_unauthorized_access_adapter()

        assert isinstance(result, UnauthorizedAccessPort)

    def test_build_cost_adapter_returns_cost_estimation_port(self) -> None:
        from hexawyn.application.ports.driven.cost_estimation_port import (
            CostEstimationPort,
        )
        from hexawyn.mcp.server import build_cost_adapter

        result = build_cost_adapter()

        assert isinstance(result, CostEstimationPort)

    def test_build_cost_adapter_aws_branch(self) -> None:
        from hexawyn.application.ports.driven.cost_estimation_port import (
            CostEstimationPort,
        )

        with patch("hexawyn.mcp.server.context_name", "eks-prod"):
            from hexawyn.mcp.server import build_cost_adapter as _build

            result = _build()

        assert isinstance(result, CostEstimationPort)

    def test_build_cost_adapter_azure_branch(self) -> None:
        from hexawyn.application.ports.driven.cost_estimation_port import (
            CostEstimationPort,
        )

        with patch("hexawyn.mcp.server.context_name", "aks-prod"):
            from hexawyn.mcp.server import build_cost_adapter as _build

            result = _build()

        assert isinstance(result, CostEstimationPort)

    def test_build_cost_adapter_gcp_branch(self) -> None:
        from hexawyn.application.ports.driven.cost_estimation_port import (
            CostEstimationPort,
        )

        with patch("hexawyn.mcp.server.context_name", "gke-prod"):
            from hexawyn.mcp.server import build_cost_adapter as _build

            result = _build()

        assert isinstance(result, CostEstimationPort)

    def test_build_cluster_diff_adapter_returns_port(self) -> None:
        from hexawyn.application.ports.driven.cluster_diff_port import ClusterDiffPort
        from hexawyn.mcp.server import build_cluster_diff_adapter

        result = build_cluster_diff_adapter()

        assert isinstance(result, ClusterDiffPort)

    def test_build_cross_cluster_incident_adapter_returns_port(self) -> None:
        from hexawyn.application.ports.driven.cross_cluster_incident_port import (
            CrossClusterIncidentPort,
        )
        from hexawyn.mcp.server import build_cross_cluster_incident_adapter

        result = build_cross_cluster_incident_adapter()

        assert isinstance(result, CrossClusterIncidentPort)

    def test_build_what_if_simulation_adapter_returns_what_if_simulation_port(self) -> None:
        from hexawyn.application.ports.driven.what_if_simulation_port import WhatIfSimulationPort
        from hexawyn.mcp.server import build_what_if_simulation_adapter

        result = build_what_if_simulation_adapter()
        assert isinstance(result, WhatIfSimulationPort)

    def test_build_zombie_detection_adapter_returns_zombie_detection_port(self) -> None:
        from hexawyn.application.ports.driven.zombie_detection_port import ZombieDetectionPort
        from hexawyn.mcp.server import build_zombie_detection_adapter

        result = build_zombie_detection_adapter()
        assert isinstance(result, ZombieDetectionPort)

    def test_build_cost_saving_adapter_returns_cost_saving_estimation_port(self) -> None:
        from hexawyn.application.ports.driven.cost_saving_estimation_port import (
            CostSavingEstimationPort,
        )
        from hexawyn.mcp.server import build_cost_saving_adapter

        result = build_cost_saving_adapter()
        assert isinstance(result, CostSavingEstimationPort)

    def test_build_fleet_health_adapter_returns_fleet_health_port(self) -> None:
        from hexawyn.application.ports.driven.fleet_health_port import FleetHealthPort
        from hexawyn.mcp.server import build_fleet_health_adapter

        result = build_fleet_health_adapter()
        assert isinstance(result, FleetHealthPort)

    def test_build_gitops_adapter_returns_gitops_port(self) -> None:
        from hexawyn.application.ports.driven.gitops_port import GitOpsPort
        from hexawyn.mcp.server import build_gitops_adapter

        result = build_gitops_adapter()
        assert isinstance(result, GitOpsPort)

    def test_build_rollouts_adapter_returns_rollouts_port(self) -> None:
        from hexawyn.application.ports.driven.rollouts_port import RolloutsPort
        from hexawyn.mcp.server import build_rollouts_adapter

        result = build_rollouts_adapter()
        assert isinstance(result, RolloutsPort)

    def test_build_policy_adapter_returns_policy_port(self) -> None:
        from hexawyn.application.ports.driven.policy_port import PolicyPort
        from hexawyn.mcp.server import build_policy_adapter

        result = build_policy_adapter()
        assert isinstance(result, PolicyPort)

    def test_build_cert_manager_adapter_returns_cert_manager_port(self) -> None:
        from hexawyn.application.ports.driven.cert_manager_port import CertManagerPort
        from hexawyn.mcp.server import build_cert_manager_adapter

        result = build_cert_manager_adapter()
        assert isinstance(result, CertManagerPort)

    def test_build_keda_adapter_returns_keda_port(self) -> None:
        from hexawyn.application.ports.driven.keda_port import KedaPort
        from hexawyn.mcp.server import build_keda_adapter

        result = build_keda_adapter()
        assert isinstance(result, KedaPort)

    def test_build_canary_comparison_adapter_returns_canary_comparison_port(self) -> None:
        from hexawyn.application.ports.driven.canary_comparison_port import CanaryComparisonPort
        from hexawyn.mcp.server import build_canary_comparison_adapter

        result = build_canary_comparison_adapter()
        assert isinstance(result, CanaryComparisonPort)

    def test_build_cost_profiling_adapter_returns_cost_profiling_port(self) -> None:
        from hexawyn.application.ports.driven.cost_profiling_port import CostProfilingPort
        from hexawyn.mcp.server import build_cost_profiling_adapter

        result = build_cost_profiling_adapter()
        assert isinstance(result, CostProfilingPort)

    def test_build_memory_saturation_adapter_returns_memory_saturation_port(self) -> None:
        from hexawyn.application.ports.driven.memory_saturation_port import MemorySaturationPort
        from hexawyn.mcp.server import build_memory_saturation_adapter

        result = build_memory_saturation_adapter()
        assert isinstance(result, MemorySaturationPort)

    def test_build_span_bottleneck_adapter_returns_span_bottleneck_port(self) -> None:
        from hexawyn.application.ports.driven.span_bottleneck_port import SpanBottleneckPort
        from hexawyn.mcp.server import build_span_bottleneck_adapter

        result = build_span_bottleneck_adapter()
        assert isinstance(result, SpanBottleneckPort)

    def test_build_latency_percentile_adapter_returns_latency_percentile_port(self) -> None:
        from hexawyn.application.ports.driven.latency_percentile_port import LatencyPercentilePort
        from hexawyn.mcp.server import build_latency_percentile_adapter

        result = build_latency_percentile_adapter()
        assert isinstance(result, LatencyPercentilePort)

    def test_build_metric_correlation_adapter_returns_metric_correlation_port(self) -> None:
        from hexawyn.application.ports.driven.metric_correlation_port import MetricCorrelationPort
        from hexawyn.mcp.server import build_metric_correlation_adapter

        result = build_metric_correlation_adapter()
        assert isinstance(result, MetricCorrelationPort)

    def test_build_capacity_forecast_adapter_returns_capacity_forecast_port(self) -> None:
        from hexawyn.application.ports.driven.capacity_forecast_port import CapacityForecastPort
        from hexawyn.mcp.server import build_capacity_forecast_adapter

        result = build_capacity_forecast_adapter()
        assert isinstance(result, CapacityForecastPort)

    def test_build_headroom_simulation_adapter_returns_headroom_simulation_port(self) -> None:
        from hexawyn.application.ports.driven.headroom_simulation_port import HeadroomSimulationPort
        from hexawyn.mcp.server import build_headroom_simulation_adapter

        result = build_headroom_simulation_adapter()
        assert isinstance(result, HeadroomSimulationPort)

    def test_build_node_analysis_adapter_returns_hot_node_analysis_port(self) -> None:
        from hexawyn.application.ports.driven.hot_node_analysis_port import HotNodeAnalysisPort
        from hexawyn.mcp.server import build_node_analysis_adapter

        result = build_node_analysis_adapter()
        assert isinstance(result, HotNodeAnalysisPort)

    def test_build_helm_drift_adapter_returns_drift_detection_port(self) -> None:
        from hexawyn.application.ports.driven.drift_detection_port import DriftDetectionPort
        from hexawyn.mcp.server import build_helm_drift_adapter

        result = build_helm_drift_adapter()
        assert isinstance(result, DriftDetectionPort)

    def test_build_kustomize_drift_adapter_returns_drift_detection_port(self) -> None:
        from hexawyn.application.ports.driven.drift_detection_port import DriftDetectionPort
        from hexawyn.mcp.server import build_kustomize_drift_adapter

        result = build_kustomize_drift_adapter()
        assert isinstance(result, DriftDetectionPort)

    def test_build_live_resource_adapter_returns_live_resource_port(self) -> None:
        from hexawyn.application.ports.driven.live_resource_port import LiveResourcePort
        from hexawyn.mcp.server import build_live_resource_adapter

        result = build_live_resource_adapter()
        assert isinstance(result, LiveResourcePort)

    def test_build_audit_log_adapter_returns_gitops_drift_audit_port(self) -> None:
        from hexawyn.application.ports.driven.gitops_drift_audit_port import GitOpsDriftAuditPort
        from hexawyn.mcp.server import build_audit_log_adapter

        result = build_audit_log_adapter()
        assert isinstance(result, GitOpsDriftAuditPort)

    def test_build_image_drift_adapter_returns_image_drift_port(self) -> None:
        from hexawyn.application.ports.driven.image_drift_port import ImageDriftPort
        from hexawyn.mcp.server import build_image_drift_adapter

        result = build_image_drift_adapter()
        assert isinstance(result, ImageDriftPort)

    def test_build_rbac_audit_adapter_returns_rbac_security_audit_port(self) -> None:
        from hexawyn.application.ports.driven.rbac_security_audit_port import RBACSecurityAuditPort
        from hexawyn.mcp.server import build_rbac_audit_adapter

        result = build_rbac_audit_adapter()
        assert isinstance(result, RBACSecurityAuditPort)

    def test_build_pod_security_adapter_returns_pod_security_context_audit_port(self) -> None:
        from hexawyn.application.ports.driven.pod_security_context_audit_port import (
            PodSecurityContextAuditPort,
        )
        from hexawyn.mcp.server import build_pod_security_adapter

        result = build_pod_security_adapter()
        assert isinstance(result, PodSecurityContextAuditPort)

    def test_build_image_inventory_adapter_returns_image_inventory_port(self) -> None:
        from hexawyn.application.ports.driven.image_inventory_port import ImageInventoryPort
        from hexawyn.mcp.server import build_image_inventory_adapter

        result = build_image_inventory_adapter()
        assert isinstance(result, ImageInventoryPort)

    def test_build_image_vulnerability_scan_adapter_returns_image_vulnerability_scan_port(
        self,
    ) -> None:
        from hexawyn.application.ports.driven.image_vulnerability_scan_port import (
            ImageVulnerabilityScanPort,
        )
        from hexawyn.mcp.server import build_image_vulnerability_scan_adapter

        result = build_image_vulnerability_scan_adapter()
        assert isinstance(result, ImageVulnerabilityScanPort)

    def test_build_secret_rotation_audit_adapter_returns_secret_rotation_audit_port(self) -> None:
        from hexawyn.application.ports.driven.secret_rotation_audit_port import (
            SecretRotationAuditPort,
        )
        from hexawyn.mcp.server import build_secret_rotation_audit_adapter

        result = build_secret_rotation_audit_adapter()
        assert isinstance(result, SecretRotationAuditPort)

    def test_build_network_policy_audit_adapter_returns_network_policy_audit_port(self) -> None:
        from hexawyn.application.ports.driven.network_policy_audit_port import (
            NetworkPolicyAuditPort,
        )
        from hexawyn.mcp.server import build_network_policy_audit_adapter

        result = build_network_policy_audit_adapter()
        assert isinstance(result, NetworkPolicyAuditPort)

    def test_build_external_exposure_audit_adapter_returns_external_exposure_audit_port(
        self,
    ) -> None:
        from hexawyn.application.ports.driven.external_exposure_audit_port import (
            ExternalExposureAuditPort,
        )
        from hexawyn.mcp.server import build_external_exposure_audit_adapter

        result = build_external_exposure_audit_adapter()
        assert isinstance(result, ExternalExposureAuditPort)

    def test_build_trace_log_correlation_adapter_returns_trace_log_correlation_port(self) -> None:
        from hexawyn.application.ports.driven.trace_log_correlation_port import (
            TraceLogCorrelationPort,
        )
        from hexawyn.mcp.server import build_trace_log_correlation_adapter

        result = build_trace_log_correlation_adapter()
        assert isinstance(result, TraceLogCorrelationPort)

    def test_build_security_audit_adapter_returns_security_audit_port(self) -> None:
        from hexawyn.application.ports.driven.security_audit_port import SecurityAuditPort
        from hexawyn.mcp.server import build_security_audit_adapter

        result = build_security_audit_adapter()
        assert isinstance(result, SecurityAuditPort)

    def test_build_service_dependency_graph_adapter_returns_service_dependency_graph_port(
        self,
    ) -> None:
        from hexawyn.application.ports.driven.service_dependency_graph_port import (
            ServiceDependencyGraphPort,
        )
        from hexawyn.mcp.server import build_service_dependency_graph_adapter

        result = build_service_dependency_graph_adapter()
        assert isinstance(result, ServiceDependencyGraphPort)

    def test_build_trace_event_correlation_adapter_returns_trace_event_correlation_port(
        self,
    ) -> None:
        from hexawyn.application.ports.driven.trace_event_correlation_port import (
            TraceEventCorrelationPort,
        )
        from hexawyn.mcp.server import build_trace_event_correlation_adapter

        result = build_trace_event_correlation_adapter()
        assert isinstance(result, TraceEventCorrelationPort)

    def test_build_slow_trace_search_adapter_returns_slow_trace_search_port(self) -> None:
        from hexawyn.application.ports.driven.slow_trace_search_port import SlowTraceSearchPort
        from hexawyn.mcp.server import build_slow_trace_search_adapter

        result = build_slow_trace_search_adapter()
        assert isinstance(result, SlowTraceSearchPort)

    def test_build_deployment_latency_comparison_adapter_returns_deployment_latency_comparison_port(
        self,
    ) -> None:
        from hexawyn.application.ports.driven.deployment_latency_comparison_port import (
            DeploymentLatencyComparisonPort,
        )
        from hexawyn.mcp.server import build_deployment_latency_comparison_adapter

        result = build_deployment_latency_comparison_adapter()
        assert isinstance(result, DeploymentLatencyComparisonPort)

    def test_build_version_regression_adapter_returns_version_regression_port(self) -> None:
        from hexawyn.application.ports.driven.version_regression_port import VersionRegressionPort
        from hexawyn.mcp.server import build_version_regression_adapter

        result = build_version_regression_adapter()
        assert isinstance(result, VersionRegressionPort)

    def test_build_redundant_call_detection_adapter_returns_redundant_call_detection_port(
        self,
    ) -> None:
        from hexawyn.application.ports.driven.redundant_call_detection_port import (
            RedundantCallDetectionPort,
        )
        from hexawyn.mcp.server import build_redundant_call_detection_adapter

        result = build_redundant_call_detection_adapter()
        assert isinstance(result, RedundantCallDetectionPort)

    def test_build_compliance_audit_adapter_returns_compliance_audit_port(self) -> None:
        from hexawyn.application.ports.driven.compliance_audit_port import ComplianceAuditPort
        from hexawyn.mcp.server import build_compliance_audit_adapter

        result = build_compliance_audit_adapter()
        assert isinstance(result, ComplianceAuditPort)

    def test_build_error_attribution_adapter_returns_error_attribution_port(self) -> None:
        from hexawyn.application.ports.driven.error_attribution_port import ErrorAttributionPort
        from hexawyn.mcp.server import build_error_attribution_adapter

        result = build_error_attribution_adapter()
        assert isinstance(result, ErrorAttributionPort)

    def test_build_slo_breach_prediction_adapter_returns_slo_breach_prediction_port(self) -> None:
        from hexawyn.application.ports.driven.slo_breach_prediction_port import (
            SLOBreachPredictionPort,
        )
        from hexawyn.mcp.server import build_slo_breach_prediction_adapter

        result = build_slo_breach_prediction_adapter()
        assert isinstance(result, SLOBreachPredictionPort)

    def test_build_certificate_investigation_adapter_returns_certificate_investigation_port(
        self,
    ) -> None:
        from hexawyn.application.ports.driven.certificate_investigation_port import (
            CertificateInvestigationPort,
        )
        from hexawyn.mcp.server import build_certificate_investigation_adapter

        result = build_certificate_investigation_adapter()
        assert isinstance(result, CertificateInvestigationPort)

    def test_build_resource_yaml_adapter_returns_resource_yaml_port(self) -> None:
        from hexawyn.application.ports.driven.resource_yaml_port import ResourceYAMLPort
        from hexawyn.mcp.server import build_resource_yaml_adapter

        result = build_resource_yaml_adapter()
        assert isinstance(result, ResourceYAMLPort)

    def test_build_pipeline_run_logs_adapter_returns_pipeline_run_logs_port(self) -> None:
        from hexawyn.application.ports.driven.pipeline_run_logs_port import PipelineRunLogsPort
        from hexawyn.mcp.server import build_pipeline_run_logs_adapter

        result = build_pipeline_run_logs_adapter()
        assert isinstance(result, PipelineRunLogsPort)

    def test_build_etcd_logs_adapter_returns_etcd_logs_port(self) -> None:
        from hexawyn.application.ports.driven.etcd_logs_port import ETCDLogsPort
        from hexawyn.mcp.server import build_etcd_logs_adapter

        result = build_etcd_logs_adapter()
        assert isinstance(result, ETCDLogsPort)

    def test_build_pod_logs_adapter_returns_pod_logs_port(self) -> None:
        from hexawyn.application.ports.driven.pod_logs_port import PodLogsPort
        from hexawyn.mcp.server import build_pod_logs_adapter

        result = build_pod_logs_adapter()
        assert isinstance(result, PodLogsPort)

    def test_build_pod_metrics_baseline_adapter_returns_pod_metrics_baseline_port(self) -> None:
        from hexawyn.application.ports.driven.pod_metrics_baseline_port import (
            PodMetricsBaselinePort,
        )
        from hexawyn.mcp.server import build_pod_metrics_baseline_adapter

        result = build_pod_metrics_baseline_adapter()
        assert isinstance(result, PodMetricsBaselinePort)

    def test_build_resource_search_adapter_returns_resource_search_port(self) -> None:
        from hexawyn.application.ports.driven.resource_search_port import ResourceSearchPort
        from hexawyn.mcp.server import build_resource_search_adapter

        result = build_resource_search_adapter()
        assert isinstance(result, ResourceSearchPort)

    def test_build_namespace_events_adapter_returns_namespace_events_port(self) -> None:
        from hexawyn.application.ports.driven.namespace_events_port import NamespaceEventsPort
        from hexawyn.mcp.server import build_namespace_events_adapter

        result = build_namespace_events_adapter()
        assert isinstance(result, NamespaceEventsPort)

    def test_build_namespace_overview_adapter_returns_namespace_overview_port(self) -> None:
        from hexawyn.application.ports.driven.namespace_overview_port import NamespaceOverviewPort
        from hexawyn.mcp.server import build_namespace_overview_adapter

        result = build_namespace_overview_adapter()
        assert isinstance(result, NamespaceOverviewPort)

    def test_build_adaptive_investigation_adapter_returns_adaptive_investigation_port(self) -> None:
        from hexawyn.application.ports.driven.adaptive_investigation_port import (
            AdaptiveInvestigationPort,
        )
        from hexawyn.mcp.server import build_adaptive_investigation_adapter

        result = build_adaptive_investigation_adapter()
        assert isinstance(result, AdaptiveInvestigationPort)

    def test_build_pod_log_watch_adapter_returns_pod_log_watch_port(self) -> None:
        from hexawyn.application.ports.driven.pod_log_watch_port import PodLogWatchPort
        from hexawyn.mcp.server import build_pod_log_watch_adapter

        result = build_pod_log_watch_adapter()
        assert isinstance(result, PodLogWatchPort)

    def test_build_alert_notification_adapter_returns_alert_notification_port(self) -> None:
        from hexawyn.application.ports.driven.alert_notification_port import AlertNotificationPort
        from hexawyn.mcp.server import build_alert_notification_adapter

        result = build_alert_notification_adapter()
        assert isinstance(result, AlertNotificationPort)

    def test_build_pipeline_for_service_adapter_returns_pipeline_for_service_port(self) -> None:
        from hexawyn.application.ports.driven.pipeline_for_service_port import (
            PipelineForServicePort,
        )
        from hexawyn.mcp.server import build_pipeline_for_service_adapter

        result = build_pipeline_for_service_adapter()
        assert isinstance(result, PipelineForServicePort)

    def test_register_tools_does_not_crash_on_import_error(self) -> None:
        from pathlib import Path
        from unittest.mock import patch

        tools_path = Path(__file__).parent.parent.parent / "src" / "hexawyn" / "mcp" / "tools"
        py_files = list(tools_path.glob("*.py"))

        if not py_files:
            return

        with patch(
            "importlib.import_module",
            side_effect=ImportError("simulated import failure"),
        ):
            from fastmcp import FastMCP
            from hexawyn.mcp.server import register_tools

            test_server = FastMCP("test-register")
            register_tools(test_server)


class TestMCPListPodsTool:
    def test_list_pods_returns_pods_for_namespace(self) -> None:
        from hexawyn.adapters.secondary.mock.demo_adapter import DemoAdapter

        with patch(
            "hexawyn.mcp.server.build_k8s_adapter",
            return_value=DemoAdapter(scenario="aws_eks"),
        ):
            from hexawyn.mcp.tools.list_pods import list_pods

            result = list_pods(namespace="production")
            assert isinstance(result, dict)
            assert "pods" in result
            assert isinstance(result["pods"], list)
            assert len(result["pods"]) > 0

    def test_list_pods_empty_namespace(self) -> None:
        from hexawyn.adapters.secondary.mock.demo_adapter import DemoAdapter

        with patch(
            "hexawyn.mcp.server.build_k8s_adapter",
            return_value=DemoAdapter(scenario="aws_eks"),
        ):
            from hexawyn.mcp.tools.list_pods import list_pods

            result = list_pods(namespace="nonexistent")
            assert result["pods"] == []

    def test_list_pods_handles_error(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_k8s_adapter",
            side_effect=Exception("k8s down"),
        ):
            from hexawyn.mcp.tools.list_pods import list_pods

            result = list_pods(namespace="default")
            assert result["error"] == "k8s down"
            assert result["pods"] == []


class TestMCPListTaskRunsTool:
    def test_list_task_runs_returns_task_runs_list(self) -> None:
        from unittest.mock import MagicMock

        from hexawyn.application.ports.driven.tekton_port import TaskRunInfo, TektonPort

        fake_run: TaskRunInfo = {
            "name": "build-deploy-clone-repo-abc",
            "task_ref": "clone-repo",
            "status": "Succeeded",
            "start_time": "2024-01-01T10:00:00Z",
            "duration": "12s",
            "failing_step": None,
            "failing_step_error": None,
        }
        mock_adapter = MagicMock(spec=TektonPort)
        mock_adapter.list_task_runs.return_value = [fake_run]

        with patch(
            "hexawyn.mcp.server.build_tekton_adapter",
            return_value=mock_adapter,
        ):
            from hexawyn.mcp.tools.list_task_runs import list_task_runs

            result = list_task_runs(pipeline_name="build-deploy", namespace="ci")
            assert isinstance(result["task_runs"], list)
            assert len(result["task_runs"]) == 1
            assert result["error"] is None

    def test_list_task_runs_returns_error_when_pipeline_not_found(self) -> None:
        from hexawyn.domain.errors import PipelineNotFoundError

        with patch(
            "hexawyn.mcp.server.build_tekton_adapter",
            side_effect=PipelineNotFoundError(pipeline_name="ghost"),
        ):
            from hexawyn.mcp.tools.list_task_runs import list_task_runs

            result = list_task_runs(pipeline_name="ghost", namespace="ci")
            assert result["task_runs"] == []
            assert result["error"] is not None
            assert "ghost" in str(result["error"])

    def test_list_task_runs_returns_error_on_cluster_failure(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_tekton_adapter",
            side_effect=Exception("tekton API down"),
        ):
            from hexawyn.mcp.tools.list_task_runs import list_task_runs

            result = list_task_runs(pipeline_name="build-deploy", namespace="ci")
            assert result["task_runs"] == []
            assert result["error"] == "tekton API down"


class TestMCPListPipelineRunsTool:
    def test_list_pipeline_runs_tool_is_registered(self) -> None:
        from hexawyn.mcp.server import mcp

        tools = asyncio.run(mcp.list_tools())
        tool_names = [tool.name for tool in tools]
        assert "list_pipeline_runs" in tool_names

    def test_list_pipeline_runs_returns_runs_and_stats(self) -> None:
        from unittest.mock import MagicMock

        from hexawyn.application.ports.driven.tekton_port import PipelineRunInfo, TektonPort

        fake_run: PipelineRunInfo = {
            "name": "payment-service-run-abc",
            "status": "Succeeded",
            "start_time": "2024-01-15T10:00:00Z",
            "duration": "4m30s",
            "duration_seconds": 270,
            "triggered_by": "github-push",
        }
        mock_adapter = MagicMock(spec=TektonPort)
        mock_adapter.list_pipeline_runs.return_value = [fake_run]

        with patch("hexawyn.mcp.server.build_tekton_adapter", return_value=mock_adapter):
            from hexawyn.mcp.tools.list_pipeline_runs import list_pipeline_runs

            result = list_pipeline_runs(service_name="payment-service", namespace="ci")
            assert isinstance(result["runs"], list)
            assert len(result["runs"]) == 1
            assert isinstance(result["stats"], dict)
            assert result["error"] is None

    def test_list_pipeline_runs_returns_error_when_service_not_found(self) -> None:
        from hexawyn.domain.errors import ServiceNotFoundError

        with patch(
            "hexawyn.mcp.server.build_tekton_adapter",
            side_effect=ServiceNotFoundError(service_name="ghost"),
        ):
            from hexawyn.mcp.tools.list_pipeline_runs import list_pipeline_runs

            result = list_pipeline_runs(service_name="ghost", namespace="ci")
            assert result["runs"] == []
            assert result["error"] is not None
            assert "ghost" in str(result["error"])

    def test_list_pipeline_runs_returns_error_on_cluster_failure(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_tekton_adapter",
            side_effect=Exception("tekton API down"),
        ):
            from hexawyn.mcp.tools.list_pipeline_runs import list_pipeline_runs

            result = list_pipeline_runs(service_name="payment-service", namespace="ci")
            assert result["runs"] == []
            assert result["error"] == "tekton API down"

    def test_list_pipeline_runs_includes_outliers_and_note(self) -> None:
        from unittest.mock import MagicMock

        from hexawyn.application.ports.driven.tekton_port import PipelineRunInfo, TektonPort

        normal = [
            {
                "name": f"run-{i}",
                "status": "Succeeded",
                "start_time": f"2024-01-{15 - i:02d}T10:00:00Z",
                "duration": "5m",
                "duration_seconds": 300,
                "triggered_by": None,
            }
            for i in range(2)
        ]
        outlier: PipelineRunInfo = {
            "name": "run-outlier",
            "status": "Succeeded",
            "start_time": "2024-01-10T10:00:00Z",
            "duration": "22m",
            "duration_seconds": 1320,
            "triggered_by": None,
        }
        mock_adapter = MagicMock(spec=TektonPort)
        mock_adapter.list_pipeline_runs.return_value = normal + [outlier]

        with patch("hexawyn.mcp.server.build_tekton_adapter", return_value=mock_adapter):
            from hexawyn.mcp.tools.list_pipeline_runs import list_pipeline_runs

            result = list_pipeline_runs(service_name="payment-service", namespace="ci", limit=10)
            assert "run-outlier" in result["outliers"]
            assert result["note"] is not None


class TestMCPListPipelineRunsInNamespaceTool:
    def test_tool_is_registered(self) -> None:
        from fastmcp import FastMCP
        from hexawyn.mcp.tools.list_pipeline_runs_in_namespace import register

        mcp = FastMCP("test-server")
        register(mcp)
        tools = asyncio.run(mcp.list_tools())
        tool_names = {t.name for t in tools}
        assert "list_pipeline_runs_in_namespace" in tool_names

    def test_returns_runs_and_stuck_list(self) -> None:
        from datetime import UTC, datetime, timedelta

        from hexawyn.application.ports.driven.tekton_port import (
            NamespacedPipelineRunInfo,
            TektonPort,
        )

        stuck_start = (datetime.now(UTC) - timedelta(hours=3)).strftime("%Y-%m-%dT%H:%M:%SZ")
        runs: list[NamespacedPipelineRunInfo] = [
            {
                "name": "deploy-stuck",
                "status": "Running",
                "start_time": stuck_start,
                "duration": None,
                "duration_seconds": None,
                "pipeline_ref": "deploy-payment",
            },
            {
                "name": "deploy-ok",
                "status": "Succeeded",
                "start_time": "2024-01-15T09:00:00Z",
                "duration": "4m30s",
                "duration_seconds": 270,
                "pipeline_ref": "deploy-auth",
            },
        ]
        mock_adapter = MagicMock(spec=TektonPort)
        mock_adapter.list_pipeline_runs_in_namespace.return_value = runs

        with patch("hexawyn.mcp.server.build_tekton_adapter", return_value=mock_adapter):
            from hexawyn.mcp.tools.list_pipeline_runs_in_namespace import (
                list_pipeline_runs_in_namespace,
            )

            result = list_pipeline_runs_in_namespace(namespace="tekton")

        assert result["error"] is None
        assert "deploy-stuck" in result["stuck_runs"]
        assert any(r["name"] == "deploy-stuck" and r["is_stuck"] for r in result["runs"])  # type: ignore[index]

    def test_empty_namespace_returns_note(self) -> None:
        from hexawyn.application.ports.driven.tekton_port import TektonPort

        mock_adapter = MagicMock(spec=TektonPort)
        mock_adapter.list_pipeline_runs_in_namespace.return_value = []

        with patch("hexawyn.mcp.server.build_tekton_adapter", return_value=mock_adapter):
            from hexawyn.mcp.tools.list_pipeline_runs_in_namespace import (
                list_pipeline_runs_in_namespace,
            )

            result = list_pipeline_runs_in_namespace(namespace="tekton")

        assert result["runs"] == []
        assert result["note"] is not None
        assert result["error"] is None

    def test_rbac_error_returns_error_field(self) -> None:
        from hexawyn.application.ports.driven.tekton_port import TektonPort
        from hexawyn.domain.errors import InsufficientPermissionsError

        mock_adapter = MagicMock(spec=TektonPort)
        mock_adapter.list_pipeline_runs_in_namespace.side_effect = InsufficientPermissionsError(
            "forbidden"
        )

        with patch("hexawyn.mcp.server.build_tekton_adapter", return_value=mock_adapter):
            from hexawyn.mcp.tools.list_pipeline_runs_in_namespace import (
                list_pipeline_runs_in_namespace,
            )

            result = list_pipeline_runs_in_namespace(namespace="tekton")

        assert result["error"] is not None
        assert "forbidden" in str(result["error"])
        assert result["runs"] == []

    def test_tekton_not_installed_returns_error_field(self) -> None:
        from hexawyn.application.ports.driven.tekton_port import TektonPort
        from hexawyn.domain.errors import TektonNotInstalledError

        mock_adapter = MagicMock(spec=TektonPort)
        mock_adapter.list_pipeline_runs_in_namespace.side_effect = TektonNotInstalledError()

        with patch("hexawyn.mcp.server.build_tekton_adapter", return_value=mock_adapter):
            from hexawyn.mcp.tools.list_pipeline_runs_in_namespace import (
                list_pipeline_runs_in_namespace,
            )

            result = list_pipeline_runs_in_namespace(namespace="tekton")

        assert result["error"] is not None
        assert "Tekton" in str(result["error"])


class TestMCPDetectOverProvisionedNamespacesTool:
    def test_tool_is_registered(self) -> None:
        from hexawyn.mcp.server import mcp

        tools = asyncio.run(mcp.list_tools())
        tool_names = {t.name for t in tools}
        assert "detect_over_provisioned_namespaces" in tool_names

    def test_dev_namespace_flagged_over_provisioned(self) -> None:
        from hexawyn.application.ports.driven.namespace_waste_port import NamespaceWasteAnalysisPort

        mock_adapter = MagicMock(spec=NamespaceWasteAnalysisPort)
        mock_adapter.get_all_namespace_waste_data.return_value = [
            {
                "namespace": "dev",
                "cpu_requested_cores": 8.0,
                "memory_requested_gb": 16.0,
                "cpu_actual_avg_cores": 0.45,
                "memory_actual_avg_gb": 1.2,
                "age_hours": 720.0,
                "has_resource_requests": True,
            },
        ]

        with patch("hexawyn.mcp.server.build_waste_adapter", return_value=mock_adapter):
            from hexawyn.mcp.tools.detect_over_provisioned_namespaces import (
                detect_over_provisioned_namespaces,
            )

            result = detect_over_provisioned_namespaces()

        assert result["error"] is None
        assert len(result["namespaces"]) == 1
        ns = result["namespaces"][0]  # type: ignore[index]
        assert ns["namespace"] == "dev"
        assert ns["is_over_provisioned"] is True
        assert result["prometheus_available"] is True

    def test_empty_returns_empty_list_no_error(self) -> None:
        from hexawyn.application.ports.driven.namespace_waste_port import NamespaceWasteAnalysisPort

        mock_adapter = MagicMock(spec=NamespaceWasteAnalysisPort)
        mock_adapter.get_all_namespace_waste_data.return_value = []

        with patch("hexawyn.mcp.server.build_waste_adapter", return_value=mock_adapter):
            from hexawyn.mcp.tools.detect_over_provisioned_namespaces import (
                detect_over_provisioned_namespaces,
            )

            result = detect_over_provisioned_namespaces()

        assert result["namespaces"] == []
        assert result["error"] is None

    def test_cluster_error_returns_error_field(self) -> None:
        from hexawyn.application.ports.driven.namespace_waste_port import NamespaceWasteAnalysisPort
        from hexawyn.domain.errors import ClusterUnreachableError

        mock_adapter = MagicMock(spec=NamespaceWasteAnalysisPort)
        mock_adapter.get_all_namespace_waste_data.side_effect = ClusterUnreachableError(
            "connection refused"
        )

        with patch("hexawyn.mcp.server.build_waste_adapter", return_value=mock_adapter):
            from hexawyn.mcp.tools.detect_over_provisioned_namespaces import (
                detect_over_provisioned_namespaces,
            )

            result = detect_over_provisioned_namespaces()

        assert result["error"] is not None
        assert result["namespaces"] == []

    def test_excluded_namespace_in_response(self) -> None:
        from hexawyn.application.ports.driven.namespace_waste_port import NamespaceWasteAnalysisPort

        mock_adapter = MagicMock(spec=NamespaceWasteAnalysisPort)
        mock_adapter.get_all_namespace_waste_data.return_value = [
            {
                "namespace": "new-ns",
                "cpu_requested_cores": 4.0,
                "memory_requested_gb": 8.0,
                "cpu_actual_avg_cores": None,
                "memory_actual_avg_gb": None,
                "age_hours": 6.0,
                "has_resource_requests": True,
            },
        ]

        with patch("hexawyn.mcp.server.build_waste_adapter", return_value=mock_adapter):
            from hexawyn.mcp.tools.detect_over_provisioned_namespaces import (
                detect_over_provisioned_namespaces,
            )

            result = detect_over_provisioned_namespaces()

        assert result["namespaces"] == []
        excluded = result["excluded"]  # type: ignore[index]
        assert len(excluded) == 1
        assert excluded[0]["namespace"] == "new-ns"


class TestMCPTopologyAdapterFactories:
    def test_build_kubernetes_topology_adapter_returns_kubernetes_topology_port(self) -> None:
        from hexawyn.application.ports.driven.kubernetes_topology_port import (
            KubernetesTopologyPort,
        )
        from hexawyn.mcp.server import build_kubernetes_topology_adapter

        result = build_kubernetes_topology_adapter()

        assert isinstance(result, KubernetesTopologyPort)

    def test_build_istio_topology_adapter_returns_istio_topology_port(self) -> None:
        from hexawyn.application.ports.driven.istio_topology_port import IstioTopologyPort
        from hexawyn.mcp.server import build_istio_topology_adapter

        result = build_istio_topology_adapter()

        assert isinstance(result, IstioTopologyPort)

    def test_build_topology_snapshot_adapter_returns_topology_snapshot_port(self) -> None:
        from hexawyn.application.ports.driven.topology_snapshot_port import TopologySnapshotPort
        from hexawyn.mcp.server import build_topology_snapshot_adapter

        with patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()):
            result = build_topology_snapshot_adapter()

        assert isinstance(result, TopologySnapshotPort)

    def test_build_cross_namespace_traffic_adapter_returns_cross_namespace_traffic_port(
        self,
    ) -> None:
        from hexawyn.application.ports.driven.cross_namespace_traffic_port import (
            CrossNamespaceTrafficPort,
        )
        from hexawyn.mcp.server import build_cross_namespace_traffic_adapter

        result = build_cross_namespace_traffic_adapter()

        assert isinstance(result, CrossNamespaceTrafficPort)

    def test_build_probe_audit_adapter_returns_probe_audit_port(self) -> None:
        from hexawyn.application.ports.driven.probe_audit_port import ProbeAuditPort
        from hexawyn.mcp.server import build_probe_audit_adapter

        result = build_probe_audit_adapter()

        assert isinstance(result, ProbeAuditPort)

    def test_build_error_budget_adapter_returns_error_budget_port(self) -> None:
        from hexawyn.application.ports.driven.error_budget_port import ErrorBudgetPort
        from hexawyn.mcp.server import build_error_budget_adapter

        with patch(
            "hexawyn.mcp.server.build_metrics_query_adapter",
            return_value=MagicMock(),
        ):
            result = build_error_budget_adapter()

        assert isinstance(result, ErrorBudgetPort)


class TestMCPClusterResourceMetricsFactory:
    def test_returns_prometheus_adapter_when_not_eks(self) -> None:
        from hexawyn.adapters.secondary.gitops.prometheus_cluster_resource_metrics_adapter import (
            PrometheusClusterResourceMetricsAdapter,
        )
        from hexawyn.application.ports.driven.cluster_resource_metrics_port import (
            ClusterResourceMetricsPort,
        )
        from hexawyn.mcp.server import build_cluster_resource_metrics_adapter

        with (
            patch("hexawyn.mcp.server._is_datadog_enabled", return_value=False),
            patch("hexawyn.mcp.server._is_aws_eks_context", return_value=False),
            patch("hexawyn.mcp.server.build_metrics_query_adapter", return_value=MagicMock()),
        ):
            result = build_cluster_resource_metrics_adapter()

        assert isinstance(result, ClusterResourceMetricsPort)
        assert isinstance(result, PrometheusClusterResourceMetricsAdapter)

    def test_returns_cloudwatch_adapter_when_eks(self) -> None:
        from hexawyn.adapters.secondary.aws.cloudwatch_metrics_adapter import (
            CloudWatchClusterResourceMetricsAdapter,
        )
        from hexawyn.mcp.server import build_cluster_resource_metrics_adapter

        with (
            patch("hexawyn.mcp.server._is_datadog_enabled", return_value=False),
            patch("hexawyn.mcp.server._is_aws_eks_context", return_value=True),
        ):
            result = build_cluster_resource_metrics_adapter()

        assert isinstance(result, CloudWatchClusterResourceMetricsAdapter)

    def test_returns_datadog_adapter_when_enabled(self) -> None:
        from hexawyn.adapters.secondary.datadog.datadog_metrics_adapter import (
            DatadogClusterResourceMetricsAdapter,
        )
        from hexawyn.mcp.server import build_cluster_resource_metrics_adapter

        with patch("hexawyn.mcp.server._is_datadog_enabled", return_value=True):
            result = build_cluster_resource_metrics_adapter()

        assert isinstance(result, DatadogClusterResourceMetricsAdapter)


class TestMCPDatadogDetection:
    def test_override_datadog_enables(self) -> None:
        from hexawyn.mcp.server import _current_cluster_context, _is_datadog_enabled

        with patch(
            "hexawyn.infrastructure.config.stack_config.get_stack_override", return_value="datadog"
        ):
            assert _is_datadog_enabled(_current_cluster_context()) is True

    def test_override_other_provider_disables_datadog(self) -> None:
        from hexawyn.mcp.server import _current_cluster_context, _is_datadog_enabled

        with patch(
            "hexawyn.infrastructure.config.stack_config.get_stack_override", return_value="aws"
        ):
            assert _is_datadog_enabled(_current_cluster_context()) is False

    def test_env_configured_enables_when_no_override(self) -> None:
        from hexawyn.mcp.server import _current_cluster_context, _is_datadog_enabled

        with (
            patch(
                "hexawyn.infrastructure.config.stack_config.get_stack_override", return_value=None
            ),
            patch(
                "hexawyn.infrastructure.config.datadog_config.is_datadog_configured",
                return_value=True,
            ),
        ):
            assert _is_datadog_enabled(_current_cluster_context()) is True


class TestMCPTraceQueryFactory:
    def test_returns_otel_stub_when_not_eks(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_http_adapter import OTelHTTPAdapter
        from hexawyn.application.ports.driven.trace_query_port import TraceQueryPort
        from hexawyn.mcp.server import build_trace_query_adapter

        with (
            patch("hexawyn.mcp.server._is_datadog_enabled", return_value=False),
            patch("hexawyn.mcp.server._is_aws_eks_context", return_value=False),
        ):
            result = build_trace_query_adapter()

        assert isinstance(result, TraceQueryPort)
        assert isinstance(result, OTelHTTPAdapter)

    def test_returns_xray_adapter_when_eks(self) -> None:
        from hexawyn.adapters.secondary.aws.xray_trace_adapter import AWSXRayTraceAdapter
        from hexawyn.mcp.server import build_trace_query_adapter

        with (
            patch("hexawyn.mcp.server._is_datadog_enabled", return_value=False),
            patch("hexawyn.mcp.server._is_aws_eks_context", return_value=True),
        ):
            result = build_trace_query_adapter()

        assert isinstance(result, AWSXRayTraceAdapter)

    def test_returns_cloud_trace_adapter_when_gke(self) -> None:
        from hexawyn.adapters.secondary.gcp.cloud_trace_adapter import GCPCloudTraceAdapter
        from hexawyn.mcp.server import build_trace_query_adapter

        with (
            patch("hexawyn.mcp.server._is_datadog_enabled", return_value=False),
            patch("hexawyn.mcp.server._is_aws_eks_context", return_value=False),
            patch("hexawyn.mcp.server._is_gcp_gke_context", return_value=True),
        ):
            result = build_trace_query_adapter()

        assert isinstance(result, GCPCloudTraceAdapter)

    def test_returns_azure_monitor_traces_adapter_when_aks(self) -> None:
        from hexawyn.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )
        from hexawyn.mcp.server import build_trace_query_adapter

        with (
            patch("hexawyn.mcp.server._is_datadog_enabled", return_value=False),
            patch("hexawyn.mcp.server._is_aws_eks_context", return_value=False),
            patch("hexawyn.mcp.server._is_gcp_gke_context", return_value=False),
            patch("hexawyn.mcp.server._is_azure_aks_context", return_value=True),
        ):
            result = build_trace_query_adapter()

        assert isinstance(result, AzureMonitorTracesAdapter)

    def test_returns_datadog_traces_adapter_when_enabled(self) -> None:
        from hexawyn.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )
        from hexawyn.mcp.server import build_trace_query_adapter

        with patch("hexawyn.mcp.server._is_datadog_enabled", return_value=True):
            result = build_trace_query_adapter()

        assert isinstance(result, DatadogTracesAdapter)


class TestMCPStackOverride:
    def test_override_aws_forces_eks_context(self) -> None:
        from hexawyn.mcp.server import _current_cluster_context, _is_aws_eks_context

        with patch(
            "hexawyn.infrastructure.config.stack_config.get_stack_override", return_value="aws"
        ):
            assert _is_aws_eks_context(_current_cluster_context()) is True

    def test_override_vanilla_forces_non_eks(self) -> None:
        from hexawyn.mcp.server import _current_cluster_context, _is_aws_eks_context

        with patch(
            "hexawyn.infrastructure.config.stack_config.get_stack_override", return_value="vanilla"
        ):
            assert _is_aws_eks_context(_current_cluster_context()) is False

    def test_override_gcp_disables_eks(self) -> None:
        from hexawyn.mcp.server import _current_cluster_context, _is_aws_eks_context

        with patch(
            "hexawyn.infrastructure.config.stack_config.get_stack_override", return_value="gcp"
        ):
            assert _is_aws_eks_context(_current_cluster_context()) is False

    def test_auto_detection_used_when_no_override(self) -> None:
        from hexawyn.mcp.server import _current_cluster_context, _is_aws_eks_context

        with (
            patch(
                "hexawyn.infrastructure.config.stack_config.get_stack_override", return_value=None
            ),
            patch(
                "hexawyn.adapters.secondary.aws.aws_eks_provider.AWSEKSProvider.supports",
                return_value=True,
            ),
        ):
            assert _is_aws_eks_context(_current_cluster_context()) is True

    def test_auto_detection_swallows_provider_errors(self) -> None:
        from hexawyn.mcp.server import _current_cluster_context, _is_aws_eks_context

        with (
            patch(
                "hexawyn.infrastructure.config.stack_config.get_stack_override", return_value=None
            ),
            patch(
                "hexawyn.adapters.secondary.aws.aws_eks_provider.AWSEKSProvider.supports",
                side_effect=RuntimeError("boom"),
            ),
        ):
            assert _is_aws_eks_context(_current_cluster_context()) is False


class TestMCPMetricsQueryFactory:
    def test_returns_prometheus_http_adapter_when_not_gke(self) -> None:
        from hexawyn.adapters.secondary.gitops.prometheus_http_adapter import PrometheusHTTPAdapter
        from hexawyn.mcp.server import build_metrics_query_adapter

        with patch("hexawyn.mcp.server._is_gcp_gke_context", return_value=False):
            result = build_metrics_query_adapter()

        assert isinstance(result, PrometheusHTTPAdapter)

    def test_returns_managed_prometheus_adapter_when_gke(self) -> None:
        from hexawyn.adapters.secondary.gcp.managed_prometheus_adapter import (
            GCPManagedPrometheusAdapter,
        )
        from hexawyn.mcp.server import build_metrics_query_adapter

        with patch("hexawyn.mcp.server._is_gcp_gke_context", return_value=True):
            result = build_metrics_query_adapter()

        assert isinstance(result, GCPManagedPrometheusAdapter)

    def test_returns_azure_monitor_adapter_when_aks(self) -> None:
        from hexawyn.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )
        from hexawyn.mcp.server import build_metrics_query_adapter

        with (
            patch("hexawyn.mcp.server._is_gcp_gke_context", return_value=False),
            patch("hexawyn.mcp.server._is_azure_aks_context", return_value=True),
        ):
            result = build_metrics_query_adapter()

        assert isinstance(result, AzureMonitorMetricsAdapter)


class TestMCPGkeContextDetection:
    def test_override_gcp_forces_gke(self) -> None:
        from hexawyn.mcp.server import _current_cluster_context, _is_gcp_gke_context

        with patch(
            "hexawyn.infrastructure.config.stack_config.get_stack_override", return_value="gcp"
        ):
            assert _is_gcp_gke_context(_current_cluster_context()) is True

    def test_override_vanilla_disables_gke(self) -> None:
        from hexawyn.mcp.server import _current_cluster_context, _is_gcp_gke_context

        with patch(
            "hexawyn.infrastructure.config.stack_config.get_stack_override", return_value="vanilla"
        ):
            assert _is_gcp_gke_context(_current_cluster_context()) is False

    def test_auto_detection_swallows_provider_errors(self) -> None:
        from hexawyn.mcp.server import _current_cluster_context, _is_gcp_gke_context

        with (
            patch(
                "hexawyn.infrastructure.config.stack_config.get_stack_override", return_value=None
            ),
            patch(
                "hexawyn.adapters.secondary.gcp.gcp_gke_provider.GCPGKEProvider.supports",
                side_effect=RuntimeError("boom"),
            ),
        ):
            assert _is_gcp_gke_context(_current_cluster_context()) is False

    def test_azure_override_forces_aks(self) -> None:
        from hexawyn.mcp.server import _current_cluster_context, _is_azure_aks_context

        with patch(
            "hexawyn.infrastructure.config.stack_config.get_stack_override", return_value="azure"
        ):
            assert _is_azure_aks_context(_current_cluster_context()) is True

    def test_azure_override_disables_gke_and_eks(self) -> None:
        from hexawyn.mcp.server import (
            _current_cluster_context,
            _is_aws_eks_context,
            _is_gcp_gke_context,
        )

        with patch(
            "hexawyn.infrastructure.config.stack_config.get_stack_override", return_value="azure"
        ):
            ctx = _current_cluster_context()
            assert _is_aws_eks_context(ctx) is False
            assert _is_gcp_gke_context(ctx) is False


class TestMCPLogSearchFactory:
    def test_returns_kubernetes_adapter_when_not_eks(self) -> None:
        from hexawyn.adapters.secondary.gitops.kubernetes_pod_log_search_adapter import (
            KubernetesPodLogSearchAdapter,
        )
        from hexawyn.application.ports.driven.log_search_port import LogSearchPort
        from hexawyn.mcp.server import build_log_search_adapter

        with (
            patch("hexawyn.mcp.server._is_datadog_enabled", return_value=False),
            patch("hexawyn.mcp.server._is_aws_eks_context", return_value=False),
        ):
            result = build_log_search_adapter()

        assert isinstance(result, LogSearchPort)
        assert isinstance(result, KubernetesPodLogSearchAdapter)

    def test_returns_cloudwatch_logs_adapter_when_eks(self) -> None:
        from hexawyn.adapters.secondary.aws.cloudwatch_logs_adapter import CloudWatchLogsAdapter
        from hexawyn.mcp.server import build_log_search_adapter

        with (
            patch("hexawyn.mcp.server._is_datadog_enabled", return_value=False),
            patch("hexawyn.mcp.server._is_aws_eks_context", return_value=True),
        ):
            result = build_log_search_adapter()

        assert isinstance(result, CloudWatchLogsAdapter)

    def test_returns_cloud_logging_adapter_when_gke(self) -> None:
        from hexawyn.adapters.secondary.gcp.cloud_logging_adapter import GCPCloudLoggingAdapter
        from hexawyn.mcp.server import build_log_search_adapter

        with (
            patch("hexawyn.mcp.server._is_datadog_enabled", return_value=False),
            patch("hexawyn.mcp.server._is_aws_eks_context", return_value=False),
            patch("hexawyn.mcp.server._is_gcp_gke_context", return_value=True),
        ):
            result = build_log_search_adapter()

        assert isinstance(result, GCPCloudLoggingAdapter)

    def test_returns_log_analytics_adapter_when_aks(self) -> None:
        from hexawyn.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )
        from hexawyn.mcp.server import build_log_search_adapter

        with (
            patch("hexawyn.mcp.server._is_datadog_enabled", return_value=False),
            patch("hexawyn.mcp.server._is_aws_eks_context", return_value=False),
            patch("hexawyn.mcp.server._is_gcp_gke_context", return_value=False),
            patch("hexawyn.mcp.server._is_azure_aks_context", return_value=True),
        ):
            result = build_log_search_adapter()

        assert isinstance(result, AzureLogAnalyticsAdapter)

    def test_returns_datadog_logs_adapter_when_enabled(self) -> None:
        from hexawyn.adapters.secondary.datadog.datadog_logs_adapter import DatadogLogsAdapter
        from hexawyn.mcp.server import build_log_search_adapter

        with patch("hexawyn.mcp.server._is_datadog_enabled", return_value=True):
            result = build_log_search_adapter()

        assert isinstance(result, DatadogLogsAdapter)

    def test_build_reliability_report_adapter_returns_weekly_reliability_report_port(
        self,
    ) -> None:
        from hexawyn.application.ports.driven.weekly_reliability_report_port import (
            WeeklyReliabilityReportPort,
        )
        from hexawyn.mcp.server import build_reliability_report_adapter

        with patch(
            "hexawyn.mcp.server.build_metrics_query_adapter",
            return_value=MagicMock(),
        ):
            result = build_reliability_report_adapter()

        assert isinstance(result, WeeklyReliabilityReportPort)

    def test_build_helm_release_version_adapter_returns_helm_release_version_port(
        self,
    ) -> None:
        from hexawyn.application.ports.driven.helm_release_version_port import (
            HelmReleaseVersionPort,
        )
        from hexawyn.mcp.server import build_helm_release_version_adapter

        result = build_helm_release_version_adapter()

        assert isinstance(result, HelmReleaseVersionPort)

    def test_build_helm_values_diff_adapter_returns_helm_values_diff_port(self) -> None:
        from hexawyn.application.ports.driven.helm_values_diff_port import (
            HelmValuesDiffPort,
        )
        from hexawyn.mcp.server import build_helm_values_diff_adapter

        result = build_helm_values_diff_adapter()

        assert isinstance(result, HelmValuesDiffPort)

    def test_build_kustomize_patch_analysis_adapter_returns_kustomize_patch_analysis_port(
        self,
    ) -> None:
        from hexawyn.application.ports.driven.kustomize_patch_analysis_port import (
            KustomizePatchAnalysisPort,
        )
        from hexawyn.mcp.server import build_kustomize_patch_analysis_adapter

        result = build_kustomize_patch_analysis_adapter()

        assert isinstance(result, KustomizePatchAnalysisPort)

    def test_build_service_cost_adapter_returns_service_cost_port(self) -> None:
        from hexawyn.application.ports.driven.service_cost_port import ServiceCostPort
        from hexawyn.mcp.server import build_service_cost_adapter

        result = build_service_cost_adapter()

        assert isinstance(result, ServiceCostPort)

    def test_build_team_cost_adapter_returns_team_cost_port(self) -> None:
        from hexawyn.application.ports.driven.team_cost_port import TeamCostPort
        from hexawyn.mcp.server import build_team_cost_adapter

        result = build_team_cost_adapter()

        assert isinstance(result, TeamCostPort)

    def test_build_monthly_incident_adapter_returns_monthly_incident_port(self) -> None:
        from hexawyn.application.ports.driven.monthly_incident_port import (
            MonthlyIncidentPort,
        )
        from hexawyn.mcp.server import build_monthly_incident_adapter

        result = build_monthly_incident_adapter()

        assert isinstance(result, MonthlyIncidentPort)

    def test_build_mttr_trend_adapter_returns_mttr_trend_port(self) -> None:
        from hexawyn.application.ports.driven.mttr_trend_port import MTTRTrendPort
        from hexawyn.mcp.server import build_mttr_trend_adapter

        result = build_mttr_trend_adapter()

        assert isinstance(result, MTTRTrendPort)

    def test_build_recurring_incident_adapter_returns_recurring_incident_port(
        self,
    ) -> None:
        from hexawyn.application.ports.driven.recurring_incident_port import (
            RecurringIncidentPort,
        )
        from hexawyn.mcp.server import build_recurring_incident_adapter

        result = build_recurring_incident_adapter()

        assert isinstance(result, RecurringIncidentPort)

    def test_build_tls_compliance_adapter_returns_tls_compliance_port(self) -> None:
        from hexawyn.application.ports.driven.tls_compliance_port import (
            TLSCompliancePort,
        )
        from hexawyn.mcp.server import build_tls_compliance_adapter

        result = build_tls_compliance_adapter()

        assert isinstance(result, TLSCompliancePort)

    def test_build_security_posture_adapter_returns_port(self) -> None:
        from hexawyn.application.ports.driven.security_posture_port import (
            SecurityPosturePort,
        )
        from hexawyn.mcp.server import build_security_posture_adapter

        result = build_security_posture_adapter()

        assert isinstance(result, SecurityPosturePort)

    def test_build_cluster_operator_status_adapter_returns_port(self) -> None:
        from hexawyn.application.ports.driven.cluster_operator_status_port import (
            ClusterOperatorStatusPort,
        )
        from hexawyn.mcp.server import build_cluster_operator_status_adapter

        result = build_cluster_operator_status_adapter()

        assert isinstance(result, ClusterOperatorStatusPort)

    def test_build_machine_config_pool_adapter_returns_port(self) -> None:
        from hexawyn.application.ports.driven.machine_config_pool_port import (
            MachineConfigPoolPort,
        )
        from hexawyn.mcp.server import build_machine_config_pool_adapter

        result = build_machine_config_pool_adapter()

        assert isinstance(result, MachineConfigPoolPort)
