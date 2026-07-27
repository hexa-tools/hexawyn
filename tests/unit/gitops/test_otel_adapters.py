from __future__ import annotations


class TestOtelCanaryComparisonAdapter:
    def test_fetch_canary_metrics_returns_version_metrics(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_canary_comparison_adapter import (
            OTelCanaryComparisonAdapter,
        )
        from hexawyn.domain.models.canary_comparison import CanaryComparisonRequest

        adapter = OTelCanaryComparisonAdapter()
        result = adapter.fetch_canary_metrics(CanaryComparisonRequest(service_name="test"))

        assert result.version == "unknown"
        assert result.request_count >= 0

    def test_fetch_stable_metrics_returns_version_metrics(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_canary_comparison_adapter import (
            OTelCanaryComparisonAdapter,
        )
        from hexawyn.domain.models.canary_comparison import CanaryComparisonRequest

        adapter = OTelCanaryComparisonAdapter()
        result = adapter.fetch_stable_metrics(CanaryComparisonRequest(service_name="test"))

        assert result.version == "unknown"


class TestOtelVersionRegressionAdapter:
    def test_fetch_baseline_metrics_returns_metrics(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_version_regression_adapter import (
            OTelVersionRegressionAdapter,
        )
        from hexawyn.domain.models.version_regression import VersionComparisonRequest

        adapter = OTelVersionRegressionAdapter()
        result = adapter.fetch_baseline_metrics(VersionComparisonRequest(service_name="test"))

        assert result.version == "unknown"
        assert result.p50_ms >= 0.0

    def test_fetch_current_metrics_returns_metrics(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_version_regression_adapter import (
            OTelVersionRegressionAdapter,
        )
        from hexawyn.domain.models.version_regression import VersionComparisonRequest

        adapter = OTelVersionRegressionAdapter()
        result = adapter.fetch_current_metrics(VersionComparisonRequest(service_name="test"))

        assert result.version == "unknown"


class TestOtelDeploymentComparisonAdapter:
    def test_fetch_pre_deploy_latency_returns_window(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_deployment_comparison_adapter import (
            OTelDeploymentComparisonAdapter,
        )
        from hexawyn.domain.models.deployment_latency import DeploymentComparisonRequest

        adapter = OTelDeploymentComparisonAdapter()
        result = adapter.fetch_pre_deploy_latency(DeploymentComparisonRequest(service_name="test"))

        assert result.sample_count >= 0

    def test_fetch_post_deploy_latency_returns_window(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_deployment_comparison_adapter import (
            OTelDeploymentComparisonAdapter,
        )
        from hexawyn.domain.models.deployment_latency import DeploymentComparisonRequest

        adapter = OTelDeploymentComparisonAdapter()
        result = adapter.fetch_post_deploy_latency(DeploymentComparisonRequest(service_name="test"))

        assert result.p50_ms >= 0.0


class TestOtelDependencyGraphAdapter:
    def test_fetch_edges_returns_list(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_dependency_graph_adapter import (
            OTelDependencyGraphAdapter,
        )
        from hexawyn.domain.models.service_dependency_graph import DependencyGraphRequest

        adapter = OTelDependencyGraphAdapter()
        result = adapter.fetch_edges(DependencyGraphRequest())

        assert isinstance(result, list)


class TestOtelCrossNamespaceTrafficAdapter:
    def test_list_cross_namespace_flows_returns_list(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_cross_namespace_traffic_adapter import (
            OTelCrossNamespaceTrafficAdapter,
        )

        adapter = OTelCrossNamespaceTrafficAdapter()
        result = adapter.list_cross_namespace_flows()

        assert isinstance(result, list)


class TestOtelCostProfilingAdapter:
    def test_fetch_endpoint_cpu_metrics_returns_list(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_cost_profiling_adapter import (
            OTelCostProfilingAdapter,
        )
        from hexawyn.domain.models.cost_profiling import CostProfilingRequest

        adapter = OTelCostProfilingAdapter()
        result = adapter.fetch_endpoint_cpu_metrics(CostProfilingRequest())

        assert isinstance(result, list)


class TestOtelComplianceAuditAdapter:
    def test_fetch_access_matches_returns_list(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_compliance_audit_adapter import (
            OTelComplianceAuditAdapter,
        )
        from hexawyn.domain.models.sensitive_data_audit import SensitiveAccessRequest

        adapter = OTelComplianceAuditAdapter()
        result = adapter.fetch_access_matches(SensitiveAccessRequest(pattern="credit_card"))

        assert isinstance(result, list)


class TestOtelSecurityAuditAdapter:
    def test_fetch_failed_admin_calls_returns_list(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_security_audit_adapter import (
            OTelSecurityAuditAdapter,
        )
        from hexawyn.domain.models.admin_endpoint_audit import AdminAuditRequest

        adapter = OTelSecurityAuditAdapter()
        result = adapter.fetch_failed_admin_calls(AdminAuditRequest())

        assert isinstance(result, list)

    def test_fetch_total_requests_returns_int(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_security_audit_adapter import (
            OTelSecurityAuditAdapter,
        )
        from hexawyn.domain.models.admin_endpoint_audit import AdminAuditRequest

        adapter = OTelSecurityAuditAdapter()
        result = adapter.fetch_total_requests(AdminAuditRequest())

        assert isinstance(result, int)
