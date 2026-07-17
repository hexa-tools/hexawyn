import json
from unittest.mock import MagicMock, patch

import pytest

boto3 = pytest.importorskip("boto3")
from botocore.exceptions import (  # noqa: E402
    ClientError,
    EndpointConnectionError,
    NoCredentialsError,
)
from hexawyn.application.ports.driven.trace_query_port import (  # noqa: E402
    LatencyDiagnosticRequest,
    TraceQueryPort,
)
from hexawyn.domain.errors import TracesUnavailableError  # noqa: E402


def _summary(trace_id: str, duration: float = 1.0) -> dict:
    return {"Id": trace_id, "Duration": duration}


def _segment(document: dict) -> dict:
    return {"Id": "seg", "Document": json.dumps(document)}


def _request() -> LatencyDiagnosticRequest:
    return LatencyDiagnosticRequest(
        service_name="checkout", time_window_minutes=15, threshold_ms=500.0
    )


def _adapter(client: MagicMock):
    from hexawyn.adapters.secondary.aws.xray_trace_adapter import AWSXRayTraceAdapter

    return AWSXRayTraceAdapter(region="eu-west-1", xray_client=client)


class TestContract:
    def test_is_a_trace_query_port(self) -> None:
        assert isinstance(_adapter(MagicMock()), TraceQueryPort)


class TestFetchSlowSpans:
    def test_parses_segments_and_subsegments_into_spans(self) -> None:
        client = MagicMock()
        client.get_trace_summaries.return_value = {"TraceSummaries": [_summary("t1")]}
        client.batch_get_traces.return_value = {
            "Traces": [
                {
                    "Id": "t1",
                    "Segments": [
                        _segment(
                            {
                                "name": "frontend",
                                "start_time": 0.0,
                                "end_time": 1.5,
                                "subsegments": [{"name": "db", "start_time": 0.2, "end_time": 1.4}],
                            }
                        )
                    ],
                }
            ]
        }
        adapter = _adapter(client)

        result = adapter.fetch_slow_spans(_request())

        assert len(result) == 1
        spans = result[0]
        names = {s.span_name: s.duration_ms for s in spans}
        assert names["frontend"] == 1500.0
        assert names["db"] == 1200.0
        for span in spans:
            assert span.trace_id == "t1"

    def test_returns_empty_when_no_slow_traces(self) -> None:
        client = MagicMock()
        client.get_trace_summaries.return_value = {"TraceSummaries": []}
        adapter = _adapter(client)

        result = adapter.fetch_slow_spans(_request())

        assert result == []
        client.batch_get_traces.assert_not_called()

    def test_span_without_timestamps_defaults_to_zero_duration(self) -> None:
        client = MagicMock()
        client.get_trace_summaries.return_value = {"TraceSummaries": [_summary("t1")]}
        client.batch_get_traces.return_value = {
            "Traces": [{"Id": "t1", "Segments": [_segment({"name": "no-timing"})]}]
        }
        adapter = _adapter(client)

        result = adapter.fetch_slow_spans(_request())

        assert result[0][0].span_name == "no-timing"
        assert result[0][0].duration_ms == 0.0

    def test_filter_expression_includes_service_and_threshold(self) -> None:
        client = MagicMock()
        client.get_trace_summaries.return_value = {"TraceSummaries": []}
        adapter = _adapter(client)

        adapter.fetch_slow_spans(_request())

        filter_expr = client.get_trace_summaries.call_args.kwargs["FilterExpression"]
        assert 'service("checkout")' in filter_expr
        assert "responsetime > 0.5" in filter_expr

    def test_paginates_trace_summaries(self) -> None:
        client = MagicMock()
        client.get_trace_summaries.side_effect = [
            {"TraceSummaries": [_summary("t1")], "NextToken": "next"},
            {"TraceSummaries": [_summary("t2")]},
        ]
        client.batch_get_traces.return_value = {"Traces": []}
        adapter = _adapter(client)

        adapter.fetch_slow_spans(_request())

        assert client.get_trace_summaries.call_count == 2
        ids = client.batch_get_traces.call_args.kwargs["TraceIds"]
        assert ids == ["t1", "t2"]

    def test_batches_trace_ids_by_five(self) -> None:
        client = MagicMock()
        client.get_trace_summaries.return_value = {
            "TraceSummaries": [_summary(f"t{i}") for i in range(6)]
        }
        client.batch_get_traces.side_effect = [
            {"Traces": []},
            {"Traces": []},
        ]
        adapter = _adapter(client)

        adapter.fetch_slow_spans(_request())

        assert client.batch_get_traces.call_count == 2
        first = client.batch_get_traces.call_args_list[0].kwargs["TraceIds"]
        second = client.batch_get_traces.call_args_list[1].kwargs["TraceIds"]
        assert len(first) == 5
        assert len(second) == 1


class TestFetchTotalTraces:
    def test_counts_summaries_without_threshold(self) -> None:
        client = MagicMock()
        client.get_trace_summaries.return_value = {
            "TraceSummaries": [_summary("t1"), _summary("t2"), _summary("t3")]
        }
        adapter = _adapter(client)

        total = adapter.fetch_total_traces(_request())

        assert total == 3
        filter_expr = client.get_trace_summaries.call_args.kwargs["FilterExpression"]
        assert "responsetime" not in filter_expr


class TestErrorTranslation:
    def test_missing_credentials(self) -> None:
        client = MagicMock()
        client.get_trace_summaries.side_effect = NoCredentialsError()
        adapter = _adapter(client)

        with pytest.raises(TracesUnavailableError) as exc_info:
            adapter.fetch_slow_spans(_request())

        assert "aws configure" in str(exc_info.value).lower()

    def test_client_error(self) -> None:
        client = MagicMock()
        client.get_trace_summaries.side_effect = ClientError(
            {"Error": {"Code": "AccessDenied", "Message": "no"}}, "GetTraceSummaries"
        )
        adapter = _adapter(client)

        with pytest.raises(TracesUnavailableError):
            adapter.fetch_total_traces(_request())

    def test_endpoint_connection_error(self) -> None:
        client = MagicMock()
        client.get_trace_summaries.side_effect = EndpointConnectionError(
            endpoint_url="https://xray.eu-west-1.amazonaws.com"
        )
        adapter = _adapter(client)

        with pytest.raises(TracesUnavailableError):
            adapter.fetch_slow_spans(_request())


class TestLazyClientCreation:
    def test_lazily_creates_boto3_client(self) -> None:
        from hexawyn.adapters.secondary.aws.xray_trace_adapter import AWSXRayTraceAdapter

        created = MagicMock()
        created.get_trace_summaries.return_value = {"TraceSummaries": []}
        adapter = AWSXRayTraceAdapter(region="eu-west-1")

        with patch.object(boto3, "client", return_value=created) as mock_client:
            adapter.fetch_total_traces(_request())

        mock_client.assert_called_once_with("xray", region_name="eu-west-1")
