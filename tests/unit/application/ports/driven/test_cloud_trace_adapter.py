from datetime import UTC, datetime, timedelta
from unittest.mock import MagicMock, patch

import pytest

pytest.importorskip("google.cloud.trace_v1")
from google.api_core.exceptions import PermissionDenied  # noqa: E402
from google.auth.exceptions import DefaultCredentialsError  # noqa: E402
from hexawyn.application.ports.driven.trace_query_port import (  # noqa: E402
    LatencyDiagnosticRequest,
    TraceQueryPort,
)
from hexawyn.domain.errors import TracesUnavailableError  # noqa: E402

_PROJECT = "my-project"


def _request() -> LatencyDiagnosticRequest:
    return LatencyDiagnosticRequest(
        service_name="checkout", time_window_minutes=15, threshold_ms=500.0
    )


def _span(name: str, duration_ms: float) -> MagicMock:
    start = datetime(2026, 1, 1, tzinfo=UTC)
    span = MagicMock()
    span.name = name
    span.start_time = start
    span.end_time = start + timedelta(milliseconds=duration_ms)
    return span


def _trace(trace_id: str, spans: list[MagicMock]) -> MagicMock:
    trace = MagicMock()
    trace.trace_id = trace_id
    trace.spans = spans
    return trace


def _adapter(client: MagicMock):
    from hexawyn.adapters.secondary.gcp.cloud_trace_adapter import GCPCloudTraceAdapter

    return GCPCloudTraceAdapter(project_id=_PROJECT, trace_client=client)


class TestContract:
    def test_is_a_trace_query_port(self) -> None:
        assert isinstance(_adapter(MagicMock()), TraceQueryPort)


class TestFetchSlowSpans:
    def test_maps_traces_to_spans(self) -> None:
        client = MagicMock()
        client.list_traces.return_value = [
            _trace("t1", [_span("frontend", 1500.0), _span("db", 1200.0)])
        ]
        adapter = _adapter(client)

        result = adapter.fetch_slow_spans(_request())

        assert len(result) == 1
        names = {s.span_name: s.duration_ms for s in result[0]}
        assert names["frontend"] == 1500.0
        assert names["db"] == 1200.0
        assert all(s.trace_id == "t1" for s in result[0])

    def test_returns_empty_when_no_traces(self) -> None:
        client = MagicMock()
        client.list_traces.return_value = []
        adapter = _adapter(client)

        assert adapter.fetch_slow_spans(_request()) == []

    def test_filter_includes_service_and_latency(self) -> None:
        client = MagicMock()
        client.list_traces.return_value = []
        adapter = _adapter(client)

        adapter.fetch_slow_spans(_request())

        request = client.list_traces.call_args.kwargs["request"]
        assert "checkout" in request.filter
        assert "500" in request.filter
        assert request.project_id == _PROJECT

    def test_span_without_timestamps_defaults_to_zero(self) -> None:
        client = MagicMock()
        span = MagicMock()
        span.name = "no-timing"
        span.start_time = None
        span.end_time = None
        client.list_traces.return_value = [_trace("t1", [span])]
        adapter = _adapter(client)

        result = adapter.fetch_slow_spans(_request())

        assert result[0][0].duration_ms == 0.0


class TestFetchTotalTraces:
    def test_counts_traces_without_latency_filter(self) -> None:
        client = MagicMock()
        client.list_traces.return_value = [_trace("t1", []), _trace("t2", [])]
        adapter = _adapter(client)

        total = adapter.fetch_total_traces(_request())

        assert total == 2
        request = client.list_traces.call_args.kwargs["request"]
        assert "latency" not in request.filter


class TestErrorTranslation:
    def test_missing_credentials(self) -> None:
        client = MagicMock()
        client.list_traces.side_effect = DefaultCredentialsError("no creds")
        adapter = _adapter(client)

        with pytest.raises(TracesUnavailableError) as exc_info:
            adapter.fetch_slow_spans(_request())

        assert "gcloud auth" in str(exc_info.value).lower()

    def test_api_error(self) -> None:
        client = MagicMock()
        client.list_traces.side_effect = PermissionDenied("denied")
        adapter = _adapter(client)

        with pytest.raises(TracesUnavailableError):
            adapter.fetch_total_traces(_request())


class TestLazyClientCreation:
    def test_lazily_creates_client(self) -> None:
        from hexawyn.adapters.secondary.gcp.cloud_trace_adapter import GCPCloudTraceAdapter

        created = MagicMock()
        created.list_traces.return_value = []
        adapter = GCPCloudTraceAdapter(project_id=_PROJECT)

        with patch("google.cloud.trace_v1.TraceServiceClient", return_value=created) as client_cls:
            adapter.fetch_total_traces(_request())

        client_cls.assert_called_once_with()
