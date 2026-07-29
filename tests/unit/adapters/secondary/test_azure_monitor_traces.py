"""Comprehensive tests for Azure Monitor Traces — target 95%+ coverage."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
from hexawyn.adapters.secondary.azure.monitor_traces_adapter import (
    AzureMonitorTracesAdapter,
    _as_float,
    _rows_as_dicts,
)
from hexawyn.domain.models.latency_diagnostic import LatencyDiagnosticRequest


def _make_request(**kwargs: object) -> LatencyDiagnosticRequest:
    defaults: dict[str, object] = {
        "service_name": "payment-service",
        "time_window_minutes": 30,
        "threshold_ms": 500.0,
    }
    defaults.update(kwargs)
    return LatencyDiagnosticRequest(**defaults)  # type: ignore[arg-type]


class TestAsFloat:
    """Cover _as_float (lines 135-141)."""

    def test_int(self) -> None:
        assert _as_float(42) == 42.0  # noqa: PLR2004

    def test_float(self) -> None:
        assert _as_float(3.14) == 3.14  # noqa: PLR2004

    def test_string_number(self) -> None:
        assert _as_float("99.9") == 99.9  # noqa: PLR2004

    def test_string_int(self) -> None:
        assert _as_float("100") == 100.0  # noqa: PLR2004

    def test_invalid_string(self) -> None:
        assert _as_float("not_a_number") == 0.0  # noqa: PLR2004

    def test_none(self) -> None:
        assert _as_float(None) == 0.0  # noqa: PLR2004

    def test_list(self) -> None:
        assert _as_float([1, 2, 3]) == 0.0  # noqa: PLR2004


class TestRowsAsDicts:
    """Cover _rows_as_dicts (lines 126-132)."""

    def test_converts_rows(self) -> None:
        table = MagicMock()
        table.columns = ["col_a", "col_b"]
        table.rows = [("val1", "val2"), ("val3", "val4")]

        result = _rows_as_dicts(table)
        assert len(result) == 2  # noqa: PLR2004
        assert result[0] == {"col_a": "val1", "col_b": "val2"}
        assert result[1] == {"col_a": "val3", "col_b": "val4"}

    def test_empty_rows(self) -> None:
        table = MagicMock()
        table.columns = ["col_a"]
        table.rows = []

        result = _rows_as_dicts(table)
        assert result == []

    def test_single_row(self) -> None:
        table = MagicMock()
        table.columns = ["OperationId", "Name", "DurationMs"]
        table.rows = [("op-1", "span-1", 250)]

        result = _rows_as_dicts(table)
        assert len(result) == 1  # noqa: PLR2004
        assert result[0]["OperationId"] == "op-1"


class TestAzureMonitorTracesAdapter:
    """Cover all AzureMonitorTracesAdapter methods."""

    def test_instantiation(self) -> None:
        adapter = AzureMonitorTracesAdapter(workspace_id="ws-123")
        assert adapter._workspace_id == "ws-123"
        assert adapter._logs_client is None

    def test_slow_kql(self) -> None:
        adapter = AzureMonitorTracesAdapter(workspace_id="ws-123")
        kql = adapter._slow_kql(_make_request())
        assert "AppDependencies" in kql
        assert "payment-service" in kql
        assert "DurationMs" in kql
        assert "1000" in kql

    def test_total_kql(self) -> None:
        adapter = AzureMonitorTracesAdapter(workspace_id="ws-123")
        kql = adapter._total_kql(_make_request())
        assert "AppDependencies" in kql
        assert "payment-service" in kql
        assert "dcount" in kql

    def test_fetch_slow_spans_empty(self) -> None:
        adapter = AzureMonitorTracesAdapter(workspace_id="ws-123")
        with patch.object(adapter, "_query", return_value=None):
            result = adapter.fetch_slow_spans(_make_request())
            assert result == []

    def test_fetch_slow_spans_with_data(self) -> None:
        mock_table = MagicMock()
        mock_table.columns = ["OperationId", "Name", "DurationMs"]
        mock_table.rows = [
            ("trace-1", "http-get", 1500),
            ("trace-1", "db-query", 800),
            ("trace-2", "http-post", 200),
        ]

        adapter = AzureMonitorTracesAdapter(workspace_id="ws-123")
        with patch.object(adapter, "_query", return_value=mock_table):
            result = adapter.fetch_slow_spans(_make_request())
            assert len(result) == 2  # noqa: PLR2004
            assert len(result[0]) == 2  # noqa: PLR2004
            assert result[0][0].span_name == "http-get"

    def test_fetch_total_traces_empty(self) -> None:
        adapter = AzureMonitorTracesAdapter(workspace_id="ws-123")
        with patch.object(adapter, "_query", return_value=None):
            result = adapter.fetch_total_traces(_make_request())
            assert result == 0  # noqa: PLR2004

    def test_fetch_total_traces_with_data(self) -> None:
        mock_table = MagicMock()
        mock_table.columns = ["Total"]
        mock_table.rows = [(42,)]

        adapter = AzureMonitorTracesAdapter(workspace_id="ws-123")
        with patch.object(adapter, "_query", return_value=mock_table):
            result = adapter.fetch_total_traces(_make_request())
            assert result == 42  # noqa: PLR2004

    def test_fetch_total_traces_empty_rows(self) -> None:
        mock_table = MagicMock()
        mock_table.columns = ["Total"]
        mock_table.rows = []

        adapter = AzureMonitorTracesAdapter(workspace_id="ws-123")
        with patch.object(adapter, "_query", return_value=mock_table):
            result = adapter.fetch_total_traces(_make_request())
            assert result == 0  # noqa: PLR2004

    def test_query_with_injected_client(self) -> None:
        from azure.monitor.query import LogsQueryStatus

        mock_logs = MagicMock()
        mock_result = MagicMock()
        mock_result.status = LogsQueryStatus.SUCCESS
        mock_table = MagicMock()
        mock_table.columns = ["col"]
        mock_table.rows = []
        mock_result.tables = [mock_table]
        mock_logs.query_workspace.return_value = mock_result

        adapter = AzureMonitorTracesAdapter(workspace_id="ws-123", logs_client=mock_logs)
        result = adapter._query("some kql", 30)
        assert result is not None

    def test_query_empty_tables(self) -> None:
        from azure.monitor.query import LogsQueryStatus

        mock_logs = MagicMock()
        mock_result = MagicMock()
        mock_result.status = LogsQueryStatus.SUCCESS
        mock_result.tables = []
        mock_logs.query_workspace.return_value = mock_result

        adapter = AzureMonitorTracesAdapter(workspace_id="ws-123", logs_client=mock_logs)
        result = adapter._query("some kql", 30)
        assert result is None

    def test_query_auth_error(self) -> None:
        from azure.core.exceptions import ClientAuthenticationError
        from hexawyn.domain.errors import TracesUnavailableError

        mock_logs = MagicMock()
        mock_logs.query_workspace.side_effect = ClientAuthenticationError()

        adapter = AzureMonitorTracesAdapter(workspace_id="ws-123", logs_client=mock_logs)
        with pytest.raises(TracesUnavailableError, match="credentials"):
            adapter._query("some kql", 30)

    def test_query_http_error(self) -> None:
        from azure.core.exceptions import HttpResponseError
        from hexawyn.domain.errors import TracesUnavailableError

        mock_logs = MagicMock()
        mock_logs.query_workspace.side_effect = HttpResponseError(
            message="not found", response=MagicMock()
        )

        adapter = AzureMonitorTracesAdapter(workspace_id="ws-123", logs_client=mock_logs)
        with pytest.raises(TracesUnavailableError):
            adapter._query("some kql", 30)

    def test_query_failure_status(self) -> None:
        from azure.monitor.query import LogsQueryStatus
        from hexawyn.domain.errors import TracesUnavailableError

        mock_logs = MagicMock()
        mock_result = MagicMock()
        mock_result.status = LogsQueryStatus.FAILURE
        mock_logs.query_workspace.return_value = mock_result

        adapter = AzureMonitorTracesAdapter(workspace_id="ws-123", logs_client=mock_logs)
        with pytest.raises(TracesUnavailableError):
            adapter._query("some kql", 30)

    def test_client_or_create_lazy(self) -> None:
        adapter = AzureMonitorTracesAdapter(workspace_id="ws-123")
        assert adapter._logs_client is None
        with patch("azure.monitor.query.LogsQueryClient", return_value=MagicMock()) as mock_client:
            with patch(
                "azure.identity.DefaultAzureCredential",
                return_value=MagicMock(),
            ):
                result = adapter._client_or_create()
                mock_client.assert_called_once()
                assert result is not None
                assert adapter._logs_client is not None

    def test_client_or_create_reuses_cached(self) -> None:
        adapter = AzureMonitorTracesAdapter(workspace_id="ws-123")
        mock_client = MagicMock()
        adapter._logs_client = mock_client
        result = adapter._client_or_create()
        assert result is mock_client
