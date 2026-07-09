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


class AWSXRayTraceAdapter(TraceQueryPort):
    """TraceQueryPort backed by AWS X-Ray (the span store behind Application
    Signals). Fetches slow traces and their spans natively — no Tempo/Jaeger.
    """

    def __init__(self, region: str | None, xray_client: XRayClient | None = None) -> None:
        self._region = region
        self._xray_client = xray_client

    def fetch_slow_spans(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        summaries = self._all_trace_summaries(self._slow_filter(request), request)
        trace_ids = [summary["Id"] for summary in summaries if summary.get("Id")]
        if not trace_ids:
            return []
        return self._fetch_spans_for_traces(trace_ids)

    def fetch_total_traces(self, request: LatencyDiagnosticRequest) -> int:
        summaries = self._all_trace_summaries(self._total_filter(request), request)
        return len(summaries)

    def _slow_filter(self, request: LatencyDiagnosticRequest) -> str:
        threshold_seconds = request.threshold_ms / _MILLIS_PER_SECOND
        return f'service("{request.service_name}") AND responsetime > {threshold_seconds}'

    def _total_filter(self, request: LatencyDiagnosticRequest) -> str:
        return f'service("{request.service_name}")'

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

    def _fetch_spans_for_traces(self, trace_ids: list[str]) -> list[list[TraceSpan]]:
        traces_spans: list[list[TraceSpan]] = []
        for batch in _chunked(trace_ids, _MAX_TRACE_IDS_PER_BATCH):
            response = self._batch_get_traces(batch)
            for trace in response.get("Traces", []):
                traces_spans.append(_trace_to_spans(trace))
        return traces_spans

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

    def _batch_get_traces(self, trace_ids: list[str]) -> _BatchGetTracesResponse:
        return self._call(lambda: self._client_or_create().batch_get_traces(TraceIds=trace_ids))

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

    def _client_or_create(self) -> XRayClient:
        if self._xray_client is None:
            import boto3

            self._xray_client = boto3.client("xray", region_name=self._region)
        return self._xray_client


def _chunked(items: list[str], size: int) -> list[list[str]]:
    return [items[i : i + size] for i in range(0, len(items), size)]


def _trace_to_spans(trace: _Trace) -> list[TraceSpan]:
    trace_id = trace.get("Id", "unknown")
    spans: list[TraceSpan] = []
    for segment in trace.get("Segments", []):
        document = segment.get("Document")
        if document:
            _walk_document(trace_id, json.loads(document), spans)
    return spans


def _walk_document(trace_id: str, node: dict[str, object], spans: list[TraceSpan]) -> None:
    name = node.get("name", "unknown")
    spans.append(TraceSpan(trace_id=trace_id, span_name=str(name), duration_ms=_duration_ms(node)))
    subsegments = node.get("subsegments", [])
    if isinstance(subsegments, list):
        for subsegment in subsegments:
            if isinstance(subsegment, dict):
                _walk_document(trace_id, subsegment, spans)


def _duration_ms(node: dict[str, object]) -> float:
    start = node.get("start_time")
    end = node.get("end_time")
    if isinstance(start, int | float) and isinstance(end, int | float):
        return round((end - start) * _MILLIS_PER_SECOND, 2)
    return 0.0
