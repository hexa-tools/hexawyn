from unittest.mock import MagicMock, patch

import httpx
import pytest

pytest.importorskip("azure.identity")
from azure.core.exceptions import ClientAuthenticationError  # noqa: E402
from hexawyn.application.ports.driven.metrics_query_port import MetricsQueryPort  # noqa: E402
from hexawyn.domain.errors import (  # noqa: E402
    AdapterTimeoutError,
    PrometheusQueryError,
    PrometheusUnavailableError,
)

_ENDPOINT = "https://ws-abc.westeurope.prometheus.monitor.azure.com"


def _response(status_code: int = 200, result: list | None = None, text: str = "") -> MagicMock:
    response = MagicMock()
    response.status_code = status_code
    response.text = text
    response.json.return_value = {
        "status": "success",
        "data": {"resultType": "vector", "result": result or []},
    }
    return response


def _adapter(client: MagicMock):
    from hexawyn.adapters.secondary.azure.monitor_metrics_adapter import (
        AzureMonitorMetricsAdapter,
    )

    return AzureMonitorMetricsAdapter(
        endpoint=_ENDPOINT, http_client=client, token_provider=lambda: "tok-xyz"
    )


class TestContract:
    def test_is_a_metrics_query_port(self) -> None:
        assert isinstance(_adapter(MagicMock()), MetricsQueryPort)

    def test_endpoint_strips_trailing_slash(self) -> None:
        from hexawyn.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        adapter = AzureMonitorMetricsAdapter(
            endpoint=_ENDPOINT + "/", http_client=MagicMock(), token_provider=lambda: "t"
        )

        assert adapter.endpoint == _ENDPOINT


class TestInstantQuery:
    def test_parses_instant_sample(self) -> None:
        client = MagicMock()
        client.get.return_value = _response(
            result=[{"metric": {"pod": "p"}, "value": [123.0, "1.5"]}]
        )
        adapter = _adapter(client)

        samples = adapter.instant_query("up", timeout_seconds=10.0)

        assert samples[0]["value"] == 1.5

    def test_calls_query_endpoint_with_auth(self) -> None:
        client = MagicMock()
        client.get.return_value = _response(result=[])
        adapter = _adapter(client)

        adapter.instant_query("up", timeout_seconds=10.0)

        call = client.get.call_args
        assert call.args[0].endswith("/api/v1/query")
        assert call.kwargs["headers"]["Authorization"] == "Bearer tok-xyz"


class TestRangeQuery:
    def test_parses_range_sample(self) -> None:
        client = MagicMock()
        client.get.return_value = _response(result=[{"metric": {}, "values": [[123.0, "2.0"]]}])
        adapter = _adapter(client)

        samples = adapter.range_query("up", start="0", end="1", step="1m", timeout_seconds=10.0)

        assert samples[0]["values"][0][1] == 2.0
        assert client.get.call_args.args[0].endswith("/api/v1/query_range")


class TestErrorTranslation:
    def test_timeout(self) -> None:
        client = MagicMock()
        client.get.side_effect = httpx.TimeoutException("slow")
        adapter = _adapter(client)

        with pytest.raises(AdapterTimeoutError):
            adapter.instant_query("up", timeout_seconds=1.0)

    def test_http_error(self) -> None:
        client = MagicMock()
        client.get.side_effect = httpx.ConnectError("down")
        adapter = _adapter(client)

        with pytest.raises(PrometheusUnavailableError):
            adapter.instant_query("up", timeout_seconds=1.0)

    def test_http_400(self) -> None:
        client = MagicMock()
        client.get.return_value = _response(status_code=400, text="bad")
        adapter = _adapter(client)

        with pytest.raises(PrometheusQueryError):
            adapter.instant_query("bad{", timeout_seconds=1.0)

    def test_missing_credentials(self) -> None:
        from hexawyn.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        def _boom() -> str:
            raise ClientAuthenticationError("no creds")

        adapter = AzureMonitorMetricsAdapter(
            endpoint=_ENDPOINT, http_client=MagicMock(), token_provider=_boom
        )

        with pytest.raises(PrometheusUnavailableError):
            adapter.instant_query("up", timeout_seconds=1.0)

    def test_error_status_raises_prometheus_unavailable(self) -> None:
        response = MagicMock()
        response.status_code = 500
        response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "boom",
            request=httpx.Request("GET", "https://x"),
            response=httpx.Response(500),
        )
        client = MagicMock()
        client.get.return_value = response
        adapter = _adapter(client)

        with pytest.raises(PrometheusUnavailableError):
            adapter.instant_query("up", timeout_seconds=1.0)


class TestBodyParsing:
    def test_returns_empty_when_data_not_dict(self) -> None:
        response = MagicMock()
        response.status_code = 200
        response.raise_for_status.return_value = None
        response.json.return_value = {"data": "nope"}
        client = MagicMock()
        client.get.return_value = response
        adapter = _adapter(client)

        assert adapter.instant_query("up", timeout_seconds=1.0) == []

    def test_returns_empty_when_result_not_list(self) -> None:
        response = MagicMock()
        response.status_code = 200
        response.raise_for_status.return_value = None
        response.json.return_value = {"data": {"result": "nope"}}
        client = MagicMock()
        client.get.return_value = response
        adapter = _adapter(client)

        assert adapter.instant_query("up", timeout_seconds=1.0) == []


class TestAzureToken:
    def test_acquire_azure_token(self) -> None:
        from hexawyn.adapters.secondary.azure import monitor_metrics_adapter as module

        credential = MagicMock()
        credential.get_token.return_value = MagicMock(token="fresh")
        with patch("azure.identity.DefaultAzureCredential", return_value=credential):
            token = module._acquire_azure_token()

        assert token == "fresh"
        credential.get_token.assert_called_once()

    def test_default_token_used_when_no_provider(self) -> None:
        from hexawyn.adapters.secondary.azure import monitor_metrics_adapter as module
        from hexawyn.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        client = MagicMock()
        client.get.return_value = _response(result=[])
        adapter = AzureMonitorMetricsAdapter(endpoint=_ENDPOINT, http_client=client)

        with patch.object(module, "_acquire_azure_token", return_value="def-tok"):
            adapter.instant_query("up", timeout_seconds=1.0)

        assert client.get.call_args.kwargs["headers"]["Authorization"] == "Bearer def-tok"


class TestLazyHttpClient:
    def test_creates_httpx_client_when_not_injected(self) -> None:
        from hexawyn.adapters.secondary.azure import monitor_metrics_adapter as module
        from hexawyn.adapters.secondary.azure.monitor_metrics_adapter import (
            AzureMonitorMetricsAdapter,
        )

        fake_client = MagicMock()
        fake_client.get.return_value = _response(result=[])
        adapter = AzureMonitorMetricsAdapter(endpoint=_ENDPOINT, token_provider=lambda: "t")

        with patch.object(module.httpx, "Client", return_value=fake_client) as client_cls:
            adapter.instant_query("up", timeout_seconds=1.0)

        client_cls.assert_called_once()
