from __future__ import annotations

from collections.abc import Iterable, Sequence
from datetime import timedelta
from typing import Protocol, cast

from hexawyn.application.ports.driven.trace_query_port import (
    LatencyDiagnosticRequest,
    TraceQueryPort,
    TraceSpan,
)
from hexawyn.domain.errors import TracesUnavailableError

_CREDENTIALS_HINT = "Run 'az login' or attach a managed identity, then retry."
_DEPENDENCIES_TABLE = "AppDependencies"
_ROW_LIMIT = 1000


class _LogsTable(Protocol):
    columns: Sequence[str]
    rows: Iterable[Sequence[object]]


class _LogsResult(Protocol):
    status: object
    tables: Sequence[_LogsTable]


class LogsClient(Protocol):
    """Minimal contract for the azure-monitor-query LogsQueryClient used here."""

    def query_workspace(
        self, workspace_id: str, query: str, *, timespan: timedelta
    ) -> _LogsResult: ...


class AzureMonitorTracesAdapter(TraceQueryPort):
    """TraceQueryPort backed by Azure Monitor (Application Insights) via KQL.

    Reads dependency spans from the Log Analytics workspace — no Tempo/Jaeger.
    """

    def __init__(self, workspace_id: str, logs_client: LogsClient | None = None) -> None:
        self._workspace_id = workspace_id
        self._logs_client = logs_client

    def fetch_slow_spans(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is None:
            return []
        by_trace: dict[str, list[TraceSpan]] = {}
        for row in _rows_as_dicts(table):
            trace_id = str(row.get("OperationId", "unknown"))
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(row.get("Name", "unknown")),
                    duration_ms=_as_float(row.get("DurationMs")),
                )
            )
        return list(by_trace.values())

    def fetch_total_traces(self, request: LatencyDiagnosticRequest) -> int:
        table = self._query(self._total_kql(request), request.time_window_minutes)
        if table is None:
            return 0
        rows = _rows_as_dicts(table)
        if not rows:
            return 0
        return int(_as_float(next(iter(rows[0].values()), 0)))

    def _slow_kql(self, request: LatencyDiagnosticRequest) -> str:
        threshold = int(request.threshold_ms)
        return (
            f"{_DEPENDENCIES_TABLE} "
            f'| where Target contains "{request.service_name}" and DurationMs > {threshold} '
            f"| project OperationId, Name, DurationMs "
            f"| take {_ROW_LIMIT}"
        )

    def _total_kql(self, request: LatencyDiagnosticRequest) -> str:
        return (
            f"{_DEPENDENCIES_TABLE} "
            f'| where Target contains "{request.service_name}" '
            f"| summarize Total = dcount(OperationId)"
        )

    def _query(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise TracesUnavailableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"workspace": self._workspace_id},
            ) from exc
        except HttpResponseError as exc:
            raise TracesUnavailableError(
                "Unable to query Azure Monitor.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise TracesUnavailableError(
                "Azure Monitor query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def _client_or_create(self) -> LogsClient:
        client = self._logs_client
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.monitor.query import LogsQueryClient

            client = cast(LogsClient, LogsQueryClient(DefaultAzureCredential()))
            self._logs_client = client
        return client


def _rows_as_dicts(table: _LogsTable) -> list[dict[str, object]]:
    columns = list(table.columns)
    dicts: list[dict[str, object]] = []
    for row in table.rows:
        values = [row[index] for index in range(len(columns))]
        dicts.append(dict(zip(columns, values, strict=False)))
    return dicts


def _as_float(value: object) -> float:
    if isinstance(value, int | float):
        return float(value)
    try:
        return float(str(value))
    except (TypeError, ValueError):
        return 0.0
