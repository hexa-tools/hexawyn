from datetime import timedelta
from unittest.mock import MagicMock, patch

import pytest

pytest.importorskip("azure.monitor.query")
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError  # noqa: E402
from azure.monitor.query import LogsQueryStatus  # noqa: E402
from hexawyn.application.ports.driven.trace_query_port import (  # noqa: E402
    LatencyDiagnosticRequest,
    TraceQueryPort,
)
from hexawyn.domain.errors import TracesUnavailableError  # noqa: E402

_WORKSPACE = "ws-123"


def _request() -> LatencyDiagnosticRequest:
    return LatencyDiagnosticRequest(
        service_name="checkout", time_window_minutes=15, threshold_ms=500.0
    )


def _table(columns: list[str], rows: list[list[object]]) -> MagicMock:
    table = MagicMock()
    table.columns = columns
    table.rows = rows
    return table


def _result(tables: list[MagicMock], status: object = LogsQueryStatus.SUCCESS) -> MagicMock:
    result = MagicMock()
    result.status = status
    result.tables = tables
    return result


def _adapter(client: MagicMock):
    from hexawyn.adapters.secondary.azure.monitor_traces_adapter import (
        AzureMonitorTracesAdapter,
    )

    return AzureMonitorTracesAdapter(workspace_id=_WORKSPACE, logs_client=client)


class TestContract:
    def test_is_a_trace_query_port(self) -> None:
        assert isinstance(_adapter(MagicMock()), TraceQueryPort)


class TestFetchSlowSpans:
    def test_groups_rows_by_operation_id(self) -> None:
        client = MagicMock()
        client.query_workspace.return_value = _result(
            [
                _table(
                    ["OperationId", "Name", "DurationMs"],
                    [
                        ["op1", "GET /pay", 1500.0],
                        ["op1", "SELECT db", 1200.0],
                        ["op2", "GET /cart", 900.0],
                    ],
                )
            ]
        )
        adapter = _adapter(client)

        result = adapter.fetch_slow_spans(_request())

        assert len(result) == 2
        op1 = next(spans for spans in result if spans[0].trace_id == "op1")
        names = {s.span_name: s.duration_ms for s in op1}
        assert names["GET /pay"] == 1500.0
        assert names["SELECT db"] == 1200.0

    def test_returns_empty_when_no_tables(self) -> None:
        client = MagicMock()
        client.query_workspace.return_value = _result([])
        adapter = _adapter(client)

        assert adapter.fetch_slow_spans(_request()) == []

    def test_query_includes_service_and_threshold(self) -> None:
        client = MagicMock()
        client.query_workspace.return_value = _result([])
        adapter = _adapter(client)

        adapter.fetch_slow_spans(_request())

        call = client.query_workspace.call_args
        assert call.args[0] == _WORKSPACE
        kql = call.args[1]
        assert "checkout" in kql
        assert "500" in kql
        assert call.kwargs["timespan"] == timedelta(minutes=15)

    def test_non_numeric_duration_defaults_to_zero(self) -> None:
        client = MagicMock()
        client.query_workspace.return_value = _result(
            [_table(["OperationId", "Name", "DurationMs"], [["op1", "weird", "n/a"]])]
        )
        adapter = _adapter(client)

        result = adapter.fetch_slow_spans(_request())

        assert result[0][0].duration_ms == 0.0


class TestFetchTotalTraces:
    def test_reads_count_value(self) -> None:
        client = MagicMock()
        client.query_workspace.return_value = _result([_table(["Total"], [[42]])])
        adapter = _adapter(client)

        assert adapter.fetch_total_traces(_request()) == 42

    def test_returns_zero_when_empty(self) -> None:
        client = MagicMock()
        client.query_workspace.return_value = _result([_table(["Total"], [])])
        adapter = _adapter(client)

        assert adapter.fetch_total_traces(_request()) == 0

    def test_returns_zero_when_no_tables(self) -> None:
        client = MagicMock()
        client.query_workspace.return_value = _result([])
        adapter = _adapter(client)

        assert adapter.fetch_total_traces(_request()) == 0


class TestErrorTranslation:
    def test_query_failure_status_raises(self) -> None:
        client = MagicMock()
        client.query_workspace.return_value = _result([], status=LogsQueryStatus.FAILURE)
        adapter = _adapter(client)

        with pytest.raises(TracesUnavailableError):
            adapter.fetch_slow_spans(_request())

    def test_auth_error_raises_with_hint(self) -> None:
        client = MagicMock()
        client.query_workspace.side_effect = ClientAuthenticationError("no creds")
        adapter = _adapter(client)

        with pytest.raises(TracesUnavailableError) as exc_info:
            adapter.fetch_slow_spans(_request())

        assert "az login" in str(exc_info.value).lower()

    def test_http_error_raises(self) -> None:
        client = MagicMock()
        client.query_workspace.side_effect = HttpResponseError("boom")
        adapter = _adapter(client)

        with pytest.raises(TracesUnavailableError):
            adapter.fetch_total_traces(_request())


class TestLazyClientCreation:
    def test_lazily_creates_client(self) -> None:
        created = MagicMock()
        created.query_workspace.return_value = _result([_table(["Total"], [[0]])])
        from hexawyn.adapters.secondary.azure.monitor_traces_adapter import (
            AzureMonitorTracesAdapter,
        )

        adapter = AzureMonitorTracesAdapter(workspace_id=_WORKSPACE)

        with (
            patch("azure.identity.DefaultAzureCredential", return_value=MagicMock()),
            patch("azure.monitor.query.LogsQueryClient", return_value=created) as client_cls,
        ):
            adapter.fetch_total_traces(_request())

        client_cls.assert_called_once()
