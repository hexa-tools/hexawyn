"""Tests for Azure monitor traces, log analytics, cost adapter and GCP cloud trace."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestAzureMonitorTracesAdapter:
    """Cover AzureMonitorTracesAdapter."""

    def test_instantiation(self) -> None:
        from hexawyn.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )
        from hexawyn.application.ports.driven.trace_query_port import TraceQueryPort

        adapter = AzureMonitorTracesAdapter(workspace_id="ws-123")
        assert isinstance(adapter, TraceQueryPort)

    def test_fetch_slow_spans_empty(self) -> None:
        from hexawyn.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )
        from hexawyn.application.ports.driven.trace_query_port import (
            LatencyDiagnosticRequest,
        )

        adapter = AzureMonitorTracesAdapter(workspace_id="ws-123")
        with patch.object(adapter, "_query", return_value=None):
            request = LatencyDiagnosticRequest(
                service_name="svc",
                time_window_minutes=30,
            )
            result = adapter.fetch_slow_spans(request)
            assert result == []

    def test_fetch_slow_spans_with_data(self) -> None:
        from hexawyn.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )
        from hexawyn.application.ports.driven.trace_query_port import (
            LatencyDiagnosticRequest,
        )

        mock_table = MagicMock()
        mock_table.columns = [
            "operation_Id",
            "name",
            "duration",
            "cloud_RoleName",
            "timestamp",
            "sdkVersion",
        ]
        adapter = AzureMonitorTracesAdapter(workspace_id="ws-123")
        with patch.object(adapter, "_query", return_value=mock_table):
            request = LatencyDiagnosticRequest(
                service_name="svc",
                time_window_minutes=30,
            )
            result = adapter.fetch_slow_spans(request)
            assert isinstance(result, list)


class TestAzureLogAnalyticsAdapter:
    """Cover AzureLogAnalyticsAdapter."""

    def test_instantiation(self) -> None:
        from hexawyn.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )
        from hexawyn.application.ports.driven.log_search_port import LogSearchPort

        adapter = AzureLogAnalyticsAdapter(workspace_id="ws-123")
        assert isinstance(adapter, LogSearchPort)

    def test_fetch_pod_container_logs_empty(self) -> None:
        from hexawyn.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        adapter = AzureLogAnalyticsAdapter(workspace_id="ws-123")
        with patch.object(adapter, "_query", return_value=None):
            result = adapter.fetch_pod_container_logs("pod", "ns", 30)
            assert result == []

    def test_fetch_pod_container_logs_with_data(self) -> None:
        from hexawyn.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        mock_table = MagicMock()
        mock_table.columns = ["ContainerID", "LogMessage", "LogSource", "TimeGenerated", "Computer"]
        mock_table.rows = [("cid1", "log line", "stdout", "2024-01-01", "node")]

        adapter = AzureLogAnalyticsAdapter(workspace_id="ws-123")
        with patch.object(adapter, "_query", return_value=mock_table):
            result = adapter.fetch_pod_container_logs("pod", "ns", 30)
            assert isinstance(result, list)

    def test_query_with_injected_client(self) -> None:
        from hexawyn.adapters.secondary.azure.log_analytics_adapter import (
            AzureLogAnalyticsAdapter,
        )

        mock_logs = MagicMock()
        mock_result = MagicMock()
        mock_result.tables = []
        mock_logs.query_workspace.return_value = mock_result

        adapter = AzureLogAnalyticsAdapter(workspace_id="ws-123", logs_client=mock_logs)
        result = adapter._query("some kql", 30)
        assert result is None


class TestGCPCloudTraceAdapter:
    """Cover GCPCloudTraceAdapter."""

    def test_instantiation(self) -> None:
        from hexawyn.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.application.ports.driven.trace_query_port import TraceQueryPort

        adapter = GCPCloudTraceAdapter(project_id="myproj")
        assert isinstance(adapter, TraceQueryPort)

    def test_fetch_slow_spans(self) -> None:
        from hexawyn.adapters.secondary.gcp.cloud_trace_adapter import (
            GCPCloudTraceAdapter,
        )
        from hexawyn.application.ports.driven.trace_query_port import (
            LatencyDiagnosticRequest,
        )

        adapter = GCPCloudTraceAdapter(project_id="myproj")
        with patch.object(adapter, "_list_traces", return_value=[]):
            request = LatencyDiagnosticRequest(
                service_name="svc",
                time_window_minutes=30,
            )
            result = adapter.fetch_slow_spans(request)
            assert result == []


class TestAzureCostAdapter:
    """Cover AzureCostAdapter."""

    def test_instantiation(self) -> None:
        from hexawyn.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )
        from hexawyn.application.ports.driven.cost_estimation_port import (
            CostEstimationPort,
        )

        adapter = AzureCostAdapter(subscription_id="sub-123")
        assert isinstance(adapter, CostEstimationPort)

    def test_estimate_cluster_cost_with_injected_client(self) -> None:
        from hexawyn.adapters.secondary.azure.azure_cost_adapter import (
            AzureCostAdapter,
        )

        mock_client = MagicMock()
        mock_client.query_usage.return_value = {"properties": {"rows": []}}

        adapter = AzureCostAdapter(subscription_id="sub-123", cm_client=mock_client)
        result = adapter.estimate_cluster_cost("aks-prod")
        assert isinstance(result, dict)
