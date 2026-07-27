# Auto-generated test for otel_http_client

from __future__ import annotations

from unittest.mock import patch

from hexawyn.adapters.secondary.gitops.otel_http_client import (
    list_jaeger_services,
    query_prometheus_instant,
    search_jaeger_traces,
)


class TestOtelHttpClientUnit:
    def test_list_services_mocked(self) -> None:
        with patch("httpx.get") as m:
            m.return_value.status_code = 200
            m.return_value.json = lambda: {"data": [], "total": 0}
            assert list_jaeger_services() == []

    def test_search_traces_mocked(self) -> None:
        assert search_jaeger_traces("test") == []

    def test_prometheus_mocked(self) -> None:
        with patch("httpx.get") as m:
            m.return_value.status_code = 200
            m.return_value.json = lambda: {"status": "error", "data": {"result": []}}
            assert query_prometheus_instant("up") == []
