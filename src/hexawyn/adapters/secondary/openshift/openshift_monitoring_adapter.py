from __future__ import annotations

from hexawyn.application.ports.driven.metrics_query_port import (
    MetricsQueryPort,
    PrometheusInstantSample,
    PrometheusRangeSample,
)


class OpenShiftMonitoringAdapter(MetricsQueryPort):
    """MetricsQueryPort backed by the built-in OpenShift Monitoring stack.

    OpenShift ships a Thanos Querier exposing a Prometheus-compatible API, so
    this adapter is thin: it targets the in-cluster monitoring endpoint and
    reuses the vanilla Prometheus HTTP adapter for query execution and parsing.
    """

    def __init__(
        self,
        endpoint: str,
        token: str | None = None,
        delegate: MetricsQueryPort | None = None,
    ) -> None:
        self._endpoint = endpoint
        self._token = token
        self._delegate = delegate

    @property
    def endpoint(self) -> str:
        return self._endpoint

    def instant_query(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        return self._prometheus().instant_query(promql, timeout_seconds)

    def range_query(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        return self._prometheus().range_query(promql, start, end, step, timeout_seconds)

    def _prometheus(self) -> MetricsQueryPort:
        if self._delegate is None:
            from hexawyn.adapters.secondary.gitops.prometheus_http_adapter import (
                PrometheusHTTPAdapter,
            )

            self._delegate = PrometheusHTTPAdapter(self._endpoint, token=self._token)
        return self._delegate
