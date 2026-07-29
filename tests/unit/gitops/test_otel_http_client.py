from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.adapters.secondary.gitops.otel_http_client import (
    get_jaeger_dependencies,
    get_jaeger_trace,
    list_jaeger_operations,
    list_jaeger_services,
    query_prometheus_instant,
    query_prometheus_range,
    search_jaeger_traces,
)


class TestListJaegerServices:
    def test_returns_list_with_data(self) -> None:
        with patch("httpx.get") as m:
            m.return_value = MagicMock(
                status_code=200,
                json=lambda: {"data": ["hotrod", "jaeger-query"], "total": 2},
            )
            result = list_jaeger_services()
            assert result == ["hotrod", "jaeger-query"]

    def test_returns_empty_on_error(self) -> None:
        with patch("httpx.get", side_effect=Exception("timeout")):
            assert list_jaeger_services() == []

    def test_returns_empty_on_non_list_data(self) -> None:
        with patch("httpx.get") as m:
            m.return_value = MagicMock(
                status_code=200,
                json=lambda: {"data": None, "total": 0},
            )
            assert list_jaeger_services() == []


class TestListJaegerOperations:
    def test_returns_string_list(self) -> None:
        with patch("httpx.get") as m:
            m.return_value = MagicMock(
                status_code=200,
                json=lambda: {
                    "data": ["GET /api", "POST /api"],
                    "total": 2,
                },
            )
            result = list_jaeger_operations("hotrod")
            assert result == ["GET /api", "POST /api"]

    def test_returns_dict_list(self) -> None:
        with patch("httpx.get") as m:
            m.return_value = MagicMock(
                status_code=200,
                json=lambda: {
                    "data": [{"name": "GET /api"}, {"name": "POST /api"}],
                    "total": 2,
                },
            )
            result = list_jaeger_operations("hotrod")
            assert result == ["GET /api", "POST /api"]

    def test_returns_empty_on_error(self) -> None:
        with patch("httpx.get", side_effect=Exception("timeout")):
            assert list_jaeger_operations("hotrod") == []

    def test_returns_empty_on_non_list_data(self) -> None:
        with patch("httpx.get") as m:
            m.return_value = MagicMock(
                status_code=200,
                json=lambda: {"data": None},
            )
            assert list_jaeger_operations("hotrod") == []


class TestSearchJaegerTraces:
    def test_returns_summaries(self) -> None:
        with patch("httpx.get") as m:
            m.return_value = MagicMock(
                status_code=200,
                json=lambda: {
                    "data": [
                        {
                            "traceID": "abc123",
                            "spans": [
                                {"duration": 5000, "tags": []},
                                {"duration": 3000, "tags": [{"key": "error", "value": True}]},
                            ],
                            "processes": {},
                        }
                    ],
                    "total": 1,
                },
            )
            traces = search_jaeger_traces("hotrod")
            assert len(traces) == 1  # noqa: PLR2004
            assert traces[0]["traceID"] == "abc123"
            assert traces[0]["hasErrors"] is True

    def test_returns_empty_on_error(self) -> None:
        with patch("httpx.get", side_effect=Exception("timeout")):
            assert search_jaeger_traces("hotrod") == []

    def test_returns_empty_on_non_list(self) -> None:
        with patch("httpx.get") as m:
            m.return_value = MagicMock(
                status_code=200,
                json=lambda: {"data": None},
            )
            assert search_jaeger_traces("hotrod") == []

    def test_with_error_filter(self) -> None:
        with patch("httpx.get") as m:
            m.return_value = MagicMock(
                status_code=200,
                json=lambda: {"data": [], "total": 0},
            )
            traces = search_jaeger_traces("hotrod", with_errors=True)
            assert traces == []

    def test_with_operation_filter(self) -> None:
        with patch("httpx.get") as m:
            m.return_value = MagicMock(
                status_code=200,
                json=lambda: {"data": [], "total": 0},
            )
            traces = search_jaeger_traces("hotrod", operation="GET /api")
            assert traces == []

    def test_with_duration_min(self) -> None:
        with patch("httpx.get") as m:
            m.return_value = MagicMock(
                status_code=200,
                json=lambda: {"data": [], "total": 0},
            )
            traces = search_jaeger_traces("hotrod", duration_min="100ms")
            assert traces == []

    def test_with_start_time(self) -> None:
        with patch("httpx.get") as m:
            m.return_value = MagicMock(
                status_code=200,
                json=lambda: {"data": [], "total": 0},
            )
            traces = search_jaeger_traces("hotrod", start_time="-1h")
            assert traces == []

    def test_empty_spans_in_trace(self) -> None:
        with patch("httpx.get") as m:
            m.return_value = MagicMock(
                status_code=200,
                json=lambda: {
                    "data": [{"traceID": "abc", "spans": None}],
                    "total": 1,
                },
            )
            traces = search_jaeger_traces("hotrod")
            assert len(traces) == 1  # noqa: PLR2004


class TestGetJaegerTrace:
    def test_returns_trace_with_spans(self) -> None:
        with patch("httpx.get") as m:
            m.return_value = MagicMock(
                status_code=200,
                json=lambda: {
                    "data": [
                        {
                            "traceID": "abc123",
                            "spans": [
                                {
                                    "traceID": "abc123",
                                    "spanID": "span1",
                                    "operationName": "GET /api",
                                    "duration": 5000,
                                    "startTime": 1700000000,
                                    "tags": [{"key": "http.method", "value": "GET"}],
                                }
                            ],
                            "processes": {"p1": {"serviceName": "hotrod"}},
                        }
                    ]
                },
            )
            trace = get_jaeger_trace("abc123")
            assert trace is not None
            assert trace["traceID"] == "abc123"
            assert len(trace["spans"]) == 1  # noqa: PLR2004

    def test_returns_none_on_empty_data(self) -> None:
        with patch("httpx.get") as m:
            m.return_value = MagicMock(
                status_code=200,
                json=lambda: {"data": []},
            )
            assert get_jaeger_trace("abc") is None

    def test_returns_none_on_non_list_data(self) -> None:
        with patch("httpx.get") as m:
            m.return_value = MagicMock(
                status_code=200,
                json=lambda: {"data": None},
            )
            assert get_jaeger_trace("abc") is None

    def test_returns_none_on_non_list_spans(self) -> None:
        with patch("httpx.get") as m:
            m.return_value = MagicMock(
                status_code=200,
                json=lambda: {
                    "data": [{"traceID": "abc", "spans": "not-a-list"}],
                },
            )
            trace = get_jaeger_trace("abc")
            assert trace is not None
            assert trace["spans"] == []

    def test_returns_none_on_error(self) -> None:
        with patch("httpx.get", side_effect=Exception("timeout")):
            assert get_jaeger_trace("abc") is None


class TestGetJaegerDependencies:
    def test_returns_dependencies(self) -> None:
        with patch("httpx.get") as m:
            m.return_value = MagicMock(
                status_code=200,
                json=lambda: {"data": [{"parent": "a", "child": "b", "callCount": 10}]},
            )
            deps = get_jaeger_dependencies(1700000000)
            assert len(deps) == 1  # noqa: PLR2004
            assert deps[0]["parent"] == "a"

    def test_returns_empty_on_error(self) -> None:
        with patch("httpx.get", side_effect=Exception("timeout")):
            assert get_jaeger_dependencies(1700000000) == []

    def test_returns_empty_on_non_list(self) -> None:
        with patch("httpx.get") as m:
            m.return_value = MagicMock(
                status_code=200,
                json=lambda: {"data": None},
            )
            assert get_jaeger_dependencies(1700000000) == []


class TestPrometheusInstant:
    def test_returns_metrics(self) -> None:
        with patch("httpx.get") as m:
            m.return_value = MagicMock(
                status_code=200,
                json=lambda: {
                    "status": "success",
                    "data": {
                        "resultType": "vector",
                        "result": [
                            {
                                "metric": {"__name__": "up", "job": "prometheus"},
                                "value": [1700000000, "1"],
                            }
                        ],
                    },
                },
            )
            metrics = query_prometheus_instant("up")
            assert len(metrics) == 1  # noqa: PLR2004
            assert metrics[0]["value"] == 1.0  # noqa: PLR2004
            assert metrics[0]["labels"]["job"] == "prometheus"

    def test_returns_empty_on_error(self) -> None:
        with patch("httpx.get", side_effect=Exception("timeout")):
            assert query_prometheus_instant("up") == []

    def test_with_time_param(self) -> None:
        with patch("httpx.get") as m:
            m.return_value = MagicMock(
                status_code=200,
                json=lambda: {
                    "status": "success",
                    "data": {"resultType": "vector", "result": []},
                },
            )
            result = query_prometheus_instant("up", time="1700000000")
            assert result == []

    def test_non_list_result(self) -> None:
        with patch("httpx.get") as m:
            m.return_value = MagicMock(
                status_code=200,
                json=lambda: {"status": "success", "data": {"result": None}},
            )
            assert query_prometheus_instant("up") == []


class TestPrometheusRange:
    def test_returns_results(self) -> None:
        with patch("httpx.get") as m:
            m.return_value = MagicMock(
                status_code=200,
                json=lambda: {
                    "status": "success",
                    "data": {
                        "resultType": "matrix",
                        "result": [
                            {
                                "metric": {"__name__": "up"},
                                "values": [
                                    [1700000000, "1"],
                                    [1700000060, "1"],
                                ],
                            }
                        ],
                    },
                },
            )
            results = query_prometheus_range("up", "1700000000", "1700000100")
            assert len(results) == 1  # noqa: PLR2004
            assert len(results[0]["values"]) == 2  # noqa: PLR2004

    def test_returns_empty_on_range_error(self) -> None:
        with patch("httpx.get", side_effect=Exception("timeout")):
            assert query_prometheus_range("up", "0", "1") == []

    def test_non_list_range_result(self) -> None:
        with patch("httpx.get") as m:
            m.return_value = MagicMock(
                status_code=200,
                json=lambda: {"status": "success", "data": {"result": "not-a-list"}},
            )
            assert query_prometheus_range("up", "0", "1") == []

    def test_value_non_numeric_returns_zero(self) -> None:
        with patch("httpx.get") as m:
            m.return_value = MagicMock(
                status_code=200,
                json=lambda: {
                    "status": "success",
                    "data": {
                        "resultType": "vector",
                        "result": [
                            {
                                "metric": {"__name__": "up"},
                                "value": [1700000000, "not-floatable"],
                            }
                        ],
                    },
                },
            )
            metrics = query_prometheus_instant("up")
            assert metrics[0]["value"] == 0.0  # noqa: PLR2004

    def test_invalid_prometheus_value_return_zero(self) -> None:
        with patch("httpx.get") as m:
            m.return_value = MagicMock(
                status_code=200,
                json=lambda: {
                    "status": "success",
                    "data": {
                        "resultType": "vector",
                        "result": [
                            {
                                "metric": {"__name__": "up"},
                                "value": "not-a-list-at-all",  # noqa: PLR2004
                            }
                        ],
                    },
                },
            )
            metrics = query_prometheus_instant("up")
            assert metrics[0]["value"] == 0.0  # noqa: PLR2004
