from __future__ import annotations

from datetime import UTC, datetime
from typing import cast

import httpx
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


class PrometheusHTTPAdapter(MetricsQueryPort):
    def __init__(self, endpoint: str, token: str | None = None) -> None:
        self._endpoint = endpoint.rstrip("/")
        headers = {"Authorization": f"Bearer {token}"} if token else {}
        self._client = httpx.Client(headers=headers)

    def close(self) -> None:
        self._client.close()

    def instant_query(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        params = _instant_query_params(promql)
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query", params, promql, timeout_seconds
        )
        return [_to_instant_sample(item) for item in raw_results]

    def range_query(
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        params = _range_query_params(promql, start, end, step)
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range", params, promql, timeout_seconds
        )
        return [_to_range_sample(item) for item in raw_results]

    def _execute(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        try:
            response = self._client.get(url, params=params, timeout=timeout_seconds)
        except httpx.TimeoutException as exc:
            raise AdapterTimeoutError(
                f"Prometheus query timed out after {timeout_seconds}s",
                context={"endpoint": self._endpoint, "promql": promql},
            ) from exc
        except httpx.HTTPError as exc:
            raise PrometheusUnavailableError(self._endpoint) from exc

        if response.status_code == 400:
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


def _instant_query_params(promql: str) -> dict[str, str]:
    """Builds the query params for Prometheus's `/api/v1/query` endpoint."""
    return {"query": promql}


def _range_query_params(promql: str, start: str, end: str, step: str) -> dict[str, str]:
    """Builds the query params for Prometheus's `/api/v1/query_range` endpoint."""
    return {"query": promql, "start": start, "end": end, "step": step}


def _to_instant_sample(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    value_pair = cast(list[object], item.get("value", [0, "0"]))
    return PrometheusInstantSample(metric=metric, value=float(cast(str, value_pair[1])))


def _to_range_sample(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    raw_values = cast(list[list[object]], item.get("values", []))
    values = [(_to_iso(cast(float, point[0])), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def _error_detail(response: httpx.Response) -> str:
    try:
        body = response.json()
    except ValueError:
        return response.text
    if isinstance(body, dict) and "error" in body:
        return str(body["error"])
    return response.text


def _to_iso(epoch_seconds: float) -> str:
    return datetime.fromtimestamp(epoch_seconds, tz=UTC).isoformat().replace("+00:00", "Z")
