from __future__ import annotations

from collections.abc import Iterable
from datetime import UTC, datetime, timedelta
from typing import Protocol

from hexawyn.application.ports.driven.trace_query_port import (
    LatencyDiagnosticRequest,
    TraceQueryPort,
    TraceSpan,
)
from hexawyn.domain.errors import TracesUnavailableError

_MILLIS_PER_SECOND = 1000.0
_CREDENTIALS_HINT = "Run 'gcloud auth application-default login', then retry."


class _TraceSpanProto(Protocol):
    name: str
    start_time: datetime | None
    end_time: datetime | None


class _TraceProto(Protocol):
    trace_id: str
    spans: Iterable[_TraceSpanProto]


class TraceClient(Protocol):
    """Minimal contract for the google-cloud-trace v1 client used here."""

    def list_traces(self, request: object) -> Iterable[_TraceProto]:
        """Return traces matching the request filter and time window."""


class GCPCloudTraceAdapter(TraceQueryPort):
    """TraceQueryPort backed by Google Cloud Trace (v1 read API).

    Fetches slow traces and their spans natively on GKE — no Tempo/Jaeger.
    """

    def __init__(self, project_id: str, trace_client: TraceClient | None = None) -> None:
        self._project_id = project_id
        self._trace_client = trace_client

    def fetch_slow_spans(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        traces = self._list_traces(self._slow_filter(request), request, complete=True)
        return [_trace_to_spans(trace) for trace in traces]

    def fetch_total_traces(self, request: LatencyDiagnosticRequest) -> int:
        traces = self._list_traces(self._total_filter(request), request, complete=False)
        return sum(1 for _ in traces)

    def _slow_filter(self, request: LatencyDiagnosticRequest) -> str:
        return f"span:{request.service_name} latency:{int(request.threshold_ms)}ms"

    def _total_filter(self, request: LatencyDiagnosticRequest) -> str:
        return f"span:{request.service_name}"

    def _list_traces(
        self, filter_expression: str, request: LatencyDiagnosticRequest, complete: bool
    ) -> list[_TraceProto]:
        from google.api_core.exceptions import GoogleAPICallError
        from google.auth.exceptions import DefaultCredentialsError
        from google.cloud import trace_v1

        end = datetime.now(UTC)
        start = end - timedelta(minutes=request.time_window_minutes)
        view = (
            trace_v1.ListTracesRequest.ViewType.COMPLETE
            if complete
            else trace_v1.ListTracesRequest.ViewType.MINIMAL
        )
        list_request = trace_v1.ListTracesRequest(
            project_id=self._project_id,
            view=view,
            filter=filter_expression,
            start_time=start,
            end_time=end,
        )
        try:
            return list(self._client_or_create().list_traces(request=list_request))
        except DefaultCredentialsError as exc:
            raise TracesUnavailableError(
                f"GCP credentials not found. {_CREDENTIALS_HINT}",
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise TracesUnavailableError(
                "Unable to query Google Cloud Trace.",
                context={"project": self._project_id, "error": str(exc)},
            ) from exc

    def _client_or_create(self) -> TraceClient:
        client = self._trace_client
        if client is None:
            from google.cloud import trace_v1

            client = _as_trace_client(trace_v1.TraceServiceClient())
            self._trace_client = client
        return client


def _as_trace_client(client: object) -> TraceClient:
    return client  # type: ignore[return-value]


def _trace_to_spans(trace: _TraceProto) -> list[TraceSpan]:
    trace_id = str(trace.trace_id)
    return [
        TraceSpan(
            trace_id=trace_id,
            span_name=str(span.name),
            duration_ms=_duration_ms(span),
        )
        for span in trace.spans
    ]


def _duration_ms(span: _TraceSpanProto) -> float:
    start = span.start_time
    end = span.end_time
    if start is None or end is None:
        return 0.0
    return round((end - start).total_seconds() * _MILLIS_PER_SECOND, 2)
