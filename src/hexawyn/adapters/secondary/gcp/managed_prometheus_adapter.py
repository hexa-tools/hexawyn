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

_MONITORING_SCOPE = "https://www.googleapis.com/auth/monitoring.read"
_HTTP_BAD_REQUEST = 400


class GCPManagedPrometheusAdapter(MetricsQueryPort):
    """MetricsQueryPort backed by GCP Managed Prometheus.

    Managed Prometheus exposes a Prometheus-compatible query API, so this
    adapter is thin: it targets the GMP endpoint and injects a refreshed
    Google bearer token per request, reusing the vanilla Prometheus parsing.
    """

    def __init__(
        self,
        project_id: str,
        http_client: httpx.Client | None = None,
        token_provider: Callable[[], str] | None = None,
    ) -> None:
        self._project_id = project_id
        self._endpoint = (
            f"https://monitoring.googleapis.com/v1/projects/{project_id}/location/global/prometheus"
        )
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
                f"GCP Managed Prometheus query timed out after {timeout_seconds}s",
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
        from google.auth.exceptions import DefaultCredentialsError

        try:
            bearer = self._token_provider() if self._token_provider else _acquire_google_token()
        except DefaultCredentialsError as exc:
            raise PrometheusUnavailableError(self._endpoint) from exc
        return {"Authorization": f"Bearer {bearer}"}

    def _client_or_create(self) -> httpx.Client:
        if self._http_client is None:
            self._http_client = httpx.Client()
        return self._http_client


def _acquire_google_token() -> str:
    from google.auth import default
    from google.auth.transport.requests import Request

    credentials, _ = default(scopes=[_MONITORING_SCOPE])
    credentials.refresh(Request())
    return str(credentials.token)
