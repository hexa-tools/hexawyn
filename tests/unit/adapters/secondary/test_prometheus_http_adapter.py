from __future__ import annotations

from unittest.mock import MagicMock, patch

import httpx
import pytest
from hexawyn.adapters.secondary.gitops.prometheus_http_adapter import (
    PrometheusHTTPAdapter,
    _instant_query_params,
    _range_query_params,
)
from hexawyn.application.ports.driven.metrics_query_port import MetricsQueryPort
from hexawyn.domain.errors import (
    AdapterTimeoutError,
    PrometheusQueryError,
    PrometheusUnavailableError,
)


def _response(status_code: int = 200, json_body: dict | None = None) -> MagicMock:
    mock_response = MagicMock(spec=httpx.Response)
    mock_response.status_code = status_code
    mock_response.json.return_value = json_body or {}
    if status_code >= 400:
        mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "error", request=MagicMock(), response=mock_response
        )
    else:
        mock_response.raise_for_status.return_value = None
    return mock_response


class TestInstantQuery:
    def test_valid_query_returns_metric_and_value(self) -> None:
        mock_response = _response(
            200,
            {
                "status": "success",
                "data": {
                    "resultType": "vector",
                    "result": [
                        {
                            "metric": {"pod": "payment-pod-abc", "container": "app"},
                            "value": [1717257300, "0.0032"],
                        }
                    ],
                },
            },
        )

        with patch("httpx.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_client.get.return_value = mock_response
            mock_client_class.return_value = mock_client

            adapter = PrometheusHTTPAdapter(endpoint="http://prometheus.monitoring.svc:9090")
            samples = adapter.instant_query(
                'rate(container_cpu_usage_seconds_total{namespace="payment"}[5m])',
                timeout_seconds=15.0,
            )

        assert samples == [
            {"metric": {"pod": "payment-pod-abc", "container": "app"}, "value": 0.0032}
        ]

    def test_implements_metrics_query_port(self) -> None:
        adapter = PrometheusHTTPAdapter(endpoint="http://prometheus.monitoring.svc:9090")
        assert isinstance(adapter, MetricsQueryPort)


class TestRangeQuery:
    def test_range_query_returns_series_with_iso_timestamps(self) -> None:
        mock_response = _response(
            200,
            {
                "status": "success",
                "data": {
                    "resultType": "matrix",
                    "result": [
                        {
                            "metric": {"pod": "payment-pod-abc"},
                            "values": [[1717257300, "0.001"], [1717257360, "0.002"]],
                        }
                    ],
                },
            },
        )

        with patch("httpx.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_client.get.return_value = mock_response
            mock_client_class.return_value = mock_client

            adapter = PrometheusHTTPAdapter(endpoint="http://prometheus.monitoring.svc:9090")
            samples = adapter.range_query(
                "rate(container_cpu_usage_seconds_total[5m])",
                start="2024-06-01T14:00:00Z",
                end="2024-06-01T14:05:00Z",
                step="30s",
                timeout_seconds=15.0,
            )

        assert len(samples) == 1
        assert samples[0]["metric"] == {"pod": "payment-pod-abc"}
        assert samples[0]["values"][0] == ("2024-06-01T15:55:00Z", 0.001)


class TestConnectionErrors:
    def test_connection_refused_raises_unavailable_with_endpoint(self) -> None:
        with patch("httpx.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_client.get.side_effect = httpx.ConnectError("Connection refused")
            mock_client_class.return_value = mock_client

            adapter = PrometheusHTTPAdapter(endpoint="http://prometheus.monitoring.svc:9090")

            with pytest.raises(PrometheusUnavailableError) as exc_info:
                adapter.instant_query("up", timeout_seconds=15.0)

        assert "prometheus.monitoring.svc:9090" in str(exc_info.value)

    def test_timeout_raises_adapter_timeout_error(self) -> None:
        with patch("httpx.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_client.get.side_effect = httpx.TimeoutException("timed out")
            mock_client_class.return_value = mock_client

            adapter = PrometheusHTTPAdapter(endpoint="http://prometheus.monitoring.svc:9090")

            with pytest.raises(AdapterTimeoutError):
                adapter.instant_query("up", timeout_seconds=5.0)

    def test_non_400_http_error_raises_unavailable(self) -> None:
        mock_response = _response(500, {})

        with patch("httpx.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_client.get.return_value = mock_response
            mock_client_class.return_value = mock_client

            adapter = PrometheusHTTPAdapter(endpoint="http://prometheus.monitoring.svc:9090")

            with pytest.raises(PrometheusUnavailableError):
                adapter.instant_query("up", timeout_seconds=15.0)


class TestSyntaxError:
    def test_400_response_raises_prometheus_query_error(self) -> None:
        mock_response = _response(
            400,
            {
                "status": "error",
                "errorType": "bad_data",
                "error": "parse error at char 1: unexpected end of input",
            },
        )

        with patch("httpx.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_client.get.return_value = mock_response
            mock_client_class.return_value = mock_client

            adapter = PrometheusHTTPAdapter(endpoint="http://prometheus.monitoring.svc:9090")

            with pytest.raises(PrometheusQueryError) as exc_info:
                adapter.instant_query("rate(foo[5m]", timeout_seconds=15.0)

        assert "unexpected end of input" in str(exc_info.value)


class TestAuthentication:
    def test_bearer_token_added_to_client_headers(self) -> None:
        with patch("httpx.Client") as mock_client_class:
            PrometheusHTTPAdapter(
                endpoint="http://prometheus.monitoring.svc:9090", token="secret-token"
            )

        _, kwargs = mock_client_class.call_args
        assert kwargs["headers"]["Authorization"] == "Bearer secret-token"

    def test_no_token_means_no_auth_header(self) -> None:
        with patch("httpx.Client") as mock_client_class:
            PrometheusHTTPAdapter(endpoint="http://prometheus.monitoring.svc:9090")

        _, kwargs = mock_client_class.call_args
        assert "Authorization" not in kwargs["headers"]


class TestQueryParamConstruction:
    def test_instant_query_params_wraps_promql(self) -> None:
        assert _instant_query_params("up") == {"query": "up"}

    def test_range_query_params_includes_start_end_step(self) -> None:
        params = _range_query_params(
            "up", start="2024-06-01T14:00:00Z", end="2024-06-01T14:05:00Z", step="30s"
        )
        assert params == {
            "query": "up",
            "start": "2024-06-01T14:00:00Z",
            "end": "2024-06-01T14:05:00Z",
            "step": "30s",
        }


class TestClose:
    def test_close_calls_client_close(self) -> None:
        with patch("httpx.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_client_class.return_value = mock_client

            adapter = PrometheusHTTPAdapter(endpoint="http://prometheus.monitoring.svc:9090")
            adapter.close()

        mock_client.close.assert_called_once()


class TestMalformedResponseBody:
    def test_missing_data_field_returns_empty_list(self) -> None:
        mock_response = _response(200, {"status": "success"})

        with patch("httpx.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_client.get.return_value = mock_response
            mock_client_class.return_value = mock_client

            adapter = PrometheusHTTPAdapter(endpoint="http://prometheus.monitoring.svc:9090")
            samples = adapter.instant_query("up", timeout_seconds=15.0)

        assert samples == []

    def test_non_list_result_field_returns_empty_list(self) -> None:
        mock_response = _response(
            200, {"status": "success", "data": {"resultType": "vector", "result": "not-a-list"}}
        )

        with patch("httpx.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_client.get.return_value = mock_response
            mock_client_class.return_value = mock_client

            adapter = PrometheusHTTPAdapter(endpoint="http://prometheus.monitoring.svc:9090")
            samples = adapter.instant_query("up", timeout_seconds=15.0)

        assert samples == []


class TestErrorDetailFallback:
    def test_non_json_400_body_falls_back_to_response_text(self) -> None:
        mock_response = MagicMock(spec=httpx.Response)
        mock_response.status_code = 400
        mock_response.json.side_effect = ValueError("not JSON")
        mock_response.text = "Bad Request"

        with patch("httpx.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_client.get.return_value = mock_response
            mock_client_class.return_value = mock_client

            adapter = PrometheusHTTPAdapter(endpoint="http://prometheus.monitoring.svc:9090")

            with pytest.raises(PrometheusQueryError) as exc_info:
                adapter.instant_query("bad{", timeout_seconds=15.0)

        assert "Bad Request" in str(exc_info.value)

    def test_json_400_body_without_error_key_falls_back_to_response_text(self) -> None:
        mock_response = MagicMock(spec=httpx.Response)
        mock_response.status_code = 400
        mock_response.json.return_value = {"status": "error"}
        mock_response.text = "raw body"

        with patch("httpx.Client") as mock_client_class:
            mock_client = MagicMock()
            mock_client.get.return_value = mock_response
            mock_client_class.return_value = mock_client

            adapter = PrometheusHTTPAdapter(endpoint="http://prometheus.monitoring.svc:9090")

            with pytest.raises(PrometheusQueryError) as exc_info:
                adapter.instant_query("bad{", timeout_seconds=15.0)

        assert "raw body" in str(exc_info.value)
