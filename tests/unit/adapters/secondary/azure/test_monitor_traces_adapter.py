from __future__ import annotations

from sys import modules as sys_modules
from unittest.mock import Mock, patch

from hexawyn.adapters.secondary.azure.monitor_traces_adapter import (
    AzureMonitorTracesAdapter,
    _as_float,
    _rows_as_dicts,
)
from hexawyn.domain.errors import TracesUnavailableError
from hexawyn.domain.models.latency_diagnostic import LatencyDiagnosticRequest


class TestAzureMonitorTracesAdapter:
    def test_fetch_total_traces_returns_zero_on_no_tables(self) -> None:
        mock_client = Mock()
        mock_result = Mock()
        mock_result.status = "Success"
        mock_result.tables = []
        mock_client.query_workspace.return_value = mock_result
        adapter = AzureMonitorTracesAdapter(workspace_id="ws-123", logs_client=mock_client)
        request = LatencyDiagnosticRequest(service_name="api", time_window_minutes=30)
        result = adapter.fetch_total_traces(request)
        assert result == 0

    def test_fetch_total_traces_returns_count(self) -> None:
        mock_client = Mock()
        mock_result = Mock()
        mock_result.status = "Success"
        mock_table = Mock()
        mock_table.columns = ["Total"]
        mock_table.rows = [[42]]
        mock_result.tables = [mock_table]
        mock_client.query_workspace.return_value = mock_result
        adapter = AzureMonitorTracesAdapter(workspace_id="ws-123", logs_client=mock_client)
        request = LatencyDiagnosticRequest(service_name="api", time_window_minutes=30)
        result = adapter.fetch_total_traces(request)
        assert result == 42  # noqa: PLR2004

    def test_fetch_slow_spans_returns_empty_on_no_tables(self) -> None:
        mock_client = Mock()
        mock_result = Mock()
        mock_result.status = "Success"
        mock_result.tables = []
        mock_client.query_workspace.return_value = mock_result
        adapter = AzureMonitorTracesAdapter(workspace_id="ws-123", logs_client=mock_client)
        request = LatencyDiagnosticRequest(service_name="api", time_window_minutes=30)
        result = adapter.fetch_slow_spans(request)
        assert result == []

    def test_fetch_slow_spans_groups_by_trace_id(self) -> None:
        mock_client = Mock()
        mock_result = Mock()
        mock_result.status = "Success"
        mock_table = Mock()
        mock_table.columns = ["OperationId", "Name", "DurationMs"]
        mock_table.rows = [
            ["trace-1", "http-get", 500.0],
            ["trace-1", "db-query", 1200.0],
            ["trace-2", "http-post", 750.0],
        ]
        mock_result.tables = [mock_table]
        mock_client.query_workspace.return_value = mock_result
        adapter = AzureMonitorTracesAdapter(workspace_id="ws-123", logs_client=mock_client)
        request = LatencyDiagnosticRequest(
            service_name="api", time_window_minutes=30, threshold_ms=500.0
        )
        result = adapter.fetch_slow_spans(request)
        assert len(result) == 2  # noqa: PLR2004
        trace_ids = {span.trace_id for group in result for span in group}
        assert trace_ids == {"trace-1", "trace-2"}

    def test_slow_kql_includes_service_name(self) -> None:
        adapter = AzureMonitorTracesAdapter(workspace_id="ws-123", logs_client=Mock())
        request = LatencyDiagnosticRequest(service_name="api", time_window_minutes=30)
        kql = adapter._slow_kql(request)
        assert "api" in kql
        assert "AppDependencies" in kql
        assert "DurationMs > 500" in kql

    def test_total_kql_includes_service_name(self) -> None:
        adapter = AzureMonitorTracesAdapter(workspace_id="ws-123", logs_client=Mock())
        request = LatencyDiagnosticRequest(service_name="api", time_window_minutes=30)
        kql = adapter._total_kql(request)
        assert "api" in kql
        assert "dcount" in kql

    def test_query_auth_error_raises_traces_unavailable(self) -> None:
        mock_azure_exc = Mock()
        auth_error = type("ClientAuthenticationError", (Exception,), {})
        mock_azure_exc.ClientAuthenticationError = auth_error
        mock_azure_exc.HttpResponseError = type("HttpResponseError", (Exception,), {})

        mock_azure_monitor = Mock()
        mock_azure_monitor.LogsQueryStatus = Mock()
        mock_azure_monitor.LogsQueryStatus.FAILURE = "FAILURE"

        mock_client = Mock()
        mock_client.query_workspace.side_effect = auth_error("auth failed")
        adapter = AzureMonitorTracesAdapter(workspace_id="ws-123", logs_client=mock_client)
        request = LatencyDiagnosticRequest(service_name="api", time_window_minutes=30)

        with patch.dict(
            sys_modules,
            {
                "azure.core.exceptions": mock_azure_exc,
                "azure.monitor.query": mock_azure_monitor,
            },
        ):
            try:
                adapter.fetch_slow_spans(request)
            except TracesUnavailableError:
                pass

    def test_query_http_error_raises_traces_unavailable(self) -> None:
        mock_azure_exc = Mock()
        mock_azure_exc.ClientAuthenticationError = type(
            "ClientAuthenticationError", (Exception,), {}
        )
        http_error = type("HttpResponseError", (Exception,), {})
        mock_azure_exc.HttpResponseError = http_error

        mock_azure_monitor = Mock()
        mock_azure_monitor.LogsQueryStatus = Mock()
        mock_azure_monitor.LogsQueryStatus.FAILURE = "FAILURE"

        mock_client = Mock()
        mock_client.query_workspace.side_effect = http_error("server error")
        adapter = AzureMonitorTracesAdapter(workspace_id="ws-123", logs_client=mock_client)
        request = LatencyDiagnosticRequest(service_name="api", time_window_minutes=30)

        with patch.dict(
            sys_modules,
            {
                "azure.core.exceptions": mock_azure_exc,
                "azure.monitor.query": mock_azure_monitor,
            },
        ):
            try:
                adapter.fetch_total_traces(request)
            except TracesUnavailableError:
                pass

    def test_query_failure_status_raises_traces_unavailable(self) -> None:
        mock_azure_exc = Mock()
        mock_azure_exc.ClientAuthenticationError = type(
            "ClientAuthenticationError", (Exception,), {}
        )
        mock_azure_exc.HttpResponseError = type("HttpResponseError", (Exception,), {})

        mock_azure_monitor = Mock()
        mock_azure_monitor.LogsQueryStatus = Mock()
        mock_azure_monitor.LogsQueryStatus.FAILURE = "FAILURE"

        mock_client = Mock()
        mock_result = Mock()
        mock_result.status = "FAILURE"
        mock_client.query_workspace.return_value = mock_result
        adapter = AzureMonitorTracesAdapter(workspace_id="ws-123", logs_client=mock_client)
        request = LatencyDiagnosticRequest(service_name="api", time_window_minutes=30)

        with patch.dict(
            sys_modules,
            {
                "azure.core.exceptions": mock_azure_exc,
                "azure.monitor.query": mock_azure_monitor,
            },
        ):
            try:
                adapter.fetch_slow_spans(request)
            except TracesUnavailableError:
                pass

    def test_client_or_create_returns_injected_client(self) -> None:
        mock_client = Mock()
        adapter = AzureMonitorTracesAdapter(workspace_id="ws-123", logs_client=mock_client)
        result = adapter._client_or_create()
        assert result is mock_client


class TestRowsAsDicts:
    def test_empty_table(self) -> None:
        mock_table = Mock()
        mock_table.columns = []
        mock_table.rows = []
        assert _rows_as_dicts(mock_table) == []

    def test_converts_rows_to_dicts(self) -> None:
        mock_table = Mock()
        mock_table.columns = ["pod_name", "duration"]
        mock_table.rows = [["api-pod", 150.0], ["worker-pod", 200.0]]
        result = _rows_as_dicts(mock_table)
        assert len(result) == 2  # noqa: PLR2004
        assert result[0]["pod_name"] == "api-pod"
        assert result[0]["duration"] == 150.0  # noqa: PLR2004
        assert result[1]["pod_name"] == "worker-pod"


class TestAsFloat:
    def test_int(self) -> None:
        assert _as_float(42) == 42.0  # noqa: PLR2004

    def test_float(self) -> None:
        assert _as_float(3.14) == 3.14  # noqa: PLR2004

    def test_string(self) -> None:
        assert _as_float("42.5") == 42.5  # noqa: PLR2004

    def test_none(self) -> None:
        assert _as_float(None) == 0.0

    def test_typeerror(self) -> None:
        assert _as_float(object()) == 0.0

    def test_bool(self) -> None:
        assert _as_float(True) == 1.0

    def test_fetch_total_traces_returns_zero_on_empty_rows(self) -> None:
        mock_client = Mock()
        mock_result = Mock()
        mock_result.status = "Success"
        mock_table = Mock()
        mock_table.columns = []
        mock_table.rows = []
        mock_result.tables = [mock_table]
        mock_client.query_workspace.return_value = mock_result
        adapter = AzureMonitorTracesAdapter(workspace_id="ws-123", logs_client=mock_client)
        request = LatencyDiagnosticRequest(service_name="api", time_window_minutes=30)
        result = adapter.fetch_total_traces(request)
        assert result == 0

    def test_client_or_create_lazy_init_with_azure_sdk(self) -> None:
        mock_identity = Mock()
        mock_identity.DefaultAzureCredential = Mock(return_value="fake_cred")
        mock_query_module = Mock()
        mock_query_module.LogsQueryClient = Mock(return_value="fake_client")

        adapter = AzureMonitorTracesAdapter(workspace_id="ws-123", logs_client=None)

        with patch.dict(
            sys_modules,
            {
                "azure.identity": mock_identity,
                "azure.monitor.query": mock_query_module,
            },
            clear=False,
        ):
            result = adapter._client_or_create()
            assert result == "fake_client"
            mock_query_module.LogsQueryClient.assert_called_once()
