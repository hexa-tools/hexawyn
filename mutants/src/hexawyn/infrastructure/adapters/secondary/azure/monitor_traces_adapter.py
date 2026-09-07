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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


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
mutants_xǁAzureMonitorTracesAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAzureMonitorTracesAdapterǁ_slow_kql__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut: MutantDict = {}  # type: ignore


class AzureMonitorTracesAdapter(TraceQueryPort):
    """TraceQueryPort backed by Azure Monitor (Application Insights) via KQL.

    Reads dependency spans from the Log Analytics workspace — no Tempo/Jaeger.
    """

    @_mutmut_mutated(mutants_xǁAzureMonitorTracesAdapterǁ__init____mutmut)
    def __init__(self, workspace_id: str, logs_client: LogsClient | None = None) -> None:
        self._workspace_id = workspace_id
        self._logs_client = logs_client

    def xǁAzureMonitorTracesAdapterǁ__init____mutmut_orig(self, workspace_id: str, logs_client: LogsClient | None = None) -> None:
        self._workspace_id = workspace_id
        self._logs_client = logs_client

    def xǁAzureMonitorTracesAdapterǁ__init____mutmut_1(self, workspace_id: str, logs_client: LogsClient | None = None) -> None:
        self._workspace_id = None
        self._logs_client = logs_client

    def xǁAzureMonitorTracesAdapterǁ__init____mutmut_2(self, workspace_id: str, logs_client: LogsClient | None = None) -> None:
        self._workspace_id = workspace_id
        self._logs_client = None

    @_mutmut_mutated(mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut)
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

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_orig(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
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

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_1(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = None
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

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_2(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(None, request.time_window_minutes)
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

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_3(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), None)
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

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_4(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(request.time_window_minutes)
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

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_5(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), )
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

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_6(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(None), request.time_window_minutes)
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

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_7(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is not None:
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

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_8(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is None:
            return []
        by_trace: dict[str, list[TraceSpan]] = None
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

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_9(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is None:
            return []
        by_trace: dict[str, list[TraceSpan]] = {}
        for row in _rows_as_dicts(None):
            trace_id = str(row.get("OperationId", "unknown"))
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(row.get("Name", "unknown")),
                    duration_ms=_as_float(row.get("DurationMs")),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_10(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is None:
            return []
        by_trace: dict[str, list[TraceSpan]] = {}
        for row in _rows_as_dicts(table):
            trace_id = None
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(row.get("Name", "unknown")),
                    duration_ms=_as_float(row.get("DurationMs")),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_11(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is None:
            return []
        by_trace: dict[str, list[TraceSpan]] = {}
        for row in _rows_as_dicts(table):
            trace_id = str(None)
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(row.get("Name", "unknown")),
                    duration_ms=_as_float(row.get("DurationMs")),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_12(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is None:
            return []
        by_trace: dict[str, list[TraceSpan]] = {}
        for row in _rows_as_dicts(table):
            trace_id = str(row.get(None, "unknown"))
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(row.get("Name", "unknown")),
                    duration_ms=_as_float(row.get("DurationMs")),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_13(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is None:
            return []
        by_trace: dict[str, list[TraceSpan]] = {}
        for row in _rows_as_dicts(table):
            trace_id = str(row.get("OperationId", None))
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(row.get("Name", "unknown")),
                    duration_ms=_as_float(row.get("DurationMs")),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_14(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is None:
            return []
        by_trace: dict[str, list[TraceSpan]] = {}
        for row in _rows_as_dicts(table):
            trace_id = str(row.get("unknown"))
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(row.get("Name", "unknown")),
                    duration_ms=_as_float(row.get("DurationMs")),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_15(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is None:
            return []
        by_trace: dict[str, list[TraceSpan]] = {}
        for row in _rows_as_dicts(table):
            trace_id = str(row.get("OperationId", ))
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(row.get("Name", "unknown")),
                    duration_ms=_as_float(row.get("DurationMs")),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_16(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is None:
            return []
        by_trace: dict[str, list[TraceSpan]] = {}
        for row in _rows_as_dicts(table):
            trace_id = str(row.get("XXOperationIdXX", "unknown"))
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(row.get("Name", "unknown")),
                    duration_ms=_as_float(row.get("DurationMs")),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_17(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is None:
            return []
        by_trace: dict[str, list[TraceSpan]] = {}
        for row in _rows_as_dicts(table):
            trace_id = str(row.get("operationid", "unknown"))
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(row.get("Name", "unknown")),
                    duration_ms=_as_float(row.get("DurationMs")),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_18(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is None:
            return []
        by_trace: dict[str, list[TraceSpan]] = {}
        for row in _rows_as_dicts(table):
            trace_id = str(row.get("OPERATIONID", "unknown"))
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(row.get("Name", "unknown")),
                    duration_ms=_as_float(row.get("DurationMs")),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_19(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is None:
            return []
        by_trace: dict[str, list[TraceSpan]] = {}
        for row in _rows_as_dicts(table):
            trace_id = str(row.get("OperationId", "XXunknownXX"))
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(row.get("Name", "unknown")),
                    duration_ms=_as_float(row.get("DurationMs")),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_20(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is None:
            return []
        by_trace: dict[str, list[TraceSpan]] = {}
        for row in _rows_as_dicts(table):
            trace_id = str(row.get("OperationId", "UNKNOWN"))
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(row.get("Name", "unknown")),
                    duration_ms=_as_float(row.get("DurationMs")),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_21(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is None:
            return []
        by_trace: dict[str, list[TraceSpan]] = {}
        for row in _rows_as_dicts(table):
            trace_id = str(row.get("OperationId", "unknown"))
            by_trace.setdefault(trace_id, []).append(
                None
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_22(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is None:
            return []
        by_trace: dict[str, list[TraceSpan]] = {}
        for row in _rows_as_dicts(table):
            trace_id = str(row.get("OperationId", "unknown"))
            by_trace.setdefault(None, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(row.get("Name", "unknown")),
                    duration_ms=_as_float(row.get("DurationMs")),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_23(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is None:
            return []
        by_trace: dict[str, list[TraceSpan]] = {}
        for row in _rows_as_dicts(table):
            trace_id = str(row.get("OperationId", "unknown"))
            by_trace.setdefault(trace_id, None).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(row.get("Name", "unknown")),
                    duration_ms=_as_float(row.get("DurationMs")),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_24(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is None:
            return []
        by_trace: dict[str, list[TraceSpan]] = {}
        for row in _rows_as_dicts(table):
            trace_id = str(row.get("OperationId", "unknown"))
            by_trace.setdefault([]).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(row.get("Name", "unknown")),
                    duration_ms=_as_float(row.get("DurationMs")),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_25(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is None:
            return []
        by_trace: dict[str, list[TraceSpan]] = {}
        for row in _rows_as_dicts(table):
            trace_id = str(row.get("OperationId", "unknown"))
            by_trace.setdefault(trace_id, ).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(row.get("Name", "unknown")),
                    duration_ms=_as_float(row.get("DurationMs")),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_26(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is None:
            return []
        by_trace: dict[str, list[TraceSpan]] = {}
        for row in _rows_as_dicts(table):
            trace_id = str(row.get("OperationId", "unknown"))
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=None,
                    span_name=str(row.get("Name", "unknown")),
                    duration_ms=_as_float(row.get("DurationMs")),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_27(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is None:
            return []
        by_trace: dict[str, list[TraceSpan]] = {}
        for row in _rows_as_dicts(table):
            trace_id = str(row.get("OperationId", "unknown"))
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=None,
                    duration_ms=_as_float(row.get("DurationMs")),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_28(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
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
                    duration_ms=None,
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_29(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is None:
            return []
        by_trace: dict[str, list[TraceSpan]] = {}
        for row in _rows_as_dicts(table):
            trace_id = str(row.get("OperationId", "unknown"))
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    span_name=str(row.get("Name", "unknown")),
                    duration_ms=_as_float(row.get("DurationMs")),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_30(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is None:
            return []
        by_trace: dict[str, list[TraceSpan]] = {}
        for row in _rows_as_dicts(table):
            trace_id = str(row.get("OperationId", "unknown"))
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    duration_ms=_as_float(row.get("DurationMs")),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_31(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
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
                    )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_32(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is None:
            return []
        by_trace: dict[str, list[TraceSpan]] = {}
        for row in _rows_as_dicts(table):
            trace_id = str(row.get("OperationId", "unknown"))
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(None),
                    duration_ms=_as_float(row.get("DurationMs")),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_33(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is None:
            return []
        by_trace: dict[str, list[TraceSpan]] = {}
        for row in _rows_as_dicts(table):
            trace_id = str(row.get("OperationId", "unknown"))
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(row.get(None, "unknown")),
                    duration_ms=_as_float(row.get("DurationMs")),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_34(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is None:
            return []
        by_trace: dict[str, list[TraceSpan]] = {}
        for row in _rows_as_dicts(table):
            trace_id = str(row.get("OperationId", "unknown"))
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(row.get("Name", None)),
                    duration_ms=_as_float(row.get("DurationMs")),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_35(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is None:
            return []
        by_trace: dict[str, list[TraceSpan]] = {}
        for row in _rows_as_dicts(table):
            trace_id = str(row.get("OperationId", "unknown"))
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(row.get("unknown")),
                    duration_ms=_as_float(row.get("DurationMs")),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_36(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is None:
            return []
        by_trace: dict[str, list[TraceSpan]] = {}
        for row in _rows_as_dicts(table):
            trace_id = str(row.get("OperationId", "unknown"))
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(row.get("Name", )),
                    duration_ms=_as_float(row.get("DurationMs")),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_37(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is None:
            return []
        by_trace: dict[str, list[TraceSpan]] = {}
        for row in _rows_as_dicts(table):
            trace_id = str(row.get("OperationId", "unknown"))
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(row.get("XXNameXX", "unknown")),
                    duration_ms=_as_float(row.get("DurationMs")),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_38(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is None:
            return []
        by_trace: dict[str, list[TraceSpan]] = {}
        for row in _rows_as_dicts(table):
            trace_id = str(row.get("OperationId", "unknown"))
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(row.get("name", "unknown")),
                    duration_ms=_as_float(row.get("DurationMs")),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_39(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is None:
            return []
        by_trace: dict[str, list[TraceSpan]] = {}
        for row in _rows_as_dicts(table):
            trace_id = str(row.get("OperationId", "unknown"))
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(row.get("NAME", "unknown")),
                    duration_ms=_as_float(row.get("DurationMs")),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_40(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is None:
            return []
        by_trace: dict[str, list[TraceSpan]] = {}
        for row in _rows_as_dicts(table):
            trace_id = str(row.get("OperationId", "unknown"))
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(row.get("Name", "XXunknownXX")),
                    duration_ms=_as_float(row.get("DurationMs")),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_41(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        table = self._query(self._slow_kql(request), request.time_window_minutes)
        if table is None:
            return []
        by_trace: dict[str, list[TraceSpan]] = {}
        for row in _rows_as_dicts(table):
            trace_id = str(row.get("OperationId", "unknown"))
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(row.get("Name", "UNKNOWN")),
                    duration_ms=_as_float(row.get("DurationMs")),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_42(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
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
                    duration_ms=_as_float(None),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_43(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
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
                    duration_ms=_as_float(row.get(None)),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_44(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
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
                    duration_ms=_as_float(row.get("XXDurationMsXX")),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_45(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
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
                    duration_ms=_as_float(row.get("durationms")),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_46(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
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
                    duration_ms=_as_float(row.get("DURATIONMS")),
                )
            )
        return list(by_trace.values())

    def xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_47(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
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
        return list(None)

    @_mutmut_mutated(mutants_xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut)
    def fetch_total_traces(self, request: LatencyDiagnosticRequest) -> int:
        table = self._query(self._total_kql(request), request.time_window_minutes)
        if table is None:
            return 0
        rows = _rows_as_dicts(table)
        if not rows:
            return 0
        return int(_as_float(next(iter(rows[0].values()), 0)))

    def xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_orig(self, request: LatencyDiagnosticRequest) -> int:
        table = self._query(self._total_kql(request), request.time_window_minutes)
        if table is None:
            return 0
        rows = _rows_as_dicts(table)
        if not rows:
            return 0
        return int(_as_float(next(iter(rows[0].values()), 0)))

    def xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_1(self, request: LatencyDiagnosticRequest) -> int:
        table = None
        if table is None:
            return 0
        rows = _rows_as_dicts(table)
        if not rows:
            return 0
        return int(_as_float(next(iter(rows[0].values()), 0)))

    def xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_2(self, request: LatencyDiagnosticRequest) -> int:
        table = self._query(None, request.time_window_minutes)
        if table is None:
            return 0
        rows = _rows_as_dicts(table)
        if not rows:
            return 0
        return int(_as_float(next(iter(rows[0].values()), 0)))

    def xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_3(self, request: LatencyDiagnosticRequest) -> int:
        table = self._query(self._total_kql(request), None)
        if table is None:
            return 0
        rows = _rows_as_dicts(table)
        if not rows:
            return 0
        return int(_as_float(next(iter(rows[0].values()), 0)))

    def xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_4(self, request: LatencyDiagnosticRequest) -> int:
        table = self._query(request.time_window_minutes)
        if table is None:
            return 0
        rows = _rows_as_dicts(table)
        if not rows:
            return 0
        return int(_as_float(next(iter(rows[0].values()), 0)))

    def xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_5(self, request: LatencyDiagnosticRequest) -> int:
        table = self._query(self._total_kql(request), )
        if table is None:
            return 0
        rows = _rows_as_dicts(table)
        if not rows:
            return 0
        return int(_as_float(next(iter(rows[0].values()), 0)))

    def xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_6(self, request: LatencyDiagnosticRequest) -> int:
        table = self._query(self._total_kql(None), request.time_window_minutes)
        if table is None:
            return 0
        rows = _rows_as_dicts(table)
        if not rows:
            return 0
        return int(_as_float(next(iter(rows[0].values()), 0)))

    def xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_7(self, request: LatencyDiagnosticRequest) -> int:
        table = self._query(self._total_kql(request), request.time_window_minutes)
        if table is not None:
            return 0
        rows = _rows_as_dicts(table)
        if not rows:
            return 0
        return int(_as_float(next(iter(rows[0].values()), 0)))

    def xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_8(self, request: LatencyDiagnosticRequest) -> int:
        table = self._query(self._total_kql(request), request.time_window_minutes)
        if table is None:
            return 1
        rows = _rows_as_dicts(table)
        if not rows:
            return 0
        return int(_as_float(next(iter(rows[0].values()), 0)))

    def xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_9(self, request: LatencyDiagnosticRequest) -> int:
        table = self._query(self._total_kql(request), request.time_window_minutes)
        if table is None:
            return 0
        rows = None
        if not rows:
            return 0
        return int(_as_float(next(iter(rows[0].values()), 0)))

    def xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_10(self, request: LatencyDiagnosticRequest) -> int:
        table = self._query(self._total_kql(request), request.time_window_minutes)
        if table is None:
            return 0
        rows = _rows_as_dicts(None)
        if not rows:
            return 0
        return int(_as_float(next(iter(rows[0].values()), 0)))

    def xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_11(self, request: LatencyDiagnosticRequest) -> int:
        table = self._query(self._total_kql(request), request.time_window_minutes)
        if table is None:
            return 0
        rows = _rows_as_dicts(table)
        if rows:
            return 0
        return int(_as_float(next(iter(rows[0].values()), 0)))

    def xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_12(self, request: LatencyDiagnosticRequest) -> int:
        table = self._query(self._total_kql(request), request.time_window_minutes)
        if table is None:
            return 0
        rows = _rows_as_dicts(table)
        if not rows:
            return 1
        return int(_as_float(next(iter(rows[0].values()), 0)))

    def xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_13(self, request: LatencyDiagnosticRequest) -> int:
        table = self._query(self._total_kql(request), request.time_window_minutes)
        if table is None:
            return 0
        rows = _rows_as_dicts(table)
        if not rows:
            return 0
        return int(None)

    def xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_14(self, request: LatencyDiagnosticRequest) -> int:
        table = self._query(self._total_kql(request), request.time_window_minutes)
        if table is None:
            return 0
        rows = _rows_as_dicts(table)
        if not rows:
            return 0
        return int(_as_float(None))

    def xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_15(self, request: LatencyDiagnosticRequest) -> int:
        table = self._query(self._total_kql(request), request.time_window_minutes)
        if table is None:
            return 0
        rows = _rows_as_dicts(table)
        if not rows:
            return 0
        return int(_as_float(next(None, 0)))

    def xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_16(self, request: LatencyDiagnosticRequest) -> int:
        table = self._query(self._total_kql(request), request.time_window_minutes)
        if table is None:
            return 0
        rows = _rows_as_dicts(table)
        if not rows:
            return 0
        return int(_as_float(next(iter(rows[0].values()), None)))

    def xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_17(self, request: LatencyDiagnosticRequest) -> int:
        table = self._query(self._total_kql(request), request.time_window_minutes)
        if table is None:
            return 0
        rows = _rows_as_dicts(table)
        if not rows:
            return 0
        return int(_as_float(next(0)))

    def xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_18(self, request: LatencyDiagnosticRequest) -> int:
        table = self._query(self._total_kql(request), request.time_window_minutes)
        if table is None:
            return 0
        rows = _rows_as_dicts(table)
        if not rows:
            return 0
        return int(_as_float(next(iter(rows[0].values()), )))

    def xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_19(self, request: LatencyDiagnosticRequest) -> int:
        table = self._query(self._total_kql(request), request.time_window_minutes)
        if table is None:
            return 0
        rows = _rows_as_dicts(table)
        if not rows:
            return 0
        return int(_as_float(next(iter(None), 0)))

    def xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_20(self, request: LatencyDiagnosticRequest) -> int:
        table = self._query(self._total_kql(request), request.time_window_minutes)
        if table is None:
            return 0
        rows = _rows_as_dicts(table)
        if not rows:
            return 0
        return int(_as_float(next(iter(rows[1].values()), 0)))

    def xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_21(self, request: LatencyDiagnosticRequest) -> int:
        table = self._query(self._total_kql(request), request.time_window_minutes)
        if table is None:
            return 0
        rows = _rows_as_dicts(table)
        if not rows:
            return 0
        return int(_as_float(next(iter(rows[0].values()), 1)))

    @_mutmut_mutated(mutants_xǁAzureMonitorTracesAdapterǁ_slow_kql__mutmut)
    def _slow_kql(self, request: LatencyDiagnosticRequest) -> str:
        threshold = int(request.threshold_ms)
        return (
            f"{_DEPENDENCIES_TABLE} "
            f'| where Target contains "{request.service_name}" and DurationMs > {threshold} '
            f"| project OperationId, Name, DurationMs "
            f"| take {_ROW_LIMIT}"
        )

    def xǁAzureMonitorTracesAdapterǁ_slow_kql__mutmut_orig(self, request: LatencyDiagnosticRequest) -> str:
        threshold = int(request.threshold_ms)
        return (
            f"{_DEPENDENCIES_TABLE} "
            f'| where Target contains "{request.service_name}" and DurationMs > {threshold} '
            f"| project OperationId, Name, DurationMs "
            f"| take {_ROW_LIMIT}"
        )

    def xǁAzureMonitorTracesAdapterǁ_slow_kql__mutmut_1(self, request: LatencyDiagnosticRequest) -> str:
        threshold = None
        return (
            f"{_DEPENDENCIES_TABLE} "
            f'| where Target contains "{request.service_name}" and DurationMs > {threshold} '
            f"| project OperationId, Name, DurationMs "
            f"| take {_ROW_LIMIT}"
        )

    def xǁAzureMonitorTracesAdapterǁ_slow_kql__mutmut_2(self, request: LatencyDiagnosticRequest) -> str:
        threshold = int(None)
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

    @_mutmut_mutated(mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut)
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

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_orig(self, kql: str, window_minutes: int) -> _LogsTable | None:
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

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_1(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = None
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

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_2(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                None, kql, timespan=timedelta(minutes=window_minutes)
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

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_3(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, None, timespan=timedelta(minutes=window_minutes)
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

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_4(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=None
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

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_5(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                kql, timespan=timedelta(minutes=window_minutes)
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

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_6(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, timespan=timedelta(minutes=window_minutes)
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

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_7(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, )
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

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_8(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=None)
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

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_9(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise TracesUnavailableError(
                None,
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

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_10(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise TracesUnavailableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context=None,
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

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_11(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise TracesUnavailableError(
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

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_12(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise TracesUnavailableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
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

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_13(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise TracesUnavailableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"XXworkspaceXX": self._workspace_id},
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

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_14(self, kql: str, window_minutes: int) -> _LogsTable | None:
        from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
        from azure.monitor.query import LogsQueryStatus

        try:
            result = self._client_or_create().query_workspace(
                self._workspace_id, kql, timespan=timedelta(minutes=window_minutes)
            )
        except ClientAuthenticationError as exc:
            raise TracesUnavailableError(
                f"Azure credentials not found. {_CREDENTIALS_HINT}",
                context={"WORKSPACE": self._workspace_id},
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

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_15(self, kql: str, window_minutes: int) -> _LogsTable | None:
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
                None,
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise TracesUnavailableError(
                "Azure Monitor query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_16(self, kql: str, window_minutes: int) -> _LogsTable | None:
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
                context=None,
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise TracesUnavailableError(
                "Azure Monitor query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_17(self, kql: str, window_minutes: int) -> _LogsTable | None:
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
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise TracesUnavailableError(
                "Azure Monitor query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_18(self, kql: str, window_minutes: int) -> _LogsTable | None:
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
                ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise TracesUnavailableError(
                "Azure Monitor query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_19(self, kql: str, window_minutes: int) -> _LogsTable | None:
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
                "XXUnable to query Azure Monitor.XX",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise TracesUnavailableError(
                "Azure Monitor query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_20(self, kql: str, window_minutes: int) -> _LogsTable | None:
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
                "unable to query azure monitor.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise TracesUnavailableError(
                "Azure Monitor query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_21(self, kql: str, window_minutes: int) -> _LogsTable | None:
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
                "UNABLE TO QUERY AZURE MONITOR.",
                context={"workspace": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise TracesUnavailableError(
                "Azure Monitor query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_22(self, kql: str, window_minutes: int) -> _LogsTable | None:
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
                context={"XXworkspaceXX": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise TracesUnavailableError(
                "Azure Monitor query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_23(self, kql: str, window_minutes: int) -> _LogsTable | None:
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
                context={"WORKSPACE": self._workspace_id, "error": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise TracesUnavailableError(
                "Azure Monitor query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_24(self, kql: str, window_minutes: int) -> _LogsTable | None:
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
                context={"workspace": self._workspace_id, "XXerrorXX": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise TracesUnavailableError(
                "Azure Monitor query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_25(self, kql: str, window_minutes: int) -> _LogsTable | None:
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
                context={"workspace": self._workspace_id, "ERROR": str(exc)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise TracesUnavailableError(
                "Azure Monitor query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_26(self, kql: str, window_minutes: int) -> _LogsTable | None:
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
                context={"workspace": self._workspace_id, "error": str(None)},
            ) from exc

        if getattr(result, "status", None) == LogsQueryStatus.FAILURE:
            raise TracesUnavailableError(
                "Azure Monitor query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_27(self, kql: str, window_minutes: int) -> _LogsTable | None:
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

        if getattr(None, "status", None) == LogsQueryStatus.FAILURE:
            raise TracesUnavailableError(
                "Azure Monitor query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_28(self, kql: str, window_minutes: int) -> _LogsTable | None:
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

        if getattr(result, None, None) == LogsQueryStatus.FAILURE:
            raise TracesUnavailableError(
                "Azure Monitor query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_29(self, kql: str, window_minutes: int) -> _LogsTable | None:
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

        if getattr("status", None) == LogsQueryStatus.FAILURE:
            raise TracesUnavailableError(
                "Azure Monitor query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_30(self, kql: str, window_minutes: int) -> _LogsTable | None:
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

        if getattr(result, None) == LogsQueryStatus.FAILURE:
            raise TracesUnavailableError(
                "Azure Monitor query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_31(self, kql: str, window_minutes: int) -> _LogsTable | None:
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

        if getattr(result, "status", ) == LogsQueryStatus.FAILURE:
            raise TracesUnavailableError(
                "Azure Monitor query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_32(self, kql: str, window_minutes: int) -> _LogsTable | None:
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

        if getattr(result, "XXstatusXX", None) == LogsQueryStatus.FAILURE:
            raise TracesUnavailableError(
                "Azure Monitor query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_33(self, kql: str, window_minutes: int) -> _LogsTable | None:
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

        if getattr(result, "STATUS", None) == LogsQueryStatus.FAILURE:
            raise TracesUnavailableError(
                "Azure Monitor query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_34(self, kql: str, window_minutes: int) -> _LogsTable | None:
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

        if getattr(result, "status", None) != LogsQueryStatus.FAILURE:
            raise TracesUnavailableError(
                "Azure Monitor query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_35(self, kql: str, window_minutes: int) -> _LogsTable | None:
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
                None,
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_36(self, kql: str, window_minutes: int) -> _LogsTable | None:
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
                context=None,
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_37(self, kql: str, window_minutes: int) -> _LogsTable | None:
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
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_38(self, kql: str, window_minutes: int) -> _LogsTable | None:
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
                )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_39(self, kql: str, window_minutes: int) -> _LogsTable | None:
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
                "XXAzure Monitor query failed.XX",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_40(self, kql: str, window_minutes: int) -> _LogsTable | None:
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
                "azure monitor query failed.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_41(self, kql: str, window_minutes: int) -> _LogsTable | None:
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
                "AZURE MONITOR QUERY FAILED.",
                context={"workspace": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_42(self, kql: str, window_minutes: int) -> _LogsTable | None:
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
                context={"XXworkspaceXX": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_43(self, kql: str, window_minutes: int) -> _LogsTable | None:
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
                context={"WORKSPACE": self._workspace_id},
            )
        tables = result.tables
        return tables[0] if tables else None

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_44(self, kql: str, window_minutes: int) -> _LogsTable | None:
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
        tables = None
        return tables[0] if tables else None

    def xǁAzureMonitorTracesAdapterǁ_query__mutmut_45(self, kql: str, window_minutes: int) -> _LogsTable | None:
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
        return tables[1] if tables else None

    @_mutmut_mutated(mutants_xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut)
    def _client_or_create(self) -> LogsClient:
        client = self._logs_client
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.monitor.query import LogsQueryClient

            client = cast(LogsClient, LogsQueryClient(DefaultAzureCredential()))
            self._logs_client = client
        return client

    def xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut_orig(self) -> LogsClient:
        client = self._logs_client
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.monitor.query import LogsQueryClient

            client = cast(LogsClient, LogsQueryClient(DefaultAzureCredential()))
            self._logs_client = client
        return client

    def xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut_1(self) -> LogsClient:
        client = None
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.monitor.query import LogsQueryClient

            client = cast(LogsClient, LogsQueryClient(DefaultAzureCredential()))
            self._logs_client = client
        return client

    def xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut_2(self) -> LogsClient:
        client = self._logs_client
        if client is not None:
            from azure.identity import DefaultAzureCredential
            from azure.monitor.query import LogsQueryClient

            client = cast(LogsClient, LogsQueryClient(DefaultAzureCredential()))
            self._logs_client = client
        return client

    def xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut_3(self) -> LogsClient:
        client = self._logs_client
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.monitor.query import LogsQueryClient

            client = None
            self._logs_client = client
        return client

    def xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut_4(self) -> LogsClient:
        client = self._logs_client
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.monitor.query import LogsQueryClient

            client = cast(None, LogsQueryClient(DefaultAzureCredential()))
            self._logs_client = client
        return client

    def xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut_5(self) -> LogsClient:
        client = self._logs_client
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.monitor.query import LogsQueryClient

            client = cast(LogsClient, None)
            self._logs_client = client
        return client

    def xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut_6(self) -> LogsClient:
        client = self._logs_client
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.monitor.query import LogsQueryClient

            client = cast(LogsQueryClient(DefaultAzureCredential()))
            self._logs_client = client
        return client

    def xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut_7(self) -> LogsClient:
        client = self._logs_client
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.monitor.query import LogsQueryClient

            client = cast(LogsClient, )
            self._logs_client = client
        return client

    def xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut_8(self) -> LogsClient:
        client = self._logs_client
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.monitor.query import LogsQueryClient

            client = cast(LogsClient, LogsQueryClient(None))
            self._logs_client = client
        return client

    def xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut_9(self) -> LogsClient:
        client = self._logs_client
        if client is None:
            from azure.identity import DefaultAzureCredential
            from azure.monitor.query import LogsQueryClient

            client = cast(LogsClient, LogsQueryClient(DefaultAzureCredential()))
            self._logs_client = None
        return client

mutants_xǁAzureMonitorTracesAdapterǁ__init____mutmut['_mutmut_orig'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ__init____mutmut['xǁAzureMonitorTracesAdapterǁ__init____mutmut_1'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ__init____mutmut['xǁAzureMonitorTracesAdapterǁ__init____mutmut_2'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['_mutmut_orig'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_1'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_2'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_3'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_4'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_5'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_6'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_7'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_8'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_9'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_10'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_11'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_12'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_13'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_14'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_15'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_16'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_17'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_18'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_19'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_20'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_21'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_22'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_23'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_24'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_25'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_26'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_27'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_27 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_28'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_28 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_29'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_29 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_30'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_30 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_31'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_31 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_32'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_32 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_33'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_33 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_34'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_34 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_35'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_35 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_36'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_36 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_37'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_37 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_38'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_38 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_39'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_39 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_40'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_40 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_41'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_41 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_42'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_42 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_43'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_43 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_44'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_44 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_45'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_45 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_46'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_46 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut['xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_47'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_slow_spans__mutmut_47 # type: ignore # mutmut generated

mutants_xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut['_mutmut_orig'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut['xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_1'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut['xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_2'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut['xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_3'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut['xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_4'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut['xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_5'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut['xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_6'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut['xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_7'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut['xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_8'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut['xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_9'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut['xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_10'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut['xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_11'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut['xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_12'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut['xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_13'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut['xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_14'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut['xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_15'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut['xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_16'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut['xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_17'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut['xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_18'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut['xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_19'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut['xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_20'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut['xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_21'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁfetch_total_traces__mutmut_21 # type: ignore # mutmut generated

mutants_xǁAzureMonitorTracesAdapterǁ_slow_kql__mutmut['_mutmut_orig'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_slow_kql__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_slow_kql__mutmut['xǁAzureMonitorTracesAdapterǁ_slow_kql__mutmut_1'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_slow_kql__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_slow_kql__mutmut['xǁAzureMonitorTracesAdapterǁ_slow_kql__mutmut_2'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_slow_kql__mutmut_2 # type: ignore # mutmut generated

mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['_mutmut_orig'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_1'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_2'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_3'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_4'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_5'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_6'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_7'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_8'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_9'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_10'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_11'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_12'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_13'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_14'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_15'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_16'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_17'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_18'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_19'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_20'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_21'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_22'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_23'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_24'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_25'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_26'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_27'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_27 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_28'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_28 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_29'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_29 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_30'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_30 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_31'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_31 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_32'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_32 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_33'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_33 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_34'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_34 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_35'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_35 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_36'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_36 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_37'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_37 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_38'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_38 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_39'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_39 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_40'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_40 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_41'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_41 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_42'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_42 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_43'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_43 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_44'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_44 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_query__mutmut['xǁAzureMonitorTracesAdapterǁ_query__mutmut_45'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_query__mutmut_45 # type: ignore # mutmut generated

mutants_xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut['_mutmut_orig'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut['xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut_1'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut['xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut_2'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut['xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut_3'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut['xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut_4'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut['xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut_5'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut['xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut_6'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut['xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut_7'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut['xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut_8'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut['xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut_9'] = AzureMonitorTracesAdapter.xǁAzureMonitorTracesAdapterǁ_client_or_create__mutmut_9 # type: ignore # mutmut generated
mutants_x__rows_as_dicts__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__rows_as_dicts__mutmut)
def _rows_as_dicts(table: _LogsTable) -> list[dict[str, object]]:
    columns = list(table.columns)
    dicts: list[dict[str, object]] = []
    for row in table.rows:
        values = [row[index] for index in range(len(columns))]
        dicts.append(dict(zip(columns, values, strict=False)))
    return dicts


def x__rows_as_dicts__mutmut_orig(table: _LogsTable) -> list[dict[str, object]]:
    columns = list(table.columns)
    dicts: list[dict[str, object]] = []
    for row in table.rows:
        values = [row[index] for index in range(len(columns))]
        dicts.append(dict(zip(columns, values, strict=False)))
    return dicts


def x__rows_as_dicts__mutmut_1(table: _LogsTable) -> list[dict[str, object]]:
    columns = None
    dicts: list[dict[str, object]] = []
    for row in table.rows:
        values = [row[index] for index in range(len(columns))]
        dicts.append(dict(zip(columns, values, strict=False)))
    return dicts


def x__rows_as_dicts__mutmut_2(table: _LogsTable) -> list[dict[str, object]]:
    columns = list(None)
    dicts: list[dict[str, object]] = []
    for row in table.rows:
        values = [row[index] for index in range(len(columns))]
        dicts.append(dict(zip(columns, values, strict=False)))
    return dicts


def x__rows_as_dicts__mutmut_3(table: _LogsTable) -> list[dict[str, object]]:
    columns = list(table.columns)
    dicts: list[dict[str, object]] = None
    for row in table.rows:
        values = [row[index] for index in range(len(columns))]
        dicts.append(dict(zip(columns, values, strict=False)))
    return dicts


def x__rows_as_dicts__mutmut_4(table: _LogsTable) -> list[dict[str, object]]:
    columns = list(table.columns)
    dicts: list[dict[str, object]] = []
    for row in table.rows:
        values = None
        dicts.append(dict(zip(columns, values, strict=False)))
    return dicts


def x__rows_as_dicts__mutmut_5(table: _LogsTable) -> list[dict[str, object]]:
    columns = list(table.columns)
    dicts: list[dict[str, object]] = []
    for row in table.rows:
        values = [row[index] for index in range(None)]
        dicts.append(dict(zip(columns, values, strict=False)))
    return dicts


def x__rows_as_dicts__mutmut_6(table: _LogsTable) -> list[dict[str, object]]:
    columns = list(table.columns)
    dicts: list[dict[str, object]] = []
    for row in table.rows:
        values = [row[index] for index in range(len(columns))]
        dicts.append(None)
    return dicts


def x__rows_as_dicts__mutmut_7(table: _LogsTable) -> list[dict[str, object]]:
    columns = list(table.columns)
    dicts: list[dict[str, object]] = []
    for row in table.rows:
        values = [row[index] for index in range(len(columns))]
        dicts.append(dict(None))
    return dicts


def x__rows_as_dicts__mutmut_8(table: _LogsTable) -> list[dict[str, object]]:
    columns = list(table.columns)
    dicts: list[dict[str, object]] = []
    for row in table.rows:
        values = [row[index] for index in range(len(columns))]
        dicts.append(dict(zip(None, values, strict=False)))
    return dicts


def x__rows_as_dicts__mutmut_9(table: _LogsTable) -> list[dict[str, object]]:
    columns = list(table.columns)
    dicts: list[dict[str, object]] = []
    for row in table.rows:
        values = [row[index] for index in range(len(columns))]
        dicts.append(dict(zip(columns, None, strict=False)))
    return dicts


def x__rows_as_dicts__mutmut_10(table: _LogsTable) -> list[dict[str, object]]:
    columns = list(table.columns)
    dicts: list[dict[str, object]] = []
    for row in table.rows:
        values = [row[index] for index in range(len(columns))]
        dicts.append(dict(zip(columns, values, strict=None)))
    return dicts


def x__rows_as_dicts__mutmut_11(table: _LogsTable) -> list[dict[str, object]]:
    columns = list(table.columns)
    dicts: list[dict[str, object]] = []
    for row in table.rows:
        values = [row[index] for index in range(len(columns))]
        dicts.append(dict(zip(values, strict=False)))
    return dicts


def x__rows_as_dicts__mutmut_12(table: _LogsTable) -> list[dict[str, object]]:
    columns = list(table.columns)
    dicts: list[dict[str, object]] = []
    for row in table.rows:
        values = [row[index] for index in range(len(columns))]
        dicts.append(dict(zip(columns, strict=False)))
    return dicts


def x__rows_as_dicts__mutmut_13(table: _LogsTable) -> list[dict[str, object]]:
    columns = list(table.columns)
    dicts: list[dict[str, object]] = []
    for row in table.rows:
        values = [row[index] for index in range(len(columns))]
        dicts.append(dict(zip(columns, values, )))
    return dicts


def x__rows_as_dicts__mutmut_14(table: _LogsTable) -> list[dict[str, object]]:
    columns = list(table.columns)
    dicts: list[dict[str, object]] = []
    for row in table.rows:
        values = [row[index] for index in range(len(columns))]
        dicts.append(dict(zip(columns, values, strict=True)))
    return dicts

mutants_x__rows_as_dicts__mutmut['_mutmut_orig'] = x__rows_as_dicts__mutmut_orig # type: ignore # mutmut generated
mutants_x__rows_as_dicts__mutmut['x__rows_as_dicts__mutmut_1'] = x__rows_as_dicts__mutmut_1 # type: ignore # mutmut generated
mutants_x__rows_as_dicts__mutmut['x__rows_as_dicts__mutmut_2'] = x__rows_as_dicts__mutmut_2 # type: ignore # mutmut generated
mutants_x__rows_as_dicts__mutmut['x__rows_as_dicts__mutmut_3'] = x__rows_as_dicts__mutmut_3 # type: ignore # mutmut generated
mutants_x__rows_as_dicts__mutmut['x__rows_as_dicts__mutmut_4'] = x__rows_as_dicts__mutmut_4 # type: ignore # mutmut generated
mutants_x__rows_as_dicts__mutmut['x__rows_as_dicts__mutmut_5'] = x__rows_as_dicts__mutmut_5 # type: ignore # mutmut generated
mutants_x__rows_as_dicts__mutmut['x__rows_as_dicts__mutmut_6'] = x__rows_as_dicts__mutmut_6 # type: ignore # mutmut generated
mutants_x__rows_as_dicts__mutmut['x__rows_as_dicts__mutmut_7'] = x__rows_as_dicts__mutmut_7 # type: ignore # mutmut generated
mutants_x__rows_as_dicts__mutmut['x__rows_as_dicts__mutmut_8'] = x__rows_as_dicts__mutmut_8 # type: ignore # mutmut generated
mutants_x__rows_as_dicts__mutmut['x__rows_as_dicts__mutmut_9'] = x__rows_as_dicts__mutmut_9 # type: ignore # mutmut generated
mutants_x__rows_as_dicts__mutmut['x__rows_as_dicts__mutmut_10'] = x__rows_as_dicts__mutmut_10 # type: ignore # mutmut generated
mutants_x__rows_as_dicts__mutmut['x__rows_as_dicts__mutmut_11'] = x__rows_as_dicts__mutmut_11 # type: ignore # mutmut generated
mutants_x__rows_as_dicts__mutmut['x__rows_as_dicts__mutmut_12'] = x__rows_as_dicts__mutmut_12 # type: ignore # mutmut generated
mutants_x__rows_as_dicts__mutmut['x__rows_as_dicts__mutmut_13'] = x__rows_as_dicts__mutmut_13 # type: ignore # mutmut generated
mutants_x__rows_as_dicts__mutmut['x__rows_as_dicts__mutmut_14'] = x__rows_as_dicts__mutmut_14 # type: ignore # mutmut generated
mutants_x__as_float__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__as_float__mutmut)
def _as_float(value: object) -> float:
    if isinstance(value, int | float):
        return float(value)
    try:
        return float(str(value))
    except (TypeError, ValueError):
        return 0.0


def x__as_float__mutmut_orig(value: object) -> float:
    if isinstance(value, int | float):
        return float(value)
    try:
        return float(str(value))
    except (TypeError, ValueError):
        return 0.0


def x__as_float__mutmut_1(value: object) -> float:
    if isinstance(value, int | float):
        return float(None)
    try:
        return float(str(value))
    except (TypeError, ValueError):
        return 0.0


def x__as_float__mutmut_2(value: object) -> float:
    if isinstance(value, int | float):
        return float(value)
    try:
        return float(None)
    except (TypeError, ValueError):
        return 0.0


def x__as_float__mutmut_3(value: object) -> float:
    if isinstance(value, int | float):
        return float(value)
    try:
        return float(str(None))
    except (TypeError, ValueError):
        return 0.0


def x__as_float__mutmut_4(value: object) -> float:
    if isinstance(value, int | float):
        return float(value)
    try:
        return float(str(value))
    except (TypeError, ValueError):
        return 1.0

mutants_x__as_float__mutmut['_mutmut_orig'] = x__as_float__mutmut_orig # type: ignore # mutmut generated
mutants_x__as_float__mutmut['x__as_float__mutmut_1'] = x__as_float__mutmut_1 # type: ignore # mutmut generated
mutants_x__as_float__mutmut['x__as_float__mutmut_2'] = x__as_float__mutmut_2 # type: ignore # mutmut generated
mutants_x__as_float__mutmut['x__as_float__mutmut_3'] = x__as_float__mutmut_3 # type: ignore # mutmut generated
mutants_x__as_float__mutmut['x__as_float__mutmut_4'] = x__as_float__mutmut_4 # type: ignore # mutmut generated
