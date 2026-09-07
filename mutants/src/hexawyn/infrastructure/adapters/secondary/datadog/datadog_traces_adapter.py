from __future__ import annotations

from datetime import UTC, datetime, timedelta
from typing import Protocol, cast

from hexawyn.application.ports.driven.trace_query_port import (
    LatencyDiagnosticRequest,
    TraceQueryPort,
    TraceSpan,
)
from hexawyn.domain.errors import (
    AdapterTimeoutError,
    InsufficientPermissionsError,
    TracesUnavailableError,
)

_RATE_LIMIT_STATUS = 429
_UNAUTHORIZED_STATUSES = (401, 403)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class _SpanAttributes(Protocol):
    trace_id: str
    operation_name: str
    duration: float | str


class _Span(Protocol):
    id: str
    attributes: _SpanAttributes


class _SpansResponse(Protocol):
    data: list[_Span] | None


class SpansApi(Protocol):
    """Minimal contract for the Datadog v2 SpansApi used here."""

    def list_spans(self, *, body: object) -> _SpansResponse: ...
mutants_xǁDatadogTracesAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDatadogTracesAdapterǁfetch_total_traces__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDatadogTracesAdapterǁ_slow_filter__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDatadogTracesAdapterǁ_list_spans__mutmut: MutantDict = {}  # type: ignore
mutants_xǁDatadogTracesAdapterǁ_api__mutmut: MutantDict = {}  # type: ignore


class DatadogTracesAdapter(TraceQueryPort):
    """TraceQueryPort backed by Datadog APM (Spans API).

    Reads slow spans and groups them by trace, natively — no Tempo/Jaeger.
    """

    @_mutmut_mutated(mutants_xǁDatadogTracesAdapterǁ__init____mutmut)
    def __init__(
        self,
        spans_api: SpansApi | None = None,
        key: str = "",
        app_key: str = "",
        site: str = "datadoghq.com",
    ) -> None:
        self._spans_api = spans_api
        self._key = key
        self._app_key = app_key
        self._site = site

    def xǁDatadogTracesAdapterǁ__init____mutmut_orig(
        self,
        spans_api: SpansApi | None = None,
        key: str = "",
        app_key: str = "",
        site: str = "datadoghq.com",
    ) -> None:
        self._spans_api = spans_api
        self._key = key
        self._app_key = app_key
        self._site = site

    def xǁDatadogTracesAdapterǁ__init____mutmut_1(
        self,
        spans_api: SpansApi | None = None,
        key: str = "XXXX",
        app_key: str = "",
        site: str = "datadoghq.com",
    ) -> None:
        self._spans_api = spans_api
        self._key = key
        self._app_key = app_key
        self._site = site

    def xǁDatadogTracesAdapterǁ__init____mutmut_2(
        self,
        spans_api: SpansApi | None = None,
        key: str = "",
        app_key: str = "XXXX",
        site: str = "datadoghq.com",
    ) -> None:
        self._spans_api = spans_api
        self._key = key
        self._app_key = app_key
        self._site = site

    def xǁDatadogTracesAdapterǁ__init____mutmut_3(
        self,
        spans_api: SpansApi | None = None,
        key: str = "",
        app_key: str = "",
        site: str = "XXdatadoghq.comXX",
    ) -> None:
        self._spans_api = spans_api
        self._key = key
        self._app_key = app_key
        self._site = site

    def xǁDatadogTracesAdapterǁ__init____mutmut_4(
        self,
        spans_api: SpansApi | None = None,
        key: str = "",
        app_key: str = "",
        site: str = "DATADOGHQ.COM",
    ) -> None:
        self._spans_api = spans_api
        self._key = key
        self._app_key = app_key
        self._site = site

    def xǁDatadogTracesAdapterǁ__init____mutmut_5(
        self,
        spans_api: SpansApi | None = None,
        key: str = "",
        app_key: str = "",
        site: str = "datadoghq.com",
    ) -> None:
        self._spans_api = None
        self._key = key
        self._app_key = app_key
        self._site = site

    def xǁDatadogTracesAdapterǁ__init____mutmut_6(
        self,
        spans_api: SpansApi | None = None,
        key: str = "",
        app_key: str = "",
        site: str = "datadoghq.com",
    ) -> None:
        self._spans_api = spans_api
        self._key = None
        self._app_key = app_key
        self._site = site

    def xǁDatadogTracesAdapterǁ__init____mutmut_7(
        self,
        spans_api: SpansApi | None = None,
        key: str = "",
        app_key: str = "",
        site: str = "datadoghq.com",
    ) -> None:
        self._spans_api = spans_api
        self._key = key
        self._app_key = None
        self._site = site

    def xǁDatadogTracesAdapterǁ__init____mutmut_8(
        self,
        spans_api: SpansApi | None = None,
        key: str = "",
        app_key: str = "",
        site: str = "datadoghq.com",
    ) -> None:
        self._spans_api = spans_api
        self._key = key
        self._app_key = app_key
        self._site = None

    @_mutmut_mutated(mutants_xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut)
    def fetch_slow_spans(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        data = self._list_spans(self._slow_filter(request), request.time_window_minutes)
        by_trace: dict[str, list[TraceSpan]] = {}
        for span in data:
            attrs = span.attributes
            trace_id = str(attrs.trace_id)
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(attrs.operation_name),
                    duration_ms=_as_float(attrs.duration),
                )
            )
        return list(by_trace.values())

    def xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_orig(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        data = self._list_spans(self._slow_filter(request), request.time_window_minutes)
        by_trace: dict[str, list[TraceSpan]] = {}
        for span in data:
            attrs = span.attributes
            trace_id = str(attrs.trace_id)
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(attrs.operation_name),
                    duration_ms=_as_float(attrs.duration),
                )
            )
        return list(by_trace.values())

    def xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_1(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        data = None
        by_trace: dict[str, list[TraceSpan]] = {}
        for span in data:
            attrs = span.attributes
            trace_id = str(attrs.trace_id)
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(attrs.operation_name),
                    duration_ms=_as_float(attrs.duration),
                )
            )
        return list(by_trace.values())

    def xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_2(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        data = self._list_spans(None, request.time_window_minutes)
        by_trace: dict[str, list[TraceSpan]] = {}
        for span in data:
            attrs = span.attributes
            trace_id = str(attrs.trace_id)
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(attrs.operation_name),
                    duration_ms=_as_float(attrs.duration),
                )
            )
        return list(by_trace.values())

    def xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_3(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        data = self._list_spans(self._slow_filter(request), None)
        by_trace: dict[str, list[TraceSpan]] = {}
        for span in data:
            attrs = span.attributes
            trace_id = str(attrs.trace_id)
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(attrs.operation_name),
                    duration_ms=_as_float(attrs.duration),
                )
            )
        return list(by_trace.values())

    def xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_4(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        data = self._list_spans(request.time_window_minutes)
        by_trace: dict[str, list[TraceSpan]] = {}
        for span in data:
            attrs = span.attributes
            trace_id = str(attrs.trace_id)
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(attrs.operation_name),
                    duration_ms=_as_float(attrs.duration),
                )
            )
        return list(by_trace.values())

    def xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_5(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        data = self._list_spans(self._slow_filter(request), )
        by_trace: dict[str, list[TraceSpan]] = {}
        for span in data:
            attrs = span.attributes
            trace_id = str(attrs.trace_id)
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(attrs.operation_name),
                    duration_ms=_as_float(attrs.duration),
                )
            )
        return list(by_trace.values())

    def xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_6(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        data = self._list_spans(self._slow_filter(None), request.time_window_minutes)
        by_trace: dict[str, list[TraceSpan]] = {}
        for span in data:
            attrs = span.attributes
            trace_id = str(attrs.trace_id)
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(attrs.operation_name),
                    duration_ms=_as_float(attrs.duration),
                )
            )
        return list(by_trace.values())

    def xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_7(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        data = self._list_spans(self._slow_filter(request), request.time_window_minutes)
        by_trace: dict[str, list[TraceSpan]] = None
        for span in data:
            attrs = span.attributes
            trace_id = str(attrs.trace_id)
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(attrs.operation_name),
                    duration_ms=_as_float(attrs.duration),
                )
            )
        return list(by_trace.values())

    def xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_8(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        data = self._list_spans(self._slow_filter(request), request.time_window_minutes)
        by_trace: dict[str, list[TraceSpan]] = {}
        for span in data:
            attrs = None
            trace_id = str(attrs.trace_id)
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(attrs.operation_name),
                    duration_ms=_as_float(attrs.duration),
                )
            )
        return list(by_trace.values())

    def xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_9(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        data = self._list_spans(self._slow_filter(request), request.time_window_minutes)
        by_trace: dict[str, list[TraceSpan]] = {}
        for span in data:
            attrs = span.attributes
            trace_id = None
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(attrs.operation_name),
                    duration_ms=_as_float(attrs.duration),
                )
            )
        return list(by_trace.values())

    def xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_10(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        data = self._list_spans(self._slow_filter(request), request.time_window_minutes)
        by_trace: dict[str, list[TraceSpan]] = {}
        for span in data:
            attrs = span.attributes
            trace_id = str(None)
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(attrs.operation_name),
                    duration_ms=_as_float(attrs.duration),
                )
            )
        return list(by_trace.values())

    def xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_11(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        data = self._list_spans(self._slow_filter(request), request.time_window_minutes)
        by_trace: dict[str, list[TraceSpan]] = {}
        for span in data:
            attrs = span.attributes
            trace_id = str(attrs.trace_id)
            by_trace.setdefault(trace_id, []).append(
                None
            )
        return list(by_trace.values())

    def xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_12(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        data = self._list_spans(self._slow_filter(request), request.time_window_minutes)
        by_trace: dict[str, list[TraceSpan]] = {}
        for span in data:
            attrs = span.attributes
            trace_id = str(attrs.trace_id)
            by_trace.setdefault(None, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(attrs.operation_name),
                    duration_ms=_as_float(attrs.duration),
                )
            )
        return list(by_trace.values())

    def xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_13(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        data = self._list_spans(self._slow_filter(request), request.time_window_minutes)
        by_trace: dict[str, list[TraceSpan]] = {}
        for span in data:
            attrs = span.attributes
            trace_id = str(attrs.trace_id)
            by_trace.setdefault(trace_id, None).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(attrs.operation_name),
                    duration_ms=_as_float(attrs.duration),
                )
            )
        return list(by_trace.values())

    def xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_14(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        data = self._list_spans(self._slow_filter(request), request.time_window_minutes)
        by_trace: dict[str, list[TraceSpan]] = {}
        for span in data:
            attrs = span.attributes
            trace_id = str(attrs.trace_id)
            by_trace.setdefault([]).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(attrs.operation_name),
                    duration_ms=_as_float(attrs.duration),
                )
            )
        return list(by_trace.values())

    def xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_15(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        data = self._list_spans(self._slow_filter(request), request.time_window_minutes)
        by_trace: dict[str, list[TraceSpan]] = {}
        for span in data:
            attrs = span.attributes
            trace_id = str(attrs.trace_id)
            by_trace.setdefault(trace_id, ).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(attrs.operation_name),
                    duration_ms=_as_float(attrs.duration),
                )
            )
        return list(by_trace.values())

    def xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_16(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        data = self._list_spans(self._slow_filter(request), request.time_window_minutes)
        by_trace: dict[str, list[TraceSpan]] = {}
        for span in data:
            attrs = span.attributes
            trace_id = str(attrs.trace_id)
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=None,
                    span_name=str(attrs.operation_name),
                    duration_ms=_as_float(attrs.duration),
                )
            )
        return list(by_trace.values())

    def xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_17(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        data = self._list_spans(self._slow_filter(request), request.time_window_minutes)
        by_trace: dict[str, list[TraceSpan]] = {}
        for span in data:
            attrs = span.attributes
            trace_id = str(attrs.trace_id)
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=None,
                    duration_ms=_as_float(attrs.duration),
                )
            )
        return list(by_trace.values())

    def xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_18(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        data = self._list_spans(self._slow_filter(request), request.time_window_minutes)
        by_trace: dict[str, list[TraceSpan]] = {}
        for span in data:
            attrs = span.attributes
            trace_id = str(attrs.trace_id)
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(attrs.operation_name),
                    duration_ms=None,
                )
            )
        return list(by_trace.values())

    def xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_19(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        data = self._list_spans(self._slow_filter(request), request.time_window_minutes)
        by_trace: dict[str, list[TraceSpan]] = {}
        for span in data:
            attrs = span.attributes
            trace_id = str(attrs.trace_id)
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    span_name=str(attrs.operation_name),
                    duration_ms=_as_float(attrs.duration),
                )
            )
        return list(by_trace.values())

    def xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_20(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        data = self._list_spans(self._slow_filter(request), request.time_window_minutes)
        by_trace: dict[str, list[TraceSpan]] = {}
        for span in data:
            attrs = span.attributes
            trace_id = str(attrs.trace_id)
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    duration_ms=_as_float(attrs.duration),
                )
            )
        return list(by_trace.values())

    def xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_21(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        data = self._list_spans(self._slow_filter(request), request.time_window_minutes)
        by_trace: dict[str, list[TraceSpan]] = {}
        for span in data:
            attrs = span.attributes
            trace_id = str(attrs.trace_id)
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(attrs.operation_name),
                    )
            )
        return list(by_trace.values())

    def xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_22(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        data = self._list_spans(self._slow_filter(request), request.time_window_minutes)
        by_trace: dict[str, list[TraceSpan]] = {}
        for span in data:
            attrs = span.attributes
            trace_id = str(attrs.trace_id)
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(None),
                    duration_ms=_as_float(attrs.duration),
                )
            )
        return list(by_trace.values())

    def xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_23(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        data = self._list_spans(self._slow_filter(request), request.time_window_minutes)
        by_trace: dict[str, list[TraceSpan]] = {}
        for span in data:
            attrs = span.attributes
            trace_id = str(attrs.trace_id)
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(attrs.operation_name),
                    duration_ms=_as_float(None),
                )
            )
        return list(by_trace.values())

    def xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_24(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        data = self._list_spans(self._slow_filter(request), request.time_window_minutes)
        by_trace: dict[str, list[TraceSpan]] = {}
        for span in data:
            attrs = span.attributes
            trace_id = str(attrs.trace_id)
            by_trace.setdefault(trace_id, []).append(
                TraceSpan(
                    trace_id=trace_id,
                    span_name=str(attrs.operation_name),
                    duration_ms=_as_float(attrs.duration),
                )
            )
        return list(None)

    @_mutmut_mutated(mutants_xǁDatadogTracesAdapterǁfetch_total_traces__mutmut)
    def fetch_total_traces(self, request: LatencyDiagnosticRequest) -> int:
        data = self._list_spans(self._total_filter(request), request.time_window_minutes)
        return len({span.attributes.trace_id for span in data})

    def xǁDatadogTracesAdapterǁfetch_total_traces__mutmut_orig(self, request: LatencyDiagnosticRequest) -> int:
        data = self._list_spans(self._total_filter(request), request.time_window_minutes)
        return len({span.attributes.trace_id for span in data})

    def xǁDatadogTracesAdapterǁfetch_total_traces__mutmut_1(self, request: LatencyDiagnosticRequest) -> int:
        data = None
        return len({span.attributes.trace_id for span in data})

    def xǁDatadogTracesAdapterǁfetch_total_traces__mutmut_2(self, request: LatencyDiagnosticRequest) -> int:
        data = self._list_spans(None, request.time_window_minutes)
        return len({span.attributes.trace_id for span in data})

    def xǁDatadogTracesAdapterǁfetch_total_traces__mutmut_3(self, request: LatencyDiagnosticRequest) -> int:
        data = self._list_spans(self._total_filter(request), None)
        return len({span.attributes.trace_id for span in data})

    def xǁDatadogTracesAdapterǁfetch_total_traces__mutmut_4(self, request: LatencyDiagnosticRequest) -> int:
        data = self._list_spans(request.time_window_minutes)
        return len({span.attributes.trace_id for span in data})

    def xǁDatadogTracesAdapterǁfetch_total_traces__mutmut_5(self, request: LatencyDiagnosticRequest) -> int:
        data = self._list_spans(self._total_filter(request), )
        return len({span.attributes.trace_id for span in data})

    def xǁDatadogTracesAdapterǁfetch_total_traces__mutmut_6(self, request: LatencyDiagnosticRequest) -> int:
        data = self._list_spans(self._total_filter(None), request.time_window_minutes)
        return len({span.attributes.trace_id for span in data})

    @_mutmut_mutated(mutants_xǁDatadogTracesAdapterǁ_slow_filter__mutmut)
    def _slow_filter(self, request: LatencyDiagnosticRequest) -> str:
        threshold = int(request.threshold_ms)
        return f"service:{request.service_name} @duration:>{threshold}ms"

    def xǁDatadogTracesAdapterǁ_slow_filter__mutmut_orig(self, request: LatencyDiagnosticRequest) -> str:
        threshold = int(request.threshold_ms)
        return f"service:{request.service_name} @duration:>{threshold}ms"

    def xǁDatadogTracesAdapterǁ_slow_filter__mutmut_1(self, request: LatencyDiagnosticRequest) -> str:
        threshold = None
        return f"service:{request.service_name} @duration:>{threshold}ms"

    def xǁDatadogTracesAdapterǁ_slow_filter__mutmut_2(self, request: LatencyDiagnosticRequest) -> str:
        threshold = int(None)
        return f"service:{request.service_name} @duration:>{threshold}ms"

    def _total_filter(self, request: LatencyDiagnosticRequest) -> str:
        return f"service:{request.service_name}"

    @_mutmut_mutated(mutants_xǁDatadogTracesAdapterǁ_list_spans__mutmut)
    def _list_spans(self, query: str, window_minutes: int) -> list[_Span]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.spans_list_request import SpansListRequest
        from datadog_api_client.v2.model.spans_list_request_attributes import (
            SpansListRequestAttributes,
        )
        from datadog_api_client.v2.model.spans_list_request_data import (
            SpansListRequestData,
        )
        from datadog_api_client.v2.model.spans_query_filter import SpansQueryFilter

        now = datetime.now(UTC)
        body = SpansListRequest(
            data=SpansListRequestData(
                attributes=SpansListRequestAttributes(
                    filter=SpansQueryFilter(
                        query=query,
                        _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                        to=now.isoformat(),
                    )
                )
            )
        )
        try:
            response = self._api().list_spans(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        data: list[_Span] = list(response.data or [])
        return data

    def xǁDatadogTracesAdapterǁ_list_spans__mutmut_orig(self, query: str, window_minutes: int) -> list[_Span]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.spans_list_request import SpansListRequest
        from datadog_api_client.v2.model.spans_list_request_attributes import (
            SpansListRequestAttributes,
        )
        from datadog_api_client.v2.model.spans_list_request_data import (
            SpansListRequestData,
        )
        from datadog_api_client.v2.model.spans_query_filter import SpansQueryFilter

        now = datetime.now(UTC)
        body = SpansListRequest(
            data=SpansListRequestData(
                attributes=SpansListRequestAttributes(
                    filter=SpansQueryFilter(
                        query=query,
                        _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                        to=now.isoformat(),
                    )
                )
            )
        )
        try:
            response = self._api().list_spans(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        data: list[_Span] = list(response.data or [])
        return data

    def xǁDatadogTracesAdapterǁ_list_spans__mutmut_1(self, query: str, window_minutes: int) -> list[_Span]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.spans_list_request import SpansListRequest
        from datadog_api_client.v2.model.spans_list_request_attributes import (
            SpansListRequestAttributes,
        )
        from datadog_api_client.v2.model.spans_list_request_data import (
            SpansListRequestData,
        )
        from datadog_api_client.v2.model.spans_query_filter import SpansQueryFilter

        now = None
        body = SpansListRequest(
            data=SpansListRequestData(
                attributes=SpansListRequestAttributes(
                    filter=SpansQueryFilter(
                        query=query,
                        _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                        to=now.isoformat(),
                    )
                )
            )
        )
        try:
            response = self._api().list_spans(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        data: list[_Span] = list(response.data or [])
        return data

    def xǁDatadogTracesAdapterǁ_list_spans__mutmut_2(self, query: str, window_minutes: int) -> list[_Span]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.spans_list_request import SpansListRequest
        from datadog_api_client.v2.model.spans_list_request_attributes import (
            SpansListRequestAttributes,
        )
        from datadog_api_client.v2.model.spans_list_request_data import (
            SpansListRequestData,
        )
        from datadog_api_client.v2.model.spans_query_filter import SpansQueryFilter

        now = datetime.now(None)
        body = SpansListRequest(
            data=SpansListRequestData(
                attributes=SpansListRequestAttributes(
                    filter=SpansQueryFilter(
                        query=query,
                        _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                        to=now.isoformat(),
                    )
                )
            )
        )
        try:
            response = self._api().list_spans(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        data: list[_Span] = list(response.data or [])
        return data

    def xǁDatadogTracesAdapterǁ_list_spans__mutmut_3(self, query: str, window_minutes: int) -> list[_Span]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.spans_list_request import SpansListRequest
        from datadog_api_client.v2.model.spans_list_request_attributes import (
            SpansListRequestAttributes,
        )
        from datadog_api_client.v2.model.spans_list_request_data import (
            SpansListRequestData,
        )
        from datadog_api_client.v2.model.spans_query_filter import SpansQueryFilter

        now = datetime.now(UTC)
        body = None
        try:
            response = self._api().list_spans(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        data: list[_Span] = list(response.data or [])
        return data

    def xǁDatadogTracesAdapterǁ_list_spans__mutmut_4(self, query: str, window_minutes: int) -> list[_Span]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.spans_list_request import SpansListRequest
        from datadog_api_client.v2.model.spans_list_request_attributes import (
            SpansListRequestAttributes,
        )
        from datadog_api_client.v2.model.spans_list_request_data import (
            SpansListRequestData,
        )
        from datadog_api_client.v2.model.spans_query_filter import SpansQueryFilter

        now = datetime.now(UTC)
        body = SpansListRequest(
            data=None
        )
        try:
            response = self._api().list_spans(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        data: list[_Span] = list(response.data or [])
        return data

    def xǁDatadogTracesAdapterǁ_list_spans__mutmut_5(self, query: str, window_minutes: int) -> list[_Span]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.spans_list_request import SpansListRequest
        from datadog_api_client.v2.model.spans_list_request_attributes import (
            SpansListRequestAttributes,
        )
        from datadog_api_client.v2.model.spans_list_request_data import (
            SpansListRequestData,
        )
        from datadog_api_client.v2.model.spans_query_filter import SpansQueryFilter

        now = datetime.now(UTC)
        body = SpansListRequest(
            data=SpansListRequestData(
                attributes=None
            )
        )
        try:
            response = self._api().list_spans(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        data: list[_Span] = list(response.data or [])
        return data

    def xǁDatadogTracesAdapterǁ_list_spans__mutmut_6(self, query: str, window_minutes: int) -> list[_Span]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.spans_list_request import SpansListRequest
        from datadog_api_client.v2.model.spans_list_request_attributes import (
            SpansListRequestAttributes,
        )
        from datadog_api_client.v2.model.spans_list_request_data import (
            SpansListRequestData,
        )
        from datadog_api_client.v2.model.spans_query_filter import SpansQueryFilter

        now = datetime.now(UTC)
        body = SpansListRequest(
            data=SpansListRequestData(
                attributes=SpansListRequestAttributes(
                    filter=None
                )
            )
        )
        try:
            response = self._api().list_spans(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        data: list[_Span] = list(response.data or [])
        return data

    def xǁDatadogTracesAdapterǁ_list_spans__mutmut_7(self, query: str, window_minutes: int) -> list[_Span]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.spans_list_request import SpansListRequest
        from datadog_api_client.v2.model.spans_list_request_attributes import (
            SpansListRequestAttributes,
        )
        from datadog_api_client.v2.model.spans_list_request_data import (
            SpansListRequestData,
        )
        from datadog_api_client.v2.model.spans_query_filter import SpansQueryFilter

        now = datetime.now(UTC)
        body = SpansListRequest(
            data=SpansListRequestData(
                attributes=SpansListRequestAttributes(
                    filter=SpansQueryFilter(
                        query=None,
                        _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                        to=now.isoformat(),
                    )
                )
            )
        )
        try:
            response = self._api().list_spans(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        data: list[_Span] = list(response.data or [])
        return data

    def xǁDatadogTracesAdapterǁ_list_spans__mutmut_8(self, query: str, window_minutes: int) -> list[_Span]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.spans_list_request import SpansListRequest
        from datadog_api_client.v2.model.spans_list_request_attributes import (
            SpansListRequestAttributes,
        )
        from datadog_api_client.v2.model.spans_list_request_data import (
            SpansListRequestData,
        )
        from datadog_api_client.v2.model.spans_query_filter import SpansQueryFilter

        now = datetime.now(UTC)
        body = SpansListRequest(
            data=SpansListRequestData(
                attributes=SpansListRequestAttributes(
                    filter=SpansQueryFilter(
                        query=query,
                        _from=None,
                        to=now.isoformat(),
                    )
                )
            )
        )
        try:
            response = self._api().list_spans(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        data: list[_Span] = list(response.data or [])
        return data

    def xǁDatadogTracesAdapterǁ_list_spans__mutmut_9(self, query: str, window_minutes: int) -> list[_Span]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.spans_list_request import SpansListRequest
        from datadog_api_client.v2.model.spans_list_request_attributes import (
            SpansListRequestAttributes,
        )
        from datadog_api_client.v2.model.spans_list_request_data import (
            SpansListRequestData,
        )
        from datadog_api_client.v2.model.spans_query_filter import SpansQueryFilter

        now = datetime.now(UTC)
        body = SpansListRequest(
            data=SpansListRequestData(
                attributes=SpansListRequestAttributes(
                    filter=SpansQueryFilter(
                        query=query,
                        _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                        to=None,
                    )
                )
            )
        )
        try:
            response = self._api().list_spans(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        data: list[_Span] = list(response.data or [])
        return data

    def xǁDatadogTracesAdapterǁ_list_spans__mutmut_10(self, query: str, window_minutes: int) -> list[_Span]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.spans_list_request import SpansListRequest
        from datadog_api_client.v2.model.spans_list_request_attributes import (
            SpansListRequestAttributes,
        )
        from datadog_api_client.v2.model.spans_list_request_data import (
            SpansListRequestData,
        )
        from datadog_api_client.v2.model.spans_query_filter import SpansQueryFilter

        now = datetime.now(UTC)
        body = SpansListRequest(
            data=SpansListRequestData(
                attributes=SpansListRequestAttributes(
                    filter=SpansQueryFilter(
                        _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                        to=now.isoformat(),
                    )
                )
            )
        )
        try:
            response = self._api().list_spans(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        data: list[_Span] = list(response.data or [])
        return data

    def xǁDatadogTracesAdapterǁ_list_spans__mutmut_11(self, query: str, window_minutes: int) -> list[_Span]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.spans_list_request import SpansListRequest
        from datadog_api_client.v2.model.spans_list_request_attributes import (
            SpansListRequestAttributes,
        )
        from datadog_api_client.v2.model.spans_list_request_data import (
            SpansListRequestData,
        )
        from datadog_api_client.v2.model.spans_query_filter import SpansQueryFilter

        now = datetime.now(UTC)
        body = SpansListRequest(
            data=SpansListRequestData(
                attributes=SpansListRequestAttributes(
                    filter=SpansQueryFilter(
                        query=query,
                        to=now.isoformat(),
                    )
                )
            )
        )
        try:
            response = self._api().list_spans(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        data: list[_Span] = list(response.data or [])
        return data

    def xǁDatadogTracesAdapterǁ_list_spans__mutmut_12(self, query: str, window_minutes: int) -> list[_Span]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.spans_list_request import SpansListRequest
        from datadog_api_client.v2.model.spans_list_request_attributes import (
            SpansListRequestAttributes,
        )
        from datadog_api_client.v2.model.spans_list_request_data import (
            SpansListRequestData,
        )
        from datadog_api_client.v2.model.spans_query_filter import SpansQueryFilter

        now = datetime.now(UTC)
        body = SpansListRequest(
            data=SpansListRequestData(
                attributes=SpansListRequestAttributes(
                    filter=SpansQueryFilter(
                        query=query,
                        _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                        )
                )
            )
        )
        try:
            response = self._api().list_spans(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        data: list[_Span] = list(response.data or [])
        return data

    def xǁDatadogTracesAdapterǁ_list_spans__mutmut_13(self, query: str, window_minutes: int) -> list[_Span]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.spans_list_request import SpansListRequest
        from datadog_api_client.v2.model.spans_list_request_attributes import (
            SpansListRequestAttributes,
        )
        from datadog_api_client.v2.model.spans_list_request_data import (
            SpansListRequestData,
        )
        from datadog_api_client.v2.model.spans_query_filter import SpansQueryFilter

        now = datetime.now(UTC)
        body = SpansListRequest(
            data=SpansListRequestData(
                attributes=SpansListRequestAttributes(
                    filter=SpansQueryFilter(
                        query=query,
                        _from=(now + timedelta(minutes=window_minutes)).isoformat(),
                        to=now.isoformat(),
                    )
                )
            )
        )
        try:
            response = self._api().list_spans(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        data: list[_Span] = list(response.data or [])
        return data

    def xǁDatadogTracesAdapterǁ_list_spans__mutmut_14(self, query: str, window_minutes: int) -> list[_Span]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.spans_list_request import SpansListRequest
        from datadog_api_client.v2.model.spans_list_request_attributes import (
            SpansListRequestAttributes,
        )
        from datadog_api_client.v2.model.spans_list_request_data import (
            SpansListRequestData,
        )
        from datadog_api_client.v2.model.spans_query_filter import SpansQueryFilter

        now = datetime.now(UTC)
        body = SpansListRequest(
            data=SpansListRequestData(
                attributes=SpansListRequestAttributes(
                    filter=SpansQueryFilter(
                        query=query,
                        _from=(now - timedelta(minutes=None)).isoformat(),
                        to=now.isoformat(),
                    )
                )
            )
        )
        try:
            response = self._api().list_spans(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        data: list[_Span] = list(response.data or [])
        return data

    def xǁDatadogTracesAdapterǁ_list_spans__mutmut_15(self, query: str, window_minutes: int) -> list[_Span]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.spans_list_request import SpansListRequest
        from datadog_api_client.v2.model.spans_list_request_attributes import (
            SpansListRequestAttributes,
        )
        from datadog_api_client.v2.model.spans_list_request_data import (
            SpansListRequestData,
        )
        from datadog_api_client.v2.model.spans_query_filter import SpansQueryFilter

        now = datetime.now(UTC)
        body = SpansListRequest(
            data=SpansListRequestData(
                attributes=SpansListRequestAttributes(
                    filter=SpansQueryFilter(
                        query=query,
                        _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                        to=now.isoformat(),
                    )
                )
            )
        )
        try:
            response = None
        except ApiException as exc:
            raise _translate_error(exc) from exc
        data: list[_Span] = list(response.data or [])
        return data

    def xǁDatadogTracesAdapterǁ_list_spans__mutmut_16(self, query: str, window_minutes: int) -> list[_Span]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.spans_list_request import SpansListRequest
        from datadog_api_client.v2.model.spans_list_request_attributes import (
            SpansListRequestAttributes,
        )
        from datadog_api_client.v2.model.spans_list_request_data import (
            SpansListRequestData,
        )
        from datadog_api_client.v2.model.spans_query_filter import SpansQueryFilter

        now = datetime.now(UTC)
        body = SpansListRequest(
            data=SpansListRequestData(
                attributes=SpansListRequestAttributes(
                    filter=SpansQueryFilter(
                        query=query,
                        _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                        to=now.isoformat(),
                    )
                )
            )
        )
        try:
            response = self._api().list_spans(body=None)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        data: list[_Span] = list(response.data or [])
        return data

    def xǁDatadogTracesAdapterǁ_list_spans__mutmut_17(self, query: str, window_minutes: int) -> list[_Span]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.spans_list_request import SpansListRequest
        from datadog_api_client.v2.model.spans_list_request_attributes import (
            SpansListRequestAttributes,
        )
        from datadog_api_client.v2.model.spans_list_request_data import (
            SpansListRequestData,
        )
        from datadog_api_client.v2.model.spans_query_filter import SpansQueryFilter

        now = datetime.now(UTC)
        body = SpansListRequest(
            data=SpansListRequestData(
                attributes=SpansListRequestAttributes(
                    filter=SpansQueryFilter(
                        query=query,
                        _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                        to=now.isoformat(),
                    )
                )
            )
        )
        try:
            response = self._api().list_spans(body=body)
        except ApiException as exc:
            raise _translate_error(None) from exc
        data: list[_Span] = list(response.data or [])
        return data

    def xǁDatadogTracesAdapterǁ_list_spans__mutmut_18(self, query: str, window_minutes: int) -> list[_Span]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.spans_list_request import SpansListRequest
        from datadog_api_client.v2.model.spans_list_request_attributes import (
            SpansListRequestAttributes,
        )
        from datadog_api_client.v2.model.spans_list_request_data import (
            SpansListRequestData,
        )
        from datadog_api_client.v2.model.spans_query_filter import SpansQueryFilter

        now = datetime.now(UTC)
        body = SpansListRequest(
            data=SpansListRequestData(
                attributes=SpansListRequestAttributes(
                    filter=SpansQueryFilter(
                        query=query,
                        _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                        to=now.isoformat(),
                    )
                )
            )
        )
        try:
            response = self._api().list_spans(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        data: list[_Span] = None
        return data

    def xǁDatadogTracesAdapterǁ_list_spans__mutmut_19(self, query: str, window_minutes: int) -> list[_Span]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.spans_list_request import SpansListRequest
        from datadog_api_client.v2.model.spans_list_request_attributes import (
            SpansListRequestAttributes,
        )
        from datadog_api_client.v2.model.spans_list_request_data import (
            SpansListRequestData,
        )
        from datadog_api_client.v2.model.spans_query_filter import SpansQueryFilter

        now = datetime.now(UTC)
        body = SpansListRequest(
            data=SpansListRequestData(
                attributes=SpansListRequestAttributes(
                    filter=SpansQueryFilter(
                        query=query,
                        _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                        to=now.isoformat(),
                    )
                )
            )
        )
        try:
            response = self._api().list_spans(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        data: list[_Span] = list(None)
        return data

    def xǁDatadogTracesAdapterǁ_list_spans__mutmut_20(self, query: str, window_minutes: int) -> list[_Span]:
        from datadog_api_client.exceptions import ApiException
        from datadog_api_client.v2.model.spans_list_request import SpansListRequest
        from datadog_api_client.v2.model.spans_list_request_attributes import (
            SpansListRequestAttributes,
        )
        from datadog_api_client.v2.model.spans_list_request_data import (
            SpansListRequestData,
        )
        from datadog_api_client.v2.model.spans_query_filter import SpansQueryFilter

        now = datetime.now(UTC)
        body = SpansListRequest(
            data=SpansListRequestData(
                attributes=SpansListRequestAttributes(
                    filter=SpansQueryFilter(
                        query=query,
                        _from=(now - timedelta(minutes=window_minutes)).isoformat(),
                        to=now.isoformat(),
                    )
                )
            )
        )
        try:
            response = self._api().list_spans(body=body)
        except ApiException as exc:
            raise _translate_error(exc) from exc
        data: list[_Span] = list(response.data and [])
        return data

    @_mutmut_mutated(mutants_xǁDatadogTracesAdapterǁ_api__mutmut)
    def _api(self) -> SpansApi:
        if self._spans_api is None:
            self._spans_api = _build_spans_api(self._key, self._app_key, self._site)
        return self._spans_api

    def xǁDatadogTracesAdapterǁ_api__mutmut_orig(self) -> SpansApi:
        if self._spans_api is None:
            self._spans_api = _build_spans_api(self._key, self._app_key, self._site)
        return self._spans_api

    def xǁDatadogTracesAdapterǁ_api__mutmut_1(self) -> SpansApi:
        if self._spans_api is not None:
            self._spans_api = _build_spans_api(self._key, self._app_key, self._site)
        return self._spans_api

    def xǁDatadogTracesAdapterǁ_api__mutmut_2(self) -> SpansApi:
        if self._spans_api is None:
            self._spans_api = None
        return self._spans_api

    def xǁDatadogTracesAdapterǁ_api__mutmut_3(self) -> SpansApi:
        if self._spans_api is None:
            self._spans_api = _build_spans_api(None, self._app_key, self._site)
        return self._spans_api

    def xǁDatadogTracesAdapterǁ_api__mutmut_4(self) -> SpansApi:
        if self._spans_api is None:
            self._spans_api = _build_spans_api(self._key, None, self._site)
        return self._spans_api

    def xǁDatadogTracesAdapterǁ_api__mutmut_5(self) -> SpansApi:
        if self._spans_api is None:
            self._spans_api = _build_spans_api(self._key, self._app_key, None)
        return self._spans_api

    def xǁDatadogTracesAdapterǁ_api__mutmut_6(self) -> SpansApi:
        if self._spans_api is None:
            self._spans_api = _build_spans_api(self._app_key, self._site)
        return self._spans_api

    def xǁDatadogTracesAdapterǁ_api__mutmut_7(self) -> SpansApi:
        if self._spans_api is None:
            self._spans_api = _build_spans_api(self._key, self._site)
        return self._spans_api

    def xǁDatadogTracesAdapterǁ_api__mutmut_8(self) -> SpansApi:
        if self._spans_api is None:
            self._spans_api = _build_spans_api(self._key, self._app_key, )
        return self._spans_api

mutants_xǁDatadogTracesAdapterǁ__init____mutmut['_mutmut_orig'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ__init____mutmut['xǁDatadogTracesAdapterǁ__init____mutmut_1'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ__init____mutmut['xǁDatadogTracesAdapterǁ__init____mutmut_2'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ__init____mutmut['xǁDatadogTracesAdapterǁ__init____mutmut_3'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ__init____mutmut['xǁDatadogTracesAdapterǁ__init____mutmut_4'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ__init____mutmut['xǁDatadogTracesAdapterǁ__init____mutmut_5'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ__init____mutmut['xǁDatadogTracesAdapterǁ__init____mutmut_6'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ__init____mutmut['xǁDatadogTracesAdapterǁ__init____mutmut_7'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ__init____mutmut['xǁDatadogTracesAdapterǁ__init____mutmut_8'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ__init____mutmut_8 # type: ignore # mutmut generated

mutants_xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut['_mutmut_orig'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut['xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_1'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut['xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_2'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut['xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_3'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut['xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_4'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut['xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_5'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut['xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_6'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut['xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_7'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut['xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_8'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut['xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_9'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut['xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_10'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut['xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_11'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut['xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_12'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut['xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_13'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut['xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_14'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut['xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_15'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut['xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_16'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut['xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_17'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut['xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_18'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut['xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_19'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut['xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_20'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut['xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_21'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut['xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_22'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut['xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_23'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut['xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_24'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁfetch_slow_spans__mutmut_24 # type: ignore # mutmut generated

mutants_xǁDatadogTracesAdapterǁfetch_total_traces__mutmut['_mutmut_orig'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁfetch_total_traces__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁfetch_total_traces__mutmut['xǁDatadogTracesAdapterǁfetch_total_traces__mutmut_1'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁfetch_total_traces__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁfetch_total_traces__mutmut['xǁDatadogTracesAdapterǁfetch_total_traces__mutmut_2'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁfetch_total_traces__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁfetch_total_traces__mutmut['xǁDatadogTracesAdapterǁfetch_total_traces__mutmut_3'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁfetch_total_traces__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁfetch_total_traces__mutmut['xǁDatadogTracesAdapterǁfetch_total_traces__mutmut_4'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁfetch_total_traces__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁfetch_total_traces__mutmut['xǁDatadogTracesAdapterǁfetch_total_traces__mutmut_5'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁfetch_total_traces__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁfetch_total_traces__mutmut['xǁDatadogTracesAdapterǁfetch_total_traces__mutmut_6'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁfetch_total_traces__mutmut_6 # type: ignore # mutmut generated

mutants_xǁDatadogTracesAdapterǁ_slow_filter__mutmut['_mutmut_orig'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ_slow_filter__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ_slow_filter__mutmut['xǁDatadogTracesAdapterǁ_slow_filter__mutmut_1'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ_slow_filter__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ_slow_filter__mutmut['xǁDatadogTracesAdapterǁ_slow_filter__mutmut_2'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ_slow_filter__mutmut_2 # type: ignore # mutmut generated

mutants_xǁDatadogTracesAdapterǁ_list_spans__mutmut['_mutmut_orig'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ_list_spans__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ_list_spans__mutmut['xǁDatadogTracesAdapterǁ_list_spans__mutmut_1'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ_list_spans__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ_list_spans__mutmut['xǁDatadogTracesAdapterǁ_list_spans__mutmut_2'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ_list_spans__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ_list_spans__mutmut['xǁDatadogTracesAdapterǁ_list_spans__mutmut_3'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ_list_spans__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ_list_spans__mutmut['xǁDatadogTracesAdapterǁ_list_spans__mutmut_4'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ_list_spans__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ_list_spans__mutmut['xǁDatadogTracesAdapterǁ_list_spans__mutmut_5'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ_list_spans__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ_list_spans__mutmut['xǁDatadogTracesAdapterǁ_list_spans__mutmut_6'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ_list_spans__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ_list_spans__mutmut['xǁDatadogTracesAdapterǁ_list_spans__mutmut_7'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ_list_spans__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ_list_spans__mutmut['xǁDatadogTracesAdapterǁ_list_spans__mutmut_8'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ_list_spans__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ_list_spans__mutmut['xǁDatadogTracesAdapterǁ_list_spans__mutmut_9'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ_list_spans__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ_list_spans__mutmut['xǁDatadogTracesAdapterǁ_list_spans__mutmut_10'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ_list_spans__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ_list_spans__mutmut['xǁDatadogTracesAdapterǁ_list_spans__mutmut_11'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ_list_spans__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ_list_spans__mutmut['xǁDatadogTracesAdapterǁ_list_spans__mutmut_12'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ_list_spans__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ_list_spans__mutmut['xǁDatadogTracesAdapterǁ_list_spans__mutmut_13'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ_list_spans__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ_list_spans__mutmut['xǁDatadogTracesAdapterǁ_list_spans__mutmut_14'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ_list_spans__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ_list_spans__mutmut['xǁDatadogTracesAdapterǁ_list_spans__mutmut_15'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ_list_spans__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ_list_spans__mutmut['xǁDatadogTracesAdapterǁ_list_spans__mutmut_16'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ_list_spans__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ_list_spans__mutmut['xǁDatadogTracesAdapterǁ_list_spans__mutmut_17'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ_list_spans__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ_list_spans__mutmut['xǁDatadogTracesAdapterǁ_list_spans__mutmut_18'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ_list_spans__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ_list_spans__mutmut['xǁDatadogTracesAdapterǁ_list_spans__mutmut_19'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ_list_spans__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ_list_spans__mutmut['xǁDatadogTracesAdapterǁ_list_spans__mutmut_20'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ_list_spans__mutmut_20 # type: ignore # mutmut generated

mutants_xǁDatadogTracesAdapterǁ_api__mutmut['_mutmut_orig'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ_api__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ_api__mutmut['xǁDatadogTracesAdapterǁ_api__mutmut_1'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ_api__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ_api__mutmut['xǁDatadogTracesAdapterǁ_api__mutmut_2'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ_api__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ_api__mutmut['xǁDatadogTracesAdapterǁ_api__mutmut_3'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ_api__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ_api__mutmut['xǁDatadogTracesAdapterǁ_api__mutmut_4'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ_api__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ_api__mutmut['xǁDatadogTracesAdapterǁ_api__mutmut_5'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ_api__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ_api__mutmut['xǁDatadogTracesAdapterǁ_api__mutmut_6'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ_api__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ_api__mutmut['xǁDatadogTracesAdapterǁ_api__mutmut_7'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ_api__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDatadogTracesAdapterǁ_api__mutmut['xǁDatadogTracesAdapterǁ_api__mutmut_8'] = DatadogTracesAdapter.xǁDatadogTracesAdapterǁ_api__mutmut_8 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__translate_error__mutmut)
def _translate_error(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_orig(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_1(exc: Exception) -> Exception:
    status = None
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_2(exc: Exception) -> Exception:
    status = getattr(None, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_3(exc: Exception) -> Exception:
    status = getattr(exc, None, None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_4(exc: Exception) -> Exception:
    status = getattr("status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_5(exc: Exception) -> Exception:
    status = getattr(exc, None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_6(exc: Exception) -> Exception:
    status = getattr(exc, "status", )
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_7(exc: Exception) -> Exception:
    status = getattr(exc, "XXstatusXX", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_8(exc: Exception) -> Exception:
    status = getattr(exc, "STATUS", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_9(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status != _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_10(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError(None, context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_11(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context=None)
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_12(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError(context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_13(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", )
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_14(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("XXDatadog rate limit reached.XX", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_15(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_16(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("DATADOG RATE LIMIT REACHED.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_17(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"XXstatusXX": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_18(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"STATUS": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_19(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(None)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_20(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status not in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_21(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            None,
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_22(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context=None,
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_23(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_24(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_25(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "XXDatadog API rejected the credentials.XX",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_26(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "datadog api rejected the credentials.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_27(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "DATADOG API REJECTED THE CREDENTIALS.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_28(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"XXstatusXX": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_29(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"STATUS": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_30(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"status": str(None)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_31(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        None, context={"status": str(status)}
    )


def x__translate_error__mutmut_32(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context=None
    )


def x__translate_error__mutmut_33(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        context={"status": str(status)}
    )


def x__translate_error__mutmut_34(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", )


def x__translate_error__mutmut_35(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "XXDatadog Spans API request failed.XX", context={"status": str(status)}
    )


def x__translate_error__mutmut_36(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "datadog spans api request failed.", context={"status": str(status)}
    )


def x__translate_error__mutmut_37(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "DATADOG SPANS API REQUEST FAILED.", context={"status": str(status)}
    )


def x__translate_error__mutmut_38(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"XXstatusXX": str(status)}
    )


def x__translate_error__mutmut_39(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"STATUS": str(status)}
    )


def x__translate_error__mutmut_40(exc: Exception) -> Exception:
    status = getattr(exc, "status", None)
    if status == _RATE_LIMIT_STATUS:
        return AdapterTimeoutError("Datadog rate limit reached.", context={"status": str(status)})
    if status in _UNAUTHORIZED_STATUSES:
        return InsufficientPermissionsError(
            "Datadog API rejected the credentials.",
            context={"status": str(status)},
        )
    return TracesUnavailableError(
        "Datadog Spans API request failed.", context={"status": str(None)}
    )

mutants_x__translate_error__mutmut['_mutmut_orig'] = x__translate_error__mutmut_orig # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_1'] = x__translate_error__mutmut_1 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_2'] = x__translate_error__mutmut_2 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_3'] = x__translate_error__mutmut_3 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_4'] = x__translate_error__mutmut_4 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_5'] = x__translate_error__mutmut_5 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_6'] = x__translate_error__mutmut_6 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_7'] = x__translate_error__mutmut_7 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_8'] = x__translate_error__mutmut_8 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_9'] = x__translate_error__mutmut_9 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_10'] = x__translate_error__mutmut_10 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_11'] = x__translate_error__mutmut_11 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_12'] = x__translate_error__mutmut_12 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_13'] = x__translate_error__mutmut_13 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_14'] = x__translate_error__mutmut_14 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_15'] = x__translate_error__mutmut_15 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_16'] = x__translate_error__mutmut_16 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_17'] = x__translate_error__mutmut_17 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_18'] = x__translate_error__mutmut_18 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_19'] = x__translate_error__mutmut_19 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_20'] = x__translate_error__mutmut_20 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_21'] = x__translate_error__mutmut_21 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_22'] = x__translate_error__mutmut_22 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_23'] = x__translate_error__mutmut_23 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_24'] = x__translate_error__mutmut_24 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_25'] = x__translate_error__mutmut_25 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_26'] = x__translate_error__mutmut_26 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_27'] = x__translate_error__mutmut_27 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_28'] = x__translate_error__mutmut_28 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_29'] = x__translate_error__mutmut_29 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_30'] = x__translate_error__mutmut_30 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_31'] = x__translate_error__mutmut_31 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_32'] = x__translate_error__mutmut_32 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_33'] = x__translate_error__mutmut_33 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_34'] = x__translate_error__mutmut_34 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_35'] = x__translate_error__mutmut_35 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_36'] = x__translate_error__mutmut_36 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_37'] = x__translate_error__mutmut_37 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_38'] = x__translate_error__mutmut_38 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_39'] = x__translate_error__mutmut_39 # type: ignore # mutmut generated
mutants_x__translate_error__mutmut['x__translate_error__mutmut_40'] = x__translate_error__mutmut_40 # type: ignore # mutmut generated
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
mutants_x__build_spans_api__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_spans_api__mutmut)
def _build_spans_api(key: str, app_key: str, site: str) -> SpansApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.spans_api import SpansApi as DatadogSpansApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(SpansApi, DatadogSpansApi(ApiClient(configuration)))


def x__build_spans_api__mutmut_orig(key: str, app_key: str, site: str) -> SpansApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.spans_api import SpansApi as DatadogSpansApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(SpansApi, DatadogSpansApi(ApiClient(configuration)))


def x__build_spans_api__mutmut_1(key: str, app_key: str, site: str) -> SpansApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.spans_api import SpansApi as DatadogSpansApi

    configuration = None
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(SpansApi, DatadogSpansApi(ApiClient(configuration)))


def x__build_spans_api__mutmut_2(key: str, app_key: str, site: str) -> SpansApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.spans_api import SpansApi as DatadogSpansApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = None
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(SpansApi, DatadogSpansApi(ApiClient(configuration)))


def x__build_spans_api__mutmut_3(key: str, app_key: str, site: str) -> SpansApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.spans_api import SpansApi as DatadogSpansApi

    configuration = Configuration()
    configuration.api_key["XXapiKeyAuthXX"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(SpansApi, DatadogSpansApi(ApiClient(configuration)))


def x__build_spans_api__mutmut_4(key: str, app_key: str, site: str) -> SpansApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.spans_api import SpansApi as DatadogSpansApi

    configuration = Configuration()
    configuration.api_key["apikeyauth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(SpansApi, DatadogSpansApi(ApiClient(configuration)))


def x__build_spans_api__mutmut_5(key: str, app_key: str, site: str) -> SpansApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.spans_api import SpansApi as DatadogSpansApi

    configuration = Configuration()
    configuration.api_key["APIKEYAUTH"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(SpansApi, DatadogSpansApi(ApiClient(configuration)))


def x__build_spans_api__mutmut_6(key: str, app_key: str, site: str) -> SpansApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.spans_api import SpansApi as DatadogSpansApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = None
    configuration.server_variables["site"] = site
    return cast(SpansApi, DatadogSpansApi(ApiClient(configuration)))


def x__build_spans_api__mutmut_7(key: str, app_key: str, site: str) -> SpansApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.spans_api import SpansApi as DatadogSpansApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["XXappKeyAuthXX"] = app_key
    configuration.server_variables["site"] = site
    return cast(SpansApi, DatadogSpansApi(ApiClient(configuration)))


def x__build_spans_api__mutmut_8(key: str, app_key: str, site: str) -> SpansApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.spans_api import SpansApi as DatadogSpansApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appkeyauth"] = app_key
    configuration.server_variables["site"] = site
    return cast(SpansApi, DatadogSpansApi(ApiClient(configuration)))


def x__build_spans_api__mutmut_9(key: str, app_key: str, site: str) -> SpansApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.spans_api import SpansApi as DatadogSpansApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["APPKEYAUTH"] = app_key
    configuration.server_variables["site"] = site
    return cast(SpansApi, DatadogSpansApi(ApiClient(configuration)))


def x__build_spans_api__mutmut_10(key: str, app_key: str, site: str) -> SpansApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.spans_api import SpansApi as DatadogSpansApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = None
    return cast(SpansApi, DatadogSpansApi(ApiClient(configuration)))


def x__build_spans_api__mutmut_11(key: str, app_key: str, site: str) -> SpansApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.spans_api import SpansApi as DatadogSpansApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["XXsiteXX"] = site
    return cast(SpansApi, DatadogSpansApi(ApiClient(configuration)))


def x__build_spans_api__mutmut_12(key: str, app_key: str, site: str) -> SpansApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.spans_api import SpansApi as DatadogSpansApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["SITE"] = site
    return cast(SpansApi, DatadogSpansApi(ApiClient(configuration)))


def x__build_spans_api__mutmut_13(key: str, app_key: str, site: str) -> SpansApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.spans_api import SpansApi as DatadogSpansApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(None, DatadogSpansApi(ApiClient(configuration)))


def x__build_spans_api__mutmut_14(key: str, app_key: str, site: str) -> SpansApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.spans_api import SpansApi as DatadogSpansApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(SpansApi, None)


def x__build_spans_api__mutmut_15(key: str, app_key: str, site: str) -> SpansApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.spans_api import SpansApi as DatadogSpansApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(DatadogSpansApi(ApiClient(configuration)))


def x__build_spans_api__mutmut_16(key: str, app_key: str, site: str) -> SpansApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.spans_api import SpansApi as DatadogSpansApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(SpansApi, )


def x__build_spans_api__mutmut_17(key: str, app_key: str, site: str) -> SpansApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.spans_api import SpansApi as DatadogSpansApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(SpansApi, DatadogSpansApi(None))


def x__build_spans_api__mutmut_18(key: str, app_key: str, site: str) -> SpansApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.spans_api import SpansApi as DatadogSpansApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(SpansApi, DatadogSpansApi(ApiClient(None)))

mutants_x__build_spans_api__mutmut['_mutmut_orig'] = x__build_spans_api__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_spans_api__mutmut['x__build_spans_api__mutmut_1'] = x__build_spans_api__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_spans_api__mutmut['x__build_spans_api__mutmut_2'] = x__build_spans_api__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_spans_api__mutmut['x__build_spans_api__mutmut_3'] = x__build_spans_api__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_spans_api__mutmut['x__build_spans_api__mutmut_4'] = x__build_spans_api__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_spans_api__mutmut['x__build_spans_api__mutmut_5'] = x__build_spans_api__mutmut_5 # type: ignore # mutmut generated
mutants_x__build_spans_api__mutmut['x__build_spans_api__mutmut_6'] = x__build_spans_api__mutmut_6 # type: ignore # mutmut generated
mutants_x__build_spans_api__mutmut['x__build_spans_api__mutmut_7'] = x__build_spans_api__mutmut_7 # type: ignore # mutmut generated
mutants_x__build_spans_api__mutmut['x__build_spans_api__mutmut_8'] = x__build_spans_api__mutmut_8 # type: ignore # mutmut generated
mutants_x__build_spans_api__mutmut['x__build_spans_api__mutmut_9'] = x__build_spans_api__mutmut_9 # type: ignore # mutmut generated
mutants_x__build_spans_api__mutmut['x__build_spans_api__mutmut_10'] = x__build_spans_api__mutmut_10 # type: ignore # mutmut generated
mutants_x__build_spans_api__mutmut['x__build_spans_api__mutmut_11'] = x__build_spans_api__mutmut_11 # type: ignore # mutmut generated
mutants_x__build_spans_api__mutmut['x__build_spans_api__mutmut_12'] = x__build_spans_api__mutmut_12 # type: ignore # mutmut generated
mutants_x__build_spans_api__mutmut['x__build_spans_api__mutmut_13'] = x__build_spans_api__mutmut_13 # type: ignore # mutmut generated
mutants_x__build_spans_api__mutmut['x__build_spans_api__mutmut_14'] = x__build_spans_api__mutmut_14 # type: ignore # mutmut generated
mutants_x__build_spans_api__mutmut['x__build_spans_api__mutmut_15'] = x__build_spans_api__mutmut_15 # type: ignore # mutmut generated
mutants_x__build_spans_api__mutmut['x__build_spans_api__mutmut_16'] = x__build_spans_api__mutmut_16 # type: ignore # mutmut generated
mutants_x__build_spans_api__mutmut['x__build_spans_api__mutmut_17'] = x__build_spans_api__mutmut_17 # type: ignore # mutmut generated
mutants_x__build_spans_api__mutmut['x__build_spans_api__mutmut_18'] = x__build_spans_api__mutmut_18 # type: ignore # mutmut generated
