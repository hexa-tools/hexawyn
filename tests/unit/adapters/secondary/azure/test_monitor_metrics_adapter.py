from __future__ import annotations

from unittest.mock import Mock, patch

import httpx
import pytest
from hexawyn.adapters.secondary.azure.monitor_metrics_adapter import (
    AzureMonitorMetricsAdapter,
)
from hexawyn.domain.errors import (
    AdapterTimeoutError,
    PrometheusQueryError,
    PrometheusUnavailableError,
)


def _mock_response(
    status_code: int = 200,
    json_data: object | None = None,
) -> Mock:
    response = Mock(spec=httpx.Response)
    response.status_code = status_code
    response.json.return_value = json_data or {}
    response.raise_for_status = Mock()
    response.text = "some text"
    return response


class TestAzureMonitorMetricsAdapter:
    @staticmethod
    def _adapter(
        endpoint: str = "https://my-workspace.monitor.azure.com",
        http_client: httpx.Client | None = None,
        token_provider: object | None = None,
    ) -> AzureMonitorMetricsAdapter:
        return AzureMonitorMetricsAdapter(
            endpoint=endpoint,
            http_client=http_client,
            token_provider=token_provider,
        )

    def test_endpoint_property_strips_trailing_slash(self) -> None:
        adapter = self._adapter(endpoint="https://my-workspace.monitor.azure.com/")
        assert adapter.endpoint == "https://my-workspace.monitor.azure.com"

    def test_instant_query_parses_data(self) -> None:
        mock_client = Mock(spec=httpx.Client)
        response_data = {
            "data": {
                "result": [
                    {
                        "metric": {"pod": "api"},
                        "value": [1700000000, "42.5"],
                    }
                ]
            }
        }
        mock_client.get.return_value = _mock_response(status_code=200, json_data=response_data)
        adapter = self._adapter(http_client=mock_client, token_provider=lambda: "fake-token")

        result = adapter.instant_query("up", timeout_seconds=30.0)

        assert len(result) == 1  # noqa: PLR2004
        assert result[0]["metric"] == {"pod": "api"}
        assert result[0]["value"] == 42.5  # noqa: PLR2004

    def test_instant_query_empty_result(self) -> None:
        mock_client = Mock(spec=httpx.Client)
        mock_client.get.return_value = _mock_response(
            status_code=200, json_data={"data": {"result": []}}
        )
        adapter = self._adapter(http_client=mock_client, token_provider=lambda: "fake-token")

        result = adapter.instant_query("up", timeout_seconds=30.0)

        assert result == []

    def test_instant_query_no_data_key(self) -> None:
        mock_client = Mock(spec=httpx.Client)
        mock_client.get.return_value = _mock_response(status_code=200, json_data={})
        adapter = self._adapter(http_client=mock_client, token_provider=lambda: "fake-token")

        result = adapter.instant_query("up", timeout_seconds=30.0)

        assert result == []

    def test_instant_query_result_not_list(self) -> None:
        mock_client = Mock(spec=httpx.Client)
        response_data = {"data": {"result": "not-a-list"}}
        mock_client.get.return_value = _mock_response(status_code=200, json_data=response_data)
        adapter = self._adapter(http_client=mock_client, token_provider=lambda: "fake-token")

        result = adapter.instant_query("up", timeout_seconds=30.0)

        assert result == []

    def test_range_query_parses_data(self) -> None:
        mock_client = Mock(spec=httpx.Client)
        response_data = {
            "data": {
                "result": [
                    {
                        "metric": {"pod": "api"},
                        "values": [[1700000000, "10.0"], [1700003600, "20.0"]],
                    }
                ]
            }
        }
        mock_client.get.return_value = _mock_response(status_code=200, json_data=response_data)
        adapter = self._adapter(http_client=mock_client, token_provider=lambda: "fake-token")

        result = adapter.range_query(
            "rate(http_requests[5m])",
            start="2024-01-01T00:00:00Z",
            end="2024-01-01T01:00:00Z",
            step="60s",
            timeout_seconds=30.0,
        )

        assert len(result) == 1  # noqa: PLR2004
        assert result[0]["metric"] == {"pod": "api"}
        assert len(result[0]["values"]) == 2  # noqa: PLR2004

    def test_range_query_empty_result(self) -> None:
        mock_client = Mock(spec=httpx.Client)
        mock_client.get.return_value = _mock_response(
            status_code=200, json_data={"data": {"result": []}}
        )
        adapter = self._adapter(http_client=mock_client, token_provider=lambda: "fake-token")

        result = adapter.range_query("up", "start", "end", "60s", timeout_seconds=30.0)

        assert result == []

    def test_timeout_raises_adapter_timeout_error(self) -> None:
        mock_client = Mock(spec=httpx.Client)
        mock_client.get.side_effect = httpx.TimeoutException("timed out")
        adapter = self._adapter(http_client=mock_client, token_provider=lambda: "fake-token")

        with pytest.raises(AdapterTimeoutError, match="timed out"):
            adapter.instant_query("up", timeout_seconds=5.0)

    def test_http_error_raises_prometheus_unavailable(self) -> None:
        mock_client = Mock(spec=httpx.Client)
        mock_client.get.side_effect = httpx.ConnectError("connection refused")
        adapter = self._adapter(http_client=mock_client, token_provider=lambda: "fake-token")

        with pytest.raises(PrometheusUnavailableError):
            adapter.instant_query("up", timeout_seconds=30.0)

    def test_bad_request_raises_prometheus_query_error(self) -> None:
        mock_client = Mock(spec=httpx.Client)
        mock_response = _mock_response(status_code=400, json_data={"error": "bad promql"})
        mock_response.raise_for_status = Mock()
        mock_client.get.return_value = mock_response
        adapter = self._adapter(http_client=mock_client, token_provider=lambda: "fake-token")

        with pytest.raises(PrometheusQueryError, match="up"):
            adapter.instant_query("up", timeout_seconds=30.0)

    def test_http_status_error_raises_prometheus_unavailable(self) -> None:
        mock_client = Mock(spec=httpx.Client)
        mock_response = _mock_response(status_code=503, json_data={})
        mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "service unavailable", request=Mock(), response=mock_response
        )
        mock_client.get.return_value = mock_response
        adapter = self._adapter(http_client=mock_client, token_provider=lambda: "fake-token")

        with pytest.raises(PrometheusUnavailableError):
            adapter.instant_query("up", timeout_seconds=30.0)

    def test_authentication_error_raises_prometheus_unavailable(self) -> None:
        from azure.core.exceptions import ClientAuthenticationError

        mock_client = Mock(spec=httpx.Client)
        mock_client.get.return_value = _mock_response(
            status_code=200, json_data={"data": {"result": []}}
        )
        adapter = self._adapter(http_client=mock_client, token_provider=None)

        with patch(
            "hexawyn.adapters.secondary.azure.monitor_metrics_adapter._acquire_azure_token",
            side_effect=ClientAuthenticationError("auth failed"),
        ):
            with pytest.raises(PrometheusUnavailableError):
                adapter.instant_query("up", timeout_seconds=30.0)

    def test_auth_headers_uses_token_provider(self) -> None:
        mock_client = Mock(spec=httpx.Client)
        mock_client.get.return_value = _mock_response(
            status_code=200, json_data={"data": {"result": []}}
        )
        adapter = self._adapter(http_client=mock_client, token_provider=lambda: "my-azure-token")

        adapter.instant_query("up", timeout_seconds=30.0)

        call_headers = mock_client.get.call_args.kwargs["headers"]
        assert call_headers["Authorization"] == "Bearer my-azure-token"

    def test_client_or_create_returns_injected_client(self) -> None:
        mock_client = Mock(spec=httpx.Client)
        adapter = self._adapter(http_client=mock_client)

        result = adapter._client_or_create()

        assert result is mock_client

    def test_client_or_create_lazy_init(self) -> None:
        adapter = self._adapter(http_client=None)

        result = adapter._client_or_create()

        assert isinstance(result, httpx.Client)
