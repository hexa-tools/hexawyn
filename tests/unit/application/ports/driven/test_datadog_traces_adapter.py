from unittest.mock import MagicMock, patch

import pytest

pytest.importorskip("datadog_api_client")
from datadog_api_client.exceptions import ApiException  # noqa: E402
from hexawyn.application.ports.driven.trace_query_port import (  # noqa: E402
    LatencyDiagnosticRequest,
    TraceQueryPort,
)
from hexawyn.domain.errors import (  # noqa: E402
    AdapterTimeoutError,
    InsufficientPermissionsError,
    TracesUnavailableError,
)


def _request() -> LatencyDiagnosticRequest:
    return LatencyDiagnosticRequest(
        service_name="checkout", time_window_minutes=15, threshold_ms=500.0
    )


def _span(trace_id: str = "t1", name: str = "GET /pay", duration: float = 1500.0) -> MagicMock:
    attrs = type("Attrs", (), {})()
    attrs.trace_id = trace_id
    attrs.operation_name = name
    attrs.duration = duration
    span = MagicMock()
    span.id = "s1"
    span.attributes = attrs
    return span


def _response(spans: list[MagicMock]) -> MagicMock:
    resp = MagicMock()
    resp.data = spans
    return resp


def _adapter(api: MagicMock):
    from hexawyn.adapters.secondary.datadog.datadog_traces_adapter import (
        DatadogTracesAdapter,
    )

    return DatadogTracesAdapter(spans_api=api)


class TestContract:
    def test_is_a_trace_query_port(self) -> None:
        assert isinstance(_adapter(MagicMock()), TraceQueryPort)


class TestFetchSlowSpans:
    def test_groups_spans_by_trace_id(self) -> None:
        api = MagicMock()
        api.list_spans.return_value = _response(
            [
                _span("t1", "GET /pay", 1500.0),
                _span("t1", "SELECT db", 1200.0),
                _span("t2", "GET /cart", 900.0),
            ]
        )
        adapter = _adapter(api)

        result = adapter.fetch_slow_spans(_request())

        assert len(result) == 2
        op1 = next(spans for spans in result if spans[0].trace_id == "t1")
        names = {s.span_name: s.duration_ms for s in op1}
        assert names["GET /pay"] == 1500.0
        assert names["SELECT db"] == 1200.0

    def test_returns_empty_when_no_data(self) -> None:
        api = MagicMock()
        api.list_spans.return_value = _response([])
        adapter = _adapter(api)

        assert adapter.fetch_slow_spans(_request()) == []

    def test_returns_zero_total_when_no_data(self) -> None:
        api = MagicMock()
        api.list_spans.return_value = _response([])
        adapter = _adapter(api)

        assert adapter.fetch_total_traces(_request()) == 0

    def test_non_numeric_duration_defaults_to_zero(self) -> None:
        api = MagicMock()
        attrs = type("Attrs", (), {})()
        attrs.trace_id = "t1"
        attrs.operation_name = "weird"
        attrs.duration = "n/a"
        span = MagicMock()
        span.id = "s1"
        span.attributes = attrs
        api.list_spans.return_value = _response([span])
        adapter = _adapter(api)

        result = adapter.fetch_slow_spans(_request())

        assert result[0][0].duration_ms == 0.0

    def test_filter_includes_service_and_duration(self) -> None:
        api = MagicMock()
        api.list_spans.return_value = _response([])
        adapter = _adapter(api)

        adapter.fetch_slow_spans(_request())

        body = api.list_spans.call_args.kwargs["body"]
        query = body.data.attributes.filter.query
        assert "checkout" in query
        assert "500" in query


class TestFetchTotalTraces:
    def test_counts_distinct_trace_ids(self) -> None:
        api = MagicMock()
        api.list_spans.return_value = _response([_span("t1", ""), _span("t1", ""), _span("t2", "")])
        adapter = _adapter(api)

        assert adapter.fetch_total_traces(_request()) == 2


class TestErrorTranslation:
    def test_rate_limit_raises_adapter_timeout(self) -> None:
        api = MagicMock()
        api.list_spans.side_effect = ApiException(status=429)
        adapter = _adapter(api)

        with pytest.raises(AdapterTimeoutError):
            adapter.fetch_slow_spans(_request())

    def test_forbidden_raises_insufficient_permissions(self) -> None:
        api = MagicMock()
        api.list_spans.side_effect = ApiException(status=403)
        adapter = _adapter(api)

        with pytest.raises(InsufficientPermissionsError):
            adapter.fetch_total_traces(_request())

    def test_other_error_raises_traces_unavailable(self) -> None:
        api = MagicMock()
        api.list_spans.side_effect = ApiException(status=500)
        adapter = _adapter(api)

        with pytest.raises(TracesUnavailableError):
            adapter.fetch_total_traces(_request())


class TestHelpers:
    def test_build_spans_api_constructs_config(self) -> None:
        from hexawyn.adapters.secondary.datadog.datadog_traces_adapter import _build_spans_api

        cfg_data: dict[str, str] = {}
        cfg_mock = MagicMock()
        cfg_mock.api_key = cfg_data
        cfg_mock.server_variables = {}

        with (
            patch("datadog_api_client.Configuration", return_value=cfg_mock),
            patch("datadog_api_client.ApiClient"),
            patch("datadog_api_client.v2.api.spans_api.SpansApi"),
        ):
            _build_spans_api("k", "a", "datadoghq.eu")

        assert cfg_data["apiKeyAuth"] == "k"
        assert cfg_data["appKeyAuth"] == "a"
        assert cfg_mock.server_variables["site"] == "datadoghq.eu"


class TestLazyApiCreation:
    def test_lazily_builds_spans_api(self) -> None:
        from hexawyn.adapters.secondary.datadog import datadog_traces_adapter as module
        from hexawyn.adapters.secondary.datadog.datadog_traces_adapter import (
            DatadogTracesAdapter,
        )

        created_api = MagicMock()
        created_api.list_spans.return_value = _response([])
        adapter = DatadogTracesAdapter(key="k", app_key="a", site="datadoghq.com")

        with patch.object(module, "_build_spans_api", return_value=created_api) as build:
            adapter.fetch_total_traces(_request())

        build.assert_called_once_with("k", "a", "datadoghq.com")
