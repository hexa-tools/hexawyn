"""Comprehensive tests for GCP Cloud Trace — target 95%+ coverage."""

from __future__ import annotations

from datetime import UTC, datetime, timedelta
from unittest.mock import MagicMock, patch

import pytest
from hexawyn.adapters.secondary.gcp.cloud_trace_adapter import (
    GCPCloudTraceAdapter,
    _as_trace_client,
    _duration_ms,
    _trace_to_spans,
)
from hexawyn.domain.models.latency_diagnostic import LatencyDiagnosticRequest


def _make_request(**kwargs: object) -> LatencyDiagnosticRequest:
    defaults: dict[str, object] = {
        "service_name": "payment-service",
        "time_window_minutes": 30,
        "threshold_ms": 500.0,
    }
    defaults.update(kwargs)
    return LatencyDiagnosticRequest(**defaults)  # type: ignore[arg-type]


class TestDurationMs:
    """Cover _duration_ms (lines 120-125)."""

    def test_with_valid_times(self) -> None:
        now = datetime.now(UTC)
        span = MagicMock()
        span.start_time = now
        span.end_time = now + timedelta(seconds=2.5)
        assert _duration_ms(span) == 2500.0  # noqa: PLR2004

    def test_with_none_start(self) -> None:
        span = MagicMock()
        span.start_time = None
        span.end_time = datetime.now(UTC)
        assert _duration_ms(span) == 0.0

    def test_with_none_end(self) -> None:
        span = MagicMock()
        span.start_time = datetime.now(UTC)
        span.end_time = None
        assert _duration_ms(span) == 0.0

    def test_with_both_none(self) -> None:
        span = MagicMock()
        span.start_time = None
        span.end_time = None
        assert _duration_ms(span) == 0.0


class TestTraceToSpans:
    """Cover _trace_to_spans (lines 108-117)."""

    def test_converts_trace(self) -> None:
        now = datetime.now(UTC)
        trace = MagicMock()
        trace.trace_id = "trace-abc"
        span1 = MagicMock()
        span1.name = "span-a"
        span1.start_time = now
        span1.end_time = now + timedelta(seconds=1)
        span2 = MagicMock()
        span2.name = "span-b"
        span2.start_time = now
        span2.end_time = now + timedelta(seconds=2)
        trace.spans = [span1, span2]

        result = _trace_to_spans(trace)
        assert len(result) == 2  # noqa: PLR2004
        assert result[0].trace_id == "trace-abc"
        assert result[0].span_name == "span-a"
        assert result[1].span_name == "span-b"

    def test_empty_spans(self) -> None:
        trace = MagicMock()
        trace.trace_id = "empty-trace"
        trace.spans = []

        result = _trace_to_spans(trace)
        assert result == []


class TestAsTraceClient:
    """Cover _as_trace_client (lines 104-105)."""

    def test_identity(self) -> None:
        client = MagicMock()
        assert _as_trace_client(client) is client


class TestGCPCloudTraceAdapter:
    """Cover all GCPCloudTraceAdapter methods."""

    def test_instantiation(self) -> None:
        adapter = GCPCloudTraceAdapter(project_id="myproj")
        assert adapter._project_id == "myproj"
        assert adapter._trace_client is None

    def test_slow_filter(self) -> None:
        adapter = GCPCloudTraceAdapter(project_id="myproj")
        result = adapter._slow_filter(_make_request())
        assert "span:payment-service" in result
        assert "500ms" in result

    def test_total_filter(self) -> None:
        adapter = GCPCloudTraceAdapter(project_id="myproj")
        result = adapter._total_filter(_make_request())
        assert result == "span:payment-service"

    def test_fetch_slow_spans(self) -> None:
        mock_trace = MagicMock()
        mock_trace.trace_id = "trace-1"
        mock_span = MagicMock()
        mock_span.name = "span-1"
        mock_span.start_time = datetime.now(UTC)
        mock_span.end_time = datetime.now(UTC) + timedelta(seconds=1)
        mock_trace.spans = [mock_span]

        adapter = GCPCloudTraceAdapter(project_id="myproj")
        with patch.object(adapter, "_list_traces", return_value=[mock_trace]):
            result = adapter.fetch_slow_spans(_make_request())
            assert len(result) == 1  # noqa: PLR2004

    def test_fetch_total_traces(self) -> None:
        mock_trace = MagicMock()
        mock_trace.spans = []

        adapter = GCPCloudTraceAdapter(project_id="myproj")
        with patch.object(adapter, "_list_traces", return_value=[mock_trace]):
            result = adapter.fetch_total_traces(_make_request())
            assert result == 1

    def test_fetch_total_traces_empty(self) -> None:
        adapter = GCPCloudTraceAdapter(project_id="myproj")
        with patch.object(adapter, "_list_traces", return_value=[]):
            result = adapter.fetch_total_traces(_make_request())
            assert result == 0

    def test_list_traces_with_injected_client(self) -> None:
        mock_client = MagicMock()
        mock_trace = MagicMock()
        mock_trace.trace_id = "t1"
        mock_trace.spans = []
        mock_client.list_traces.return_value = [mock_trace]

        adapter = GCPCloudTraceAdapter(project_id="myproj", trace_client=mock_client)
        result = adapter._list_traces("span:test", _make_request(), complete=True)
        assert len(result) == 1  # noqa: PLR2004

    def test_list_traces_no_credentials(self) -> None:
        from google.auth.exceptions import DefaultCredentialsError
        from hexawyn.domain.errors import TracesUnavailableError

        mock_client = MagicMock()
        mock_client.list_traces.side_effect = DefaultCredentialsError()

        adapter = GCPCloudTraceAdapter(project_id="myproj", trace_client=mock_client)
        with pytest.raises(TracesUnavailableError, match="credentials"):
            adapter._list_traces("span:test", _make_request(), complete=True)

    def test_list_traces_api_error(self) -> None:
        from google.api_core.exceptions import GoogleAPICallError
        from hexawyn.domain.errors import TracesUnavailableError

        mock_client = MagicMock()
        mock_client.list_traces.side_effect = GoogleAPICallError("api error")

        adapter = GCPCloudTraceAdapter(project_id="myproj", trace_client=mock_client)
        with pytest.raises(TracesUnavailableError):
            adapter._list_traces("span:test", _make_request(), complete=True)

    def test_client_or_create_lazy(self) -> None:
        adapter = GCPCloudTraceAdapter(project_id="myproj")
        assert adapter._trace_client is None
        with patch("google.cloud.trace_v1.TraceServiceClient") as mock_client:
            mock_client.return_value = MagicMock()
            result = adapter._client_or_create()
            mock_client.assert_called_once()
            assert result is not None
            assert adapter._trace_client is not None

    def test_client_or_create_reuses_cached(self) -> None:
        adapter = GCPCloudTraceAdapter(project_id="myproj")
        mock_client = MagicMock()
        adapter._trace_client = mock_client
        result = adapter._client_or_create()
        assert result is mock_client

    def test_boto3_client_not_called_when_injected(self) -> None:
        mock_client = MagicMock()
        adapter = GCPCloudTraceAdapter(project_id="myproj", trace_client=mock_client)
        with patch("google.cloud.trace_v1.TraceServiceClient") as mock_import:
            adapter._client_or_create()
            mock_import.assert_not_called()
