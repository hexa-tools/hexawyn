from __future__ import annotations

from collections.abc import Callable
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
from hexawyn.infrastructure.adapters.secondary.gitops.prometheus_http_adapter import (
    _error_detail,
    _instant_query_params,
    _range_query_params,
    _to_instant_sample,
    _to_range_sample,
)

_PROMETHEUS_SCOPE = "https://prometheus.monitor.azure.com/.default"
_HTTP_BAD_REQUEST = 400


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁAzureMonitorMetricsAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAzureMonitorMetricsAdapterǁrange_query__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAzureMonitorMetricsAdapterǁ_auth_headers__mutmut: MutantDict = {}  # type: ignore
mutants_xǁAzureMonitorMetricsAdapterǁ_client_or_create__mutmut: MutantDict = {}  # type: ignore


class AzureMonitorMetricsAdapter(MetricsQueryPort):
    """MetricsQueryPort backed by Azure Monitor managed service for Prometheus.

    The managed Prometheus query endpoint is Prometheus-compatible, so this
    adapter is thin: it targets the workspace query endpoint and injects an
    Azure AD bearer token per request, reusing the vanilla Prometheus parsing.
    """

    @_mutmut_mutated(mutants_xǁAzureMonitorMetricsAdapterǁ__init____mutmut)
    def __init__(
        self,
        endpoint: str,
        http_client: httpx.Client | None = None,
        token_provider: Callable[[], str] | None = None,
    ) -> None:
        self._endpoint = endpoint.rstrip("/")
        self._http_client = http_client
        self._token_provider = token_provider

    def xǁAzureMonitorMetricsAdapterǁ__init____mutmut_orig(
        self,
        endpoint: str,
        http_client: httpx.Client | None = None,
        token_provider: Callable[[], str] | None = None,
    ) -> None:
        self._endpoint = endpoint.rstrip("/")
        self._http_client = http_client
        self._token_provider = token_provider

    def xǁAzureMonitorMetricsAdapterǁ__init____mutmut_1(
        self,
        endpoint: str,
        http_client: httpx.Client | None = None,
        token_provider: Callable[[], str] | None = None,
    ) -> None:
        self._endpoint = None
        self._http_client = http_client
        self._token_provider = token_provider

    def xǁAzureMonitorMetricsAdapterǁ__init____mutmut_2(
        self,
        endpoint: str,
        http_client: httpx.Client | None = None,
        token_provider: Callable[[], str] | None = None,
    ) -> None:
        self._endpoint = endpoint.rstrip(None)
        self._http_client = http_client
        self._token_provider = token_provider

    def xǁAzureMonitorMetricsAdapterǁ__init____mutmut_3(
        self,
        endpoint: str,
        http_client: httpx.Client | None = None,
        token_provider: Callable[[], str] | None = None,
    ) -> None:
        self._endpoint = endpoint.lstrip("/")
        self._http_client = http_client
        self._token_provider = token_provider

    def xǁAzureMonitorMetricsAdapterǁ__init____mutmut_4(
        self,
        endpoint: str,
        http_client: httpx.Client | None = None,
        token_provider: Callable[[], str] | None = None,
    ) -> None:
        self._endpoint = endpoint.rstrip("XX/XX")
        self._http_client = http_client
        self._token_provider = token_provider

    def xǁAzureMonitorMetricsAdapterǁ__init____mutmut_5(
        self,
        endpoint: str,
        http_client: httpx.Client | None = None,
        token_provider: Callable[[], str] | None = None,
    ) -> None:
        self._endpoint = endpoint.rstrip("/")
        self._http_client = None
        self._token_provider = token_provider

    def xǁAzureMonitorMetricsAdapterǁ__init____mutmut_6(
        self,
        endpoint: str,
        http_client: httpx.Client | None = None,
        token_provider: Callable[[], str] | None = None,
    ) -> None:
        self._endpoint = endpoint.rstrip("/")
        self._http_client = http_client
        self._token_provider = None

    @property
    def endpoint(self) -> str:
        return self._endpoint

    @_mutmut_mutated(mutants_xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut)
    def instant_query(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query",
            _instant_query_params(promql),
            promql,
            timeout_seconds,
        )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_orig(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query",
            _instant_query_params(promql),
            promql,
            timeout_seconds,
        )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_1(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        raw_results = None
        return [_to_instant_sample(item) for item in raw_results]

    def xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_2(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        raw_results = self._execute(
            None,
            _instant_query_params(promql),
            promql,
            timeout_seconds,
        )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_3(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query",
            None,
            promql,
            timeout_seconds,
        )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_4(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query",
            _instant_query_params(promql),
            None,
            timeout_seconds,
        )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_5(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query",
            _instant_query_params(promql),
            promql,
            None,
        )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_6(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        raw_results = self._execute(
            _instant_query_params(promql),
            promql,
            timeout_seconds,
        )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_7(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query",
            promql,
            timeout_seconds,
        )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_8(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query",
            _instant_query_params(promql),
            timeout_seconds,
        )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_9(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query",
            _instant_query_params(promql),
            promql,
            )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_10(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query",
            _instant_query_params(None),
            promql,
            timeout_seconds,
        )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_11(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query",
            _instant_query_params(promql),
            promql,
            timeout_seconds,
        )
        return [_to_instant_sample(None) for item in raw_results]

    @_mutmut_mutated(mutants_xǁAzureMonitorMetricsAdapterǁrange_query__mutmut)
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

    def xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_orig(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range",
            _range_query_params(promql, start, end, step),
            promql,
            timeout_seconds,
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_1(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = None
        return [_to_range_sample(item) for item in raw_results]

    def xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_2(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            None,
            _range_query_params(promql, start, end, step),
            promql,
            timeout_seconds,
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_3(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range",
            None,
            promql,
            timeout_seconds,
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_4(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range",
            _range_query_params(promql, start, end, step),
            None,
            timeout_seconds,
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_5(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range",
            _range_query_params(promql, start, end, step),
            promql,
            None,
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_6(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            _range_query_params(promql, start, end, step),
            promql,
            timeout_seconds,
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_7(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range",
            promql,
            timeout_seconds,
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_8(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range",
            _range_query_params(promql, start, end, step),
            timeout_seconds,
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_9(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range",
            _range_query_params(promql, start, end, step),
            promql,
            )
        return [_to_range_sample(item) for item in raw_results]

    def xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_10(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range",
            _range_query_params(None, start, end, step),
            promql,
            timeout_seconds,
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_11(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range",
            _range_query_params(promql, None, end, step),
            promql,
            timeout_seconds,
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_12(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range",
            _range_query_params(promql, start, None, step),
            promql,
            timeout_seconds,
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_13(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range",
            _range_query_params(promql, start, end, None),
            promql,
            timeout_seconds,
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_14(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range",
            _range_query_params(start, end, step),
            promql,
            timeout_seconds,
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_15(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range",
            _range_query_params(promql, end, step),
            promql,
            timeout_seconds,
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_16(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range",
            _range_query_params(promql, start, step),
            promql,
            timeout_seconds,
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_17(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range",
            _range_query_params(promql, start, end, ),
            promql,
            timeout_seconds,
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_18(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range",
            _range_query_params(promql, start, end, step),
            promql,
            timeout_seconds,
        )
        return [_to_range_sample(None) for item in raw_results]

    @_mutmut_mutated(mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut)
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

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_orig(
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

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_1(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = None
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

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_2(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = None
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

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_3(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = self._auth_headers()
        try:
            response = None
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

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_4(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = self._auth_headers()
        try:
            response = client.get(None, params=params, headers=headers, timeout=timeout_seconds)
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

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_5(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = self._auth_headers()
        try:
            response = client.get(url, params=None, headers=headers, timeout=timeout_seconds)
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

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_6(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = self._auth_headers()
        try:
            response = client.get(url, params=params, headers=None, timeout=timeout_seconds)
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

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_7(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = self._auth_headers()
        try:
            response = client.get(url, params=params, headers=headers, timeout=None)
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

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_8(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = self._auth_headers()
        try:
            response = client.get(params=params, headers=headers, timeout=timeout_seconds)
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

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_9(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = self._auth_headers()
        try:
            response = client.get(url, headers=headers, timeout=timeout_seconds)
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

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_10(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = self._auth_headers()
        try:
            response = client.get(url, params=params, timeout=timeout_seconds)
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

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_11(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = self._auth_headers()
        try:
            response = client.get(url, params=params, headers=headers, )
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

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_12(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = self._auth_headers()
        try:
            response = client.get(url, params=params, headers=headers, timeout=timeout_seconds)
        except httpx.TimeoutException as exc:
            raise AdapterTimeoutError(
                None,
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

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_13(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = self._auth_headers()
        try:
            response = client.get(url, params=params, headers=headers, timeout=timeout_seconds)
        except httpx.TimeoutException as exc:
            raise AdapterTimeoutError(
                f"Azure Monitor Prometheus query timed out after {timeout_seconds}s",
                context=None,
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

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_14(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = self._auth_headers()
        try:
            response = client.get(url, params=params, headers=headers, timeout=timeout_seconds)
        except httpx.TimeoutException as exc:
            raise AdapterTimeoutError(
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

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_15(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = self._auth_headers()
        try:
            response = client.get(url, params=params, headers=headers, timeout=timeout_seconds)
        except httpx.TimeoutException as exc:
            raise AdapterTimeoutError(
                f"Azure Monitor Prometheus query timed out after {timeout_seconds}s",
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

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_16(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = self._auth_headers()
        try:
            response = client.get(url, params=params, headers=headers, timeout=timeout_seconds)
        except httpx.TimeoutException as exc:
            raise AdapterTimeoutError(
                f"Azure Monitor Prometheus query timed out after {timeout_seconds}s",
                context={"XXendpointXX": self._endpoint, "promql": promql},
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

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_17(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = self._auth_headers()
        try:
            response = client.get(url, params=params, headers=headers, timeout=timeout_seconds)
        except httpx.TimeoutException as exc:
            raise AdapterTimeoutError(
                f"Azure Monitor Prometheus query timed out after {timeout_seconds}s",
                context={"ENDPOINT": self._endpoint, "promql": promql},
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

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_18(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = self._auth_headers()
        try:
            response = client.get(url, params=params, headers=headers, timeout=timeout_seconds)
        except httpx.TimeoutException as exc:
            raise AdapterTimeoutError(
                f"Azure Monitor Prometheus query timed out after {timeout_seconds}s",
                context={"endpoint": self._endpoint, "XXpromqlXX": promql},
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

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_19(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = self._auth_headers()
        try:
            response = client.get(url, params=params, headers=headers, timeout=timeout_seconds)
        except httpx.TimeoutException as exc:
            raise AdapterTimeoutError(
                f"Azure Monitor Prometheus query timed out after {timeout_seconds}s",
                context={"endpoint": self._endpoint, "PROMQL": promql},
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

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_20(
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
            raise PrometheusUnavailableError(None) from exc

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

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_21(
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

        if response.status_code != _HTTP_BAD_REQUEST:
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

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_22(
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
            raise PrometheusQueryError(promql=None, detail=_error_detail(response))

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

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_23(
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
            raise PrometheusQueryError(promql=promql, detail=None)

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

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_24(
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
            raise PrometheusQueryError(detail=_error_detail(response))

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

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_25(
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
            raise PrometheusQueryError(promql=promql, )

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

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_26(
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
            raise PrometheusQueryError(promql=promql, detail=_error_detail(None))

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

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_27(
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
            raise PrometheusUnavailableError(None) from exc

        body: dict[str, object] = response.json()
        data = body.get("data")
        if not isinstance(data, dict):
            return []
        result = data.get("result")
        if not isinstance(result, list):
            return []
        return cast(list[dict[str, object]], result)

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_28(
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

        body: dict[str, object] = None
        data = body.get("data")
        if not isinstance(data, dict):
            return []
        result = data.get("result")
        if not isinstance(result, list):
            return []
        return cast(list[dict[str, object]], result)

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_29(
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
        data = None
        if not isinstance(data, dict):
            return []
        result = data.get("result")
        if not isinstance(result, list):
            return []
        return cast(list[dict[str, object]], result)

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_30(
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
        data = body.get(None)
        if not isinstance(data, dict):
            return []
        result = data.get("result")
        if not isinstance(result, list):
            return []
        return cast(list[dict[str, object]], result)

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_31(
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
        data = body.get("XXdataXX")
        if not isinstance(data, dict):
            return []
        result = data.get("result")
        if not isinstance(result, list):
            return []
        return cast(list[dict[str, object]], result)

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_32(
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
        data = body.get("DATA")
        if not isinstance(data, dict):
            return []
        result = data.get("result")
        if not isinstance(result, list):
            return []
        return cast(list[dict[str, object]], result)

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_33(
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
        if isinstance(data, dict):
            return []
        result = data.get("result")
        if not isinstance(result, list):
            return []
        return cast(list[dict[str, object]], result)

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_34(
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
        result = None
        if not isinstance(result, list):
            return []
        return cast(list[dict[str, object]], result)

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_35(
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
        result = data.get(None)
        if not isinstance(result, list):
            return []
        return cast(list[dict[str, object]], result)

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_36(
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
        result = data.get("XXresultXX")
        if not isinstance(result, list):
            return []
        return cast(list[dict[str, object]], result)

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_37(
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
        result = data.get("RESULT")
        if not isinstance(result, list):
            return []
        return cast(list[dict[str, object]], result)

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_38(
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
        if isinstance(result, list):
            return []
        return cast(list[dict[str, object]], result)

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_39(
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
        return cast(None, result)

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_40(
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
        return cast(list[dict[str, object]], None)

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_41(
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
        return cast(result)

    def xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_42(
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
        return cast(list[dict[str, object]], )

    @_mutmut_mutated(mutants_xǁAzureMonitorMetricsAdapterǁ_auth_headers__mutmut)
    def _auth_headers(self) -> dict[str, str]:
        from azure.core.exceptions import ClientAuthenticationError

        try:
            bearer = self._token_provider() if self._token_provider else _acquire_azure_token()
        except ClientAuthenticationError as exc:
            raise PrometheusUnavailableError(self._endpoint) from exc
        return {"Authorization": f"Bearer {bearer}"}

    def xǁAzureMonitorMetricsAdapterǁ_auth_headers__mutmut_orig(self) -> dict[str, str]:
        from azure.core.exceptions import ClientAuthenticationError

        try:
            bearer = self._token_provider() if self._token_provider else _acquire_azure_token()
        except ClientAuthenticationError as exc:
            raise PrometheusUnavailableError(self._endpoint) from exc
        return {"Authorization": f"Bearer {bearer}"}

    def xǁAzureMonitorMetricsAdapterǁ_auth_headers__mutmut_1(self) -> dict[str, str]:
        from azure.core.exceptions import ClientAuthenticationError

        try:
            bearer = None
        except ClientAuthenticationError as exc:
            raise PrometheusUnavailableError(self._endpoint) from exc
        return {"Authorization": f"Bearer {bearer}"}

    def xǁAzureMonitorMetricsAdapterǁ_auth_headers__mutmut_2(self) -> dict[str, str]:
        from azure.core.exceptions import ClientAuthenticationError

        try:
            bearer = self._token_provider() if self._token_provider else _acquire_azure_token()
        except ClientAuthenticationError as exc:
            raise PrometheusUnavailableError(None) from exc
        return {"Authorization": f"Bearer {bearer}"}

    def xǁAzureMonitorMetricsAdapterǁ_auth_headers__mutmut_3(self) -> dict[str, str]:
        from azure.core.exceptions import ClientAuthenticationError

        try:
            bearer = self._token_provider() if self._token_provider else _acquire_azure_token()
        except ClientAuthenticationError as exc:
            raise PrometheusUnavailableError(self._endpoint) from exc
        return {"XXAuthorizationXX": f"Bearer {bearer}"}

    def xǁAzureMonitorMetricsAdapterǁ_auth_headers__mutmut_4(self) -> dict[str, str]:
        from azure.core.exceptions import ClientAuthenticationError

        try:
            bearer = self._token_provider() if self._token_provider else _acquire_azure_token()
        except ClientAuthenticationError as exc:
            raise PrometheusUnavailableError(self._endpoint) from exc
        return {"authorization": f"Bearer {bearer}"}

    def xǁAzureMonitorMetricsAdapterǁ_auth_headers__mutmut_5(self) -> dict[str, str]:
        from azure.core.exceptions import ClientAuthenticationError

        try:
            bearer = self._token_provider() if self._token_provider else _acquire_azure_token()
        except ClientAuthenticationError as exc:
            raise PrometheusUnavailableError(self._endpoint) from exc
        return {"AUTHORIZATION": f"Bearer {bearer}"}

    @_mutmut_mutated(mutants_xǁAzureMonitorMetricsAdapterǁ_client_or_create__mutmut)
    def _client_or_create(self) -> httpx.Client:
        if self._http_client is None:
            self._http_client = httpx.Client()
        return self._http_client

    def xǁAzureMonitorMetricsAdapterǁ_client_or_create__mutmut_orig(self) -> httpx.Client:
        if self._http_client is None:
            self._http_client = httpx.Client()
        return self._http_client

    def xǁAzureMonitorMetricsAdapterǁ_client_or_create__mutmut_1(self) -> httpx.Client:
        if self._http_client is not None:
            self._http_client = httpx.Client()
        return self._http_client

    def xǁAzureMonitorMetricsAdapterǁ_client_or_create__mutmut_2(self) -> httpx.Client:
        if self._http_client is None:
            self._http_client = None
        return self._http_client

mutants_xǁAzureMonitorMetricsAdapterǁ__init____mutmut['_mutmut_orig'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ__init____mutmut['xǁAzureMonitorMetricsAdapterǁ__init____mutmut_1'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ__init____mutmut['xǁAzureMonitorMetricsAdapterǁ__init____mutmut_2'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ__init____mutmut['xǁAzureMonitorMetricsAdapterǁ__init____mutmut_3'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ__init____mutmut['xǁAzureMonitorMetricsAdapterǁ__init____mutmut_4'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ__init____mutmut['xǁAzureMonitorMetricsAdapterǁ__init____mutmut_5'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ__init____mutmut['xǁAzureMonitorMetricsAdapterǁ__init____mutmut_6'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ__init____mutmut_6 # type: ignore # mutmut generated

mutants_xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut['_mutmut_orig'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut['xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_1'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut['xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_2'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut['xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_3'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut['xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_4'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut['xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_5'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut['xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_6'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut['xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_7'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut['xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_8'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut['xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_9'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut['xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_10'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut['xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_11'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁinstant_query__mutmut_11 # type: ignore # mutmut generated

mutants_xǁAzureMonitorMetricsAdapterǁrange_query__mutmut['_mutmut_orig'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁrange_query__mutmut['xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_1'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁrange_query__mutmut['xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_2'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁrange_query__mutmut['xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_3'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁrange_query__mutmut['xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_4'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁrange_query__mutmut['xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_5'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁrange_query__mutmut['xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_6'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁrange_query__mutmut['xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_7'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁrange_query__mutmut['xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_8'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁrange_query__mutmut['xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_9'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁrange_query__mutmut['xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_10'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁrange_query__mutmut['xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_11'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁrange_query__mutmut['xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_12'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁrange_query__mutmut['xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_13'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁrange_query__mutmut['xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_14'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁrange_query__mutmut['xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_15'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁrange_query__mutmut['xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_16'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁrange_query__mutmut['xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_17'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁrange_query__mutmut['xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_18'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁrange_query__mutmut_18 # type: ignore # mutmut generated

mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['_mutmut_orig'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_1'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_2'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_3'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_4'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_5'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_6'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_7'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_8'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_9'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_10'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_11'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_12'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_13'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_14'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_15'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_16'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_17'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_18'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_19'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_20'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_21'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_22'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_23'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_24'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_25'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_26'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_27'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_28'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_29'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_30'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_31'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_32'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_33'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_34'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_35'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_36'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_37'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_38'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_39'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_39 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_40'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_40 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_41'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_41 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_execute__mutmut['xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_42'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_execute__mutmut_42 # type: ignore # mutmut generated

mutants_xǁAzureMonitorMetricsAdapterǁ_auth_headers__mutmut['_mutmut_orig'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_auth_headers__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_auth_headers__mutmut['xǁAzureMonitorMetricsAdapterǁ_auth_headers__mutmut_1'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_auth_headers__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_auth_headers__mutmut['xǁAzureMonitorMetricsAdapterǁ_auth_headers__mutmut_2'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_auth_headers__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_auth_headers__mutmut['xǁAzureMonitorMetricsAdapterǁ_auth_headers__mutmut_3'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_auth_headers__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_auth_headers__mutmut['xǁAzureMonitorMetricsAdapterǁ_auth_headers__mutmut_4'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_auth_headers__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_auth_headers__mutmut['xǁAzureMonitorMetricsAdapterǁ_auth_headers__mutmut_5'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_auth_headers__mutmut_5 # type: ignore # mutmut generated

mutants_xǁAzureMonitorMetricsAdapterǁ_client_or_create__mutmut['_mutmut_orig'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_client_or_create__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_client_or_create__mutmut['xǁAzureMonitorMetricsAdapterǁ_client_or_create__mutmut_1'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_client_or_create__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAzureMonitorMetricsAdapterǁ_client_or_create__mutmut['xǁAzureMonitorMetricsAdapterǁ_client_or_create__mutmut_2'] = AzureMonitorMetricsAdapter.xǁAzureMonitorMetricsAdapterǁ_client_or_create__mutmut_2 # type: ignore # mutmut generated
mutants_x__acquire_azure_token__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__acquire_azure_token__mutmut)
def _acquire_azure_token() -> str:
    from azure.identity import DefaultAzureCredential

    credential = DefaultAzureCredential()
    granted = credential.get_token(_PROMETHEUS_SCOPE)
    return str(granted.token)


def x__acquire_azure_token__mutmut_orig() -> str:
    from azure.identity import DefaultAzureCredential

    credential = DefaultAzureCredential()
    granted = credential.get_token(_PROMETHEUS_SCOPE)
    return str(granted.token)


def x__acquire_azure_token__mutmut_1() -> str:
    from azure.identity import DefaultAzureCredential

    credential = None
    granted = credential.get_token(_PROMETHEUS_SCOPE)
    return str(granted.token)


def x__acquire_azure_token__mutmut_2() -> str:
    from azure.identity import DefaultAzureCredential

    credential = DefaultAzureCredential()
    granted = None
    return str(granted.token)


def x__acquire_azure_token__mutmut_3() -> str:
    from azure.identity import DefaultAzureCredential

    credential = DefaultAzureCredential()
    granted = credential.get_token(None)
    return str(granted.token)


def x__acquire_azure_token__mutmut_4() -> str:
    from azure.identity import DefaultAzureCredential

    credential = DefaultAzureCredential()
    granted = credential.get_token(_PROMETHEUS_SCOPE)
    return str(None)

mutants_x__acquire_azure_token__mutmut['_mutmut_orig'] = x__acquire_azure_token__mutmut_orig # type: ignore # mutmut generated
mutants_x__acquire_azure_token__mutmut['x__acquire_azure_token__mutmut_1'] = x__acquire_azure_token__mutmut_1 # type: ignore # mutmut generated
mutants_x__acquire_azure_token__mutmut['x__acquire_azure_token__mutmut_2'] = x__acquire_azure_token__mutmut_2 # type: ignore # mutmut generated
mutants_x__acquire_azure_token__mutmut['x__acquire_azure_token__mutmut_3'] = x__acquire_azure_token__mutmut_3 # type: ignore # mutmut generated
mutants_x__acquire_azure_token__mutmut['x__acquire_azure_token__mutmut_4'] = x__acquire_azure_token__mutmut_4 # type: ignore # mutmut generated
