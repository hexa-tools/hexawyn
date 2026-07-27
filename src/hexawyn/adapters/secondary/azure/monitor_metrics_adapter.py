from __future__ import annotations

from collections.abc import Callable
from typing import cast

import httpx

from hexawyn.adapters.secondary.gitops.prometheus_http_adapter import (
    _error_detail,
    _instant_query_params,
    _range_query_params,
    _to_instant_sample,
    _to_range_sample,
)
from hexawyn.application.ports.driven.metrics_query_port import (
    MetricsQueryPort,
    PrometheusInstantSample,
    PrometheusRangeSample,
)
from hexawyn.domain.errors import (
    AdapterTimeoutError,
    PrometheusQueryError,
    PrometheusUnavailableError,
)

_PROMETHEUS_SCOPE = "https://prometheus.monitor.azure.com/.default"
_HTTP_BAD_REQUEST = 400


class AzureMonitorMetricsAdapter(MetricsQueryPort):
    """MetricsQueryPort backed by Azure Monitor managed service for Prometheus.

    The managed Prometheus query endpoint is Prometheus-compatible, so this
    adapter is thin: it targets the workspace query endpoint and injects an
    Azure AD bearer token per request, reusing the vanilla Prometheus parsing.
    """

    def __init__(
        self,
        endpoint: str,
        http_client: httpx.Client | None = None,
        token_provider: Callable[[], str] | None = None,
    ) -> None:
        self._endpoint = endpoint.rstrip("/")
        self._http_client = http_client
        self._token_provider = token_provider

    @property
    def endpoint(self) -> str:
        return self._endpoint

    def instant_query(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query",
            _instant_query_params(promql),
            promql,
            timeout_seconds,
        )
        return [_to_instant_sample(item) for item in raw_results]

    def range_query(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range",
            _range_query_params(promql, start, end, step),
            promql,
            timeout_seconds,
        )
        return [_to_range_sample(item) for item in raw_results]

    def _execute(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = self._auth_headers()
        try:
            response = client.get(url, params=params, headers=headers, timeout=timeout_seconds)
        except httpx.TimeoutException as exc:
            raise AdapterTimeoutError(
                f"Azure Monitor Prometheus query timed out after {timeout_seconds}s",
                context={"endpoint": self._endpoint, "promql": promql},
            ) from exc
        except httpx.HTTPError as exc:
            raise PrometheusUnavailableError(self._endpoint) from exc

        if response.status_code == _HTTP_BAD_REQUEST:
            raise PrometheusQueryError(promql=promql, detail=_error_detail(response))

        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as exc:
            raise PrometheusUnavailableError(self._endpoint) from exc

        body: dict[str, object] = response.json()
        data = body.get("data")
        if not isinstance(data, dict):
            return []
        result = data.get("result")
        if not isinstance(result, list):
            return []
        return cast(list[dict[str, object]], result)

    def _auth_headers(self) -> dict[str, str]:
        from azure.core.exceptions import ClientAuthenticationError

        try:
            bearer = self._token_provider() if self._token_provider else _acquire_azure_token()
        except ClientAuthenticationError as exc:
            raise PrometheusUnavailableError(self._endpoint) from exc
        return {"Authorization": f"Bearer {bearer}"}

    def _client_or_create(self) -> httpx.Client:
        if self._http_client is None:
            self._http_client = httpx.Client()
        return self._http_client


def _acquire_azure_token() -> str:
    from azure.identity import DefaultAzureCredential

    credential = DefaultAzureCredential()
    granted = credential.get_token(_PROMETHEUS_SCOPE)
    return str(granted.token)
