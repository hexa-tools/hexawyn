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

_MONITORING_SCOPE = "https://www.googleapis.com/auth/monitoring.read"
_HTTP_BAD_REQUEST = 400


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁGCPManagedPrometheusAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGCPManagedPrometheusAdapterǁrange_query__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGCPManagedPrometheusAdapterǁ_auth_headers__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGCPManagedPrometheusAdapterǁ_client_or_create__mutmut: MutantDict = {}  # type: ignore


class GCPManagedPrometheusAdapter(MetricsQueryPort):
    """MetricsQueryPort backed by GCP Managed Prometheus.

    Managed Prometheus exposes a Prometheus-compatible query API, so this
    adapter is thin: it targets the GMP endpoint and injects a refreshed
    Google bearer token per request, reusing the vanilla Prometheus parsing.
    """

    @_mutmut_mutated(mutants_xǁGCPManagedPrometheusAdapterǁ__init____mutmut)
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

    def xǁGCPManagedPrometheusAdapterǁ__init____mutmut_orig(
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

    def xǁGCPManagedPrometheusAdapterǁ__init____mutmut_1(
        self,
        project_id: str,
        http_client: httpx.Client | None = None,
        token_provider: Callable[[], str] | None = None,
    ) -> None:
        self._project_id = None
        self._endpoint = (
            f"https://monitoring.googleapis.com/v1/projects/{project_id}/location/global/prometheus"
        )
        self._http_client = http_client
        self._token_provider = token_provider

    def xǁGCPManagedPrometheusAdapterǁ__init____mutmut_2(
        self,
        project_id: str,
        http_client: httpx.Client | None = None,
        token_provider: Callable[[], str] | None = None,
    ) -> None:
        self._project_id = project_id
        self._endpoint = None
        self._http_client = http_client
        self._token_provider = token_provider

    def xǁGCPManagedPrometheusAdapterǁ__init____mutmut_3(
        self,
        project_id: str,
        http_client: httpx.Client | None = None,
        token_provider: Callable[[], str] | None = None,
    ) -> None:
        self._project_id = project_id
        self._endpoint = (
            f"https://monitoring.googleapis.com/v1/projects/{project_id}/location/global/prometheus"
        )
        self._http_client = None
        self._token_provider = token_provider

    def xǁGCPManagedPrometheusAdapterǁ__init____mutmut_4(
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
        self._token_provider = None

    @property
    def endpoint(self) -> str:
        return self._endpoint

    @_mutmut_mutated(mutants_xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut)
    def instant_query(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query",
            _instant_query_params(promql),
            promql,
            timeout_seconds,
        )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_orig(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query",
            _instant_query_params(promql),
            promql,
            timeout_seconds,
        )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_1(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        raw_results = None
        return [_to_instant_sample(item) for item in raw_results]

    def xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_2(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        raw_results = self._execute(
            None,
            _instant_query_params(promql),
            promql,
            timeout_seconds,
        )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_3(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query",
            None,
            promql,
            timeout_seconds,
        )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_4(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query",
            _instant_query_params(promql),
            None,
            timeout_seconds,
        )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_5(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query",
            _instant_query_params(promql),
            promql,
            None,
        )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_6(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        raw_results = self._execute(
            _instant_query_params(promql),
            promql,
            timeout_seconds,
        )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_7(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query",
            promql,
            timeout_seconds,
        )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_8(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query",
            _instant_query_params(promql),
            timeout_seconds,
        )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_9(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query",
            _instant_query_params(promql),
            promql,
            )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_10(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query",
            _instant_query_params(None),
            promql,
            timeout_seconds,
        )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_11(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query",
            _instant_query_params(promql),
            promql,
            timeout_seconds,
        )
        return [_to_instant_sample(None) for item in raw_results]

    @_mutmut_mutated(mutants_xǁGCPManagedPrometheusAdapterǁrange_query__mutmut)
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

    def xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_orig(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range",
            _range_query_params(promql, start, end, step),
            promql,
            timeout_seconds,
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_1(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = None
        return [_to_range_sample(item) for item in raw_results]

    def xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_2(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            None,
            _range_query_params(promql, start, end, step),
            promql,
            timeout_seconds,
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_3(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range",
            None,
            promql,
            timeout_seconds,
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_4(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range",
            _range_query_params(promql, start, end, step),
            None,
            timeout_seconds,
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_5(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range",
            _range_query_params(promql, start, end, step),
            promql,
            None,
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_6(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            _range_query_params(promql, start, end, step),
            promql,
            timeout_seconds,
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_7(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range",
            promql,
            timeout_seconds,
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_8(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range",
            _range_query_params(promql, start, end, step),
            timeout_seconds,
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_9(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range",
            _range_query_params(promql, start, end, step),
            promql,
            )
        return [_to_range_sample(item) for item in raw_results]

    def xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_10(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range",
            _range_query_params(None, start, end, step),
            promql,
            timeout_seconds,
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_11(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range",
            _range_query_params(promql, None, end, step),
            promql,
            timeout_seconds,
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_12(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range",
            _range_query_params(promql, start, None, step),
            promql,
            timeout_seconds,
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_13(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range",
            _range_query_params(promql, start, end, None),
            promql,
            timeout_seconds,
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_14(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range",
            _range_query_params(start, end, step),
            promql,
            timeout_seconds,
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_15(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range",
            _range_query_params(promql, end, step),
            promql,
            timeout_seconds,
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_16(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range",
            _range_query_params(promql, start, step),
            promql,
            timeout_seconds,
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_17(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range",
            _range_query_params(promql, start, end, ),
            promql,
            timeout_seconds,
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_18(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range",
            _range_query_params(promql, start, end, step),
            promql,
            timeout_seconds,
        )
        return [_to_range_sample(None) for item in raw_results]

    @_mutmut_mutated(mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut)
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

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_orig(
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

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_1(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = None
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

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_2(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = None
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

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_3(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = self._auth_headers()
        try:
            response = None
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

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_4(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = self._auth_headers()
        try:
            response = client.get(None, params=params, headers=headers, timeout=timeout_seconds)
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

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_5(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = self._auth_headers()
        try:
            response = client.get(url, params=None, headers=headers, timeout=timeout_seconds)
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

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_6(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = self._auth_headers()
        try:
            response = client.get(url, params=params, headers=None, timeout=timeout_seconds)
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

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_7(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = self._auth_headers()
        try:
            response = client.get(url, params=params, headers=headers, timeout=None)
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

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_8(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = self._auth_headers()
        try:
            response = client.get(params=params, headers=headers, timeout=timeout_seconds)
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

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_9(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = self._auth_headers()
        try:
            response = client.get(url, headers=headers, timeout=timeout_seconds)
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

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_10(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = self._auth_headers()
        try:
            response = client.get(url, params=params, timeout=timeout_seconds)
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

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_11(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = self._auth_headers()
        try:
            response = client.get(url, params=params, headers=headers, )
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

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_12(
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

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_13(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = self._auth_headers()
        try:
            response = client.get(url, params=params, headers=headers, timeout=timeout_seconds)
        except httpx.TimeoutException as exc:
            raise AdapterTimeoutError(
                f"GCP Managed Prometheus query timed out after {timeout_seconds}s",
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

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_14(
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

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_15(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = self._auth_headers()
        try:
            response = client.get(url, params=params, headers=headers, timeout=timeout_seconds)
        except httpx.TimeoutException as exc:
            raise AdapterTimeoutError(
                f"GCP Managed Prometheus query timed out after {timeout_seconds}s",
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

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_16(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = self._auth_headers()
        try:
            response = client.get(url, params=params, headers=headers, timeout=timeout_seconds)
        except httpx.TimeoutException as exc:
            raise AdapterTimeoutError(
                f"GCP Managed Prometheus query timed out after {timeout_seconds}s",
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

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_17(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = self._auth_headers()
        try:
            response = client.get(url, params=params, headers=headers, timeout=timeout_seconds)
        except httpx.TimeoutException as exc:
            raise AdapterTimeoutError(
                f"GCP Managed Prometheus query timed out after {timeout_seconds}s",
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

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_18(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = self._auth_headers()
        try:
            response = client.get(url, params=params, headers=headers, timeout=timeout_seconds)
        except httpx.TimeoutException as exc:
            raise AdapterTimeoutError(
                f"GCP Managed Prometheus query timed out after {timeout_seconds}s",
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

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_19(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        client = self._client_or_create()
        headers = self._auth_headers()
        try:
            response = client.get(url, params=params, headers=headers, timeout=timeout_seconds)
        except httpx.TimeoutException as exc:
            raise AdapterTimeoutError(
                f"GCP Managed Prometheus query timed out after {timeout_seconds}s",
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

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_20(
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

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_21(
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

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_22(
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

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_23(
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

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_24(
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

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_25(
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

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_26(
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

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_27(
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
            raise PrometheusUnavailableError(None) from exc

        body: dict[str, object] = response.json()
        data = body.get("data")
        if not isinstance(data, dict):
            return []
        result = data.get("result")
        if not isinstance(result, list):
            return []
        return cast(list[dict[str, object]], result)

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_28(
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

        body: dict[str, object] = None
        data = body.get("data")
        if not isinstance(data, dict):
            return []
        result = data.get("result")
        if not isinstance(result, list):
            return []
        return cast(list[dict[str, object]], result)

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_29(
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
        data = None
        if not isinstance(data, dict):
            return []
        result = data.get("result")
        if not isinstance(result, list):
            return []
        return cast(list[dict[str, object]], result)

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_30(
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
        data = body.get(None)
        if not isinstance(data, dict):
            return []
        result = data.get("result")
        if not isinstance(result, list):
            return []
        return cast(list[dict[str, object]], result)

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_31(
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
        data = body.get("XXdataXX")
        if not isinstance(data, dict):
            return []
        result = data.get("result")
        if not isinstance(result, list):
            return []
        return cast(list[dict[str, object]], result)

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_32(
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
        data = body.get("DATA")
        if not isinstance(data, dict):
            return []
        result = data.get("result")
        if not isinstance(result, list):
            return []
        return cast(list[dict[str, object]], result)

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_33(
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
        if isinstance(data, dict):
            return []
        result = data.get("result")
        if not isinstance(result, list):
            return []
        return cast(list[dict[str, object]], result)

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_34(
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
        result = None
        if not isinstance(result, list):
            return []
        return cast(list[dict[str, object]], result)

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_35(
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
        result = data.get(None)
        if not isinstance(result, list):
            return []
        return cast(list[dict[str, object]], result)

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_36(
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
        result = data.get("XXresultXX")
        if not isinstance(result, list):
            return []
        return cast(list[dict[str, object]], result)

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_37(
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
        result = data.get("RESULT")
        if not isinstance(result, list):
            return []
        return cast(list[dict[str, object]], result)

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_38(
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
        if isinstance(result, list):
            return []
        return cast(list[dict[str, object]], result)

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_39(
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
        return cast(None, result)

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_40(
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
        return cast(list[dict[str, object]], None)

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_41(
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
        return cast(result)

    def xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_42(
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
        return cast(list[dict[str, object]], )

    @_mutmut_mutated(mutants_xǁGCPManagedPrometheusAdapterǁ_auth_headers__mutmut)
    def _auth_headers(self) -> dict[str, str]:
        from google.auth.exceptions import DefaultCredentialsError

        try:
            bearer = self._token_provider() if self._token_provider else _acquire_google_token()
        except DefaultCredentialsError as exc:
            raise PrometheusUnavailableError(self._endpoint) from exc
        return {"Authorization": f"Bearer {bearer}"}

    def xǁGCPManagedPrometheusAdapterǁ_auth_headers__mutmut_orig(self) -> dict[str, str]:
        from google.auth.exceptions import DefaultCredentialsError

        try:
            bearer = self._token_provider() if self._token_provider else _acquire_google_token()
        except DefaultCredentialsError as exc:
            raise PrometheusUnavailableError(self._endpoint) from exc
        return {"Authorization": f"Bearer {bearer}"}

    def xǁGCPManagedPrometheusAdapterǁ_auth_headers__mutmut_1(self) -> dict[str, str]:
        from google.auth.exceptions import DefaultCredentialsError

        try:
            bearer = None
        except DefaultCredentialsError as exc:
            raise PrometheusUnavailableError(self._endpoint) from exc
        return {"Authorization": f"Bearer {bearer}"}

    def xǁGCPManagedPrometheusAdapterǁ_auth_headers__mutmut_2(self) -> dict[str, str]:
        from google.auth.exceptions import DefaultCredentialsError

        try:
            bearer = self._token_provider() if self._token_provider else _acquire_google_token()
        except DefaultCredentialsError as exc:
            raise PrometheusUnavailableError(None) from exc
        return {"Authorization": f"Bearer {bearer}"}

    def xǁGCPManagedPrometheusAdapterǁ_auth_headers__mutmut_3(self) -> dict[str, str]:
        from google.auth.exceptions import DefaultCredentialsError

        try:
            bearer = self._token_provider() if self._token_provider else _acquire_google_token()
        except DefaultCredentialsError as exc:
            raise PrometheusUnavailableError(self._endpoint) from exc
        return {"XXAuthorizationXX": f"Bearer {bearer}"}

    def xǁGCPManagedPrometheusAdapterǁ_auth_headers__mutmut_4(self) -> dict[str, str]:
        from google.auth.exceptions import DefaultCredentialsError

        try:
            bearer = self._token_provider() if self._token_provider else _acquire_google_token()
        except DefaultCredentialsError as exc:
            raise PrometheusUnavailableError(self._endpoint) from exc
        return {"authorization": f"Bearer {bearer}"}

    def xǁGCPManagedPrometheusAdapterǁ_auth_headers__mutmut_5(self) -> dict[str, str]:
        from google.auth.exceptions import DefaultCredentialsError

        try:
            bearer = self._token_provider() if self._token_provider else _acquire_google_token()
        except DefaultCredentialsError as exc:
            raise PrometheusUnavailableError(self._endpoint) from exc
        return {"AUTHORIZATION": f"Bearer {bearer}"}

    @_mutmut_mutated(mutants_xǁGCPManagedPrometheusAdapterǁ_client_or_create__mutmut)
    def _client_or_create(self) -> httpx.Client:
        if self._http_client is None:
            self._http_client = httpx.Client()
        return self._http_client

    def xǁGCPManagedPrometheusAdapterǁ_client_or_create__mutmut_orig(self) -> httpx.Client:
        if self._http_client is None:
            self._http_client = httpx.Client()
        return self._http_client

    def xǁGCPManagedPrometheusAdapterǁ_client_or_create__mutmut_1(self) -> httpx.Client:
        if self._http_client is not None:
            self._http_client = httpx.Client()
        return self._http_client

    def xǁGCPManagedPrometheusAdapterǁ_client_or_create__mutmut_2(self) -> httpx.Client:
        if self._http_client is None:
            self._http_client = None
        return self._http_client

mutants_xǁGCPManagedPrometheusAdapterǁ__init____mutmut['_mutmut_orig'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ__init____mutmut['xǁGCPManagedPrometheusAdapterǁ__init____mutmut_1'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ__init____mutmut['xǁGCPManagedPrometheusAdapterǁ__init____mutmut_2'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ__init____mutmut['xǁGCPManagedPrometheusAdapterǁ__init____mutmut_3'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ__init____mutmut['xǁGCPManagedPrometheusAdapterǁ__init____mutmut_4'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ__init____mutmut_4 # type: ignore # mutmut generated

mutants_xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut['_mutmut_orig'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut['xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_1'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut['xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_2'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut['xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_3'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut['xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_4'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut['xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_5'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut['xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_6'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut['xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_7'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut['xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_8'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut['xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_9'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut['xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_10'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut['xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_11'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁinstant_query__mutmut_11 # type: ignore # mutmut generated

mutants_xǁGCPManagedPrometheusAdapterǁrange_query__mutmut['_mutmut_orig'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁrange_query__mutmut['xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_1'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁrange_query__mutmut['xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_2'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁrange_query__mutmut['xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_3'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁrange_query__mutmut['xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_4'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁrange_query__mutmut['xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_5'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁrange_query__mutmut['xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_6'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁrange_query__mutmut['xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_7'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁrange_query__mutmut['xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_8'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁrange_query__mutmut['xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_9'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁrange_query__mutmut['xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_10'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁrange_query__mutmut['xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_11'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁrange_query__mutmut['xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_12'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁrange_query__mutmut['xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_13'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁrange_query__mutmut['xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_14'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁrange_query__mutmut['xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_15'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁrange_query__mutmut['xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_16'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁrange_query__mutmut['xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_17'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁrange_query__mutmut['xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_18'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁrange_query__mutmut_18 # type: ignore # mutmut generated

mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['_mutmut_orig'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_1'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_2'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_3'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_4'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_5'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_6'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_7'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_8'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_9'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_10'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_11'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_12'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_13'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_14'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_15'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_16'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_17'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_18'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_19'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_20'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_21'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_22'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_23'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_24'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_25'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_26'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_27'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_28'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_29'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_30'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_31'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_32'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_33'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_34'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_35'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_36'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_37'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_38'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_39'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_39 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_40'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_40 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_41'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_41 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_execute__mutmut['xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_42'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_execute__mutmut_42 # type: ignore # mutmut generated

mutants_xǁGCPManagedPrometheusAdapterǁ_auth_headers__mutmut['_mutmut_orig'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_auth_headers__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_auth_headers__mutmut['xǁGCPManagedPrometheusAdapterǁ_auth_headers__mutmut_1'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_auth_headers__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_auth_headers__mutmut['xǁGCPManagedPrometheusAdapterǁ_auth_headers__mutmut_2'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_auth_headers__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_auth_headers__mutmut['xǁGCPManagedPrometheusAdapterǁ_auth_headers__mutmut_3'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_auth_headers__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_auth_headers__mutmut['xǁGCPManagedPrometheusAdapterǁ_auth_headers__mutmut_4'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_auth_headers__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_auth_headers__mutmut['xǁGCPManagedPrometheusAdapterǁ_auth_headers__mutmut_5'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_auth_headers__mutmut_5 # type: ignore # mutmut generated

mutants_xǁGCPManagedPrometheusAdapterǁ_client_or_create__mutmut['_mutmut_orig'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_client_or_create__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_client_or_create__mutmut['xǁGCPManagedPrometheusAdapterǁ_client_or_create__mutmut_1'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_client_or_create__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGCPManagedPrometheusAdapterǁ_client_or_create__mutmut['xǁGCPManagedPrometheusAdapterǁ_client_or_create__mutmut_2'] = GCPManagedPrometheusAdapter.xǁGCPManagedPrometheusAdapterǁ_client_or_create__mutmut_2 # type: ignore # mutmut generated
mutants_x__acquire_google_token__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__acquire_google_token__mutmut)
def _acquire_google_token() -> str:
    from google.auth import default
    from google.auth.transport.requests import Request

    credentials, _ = default(scopes=[_MONITORING_SCOPE])
    credentials.refresh(Request())
    return str(credentials.token)


def x__acquire_google_token__mutmut_orig() -> str:
    from google.auth import default
    from google.auth.transport.requests import Request

    credentials, _ = default(scopes=[_MONITORING_SCOPE])
    credentials.refresh(Request())
    return str(credentials.token)


def x__acquire_google_token__mutmut_1() -> str:
    from google.auth import default
    from google.auth.transport.requests import Request

    credentials, _ = None
    credentials.refresh(Request())
    return str(credentials.token)


def x__acquire_google_token__mutmut_2() -> str:
    from google.auth import default
    from google.auth.transport.requests import Request

    credentials, _ = default(scopes=None)
    credentials.refresh(Request())
    return str(credentials.token)


def x__acquire_google_token__mutmut_3() -> str:
    from google.auth import default
    from google.auth.transport.requests import Request

    credentials, _ = default(scopes=[_MONITORING_SCOPE])
    credentials.refresh(None)
    return str(credentials.token)


def x__acquire_google_token__mutmut_4() -> str:
    from google.auth import default
    from google.auth.transport.requests import Request

    credentials, _ = default(scopes=[_MONITORING_SCOPE])
    credentials.refresh(Request())
    return str(None)

mutants_x__acquire_google_token__mutmut['_mutmut_orig'] = x__acquire_google_token__mutmut_orig # type: ignore # mutmut generated
mutants_x__acquire_google_token__mutmut['x__acquire_google_token__mutmut_1'] = x__acquire_google_token__mutmut_1 # type: ignore # mutmut generated
mutants_x__acquire_google_token__mutmut['x__acquire_google_token__mutmut_2'] = x__acquire_google_token__mutmut_2 # type: ignore # mutmut generated
mutants_x__acquire_google_token__mutmut['x__acquire_google_token__mutmut_3'] = x__acquire_google_token__mutmut_3 # type: ignore # mutmut generated
mutants_x__acquire_google_token__mutmut['x__acquire_google_token__mutmut_4'] = x__acquire_google_token__mutmut_4 # type: ignore # mutmut generated
