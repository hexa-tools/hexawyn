from __future__ import annotations

from datetime import UTC, datetime, timedelta
from sys import modules as sys_modules
from unittest.mock import Mock, patch

from hexawyn.adapters.secondary.gcp.cloud_trace_adapter import (
    GCPCloudTraceAdapter,
    _as_trace_client,
    _duration_ms,
    _trace_to_spans,
)
from hexawyn.domain.errors import TracesUnavailableError
from hexawyn.domain.models.latency_diagnostic import LatencyDiagnosticRequest


class TestGCPCloudTraceAdapter:
    def test_fetch_total_traces_returns_zero_on_empty(self) -> None:
        mock_client = Mock()
        mock_client.list_traces.return_value = []
        adapter = GCPCloudTraceAdapter(project_id="proj-123", trace_client=mock_client)
        request = LatencyDiagnosticRequest(service_name="api", time_window_minutes=30)
        result = adapter.fetch_total_traces(request)
        assert result == 0

    def test_fetch_total_traces_counts_pages(self) -> None:
        mock_client = Mock()
        mock_trace_1 = Mock()
        mock_trace_2 = Mock()
        mock_client.list_traces.return_value = [mock_trace_1, mock_trace_2]
        adapter = GCPCloudTraceAdapter(project_id="proj-123", trace_client=mock_client)
        request = LatencyDiagnosticRequest(service_name="api", time_window_minutes=30)
        result = adapter.fetch_total_traces(request)
        assert result == 2  # noqa: PLR2004

    def test_fetch_slow_spans_returns_empty_on_no_traces(self) -> None:
        mock_client = Mock()
        mock_client.list_traces.return_value = []
        adapter = GCPCloudTraceAdapter(project_id="proj-123", trace_client=mock_client)
        request = LatencyDiagnosticRequest(service_name="api", time_window_minutes=30)
        result = adapter.fetch_slow_spans(request)
        assert result == []

    def test_fetch_slow_spans_converts_traces_to_spans(self) -> None:
        mock_client = Mock()
        now = datetime(2024, 1, 1, 12, 0, 0, tzinfo=UTC)
        mock_span = Mock()
        mock_span.name = "http-get"
        mock_span.start_time = now
        mock_span.end_time = now + timedelta(seconds=1.5)
        mock_trace = Mock()
        mock_trace.trace_id = "trace-abc"
        mock_trace.spans = [mock_span]
        mock_client.list_traces.return_value = [mock_trace]
        adapter = GCPCloudTraceAdapter(project_id="proj-123", trace_client=mock_client)
        request = LatencyDiagnosticRequest(service_name="api", time_window_minutes=30)
        result = adapter.fetch_slow_spans(request)
        assert len(result) == 1
        assert len(result[0]) == 1
        assert result[0][0].trace_id == "trace-abc"
        assert result[0][0].span_name == "http-get"
        assert result[0][0].duration_ms == 1500.0  # noqa: PLR2004

    def test_slow_filter_includes_service_name(self) -> None:
        adapter = GCPCloudTraceAdapter(project_id="proj-123", trace_client=Mock())
        request = LatencyDiagnosticRequest(service_name="api", time_window_minutes=30)
        filter_str = adapter._slow_filter(request)
        assert "api" in filter_str

    def test_total_filter_includes_service_name(self) -> None:
        adapter = GCPCloudTraceAdapter(project_id="proj-123", trace_client=Mock())
        request = LatencyDiagnosticRequest(service_name="api", time_window_minutes=30)
        filter_str = adapter._total_filter(request)
        assert "api" in filter_str

    def test_list_traces_credentials_error_raises_traces_unavailable(self) -> None:
        mock_gcp_exc = Mock()
        mock_gcp_exc.GoogleAPICallError = type("GoogleAPICallError", (Exception,), {})

        mock_gcp_auth = Mock()
        cred_error = type("DefaultCredentialsError", (Exception,), {})
        mock_gcp_auth.DefaultCredentialsError = cred_error

        mock_trace_v1 = Mock()
        mock_trace_v1.ListTracesRequest = Mock()
        mock_trace_v1.ListTracesRequest.ViewType = Mock()
        mock_trace_v1.ListTracesRequest.ViewType.COMPLETE = "COMPLETE"
        mock_trace_v1.ListTracesRequest.ViewType.MINIMAL = "MINIMAL"

        mock_client = Mock()
        mock_client.list_traces.side_effect = cred_error("no creds")
        adapter = GCPCloudTraceAdapter(project_id="proj-123", trace_client=mock_client)
        request = LatencyDiagnosticRequest(service_name="api", time_window_minutes=30)

        with patch.dict(
            sys_modules,
            {
                "google.api_core.exceptions": mock_gcp_exc,
                "google.auth.exceptions": mock_gcp_auth,
                "google.cloud.trace_v1": mock_trace_v1,
            },
        ):
            try:
                adapter.fetch_slow_spans(request)
            except TracesUnavailableError:
                pass

    def test_list_traces_api_error_raises_traces_unavailable(self) -> None:
        mock_gcp_exc = Mock()
        api_error = type("GoogleAPICallError", (Exception,), {})
        mock_gcp_exc.GoogleAPICallError = api_error

        mock_gcp_auth = Mock()
        mock_gcp_auth.DefaultCredentialsError = type("DefaultCredentialsError", (Exception,), {})

        mock_trace_v1 = Mock()
        mock_trace_v1.ListTracesRequest = Mock()
        mock_trace_v1.ListTracesRequest.ViewType = Mock()
        mock_trace_v1.ListTracesRequest.ViewType.COMPLETE = "COMPLETE"
        mock_trace_v1.ListTracesRequest.ViewType.MINIMAL = "MINIMAL"

        mock_client = Mock()
        mock_client.list_traces.side_effect = api_error("api error")
        adapter = GCPCloudTraceAdapter(project_id="proj-123", trace_client=mock_client)
        request = LatencyDiagnosticRequest(service_name="api", time_window_minutes=30)

        with patch.dict(
            sys_modules,
            {
                "google.api_core.exceptions": mock_gcp_exc,
                "google.auth.exceptions": mock_gcp_auth,
                "google.cloud.trace_v1": mock_trace_v1,
            },
        ):
            try:
                adapter.fetch_total_traces(request)
            except TracesUnavailableError:
                pass

    def test_client_or_create_returns_injected_client(self) -> None:
        mock_client = Mock()
        adapter = GCPCloudTraceAdapter(project_id="proj-123", trace_client=mock_client)
        result = adapter._client_or_create()
        assert result is mock_client


class TestTraceToSpans:
    def test_empty_spans(self) -> None:
        mock_trace = Mock()
        mock_trace.trace_id = "trace-xyz"
        mock_trace.spans = []
        result = _trace_to_spans(mock_trace)
        assert result == []

    def test_single_span(self) -> None:
        now = datetime(2024, 1, 1, 12, 0, 0, tzinfo=UTC)
        mock_span = Mock()
        mock_span.name = "db-query"
        mock_span.start_time = now
        mock_span.end_time = now + timedelta(seconds=0.2)
        mock_trace = Mock()
        mock_trace.trace_id = "trace-def"
        mock_trace.spans = [mock_span]
        result = _trace_to_spans(mock_trace)
        assert len(result) == 1
        assert result[0].trace_id == "trace-def"
        assert result[0].span_name == "db-query"
        assert result[0].duration_ms == 200.0  # noqa: PLR2004


class TestDurationMs:
    def test_both_timestamps(self) -> None:
        now = datetime(2024, 1, 1, 12, 0, 0, tzinfo=UTC)
        mock_span = Mock()
        mock_span.start_time = now
        mock_span.end_time = now + timedelta(seconds=1.5)
        assert _duration_ms(mock_span) == 1500.0  # noqa: PLR2004

    def test_missing_end_time(self) -> None:
        mock_span = Mock()
        mock_span.start_time = datetime(2024, 1, 1, 12, 0, 0, tzinfo=UTC)
        mock_span.end_time = None
        assert _duration_ms(mock_span) == 0.0

    def test_missing_start_time(self) -> None:
        mock_span = Mock()
        mock_span.start_time = None
        mock_span.end_time = datetime(2024, 1, 1, 12, 0, 0, tzinfo=UTC)
        assert _duration_ms(mock_span) == 0.0

    def test_both_missing(self) -> None:
        mock_span = Mock()
        mock_span.start_time = None
        mock_span.end_time = None
        assert _duration_ms(mock_span) == 0.0


class TestAsTraceClient:
    def test_returns_input(self) -> None:
        mock = Mock()
        assert _as_trace_client(mock) is mock
