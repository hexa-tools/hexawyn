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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


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
mutants_xǁGCPCloudTraceAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGCPCloudTraceAdapterǁ_slow_filter__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGCPCloudTraceAdapterǁ_client_or_create__mutmut: MutantDict = {}  # type: ignore


class GCPCloudTraceAdapter(TraceQueryPort):
    """TraceQueryPort backed by Google Cloud Trace (v1 read API).

    Fetches slow traces and their spans natively on GKE — no Tempo/Jaeger.
    """

    @_mutmut_mutated(mutants_xǁGCPCloudTraceAdapterǁ__init____mutmut)
    def __init__(self, project_id: str, trace_client: TraceClient | None = None) -> None:
        self._project_id = project_id
        self._trace_client = trace_client

    def xǁGCPCloudTraceAdapterǁ__init____mutmut_orig(self, project_id: str, trace_client: TraceClient | None = None) -> None:
        self._project_id = project_id
        self._trace_client = trace_client

    def xǁGCPCloudTraceAdapterǁ__init____mutmut_1(self, project_id: str, trace_client: TraceClient | None = None) -> None:
        self._project_id = None
        self._trace_client = trace_client

    def xǁGCPCloudTraceAdapterǁ__init____mutmut_2(self, project_id: str, trace_client: TraceClient | None = None) -> None:
        self._project_id = project_id
        self._trace_client = None

    @_mutmut_mutated(mutants_xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut)
    def fetch_slow_spans(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        traces = self._list_traces(self._slow_filter(request), request, complete=True)
        return [_trace_to_spans(trace) for trace in traces]

    def xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut_orig(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        traces = self._list_traces(self._slow_filter(request), request, complete=True)
        return [_trace_to_spans(trace) for trace in traces]

    def xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut_1(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        traces = None
        return [_trace_to_spans(trace) for trace in traces]

    def xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut_2(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        traces = self._list_traces(None, request, complete=True)
        return [_trace_to_spans(trace) for trace in traces]

    def xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut_3(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        traces = self._list_traces(self._slow_filter(request), None, complete=True)
        return [_trace_to_spans(trace) for trace in traces]

    def xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut_4(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        traces = self._list_traces(self._slow_filter(request), request, complete=None)
        return [_trace_to_spans(trace) for trace in traces]

    def xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut_5(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        traces = self._list_traces(request, complete=True)
        return [_trace_to_spans(trace) for trace in traces]

    def xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut_6(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        traces = self._list_traces(self._slow_filter(request), complete=True)
        return [_trace_to_spans(trace) for trace in traces]

    def xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut_7(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        traces = self._list_traces(self._slow_filter(request), request, )
        return [_trace_to_spans(trace) for trace in traces]

    def xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut_8(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        traces = self._list_traces(self._slow_filter(None), request, complete=True)
        return [_trace_to_spans(trace) for trace in traces]

    def xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut_9(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        traces = self._list_traces(self._slow_filter(request), request, complete=False)
        return [_trace_to_spans(trace) for trace in traces]

    def xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut_10(self, request: LatencyDiagnosticRequest) -> list[list[TraceSpan]]:
        traces = self._list_traces(self._slow_filter(request), request, complete=True)
        return [_trace_to_spans(None) for trace in traces]

    @_mutmut_mutated(mutants_xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut)
    def fetch_total_traces(self, request: LatencyDiagnosticRequest) -> int:
        traces = self._list_traces(self._total_filter(request), request, complete=False)
        return sum(1 for _ in traces)

    def xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_orig(self, request: LatencyDiagnosticRequest) -> int:
        traces = self._list_traces(self._total_filter(request), request, complete=False)
        return sum(1 for _ in traces)

    def xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_1(self, request: LatencyDiagnosticRequest) -> int:
        traces = None
        return sum(1 for _ in traces)

    def xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_2(self, request: LatencyDiagnosticRequest) -> int:
        traces = self._list_traces(None, request, complete=False)
        return sum(1 for _ in traces)

    def xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_3(self, request: LatencyDiagnosticRequest) -> int:
        traces = self._list_traces(self._total_filter(request), None, complete=False)
        return sum(1 for _ in traces)

    def xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_4(self, request: LatencyDiagnosticRequest) -> int:
        traces = self._list_traces(self._total_filter(request), request, complete=None)
        return sum(1 for _ in traces)

    def xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_5(self, request: LatencyDiagnosticRequest) -> int:
        traces = self._list_traces(request, complete=False)
        return sum(1 for _ in traces)

    def xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_6(self, request: LatencyDiagnosticRequest) -> int:
        traces = self._list_traces(self._total_filter(request), complete=False)
        return sum(1 for _ in traces)

    def xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_7(self, request: LatencyDiagnosticRequest) -> int:
        traces = self._list_traces(self._total_filter(request), request, )
        return sum(1 for _ in traces)

    def xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_8(self, request: LatencyDiagnosticRequest) -> int:
        traces = self._list_traces(self._total_filter(None), request, complete=False)
        return sum(1 for _ in traces)

    def xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_9(self, request: LatencyDiagnosticRequest) -> int:
        traces = self._list_traces(self._total_filter(request), request, complete=True)
        return sum(1 for _ in traces)

    def xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_10(self, request: LatencyDiagnosticRequest) -> int:
        traces = self._list_traces(self._total_filter(request), request, complete=False)
        return sum(None)

    def xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_11(self, request: LatencyDiagnosticRequest) -> int:
        traces = self._list_traces(self._total_filter(request), request, complete=False)
        return sum(2 for _ in traces)

    @_mutmut_mutated(mutants_xǁGCPCloudTraceAdapterǁ_slow_filter__mutmut)
    def _slow_filter(self, request: LatencyDiagnosticRequest) -> str:
        return f"span:{request.service_name} latency:{int(request.threshold_ms)}ms"

    def xǁGCPCloudTraceAdapterǁ_slow_filter__mutmut_orig(self, request: LatencyDiagnosticRequest) -> str:
        return f"span:{request.service_name} latency:{int(request.threshold_ms)}ms"

    def xǁGCPCloudTraceAdapterǁ_slow_filter__mutmut_1(self, request: LatencyDiagnosticRequest) -> str:
        return f"span:{request.service_name} latency:{int(None)}ms"

    def _total_filter(self, request: LatencyDiagnosticRequest) -> str:
        return f"span:{request.service_name}"

    @_mutmut_mutated(mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut)
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

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_orig(
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

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_1(
        self, filter_expression: str, request: LatencyDiagnosticRequest, complete: bool
    ) -> list[_TraceProto]:
        from google.api_core.exceptions import GoogleAPICallError
        from google.auth.exceptions import DefaultCredentialsError
        from google.cloud import trace_v1

        end = None
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

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_2(
        self, filter_expression: str, request: LatencyDiagnosticRequest, complete: bool
    ) -> list[_TraceProto]:
        from google.api_core.exceptions import GoogleAPICallError
        from google.auth.exceptions import DefaultCredentialsError
        from google.cloud import trace_v1

        end = datetime.now(None)
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

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_3(
        self, filter_expression: str, request: LatencyDiagnosticRequest, complete: bool
    ) -> list[_TraceProto]:
        from google.api_core.exceptions import GoogleAPICallError
        from google.auth.exceptions import DefaultCredentialsError
        from google.cloud import trace_v1

        end = datetime.now(UTC)
        start = None
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

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_4(
        self, filter_expression: str, request: LatencyDiagnosticRequest, complete: bool
    ) -> list[_TraceProto]:
        from google.api_core.exceptions import GoogleAPICallError
        from google.auth.exceptions import DefaultCredentialsError
        from google.cloud import trace_v1

        end = datetime.now(UTC)
        start = end + timedelta(minutes=request.time_window_minutes)
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

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_5(
        self, filter_expression: str, request: LatencyDiagnosticRequest, complete: bool
    ) -> list[_TraceProto]:
        from google.api_core.exceptions import GoogleAPICallError
        from google.auth.exceptions import DefaultCredentialsError
        from google.cloud import trace_v1

        end = datetime.now(UTC)
        start = end - timedelta(minutes=None)
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

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_6(
        self, filter_expression: str, request: LatencyDiagnosticRequest, complete: bool
    ) -> list[_TraceProto]:
        from google.api_core.exceptions import GoogleAPICallError
        from google.auth.exceptions import DefaultCredentialsError
        from google.cloud import trace_v1

        end = datetime.now(UTC)
        start = end - timedelta(minutes=request.time_window_minutes)
        view = None
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

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_7(
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
        list_request = None
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

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_8(
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
            project_id=None,
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

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_9(
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
            view=None,
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

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_10(
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
            filter=None,
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

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_11(
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
            start_time=None,
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

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_12(
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
            end_time=None,
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

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_13(
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

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_14(
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

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_15(
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

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_16(
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

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_17(
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

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_18(
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
            return list(None)
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

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_19(
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
            return list(self._client_or_create().list_traces(request=None))
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

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_20(
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
                None,
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise TracesUnavailableError(
                "Unable to query Google Cloud Trace.",
                context={"project": self._project_id, "error": str(exc)},
            ) from exc

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_21(
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
                context=None,
            ) from exc
        except GoogleAPICallError as exc:
            raise TracesUnavailableError(
                "Unable to query Google Cloud Trace.",
                context={"project": self._project_id, "error": str(exc)},
            ) from exc

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_22(
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
                context={"project": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise TracesUnavailableError(
                "Unable to query Google Cloud Trace.",
                context={"project": self._project_id, "error": str(exc)},
            ) from exc

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_23(
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
                ) from exc
        except GoogleAPICallError as exc:
            raise TracesUnavailableError(
                "Unable to query Google Cloud Trace.",
                context={"project": self._project_id, "error": str(exc)},
            ) from exc

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_24(
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
                context={"XXprojectXX": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise TracesUnavailableError(
                "Unable to query Google Cloud Trace.",
                context={"project": self._project_id, "error": str(exc)},
            ) from exc

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_25(
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
                context={"PROJECT": self._project_id},
            ) from exc
        except GoogleAPICallError as exc:
            raise TracesUnavailableError(
                "Unable to query Google Cloud Trace.",
                context={"project": self._project_id, "error": str(exc)},
            ) from exc

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_26(
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
                None,
                context={"project": self._project_id, "error": str(exc)},
            ) from exc

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_27(
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
                context=None,
            ) from exc

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_28(
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
                context={"project": self._project_id, "error": str(exc)},
            ) from exc

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_29(
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
                ) from exc

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_30(
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
                "XXUnable to query Google Cloud Trace.XX",
                context={"project": self._project_id, "error": str(exc)},
            ) from exc

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_31(
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
                "unable to query google cloud trace.",
                context={"project": self._project_id, "error": str(exc)},
            ) from exc

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_32(
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
                "UNABLE TO QUERY GOOGLE CLOUD TRACE.",
                context={"project": self._project_id, "error": str(exc)},
            ) from exc

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_33(
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
                context={"XXprojectXX": self._project_id, "error": str(exc)},
            ) from exc

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_34(
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
                context={"PROJECT": self._project_id, "error": str(exc)},
            ) from exc

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_35(
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
                context={"project": self._project_id, "XXerrorXX": str(exc)},
            ) from exc

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_36(
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
                context={"project": self._project_id, "ERROR": str(exc)},
            ) from exc

    def xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_37(
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
                context={"project": self._project_id, "error": str(None)},
            ) from exc

    @_mutmut_mutated(mutants_xǁGCPCloudTraceAdapterǁ_client_or_create__mutmut)
    def _client_or_create(self) -> TraceClient:
        client = self._trace_client
        if client is None:
            from google.cloud import trace_v1

            client = _as_trace_client(trace_v1.TraceServiceClient())
            self._trace_client = client
        return client

    def xǁGCPCloudTraceAdapterǁ_client_or_create__mutmut_orig(self) -> TraceClient:
        client = self._trace_client
        if client is None:
            from google.cloud import trace_v1

            client = _as_trace_client(trace_v1.TraceServiceClient())
            self._trace_client = client
        return client

    def xǁGCPCloudTraceAdapterǁ_client_or_create__mutmut_1(self) -> TraceClient:
        client = None
        if client is None:
            from google.cloud import trace_v1

            client = _as_trace_client(trace_v1.TraceServiceClient())
            self._trace_client = client
        return client

    def xǁGCPCloudTraceAdapterǁ_client_or_create__mutmut_2(self) -> TraceClient:
        client = self._trace_client
        if client is not None:
            from google.cloud import trace_v1

            client = _as_trace_client(trace_v1.TraceServiceClient())
            self._trace_client = client
        return client

    def xǁGCPCloudTraceAdapterǁ_client_or_create__mutmut_3(self) -> TraceClient:
        client = self._trace_client
        if client is None:
            from google.cloud import trace_v1

            client = None
            self._trace_client = client
        return client

    def xǁGCPCloudTraceAdapterǁ_client_or_create__mutmut_4(self) -> TraceClient:
        client = self._trace_client
        if client is None:
            from google.cloud import trace_v1

            client = _as_trace_client(None)
            self._trace_client = client
        return client

    def xǁGCPCloudTraceAdapterǁ_client_or_create__mutmut_5(self) -> TraceClient:
        client = self._trace_client
        if client is None:
            from google.cloud import trace_v1

            client = _as_trace_client(trace_v1.TraceServiceClient())
            self._trace_client = None
        return client

mutants_xǁGCPCloudTraceAdapterǁ__init____mutmut['_mutmut_orig'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ__init____mutmut['xǁGCPCloudTraceAdapterǁ__init____mutmut_1'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ__init____mutmut['xǁGCPCloudTraceAdapterǁ__init____mutmut_2'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut['_mutmut_orig'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut['xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut_1'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut['xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut_2'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut['xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut_3'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut['xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut_4'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut['xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut_5'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut['xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut_6'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut['xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut_7'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut['xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut_8'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut['xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut_9'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut['xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut_10'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁfetch_slow_spans__mutmut_10 # type: ignore # mutmut generated

mutants_xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut['_mutmut_orig'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut['xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_1'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut['xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_2'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut['xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_3'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut['xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_4'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut['xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_5'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut['xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_6'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut['xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_7'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut['xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_8'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut['xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_9'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut['xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_10'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut['xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_11'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁfetch_total_traces__mutmut_11 # type: ignore # mutmut generated

mutants_xǁGCPCloudTraceAdapterǁ_slow_filter__mutmut['_mutmut_orig'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_slow_filter__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_slow_filter__mutmut['xǁGCPCloudTraceAdapterǁ_slow_filter__mutmut_1'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_slow_filter__mutmut_1 # type: ignore # mutmut generated

mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['_mutmut_orig'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_1'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_2'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_3'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_4'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_5'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_6'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_7'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_8'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_9'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_10'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_11'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_12'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_13'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_14'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_15'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_16'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_17'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_18'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_19'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_20'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_21'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_22'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_23'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_24'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_25'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_26'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_27'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_28'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_29'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_29 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_30'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_30 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_31'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_31 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_32'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_32 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_33'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_33 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_34'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_34 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_35'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_35 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_36'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_36 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_list_traces__mutmut['xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_37'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_list_traces__mutmut_37 # type: ignore # mutmut generated

mutants_xǁGCPCloudTraceAdapterǁ_client_or_create__mutmut['_mutmut_orig'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_client_or_create__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_client_or_create__mutmut['xǁGCPCloudTraceAdapterǁ_client_or_create__mutmut_1'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_client_or_create__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_client_or_create__mutmut['xǁGCPCloudTraceAdapterǁ_client_or_create__mutmut_2'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_client_or_create__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_client_or_create__mutmut['xǁGCPCloudTraceAdapterǁ_client_or_create__mutmut_3'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_client_or_create__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_client_or_create__mutmut['xǁGCPCloudTraceAdapterǁ_client_or_create__mutmut_4'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_client_or_create__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGCPCloudTraceAdapterǁ_client_or_create__mutmut['xǁGCPCloudTraceAdapterǁ_client_or_create__mutmut_5'] = GCPCloudTraceAdapter.xǁGCPCloudTraceAdapterǁ_client_or_create__mutmut_5 # type: ignore # mutmut generated


def _as_trace_client(client: object) -> TraceClient:
    return client  # type: ignore[return-value]
mutants_x__trace_to_spans__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__trace_to_spans__mutmut)
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


def x__trace_to_spans__mutmut_orig(trace: _TraceProto) -> list[TraceSpan]:
    trace_id = str(trace.trace_id)
    return [
        TraceSpan(
            trace_id=trace_id,
            span_name=str(span.name),
            duration_ms=_duration_ms(span),
        )
        for span in trace.spans
    ]


def x__trace_to_spans__mutmut_1(trace: _TraceProto) -> list[TraceSpan]:
    trace_id = None
    return [
        TraceSpan(
            trace_id=trace_id,
            span_name=str(span.name),
            duration_ms=_duration_ms(span),
        )
        for span in trace.spans
    ]


def x__trace_to_spans__mutmut_2(trace: _TraceProto) -> list[TraceSpan]:
    trace_id = str(None)
    return [
        TraceSpan(
            trace_id=trace_id,
            span_name=str(span.name),
            duration_ms=_duration_ms(span),
        )
        for span in trace.spans
    ]


def x__trace_to_spans__mutmut_3(trace: _TraceProto) -> list[TraceSpan]:
    trace_id = str(trace.trace_id)
    return [
        TraceSpan(
            trace_id=None,
            span_name=str(span.name),
            duration_ms=_duration_ms(span),
        )
        for span in trace.spans
    ]


def x__trace_to_spans__mutmut_4(trace: _TraceProto) -> list[TraceSpan]:
    trace_id = str(trace.trace_id)
    return [
        TraceSpan(
            trace_id=trace_id,
            span_name=None,
            duration_ms=_duration_ms(span),
        )
        for span in trace.spans
    ]


def x__trace_to_spans__mutmut_5(trace: _TraceProto) -> list[TraceSpan]:
    trace_id = str(trace.trace_id)
    return [
        TraceSpan(
            trace_id=trace_id,
            span_name=str(span.name),
            duration_ms=None,
        )
        for span in trace.spans
    ]


def x__trace_to_spans__mutmut_6(trace: _TraceProto) -> list[TraceSpan]:
    trace_id = str(trace.trace_id)
    return [
        TraceSpan(
            span_name=str(span.name),
            duration_ms=_duration_ms(span),
        )
        for span in trace.spans
    ]


def x__trace_to_spans__mutmut_7(trace: _TraceProto) -> list[TraceSpan]:
    trace_id = str(trace.trace_id)
    return [
        TraceSpan(
            trace_id=trace_id,
            duration_ms=_duration_ms(span),
        )
        for span in trace.spans
    ]


def x__trace_to_spans__mutmut_8(trace: _TraceProto) -> list[TraceSpan]:
    trace_id = str(trace.trace_id)
    return [
        TraceSpan(
            trace_id=trace_id,
            span_name=str(span.name),
            )
        for span in trace.spans
    ]


def x__trace_to_spans__mutmut_9(trace: _TraceProto) -> list[TraceSpan]:
    trace_id = str(trace.trace_id)
    return [
        TraceSpan(
            trace_id=trace_id,
            span_name=str(None),
            duration_ms=_duration_ms(span),
        )
        for span in trace.spans
    ]


def x__trace_to_spans__mutmut_10(trace: _TraceProto) -> list[TraceSpan]:
    trace_id = str(trace.trace_id)
    return [
        TraceSpan(
            trace_id=trace_id,
            span_name=str(span.name),
            duration_ms=_duration_ms(None),
        )
        for span in trace.spans
    ]

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
mutants_x__duration_ms__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__duration_ms__mutmut)
def _duration_ms(span: _TraceSpanProto) -> float:
    start = span.start_time
    end = span.end_time
    if start is None or end is None:
        return 0.0
    return round((end - start).total_seconds() * _MILLIS_PER_SECOND, 2)


def x__duration_ms__mutmut_orig(span: _TraceSpanProto) -> float:
    start = span.start_time
    end = span.end_time
    if start is None or end is None:
        return 0.0
    return round((end - start).total_seconds() * _MILLIS_PER_SECOND, 2)


def x__duration_ms__mutmut_1(span: _TraceSpanProto) -> float:
    start = None
    end = span.end_time
    if start is None or end is None:
        return 0.0
    return round((end - start).total_seconds() * _MILLIS_PER_SECOND, 2)


def x__duration_ms__mutmut_2(span: _TraceSpanProto) -> float:
    start = span.start_time
    end = None
    if start is None or end is None:
        return 0.0
    return round((end - start).total_seconds() * _MILLIS_PER_SECOND, 2)


def x__duration_ms__mutmut_3(span: _TraceSpanProto) -> float:
    start = span.start_time
    end = span.end_time
    if start is None and end is None:
        return 0.0
    return round((end - start).total_seconds() * _MILLIS_PER_SECOND, 2)


def x__duration_ms__mutmut_4(span: _TraceSpanProto) -> float:
    start = span.start_time
    end = span.end_time
    if start is not None or end is None:
        return 0.0
    return round((end - start).total_seconds() * _MILLIS_PER_SECOND, 2)


def x__duration_ms__mutmut_5(span: _TraceSpanProto) -> float:
    start = span.start_time
    end = span.end_time
    if start is None or end is not None:
        return 0.0
    return round((end - start).total_seconds() * _MILLIS_PER_SECOND, 2)


def x__duration_ms__mutmut_6(span: _TraceSpanProto) -> float:
    start = span.start_time
    end = span.end_time
    if start is None or end is None:
        return 1.0
    return round((end - start).total_seconds() * _MILLIS_PER_SECOND, 2)


def x__duration_ms__mutmut_7(span: _TraceSpanProto) -> float:
    start = span.start_time
    end = span.end_time
    if start is None or end is None:
        return 0.0
    return round(None, 2)


def x__duration_ms__mutmut_8(span: _TraceSpanProto) -> float:
    start = span.start_time
    end = span.end_time
    if start is None or end is None:
        return 0.0
    return round((end - start).total_seconds() * _MILLIS_PER_SECOND, None)


def x__duration_ms__mutmut_9(span: _TraceSpanProto) -> float:
    start = span.start_time
    end = span.end_time
    if start is None or end is None:
        return 0.0
    return round(2)


def x__duration_ms__mutmut_10(span: _TraceSpanProto) -> float:
    start = span.start_time
    end = span.end_time
    if start is None or end is None:
        return 0.0
    return round((end - start).total_seconds() * _MILLIS_PER_SECOND, )


def x__duration_ms__mutmut_11(span: _TraceSpanProto) -> float:
    start = span.start_time
    end = span.end_time
    if start is None or end is None:
        return 0.0
    return round((end - start).total_seconds() / _MILLIS_PER_SECOND, 2)


def x__duration_ms__mutmut_12(span: _TraceSpanProto) -> float:
    start = span.start_time
    end = span.end_time
    if start is None or end is None:
        return 0.0
    return round((end + start).total_seconds() * _MILLIS_PER_SECOND, 2)


def x__duration_ms__mutmut_13(span: _TraceSpanProto) -> float:
    start = span.start_time
    end = span.end_time
    if start is None or end is None:
        return 0.0
    return round((end - start).total_seconds() * _MILLIS_PER_SECOND, 3)

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
