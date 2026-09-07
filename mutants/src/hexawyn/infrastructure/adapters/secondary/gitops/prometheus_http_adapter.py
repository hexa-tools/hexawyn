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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁPrometheusHTTPAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁPrometheusHTTPAdapterǁinstant_query__mutmut: MutantDict = {}  # type: ignore
mutants_xǁPrometheusHTTPAdapterǁrange_query__mutmut: MutantDict = {}  # type: ignore
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut: MutantDict = {}  # type: ignore


class PrometheusHTTPAdapter(MetricsQueryPort):
    @_mutmut_mutated(mutants_xǁPrometheusHTTPAdapterǁ__init____mutmut)
    def __init__(self, endpoint: str, token: str | None = None) -> None:
        self._endpoint = endpoint.rstrip("/")
        headers = {"Authorization": f"Bearer {token}"} if token else {}
        self._client = httpx.Client(headers=headers)
    def xǁPrometheusHTTPAdapterǁ__init____mutmut_orig(self, endpoint: str, token: str | None = None) -> None:
        self._endpoint = endpoint.rstrip("/")
        headers = {"Authorization": f"Bearer {token}"} if token else {}
        self._client = httpx.Client(headers=headers)
    def xǁPrometheusHTTPAdapterǁ__init____mutmut_1(self, endpoint: str, token: str | None = None) -> None:
        self._endpoint = None
        headers = {"Authorization": f"Bearer {token}"} if token else {}
        self._client = httpx.Client(headers=headers)
    def xǁPrometheusHTTPAdapterǁ__init____mutmut_2(self, endpoint: str, token: str | None = None) -> None:
        self._endpoint = endpoint.rstrip(None)
        headers = {"Authorization": f"Bearer {token}"} if token else {}
        self._client = httpx.Client(headers=headers)
    def xǁPrometheusHTTPAdapterǁ__init____mutmut_3(self, endpoint: str, token: str | None = None) -> None:
        self._endpoint = endpoint.lstrip("/")
        headers = {"Authorization": f"Bearer {token}"} if token else {}
        self._client = httpx.Client(headers=headers)
    def xǁPrometheusHTTPAdapterǁ__init____mutmut_4(self, endpoint: str, token: str | None = None) -> None:
        self._endpoint = endpoint.rstrip("XX/XX")
        headers = {"Authorization": f"Bearer {token}"} if token else {}
        self._client = httpx.Client(headers=headers)
    def xǁPrometheusHTTPAdapterǁ__init____mutmut_5(self, endpoint: str, token: str | None = None) -> None:
        self._endpoint = endpoint.rstrip("/")
        headers = None
        self._client = httpx.Client(headers=headers)
    def xǁPrometheusHTTPAdapterǁ__init____mutmut_6(self, endpoint: str, token: str | None = None) -> None:
        self._endpoint = endpoint.rstrip("/")
        headers = {"XXAuthorizationXX": f"Bearer {token}"} if token else {}
        self._client = httpx.Client(headers=headers)
    def xǁPrometheusHTTPAdapterǁ__init____mutmut_7(self, endpoint: str, token: str | None = None) -> None:
        self._endpoint = endpoint.rstrip("/")
        headers = {"authorization": f"Bearer {token}"} if token else {}
        self._client = httpx.Client(headers=headers)
    def xǁPrometheusHTTPAdapterǁ__init____mutmut_8(self, endpoint: str, token: str | None = None) -> None:
        self._endpoint = endpoint.rstrip("/")
        headers = {"AUTHORIZATION": f"Bearer {token}"} if token else {}
        self._client = httpx.Client(headers=headers)
    def xǁPrometheusHTTPAdapterǁ__init____mutmut_9(self, endpoint: str, token: str | None = None) -> None:
        self._endpoint = endpoint.rstrip("/")
        headers = {"Authorization": f"Bearer {token}"} if token else {}
        self._client = None
    def xǁPrometheusHTTPAdapterǁ__init____mutmut_10(self, endpoint: str, token: str | None = None) -> None:
        self._endpoint = endpoint.rstrip("/")
        headers = {"Authorization": f"Bearer {token}"} if token else {}
        self._client = httpx.Client(headers=None)

    def close(self) -> None:
        self._client.close()

    @_mutmut_mutated(mutants_xǁPrometheusHTTPAdapterǁinstant_query__mutmut)
    def instant_query(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        params = _instant_query_params(promql)
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query", params, promql, timeout_seconds
        )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁPrometheusHTTPAdapterǁinstant_query__mutmut_orig(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        params = _instant_query_params(promql)
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query", params, promql, timeout_seconds
        )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁPrometheusHTTPAdapterǁinstant_query__mutmut_1(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        params = None
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query", params, promql, timeout_seconds
        )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁPrometheusHTTPAdapterǁinstant_query__mutmut_2(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        params = _instant_query_params(None)
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query", params, promql, timeout_seconds
        )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁPrometheusHTTPAdapterǁinstant_query__mutmut_3(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        params = _instant_query_params(promql)
        raw_results = None
        return [_to_instant_sample(item) for item in raw_results]

    def xǁPrometheusHTTPAdapterǁinstant_query__mutmut_4(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        params = _instant_query_params(promql)
        raw_results = self._execute(
            None, params, promql, timeout_seconds
        )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁPrometheusHTTPAdapterǁinstant_query__mutmut_5(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        params = _instant_query_params(promql)
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query", None, promql, timeout_seconds
        )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁPrometheusHTTPAdapterǁinstant_query__mutmut_6(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        params = _instant_query_params(promql)
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query", params, None, timeout_seconds
        )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁPrometheusHTTPAdapterǁinstant_query__mutmut_7(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        params = _instant_query_params(promql)
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query", params, promql, None
        )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁPrometheusHTTPAdapterǁinstant_query__mutmut_8(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        params = _instant_query_params(promql)
        raw_results = self._execute(
            params, promql, timeout_seconds
        )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁPrometheusHTTPAdapterǁinstant_query__mutmut_9(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        params = _instant_query_params(promql)
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query", promql, timeout_seconds
        )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁPrometheusHTTPAdapterǁinstant_query__mutmut_10(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        params = _instant_query_params(promql)
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query", params, timeout_seconds
        )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁPrometheusHTTPAdapterǁinstant_query__mutmut_11(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        params = _instant_query_params(promql)
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query", params, promql, )
        return [_to_instant_sample(item) for item in raw_results]

    def xǁPrometheusHTTPAdapterǁinstant_query__mutmut_12(self, promql: str, timeout_seconds: float) -> list[PrometheusInstantSample]:
        params = _instant_query_params(promql)
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query", params, promql, timeout_seconds
        )
        return [_to_instant_sample(None) for item in raw_results]

    @_mutmut_mutated(mutants_xǁPrometheusHTTPAdapterǁrange_query__mutmut)
    def range_query(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        params = _range_query_params(promql, start, end, step)
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range", params, promql, timeout_seconds
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁPrometheusHTTPAdapterǁrange_query__mutmut_orig(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        params = _range_query_params(promql, start, end, step)
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range", params, promql, timeout_seconds
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁPrometheusHTTPAdapterǁrange_query__mutmut_1(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        params = None
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range", params, promql, timeout_seconds
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁPrometheusHTTPAdapterǁrange_query__mutmut_2(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        params = _range_query_params(None, start, end, step)
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range", params, promql, timeout_seconds
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁPrometheusHTTPAdapterǁrange_query__mutmut_3(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        params = _range_query_params(promql, None, end, step)
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range", params, promql, timeout_seconds
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁPrometheusHTTPAdapterǁrange_query__mutmut_4(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        params = _range_query_params(promql, start, None, step)
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range", params, promql, timeout_seconds
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁPrometheusHTTPAdapterǁrange_query__mutmut_5(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        params = _range_query_params(promql, start, end, None)
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range", params, promql, timeout_seconds
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁPrometheusHTTPAdapterǁrange_query__mutmut_6(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        params = _range_query_params(start, end, step)
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range", params, promql, timeout_seconds
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁPrometheusHTTPAdapterǁrange_query__mutmut_7(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        params = _range_query_params(promql, end, step)
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range", params, promql, timeout_seconds
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁPrometheusHTTPAdapterǁrange_query__mutmut_8(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        params = _range_query_params(promql, start, step)
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range", params, promql, timeout_seconds
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁPrometheusHTTPAdapterǁrange_query__mutmut_9(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        params = _range_query_params(promql, start, end, )
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range", params, promql, timeout_seconds
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁPrometheusHTTPAdapterǁrange_query__mutmut_10(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        params = _range_query_params(promql, start, end, step)
        raw_results = None
        return [_to_range_sample(item) for item in raw_results]

    def xǁPrometheusHTTPAdapterǁrange_query__mutmut_11(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        params = _range_query_params(promql, start, end, step)
        raw_results = self._execute(
            None, params, promql, timeout_seconds
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁPrometheusHTTPAdapterǁrange_query__mutmut_12(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        params = _range_query_params(promql, start, end, step)
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range", None, promql, timeout_seconds
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁPrometheusHTTPAdapterǁrange_query__mutmut_13(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        params = _range_query_params(promql, start, end, step)
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range", params, None, timeout_seconds
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁPrometheusHTTPAdapterǁrange_query__mutmut_14(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        params = _range_query_params(promql, start, end, step)
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range", params, promql, None
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁPrometheusHTTPAdapterǁrange_query__mutmut_15(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        params = _range_query_params(promql, start, end, step)
        raw_results = self._execute(
            params, promql, timeout_seconds
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁPrometheusHTTPAdapterǁrange_query__mutmut_16(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        params = _range_query_params(promql, start, end, step)
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range", promql, timeout_seconds
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁPrometheusHTTPAdapterǁrange_query__mutmut_17(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        params = _range_query_params(promql, start, end, step)
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range", params, timeout_seconds
        )
        return [_to_range_sample(item) for item in raw_results]

    def xǁPrometheusHTTPAdapterǁrange_query__mutmut_18(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        params = _range_query_params(promql, start, end, step)
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range", params, promql, )
        return [_to_range_sample(item) for item in raw_results]

    def xǁPrometheusHTTPAdapterǁrange_query__mutmut_19(  # noqa: PLR0913
        self, promql: str, start: str, end: str, step: str, timeout_seconds: float
    ) -> list[PrometheusRangeSample]:
        params = _range_query_params(promql, start, end, step)
        raw_results = self._execute(
            f"{self._endpoint}/api/v1/query_range", params, promql, timeout_seconds
        )
        return [_to_range_sample(None) for item in raw_results]

    @_mutmut_mutated(mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut)
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

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_orig(
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

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_1(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        try:
            response = None
        except httpx.TimeoutException as exc:
            raise AdapterTimeoutError(
                f"Prometheus query timed out after {timeout_seconds}s",
                context={"endpoint": self._endpoint, "promql": promql},
            ) from exc
        except httpx.HTTPError as exc:
            raise PrometheusUnavailableError(self._endpoint) from exc

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_2(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        try:
            response = self._client.get(None, params=params, timeout=timeout_seconds)
        except httpx.TimeoutException as exc:
            raise AdapterTimeoutError(
                f"Prometheus query timed out after {timeout_seconds}s",
                context={"endpoint": self._endpoint, "promql": promql},
            ) from exc
        except httpx.HTTPError as exc:
            raise PrometheusUnavailableError(self._endpoint) from exc

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_3(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        try:
            response = self._client.get(url, params=None, timeout=timeout_seconds)
        except httpx.TimeoutException as exc:
            raise AdapterTimeoutError(
                f"Prometheus query timed out after {timeout_seconds}s",
                context={"endpoint": self._endpoint, "promql": promql},
            ) from exc
        except httpx.HTTPError as exc:
            raise PrometheusUnavailableError(self._endpoint) from exc

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_4(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        try:
            response = self._client.get(url, params=params, timeout=None)
        except httpx.TimeoutException as exc:
            raise AdapterTimeoutError(
                f"Prometheus query timed out after {timeout_seconds}s",
                context={"endpoint": self._endpoint, "promql": promql},
            ) from exc
        except httpx.HTTPError as exc:
            raise PrometheusUnavailableError(self._endpoint) from exc

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_5(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        try:
            response = self._client.get(params=params, timeout=timeout_seconds)
        except httpx.TimeoutException as exc:
            raise AdapterTimeoutError(
                f"Prometheus query timed out after {timeout_seconds}s",
                context={"endpoint": self._endpoint, "promql": promql},
            ) from exc
        except httpx.HTTPError as exc:
            raise PrometheusUnavailableError(self._endpoint) from exc

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_6(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        try:
            response = self._client.get(url, timeout=timeout_seconds)
        except httpx.TimeoutException as exc:
            raise AdapterTimeoutError(
                f"Prometheus query timed out after {timeout_seconds}s",
                context={"endpoint": self._endpoint, "promql": promql},
            ) from exc
        except httpx.HTTPError as exc:
            raise PrometheusUnavailableError(self._endpoint) from exc

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_7(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        try:
            response = self._client.get(url, params=params, )
        except httpx.TimeoutException as exc:
            raise AdapterTimeoutError(
                f"Prometheus query timed out after {timeout_seconds}s",
                context={"endpoint": self._endpoint, "promql": promql},
            ) from exc
        except httpx.HTTPError as exc:
            raise PrometheusUnavailableError(self._endpoint) from exc

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_8(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        try:
            response = self._client.get(url, params=params, timeout=timeout_seconds)
        except httpx.TimeoutException as exc:
            raise AdapterTimeoutError(
                None,
                context={"endpoint": self._endpoint, "promql": promql},
            ) from exc
        except httpx.HTTPError as exc:
            raise PrometheusUnavailableError(self._endpoint) from exc

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_9(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        try:
            response = self._client.get(url, params=params, timeout=timeout_seconds)
        except httpx.TimeoutException as exc:
            raise AdapterTimeoutError(
                f"Prometheus query timed out after {timeout_seconds}s",
                context=None,
            ) from exc
        except httpx.HTTPError as exc:
            raise PrometheusUnavailableError(self._endpoint) from exc

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_10(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        try:
            response = self._client.get(url, params=params, timeout=timeout_seconds)
        except httpx.TimeoutException as exc:
            raise AdapterTimeoutError(
                context={"endpoint": self._endpoint, "promql": promql},
            ) from exc
        except httpx.HTTPError as exc:
            raise PrometheusUnavailableError(self._endpoint) from exc

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_11(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        try:
            response = self._client.get(url, params=params, timeout=timeout_seconds)
        except httpx.TimeoutException as exc:
            raise AdapterTimeoutError(
                f"Prometheus query timed out after {timeout_seconds}s",
                ) from exc
        except httpx.HTTPError as exc:
            raise PrometheusUnavailableError(self._endpoint) from exc

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_12(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        try:
            response = self._client.get(url, params=params, timeout=timeout_seconds)
        except httpx.TimeoutException as exc:
            raise AdapterTimeoutError(
                f"Prometheus query timed out after {timeout_seconds}s",
                context={"XXendpointXX": self._endpoint, "promql": promql},
            ) from exc
        except httpx.HTTPError as exc:
            raise PrometheusUnavailableError(self._endpoint) from exc

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_13(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        try:
            response = self._client.get(url, params=params, timeout=timeout_seconds)
        except httpx.TimeoutException as exc:
            raise AdapterTimeoutError(
                f"Prometheus query timed out after {timeout_seconds}s",
                context={"ENDPOINT": self._endpoint, "promql": promql},
            ) from exc
        except httpx.HTTPError as exc:
            raise PrometheusUnavailableError(self._endpoint) from exc

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_14(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        try:
            response = self._client.get(url, params=params, timeout=timeout_seconds)
        except httpx.TimeoutException as exc:
            raise AdapterTimeoutError(
                f"Prometheus query timed out after {timeout_seconds}s",
                context={"endpoint": self._endpoint, "XXpromqlXX": promql},
            ) from exc
        except httpx.HTTPError as exc:
            raise PrometheusUnavailableError(self._endpoint) from exc

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_15(
        self, url: str, params: dict[str, str], promql: str, timeout_seconds: float
    ) -> list[dict[str, object]]:
        try:
            response = self._client.get(url, params=params, timeout=timeout_seconds)
        except httpx.TimeoutException as exc:
            raise AdapterTimeoutError(
                f"Prometheus query timed out after {timeout_seconds}s",
                context={"endpoint": self._endpoint, "PROMQL": promql},
            ) from exc
        except httpx.HTTPError as exc:
            raise PrometheusUnavailableError(self._endpoint) from exc

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_16(
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
            raise PrometheusUnavailableError(None) from exc

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_17(
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

        if response.status_code != 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_18(
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

        if response.status_code == 401:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_19(
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

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_20(
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

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_21(
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

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_22(
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

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_23(
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

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_24(
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

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_25(
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

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_26(
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

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_27(
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

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_28(
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

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_29(
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

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_30(
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

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_31(
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

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_32(
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

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_33(
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

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_34(
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

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_35(
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

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_36(
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

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_37(
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

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_38(
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

        if response.status_code == 400:  # noqa: PLR2004
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

    def xǁPrometheusHTTPAdapterǁ_execute__mutmut_39(
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

        if response.status_code == 400:  # noqa: PLR2004
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

mutants_xǁPrometheusHTTPAdapterǁ__init____mutmut['_mutmut_orig'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ__init____mutmut['xǁPrometheusHTTPAdapterǁ__init____mutmut_1'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ__init____mutmut['xǁPrometheusHTTPAdapterǁ__init____mutmut_2'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ__init____mutmut['xǁPrometheusHTTPAdapterǁ__init____mutmut_3'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ__init____mutmut['xǁPrometheusHTTPAdapterǁ__init____mutmut_4'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ__init____mutmut['xǁPrometheusHTTPAdapterǁ__init____mutmut_5'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ__init____mutmut['xǁPrometheusHTTPAdapterǁ__init____mutmut_6'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ__init____mutmut['xǁPrometheusHTTPAdapterǁ__init____mutmut_7'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ__init____mutmut['xǁPrometheusHTTPAdapterǁ__init____mutmut_8'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ__init____mutmut['xǁPrometheusHTTPAdapterǁ__init____mutmut_9'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ__init____mutmut['xǁPrometheusHTTPAdapterǁ__init____mutmut_10'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ__init____mutmut_10 # type: ignore # mutmut generated

mutants_xǁPrometheusHTTPAdapterǁinstant_query__mutmut['_mutmut_orig'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁinstant_query__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁinstant_query__mutmut['xǁPrometheusHTTPAdapterǁinstant_query__mutmut_1'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁinstant_query__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁinstant_query__mutmut['xǁPrometheusHTTPAdapterǁinstant_query__mutmut_2'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁinstant_query__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁinstant_query__mutmut['xǁPrometheusHTTPAdapterǁinstant_query__mutmut_3'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁinstant_query__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁinstant_query__mutmut['xǁPrometheusHTTPAdapterǁinstant_query__mutmut_4'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁinstant_query__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁinstant_query__mutmut['xǁPrometheusHTTPAdapterǁinstant_query__mutmut_5'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁinstant_query__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁinstant_query__mutmut['xǁPrometheusHTTPAdapterǁinstant_query__mutmut_6'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁinstant_query__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁinstant_query__mutmut['xǁPrometheusHTTPAdapterǁinstant_query__mutmut_7'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁinstant_query__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁinstant_query__mutmut['xǁPrometheusHTTPAdapterǁinstant_query__mutmut_8'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁinstant_query__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁinstant_query__mutmut['xǁPrometheusHTTPAdapterǁinstant_query__mutmut_9'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁinstant_query__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁinstant_query__mutmut['xǁPrometheusHTTPAdapterǁinstant_query__mutmut_10'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁinstant_query__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁinstant_query__mutmut['xǁPrometheusHTTPAdapterǁinstant_query__mutmut_11'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁinstant_query__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁinstant_query__mutmut['xǁPrometheusHTTPAdapterǁinstant_query__mutmut_12'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁinstant_query__mutmut_12 # type: ignore # mutmut generated

mutants_xǁPrometheusHTTPAdapterǁrange_query__mutmut['_mutmut_orig'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁrange_query__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁrange_query__mutmut['xǁPrometheusHTTPAdapterǁrange_query__mutmut_1'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁrange_query__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁrange_query__mutmut['xǁPrometheusHTTPAdapterǁrange_query__mutmut_2'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁrange_query__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁrange_query__mutmut['xǁPrometheusHTTPAdapterǁrange_query__mutmut_3'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁrange_query__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁrange_query__mutmut['xǁPrometheusHTTPAdapterǁrange_query__mutmut_4'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁrange_query__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁrange_query__mutmut['xǁPrometheusHTTPAdapterǁrange_query__mutmut_5'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁrange_query__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁrange_query__mutmut['xǁPrometheusHTTPAdapterǁrange_query__mutmut_6'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁrange_query__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁrange_query__mutmut['xǁPrometheusHTTPAdapterǁrange_query__mutmut_7'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁrange_query__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁrange_query__mutmut['xǁPrometheusHTTPAdapterǁrange_query__mutmut_8'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁrange_query__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁrange_query__mutmut['xǁPrometheusHTTPAdapterǁrange_query__mutmut_9'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁrange_query__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁrange_query__mutmut['xǁPrometheusHTTPAdapterǁrange_query__mutmut_10'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁrange_query__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁrange_query__mutmut['xǁPrometheusHTTPAdapterǁrange_query__mutmut_11'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁrange_query__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁrange_query__mutmut['xǁPrometheusHTTPAdapterǁrange_query__mutmut_12'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁrange_query__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁrange_query__mutmut['xǁPrometheusHTTPAdapterǁrange_query__mutmut_13'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁrange_query__mutmut_13 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁrange_query__mutmut['xǁPrometheusHTTPAdapterǁrange_query__mutmut_14'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁrange_query__mutmut_14 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁrange_query__mutmut['xǁPrometheusHTTPAdapterǁrange_query__mutmut_15'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁrange_query__mutmut_15 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁrange_query__mutmut['xǁPrometheusHTTPAdapterǁrange_query__mutmut_16'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁrange_query__mutmut_16 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁrange_query__mutmut['xǁPrometheusHTTPAdapterǁrange_query__mutmut_17'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁrange_query__mutmut_17 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁrange_query__mutmut['xǁPrometheusHTTPAdapterǁrange_query__mutmut_18'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁrange_query__mutmut_18 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁrange_query__mutmut['xǁPrometheusHTTPAdapterǁrange_query__mutmut_19'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁrange_query__mutmut_19 # type: ignore # mutmut generated

mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['_mutmut_orig'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_1'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_2'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_3'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_4'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_5'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_6'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_7'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_8'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_9'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_10'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_11'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_12'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_13'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_14'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_15'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_16'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_17'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_18'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_19'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_20'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_21'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_22'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_23'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_24'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_25'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_26'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_27'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_28'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_29'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_30'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_31'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_32'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_33'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_34'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_35'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_36'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_37'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_38'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁPrometheusHTTPAdapterǁ_execute__mutmut['xǁPrometheusHTTPAdapterǁ_execute__mutmut_39'] = PrometheusHTTPAdapter.xǁPrometheusHTTPAdapterǁ_execute__mutmut_39 # type: ignore # mutmut generated
mutants_x__instant_query_params__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__instant_query_params__mutmut)
def _instant_query_params(promql: str) -> dict[str, str]:
    """Builds the query params for Prometheus's `/api/v1/query` endpoint."""
    return {"query": promql}


def x__instant_query_params__mutmut_orig(promql: str) -> dict[str, str]:
    """Builds the query params for Prometheus's `/api/v1/query` endpoint."""
    return {"query": promql}


def x__instant_query_params__mutmut_1(promql: str) -> dict[str, str]:
    """Builds the query params for Prometheus's `/api/v1/query` endpoint."""
    return {"XXqueryXX": promql}


def x__instant_query_params__mutmut_2(promql: str) -> dict[str, str]:
    """Builds the query params for Prometheus's `/api/v1/query` endpoint."""
    return {"QUERY": promql}

mutants_x__instant_query_params__mutmut['_mutmut_orig'] = x__instant_query_params__mutmut_orig # type: ignore # mutmut generated
mutants_x__instant_query_params__mutmut['x__instant_query_params__mutmut_1'] = x__instant_query_params__mutmut_1 # type: ignore # mutmut generated
mutants_x__instant_query_params__mutmut['x__instant_query_params__mutmut_2'] = x__instant_query_params__mutmut_2 # type: ignore # mutmut generated
mutants_x__range_query_params__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__range_query_params__mutmut)
def _range_query_params(promql: str, start: str, end: str, step: str) -> dict[str, str]:
    """Builds the query params for Prometheus's `/api/v1/query_range` endpoint."""
    return {"query": promql, "start": start, "end": end, "step": step}


def x__range_query_params__mutmut_orig(promql: str, start: str, end: str, step: str) -> dict[str, str]:
    """Builds the query params for Prometheus's `/api/v1/query_range` endpoint."""
    return {"query": promql, "start": start, "end": end, "step": step}


def x__range_query_params__mutmut_1(promql: str, start: str, end: str, step: str) -> dict[str, str]:
    """Builds the query params for Prometheus's `/api/v1/query_range` endpoint."""
    return {"XXqueryXX": promql, "start": start, "end": end, "step": step}


def x__range_query_params__mutmut_2(promql: str, start: str, end: str, step: str) -> dict[str, str]:
    """Builds the query params for Prometheus's `/api/v1/query_range` endpoint."""
    return {"QUERY": promql, "start": start, "end": end, "step": step}


def x__range_query_params__mutmut_3(promql: str, start: str, end: str, step: str) -> dict[str, str]:
    """Builds the query params for Prometheus's `/api/v1/query_range` endpoint."""
    return {"query": promql, "XXstartXX": start, "end": end, "step": step}


def x__range_query_params__mutmut_4(promql: str, start: str, end: str, step: str) -> dict[str, str]:
    """Builds the query params for Prometheus's `/api/v1/query_range` endpoint."""
    return {"query": promql, "START": start, "end": end, "step": step}


def x__range_query_params__mutmut_5(promql: str, start: str, end: str, step: str) -> dict[str, str]:
    """Builds the query params for Prometheus's `/api/v1/query_range` endpoint."""
    return {"query": promql, "start": start, "XXendXX": end, "step": step}


def x__range_query_params__mutmut_6(promql: str, start: str, end: str, step: str) -> dict[str, str]:
    """Builds the query params for Prometheus's `/api/v1/query_range` endpoint."""
    return {"query": promql, "start": start, "END": end, "step": step}


def x__range_query_params__mutmut_7(promql: str, start: str, end: str, step: str) -> dict[str, str]:
    """Builds the query params for Prometheus's `/api/v1/query_range` endpoint."""
    return {"query": promql, "start": start, "end": end, "XXstepXX": step}


def x__range_query_params__mutmut_8(promql: str, start: str, end: str, step: str) -> dict[str, str]:
    """Builds the query params for Prometheus's `/api/v1/query_range` endpoint."""
    return {"query": promql, "start": start, "end": end, "STEP": step}

mutants_x__range_query_params__mutmut['_mutmut_orig'] = x__range_query_params__mutmut_orig # type: ignore # mutmut generated
mutants_x__range_query_params__mutmut['x__range_query_params__mutmut_1'] = x__range_query_params__mutmut_1 # type: ignore # mutmut generated
mutants_x__range_query_params__mutmut['x__range_query_params__mutmut_2'] = x__range_query_params__mutmut_2 # type: ignore # mutmut generated
mutants_x__range_query_params__mutmut['x__range_query_params__mutmut_3'] = x__range_query_params__mutmut_3 # type: ignore # mutmut generated
mutants_x__range_query_params__mutmut['x__range_query_params__mutmut_4'] = x__range_query_params__mutmut_4 # type: ignore # mutmut generated
mutants_x__range_query_params__mutmut['x__range_query_params__mutmut_5'] = x__range_query_params__mutmut_5 # type: ignore # mutmut generated
mutants_x__range_query_params__mutmut['x__range_query_params__mutmut_6'] = x__range_query_params__mutmut_6 # type: ignore # mutmut generated
mutants_x__range_query_params__mutmut['x__range_query_params__mutmut_7'] = x__range_query_params__mutmut_7 # type: ignore # mutmut generated
mutants_x__range_query_params__mutmut['x__range_query_params__mutmut_8'] = x__range_query_params__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_instant_sample__mutmut)
def _to_instant_sample(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    value_pair = cast(list[object], item.get("value", [0, "0"]))
    return PrometheusInstantSample(metric=metric, value=float(cast(str, value_pair[1])))


def x__to_instant_sample__mutmut_orig(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    value_pair = cast(list[object], item.get("value", [0, "0"]))
    return PrometheusInstantSample(metric=metric, value=float(cast(str, value_pair[1])))


def x__to_instant_sample__mutmut_1(item: dict[str, object]) -> PrometheusInstantSample:
    metric = None
    value_pair = cast(list[object], item.get("value", [0, "0"]))
    return PrometheusInstantSample(metric=metric, value=float(cast(str, value_pair[1])))


def x__to_instant_sample__mutmut_2(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(None, item.get("metric", {}))
    value_pair = cast(list[object], item.get("value", [0, "0"]))
    return PrometheusInstantSample(metric=metric, value=float(cast(str, value_pair[1])))


def x__to_instant_sample__mutmut_3(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], None)
    value_pair = cast(list[object], item.get("value", [0, "0"]))
    return PrometheusInstantSample(metric=metric, value=float(cast(str, value_pair[1])))


def x__to_instant_sample__mutmut_4(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(item.get("metric", {}))
    value_pair = cast(list[object], item.get("value", [0, "0"]))
    return PrometheusInstantSample(metric=metric, value=float(cast(str, value_pair[1])))


def x__to_instant_sample__mutmut_5(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], )
    value_pair = cast(list[object], item.get("value", [0, "0"]))
    return PrometheusInstantSample(metric=metric, value=float(cast(str, value_pair[1])))


def x__to_instant_sample__mutmut_6(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], item.get(None, {}))
    value_pair = cast(list[object], item.get("value", [0, "0"]))
    return PrometheusInstantSample(metric=metric, value=float(cast(str, value_pair[1])))


def x__to_instant_sample__mutmut_7(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], item.get("metric", None))
    value_pair = cast(list[object], item.get("value", [0, "0"]))
    return PrometheusInstantSample(metric=metric, value=float(cast(str, value_pair[1])))


def x__to_instant_sample__mutmut_8(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], item.get({}))
    value_pair = cast(list[object], item.get("value", [0, "0"]))
    return PrometheusInstantSample(metric=metric, value=float(cast(str, value_pair[1])))


def x__to_instant_sample__mutmut_9(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], item.get("metric", ))
    value_pair = cast(list[object], item.get("value", [0, "0"]))
    return PrometheusInstantSample(metric=metric, value=float(cast(str, value_pair[1])))


def x__to_instant_sample__mutmut_10(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], item.get("XXmetricXX", {}))
    value_pair = cast(list[object], item.get("value", [0, "0"]))
    return PrometheusInstantSample(metric=metric, value=float(cast(str, value_pair[1])))


def x__to_instant_sample__mutmut_11(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], item.get("METRIC", {}))
    value_pair = cast(list[object], item.get("value", [0, "0"]))
    return PrometheusInstantSample(metric=metric, value=float(cast(str, value_pair[1])))


def x__to_instant_sample__mutmut_12(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    value_pair = None
    return PrometheusInstantSample(metric=metric, value=float(cast(str, value_pair[1])))


def x__to_instant_sample__mutmut_13(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    value_pair = cast(None, item.get("value", [0, "0"]))
    return PrometheusInstantSample(metric=metric, value=float(cast(str, value_pair[1])))


def x__to_instant_sample__mutmut_14(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    value_pair = cast(list[object], None)
    return PrometheusInstantSample(metric=metric, value=float(cast(str, value_pair[1])))


def x__to_instant_sample__mutmut_15(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    value_pair = cast(item.get("value", [0, "0"]))
    return PrometheusInstantSample(metric=metric, value=float(cast(str, value_pair[1])))


def x__to_instant_sample__mutmut_16(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    value_pair = cast(list[object], )
    return PrometheusInstantSample(metric=metric, value=float(cast(str, value_pair[1])))


def x__to_instant_sample__mutmut_17(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    value_pair = cast(list[object], item.get(None, [0, "0"]))
    return PrometheusInstantSample(metric=metric, value=float(cast(str, value_pair[1])))


def x__to_instant_sample__mutmut_18(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    value_pair = cast(list[object], item.get("value", None))
    return PrometheusInstantSample(metric=metric, value=float(cast(str, value_pair[1])))


def x__to_instant_sample__mutmut_19(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    value_pair = cast(list[object], item.get([0, "0"]))
    return PrometheusInstantSample(metric=metric, value=float(cast(str, value_pair[1])))


def x__to_instant_sample__mutmut_20(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    value_pair = cast(list[object], item.get("value", ))
    return PrometheusInstantSample(metric=metric, value=float(cast(str, value_pair[1])))


def x__to_instant_sample__mutmut_21(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    value_pair = cast(list[object], item.get("XXvalueXX", [0, "0"]))
    return PrometheusInstantSample(metric=metric, value=float(cast(str, value_pair[1])))


def x__to_instant_sample__mutmut_22(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    value_pair = cast(list[object], item.get("VALUE", [0, "0"]))
    return PrometheusInstantSample(metric=metric, value=float(cast(str, value_pair[1])))


def x__to_instant_sample__mutmut_23(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    value_pair = cast(list[object], item.get("value", [1, "0"]))
    return PrometheusInstantSample(metric=metric, value=float(cast(str, value_pair[1])))


def x__to_instant_sample__mutmut_24(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    value_pair = cast(list[object], item.get("value", [0, "XX0XX"]))
    return PrometheusInstantSample(metric=metric, value=float(cast(str, value_pair[1])))


def x__to_instant_sample__mutmut_25(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    value_pair = cast(list[object], item.get("value", [0, "0"]))
    return PrometheusInstantSample(metric=None, value=float(cast(str, value_pair[1])))


def x__to_instant_sample__mutmut_26(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    value_pair = cast(list[object], item.get("value", [0, "0"]))
    return PrometheusInstantSample(metric=metric, value=None)


def x__to_instant_sample__mutmut_27(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    value_pair = cast(list[object], item.get("value", [0, "0"]))
    return PrometheusInstantSample(value=float(cast(str, value_pair[1])))


def x__to_instant_sample__mutmut_28(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    value_pair = cast(list[object], item.get("value", [0, "0"]))
    return PrometheusInstantSample(metric=metric, )


def x__to_instant_sample__mutmut_29(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    value_pair = cast(list[object], item.get("value", [0, "0"]))
    return PrometheusInstantSample(metric=metric, value=float(None))


def x__to_instant_sample__mutmut_30(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    value_pair = cast(list[object], item.get("value", [0, "0"]))
    return PrometheusInstantSample(metric=metric, value=float(cast(None, value_pair[1])))


def x__to_instant_sample__mutmut_31(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    value_pair = cast(list[object], item.get("value", [0, "0"]))
    return PrometheusInstantSample(metric=metric, value=float(cast(str, None)))


def x__to_instant_sample__mutmut_32(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    value_pair = cast(list[object], item.get("value", [0, "0"]))
    return PrometheusInstantSample(metric=metric, value=float(cast(value_pair[1])))


def x__to_instant_sample__mutmut_33(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    value_pair = cast(list[object], item.get("value", [0, "0"]))
    return PrometheusInstantSample(metric=metric, value=float(cast(str, )))


def x__to_instant_sample__mutmut_34(item: dict[str, object]) -> PrometheusInstantSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    value_pair = cast(list[object], item.get("value", [0, "0"]))
    return PrometheusInstantSample(metric=metric, value=float(cast(str, value_pair[2])))

mutants_x__to_instant_sample__mutmut['_mutmut_orig'] = x__to_instant_sample__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_1'] = x__to_instant_sample__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_2'] = x__to_instant_sample__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_3'] = x__to_instant_sample__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_4'] = x__to_instant_sample__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_5'] = x__to_instant_sample__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_6'] = x__to_instant_sample__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_7'] = x__to_instant_sample__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_8'] = x__to_instant_sample__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_9'] = x__to_instant_sample__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_10'] = x__to_instant_sample__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_11'] = x__to_instant_sample__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_12'] = x__to_instant_sample__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_13'] = x__to_instant_sample__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_14'] = x__to_instant_sample__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_15'] = x__to_instant_sample__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_16'] = x__to_instant_sample__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_17'] = x__to_instant_sample__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_18'] = x__to_instant_sample__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_19'] = x__to_instant_sample__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_20'] = x__to_instant_sample__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_21'] = x__to_instant_sample__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_22'] = x__to_instant_sample__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_23'] = x__to_instant_sample__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_24'] = x__to_instant_sample__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_25'] = x__to_instant_sample__mutmut_25 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_26'] = x__to_instant_sample__mutmut_26 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_27'] = x__to_instant_sample__mutmut_27 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_28'] = x__to_instant_sample__mutmut_28 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_29'] = x__to_instant_sample__mutmut_29 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_30'] = x__to_instant_sample__mutmut_30 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_31'] = x__to_instant_sample__mutmut_31 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_32'] = x__to_instant_sample__mutmut_32 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_33'] = x__to_instant_sample__mutmut_33 # type: ignore # mutmut generated
mutants_x__to_instant_sample__mutmut['x__to_instant_sample__mutmut_34'] = x__to_instant_sample__mutmut_34 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_range_sample__mutmut)
def _to_range_sample(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    raw_values = cast(list[list[object]], item.get("values", []))
    values = [(_to_iso(cast(float, point[0])), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_orig(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    raw_values = cast(list[list[object]], item.get("values", []))
    values = [(_to_iso(cast(float, point[0])), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_1(item: dict[str, object]) -> PrometheusRangeSample:
    metric = None
    raw_values = cast(list[list[object]], item.get("values", []))
    values = [(_to_iso(cast(float, point[0])), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_2(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(None, item.get("metric", {}))
    raw_values = cast(list[list[object]], item.get("values", []))
    values = [(_to_iso(cast(float, point[0])), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_3(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], None)
    raw_values = cast(list[list[object]], item.get("values", []))
    values = [(_to_iso(cast(float, point[0])), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_4(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(item.get("metric", {}))
    raw_values = cast(list[list[object]], item.get("values", []))
    values = [(_to_iso(cast(float, point[0])), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_5(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], )
    raw_values = cast(list[list[object]], item.get("values", []))
    values = [(_to_iso(cast(float, point[0])), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_6(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get(None, {}))
    raw_values = cast(list[list[object]], item.get("values", []))
    values = [(_to_iso(cast(float, point[0])), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_7(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("metric", None))
    raw_values = cast(list[list[object]], item.get("values", []))
    values = [(_to_iso(cast(float, point[0])), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_8(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get({}))
    raw_values = cast(list[list[object]], item.get("values", []))
    values = [(_to_iso(cast(float, point[0])), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_9(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("metric", ))
    raw_values = cast(list[list[object]], item.get("values", []))
    values = [(_to_iso(cast(float, point[0])), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_10(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("XXmetricXX", {}))
    raw_values = cast(list[list[object]], item.get("values", []))
    values = [(_to_iso(cast(float, point[0])), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_11(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("METRIC", {}))
    raw_values = cast(list[list[object]], item.get("values", []))
    values = [(_to_iso(cast(float, point[0])), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_12(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    raw_values = None
    values = [(_to_iso(cast(float, point[0])), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_13(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    raw_values = cast(None, item.get("values", []))
    values = [(_to_iso(cast(float, point[0])), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_14(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    raw_values = cast(list[list[object]], None)
    values = [(_to_iso(cast(float, point[0])), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_15(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    raw_values = cast(item.get("values", []))
    values = [(_to_iso(cast(float, point[0])), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_16(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    raw_values = cast(list[list[object]], )
    values = [(_to_iso(cast(float, point[0])), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_17(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    raw_values = cast(list[list[object]], item.get(None, []))
    values = [(_to_iso(cast(float, point[0])), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_18(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    raw_values = cast(list[list[object]], item.get("values", None))
    values = [(_to_iso(cast(float, point[0])), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_19(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    raw_values = cast(list[list[object]], item.get([]))
    values = [(_to_iso(cast(float, point[0])), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_20(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    raw_values = cast(list[list[object]], item.get("values", ))
    values = [(_to_iso(cast(float, point[0])), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_21(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    raw_values = cast(list[list[object]], item.get("XXvaluesXX", []))
    values = [(_to_iso(cast(float, point[0])), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_22(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    raw_values = cast(list[list[object]], item.get("VALUES", []))
    values = [(_to_iso(cast(float, point[0])), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_23(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    raw_values = cast(list[list[object]], item.get("values", []))
    values = None
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_24(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    raw_values = cast(list[list[object]], item.get("values", []))
    values = [(_to_iso(None), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_25(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    raw_values = cast(list[list[object]], item.get("values", []))
    values = [(_to_iso(cast(None, point[0])), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_26(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    raw_values = cast(list[list[object]], item.get("values", []))
    values = [(_to_iso(cast(float, None)), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_27(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    raw_values = cast(list[list[object]], item.get("values", []))
    values = [(_to_iso(cast(point[0])), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_28(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    raw_values = cast(list[list[object]], item.get("values", []))
    values = [(_to_iso(cast(float, )), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_29(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    raw_values = cast(list[list[object]], item.get("values", []))
    values = [(_to_iso(cast(float, point[1])), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_30(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    raw_values = cast(list[list[object]], item.get("values", []))
    values = [(_to_iso(cast(float, point[0])), float(None)) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_31(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    raw_values = cast(list[list[object]], item.get("values", []))
    values = [(_to_iso(cast(float, point[0])), float(cast(None, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_32(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    raw_values = cast(list[list[object]], item.get("values", []))
    values = [(_to_iso(cast(float, point[0])), float(cast(str, None))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_33(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    raw_values = cast(list[list[object]], item.get("values", []))
    values = [(_to_iso(cast(float, point[0])), float(cast(point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_34(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    raw_values = cast(list[list[object]], item.get("values", []))
    values = [(_to_iso(cast(float, point[0])), float(cast(str, ))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_35(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    raw_values = cast(list[list[object]], item.get("values", []))
    values = [(_to_iso(cast(float, point[0])), float(cast(str, point[2]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=values)


def x__to_range_sample__mutmut_36(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    raw_values = cast(list[list[object]], item.get("values", []))
    values = [(_to_iso(cast(float, point[0])), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=None, values=values)


def x__to_range_sample__mutmut_37(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    raw_values = cast(list[list[object]], item.get("values", []))
    values = [(_to_iso(cast(float, point[0])), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, values=None)


def x__to_range_sample__mutmut_38(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    raw_values = cast(list[list[object]], item.get("values", []))
    values = [(_to_iso(cast(float, point[0])), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(values=values)


def x__to_range_sample__mutmut_39(item: dict[str, object]) -> PrometheusRangeSample:
    metric = cast(dict[str, str], item.get("metric", {}))
    raw_values = cast(list[list[object]], item.get("values", []))
    values = [(_to_iso(cast(float, point[0])), float(cast(str, point[1]))) for point in raw_values]
    return PrometheusRangeSample(metric=metric, )

mutants_x__to_range_sample__mutmut['_mutmut_orig'] = x__to_range_sample__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_1'] = x__to_range_sample__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_2'] = x__to_range_sample__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_3'] = x__to_range_sample__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_4'] = x__to_range_sample__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_5'] = x__to_range_sample__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_6'] = x__to_range_sample__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_7'] = x__to_range_sample__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_8'] = x__to_range_sample__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_9'] = x__to_range_sample__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_10'] = x__to_range_sample__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_11'] = x__to_range_sample__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_12'] = x__to_range_sample__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_13'] = x__to_range_sample__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_14'] = x__to_range_sample__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_15'] = x__to_range_sample__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_16'] = x__to_range_sample__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_17'] = x__to_range_sample__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_18'] = x__to_range_sample__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_19'] = x__to_range_sample__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_20'] = x__to_range_sample__mutmut_20 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_21'] = x__to_range_sample__mutmut_21 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_22'] = x__to_range_sample__mutmut_22 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_23'] = x__to_range_sample__mutmut_23 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_24'] = x__to_range_sample__mutmut_24 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_25'] = x__to_range_sample__mutmut_25 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_26'] = x__to_range_sample__mutmut_26 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_27'] = x__to_range_sample__mutmut_27 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_28'] = x__to_range_sample__mutmut_28 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_29'] = x__to_range_sample__mutmut_29 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_30'] = x__to_range_sample__mutmut_30 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_31'] = x__to_range_sample__mutmut_31 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_32'] = x__to_range_sample__mutmut_32 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_33'] = x__to_range_sample__mutmut_33 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_34'] = x__to_range_sample__mutmut_34 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_35'] = x__to_range_sample__mutmut_35 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_36'] = x__to_range_sample__mutmut_36 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_37'] = x__to_range_sample__mutmut_37 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_38'] = x__to_range_sample__mutmut_38 # type: ignore # mutmut generated
mutants_x__to_range_sample__mutmut['x__to_range_sample__mutmut_39'] = x__to_range_sample__mutmut_39 # type: ignore # mutmut generated
mutants_x__error_detail__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__error_detail__mutmut)
def _error_detail(response: httpx.Response) -> str:
    try:
        body = response.json()
    except ValueError:
        return response.text
    if isinstance(body, dict) and "error" in body:
        return str(body["error"])
    return response.text


def x__error_detail__mutmut_orig(response: httpx.Response) -> str:
    try:
        body = response.json()
    except ValueError:
        return response.text
    if isinstance(body, dict) and "error" in body:
        return str(body["error"])
    return response.text


def x__error_detail__mutmut_1(response: httpx.Response) -> str:
    try:
        body = None
    except ValueError:
        return response.text
    if isinstance(body, dict) and "error" in body:
        return str(body["error"])
    return response.text


def x__error_detail__mutmut_2(response: httpx.Response) -> str:
    try:
        body = response.json()
    except ValueError:
        return response.text
    if isinstance(body, dict) or "error" in body:
        return str(body["error"])
    return response.text


def x__error_detail__mutmut_3(response: httpx.Response) -> str:
    try:
        body = response.json()
    except ValueError:
        return response.text
    if isinstance(body, dict) and "XXerrorXX" in body:
        return str(body["error"])
    return response.text


def x__error_detail__mutmut_4(response: httpx.Response) -> str:
    try:
        body = response.json()
    except ValueError:
        return response.text
    if isinstance(body, dict) and "ERROR" in body:
        return str(body["error"])
    return response.text


def x__error_detail__mutmut_5(response: httpx.Response) -> str:
    try:
        body = response.json()
    except ValueError:
        return response.text
    if isinstance(body, dict) and "error" not in body:
        return str(body["error"])
    return response.text


def x__error_detail__mutmut_6(response: httpx.Response) -> str:
    try:
        body = response.json()
    except ValueError:
        return response.text
    if isinstance(body, dict) and "error" in body:
        return str(None)
    return response.text


def x__error_detail__mutmut_7(response: httpx.Response) -> str:
    try:
        body = response.json()
    except ValueError:
        return response.text
    if isinstance(body, dict) and "error" in body:
        return str(body["XXerrorXX"])
    return response.text


def x__error_detail__mutmut_8(response: httpx.Response) -> str:
    try:
        body = response.json()
    except ValueError:
        return response.text
    if isinstance(body, dict) and "error" in body:
        return str(body["ERROR"])
    return response.text

mutants_x__error_detail__mutmut['_mutmut_orig'] = x__error_detail__mutmut_orig # type: ignore # mutmut generated
mutants_x__error_detail__mutmut['x__error_detail__mutmut_1'] = x__error_detail__mutmut_1 # type: ignore # mutmut generated
mutants_x__error_detail__mutmut['x__error_detail__mutmut_2'] = x__error_detail__mutmut_2 # type: ignore # mutmut generated
mutants_x__error_detail__mutmut['x__error_detail__mutmut_3'] = x__error_detail__mutmut_3 # type: ignore # mutmut generated
mutants_x__error_detail__mutmut['x__error_detail__mutmut_4'] = x__error_detail__mutmut_4 # type: ignore # mutmut generated
mutants_x__error_detail__mutmut['x__error_detail__mutmut_5'] = x__error_detail__mutmut_5 # type: ignore # mutmut generated
mutants_x__error_detail__mutmut['x__error_detail__mutmut_6'] = x__error_detail__mutmut_6 # type: ignore # mutmut generated
mutants_x__error_detail__mutmut['x__error_detail__mutmut_7'] = x__error_detail__mutmut_7 # type: ignore # mutmut generated
mutants_x__error_detail__mutmut['x__error_detail__mutmut_8'] = x__error_detail__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_iso__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_iso__mutmut)
def _to_iso(epoch_seconds: float) -> str:
    return datetime.fromtimestamp(epoch_seconds, tz=UTC).isoformat().replace("+00:00", "Z")


def x__to_iso__mutmut_orig(epoch_seconds: float) -> str:
    return datetime.fromtimestamp(epoch_seconds, tz=UTC).isoformat().replace("+00:00", "Z")


def x__to_iso__mutmut_1(epoch_seconds: float) -> str:
    return datetime.fromtimestamp(epoch_seconds, tz=UTC).isoformat().replace(None, "Z")


def x__to_iso__mutmut_2(epoch_seconds: float) -> str:
    return datetime.fromtimestamp(epoch_seconds, tz=UTC).isoformat().replace("+00:00", None)


def x__to_iso__mutmut_3(epoch_seconds: float) -> str:
    return datetime.fromtimestamp(epoch_seconds, tz=UTC).isoformat().replace("Z")


def x__to_iso__mutmut_4(epoch_seconds: float) -> str:
    return datetime.fromtimestamp(epoch_seconds, tz=UTC).isoformat().replace("+00:00", )


def x__to_iso__mutmut_5(epoch_seconds: float) -> str:
    return datetime.fromtimestamp(None, tz=UTC).isoformat().replace("+00:00", "Z")


def x__to_iso__mutmut_6(epoch_seconds: float) -> str:
    return datetime.fromtimestamp(epoch_seconds, tz=None).isoformat().replace("+00:00", "Z")


def x__to_iso__mutmut_7(epoch_seconds: float) -> str:
    return datetime.fromtimestamp(tz=UTC).isoformat().replace("+00:00", "Z")


def x__to_iso__mutmut_8(epoch_seconds: float) -> str:
    return datetime.fromtimestamp(epoch_seconds, ).isoformat().replace("+00:00", "Z")


def x__to_iso__mutmut_9(epoch_seconds: float) -> str:
    return datetime.fromtimestamp(epoch_seconds, tz=UTC).isoformat().replace("XX+00:00XX", "Z")


def x__to_iso__mutmut_10(epoch_seconds: float) -> str:
    return datetime.fromtimestamp(epoch_seconds, tz=UTC).isoformat().replace("+00:00", "XXZXX")


def x__to_iso__mutmut_11(epoch_seconds: float) -> str:
    return datetime.fromtimestamp(epoch_seconds, tz=UTC).isoformat().replace("+00:00", "z")

mutants_x__to_iso__mutmut['_mutmut_orig'] = x__to_iso__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_iso__mutmut['x__to_iso__mutmut_1'] = x__to_iso__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_iso__mutmut['x__to_iso__mutmut_2'] = x__to_iso__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_iso__mutmut['x__to_iso__mutmut_3'] = x__to_iso__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_iso__mutmut['x__to_iso__mutmut_4'] = x__to_iso__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_iso__mutmut['x__to_iso__mutmut_5'] = x__to_iso__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_iso__mutmut['x__to_iso__mutmut_6'] = x__to_iso__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_iso__mutmut['x__to_iso__mutmut_7'] = x__to_iso__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_iso__mutmut['x__to_iso__mutmut_8'] = x__to_iso__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_iso__mutmut['x__to_iso__mutmut_9'] = x__to_iso__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_iso__mutmut['x__to_iso__mutmut_10'] = x__to_iso__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_iso__mutmut['x__to_iso__mutmut_11'] = x__to_iso__mutmut_11 # type: ignore # mutmut generated
