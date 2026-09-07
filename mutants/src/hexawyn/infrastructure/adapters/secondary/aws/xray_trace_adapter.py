from __future__ import annotations

import json
from collections.abc import Callable
from datetime import UTC, datetime, timedelta
from typing import Protocol, TypedDict, TypeVar

from hexawyn.application.ports.driven.trace_query_port import (
    LatencyDiagnosticRequest,
    TraceQueryPort,
    TraceSpan,
)
from hexawyn.domain.errors import TracesUnavailableError

_MAX_TRACE_IDS_PER_BATCH = 5
_MILLIS_PER_SECOND = 1000.0
_CREDENTIALS_HINT = "Run 'aws configure' or attach an IAM role, then retry."

_ResponseT = TypeVar("_ResponseT")


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class _TraceSummary(TypedDict, total=False):
    Id: str
    Duration: float


class _GetTraceSummariesResponse(TypedDict, total=False):
    TraceSummaries: list[_TraceSummary]
    NextToken: str


class _Segment(TypedDict, total=False):
    Id: str
    Document: str


class _Trace(TypedDict, total=False):
    Id: str
    Segments: list[_Segment]


class _BatchGetTracesResponse(TypedDict, total=False):
    Traces: list[_Trace]


class XRayClient(Protocol):
    """Minimal contract for the boto3 X-Ray client used here."""

    def get_trace_summaries(self, **kwargs: object) -> _GetTraceSummariesResponse:
        """Return trace summaries matching a filter within a time window."""

    def batch_get_traces(self, **kwargs: object) -> _BatchGetTracesResponse:
        """Return full trace documents for the given trace ids."""
mutants_xǁAWSXRayTraceAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAWSXRayTraceAdapterǁfetch_total_traces__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAWSXRayTraceAdapterǁ_slow_filter__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAWSXRayTraceAdapterǁ_batch_get_traces__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAWSXRayTraceAdapterǁ_call__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut: MutantDict = {}  # type: ignore


class AWSXRayTraceAdapter(TraceQueryPort):
    """TraceQueryPort backed by AWS X-Ray (the span store behind Application
    Signals). Fetches slow traces and their spans natively — no Tempo/Jaeger.
    """

    @_mutmut_mutated(mutants_xǁAWSXRayTraceAdapterǁ__init____mutmut)
    def __init__(self, region: str | None, xray_client: XRayClient | None = None) -> None:
        self._region = region
        self._xray_client = xray_client

    def xǁAWSXRayTraceAdapterǁ__init____mutmut_orig(self, region: str | None, xray_client: XRayClient | None = None) -> None:
        self._region = region
        self._xray_client = xray_client

    def xǁAWSXRayTraceAdapterǁ__init____mutmut_1(self, region: str | None, xray_client: XRayClient | None = None) -> None:
        self._region = None
        self._xray_client = xray_client

    def xǁAWSXRayTraceAdapterǁ__init____mutmut_2(self, region: str | None, xray_client: XRayClient | None = None) -> None:
        self._region = region
        self._xray_client = None

    @_mutmut_mutated(mutants_xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut)
    def fetch_slow_spans(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        summaries = self._all_trace_summaries(self._slow_filter(request), request)
        trace_ids = [summary["Id"] for summary in summaries if summary.get("Id")]
        if not trace_ids:
            return []
        return self._fetch_spans_for_traces(trace_ids)

    def xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_orig(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        summaries = self._all_trace_summaries(self._slow_filter(request), request)
        trace_ids = [summary["Id"] for summary in summaries if summary.get("Id")]
        if not trace_ids:
            return []
        return self._fetch_spans_for_traces(trace_ids)

    def xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_1(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        summaries = None
        trace_ids = [summary["Id"] for summary in summaries if summary.get("Id")]
        if not trace_ids:
            return []
        return self._fetch_spans_for_traces(trace_ids)

    def xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_2(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        summaries = self._all_trace_summaries(None, request)
        trace_ids = [summary["Id"] for summary in summaries if summary.get("Id")]
        if not trace_ids:
            return []
        return self._fetch_spans_for_traces(trace_ids)

    def xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_3(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        summaries = self._all_trace_summaries(self._slow_filter(request), None)
        trace_ids = [summary["Id"] for summary in summaries if summary.get("Id")]
        if not trace_ids:
            return []
        return self._fetch_spans_for_traces(trace_ids)

    def xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_4(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        summaries = self._all_trace_summaries(request)
        trace_ids = [summary["Id"] for summary in summaries if summary.get("Id")]
        if not trace_ids:
            return []
        return self._fetch_spans_for_traces(trace_ids)

    def xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_5(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        summaries = self._all_trace_summaries(self._slow_filter(request), )
        trace_ids = [summary["Id"] for summary in summaries if summary.get("Id")]
        if not trace_ids:
            return []
        return self._fetch_spans_for_traces(trace_ids)

    def xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_6(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        summaries = self._all_trace_summaries(self._slow_filter(None), request)
        trace_ids = [summary["Id"] for summary in summaries if summary.get("Id")]
        if not trace_ids:
            return []
        return self._fetch_spans_for_traces(trace_ids)

    def xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_7(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        summaries = self._all_trace_summaries(self._slow_filter(request), request)
        trace_ids = None
        if not trace_ids:
            return []
        return self._fetch_spans_for_traces(trace_ids)

    def xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_8(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        summaries = self._all_trace_summaries(self._slow_filter(request), request)
        trace_ids = [summary["XXIdXX"] for summary in summaries if summary.get("Id")]
        if not trace_ids:
            return []
        return self._fetch_spans_for_traces(trace_ids)

    def xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_9(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        summaries = self._all_trace_summaries(self._slow_filter(request), request)
        trace_ids = [summary["id"] for summary in summaries if summary.get("Id")]
        if not trace_ids:
            return []
        return self._fetch_spans_for_traces(trace_ids)

    def xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_10(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        summaries = self._all_trace_summaries(self._slow_filter(request), request)
        trace_ids = [summary["ID"] for summary in summaries if summary.get("Id")]
        if not trace_ids:
            return []
        return self._fetch_spans_for_traces(trace_ids)

    def xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_11(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        summaries = self._all_trace_summaries(self._slow_filter(request), request)
        trace_ids = [summary["Id"] for summary in summaries if summary.get(None)]
        if not trace_ids:
            return []
        return self._fetch_spans_for_traces(trace_ids)

    def xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_12(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        summaries = self._all_trace_summaries(self._slow_filter(request), request)
        trace_ids = [summary["Id"] for summary in summaries if summary.get("XXIdXX")]
        if not trace_ids:
            return []
        return self._fetch_spans_for_traces(trace_ids)

    def xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_13(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        summaries = self._all_trace_summaries(self._slow_filter(request), request)
        trace_ids = [summary["Id"] for summary in summaries if summary.get("id")]
        if not trace_ids:
            return []
        return self._fetch_spans_for_traces(trace_ids)

    def xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_14(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        summaries = self._all_trace_summaries(self._slow_filter(request), request)
        trace_ids = [summary["Id"] for summary in summaries if summary.get("ID")]
        if not trace_ids:
            return []
        return self._fetch_spans_for_traces(trace_ids)

    def xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_15(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        summaries = self._all_trace_summaries(self._slow_filter(request), request)
        trace_ids = [summary["Id"] for summary in summaries if summary.get("Id")]
        if trace_ids:
            return []
        return self._fetch_spans_for_traces(trace_ids)

    def xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_16(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        summaries = self._all_trace_summaries(self._slow_filter(request), request)
        trace_ids = [summary["Id"] for summary in summaries if summary.get("Id")]
        if not trace_ids:
            return []
        return self._fetch_spans_for_traces(None)

    @_mutmut_mutated(mutants_xǁAWSXRayTraceAdapterǁfetch_total_traces__mutmut)
    def fetch_total_traces(self, request: LatencyDiagnosticRequest) -> int:
        summaries = self._all_trace_summaries(self._total_filter(request), request)
        return len(summaries)

    def xǁAWSXRayTraceAdapterǁfetch_total_traces__mutmut_orig(self, request: LatencyDiagnosticRequest) -> int:
        summaries = self._all_trace_summaries(self._total_filter(request), request)
        return len(summaries)

    def xǁAWSXRayTraceAdapterǁfetch_total_traces__mutmut_1(self, request: LatencyDiagnosticRequest) -> int:
        summaries = None
        return len(summaries)

    def xǁAWSXRayTraceAdapterǁfetch_total_traces__mutmut_2(self, request: LatencyDiagnosticRequest) -> int:
        summaries = self._all_trace_summaries(None, request)
        return len(summaries)

    def xǁAWSXRayTraceAdapterǁfetch_total_traces__mutmut_3(self, request: LatencyDiagnosticRequest) -> int:
        summaries = self._all_trace_summaries(self._total_filter(request), None)
        return len(summaries)

    def xǁAWSXRayTraceAdapterǁfetch_total_traces__mutmut_4(self, request: LatencyDiagnosticRequest) -> int:
        summaries = self._all_trace_summaries(request)
        return len(summaries)

    def xǁAWSXRayTraceAdapterǁfetch_total_traces__mutmut_5(self, request: LatencyDiagnosticRequest) -> int:
        summaries = self._all_trace_summaries(self._total_filter(request), )
        return len(summaries)

    def xǁAWSXRayTraceAdapterǁfetch_total_traces__mutmut_6(self, request: LatencyDiagnosticRequest) -> int:
        summaries = self._all_trace_summaries(self._total_filter(None), request)
        return len(summaries)

    @_mutmut_mutated(mutants_xǁAWSXRayTraceAdapterǁ_slow_filter__mutmut)
    def _slow_filter(self, request: LatencyDiagnosticRequest) -> str:
        threshold_seconds = request.threshold_ms / _MILLIS_PER_SECOND
        return f'service("{request.service_name}") AND responsetime > {threshold_seconds}'

    def xǁAWSXRayTraceAdapterǁ_slow_filter__mutmut_orig(self, request: LatencyDiagnosticRequest) -> str:
        threshold_seconds = request.threshold_ms / _MILLIS_PER_SECOND
        return f'service("{request.service_name}") AND responsetime > {threshold_seconds}'

    def xǁAWSXRayTraceAdapterǁ_slow_filter__mutmut_1(self, request: LatencyDiagnosticRequest) -> str:
        threshold_seconds = None
        return f'service("{request.service_name}") AND responsetime > {threshold_seconds}'

    def xǁAWSXRayTraceAdapterǁ_slow_filter__mutmut_2(self, request: LatencyDiagnosticRequest) -> str:
        threshold_seconds = request.threshold_ms * _MILLIS_PER_SECOND
        return f'service("{request.service_name}") AND responsetime > {threshold_seconds}'

    def _total_filter(self, request: LatencyDiagnosticRequest) -> str:
        return f'service("{request.service_name}")'

    @_mutmut_mutated(mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut)
    def _all_trace_summaries(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = datetime.now(UTC)
        start = end - timedelta(minutes=request.time_window_minutes)
        summaries: list[_TraceSummary] = []
        page_cursor: str | None = None
        while True:
            response = self._get_trace_summaries(filter_expression, start, end, page_cursor)
            summaries.extend(response.get("TraceSummaries", []))
            page_cursor = response.get("NextToken")
            if not page_cursor:
                break
        return summaries

    def xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_orig(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = datetime.now(UTC)
        start = end - timedelta(minutes=request.time_window_minutes)
        summaries: list[_TraceSummary] = []
        page_cursor: str | None = None
        while True:
            response = self._get_trace_summaries(filter_expression, start, end, page_cursor)
            summaries.extend(response.get("TraceSummaries", []))
            page_cursor = response.get("NextToken")
            if not page_cursor:
                break
        return summaries

    def xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_1(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = None
        start = end - timedelta(minutes=request.time_window_minutes)
        summaries: list[_TraceSummary] = []
        page_cursor: str | None = None
        while True:
            response = self._get_trace_summaries(filter_expression, start, end, page_cursor)
            summaries.extend(response.get("TraceSummaries", []))
            page_cursor = response.get("NextToken")
            if not page_cursor:
                break
        return summaries

    def xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_2(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = datetime.now(None)
        start = end - timedelta(minutes=request.time_window_minutes)
        summaries: list[_TraceSummary] = []
        page_cursor: str | None = None
        while True:
            response = self._get_trace_summaries(filter_expression, start, end, page_cursor)
            summaries.extend(response.get("TraceSummaries", []))
            page_cursor = response.get("NextToken")
            if not page_cursor:
                break
        return summaries

    def xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_3(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = datetime.now(UTC)
        start = None
        summaries: list[_TraceSummary] = []
        page_cursor: str | None = None
        while True:
            response = self._get_trace_summaries(filter_expression, start, end, page_cursor)
            summaries.extend(response.get("TraceSummaries", []))
            page_cursor = response.get("NextToken")
            if not page_cursor:
                break
        return summaries

    def xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_4(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = datetime.now(UTC)
        start = end + timedelta(minutes=request.time_window_minutes)
        summaries: list[_TraceSummary] = []
        page_cursor: str | None = None
        while True:
            response = self._get_trace_summaries(filter_expression, start, end, page_cursor)
            summaries.extend(response.get("TraceSummaries", []))
            page_cursor = response.get("NextToken")
            if not page_cursor:
                break
        return summaries

    def xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_5(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = datetime.now(UTC)
        start = end - timedelta(minutes=None)
        summaries: list[_TraceSummary] = []
        page_cursor: str | None = None
        while True:
            response = self._get_trace_summaries(filter_expression, start, end, page_cursor)
            summaries.extend(response.get("TraceSummaries", []))
            page_cursor = response.get("NextToken")
            if not page_cursor:
                break
        return summaries

    def xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_6(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = datetime.now(UTC)
        start = end - timedelta(minutes=request.time_window_minutes)
        summaries: list[_TraceSummary] = None
        page_cursor: str | None = None
        while True:
            response = self._get_trace_summaries(filter_expression, start, end, page_cursor)
            summaries.extend(response.get("TraceSummaries", []))
            page_cursor = response.get("NextToken")
            if not page_cursor:
                break
        return summaries

    def xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_7(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = datetime.now(UTC)
        start = end - timedelta(minutes=request.time_window_minutes)
        summaries: list[_TraceSummary] = []
        page_cursor: str | None = ""
        while True:
            response = self._get_trace_summaries(filter_expression, start, end, page_cursor)
            summaries.extend(response.get("TraceSummaries", []))
            page_cursor = response.get("NextToken")
            if not page_cursor:
                break
        return summaries

    def xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_8(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = datetime.now(UTC)
        start = end - timedelta(minutes=request.time_window_minutes)
        summaries: list[_TraceSummary] = []
        page_cursor: str | None = None
        while False:
            response = self._get_trace_summaries(filter_expression, start, end, page_cursor)
            summaries.extend(response.get("TraceSummaries", []))
            page_cursor = response.get("NextToken")
            if not page_cursor:
                break
        return summaries

    def xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_9(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = datetime.now(UTC)
        start = end - timedelta(minutes=request.time_window_minutes)
        summaries: list[_TraceSummary] = []
        page_cursor: str | None = None
        while True:
            response = None
            summaries.extend(response.get("TraceSummaries", []))
            page_cursor = response.get("NextToken")
            if not page_cursor:
                break
        return summaries

    def xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_10(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = datetime.now(UTC)
        start = end - timedelta(minutes=request.time_window_minutes)
        summaries: list[_TraceSummary] = []
        page_cursor: str | None = None
        while True:
            response = self._get_trace_summaries(None, start, end, page_cursor)
            summaries.extend(response.get("TraceSummaries", []))
            page_cursor = response.get("NextToken")
            if not page_cursor:
                break
        return summaries

    def xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_11(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = datetime.now(UTC)
        start = end - timedelta(minutes=request.time_window_minutes)
        summaries: list[_TraceSummary] = []
        page_cursor: str | None = None
        while True:
            response = self._get_trace_summaries(filter_expression, None, end, page_cursor)
            summaries.extend(response.get("TraceSummaries", []))
            page_cursor = response.get("NextToken")
            if not page_cursor:
                break
        return summaries

    def xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_12(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = datetime.now(UTC)
        start = end - timedelta(minutes=request.time_window_minutes)
        summaries: list[_TraceSummary] = []
        page_cursor: str | None = None
        while True:
            response = self._get_trace_summaries(filter_expression, start, None, page_cursor)
            summaries.extend(response.get("TraceSummaries", []))
            page_cursor = response.get("NextToken")
            if not page_cursor:
                break
        return summaries

    def xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_13(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = datetime.now(UTC)
        start = end - timedelta(minutes=request.time_window_minutes)
        summaries: list[_TraceSummary] = []
        page_cursor: str | None = None
        while True:
            response = self._get_trace_summaries(filter_expression, start, end, None)
            summaries.extend(response.get("TraceSummaries", []))
            page_cursor = response.get("NextToken")
            if not page_cursor:
                break
        return summaries

    def xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_14(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = datetime.now(UTC)
        start = end - timedelta(minutes=request.time_window_minutes)
        summaries: list[_TraceSummary] = []
        page_cursor: str | None = None
        while True:
            response = self._get_trace_summaries(start, end, page_cursor)
            summaries.extend(response.get("TraceSummaries", []))
            page_cursor = response.get("NextToken")
            if not page_cursor:
                break
        return summaries

    def xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_15(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = datetime.now(UTC)
        start = end - timedelta(minutes=request.time_window_minutes)
        summaries: list[_TraceSummary] = []
        page_cursor: str | None = None
        while True:
            response = self._get_trace_summaries(filter_expression, end, page_cursor)
            summaries.extend(response.get("TraceSummaries", []))
            page_cursor = response.get("NextToken")
            if not page_cursor:
                break
        return summaries

    def xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_16(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = datetime.now(UTC)
        start = end - timedelta(minutes=request.time_window_minutes)
        summaries: list[_TraceSummary] = []
        page_cursor: str | None = None
        while True:
            response = self._get_trace_summaries(filter_expression, start, page_cursor)
            summaries.extend(response.get("TraceSummaries", []))
            page_cursor = response.get("NextToken")
            if not page_cursor:
                break
        return summaries

    def xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_17(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = datetime.now(UTC)
        start = end - timedelta(minutes=request.time_window_minutes)
        summaries: list[_TraceSummary] = []
        page_cursor: str | None = None
        while True:
            response = self._get_trace_summaries(filter_expression, start, end, )
            summaries.extend(response.get("TraceSummaries", []))
            page_cursor = response.get("NextToken")
            if not page_cursor:
                break
        return summaries

    def xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_18(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = datetime.now(UTC)
        start = end - timedelta(minutes=request.time_window_minutes)
        summaries: list[_TraceSummary] = []
        page_cursor: str | None = None
        while True:
            response = self._get_trace_summaries(filter_expression, start, end, page_cursor)
            summaries.extend(None)
            page_cursor = response.get("NextToken")
            if not page_cursor:
                break
        return summaries

    def xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_19(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = datetime.now(UTC)
        start = end - timedelta(minutes=request.time_window_minutes)
        summaries: list[_TraceSummary] = []
        page_cursor: str | None = None
        while True:
            response = self._get_trace_summaries(filter_expression, start, end, page_cursor)
            summaries.extend(response.get(None, []))
            page_cursor = response.get("NextToken")
            if not page_cursor:
                break
        return summaries

    def xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_20(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = datetime.now(UTC)
        start = end - timedelta(minutes=request.time_window_minutes)
        summaries: list[_TraceSummary] = []
        page_cursor: str | None = None
        while True:
            response = self._get_trace_summaries(filter_expression, start, end, page_cursor)
            summaries.extend(response.get("TraceSummaries", None))
            page_cursor = response.get("NextToken")
            if not page_cursor:
                break
        return summaries

    def xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_21(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = datetime.now(UTC)
        start = end - timedelta(minutes=request.time_window_minutes)
        summaries: list[_TraceSummary] = []
        page_cursor: str | None = None
        while True:
            response = self._get_trace_summaries(filter_expression, start, end, page_cursor)
            summaries.extend(response.get([]))
            page_cursor = response.get("NextToken")
            if not page_cursor:
                break
        return summaries

    def xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_22(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = datetime.now(UTC)
        start = end - timedelta(minutes=request.time_window_minutes)
        summaries: list[_TraceSummary] = []
        page_cursor: str | None = None
        while True:
            response = self._get_trace_summaries(filter_expression, start, end, page_cursor)
            summaries.extend(response.get("TraceSummaries", ))
            page_cursor = response.get("NextToken")
            if not page_cursor:
                break
        return summaries

    def xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_23(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = datetime.now(UTC)
        start = end - timedelta(minutes=request.time_window_minutes)
        summaries: list[_TraceSummary] = []
        page_cursor: str | None = None
        while True:
            response = self._get_trace_summaries(filter_expression, start, end, page_cursor)
            summaries.extend(response.get("XXTraceSummariesXX", []))
            page_cursor = response.get("NextToken")
            if not page_cursor:
                break
        return summaries

    def xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_24(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = datetime.now(UTC)
        start = end - timedelta(minutes=request.time_window_minutes)
        summaries: list[_TraceSummary] = []
        page_cursor: str | None = None
        while True:
            response = self._get_trace_summaries(filter_expression, start, end, page_cursor)
            summaries.extend(response.get("tracesummaries", []))
            page_cursor = response.get("NextToken")
            if not page_cursor:
                break
        return summaries

    def xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_25(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = datetime.now(UTC)
        start = end - timedelta(minutes=request.time_window_minutes)
        summaries: list[_TraceSummary] = []
        page_cursor: str | None = None
        while True:
            response = self._get_trace_summaries(filter_expression, start, end, page_cursor)
            summaries.extend(response.get("TRACESUMMARIES", []))
            page_cursor = response.get("NextToken")
            if not page_cursor:
                break
        return summaries

    def xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_26(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = datetime.now(UTC)
        start = end - timedelta(minutes=request.time_window_minutes)
        summaries: list[_TraceSummary] = []
        page_cursor: str | None = None
        while True:
            response = self._get_trace_summaries(filter_expression, start, end, page_cursor)
            summaries.extend(response.get("TraceSummaries", []))
            page_cursor = None
            if not page_cursor:
                break
        return summaries

    def xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_27(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = datetime.now(UTC)
        start = end - timedelta(minutes=request.time_window_minutes)
        summaries: list[_TraceSummary] = []
        page_cursor: str | None = None
        while True:
            response = self._get_trace_summaries(filter_expression, start, end, page_cursor)
            summaries.extend(response.get("TraceSummaries", []))
            page_cursor = response.get(None)
            if not page_cursor:
                break
        return summaries

    def xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_28(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = datetime.now(UTC)
        start = end - timedelta(minutes=request.time_window_minutes)
        summaries: list[_TraceSummary] = []
        page_cursor: str | None = None
        while True:
            response = self._get_trace_summaries(filter_expression, start, end, page_cursor)
            summaries.extend(response.get("TraceSummaries", []))
            page_cursor = response.get("XXNextTokenXX")
            if not page_cursor:
                break
        return summaries

    def xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_29(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = datetime.now(UTC)
        start = end - timedelta(minutes=request.time_window_minutes)
        summaries: list[_TraceSummary] = []
        page_cursor: str | None = None
        while True:
            response = self._get_trace_summaries(filter_expression, start, end, page_cursor)
            summaries.extend(response.get("TraceSummaries", []))
            page_cursor = response.get("nexttoken")
            if not page_cursor:
                break
        return summaries

    def xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_30(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = datetime.now(UTC)
        start = end - timedelta(minutes=request.time_window_minutes)
        summaries: list[_TraceSummary] = []
        page_cursor: str | None = None
        while True:
            response = self._get_trace_summaries(filter_expression, start, end, page_cursor)
            summaries.extend(response.get("TraceSummaries", []))
            page_cursor = response.get("NEXTTOKEN")
            if not page_cursor:
                break
        return summaries

    def xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_31(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = datetime.now(UTC)
        start = end - timedelta(minutes=request.time_window_minutes)
        summaries: list[_TraceSummary] = []
        page_cursor: str | None = None
        while True:
            response = self._get_trace_summaries(filter_expression, start, end, page_cursor)
            summaries.extend(response.get("TraceSummaries", []))
            page_cursor = response.get("NextToken")
            if page_cursor:
                break
        return summaries

    def xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_32(
        self, filter_expression: str, request: LatencyDiagnosticRequest
    ) -> list[_TraceSummary]:
        end = datetime.now(UTC)
        start = end - timedelta(minutes=request.time_window_minutes)
        summaries: list[_TraceSummary] = []
        page_cursor: str | None = None
        while True:
            response = self._get_trace_summaries(filter_expression, start, end, page_cursor)
            summaries.extend(response.get("TraceSummaries", []))
            page_cursor = response.get("NextToken")
            if not page_cursor:
                return
        return summaries

    @_mutmut_mutated(mutants_xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut)
    def _fetch_spans_for_traces(self, trace_ids: list[str]) -> list[list[TraceSpan]]:
        traces_spans: list[list[TraceSpan]] = []
        for batch in _chunked(trace_ids, _MAX_TRACE_IDS_PER_BATCH):
            response = self._batch_get_traces(batch)
            for trace in response.get("Traces", []):
                traces_spans.append(_trace_to_spans(trace))
        return traces_spans

    def xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_orig(self, trace_ids: list[str]) -> list[list[TraceSpan]]:
        traces_spans: list[list[TraceSpan]] = []
        for batch in _chunked(trace_ids, _MAX_TRACE_IDS_PER_BATCH):
            response = self._batch_get_traces(batch)
            for trace in response.get("Traces", []):
                traces_spans.append(_trace_to_spans(trace))
        return traces_spans

    def xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_1(self, trace_ids: list[str]) -> list[list[TraceSpan]]:
        traces_spans: list[list[TraceSpan]] = None
        for batch in _chunked(trace_ids, _MAX_TRACE_IDS_PER_BATCH):
            response = self._batch_get_traces(batch)
            for trace in response.get("Traces", []):
                traces_spans.append(_trace_to_spans(trace))
        return traces_spans

    def xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_2(self, trace_ids: list[str]) -> list[list[TraceSpan]]:
        traces_spans: list[list[TraceSpan]] = []
        for batch in _chunked(None, _MAX_TRACE_IDS_PER_BATCH):
            response = self._batch_get_traces(batch)
            for trace in response.get("Traces", []):
                traces_spans.append(_trace_to_spans(trace))
        return traces_spans

    def xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_3(self, trace_ids: list[str]) -> list[list[TraceSpan]]:
        traces_spans: list[list[TraceSpan]] = []
        for batch in _chunked(trace_ids, None):
            response = self._batch_get_traces(batch)
            for trace in response.get("Traces", []):
                traces_spans.append(_trace_to_spans(trace))
        return traces_spans

    def xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_4(self, trace_ids: list[str]) -> list[list[TraceSpan]]:
        traces_spans: list[list[TraceSpan]] = []
        for batch in _chunked(_MAX_TRACE_IDS_PER_BATCH):
            response = self._batch_get_traces(batch)
            for trace in response.get("Traces", []):
                traces_spans.append(_trace_to_spans(trace))
        return traces_spans

    def xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_5(self, trace_ids: list[str]) -> list[list[TraceSpan]]:
        traces_spans: list[list[TraceSpan]] = []
        for batch in _chunked(trace_ids, ):
            response = self._batch_get_traces(batch)
            for trace in response.get("Traces", []):
                traces_spans.append(_trace_to_spans(trace))
        return traces_spans

    def xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_6(self, trace_ids: list[str]) -> list[list[TraceSpan]]:
        traces_spans: list[list[TraceSpan]] = []
        for batch in _chunked(trace_ids, _MAX_TRACE_IDS_PER_BATCH):
            response = None
            for trace in response.get("Traces", []):
                traces_spans.append(_trace_to_spans(trace))
        return traces_spans

    def xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_7(self, trace_ids: list[str]) -> list[list[TraceSpan]]:
        traces_spans: list[list[TraceSpan]] = []
        for batch in _chunked(trace_ids, _MAX_TRACE_IDS_PER_BATCH):
            response = self._batch_get_traces(None)
            for trace in response.get("Traces", []):
                traces_spans.append(_trace_to_spans(trace))
        return traces_spans

    def xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_8(self, trace_ids: list[str]) -> list[list[TraceSpan]]:
        traces_spans: list[list[TraceSpan]] = []
        for batch in _chunked(trace_ids, _MAX_TRACE_IDS_PER_BATCH):
            response = self._batch_get_traces(batch)
            for trace in response.get(None, []):
                traces_spans.append(_trace_to_spans(trace))
        return traces_spans

    def xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_9(self, trace_ids: list[str]) -> list[list[TraceSpan]]:
        traces_spans: list[list[TraceSpan]] = []
        for batch in _chunked(trace_ids, _MAX_TRACE_IDS_PER_BATCH):
            response = self._batch_get_traces(batch)
            for trace in response.get("Traces", None):
                traces_spans.append(_trace_to_spans(trace))
        return traces_spans

    def xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_10(self, trace_ids: list[str]) -> list[list[TraceSpan]]:
        traces_spans: list[list[TraceSpan]] = []
        for batch in _chunked(trace_ids, _MAX_TRACE_IDS_PER_BATCH):
            response = self._batch_get_traces(batch)
            for trace in response.get([]):
                traces_spans.append(_trace_to_spans(trace))
        return traces_spans

    def xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_11(self, trace_ids: list[str]) -> list[list[TraceSpan]]:
        traces_spans: list[list[TraceSpan]] = []
        for batch in _chunked(trace_ids, _MAX_TRACE_IDS_PER_BATCH):
            response = self._batch_get_traces(batch)
            for trace in response.get("Traces", ):
                traces_spans.append(_trace_to_spans(trace))
        return traces_spans

    def xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_12(self, trace_ids: list[str]) -> list[list[TraceSpan]]:
        traces_spans: list[list[TraceSpan]] = []
        for batch in _chunked(trace_ids, _MAX_TRACE_IDS_PER_BATCH):
            response = self._batch_get_traces(batch)
            for trace in response.get("XXTracesXX", []):
                traces_spans.append(_trace_to_spans(trace))
        return traces_spans

    def xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_13(self, trace_ids: list[str]) -> list[list[TraceSpan]]:
        traces_spans: list[list[TraceSpan]] = []
        for batch in _chunked(trace_ids, _MAX_TRACE_IDS_PER_BATCH):
            response = self._batch_get_traces(batch)
            for trace in response.get("traces", []):
                traces_spans.append(_trace_to_spans(trace))
        return traces_spans

    def xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_14(self, trace_ids: list[str]) -> list[list[TraceSpan]]:
        traces_spans: list[list[TraceSpan]] = []
        for batch in _chunked(trace_ids, _MAX_TRACE_IDS_PER_BATCH):
            response = self._batch_get_traces(batch)
            for trace in response.get("TRACES", []):
                traces_spans.append(_trace_to_spans(trace))
        return traces_spans

    def xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_15(self, trace_ids: list[str]) -> list[list[TraceSpan]]:
        traces_spans: list[list[TraceSpan]] = []
        for batch in _chunked(trace_ids, _MAX_TRACE_IDS_PER_BATCH):
            response = self._batch_get_traces(batch)
            for trace in response.get("Traces", []):
                traces_spans.append(None)
        return traces_spans

    def xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_16(self, trace_ids: list[str]) -> list[list[TraceSpan]]:
        traces_spans: list[list[TraceSpan]] = []
        for batch in _chunked(trace_ids, _MAX_TRACE_IDS_PER_BATCH):
            response = self._batch_get_traces(batch)
            for trace in response.get("Traces", []):
                traces_spans.append(_trace_to_spans(None))
        return traces_spans

    @_mutmut_mutated(mutants_xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut)
    def _get_trace_summaries(
        self, filter_expression: str, start: datetime, end: datetime, page_cursor: str | None
    ) -> _GetTraceSummariesResponse:
        request: dict[str, object] = {
            "StartTime": start,
            "EndTime": end,
            "FilterExpression": filter_expression,
        }
        if page_cursor:
            request["NextToken"] = page_cursor
        return self._call(lambda: self._client_or_create().get_trace_summaries(**request))

    def xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_orig(
        self, filter_expression: str, start: datetime, end: datetime, page_cursor: str | None
    ) -> _GetTraceSummariesResponse:
        request: dict[str, object] = {
            "StartTime": start,
            "EndTime": end,
            "FilterExpression": filter_expression,
        }
        if page_cursor:
            request["NextToken"] = page_cursor
        return self._call(lambda: self._client_or_create().get_trace_summaries(**request))

    def xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_1(
        self, filter_expression: str, start: datetime, end: datetime, page_cursor: str | None
    ) -> _GetTraceSummariesResponse:
        request: dict[str, object] = None
        if page_cursor:
            request["NextToken"] = page_cursor
        return self._call(lambda: self._client_or_create().get_trace_summaries(**request))

    def xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_2(
        self, filter_expression: str, start: datetime, end: datetime, page_cursor: str | None
    ) -> _GetTraceSummariesResponse:
        request: dict[str, object] = {
            "XXStartTimeXX": start,
            "EndTime": end,
            "FilterExpression": filter_expression,
        }
        if page_cursor:
            request["NextToken"] = page_cursor
        return self._call(lambda: self._client_or_create().get_trace_summaries(**request))

    def xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_3(
        self, filter_expression: str, start: datetime, end: datetime, page_cursor: str | None
    ) -> _GetTraceSummariesResponse:
        request: dict[str, object] = {
            "starttime": start,
            "EndTime": end,
            "FilterExpression": filter_expression,
        }
        if page_cursor:
            request["NextToken"] = page_cursor
        return self._call(lambda: self._client_or_create().get_trace_summaries(**request))

    def xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_4(
        self, filter_expression: str, start: datetime, end: datetime, page_cursor: str | None
    ) -> _GetTraceSummariesResponse:
        request: dict[str, object] = {
            "STARTTIME": start,
            "EndTime": end,
            "FilterExpression": filter_expression,
        }
        if page_cursor:
            request["NextToken"] = page_cursor
        return self._call(lambda: self._client_or_create().get_trace_summaries(**request))

    def xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_5(
        self, filter_expression: str, start: datetime, end: datetime, page_cursor: str | None
    ) -> _GetTraceSummariesResponse:
        request: dict[str, object] = {
            "StartTime": start,
            "XXEndTimeXX": end,
            "FilterExpression": filter_expression,
        }
        if page_cursor:
            request["NextToken"] = page_cursor
        return self._call(lambda: self._client_or_create().get_trace_summaries(**request))

    def xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_6(
        self, filter_expression: str, start: datetime, end: datetime, page_cursor: str | None
    ) -> _GetTraceSummariesResponse:
        request: dict[str, object] = {
            "StartTime": start,
            "endtime": end,
            "FilterExpression": filter_expression,
        }
        if page_cursor:
            request["NextToken"] = page_cursor
        return self._call(lambda: self._client_or_create().get_trace_summaries(**request))

    def xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_7(
        self, filter_expression: str, start: datetime, end: datetime, page_cursor: str | None
    ) -> _GetTraceSummariesResponse:
        request: dict[str, object] = {
            "StartTime": start,
            "ENDTIME": end,
            "FilterExpression": filter_expression,
        }
        if page_cursor:
            request["NextToken"] = page_cursor
        return self._call(lambda: self._client_or_create().get_trace_summaries(**request))

    def xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_8(
        self, filter_expression: str, start: datetime, end: datetime, page_cursor: str | None
    ) -> _GetTraceSummariesResponse:
        request: dict[str, object] = {
            "StartTime": start,
            "EndTime": end,
            "XXFilterExpressionXX": filter_expression,
        }
        if page_cursor:
            request["NextToken"] = page_cursor
        return self._call(lambda: self._client_or_create().get_trace_summaries(**request))

    def xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_9(
        self, filter_expression: str, start: datetime, end: datetime, page_cursor: str | None
    ) -> _GetTraceSummariesResponse:
        request: dict[str, object] = {
            "StartTime": start,
            "EndTime": end,
            "filterexpression": filter_expression,
        }
        if page_cursor:
            request["NextToken"] = page_cursor
        return self._call(lambda: self._client_or_create().get_trace_summaries(**request))

    def xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_10(
        self, filter_expression: str, start: datetime, end: datetime, page_cursor: str | None
    ) -> _GetTraceSummariesResponse:
        request: dict[str, object] = {
            "StartTime": start,
            "EndTime": end,
            "FILTEREXPRESSION": filter_expression,
        }
        if page_cursor:
            request["NextToken"] = page_cursor
        return self._call(lambda: self._client_or_create().get_trace_summaries(**request))

    def xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_11(
        self, filter_expression: str, start: datetime, end: datetime, page_cursor: str | None
    ) -> _GetTraceSummariesResponse:
        request: dict[str, object] = {
            "StartTime": start,
            "EndTime": end,
            "FilterExpression": filter_expression,
        }
        if page_cursor:
            request["NextToken"] = None
        return self._call(lambda: self._client_or_create().get_trace_summaries(**request))

    def xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_12(
        self, filter_expression: str, start: datetime, end: datetime, page_cursor: str | None
    ) -> _GetTraceSummariesResponse:
        request: dict[str, object] = {
            "StartTime": start,
            "EndTime": end,
            "FilterExpression": filter_expression,
        }
        if page_cursor:
            request["XXNextTokenXX"] = page_cursor
        return self._call(lambda: self._client_or_create().get_trace_summaries(**request))

    def xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_13(
        self, filter_expression: str, start: datetime, end: datetime, page_cursor: str | None
    ) -> _GetTraceSummariesResponse:
        request: dict[str, object] = {
            "StartTime": start,
            "EndTime": end,
            "FilterExpression": filter_expression,
        }
        if page_cursor:
            request["nexttoken"] = page_cursor
        return self._call(lambda: self._client_or_create().get_trace_summaries(**request))

    def xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_14(
        self, filter_expression: str, start: datetime, end: datetime, page_cursor: str | None
    ) -> _GetTraceSummariesResponse:
        request: dict[str, object] = {
            "StartTime": start,
            "EndTime": end,
            "FilterExpression": filter_expression,
        }
        if page_cursor:
            request["NEXTTOKEN"] = page_cursor
        return self._call(lambda: self._client_or_create().get_trace_summaries(**request))

    def xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_15(
        self, filter_expression: str, start: datetime, end: datetime, page_cursor: str | None
    ) -> _GetTraceSummariesResponse:
        request: dict[str, object] = {
            "StartTime": start,
            "EndTime": end,
            "FilterExpression": filter_expression,
        }
        if page_cursor:
            request["NextToken"] = page_cursor
        return self._call(None)

    def xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_16(
        self, filter_expression: str, start: datetime, end: datetime, page_cursor: str | None
    ) -> _GetTraceSummariesResponse:
        request: dict[str, object] = {
            "StartTime": start,
            "EndTime": end,
            "FilterExpression": filter_expression,
        }
        if page_cursor:
            request["NextToken"] = page_cursor
        return self._call(lambda: None)

    @_mutmut_mutated(mutants_xǁAWSXRayTraceAdapterǁ_batch_get_traces__mutmut)
    def _batch_get_traces(self, trace_ids: list[str]) -> _BatchGetTracesResponse:
        return self._call(lambda: self._client_or_create().batch_get_traces(TraceIds=trace_ids))

    def xǁAWSXRayTraceAdapterǁ_batch_get_traces__mutmut_orig(self, trace_ids: list[str]) -> _BatchGetTracesResponse:
        return self._call(lambda: self._client_or_create().batch_get_traces(TraceIds=trace_ids))

    def xǁAWSXRayTraceAdapterǁ_batch_get_traces__mutmut_1(self, trace_ids: list[str]) -> _BatchGetTracesResponse:
        return self._call(None)

    def xǁAWSXRayTraceAdapterǁ_batch_get_traces__mutmut_2(self, trace_ids: list[str]) -> _BatchGetTracesResponse:
        return self._call(lambda: None)

    def xǁAWSXRayTraceAdapterǁ_batch_get_traces__mutmut_3(self, trace_ids: list[str]) -> _BatchGetTracesResponse:
        return self._call(lambda: self._client_or_create().batch_get_traces(TraceIds=None))

    @_mutmut_mutated(mutants_xǁAWSXRayTraceAdapterǁ_call__mutmut)
    def _call(self, operation: Callable[[], _ResponseT]) -> _ResponseT:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        try:
            return operation()
        except NoCredentialsError as exc:
            raise TracesUnavailableError(
                f"AWS credentials not found. {_CREDENTIALS_HINT}",
                context={"region": self._region or "unknown"},
            ) from exc
        except (ClientError, BotoCoreError) as exc:
            raise TracesUnavailableError(
                "Unable to query AWS X-Ray traces.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc

    def xǁAWSXRayTraceAdapterǁ_call__mutmut_orig(self, operation: Callable[[], _ResponseT]) -> _ResponseT:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        try:
            return operation()
        except NoCredentialsError as exc:
            raise TracesUnavailableError(
                f"AWS credentials not found. {_CREDENTIALS_HINT}",
                context={"region": self._region or "unknown"},
            ) from exc
        except (ClientError, BotoCoreError) as exc:
            raise TracesUnavailableError(
                "Unable to query AWS X-Ray traces.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc

    def xǁAWSXRayTraceAdapterǁ_call__mutmut_1(self, operation: Callable[[], _ResponseT]) -> _ResponseT:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        try:
            return operation()
        except NoCredentialsError as exc:
            raise TracesUnavailableError(
                None,
                context={"region": self._region or "unknown"},
            ) from exc
        except (ClientError, BotoCoreError) as exc:
            raise TracesUnavailableError(
                "Unable to query AWS X-Ray traces.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc

    def xǁAWSXRayTraceAdapterǁ_call__mutmut_2(self, operation: Callable[[], _ResponseT]) -> _ResponseT:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        try:
            return operation()
        except NoCredentialsError as exc:
            raise TracesUnavailableError(
                f"AWS credentials not found. {_CREDENTIALS_HINT}",
                context=None,
            ) from exc
        except (ClientError, BotoCoreError) as exc:
            raise TracesUnavailableError(
                "Unable to query AWS X-Ray traces.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc

    def xǁAWSXRayTraceAdapterǁ_call__mutmut_3(self, operation: Callable[[], _ResponseT]) -> _ResponseT:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        try:
            return operation()
        except NoCredentialsError as exc:
            raise TracesUnavailableError(
                context={"region": self._region or "unknown"},
            ) from exc
        except (ClientError, BotoCoreError) as exc:
            raise TracesUnavailableError(
                "Unable to query AWS X-Ray traces.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc

    def xǁAWSXRayTraceAdapterǁ_call__mutmut_4(self, operation: Callable[[], _ResponseT]) -> _ResponseT:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        try:
            return operation()
        except NoCredentialsError as exc:
            raise TracesUnavailableError(
                f"AWS credentials not found. {_CREDENTIALS_HINT}",
                ) from exc
        except (ClientError, BotoCoreError) as exc:
            raise TracesUnavailableError(
                "Unable to query AWS X-Ray traces.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc

    def xǁAWSXRayTraceAdapterǁ_call__mutmut_5(self, operation: Callable[[], _ResponseT]) -> _ResponseT:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        try:
            return operation()
        except NoCredentialsError as exc:
            raise TracesUnavailableError(
                f"AWS credentials not found. {_CREDENTIALS_HINT}",
                context={"XXregionXX": self._region or "unknown"},
            ) from exc
        except (ClientError, BotoCoreError) as exc:
            raise TracesUnavailableError(
                "Unable to query AWS X-Ray traces.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc

    def xǁAWSXRayTraceAdapterǁ_call__mutmut_6(self, operation: Callable[[], _ResponseT]) -> _ResponseT:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        try:
            return operation()
        except NoCredentialsError as exc:
            raise TracesUnavailableError(
                f"AWS credentials not found. {_CREDENTIALS_HINT}",
                context={"REGION": self._region or "unknown"},
            ) from exc
        except (ClientError, BotoCoreError) as exc:
            raise TracesUnavailableError(
                "Unable to query AWS X-Ray traces.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc

    def xǁAWSXRayTraceAdapterǁ_call__mutmut_7(self, operation: Callable[[], _ResponseT]) -> _ResponseT:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        try:
            return operation()
        except NoCredentialsError as exc:
            raise TracesUnavailableError(
                f"AWS credentials not found. {_CREDENTIALS_HINT}",
                context={"region": self._region and "unknown"},
            ) from exc
        except (ClientError, BotoCoreError) as exc:
            raise TracesUnavailableError(
                "Unable to query AWS X-Ray traces.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc

    def xǁAWSXRayTraceAdapterǁ_call__mutmut_8(self, operation: Callable[[], _ResponseT]) -> _ResponseT:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        try:
            return operation()
        except NoCredentialsError as exc:
            raise TracesUnavailableError(
                f"AWS credentials not found. {_CREDENTIALS_HINT}",
                context={"region": self._region or "XXunknownXX"},
            ) from exc
        except (ClientError, BotoCoreError) as exc:
            raise TracesUnavailableError(
                "Unable to query AWS X-Ray traces.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc

    def xǁAWSXRayTraceAdapterǁ_call__mutmut_9(self, operation: Callable[[], _ResponseT]) -> _ResponseT:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        try:
            return operation()
        except NoCredentialsError as exc:
            raise TracesUnavailableError(
                f"AWS credentials not found. {_CREDENTIALS_HINT}",
                context={"region": self._region or "UNKNOWN"},
            ) from exc
        except (ClientError, BotoCoreError) as exc:
            raise TracesUnavailableError(
                "Unable to query AWS X-Ray traces.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc

    def xǁAWSXRayTraceAdapterǁ_call__mutmut_10(self, operation: Callable[[], _ResponseT]) -> _ResponseT:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        try:
            return operation()
        except NoCredentialsError as exc:
            raise TracesUnavailableError(
                f"AWS credentials not found. {_CREDENTIALS_HINT}",
                context={"region": self._region or "unknown"},
            ) from exc
        except (ClientError, BotoCoreError) as exc:
            raise TracesUnavailableError(
                None,
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc

    def xǁAWSXRayTraceAdapterǁ_call__mutmut_11(self, operation: Callable[[], _ResponseT]) -> _ResponseT:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        try:
            return operation()
        except NoCredentialsError as exc:
            raise TracesUnavailableError(
                f"AWS credentials not found. {_CREDENTIALS_HINT}",
                context={"region": self._region or "unknown"},
            ) from exc
        except (ClientError, BotoCoreError) as exc:
            raise TracesUnavailableError(
                "Unable to query AWS X-Ray traces.",
                context=None,
            ) from exc

    def xǁAWSXRayTraceAdapterǁ_call__mutmut_12(self, operation: Callable[[], _ResponseT]) -> _ResponseT:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        try:
            return operation()
        except NoCredentialsError as exc:
            raise TracesUnavailableError(
                f"AWS credentials not found. {_CREDENTIALS_HINT}",
                context={"region": self._region or "unknown"},
            ) from exc
        except (ClientError, BotoCoreError) as exc:
            raise TracesUnavailableError(
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc

    def xǁAWSXRayTraceAdapterǁ_call__mutmut_13(self, operation: Callable[[], _ResponseT]) -> _ResponseT:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        try:
            return operation()
        except NoCredentialsError as exc:
            raise TracesUnavailableError(
                f"AWS credentials not found. {_CREDENTIALS_HINT}",
                context={"region": self._region or "unknown"},
            ) from exc
        except (ClientError, BotoCoreError) as exc:
            raise TracesUnavailableError(
                "Unable to query AWS X-Ray traces.",
                ) from exc

    def xǁAWSXRayTraceAdapterǁ_call__mutmut_14(self, operation: Callable[[], _ResponseT]) -> _ResponseT:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        try:
            return operation()
        except NoCredentialsError as exc:
            raise TracesUnavailableError(
                f"AWS credentials not found. {_CREDENTIALS_HINT}",
                context={"region": self._region or "unknown"},
            ) from exc
        except (ClientError, BotoCoreError) as exc:
            raise TracesUnavailableError(
                "XXUnable to query AWS X-Ray traces.XX",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc

    def xǁAWSXRayTraceAdapterǁ_call__mutmut_15(self, operation: Callable[[], _ResponseT]) -> _ResponseT:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        try:
            return operation()
        except NoCredentialsError as exc:
            raise TracesUnavailableError(
                f"AWS credentials not found. {_CREDENTIALS_HINT}",
                context={"region": self._region or "unknown"},
            ) from exc
        except (ClientError, BotoCoreError) as exc:
            raise TracesUnavailableError(
                "unable to query aws x-ray traces.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc

    def xǁAWSXRayTraceAdapterǁ_call__mutmut_16(self, operation: Callable[[], _ResponseT]) -> _ResponseT:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        try:
            return operation()
        except NoCredentialsError as exc:
            raise TracesUnavailableError(
                f"AWS credentials not found. {_CREDENTIALS_HINT}",
                context={"region": self._region or "unknown"},
            ) from exc
        except (ClientError, BotoCoreError) as exc:
            raise TracesUnavailableError(
                "UNABLE TO QUERY AWS X-RAY TRACES.",
                context={"region": self._region or "unknown", "error": str(exc)},
            ) from exc

    def xǁAWSXRayTraceAdapterǁ_call__mutmut_17(self, operation: Callable[[], _ResponseT]) -> _ResponseT:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        try:
            return operation()
        except NoCredentialsError as exc:
            raise TracesUnavailableError(
                f"AWS credentials not found. {_CREDENTIALS_HINT}",
                context={"region": self._region or "unknown"},
            ) from exc
        except (ClientError, BotoCoreError) as exc:
            raise TracesUnavailableError(
                "Unable to query AWS X-Ray traces.",
                context={"XXregionXX": self._region or "unknown", "error": str(exc)},
            ) from exc

    def xǁAWSXRayTraceAdapterǁ_call__mutmut_18(self, operation: Callable[[], _ResponseT]) -> _ResponseT:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        try:
            return operation()
        except NoCredentialsError as exc:
            raise TracesUnavailableError(
                f"AWS credentials not found. {_CREDENTIALS_HINT}",
                context={"region": self._region or "unknown"},
            ) from exc
        except (ClientError, BotoCoreError) as exc:
            raise TracesUnavailableError(
                "Unable to query AWS X-Ray traces.",
                context={"REGION": self._region or "unknown", "error": str(exc)},
            ) from exc

    def xǁAWSXRayTraceAdapterǁ_call__mutmut_19(self, operation: Callable[[], _ResponseT]) -> _ResponseT:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        try:
            return operation()
        except NoCredentialsError as exc:
            raise TracesUnavailableError(
                f"AWS credentials not found. {_CREDENTIALS_HINT}",
                context={"region": self._region or "unknown"},
            ) from exc
        except (ClientError, BotoCoreError) as exc:
            raise TracesUnavailableError(
                "Unable to query AWS X-Ray traces.",
                context={"region": self._region and "unknown", "error": str(exc)},
            ) from exc

    def xǁAWSXRayTraceAdapterǁ_call__mutmut_20(self, operation: Callable[[], _ResponseT]) -> _ResponseT:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        try:
            return operation()
        except NoCredentialsError as exc:
            raise TracesUnavailableError(
                f"AWS credentials not found. {_CREDENTIALS_HINT}",
                context={"region": self._region or "unknown"},
            ) from exc
        except (ClientError, BotoCoreError) as exc:
            raise TracesUnavailableError(
                "Unable to query AWS X-Ray traces.",
                context={"region": self._region or "XXunknownXX", "error": str(exc)},
            ) from exc

    def xǁAWSXRayTraceAdapterǁ_call__mutmut_21(self, operation: Callable[[], _ResponseT]) -> _ResponseT:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        try:
            return operation()
        except NoCredentialsError as exc:
            raise TracesUnavailableError(
                f"AWS credentials not found. {_CREDENTIALS_HINT}",
                context={"region": self._region or "unknown"},
            ) from exc
        except (ClientError, BotoCoreError) as exc:
            raise TracesUnavailableError(
                "Unable to query AWS X-Ray traces.",
                context={"region": self._region or "UNKNOWN", "error": str(exc)},
            ) from exc

    def xǁAWSXRayTraceAdapterǁ_call__mutmut_22(self, operation: Callable[[], _ResponseT]) -> _ResponseT:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        try:
            return operation()
        except NoCredentialsError as exc:
            raise TracesUnavailableError(
                f"AWS credentials not found. {_CREDENTIALS_HINT}",
                context={"region": self._region or "unknown"},
            ) from exc
        except (ClientError, BotoCoreError) as exc:
            raise TracesUnavailableError(
                "Unable to query AWS X-Ray traces.",
                context={"region": self._region or "unknown", "XXerrorXX": str(exc)},
            ) from exc

    def xǁAWSXRayTraceAdapterǁ_call__mutmut_23(self, operation: Callable[[], _ResponseT]) -> _ResponseT:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        try:
            return operation()
        except NoCredentialsError as exc:
            raise TracesUnavailableError(
                f"AWS credentials not found. {_CREDENTIALS_HINT}",
                context={"region": self._region or "unknown"},
            ) from exc
        except (ClientError, BotoCoreError) as exc:
            raise TracesUnavailableError(
                "Unable to query AWS X-Ray traces.",
                context={"region": self._region or "unknown", "ERROR": str(exc)},
            ) from exc

    def xǁAWSXRayTraceAdapterǁ_call__mutmut_24(self, operation: Callable[[], _ResponseT]) -> _ResponseT:
        from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

        try:
            return operation()
        except NoCredentialsError as exc:
            raise TracesUnavailableError(
                f"AWS credentials not found. {_CREDENTIALS_HINT}",
                context={"region": self._region or "unknown"},
            ) from exc
        except (ClientError, BotoCoreError) as exc:
            raise TracesUnavailableError(
                "Unable to query AWS X-Ray traces.",
                context={"region": self._region or "unknown", "error": str(None)},
            ) from exc

    @_mutmut_mutated(mutants_xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut)
    def _client_or_create(self) -> XRayClient:
        if self._xray_client is None:
            import boto3

            self._xray_client = boto3.client("xray", region_name=self._region)
        return self._xray_client

    def xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut_orig(self) -> XRayClient:
        if self._xray_client is None:
            import boto3

            self._xray_client = boto3.client("xray", region_name=self._region)
        return self._xray_client

    def xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut_1(self) -> XRayClient:
        if self._xray_client is not None:
            import boto3

            self._xray_client = boto3.client("xray", region_name=self._region)
        return self._xray_client

    def xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut_2(self) -> XRayClient:
        if self._xray_client is None:
            import boto3

            self._xray_client = None
        return self._xray_client

    def xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut_3(self) -> XRayClient:
        if self._xray_client is None:
            import boto3

            self._xray_client = boto3.client(None, region_name=self._region)
        return self._xray_client

    def xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut_4(self) -> XRayClient:
        if self._xray_client is None:
            import boto3

            self._xray_client = boto3.client("xray", region_name=None)
        return self._xray_client

    def xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut_5(self) -> XRayClient:
        if self._xray_client is None:
            import boto3

            self._xray_client = boto3.client(region_name=self._region)
        return self._xray_client

    def xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut_6(self) -> XRayClient:
        if self._xray_client is None:
            import boto3

            self._xray_client = boto3.client("xray", )
        return self._xray_client

    def xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut_7(self) -> XRayClient:
        if self._xray_client is None:
            import boto3

            self._xray_client = boto3.client("XXxrayXX", region_name=self._region)
        return self._xray_client

    def xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut_8(self) -> XRayClient:
        if self._xray_client is None:
            import boto3

            self._xray_client = boto3.client("XRAY", region_name=self._region)
        return self._xray_client

mutants_xǁAWSXRayTraceAdapterǁ__init____mutmut['_mutmut_orig'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ__init____mutmut['xǁAWSXRayTraceAdapterǁ__init____mutmut_1'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ__init____mutmut['xǁAWSXRayTraceAdapterǁ__init____mutmut_2'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut['_mutmut_orig'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut['xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_1'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut['xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_2'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut['xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_3'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut['xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_4'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut['xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_5'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut['xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_6'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut['xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_7'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut['xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_8'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut['xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_9'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut['xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_10'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut['xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_11'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut['xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_12'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut['xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_13'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut['xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_14'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut['xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_15'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut['xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_16'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁfetch_slow_spans__mutmut_16 # type: ignore # mutmut generated

mutants_xǁAWSXRayTraceAdapterǁfetch_total_traces__mutmut['_mutmut_orig'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁfetch_total_traces__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁfetch_total_traces__mutmut['xǁAWSXRayTraceAdapterǁfetch_total_traces__mutmut_1'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁfetch_total_traces__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁfetch_total_traces__mutmut['xǁAWSXRayTraceAdapterǁfetch_total_traces__mutmut_2'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁfetch_total_traces__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁfetch_total_traces__mutmut['xǁAWSXRayTraceAdapterǁfetch_total_traces__mutmut_3'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁfetch_total_traces__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁfetch_total_traces__mutmut['xǁAWSXRayTraceAdapterǁfetch_total_traces__mutmut_4'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁfetch_total_traces__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁfetch_total_traces__mutmut['xǁAWSXRayTraceAdapterǁfetch_total_traces__mutmut_5'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁfetch_total_traces__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁfetch_total_traces__mutmut['xǁAWSXRayTraceAdapterǁfetch_total_traces__mutmut_6'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁfetch_total_traces__mutmut_6 # type: ignore # mutmut generated

mutants_xǁAWSXRayTraceAdapterǁ_slow_filter__mutmut['_mutmut_orig'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_slow_filter__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_slow_filter__mutmut['xǁAWSXRayTraceAdapterǁ_slow_filter__mutmut_1'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_slow_filter__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_slow_filter__mutmut['xǁAWSXRayTraceAdapterǁ_slow_filter__mutmut_2'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_slow_filter__mutmut_2 # type: ignore # mutmut generated

mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut['_mutmut_orig'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_1'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_2'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_3'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_4'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_5'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_6'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_7'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_8'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_9'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_10'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_11'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_12'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_13'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_14'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_15'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_16'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_17'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_18'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_19'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_20'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_21'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_22'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_23'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_24'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_25'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_26'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_27'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_27 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_28'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_28 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_29'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_29 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_30'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_30 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_31'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_31 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_32'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_all_trace_summaries__mutmut_32 # type: ignore # mutmut generated

mutants_xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut['_mutmut_orig'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut['xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_1'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut['xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_2'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut['xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_3'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut['xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_4'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut['xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_5'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut['xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_6'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut['xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_7'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut['xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_8'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut['xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_9'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut['xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_10'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut['xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_11'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut['xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_12'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut['xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_13'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut['xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_14'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut['xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_15'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut['xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_16'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_fetch_spans_for_traces__mutmut_16 # type: ignore # mutmut generated

mutants_xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut['_mutmut_orig'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_1'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_2'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_3'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_4'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_5'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_6'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_7'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_8'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_9'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_10'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_11'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_12'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_13'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_14'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_15'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut['xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_16'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_get_trace_summaries__mutmut_16 # type: ignore # mutmut generated

mutants_xǁAWSXRayTraceAdapterǁ_batch_get_traces__mutmut['_mutmut_orig'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_batch_get_traces__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_batch_get_traces__mutmut['xǁAWSXRayTraceAdapterǁ_batch_get_traces__mutmut_1'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_batch_get_traces__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_batch_get_traces__mutmut['xǁAWSXRayTraceAdapterǁ_batch_get_traces__mutmut_2'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_batch_get_traces__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_batch_get_traces__mutmut['xǁAWSXRayTraceAdapterǁ_batch_get_traces__mutmut_3'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_batch_get_traces__mutmut_3 # type: ignore # mutmut generated

mutants_xǁAWSXRayTraceAdapterǁ_call__mutmut['_mutmut_orig'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_call__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_call__mutmut['xǁAWSXRayTraceAdapterǁ_call__mutmut_1'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_call__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_call__mutmut['xǁAWSXRayTraceAdapterǁ_call__mutmut_2'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_call__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_call__mutmut['xǁAWSXRayTraceAdapterǁ_call__mutmut_3'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_call__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_call__mutmut['xǁAWSXRayTraceAdapterǁ_call__mutmut_4'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_call__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_call__mutmut['xǁAWSXRayTraceAdapterǁ_call__mutmut_5'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_call__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_call__mutmut['xǁAWSXRayTraceAdapterǁ_call__mutmut_6'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_call__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_call__mutmut['xǁAWSXRayTraceAdapterǁ_call__mutmut_7'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_call__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_call__mutmut['xǁAWSXRayTraceAdapterǁ_call__mutmut_8'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_call__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_call__mutmut['xǁAWSXRayTraceAdapterǁ_call__mutmut_9'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_call__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_call__mutmut['xǁAWSXRayTraceAdapterǁ_call__mutmut_10'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_call__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_call__mutmut['xǁAWSXRayTraceAdapterǁ_call__mutmut_11'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_call__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_call__mutmut['xǁAWSXRayTraceAdapterǁ_call__mutmut_12'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_call__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_call__mutmut['xǁAWSXRayTraceAdapterǁ_call__mutmut_13'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_call__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_call__mutmut['xǁAWSXRayTraceAdapterǁ_call__mutmut_14'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_call__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_call__mutmut['xǁAWSXRayTraceAdapterǁ_call__mutmut_15'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_call__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_call__mutmut['xǁAWSXRayTraceAdapterǁ_call__mutmut_16'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_call__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_call__mutmut['xǁAWSXRayTraceAdapterǁ_call__mutmut_17'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_call__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_call__mutmut['xǁAWSXRayTraceAdapterǁ_call__mutmut_18'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_call__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_call__mutmut['xǁAWSXRayTraceAdapterǁ_call__mutmut_19'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_call__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_call__mutmut['xǁAWSXRayTraceAdapterǁ_call__mutmut_20'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_call__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_call__mutmut['xǁAWSXRayTraceAdapterǁ_call__mutmut_21'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_call__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_call__mutmut['xǁAWSXRayTraceAdapterǁ_call__mutmut_22'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_call__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_call__mutmut['xǁAWSXRayTraceAdapterǁ_call__mutmut_23'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_call__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_call__mutmut['xǁAWSXRayTraceAdapterǁ_call__mutmut_24'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_call__mutmut_24 # type: ignore # mutmut generated

mutants_xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut['_mutmut_orig'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut['xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut_1'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut['xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut_2'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut['xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut_3'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut['xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut_4'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut['xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut_5'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut['xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut_6'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut['xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut_7'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut['xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut_8'] = AWSXRayTraceAdapter.xǁAWSXRayTraceAdapterǁ_client_or_create__mutmut_8 # type: ignore # mutmut generated
mutants_x__chunked__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__chunked__mutmut)
def _chunked(items: list[str], size: int) -> list[list[str]]:
    return [items[i : i + size] for i in range(0, len(items), size)]


def x__chunked__mutmut_orig(items: list[str], size: int) -> list[list[str]]:
    return [items[i : i + size] for i in range(0, len(items), size)]


def x__chunked__mutmut_1(items: list[str], size: int) -> list[list[str]]:
    return [items[i : i - size] for i in range(0, len(items), size)]


def x__chunked__mutmut_2(items: list[str], size: int) -> list[list[str]]:
    return [items[i : i + size] for i in range(None, len(items), size)]


def x__chunked__mutmut_3(items: list[str], size: int) -> list[list[str]]:
    return [items[i : i + size] for i in range(0, None, size)]


def x__chunked__mutmut_4(items: list[str], size: int) -> list[list[str]]:
    return [items[i : i + size] for i in range(0, len(items), None)]


def x__chunked__mutmut_5(items: list[str], size: int) -> list[list[str]]:
    return [items[i : i + size] for i in range(len(items), size)]


def x__chunked__mutmut_6(items: list[str], size: int) -> list[list[str]]:
    return [items[i : i + size] for i in range(0, size)]


def x__chunked__mutmut_7(items: list[str], size: int) -> list[list[str]]:
    return [items[i : i + size] for i in range(0, len(items), )]


def x__chunked__mutmut_8(items: list[str], size: int) -> list[list[str]]:
    return [items[i : i + size] for i in range(1, len(items), size)]

mutants_x__chunked__mutmut['_mutmut_orig'] = x__chunked__mutmut_orig # type: ignore # mutmut generated
mutants_x__chunked__mutmut['x__chunked__mutmut_1'] = x__chunked__mutmut_1 # type: ignore # mutmut generated
mutants_x__chunked__mutmut['x__chunked__mutmut_2'] = x__chunked__mutmut_2 # type: ignore # mutmut generated
mutants_x__chunked__mutmut['x__chunked__mutmut_3'] = x__chunked__mutmut_3 # type: ignore # mutmut generated
mutants_x__chunked__mutmut['x__chunked__mutmut_4'] = x__chunked__mutmut_4 # type: ignore # mutmut generated
mutants_x__chunked__mutmut['x__chunked__mutmut_5'] = x__chunked__mutmut_5 # type: ignore # mutmut generated
mutants_x__chunked__mutmut['x__chunked__mutmut_6'] = x__chunked__mutmut_6 # type: ignore # mutmut generated
mutants_x__chunked__mutmut['x__chunked__mutmut_7'] = x__chunked__mutmut_7 # type: ignore # mutmut generated
mutants_x__chunked__mutmut['x__chunked__mutmut_8'] = x__chunked__mutmut_8 # type: ignore # mutmut generated
mutants_x__trace_to_spans__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__trace_to_spans__mutmut)
def _trace_to_spans(trace: _Trace) -> list[TraceSpan]:
    trace_id = trace.get("Id", "unknown")
    spans: list[TraceSpan] = []
    for segment in trace.get("Segments", []):
        document = segment.get("Document")
        if document:
            _walk_document(trace_id, json.loads(document), spans)
    return spans


def x__trace_to_spans__mutmut_orig(trace: _Trace) -> list[TraceSpan]:
    trace_id = trace.get("Id", "unknown")
    spans: list[TraceSpan] = []
    for segment in trace.get("Segments", []):
        document = segment.get("Document")
        if document:
            _walk_document(trace_id, json.loads(document), spans)
    return spans


def x__trace_to_spans__mutmut_1(trace: _Trace) -> list[TraceSpan]:
    trace_id = None
    spans: list[TraceSpan] = []
    for segment in trace.get("Segments", []):
        document = segment.get("Document")
        if document:
            _walk_document(trace_id, json.loads(document), spans)
    return spans


def x__trace_to_spans__mutmut_2(trace: _Trace) -> list[TraceSpan]:
    trace_id = trace.get(None, "unknown")
    spans: list[TraceSpan] = []
    for segment in trace.get("Segments", []):
        document = segment.get("Document")
        if document:
            _walk_document(trace_id, json.loads(document), spans)
    return spans


def x__trace_to_spans__mutmut_3(trace: _Trace) -> list[TraceSpan]:
    trace_id = trace.get("Id", None)
    spans: list[TraceSpan] = []
    for segment in trace.get("Segments", []):
        document = segment.get("Document")
        if document:
            _walk_document(trace_id, json.loads(document), spans)
    return spans


def x__trace_to_spans__mutmut_4(trace: _Trace) -> list[TraceSpan]:
    trace_id = trace.get("unknown")
    spans: list[TraceSpan] = []
    for segment in trace.get("Segments", []):
        document = segment.get("Document")
        if document:
            _walk_document(trace_id, json.loads(document), spans)
    return spans


def x__trace_to_spans__mutmut_5(trace: _Trace) -> list[TraceSpan]:
    trace_id = trace.get("Id", )
    spans: list[TraceSpan] = []
    for segment in trace.get("Segments", []):
        document = segment.get("Document")
        if document:
            _walk_document(trace_id, json.loads(document), spans)
    return spans


def x__trace_to_spans__mutmut_6(trace: _Trace) -> list[TraceSpan]:
    trace_id = trace.get("XXIdXX", "unknown")
    spans: list[TraceSpan] = []
    for segment in trace.get("Segments", []):
        document = segment.get("Document")
        if document:
            _walk_document(trace_id, json.loads(document), spans)
    return spans


def x__trace_to_spans__mutmut_7(trace: _Trace) -> list[TraceSpan]:
    trace_id = trace.get("id", "unknown")
    spans: list[TraceSpan] = []
    for segment in trace.get("Segments", []):
        document = segment.get("Document")
        if document:
            _walk_document(trace_id, json.loads(document), spans)
    return spans


def x__trace_to_spans__mutmut_8(trace: _Trace) -> list[TraceSpan]:
    trace_id = trace.get("ID", "unknown")
    spans: list[TraceSpan] = []
    for segment in trace.get("Segments", []):
        document = segment.get("Document")
        if document:
            _walk_document(trace_id, json.loads(document), spans)
    return spans


def x__trace_to_spans__mutmut_9(trace: _Trace) -> list[TraceSpan]:
    trace_id = trace.get("Id", "XXunknownXX")
    spans: list[TraceSpan] = []
    for segment in trace.get("Segments", []):
        document = segment.get("Document")
        if document:
            _walk_document(trace_id, json.loads(document), spans)
    return spans


def x__trace_to_spans__mutmut_10(trace: _Trace) -> list[TraceSpan]:
    trace_id = trace.get("Id", "UNKNOWN")
    spans: list[TraceSpan] = []
    for segment in trace.get("Segments", []):
        document = segment.get("Document")
        if document:
            _walk_document(trace_id, json.loads(document), spans)
    return spans


def x__trace_to_spans__mutmut_11(trace: _Trace) -> list[TraceSpan]:
    trace_id = trace.get("Id", "unknown")
    spans: list[TraceSpan] = None
    for segment in trace.get("Segments", []):
        document = segment.get("Document")
        if document:
            _walk_document(trace_id, json.loads(document), spans)
    return spans


def x__trace_to_spans__mutmut_12(trace: _Trace) -> list[TraceSpan]:
    trace_id = trace.get("Id", "unknown")
    spans: list[TraceSpan] = []
    for segment in trace.get(None, []):
        document = segment.get("Document")
        if document:
            _walk_document(trace_id, json.loads(document), spans)
    return spans


def x__trace_to_spans__mutmut_13(trace: _Trace) -> list[TraceSpan]:
    trace_id = trace.get("Id", "unknown")
    spans: list[TraceSpan] = []
    for segment in trace.get("Segments", None):
        document = segment.get("Document")
        if document:
            _walk_document(trace_id, json.loads(document), spans)
    return spans


def x__trace_to_spans__mutmut_14(trace: _Trace) -> list[TraceSpan]:
    trace_id = trace.get("Id", "unknown")
    spans: list[TraceSpan] = []
    for segment in trace.get([]):
        document = segment.get("Document")
        if document:
            _walk_document(trace_id, json.loads(document), spans)
    return spans


def x__trace_to_spans__mutmut_15(trace: _Trace) -> list[TraceSpan]:
    trace_id = trace.get("Id", "unknown")
    spans: list[TraceSpan] = []
    for segment in trace.get("Segments", ):
        document = segment.get("Document")
        if document:
            _walk_document(trace_id, json.loads(document), spans)
    return spans


def x__trace_to_spans__mutmut_16(trace: _Trace) -> list[TraceSpan]:
    trace_id = trace.get("Id", "unknown")
    spans: list[TraceSpan] = []
    for segment in trace.get("XXSegmentsXX", []):
        document = segment.get("Document")
        if document:
            _walk_document(trace_id, json.loads(document), spans)
    return spans


def x__trace_to_spans__mutmut_17(trace: _Trace) -> list[TraceSpan]:
    trace_id = trace.get("Id", "unknown")
    spans: list[TraceSpan] = []
    for segment in trace.get("segments", []):
        document = segment.get("Document")
        if document:
            _walk_document(trace_id, json.loads(document), spans)
    return spans


def x__trace_to_spans__mutmut_18(trace: _Trace) -> list[TraceSpan]:
    trace_id = trace.get("Id", "unknown")
    spans: list[TraceSpan] = []
    for segment in trace.get("SEGMENTS", []):
        document = segment.get("Document")
        if document:
            _walk_document(trace_id, json.loads(document), spans)
    return spans


def x__trace_to_spans__mutmut_19(trace: _Trace) -> list[TraceSpan]:
    trace_id = trace.get("Id", "unknown")
    spans: list[TraceSpan] = []
    for segment in trace.get("Segments", []):
        document = None
        if document:
            _walk_document(trace_id, json.loads(document), spans)
    return spans


def x__trace_to_spans__mutmut_20(trace: _Trace) -> list[TraceSpan]:
    trace_id = trace.get("Id", "unknown")
    spans: list[TraceSpan] = []
    for segment in trace.get("Segments", []):
        document = segment.get(None)
        if document:
            _walk_document(trace_id, json.loads(document), spans)
    return spans


def x__trace_to_spans__mutmut_21(trace: _Trace) -> list[TraceSpan]:
    trace_id = trace.get("Id", "unknown")
    spans: list[TraceSpan] = []
    for segment in trace.get("Segments", []):
        document = segment.get("XXDocumentXX")
        if document:
            _walk_document(trace_id, json.loads(document), spans)
    return spans


def x__trace_to_spans__mutmut_22(trace: _Trace) -> list[TraceSpan]:
    trace_id = trace.get("Id", "unknown")
    spans: list[TraceSpan] = []
    for segment in trace.get("Segments", []):
        document = segment.get("document")
        if document:
            _walk_document(trace_id, json.loads(document), spans)
    return spans


def x__trace_to_spans__mutmut_23(trace: _Trace) -> list[TraceSpan]:
    trace_id = trace.get("Id", "unknown")
    spans: list[TraceSpan] = []
    for segment in trace.get("Segments", []):
        document = segment.get("DOCUMENT")
        if document:
            _walk_document(trace_id, json.loads(document), spans)
    return spans


def x__trace_to_spans__mutmut_24(trace: _Trace) -> list[TraceSpan]:
    trace_id = trace.get("Id", "unknown")
    spans: list[TraceSpan] = []
    for segment in trace.get("Segments", []):
        document = segment.get("Document")
        if document:
            _walk_document(None, json.loads(document), spans)
    return spans


def x__trace_to_spans__mutmut_25(trace: _Trace) -> list[TraceSpan]:
    trace_id = trace.get("Id", "unknown")
    spans: list[TraceSpan] = []
    for segment in trace.get("Segments", []):
        document = segment.get("Document")
        if document:
            _walk_document(trace_id, None, spans)
    return spans


def x__trace_to_spans__mutmut_26(trace: _Trace) -> list[TraceSpan]:
    trace_id = trace.get("Id", "unknown")
    spans: list[TraceSpan] = []
    for segment in trace.get("Segments", []):
        document = segment.get("Document")
        if document:
            _walk_document(trace_id, json.loads(document), None)
    return spans


def x__trace_to_spans__mutmut_27(trace: _Trace) -> list[TraceSpan]:
    trace_id = trace.get("Id", "unknown")
    spans: list[TraceSpan] = []
    for segment in trace.get("Segments", []):
        document = segment.get("Document")
        if document:
            _walk_document(json.loads(document), spans)
    return spans


def x__trace_to_spans__mutmut_28(trace: _Trace) -> list[TraceSpan]:
    trace_id = trace.get("Id", "unknown")
    spans: list[TraceSpan] = []
    for segment in trace.get("Segments", []):
        document = segment.get("Document")
        if document:
            _walk_document(trace_id, spans)
    return spans


def x__trace_to_spans__mutmut_29(trace: _Trace) -> list[TraceSpan]:
    trace_id = trace.get("Id", "unknown")
    spans: list[TraceSpan] = []
    for segment in trace.get("Segments", []):
        document = segment.get("Document")
        if document:
            _walk_document(trace_id, json.loads(document), )
    return spans


def x__trace_to_spans__mutmut_30(trace: _Trace) -> list[TraceSpan]:
    trace_id = trace.get("Id", "unknown")
    spans: list[TraceSpan] = []
    for segment in trace.get("Segments", []):
        document = segment.get("Document")
        if document:
            _walk_document(trace_id, json.loads(None), spans)
    return spans

mutants_x__trace_to_spans__mutmut['_mutmut_orig'] = x__trace_to_spans__mutmut_orig # type: ignore # mutmut generated
mutants_x__trace_to_spans__mutmut['x__trace_to_spans__mutmut_1'] = x__trace_to_spans__mutmut_1 # type: ignore # mutmut generated
mutants_x__trace_to_spans__mutmut['x__trace_to_spans__mutmut_2'] = x__trace_to_spans__mutmut_2 # type: ignore # mutmut generated
mutants_x__trace_to_spans__mutmut['x__trace_to_spans__mutmut_3'] = x__trace_to_spans__mutmut_3 # type: ignore # mutmut generated
mutants_x__trace_to_spans__mutmut['x__trace_to_spans__mutmut_4'] = x__trace_to_spans__mutmut_4 # type: ignore # mutmut generated
mutants_x__trace_to_spans__mutmut['x__trace_to_spans__mutmut_5'] = x__trace_to_spans__mutmut_5 # type: ignore # mutmut generated
mutants_x__trace_to_spans__mutmut['x__trace_to_spans__mutmut_6'] = x__trace_to_spans__mutmut_6 # type: ignore # mutmut generated
mutants_x__trace_to_spans__mutmut['x__trace_to_spans__mutmut_7'] = x__trace_to_spans__mutmut_7 # type: ignore # mutmut generated
mutants_x__trace_to_spans__mutmut['x__trace_to_spans__mutmut_8'] = x__trace_to_spans__mutmut_8 # type: ignore # mutmut generated
mutants_x__trace_to_spans__mutmut['x__trace_to_spans__mutmut_9'] = x__trace_to_spans__mutmut_9 # type: ignore # mutmut generated
mutants_x__trace_to_spans__mutmut['x__trace_to_spans__mutmut_10'] = x__trace_to_spans__mutmut_10 # type: ignore # mutmut generated
mutants_x__trace_to_spans__mutmut['x__trace_to_spans__mutmut_11'] = x__trace_to_spans__mutmut_11 # type: ignore # mutmut generated
mutants_x__trace_to_spans__mutmut['x__trace_to_spans__mutmut_12'] = x__trace_to_spans__mutmut_12 # type: ignore # mutmut generated
mutants_x__trace_to_spans__mutmut['x__trace_to_spans__mutmut_13'] = x__trace_to_spans__mutmut_13 # type: ignore # mutmut generated
mutants_x__trace_to_spans__mutmut['x__trace_to_spans__mutmut_14'] = x__trace_to_spans__mutmut_14 # type: ignore # mutmut generated
mutants_x__trace_to_spans__mutmut['x__trace_to_spans__mutmut_15'] = x__trace_to_spans__mutmut_15 # type: ignore # mutmut generated
mutants_x__trace_to_spans__mutmut['x__trace_to_spans__mutmut_16'] = x__trace_to_spans__mutmut_16 # type: ignore # mutmut generated
mutants_x__trace_to_spans__mutmut['x__trace_to_spans__mutmut_17'] = x__trace_to_spans__mutmut_17 # type: ignore # mutmut generated
mutants_x__trace_to_spans__mutmut['x__trace_to_spans__mutmut_18'] = x__trace_to_spans__mutmut_18 # type: ignore # mutmut generated
mutants_x__trace_to_spans__mutmut['x__trace_to_spans__mutmut_19'] = x__trace_to_spans__mutmut_19 # type: ignore # mutmut generated
mutants_x__trace_to_spans__mutmut['x__trace_to_spans__mutmut_20'] = x__trace_to_spans__mutmut_20 # type: ignore # mutmut generated
mutants_x__trace_to_spans__mutmut['x__trace_to_spans__mutmut_21'] = x__trace_to_spans__mutmut_21 # type: ignore # mutmut generated
mutants_x__trace_to_spans__mutmut['x__trace_to_spans__mutmut_22'] = x__trace_to_spans__mutmut_22 # type: ignore # mutmut generated
mutants_x__trace_to_spans__mutmut['x__trace_to_spans__mutmut_23'] = x__trace_to_spans__mutmut_23 # type: ignore # mutmut generated
mutants_x__trace_to_spans__mutmut['x__trace_to_spans__mutmut_24'] = x__trace_to_spans__mutmut_24 # type: ignore # mutmut generated
mutants_x__trace_to_spans__mutmut['x__trace_to_spans__mutmut_25'] = x__trace_to_spans__mutmut_25 # type: ignore # mutmut generated
mutants_x__trace_to_spans__mutmut['x__trace_to_spans__mutmut_26'] = x__trace_to_spans__mutmut_26 # type: ignore # mutmut generated
mutants_x__trace_to_spans__mutmut['x__trace_to_spans__mutmut_27'] = x__trace_to_spans__mutmut_27 # type: ignore # mutmut generated
mutants_x__trace_to_spans__mutmut['x__trace_to_spans__mutmut_28'] = x__trace_to_spans__mutmut_28 # type: ignore # mutmut generated
mutants_x__trace_to_spans__mutmut['x__trace_to_spans__mutmut_29'] = x__trace_to_spans__mutmut_29 # type: ignore # mutmut generated
mutants_x__trace_to_spans__mutmut['x__trace_to_spans__mutmut_30'] = x__trace_to_spans__mutmut_30 # type: ignore # mutmut generated
mutants_x__walk_document__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__walk_document__mutmut)
def _walk_document(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = node.get("name", "unknown")
    spans.append(TraceSpan(trace_id=trace_id, span_name=str(name), duration_ms=_duration_ms(node)))
    subsegments = node.get("subsegments", [])
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(trace_id, subsegment, spans)


def x__walk_document__mutmut_orig(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = node.get("name", "unknown")
    spans.append(TraceSpan(trace_id=trace_id, span_name=str(name), duration_ms=_duration_ms(node)))
    subsegments = node.get("subsegments", [])
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(trace_id, subsegment, spans)


def x__walk_document__mutmut_1(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = None
    spans.append(TraceSpan(trace_id=trace_id, span_name=str(name), duration_ms=_duration_ms(node)))
    subsegments = node.get("subsegments", [])
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(trace_id, subsegment, spans)


def x__walk_document__mutmut_2(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = node.get(None, "unknown")
    spans.append(TraceSpan(trace_id=trace_id, span_name=str(name), duration_ms=_duration_ms(node)))
    subsegments = node.get("subsegments", [])
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(trace_id, subsegment, spans)


def x__walk_document__mutmut_3(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = node.get("name", None)
    spans.append(TraceSpan(trace_id=trace_id, span_name=str(name), duration_ms=_duration_ms(node)))
    subsegments = node.get("subsegments", [])
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(trace_id, subsegment, spans)


def x__walk_document__mutmut_4(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = node.get("unknown")
    spans.append(TraceSpan(trace_id=trace_id, span_name=str(name), duration_ms=_duration_ms(node)))
    subsegments = node.get("subsegments", [])
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(trace_id, subsegment, spans)


def x__walk_document__mutmut_5(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = node.get("name", )
    spans.append(TraceSpan(trace_id=trace_id, span_name=str(name), duration_ms=_duration_ms(node)))
    subsegments = node.get("subsegments", [])
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(trace_id, subsegment, spans)


def x__walk_document__mutmut_6(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = node.get("XXnameXX", "unknown")
    spans.append(TraceSpan(trace_id=trace_id, span_name=str(name), duration_ms=_duration_ms(node)))
    subsegments = node.get("subsegments", [])
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(trace_id, subsegment, spans)


def x__walk_document__mutmut_7(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = node.get("NAME", "unknown")
    spans.append(TraceSpan(trace_id=trace_id, span_name=str(name), duration_ms=_duration_ms(node)))
    subsegments = node.get("subsegments", [])
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(trace_id, subsegment, spans)


def x__walk_document__mutmut_8(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = node.get("name", "XXunknownXX")
    spans.append(TraceSpan(trace_id=trace_id, span_name=str(name), duration_ms=_duration_ms(node)))
    subsegments = node.get("subsegments", [])
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(trace_id, subsegment, spans)


def x__walk_document__mutmut_9(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = node.get("name", "UNKNOWN")
    spans.append(TraceSpan(trace_id=trace_id, span_name=str(name), duration_ms=_duration_ms(node)))
    subsegments = node.get("subsegments", [])
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(trace_id, subsegment, spans)


def x__walk_document__mutmut_10(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = node.get("name", "unknown")
    spans.append(None)
    subsegments = node.get("subsegments", [])
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(trace_id, subsegment, spans)


def x__walk_document__mutmut_11(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = node.get("name", "unknown")
    spans.append(TraceSpan(trace_id=None, span_name=str(name), duration_ms=_duration_ms(node)))
    subsegments = node.get("subsegments", [])
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(trace_id, subsegment, spans)


def x__walk_document__mutmut_12(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = node.get("name", "unknown")
    spans.append(TraceSpan(trace_id=trace_id, span_name=None, duration_ms=_duration_ms(node)))
    subsegments = node.get("subsegments", [])
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(trace_id, subsegment, spans)


def x__walk_document__mutmut_13(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = node.get("name", "unknown")
    spans.append(TraceSpan(trace_id=trace_id, span_name=str(name), duration_ms=None))
    subsegments = node.get("subsegments", [])
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(trace_id, subsegment, spans)


def x__walk_document__mutmut_14(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = node.get("name", "unknown")
    spans.append(TraceSpan(span_name=str(name), duration_ms=_duration_ms(node)))
    subsegments = node.get("subsegments", [])
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(trace_id, subsegment, spans)


def x__walk_document__mutmut_15(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = node.get("name", "unknown")
    spans.append(TraceSpan(trace_id=trace_id, duration_ms=_duration_ms(node)))
    subsegments = node.get("subsegments", [])
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(trace_id, subsegment, spans)


def x__walk_document__mutmut_16(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = node.get("name", "unknown")
    spans.append(TraceSpan(trace_id=trace_id, span_name=str(name), ))
    subsegments = node.get("subsegments", [])
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(trace_id, subsegment, spans)


def x__walk_document__mutmut_17(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = node.get("name", "unknown")
    spans.append(TraceSpan(trace_id=trace_id, span_name=str(None), duration_ms=_duration_ms(node)))
    subsegments = node.get("subsegments", [])
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(trace_id, subsegment, spans)


def x__walk_document__mutmut_18(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = node.get("name", "unknown")
    spans.append(TraceSpan(trace_id=trace_id, span_name=str(name), duration_ms=_duration_ms(None)))
    subsegments = node.get("subsegments", [])
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(trace_id, subsegment, spans)


def x__walk_document__mutmut_19(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = node.get("name", "unknown")
    spans.append(TraceSpan(trace_id=trace_id, span_name=str(name), duration_ms=_duration_ms(node)))
    subsegments = None
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(trace_id, subsegment, spans)


def x__walk_document__mutmut_20(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = node.get("name", "unknown")
    spans.append(TraceSpan(trace_id=trace_id, span_name=str(name), duration_ms=_duration_ms(node)))
    subsegments = node.get(None, [])
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(trace_id, subsegment, spans)


def x__walk_document__mutmut_21(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = node.get("name", "unknown")
    spans.append(TraceSpan(trace_id=trace_id, span_name=str(name), duration_ms=_duration_ms(node)))
    subsegments = node.get("subsegments", None)
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(trace_id, subsegment, spans)


def x__walk_document__mutmut_22(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = node.get("name", "unknown")
    spans.append(TraceSpan(trace_id=trace_id, span_name=str(name), duration_ms=_duration_ms(node)))
    subsegments = node.get([])
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(trace_id, subsegment, spans)


def x__walk_document__mutmut_23(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = node.get("name", "unknown")
    spans.append(TraceSpan(trace_id=trace_id, span_name=str(name), duration_ms=_duration_ms(node)))
    subsegments = node.get("subsegments", )
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(trace_id, subsegment, spans)


def x__walk_document__mutmut_24(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = node.get("name", "unknown")
    spans.append(TraceSpan(trace_id=trace_id, span_name=str(name), duration_ms=_duration_ms(node)))
    subsegments = node.get("XXsubsegmentsXX", [])
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(trace_id, subsegment, spans)


def x__walk_document__mutmut_25(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = node.get("name", "unknown")
    spans.append(TraceSpan(trace_id=trace_id, span_name=str(name), duration_ms=_duration_ms(node)))
    subsegments = node.get("SUBSEGMENTS", [])
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(trace_id, subsegment, spans)


def x__walk_document__mutmut_26(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = node.get("name", "unknown")
    spans.append(TraceSpan(trace_id=trace_id, span_name=str(name), duration_ms=_duration_ms(node)))
    subsegments = node.get("subsegments", [])
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(None, subsegment, spans)


def x__walk_document__mutmut_27(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = node.get("name", "unknown")
    spans.append(TraceSpan(trace_id=trace_id, span_name=str(name), duration_ms=_duration_ms(node)))
    subsegments = node.get("subsegments", [])
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(trace_id, None, spans)


def x__walk_document__mutmut_28(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = node.get("name", "unknown")
    spans.append(TraceSpan(trace_id=trace_id, span_name=str(name), duration_ms=_duration_ms(node)))
    subsegments = node.get("subsegments", [])
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(trace_id, subsegment, None)


def x__walk_document__mutmut_29(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = node.get("name", "unknown")
    spans.append(TraceSpan(trace_id=trace_id, span_name=str(name), duration_ms=_duration_ms(node)))
    subsegments = node.get("subsegments", [])
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(subsegment, spans)


def x__walk_document__mutmut_30(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = node.get("name", "unknown")
    spans.append(TraceSpan(trace_id=trace_id, span_name=str(name), duration_ms=_duration_ms(node)))
    subsegments = node.get("subsegments", [])
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(trace_id, spans)


def x__walk_document__mutmut_31(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = node.get("name", "unknown")
    spans.append(TraceSpan(trace_id=trace_id, span_name=str(name), duration_ms=_duration_ms(node)))
    subsegments = node.get("subsegments", [])
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(trace_id, subsegment, )

mutants_x__walk_document__mutmut['_mutmut_orig'] = x__walk_document__mutmut_orig # type: ignore # mutmut generated
mutants_x__walk_document__mutmut['x__walk_document__mutmut_1'] = x__walk_document__mutmut_1 # type: ignore # mutmut generated
mutants_x__walk_document__mutmut['x__walk_document__mutmut_2'] = x__walk_document__mutmut_2 # type: ignore # mutmut generated
mutants_x__walk_document__mutmut['x__walk_document__mutmut_3'] = x__walk_document__mutmut_3 # type: ignore # mutmut generated
mutants_x__walk_document__mutmut['x__walk_document__mutmut_4'] = x__walk_document__mutmut_4 # type: ignore # mutmut generated
mutants_x__walk_document__mutmut['x__walk_document__mutmut_5'] = x__walk_document__mutmut_5 # type: ignore # mutmut generated
mutants_x__walk_document__mutmut['x__walk_document__mutmut_6'] = x__walk_document__mutmut_6 # type: ignore # mutmut generated
mutants_x__walk_document__mutmut['x__walk_document__mutmut_7'] = x__walk_document__mutmut_7 # type: ignore # mutmut generated
mutants_x__walk_document__mutmut['x__walk_document__mutmut_8'] = x__walk_document__mutmut_8 # type: ignore # mutmut generated
mutants_x__walk_document__mutmut['x__walk_document__mutmut_9'] = x__walk_document__mutmut_9 # type: ignore # mutmut generated
mutants_x__walk_document__mutmut['x__walk_document__mutmut_10'] = x__walk_document__mutmut_10 # type: ignore # mutmut generated
mutants_x__walk_document__mutmut['x__walk_document__mutmut_11'] = x__walk_document__mutmut_11 # type: ignore # mutmut generated
mutants_x__walk_document__mutmut['x__walk_document__mutmut_12'] = x__walk_document__mutmut_12 # type: ignore # mutmut generated
mutants_x__walk_document__mutmut['x__walk_document__mutmut_13'] = x__walk_document__mutmut_13 # type: ignore # mutmut generated
mutants_x__walk_document__mutmut['x__walk_document__mutmut_14'] = x__walk_document__mutmut_14 # type: ignore # mutmut generated
mutants_x__walk_document__mutmut['x__walk_document__mutmut_15'] = x__walk_document__mutmut_15 # type: ignore # mutmut generated
mutants_x__walk_document__mutmut['x__walk_document__mutmut_16'] = x__walk_document__mutmut_16 # type: ignore # mutmut generated
mutants_x__walk_document__mutmut['x__walk_document__mutmut_17'] = x__walk_document__mutmut_17 # type: ignore # mutmut generated
mutants_x__walk_document__mutmut['x__walk_document__mutmut_18'] = x__walk_document__mutmut_18 # type: ignore # mutmut generated
mutants_x__walk_document__mutmut['x__walk_document__mutmut_19'] = x__walk_document__mutmut_19 # type: ignore # mutmut generated
mutants_x__walk_document__mutmut['x__walk_document__mutmut_20'] = x__walk_document__mutmut_20 # type: ignore # mutmut generated
mutants_x__walk_document__mutmut['x__walk_document__mutmut_21'] = x__walk_document__mutmut_21 # type: ignore # mutmut generated
mutants_x__walk_document__mutmut['x__walk_document__mutmut_22'] = x__walk_document__mutmut_22 # type: ignore # mutmut generated
mutants_x__walk_document__mutmut['x__walk_document__mutmut_23'] = x__walk_document__mutmut_23 # type: ignore # mutmut generated
mutants_x__walk_document__mutmut['x__walk_document__mutmut_24'] = x__walk_document__mutmut_24 # type: ignore # mutmut generated
mutants_x__walk_document__mutmut['x__walk_document__mutmut_25'] = x__walk_document__mutmut_25 # type: ignore # mutmut generated
mutants_x__walk_document__mutmut['x__walk_document__mutmut_26'] = x__walk_document__mutmut_26 # type: ignore # mutmut generated
mutants_x__walk_document__mutmut['x__walk_document__mutmut_27'] = x__walk_document__mutmut_27 # type: ignore # mutmut generated
mutants_x__walk_document__mutmut['x__walk_document__mutmut_28'] = x__walk_document__mutmut_28 # type: ignore # mutmut generated
mutants_x__walk_document__mutmut['x__walk_document__mutmut_29'] = x__walk_document__mutmut_29 # type: ignore # mutmut generated
mutants_x__walk_document__mutmut['x__walk_document__mutmut_30'] = x__walk_document__mutmut_30 # type: ignore # mutmut generated
mutants_x__walk_document__mutmut['x__walk_document__mutmut_31'] = x__walk_document__mutmut_31 # type: ignore # mutmut generated
mutants_x__duration_ms__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__duration_ms__mutmut)
def _duration_ms(node: dict[str, object]) -> float:
    start = node.get("start_time")
    end = node.get("end_time")
    if isinstance(start, int | float) and isinstance(end, int | float):
        return round((end - start) * _MILLIS_PER_SECOND, 2)
    return 0.0


def x__duration_ms__mutmut_orig(node: dict[str, object]) -> float:
    start = node.get("start_time")
    end = node.get("end_time")
    if isinstance(start, int | float) and isinstance(end, int | float):
        return round((end - start) * _MILLIS_PER_SECOND, 2)
    return 0.0


def x__duration_ms__mutmut_1(node: dict[str, object]) -> float:
    start = None
    end = node.get("end_time")
    if isinstance(start, int | float) and isinstance(end, int | float):
        return round((end - start) * _MILLIS_PER_SECOND, 2)
    return 0.0


def x__duration_ms__mutmut_2(node: dict[str, object]) -> float:
    start = node.get(None)
    end = node.get("end_time")
    if isinstance(start, int | float) and isinstance(end, int | float):
        return round((end - start) * _MILLIS_PER_SECOND, 2)
    return 0.0


def x__duration_ms__mutmut_3(node: dict[str, object]) -> float:
    start = node.get("XXstart_timeXX")
    end = node.get("end_time")
    if isinstance(start, int | float) and isinstance(end, int | float):
        return round((end - start) * _MILLIS_PER_SECOND, 2)
    return 0.0


def x__duration_ms__mutmut_4(node: dict[str, object]) -> float:
    start = node.get("START_TIME")
    end = node.get("end_time")
    if isinstance(start, int | float) and isinstance(end, int | float):
        return round((end - start) * _MILLIS_PER_SECOND, 2)
    return 0.0


def x__duration_ms__mutmut_5(node: dict[str, object]) -> float:
    start = node.get("start_time")
    end = None
    if isinstance(start, int | float) and isinstance(end, int | float):
        return round((end - start) * _MILLIS_PER_SECOND, 2)
    return 0.0


def x__duration_ms__mutmut_6(node: dict[str, object]) -> float:
    start = node.get("start_time")
    end = node.get(None)
    if isinstance(start, int | float) and isinstance(end, int | float):
        return round((end - start) * _MILLIS_PER_SECOND, 2)
    return 0.0


def x__duration_ms__mutmut_7(node: dict[str, object]) -> float:
    start = node.get("start_time")
    end = node.get("XXend_timeXX")
    if isinstance(start, int | float) and isinstance(end, int | float):
        return round((end - start) * _MILLIS_PER_SECOND, 2)
    return 0.0


def x__duration_ms__mutmut_8(node: dict[str, object]) -> float:
    start = node.get("start_time")
    end = node.get("END_TIME")
    if isinstance(start, int | float) and isinstance(end, int | float):
        return round((end - start) * _MILLIS_PER_SECOND, 2)
    return 0.0


def x__duration_ms__mutmut_9(node: dict[str, object]) -> float:
    start = node.get("start_time")
    end = node.get("end_time")
    if isinstance(start, int | float) or isinstance(end, int | float):
        return round((end - start) * _MILLIS_PER_SECOND, 2)
    return 0.0


def x__duration_ms__mutmut_10(node: dict[str, object]) -> float:
    start = node.get("start_time")
    end = node.get("end_time")
    if isinstance(start, int | float) and isinstance(end, int | float):
        return round(None, 2)
    return 0.0


def x__duration_ms__mutmut_11(node: dict[str, object]) -> float:
    start = node.get("start_time")
    end = node.get("end_time")
    if isinstance(start, int | float) and isinstance(end, int | float):
        return round((end - start) * _MILLIS_PER_SECOND, None)
    return 0.0


def x__duration_ms__mutmut_12(node: dict[str, object]) -> float:
    start = node.get("start_time")
    end = node.get("end_time")
    if isinstance(start, int | float) and isinstance(end, int | float):
        return round(2)
    return 0.0


def x__duration_ms__mutmut_13(node: dict[str, object]) -> float:
    start = node.get("start_time")
    end = node.get("end_time")
    if isinstance(start, int | float) and isinstance(end, int | float):
        return round((end - start) * _MILLIS_PER_SECOND, )
    return 0.0


def x__duration_ms__mutmut_14(node: dict[str, object]) -> float:
    start = node.get("start_time")
    end = node.get("end_time")
    if isinstance(start, int | float) and isinstance(end, int | float):
        return round((end - start) / _MILLIS_PER_SECOND, 2)
    return 0.0


def x__duration_ms__mutmut_15(node: dict[str, object]) -> float:
    start = node.get("start_time")
    end = node.get("end_time")
    if isinstance(start, int | float) and isinstance(end, int | float):
        return round((end + start) * _MILLIS_PER_SECOND, 2)
    return 0.0


def x__duration_ms__mutmut_16(node: dict[str, object]) -> float:
    start = node.get("start_time")
    end = node.get("end_time")
    if isinstance(start, int | float) and isinstance(end, int | float):
        return round((end - start) * _MILLIS_PER_SECOND, 3)
    return 0.0


def x__duration_ms__mutmut_17(node: dict[str, object]) -> float:
    start = node.get("start_time")
    end = node.get("end_time")
    if isinstance(start, int | float) and isinstance(end, int | float):
        return round((end - start) * _MILLIS_PER_SECOND, 2)
    return 1.0

mutants_x__duration_ms__mutmut['_mutmut_orig'] = x__duration_ms__mutmut_orig # type: ignore # mutmut generated
mutants_x__duration_ms__mutmut['x__duration_ms__mutmut_1'] = x__duration_ms__mutmut_1 # type: ignore # mutmut generated
mutants_x__duration_ms__mutmut['x__duration_ms__mutmut_2'] = x__duration_ms__mutmut_2 # type: ignore # mutmut generated
mutants_x__duration_ms__mutmut['x__duration_ms__mutmut_3'] = x__duration_ms__mutmut_3 # type: ignore # mutmut generated
mutants_x__duration_ms__mutmut['x__duration_ms__mutmut_4'] = x__duration_ms__mutmut_4 # type: ignore # mutmut generated
mutants_x__duration_ms__mutmut['x__duration_ms__mutmut_5'] = x__duration_ms__mutmut_5 # type: ignore # mutmut generated
mutants_x__duration_ms__mutmut['x__duration_ms__mutmut_6'] = x__duration_ms__mutmut_6 # type: ignore # mutmut generated
mutants_x__duration_ms__mutmut['x__duration_ms__mutmut_7'] = x__duration_ms__mutmut_7 # type: ignore # mutmut generated
mutants_x__duration_ms__mutmut['x__duration_ms__mutmut_8'] = x__duration_ms__mutmut_8 # type: ignore # mutmut generated
mutants_x__duration_ms__mutmut['x__duration_ms__mutmut_9'] = x__duration_ms__mutmut_9 # type: ignore # mutmut generated
mutants_x__duration_ms__mutmut['x__duration_ms__mutmut_10'] = x__duration_ms__mutmut_10 # type: ignore # mutmut generated
mutants_x__duration_ms__mutmut['x__duration_ms__mutmut_11'] = x__duration_ms__mutmut_11 # type: ignore # mutmut generated
mutants_x__duration_ms__mutmut['x__duration_ms__mutmut_12'] = x__duration_ms__mutmut_12 # type: ignore # mutmut generated
mutants_x__duration_ms__mutmut['x__duration_ms__mutmut_13'] = x__duration_ms__mutmut_13 # type: ignore # mutmut generated
mutants_x__duration_ms__mutmut['x__duration_ms__mutmut_14'] = x__duration_ms__mutmut_14 # type: ignore # mutmut generated
mutants_x__duration_ms__mutmut['x__duration_ms__mutmut_15'] = x__duration_ms__mutmut_15 # type: ignore # mutmut generated
mutants_x__duration_ms__mutmut['x__duration_ms__mutmut_16'] = x__duration_ms__mutmut_16 # type: ignore # mutmut generated
mutants_x__duration_ms__mutmut['x__duration_ms__mutmut_17'] = x__duration_ms__mutmut_17 # type: ignore # mutmut generated
