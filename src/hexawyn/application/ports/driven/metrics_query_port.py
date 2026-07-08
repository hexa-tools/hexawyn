from abc import ABC, abstractmethod
from typing import TypedDict


class PrometheusInstantSample(TypedDict):
    metric: dict[str, str]
    value: float


class PrometheusRangeSample(TypedDict):
    metric: dict[str, str]
    values: list[tuple[str, float]]


class MetricsQueryPort(ABC):
    """Driven port: executes PromQL instant/range queries against Prometheus."""

    @abstractmethod
    def instant_query(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        """Executes `/api/v1/query`.

        Raises PrometheusUnavailableError when Prometheus is unreachable.
        Raises PrometheusQueryError when Prometheus rejects the PromQL (e.g. HTTP 400).
        Raises AdapterTimeoutError when the query exceeds timeout_seconds.
        """

    @abstractmethod
    def range_query(
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        """Executes `/api/v1/query_range`.

        Raises PrometheusUnavailableError when Prometheus is unreachable.
        Raises PrometheusQueryError when Prometheus rejects the PromQL (e.g. HTTP 400).
        Raises AdapterTimeoutError when the query exceeds timeout_seconds.
        """
