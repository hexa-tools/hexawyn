from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from botocore.exceptions import ClientError, NoCredentialsError
from hexawyn.adapters.secondary.aws.xray_trace_adapter import (
    AWSXRayTraceAdapter,
    _chunked,
    _duration_ms,
    _trace_to_spans,
    _walk_document,
)
from hexawyn.domain.errors import TracesUnavailableError
from hexawyn.domain.models.latency_diagnostic import LatencyDiagnosticRequest, TraceSpan


class TestAWSXRayTraceAdapter:
    @staticmethod
    def _adapter(
        region: str | None = "us-east-1",
        xray_client: object | None = None,
    ) -> AWSXRayTraceAdapter:
        return AWSXRayTraceAdapter(region=region, xray_client=xray_client)

    @staticmethod
    def _request(
        service_name: str = "test-service",
        time_window_minutes: int = 30,
        threshold_ms: float = 500.0,
    ) -> LatencyDiagnosticRequest:
        return LatencyDiagnosticRequest(
            service_name=service_name,
            time_window_minutes=time_window_minutes,
            threshold_ms=threshold_ms,
        )

    def test_fetch_total_traces_empty_returns_zero(self) -> None:
        mock_client = MagicMock()
        mock_client.get_trace_summaries.return_value = {"TraceSummaries": []}
        adapter = self._adapter(xray_client=mock_client)

        result = adapter.fetch_total_traces(self._request())

        assert result == 0  # noqa: PLR2004

    def test_fetch_total_traces_counts_summaries(self) -> None:
        mock_client = MagicMock()
        mock_client.get_trace_summaries.return_value = {
            "TraceSummaries": [
                {"Id": "trace-1", "Duration": 1.0},
                {"Id": "trace-2", "Duration": 2.0},
            ]
        }
        adapter = self._adapter(xray_client=mock_client)

        result = adapter.fetch_total_traces(self._request())

        assert result == 2  # noqa: PLR2004

    def test_fetch_slow_spans_empty_summaries_returns_empty(self) -> None:
        mock_client = MagicMock()
        mock_client.get_trace_summaries.return_value = {"TraceSummaries": []}
        adapter = self._adapter(xray_client=mock_client)

        result = adapter.fetch_slow_spans(self._request())

        assert result == []

    def test_fetch_slow_spans_with_data_returns_spans(self) -> None:
        mock_client = MagicMock()
        mock_client.get_trace_summaries.return_value = {
            "TraceSummaries": [
                {"Id": "trace-abc", "Duration": 2.5},
            ]
        }
        segment_doc = '{"name": "http-get", "start_time": 1.0, "end_time": 1.5, "subsegments": []}'
        mock_client.batch_get_traces.return_value = {
            "Traces": [
                {
                    "Id": "trace-abc",
                    "Segments": [{"Id": "seg-1", "Document": segment_doc}],
                }
            ]
        }
        adapter = self._adapter(xray_client=mock_client)

        result = adapter.fetch_slow_spans(self._request())

        assert len(result) == 1  # noqa: PLR2004
        assert len(result[0]) == 1  # noqa: PLR2004
        assert result[0][0].trace_id == "trace-abc"
        assert result[0][0].span_name == "http-get"

    def test_fetch_slow_spans_without_id_skips(self) -> None:
        mock_client = MagicMock()
        mock_client.get_trace_summaries.return_value = {
            "TraceSummaries": [
                {"Duration": 2.5},
            ]
        }
        adapter = self._adapter(xray_client=mock_client)

        result = adapter.fetch_slow_spans(self._request())

        assert result == []

    def test_no_credentials_raises_traces_unavailable(self) -> None:
        mock_client = MagicMock()
        mock_client.get_trace_summaries.side_effect = NoCredentialsError()
        adapter = self._adapter(xray_client=mock_client)

        with pytest.raises(TracesUnavailableError, match="credentials"):
            adapter.fetch_slow_spans(self._request())

    def test_client_error_raises_traces_unavailable(self) -> None:
        mock_client = MagicMock()
        error_response = {"Error": {"Code": "Throttling", "Message": "too fast"}}
        mock_client.get_trace_summaries.side_effect = ClientError(
            error_response, "GetTraceSummaries"
        )
        adapter = self._adapter(xray_client=mock_client)

        with pytest.raises(TracesUnavailableError, match="X-Ray"):
            adapter.fetch_total_traces(self._request())

    def test_paginated_summaries_aggregates_all_pages(self) -> None:
        mock_client = MagicMock()
        call_count = [0]

        def _side_effect(**kwargs: object) -> dict[str, object]:
            call_count[0] += 1
            if call_count[0] == 1:
                return {
                    "TraceSummaries": [{"Id": "trace-1", "Duration": 1.0}],
                    "NextToken": "page-2",
                }
            return {"TraceSummaries": [{"Id": "trace-2", "Duration": 2.0}]}

        mock_client.get_trace_summaries.side_effect = _side_effect
        adapter = self._adapter(xray_client=mock_client)

        result = adapter.fetch_total_traces(self._request())

        assert result == 2  # noqa: PLR2004

    def test_slow_filter_includes_service_name_and_threshold(self) -> None:
        adapter = self._adapter()
        request = LatencyDiagnosticRequest(
            service_name="my-api", time_window_minutes=30, threshold_ms=1000.0
        )

        filter_str = adapter._slow_filter(request)

        assert "my-api" in filter_str
        assert "responsetime > 1.0" in filter_str

    def test_total_filter_includes_service_name(self) -> None:
        adapter = self._adapter()
        request = LatencyDiagnosticRequest(service_name="my-api", time_window_minutes=30)

        filter_str = adapter._total_filter(request)

        assert "my-api" in filter_str

    def test_client_or_create_returns_injected_client(self) -> None:
        mock_client = MagicMock()
        adapter = self._adapter(xray_client=mock_client)

        result = adapter._client_or_create()

        assert result is mock_client

    def test_fetch_slow_spans_batches_trace_ids(self) -> None:
        mock_client = MagicMock()
        mock_client.get_trace_summaries.return_value = {
            "TraceSummaries": [{"Id": f"trace-{i}", "Duration": float(i)} for i in range(7)]
        }
        mock_client.batch_get_traces.return_value = {"Traces": []}
        adapter = self._adapter(xray_client=mock_client)

        adapter.fetch_slow_spans(self._request())

        assert mock_client.batch_get_traces.call_count == 2  # noqa: PLR2004


class TestChunked:
    def test_chunks_list(self) -> None:
        items = ["a", "b", "c", "d", "e"]
        assert _chunked(items, 2) == [["a", "b"], ["c", "d"], ["e"]]

    def test_empty_list(self) -> None:
        assert _chunked([], 3) == []

    def test_exact_divisor(self) -> None:
        assert _chunked(["a", "b", "c", "d"], 2) == [["a", "b"], ["c", "d"]]


class TestDurationMs:
    def test_computes_from_start_and_end(self) -> None:
        node: dict[str, object] = {"start_time": 1.5, "end_time": 2.0}
        assert _duration_ms(node) == 500.0  # noqa: PLR2004

    def test_returns_zero_when_missing_start(self) -> None:
        node: dict[str, object] = {"end_time": 2.0}
        assert _duration_ms(node) == 0.0  # noqa: PLR2004

    def test_returns_zero_when_missing_end(self) -> None:
        node: dict[str, object] = {"start_time": 1.0}
        assert _duration_ms(node) == 0.0  # noqa: PLR2004

    def test_returns_zero_when_non_numeric(self) -> None:
        node: dict[str, object] = {"start_time": "abc", "end_time": "def"}
        assert _duration_ms(node) == 0.0  # noqa: PLR2004


class TestTraceToSpans:
    def test_empty_trace_returns_empty(self) -> None:
        trace = {"Id": "trace-1"}
        assert _trace_to_spans(trace) == []

    def test_ignores_segments_without_document(self) -> None:
        trace = {
            "Id": "trace-1",
            "Segments": [{"Id": "seg-1"}],
        }
        assert _trace_to_spans(trace) == []

    def test_parses_document_into_spans(self) -> None:
        trace = {
            "Id": "trace-1",
            "Segments": [
                {
                    "Id": "seg-1",
                    "Document": '{"name": "http-get", "start_time": 1.0, "end_time": 1.5}',
                }
            ],
        }
        spans = _trace_to_spans(trace)
        assert len(spans) == 1  # noqa: PLR2004
        assert spans[0].trace_id == "trace-1"
        assert spans[0].span_name == "http-get"
        assert spans[0].duration_ms == 500.0  # noqa: PLR2004


class TestWalkDocument:
    def test_appends_single_node(self) -> None:
        doc: dict[str, object] = {"name": "root", "start_time": 1.0, "end_time": 2.0}
        spans: list[TraceSpan] = []
        _walk_document("trace-1", doc, spans)
        assert len(spans) == 1  # noqa: PLR2004
        assert spans[0].span_name == "root"

    def test_walks_subsegments(self) -> None:
        doc: dict[str, object] = {
            "name": "root",
            "start_time": 1.0,
            "end_time": 2.0,
            "subsegments": [
                {"name": "child", "start_time": 1.1, "end_time": 1.3},
            ],
        }
        spans: list[TraceSpan] = []
        _walk_document("trace-1", doc, spans)
        assert len(spans) == 2  # noqa: PLR2004
        assert {s.span_name for s in spans} == {"root", "child"}

    def test_skips_non_dict_subsegments(self) -> None:
        doc: dict[str, object] = {
            "name": "root",
            "start_time": 1.0,
            "end_time": 2.0,
            "subsegments": ["not-a-dict"],
        }
        spans: list[TraceSpan] = []
        _walk_document("trace-1", doc, spans)
        assert len(spans) == 1  # noqa: PLR2004

    def test_missing_name_defaults_to_unknown(self) -> None:
        doc: dict[str, object] = {"start_time": 1.0, "end_time": 2.0}
        spans: list[TraceSpan] = []
        _walk_document("trace-1", doc, spans)
        assert spans[0].span_name == "unknown"
