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


class DatadogTracesAdapter(TraceQueryPort):
    """TraceQueryPort backed by Datadog APM (Spans API).

    Reads slow spans and groups them by trace, natively — no Tempo/Jaeger.
    """

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

    def fetch_total_traces(self, request: LatencyDiagnosticRequest) -> int:
        data = self._list_spans(self._total_filter(request), request.time_window_minutes)
        return len({span.attributes.trace_id for span in data})

    def _slow_filter(self, request: LatencyDiagnosticRequest) -> str:
        threshold = int(request.threshold_ms)
        return f"service:{request.service_name} @duration:>{threshold}ms"

    def _total_filter(self, request: LatencyDiagnosticRequest) -> str:
        return f"service:{request.service_name}"

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

    def _api(self) -> SpansApi:
        if self._spans_api is None:
            self._spans_api = _build_spans_api(self._key, self._app_key, self._site)
        return self._spans_api


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


def _as_float(value: object) -> float:
    if isinstance(value, int | float):
        return float(value)
    try:
        return float(str(value))
    except (TypeError, ValueError):
        return 0.0


def _build_spans_api(key: str, app_key: str, site: str) -> SpansApi:
    from datadog_api_client import ApiClient, Configuration
    from datadog_api_client.v2.api.spans_api import SpansApi as DatadogSpansApi

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = key
    configuration.api_key["appKeyAuth"] = app_key
    configuration.server_variables["site"] = site
    return cast(SpansApi, DatadogSpansApi(ApiClient(configuration)))
