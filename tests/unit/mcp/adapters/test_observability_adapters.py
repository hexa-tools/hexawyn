"""Tests for observability_adapters.py — all build_*_adapter() functions."""

from __future__ import annotations

from unittest.mock import patch

import pytest
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


class TestObservabilityAdapterFactories:
    """Verify each build_*_adapter() returns the correct port type."""

    @pytest.fixture(autouse=True)
    def _setup(self) -> None:
        from hexawyn.mcp.adapters import observability_adapters as adapter_mod

        self.adapter_mod = adapter_mod

    def test_build_span_bottleneck_adapter(self) -> None:
        result = self.adapter_mod.build_span_bottleneck_adapter()
        assert isinstance(result, SpanBottleneckPort)

    def test_build_latency_percentile_adapter(self) -> None:
        result = self.adapter_mod.build_latency_percentile_adapter()
        assert isinstance(result, LatencyPercentilePort)

    def test_build_metric_correlation_adapter(self) -> None:
        result = self.adapter_mod.build_metric_correlation_adapter()
        assert isinstance(result, MetricCorrelationPort)

    def test_build_metrics_query_adapter(self) -> None:
        from hexawyn.application.ports.driven.k8s_port import ClusterContext

        mock_context: ClusterContext = {
            "name": "vanilla",
            "cluster": "test",
            "provider": "vanilla",
            "namespace": "ns",
        }
        with patch.object(self.adapter_mod, "_current_cluster_context", return_value=mock_context):
            result = self.adapter_mod.build_metrics_query_adapter()
            assert isinstance(result, MetricsQueryPort)

    def test_build_cross_namespace_traffic_adapter(self) -> None:
        result = self.adapter_mod.build_cross_namespace_traffic_adapter()
        assert isinstance(result, CrossNamespaceTrafficPort)

    def test_build_trace_log_correlation_adapter(self) -> None:
        result = self.adapter_mod.build_trace_log_correlation_adapter()
        assert isinstance(result, TraceLogCorrelationPort)

    def test_build_service_dependency_graph_adapter(self) -> None:
        result = self.adapter_mod.build_service_dependency_graph_adapter()
        assert isinstance(result, ServiceDependencyGraphPort)

    def test_build_trace_event_correlation_adapter(self) -> None:
        result = self.adapter_mod.build_trace_event_correlation_adapter()
        assert isinstance(result, TraceEventCorrelationPort)

    def test_build_trace_query_adapter(self) -> None:
        result = self.adapter_mod.build_trace_query_adapter()
        assert isinstance(result, TraceQueryPort)

    def test_build_slow_trace_search_adapter(self) -> None:
        result = self.adapter_mod.build_slow_trace_search_adapter()
        assert isinstance(result, SlowTraceSearchPort)

    def test_build_deployment_latency_comparison_adapter(self) -> None:
        result = self.adapter_mod.build_deployment_latency_comparison_adapter()
        assert isinstance(result, DeploymentLatencyComparisonPort)

    def test_build_redundant_call_detection_adapter(self) -> None:
        result = self.adapter_mod.build_redundant_call_detection_adapter()
        assert isinstance(result, RedundantCallDetectionPort)

    def test_build_error_attribution_adapter(self) -> None:
        result = self.adapter_mod.build_error_attribution_adapter()
        assert isinstance(result, ErrorAttributionPort)

    def test_build_slo_breach_prediction_adapter(self) -> None:
        result = self.adapter_mod.build_slo_breach_prediction_adapter()
        assert isinstance(result, SLOBreachPredictionPort)

    def test_build_pod_logs_adapter(self) -> None:
        result = self.adapter_mod.build_pod_logs_adapter()
        assert isinstance(result, PodLogsPort)

    def test_build_log_search_adapter(self) -> None:
        result = self.adapter_mod.build_log_search_adapter()
        assert isinstance(result, LogSearchPort)

    def test_build_pod_metrics_baseline_adapter(self) -> None:
        result = self.adapter_mod.build_pod_metrics_baseline_adapter()
        assert isinstance(result, PodMetricsBaselinePort)

    def test_build_namespace_events_adapter(self) -> None:
        result = self.adapter_mod.build_namespace_events_adapter()
        assert isinstance(result, NamespaceEventsPort)

    def test_build_namespace_overview_adapter(self) -> None:
        result = self.adapter_mod.build_namespace_overview_adapter()
        assert isinstance(result, NamespaceOverviewPort)

    def test_build_pod_log_watch_adapter(self) -> None:
        result = self.adapter_mod.build_pod_log_watch_adapter()
        assert isinstance(result, PodLogWatchPort)

    def test_build_error_budget_adapter(self) -> None:
        result = self.adapter_mod.build_error_budget_adapter()
        assert isinstance(result, ErrorBudgetPort)


class TestCloudBuilderBranches:
    """Cover GCP, Azure, Datadog, AWS branches in observability builders."""

    @pytest.fixture(autouse=True)
    def _setup(self) -> None:
        from hexawyn.mcp.adapters import observability_adapters as adapter_mod

        self.adapter_mod = adapter_mod

    def test_metrics_query_gcp_gke_branch(self) -> None:
        from hexawyn.application.ports.driven.k8s_port import ClusterContext

        gcp_ctx: ClusterContext = {
            "name": "gke_myproj_us-central1-a_mycluster",
            "cluster": "gke",
            "provider": "gcp",
            "namespace": "default",
        }
        with patch(
            "hexawyn.mcp.adapters.observability_adapters._current_cluster_context",
            return_value=gcp_ctx,
        ):
            with patch(
                "hexawyn.mcp.adapters.observability_adapters._is_gcp_gke_context",
                return_value=True,
            ):
                with patch(
                    "hexawyn.mcp.adapters.observability_adapters._is_azure_aks_context",
                    return_value=False,
                ):
                    result = self.adapter_mod.build_metrics_query_adapter()
                    assert isinstance(result, MetricsQueryPort)

    def test_metrics_query_azure_aks_branch(self) -> None:
        from hexawyn.application.ports.driven.k8s_port import ClusterContext

        az_ctx: ClusterContext = {
            "name": "aks-mycluster",
            "cluster": "aks",
            "provider": "azure",
            "namespace": "default",
        }
        with patch(
            "hexawyn.mcp.adapters.observability_adapters._current_cluster_context",
            return_value=az_ctx,
        ):
            with patch(
                "hexawyn.mcp.adapters.observability_adapters._is_gcp_gke_context",
                return_value=False,
            ):
                with patch(
                    "hexawyn.mcp.adapters.observability_adapters._is_azure_aks_context",
                    return_value=True,
                ):
                    result = self.adapter_mod.build_metrics_query_adapter()
                    assert isinstance(result, MetricsQueryPort)

    def test_trace_query_adapter_datadog_branch(self) -> None:
        with patch(
            "hexawyn.mcp.adapters.observability_adapters._current_cluster_context",
            return_value={
                "name": "vanilla",
                "cluster": "test",
                "provider": "vanilla",
                "namespace": "ns",
            },
        ):
            with patch(
                "hexawyn.mcp.adapters.observability_adapters._is_datadog_enabled",
                return_value=True,
            ):
                result = self.adapter_mod.build_trace_query_adapter()
                assert isinstance(result, TraceQueryPort)

    def test_trace_query_adapter_aws_branch(self) -> None:
        with patch(
            "hexawyn.mcp.adapters.observability_adapters._current_cluster_context",
            return_value={
                "name": "vanilla",
                "cluster": "test",
                "provider": "vanilla",
                "namespace": "ns",
            },
        ):
            with patch(
                "hexawyn.mcp.adapters.observability_adapters._is_aws_eks_context",
                return_value=True,
            ):
                with patch(
                    "hexawyn.mcp.adapters.observability_adapters._is_datadog_enabled",
                    return_value=False,
                ):
                    result = self.adapter_mod.build_trace_query_adapter()
                    assert isinstance(result, TraceQueryPort)

    def test_log_search_datadog_branch(self) -> None:
        with patch(
            "hexawyn.mcp.adapters.observability_adapters._current_cluster_context",
            return_value={
                "name": "vanilla",
                "cluster": "test",
                "provider": "vanilla",
                "namespace": "ns",
            },
        ):
            with patch(
                "hexawyn.mcp.adapters.observability_adapters._is_datadog_enabled",
                return_value=True,
            ):
                result = self.adapter_mod.build_log_search_adapter()
                assert isinstance(result, LogSearchPort)

    def test_log_search_aws_branch(self) -> None:
        with patch(
            "hexawyn.mcp.adapters.observability_adapters._current_cluster_context",
            return_value={
                "name": "vanilla",
                "cluster": "test",
                "provider": "vanilla",
                "namespace": "ns",
            },
        ):
            with patch(
                "hexawyn.mcp.adapters.observability_adapters._is_aws_eks_context",
                return_value=True,
            ):
                with patch(
                    "hexawyn.mcp.adapters.observability_adapters._is_datadog_enabled",
                    return_value=False,
                ):
                    result = self.adapter_mod.build_log_search_adapter()
                    assert isinstance(result, LogSearchPort)

    def test_log_search_gcp_branch(self) -> None:
        with patch(
            "hexawyn.mcp.adapters.observability_adapters._current_cluster_context",
            return_value={
                "name": "gke-test",
                "cluster": "gke",
                "provider": "gcp",
                "namespace": "ns",
            },
        ):
            with patch(
                "hexawyn.mcp.adapters.observability_adapters._is_gcp_gke_context",
                return_value=True,
            ):
                with patch(
                    "hexawyn.mcp.adapters.observability_adapters._is_datadog_enabled",
                    return_value=False,
                ):
                    with patch(
                        "hexawyn.mcp.adapters.observability_adapters._is_aws_eks_context",
                        return_value=False,
                    ):
                        result = self.adapter_mod.build_log_search_adapter()
                        assert isinstance(result, LogSearchPort)

    def test_log_search_azure_branch(self) -> None:
        with patch(
            "hexawyn.mcp.adapters.observability_adapters._current_cluster_context",
            return_value={
                "name": "aks-test",
                "cluster": "aks",
                "provider": "azure",
                "namespace": "ns",
            },
        ):
            with patch(
                "hexawyn.mcp.adapters.observability_adapters._is_azure_aks_context",
                return_value=True,
            ):
                with patch(
                    "hexawyn.mcp.adapters.observability_adapters._is_datadog_enabled",
                    return_value=False,
                ):
                    with patch(
                        "hexawyn.mcp.adapters.observability_adapters._is_aws_eks_context",
                        return_value=False,
                    ):
                        with patch(
                            "hexawyn.mcp.adapters.observability_adapters._is_gcp_gke_context",
                            return_value=False,
                        ):
                            result = self.adapter_mod.build_log_search_adapter()
                            assert isinstance(result, LogSearchPort)

    def test_trace_query_gcp_branch(self) -> None:
        with patch(
            "hexawyn.mcp.adapters.observability_adapters._current_cluster_context",
            return_value={
                "name": "gke-test",
                "cluster": "gke",
                "provider": "gcp",
                "namespace": "ns",
            },
        ):
            with patch(
                "hexawyn.mcp.adapters.observability_adapters._is_gcp_gke_context",
                return_value=True,
            ):
                with patch(
                    "hexawyn.mcp.adapters.observability_adapters._is_datadog_enabled",
                    return_value=False,
                ):
                    with patch(
                        "hexawyn.mcp.adapters.observability_adapters._is_aws_eks_context",
                        return_value=False,
                    ):
                        result = self.adapter_mod.build_trace_query_adapter()
                        assert isinstance(result, TraceQueryPort)

    def test_trace_query_azure_branch(self) -> None:
        with patch(
            "hexawyn.mcp.adapters.observability_adapters._current_cluster_context",
            return_value={
                "name": "aks-test",
                "cluster": "aks",
                "provider": "azure",
                "namespace": "ns",
            },
        ):
            with patch(
                "hexawyn.mcp.adapters.observability_adapters._is_azure_aks_context",
                return_value=True,
            ):
                with patch(
                    "hexawyn.mcp.adapters.observability_adapters._is_datadog_enabled",
                    return_value=False,
                ):
                    with patch(
                        "hexawyn.mcp.adapters.observability_adapters._is_aws_eks_context",
                        return_value=False,
                    ):
                        with patch(
                            "hexawyn.mcp.adapters.observability_adapters._is_gcp_gke_context",
                            return_value=False,
                        ):
                            result = self.adapter_mod.build_trace_query_adapter()
                            assert isinstance(result, TraceQueryPort)
