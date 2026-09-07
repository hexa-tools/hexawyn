from __future__ import annotations

import os
from typing import TypedDict

import httpx

_JAEGER_QUERY_URL = os.environ.get("JAEGER_QUERY_URL", "http://localhost:16686")
_PROMETHEUS_URL = os.environ.get("PROMETHEUS_URL", "http://localhost:9090")
_REQUEST_TIMEOUT = 10.0


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class JaegerServiceDict(TypedDict):
    name: str


class JaegerOperationDict(TypedDict):
    name: str
    spanKind: str


class JaegerSpanDict(TypedDict, total=False):
    traceID: str
    spanID: str
    operationName: str
    duration: int
    startTime: int
    tags: list[dict[str, object]]
    processID: str
    references: list[dict[str, object]]


class JaegerTraceDict(TypedDict, total=False):
    traceID: str
    spans: list[JaegerSpanDict]
    processes: dict[str, dict[str, object]]


class JaegerTraceSummaryDict(TypedDict, total=False):
    traceID: str
    serviceCount: int
    spanCount: int
    duration: int
    hasErrors: bool


class JaegerDependencyDict(TypedDict):
    parent: str
    child: str
    callCount: int


class PrometheusMetricDict(TypedDict):
    name: str
    value: float
    labels: dict[str, str]


class PrometheusResultDict(TypedDict):
    metric: dict[str, str]
    values: list[tuple[float, str]]
mutants_x__jaeger_get__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__jaeger_get__mutmut)
def _jaeger_get(path: str, params: dict[str, object] | None = None) -> dict[str, object]:
    try:
        response = httpx.get(
            f"{_JAEGER_QUERY_URL}{path}",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"data": [], "total": 0}


def x__jaeger_get__mutmut_orig(path: str, params: dict[str, object] | None = None) -> dict[str, object]:
    try:
        response = httpx.get(
            f"{_JAEGER_QUERY_URL}{path}",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"data": [], "total": 0}


def x__jaeger_get__mutmut_1(path: str, params: dict[str, object] | None = None) -> dict[str, object]:
    try:
        response = None
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"data": [], "total": 0}


def x__jaeger_get__mutmut_2(path: str, params: dict[str, object] | None = None) -> dict[str, object]:
    try:
        response = httpx.get(
            None,
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"data": [], "total": 0}


def x__jaeger_get__mutmut_3(path: str, params: dict[str, object] | None = None) -> dict[str, object]:
    try:
        response = httpx.get(
            f"{_JAEGER_QUERY_URL}{path}",
            params=None,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"data": [], "total": 0}


def x__jaeger_get__mutmut_4(path: str, params: dict[str, object] | None = None) -> dict[str, object]:
    try:
        response = httpx.get(
            f"{_JAEGER_QUERY_URL}{path}",
            params=params,  # type: ignore
            timeout=None,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"data": [], "total": 0}


def x__jaeger_get__mutmut_5(path: str, params: dict[str, object] | None = None) -> dict[str, object]:
    try:
        response = httpx.get(
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"data": [], "total": 0}


def x__jaeger_get__mutmut_6(path: str, params: dict[str, object] | None = None) -> dict[str, object]:
    try:
        response = httpx.get(
            f"{_JAEGER_QUERY_URL}{path}",
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"data": [], "total": 0}


def x__jaeger_get__mutmut_7(path: str, params: dict[str, object] | None = None) -> dict[str, object]:
    try:
        response = httpx.get(
            f"{_JAEGER_QUERY_URL}{path}",
            params=params,  # type: ignore
            )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"data": [], "total": 0}


def x__jaeger_get__mutmut_8(path: str, params: dict[str, object] | None = None) -> dict[str, object]:
    try:
        response = httpx.get(
            f"{_JAEGER_QUERY_URL}{path}",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"XXdataXX": [], "total": 0}


def x__jaeger_get__mutmut_9(path: str, params: dict[str, object] | None = None) -> dict[str, object]:
    try:
        response = httpx.get(
            f"{_JAEGER_QUERY_URL}{path}",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"DATA": [], "total": 0}


def x__jaeger_get__mutmut_10(path: str, params: dict[str, object] | None = None) -> dict[str, object]:
    try:
        response = httpx.get(
            f"{_JAEGER_QUERY_URL}{path}",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"data": [], "XXtotalXX": 0}


def x__jaeger_get__mutmut_11(path: str, params: dict[str, object] | None = None) -> dict[str, object]:
    try:
        response = httpx.get(
            f"{_JAEGER_QUERY_URL}{path}",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"data": [], "TOTAL": 0}


def x__jaeger_get__mutmut_12(path: str, params: dict[str, object] | None = None) -> dict[str, object]:
    try:
        response = httpx.get(
            f"{_JAEGER_QUERY_URL}{path}",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"data": [], "total": 1}

mutants_x__jaeger_get__mutmut['_mutmut_orig'] = x__jaeger_get__mutmut_orig # type: ignore # mutmut generated
mutants_x__jaeger_get__mutmut['x__jaeger_get__mutmut_1'] = x__jaeger_get__mutmut_1 # type: ignore # mutmut generated
mutants_x__jaeger_get__mutmut['x__jaeger_get__mutmut_2'] = x__jaeger_get__mutmut_2 # type: ignore # mutmut generated
mutants_x__jaeger_get__mutmut['x__jaeger_get__mutmut_3'] = x__jaeger_get__mutmut_3 # type: ignore # mutmut generated
mutants_x__jaeger_get__mutmut['x__jaeger_get__mutmut_4'] = x__jaeger_get__mutmut_4 # type: ignore # mutmut generated
mutants_x__jaeger_get__mutmut['x__jaeger_get__mutmut_5'] = x__jaeger_get__mutmut_5 # type: ignore # mutmut generated
mutants_x__jaeger_get__mutmut['x__jaeger_get__mutmut_6'] = x__jaeger_get__mutmut_6 # type: ignore # mutmut generated
mutants_x__jaeger_get__mutmut['x__jaeger_get__mutmut_7'] = x__jaeger_get__mutmut_7 # type: ignore # mutmut generated
mutants_x__jaeger_get__mutmut['x__jaeger_get__mutmut_8'] = x__jaeger_get__mutmut_8 # type: ignore # mutmut generated
mutants_x__jaeger_get__mutmut['x__jaeger_get__mutmut_9'] = x__jaeger_get__mutmut_9 # type: ignore # mutmut generated
mutants_x__jaeger_get__mutmut['x__jaeger_get__mutmut_10'] = x__jaeger_get__mutmut_10 # type: ignore # mutmut generated
mutants_x__jaeger_get__mutmut['x__jaeger_get__mutmut_11'] = x__jaeger_get__mutmut_11 # type: ignore # mutmut generated
mutants_x__jaeger_get__mutmut['x__jaeger_get__mutmut_12'] = x__jaeger_get__mutmut_12 # type: ignore # mutmut generated
mutants_x__prometheus_query__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__prometheus_query__mutmut)
def _prometheus_query(query: str, time: str | None = None) -> dict[str, object]:
    params: dict[str, object] = {"query": query}
    if time is not None:
        params["time"] = time
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query__mutmut_orig(query: str, time: str | None = None) -> dict[str, object]:
    params: dict[str, object] = {"query": query}
    if time is not None:
        params["time"] = time
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query__mutmut_1(query: str, time: str | None = None) -> dict[str, object]:
    params: dict[str, object] = None
    if time is not None:
        params["time"] = time
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query__mutmut_2(query: str, time: str | None = None) -> dict[str, object]:
    params: dict[str, object] = {"XXqueryXX": query}
    if time is not None:
        params["time"] = time
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query__mutmut_3(query: str, time: str | None = None) -> dict[str, object]:
    params: dict[str, object] = {"QUERY": query}
    if time is not None:
        params["time"] = time
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query__mutmut_4(query: str, time: str | None = None) -> dict[str, object]:
    params: dict[str, object] = {"query": query}
    if time is None:
        params["time"] = time
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query__mutmut_5(query: str, time: str | None = None) -> dict[str, object]:
    params: dict[str, object] = {"query": query}
    if time is not None:
        params["time"] = None
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query__mutmut_6(query: str, time: str | None = None) -> dict[str, object]:
    params: dict[str, object] = {"query": query}
    if time is not None:
        params["XXtimeXX"] = time
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query__mutmut_7(query: str, time: str | None = None) -> dict[str, object]:
    params: dict[str, object] = {"query": query}
    if time is not None:
        params["TIME"] = time
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query__mutmut_8(query: str, time: str | None = None) -> dict[str, object]:
    params: dict[str, object] = {"query": query}
    if time is not None:
        params["time"] = time
    try:
        response = None
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query__mutmut_9(query: str, time: str | None = None) -> dict[str, object]:
    params: dict[str, object] = {"query": query}
    if time is not None:
        params["time"] = time
    try:
        response = httpx.get(
            None,
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query__mutmut_10(query: str, time: str | None = None) -> dict[str, object]:
    params: dict[str, object] = {"query": query}
    if time is not None:
        params["time"] = time
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query",
            params=None,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query__mutmut_11(query: str, time: str | None = None) -> dict[str, object]:
    params: dict[str, object] = {"query": query}
    if time is not None:
        params["time"] = time
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query",
            params=params,  # type: ignore
            timeout=None,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query__mutmut_12(query: str, time: str | None = None) -> dict[str, object]:
    params: dict[str, object] = {"query": query}
    if time is not None:
        params["time"] = time
    try:
        response = httpx.get(
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query__mutmut_13(query: str, time: str | None = None) -> dict[str, object]:
    params: dict[str, object] = {"query": query}
    if time is not None:
        params["time"] = time
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query",
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query__mutmut_14(query: str, time: str | None = None) -> dict[str, object]:
    params: dict[str, object] = {"query": query}
    if time is not None:
        params["time"] = time
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query",
            params=params,  # type: ignore
            )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query__mutmut_15(query: str, time: str | None = None) -> dict[str, object]:
    params: dict[str, object] = {"query": query}
    if time is not None:
        params["time"] = time
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"XXstatusXX": "error", "data": {"result": []}}


def x__prometheus_query__mutmut_16(query: str, time: str | None = None) -> dict[str, object]:
    params: dict[str, object] = {"query": query}
    if time is not None:
        params["time"] = time
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"STATUS": "error", "data": {"result": []}}


def x__prometheus_query__mutmut_17(query: str, time: str | None = None) -> dict[str, object]:
    params: dict[str, object] = {"query": query}
    if time is not None:
        params["time"] = time
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "XXerrorXX", "data": {"result": []}}


def x__prometheus_query__mutmut_18(query: str, time: str | None = None) -> dict[str, object]:
    params: dict[str, object] = {"query": query}
    if time is not None:
        params["time"] = time
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "ERROR", "data": {"result": []}}


def x__prometheus_query__mutmut_19(query: str, time: str | None = None) -> dict[str, object]:
    params: dict[str, object] = {"query": query}
    if time is not None:
        params["time"] = time
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "XXdataXX": {"result": []}}


def x__prometheus_query__mutmut_20(query: str, time: str | None = None) -> dict[str, object]:
    params: dict[str, object] = {"query": query}
    if time is not None:
        params["time"] = time
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "DATA": {"result": []}}


def x__prometheus_query__mutmut_21(query: str, time: str | None = None) -> dict[str, object]:
    params: dict[str, object] = {"query": query}
    if time is not None:
        params["time"] = time
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"XXresultXX": []}}


def x__prometheus_query__mutmut_22(query: str, time: str | None = None) -> dict[str, object]:
    params: dict[str, object] = {"query": query}
    if time is not None:
        params["time"] = time
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"RESULT": []}}

mutants_x__prometheus_query__mutmut['_mutmut_orig'] = x__prometheus_query__mutmut_orig # type: ignore # mutmut generated
mutants_x__prometheus_query__mutmut['x__prometheus_query__mutmut_1'] = x__prometheus_query__mutmut_1 # type: ignore # mutmut generated
mutants_x__prometheus_query__mutmut['x__prometheus_query__mutmut_2'] = x__prometheus_query__mutmut_2 # type: ignore # mutmut generated
mutants_x__prometheus_query__mutmut['x__prometheus_query__mutmut_3'] = x__prometheus_query__mutmut_3 # type: ignore # mutmut generated
mutants_x__prometheus_query__mutmut['x__prometheus_query__mutmut_4'] = x__prometheus_query__mutmut_4 # type: ignore # mutmut generated
mutants_x__prometheus_query__mutmut['x__prometheus_query__mutmut_5'] = x__prometheus_query__mutmut_5 # type: ignore # mutmut generated
mutants_x__prometheus_query__mutmut['x__prometheus_query__mutmut_6'] = x__prometheus_query__mutmut_6 # type: ignore # mutmut generated
mutants_x__prometheus_query__mutmut['x__prometheus_query__mutmut_7'] = x__prometheus_query__mutmut_7 # type: ignore # mutmut generated
mutants_x__prometheus_query__mutmut['x__prometheus_query__mutmut_8'] = x__prometheus_query__mutmut_8 # type: ignore # mutmut generated
mutants_x__prometheus_query__mutmut['x__prometheus_query__mutmut_9'] = x__prometheus_query__mutmut_9 # type: ignore # mutmut generated
mutants_x__prometheus_query__mutmut['x__prometheus_query__mutmut_10'] = x__prometheus_query__mutmut_10 # type: ignore # mutmut generated
mutants_x__prometheus_query__mutmut['x__prometheus_query__mutmut_11'] = x__prometheus_query__mutmut_11 # type: ignore # mutmut generated
mutants_x__prometheus_query__mutmut['x__prometheus_query__mutmut_12'] = x__prometheus_query__mutmut_12 # type: ignore # mutmut generated
mutants_x__prometheus_query__mutmut['x__prometheus_query__mutmut_13'] = x__prometheus_query__mutmut_13 # type: ignore # mutmut generated
mutants_x__prometheus_query__mutmut['x__prometheus_query__mutmut_14'] = x__prometheus_query__mutmut_14 # type: ignore # mutmut generated
mutants_x__prometheus_query__mutmut['x__prometheus_query__mutmut_15'] = x__prometheus_query__mutmut_15 # type: ignore # mutmut generated
mutants_x__prometheus_query__mutmut['x__prometheus_query__mutmut_16'] = x__prometheus_query__mutmut_16 # type: ignore # mutmut generated
mutants_x__prometheus_query__mutmut['x__prometheus_query__mutmut_17'] = x__prometheus_query__mutmut_17 # type: ignore # mutmut generated
mutants_x__prometheus_query__mutmut['x__prometheus_query__mutmut_18'] = x__prometheus_query__mutmut_18 # type: ignore # mutmut generated
mutants_x__prometheus_query__mutmut['x__prometheus_query__mutmut_19'] = x__prometheus_query__mutmut_19 # type: ignore # mutmut generated
mutants_x__prometheus_query__mutmut['x__prometheus_query__mutmut_20'] = x__prometheus_query__mutmut_20 # type: ignore # mutmut generated
mutants_x__prometheus_query__mutmut['x__prometheus_query__mutmut_21'] = x__prometheus_query__mutmut_21 # type: ignore # mutmut generated
mutants_x__prometheus_query__mutmut['x__prometheus_query__mutmut_22'] = x__prometheus_query__mutmut_22 # type: ignore # mutmut generated
mutants_x__prometheus_query_range__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__prometheus_query_range__mutmut)
def _prometheus_query_range(
    query: str,
    start: str,
    end: str,
    step: str = "60s",
) -> dict[str, object]:
    params: dict[str, object] = {
        "query": query,
        "start": start,
        "end": end,
        "step": step,
    }
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query_range",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query_range__mutmut_orig(
    query: str,
    start: str,
    end: str,
    step: str = "60s",
) -> dict[str, object]:
    params: dict[str, object] = {
        "query": query,
        "start": start,
        "end": end,
        "step": step,
    }
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query_range",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query_range__mutmut_1(
    query: str,
    start: str,
    end: str,
    step: str = "XX60sXX",
) -> dict[str, object]:
    params: dict[str, object] = {
        "query": query,
        "start": start,
        "end": end,
        "step": step,
    }
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query_range",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query_range__mutmut_2(
    query: str,
    start: str,
    end: str,
    step: str = "60S",
) -> dict[str, object]:
    params: dict[str, object] = {
        "query": query,
        "start": start,
        "end": end,
        "step": step,
    }
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query_range",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query_range__mutmut_3(
    query: str,
    start: str,
    end: str,
    step: str = "60s",
) -> dict[str, object]:
    params: dict[str, object] = None
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query_range",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query_range__mutmut_4(
    query: str,
    start: str,
    end: str,
    step: str = "60s",
) -> dict[str, object]:
    params: dict[str, object] = {
        "XXqueryXX": query,
        "start": start,
        "end": end,
        "step": step,
    }
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query_range",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query_range__mutmut_5(
    query: str,
    start: str,
    end: str,
    step: str = "60s",
) -> dict[str, object]:
    params: dict[str, object] = {
        "QUERY": query,
        "start": start,
        "end": end,
        "step": step,
    }
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query_range",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query_range__mutmut_6(
    query: str,
    start: str,
    end: str,
    step: str = "60s",
) -> dict[str, object]:
    params: dict[str, object] = {
        "query": query,
        "XXstartXX": start,
        "end": end,
        "step": step,
    }
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query_range",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query_range__mutmut_7(
    query: str,
    start: str,
    end: str,
    step: str = "60s",
) -> dict[str, object]:
    params: dict[str, object] = {
        "query": query,
        "START": start,
        "end": end,
        "step": step,
    }
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query_range",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query_range__mutmut_8(
    query: str,
    start: str,
    end: str,
    step: str = "60s",
) -> dict[str, object]:
    params: dict[str, object] = {
        "query": query,
        "start": start,
        "XXendXX": end,
        "step": step,
    }
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query_range",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query_range__mutmut_9(
    query: str,
    start: str,
    end: str,
    step: str = "60s",
) -> dict[str, object]:
    params: dict[str, object] = {
        "query": query,
        "start": start,
        "END": end,
        "step": step,
    }
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query_range",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query_range__mutmut_10(
    query: str,
    start: str,
    end: str,
    step: str = "60s",
) -> dict[str, object]:
    params: dict[str, object] = {
        "query": query,
        "start": start,
        "end": end,
        "XXstepXX": step,
    }
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query_range",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query_range__mutmut_11(
    query: str,
    start: str,
    end: str,
    step: str = "60s",
) -> dict[str, object]:
    params: dict[str, object] = {
        "query": query,
        "start": start,
        "end": end,
        "STEP": step,
    }
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query_range",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query_range__mutmut_12(
    query: str,
    start: str,
    end: str,
    step: str = "60s",
) -> dict[str, object]:
    params: dict[str, object] = {
        "query": query,
        "start": start,
        "end": end,
        "step": step,
    }
    try:
        response = None
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query_range__mutmut_13(
    query: str,
    start: str,
    end: str,
    step: str = "60s",
) -> dict[str, object]:
    params: dict[str, object] = {
        "query": query,
        "start": start,
        "end": end,
        "step": step,
    }
    try:
        response = httpx.get(
            None,
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query_range__mutmut_14(
    query: str,
    start: str,
    end: str,
    step: str = "60s",
) -> dict[str, object]:
    params: dict[str, object] = {
        "query": query,
        "start": start,
        "end": end,
        "step": step,
    }
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query_range",
            params=None,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query_range__mutmut_15(
    query: str,
    start: str,
    end: str,
    step: str = "60s",
) -> dict[str, object]:
    params: dict[str, object] = {
        "query": query,
        "start": start,
        "end": end,
        "step": step,
    }
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query_range",
            params=params,  # type: ignore
            timeout=None,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query_range__mutmut_16(
    query: str,
    start: str,
    end: str,
    step: str = "60s",
) -> dict[str, object]:
    params: dict[str, object] = {
        "query": query,
        "start": start,
        "end": end,
        "step": step,
    }
    try:
        response = httpx.get(
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query_range__mutmut_17(
    query: str,
    start: str,
    end: str,
    step: str = "60s",
) -> dict[str, object]:
    params: dict[str, object] = {
        "query": query,
        "start": start,
        "end": end,
        "step": step,
    }
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query_range",
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query_range__mutmut_18(
    query: str,
    start: str,
    end: str,
    step: str = "60s",
) -> dict[str, object]:
    params: dict[str, object] = {
        "query": query,
        "start": start,
        "end": end,
        "step": step,
    }
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query_range",
            params=params,  # type: ignore
            )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"result": []}}


def x__prometheus_query_range__mutmut_19(
    query: str,
    start: str,
    end: str,
    step: str = "60s",
) -> dict[str, object]:
    params: dict[str, object] = {
        "query": query,
        "start": start,
        "end": end,
        "step": step,
    }
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query_range",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"XXstatusXX": "error", "data": {"result": []}}


def x__prometheus_query_range__mutmut_20(
    query: str,
    start: str,
    end: str,
    step: str = "60s",
) -> dict[str, object]:
    params: dict[str, object] = {
        "query": query,
        "start": start,
        "end": end,
        "step": step,
    }
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query_range",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"STATUS": "error", "data": {"result": []}}


def x__prometheus_query_range__mutmut_21(
    query: str,
    start: str,
    end: str,
    step: str = "60s",
) -> dict[str, object]:
    params: dict[str, object] = {
        "query": query,
        "start": start,
        "end": end,
        "step": step,
    }
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query_range",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "XXerrorXX", "data": {"result": []}}


def x__prometheus_query_range__mutmut_22(
    query: str,
    start: str,
    end: str,
    step: str = "60s",
) -> dict[str, object]:
    params: dict[str, object] = {
        "query": query,
        "start": start,
        "end": end,
        "step": step,
    }
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query_range",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "ERROR", "data": {"result": []}}


def x__prometheus_query_range__mutmut_23(
    query: str,
    start: str,
    end: str,
    step: str = "60s",
) -> dict[str, object]:
    params: dict[str, object] = {
        "query": query,
        "start": start,
        "end": end,
        "step": step,
    }
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query_range",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "XXdataXX": {"result": []}}


def x__prometheus_query_range__mutmut_24(
    query: str,
    start: str,
    end: str,
    step: str = "60s",
) -> dict[str, object]:
    params: dict[str, object] = {
        "query": query,
        "start": start,
        "end": end,
        "step": step,
    }
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query_range",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "DATA": {"result": []}}


def x__prometheus_query_range__mutmut_25(
    query: str,
    start: str,
    end: str,
    step: str = "60s",
) -> dict[str, object]:
    params: dict[str, object] = {
        "query": query,
        "start": start,
        "end": end,
        "step": step,
    }
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query_range",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"XXresultXX": []}}


def x__prometheus_query_range__mutmut_26(
    query: str,
    start: str,
    end: str,
    step: str = "60s",
) -> dict[str, object]:
    params: dict[str, object] = {
        "query": query,
        "start": start,
        "end": end,
        "step": step,
    }
    try:
        response = httpx.get(
            f"{_PROMETHEUS_URL}/api/v1/query_range",
            params=params,  # type: ignore
            timeout=_REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        return response.json()  # type: ignore
    except Exception:
        return {"status": "error", "data": {"RESULT": []}}

mutants_x__prometheus_query_range__mutmut['_mutmut_orig'] = x__prometheus_query_range__mutmut_orig # type: ignore # mutmut generated
mutants_x__prometheus_query_range__mutmut['x__prometheus_query_range__mutmut_1'] = x__prometheus_query_range__mutmut_1 # type: ignore # mutmut generated
mutants_x__prometheus_query_range__mutmut['x__prometheus_query_range__mutmut_2'] = x__prometheus_query_range__mutmut_2 # type: ignore # mutmut generated
mutants_x__prometheus_query_range__mutmut['x__prometheus_query_range__mutmut_3'] = x__prometheus_query_range__mutmut_3 # type: ignore # mutmut generated
mutants_x__prometheus_query_range__mutmut['x__prometheus_query_range__mutmut_4'] = x__prometheus_query_range__mutmut_4 # type: ignore # mutmut generated
mutants_x__prometheus_query_range__mutmut['x__prometheus_query_range__mutmut_5'] = x__prometheus_query_range__mutmut_5 # type: ignore # mutmut generated
mutants_x__prometheus_query_range__mutmut['x__prometheus_query_range__mutmut_6'] = x__prometheus_query_range__mutmut_6 # type: ignore # mutmut generated
mutants_x__prometheus_query_range__mutmut['x__prometheus_query_range__mutmut_7'] = x__prometheus_query_range__mutmut_7 # type: ignore # mutmut generated
mutants_x__prometheus_query_range__mutmut['x__prometheus_query_range__mutmut_8'] = x__prometheus_query_range__mutmut_8 # type: ignore # mutmut generated
mutants_x__prometheus_query_range__mutmut['x__prometheus_query_range__mutmut_9'] = x__prometheus_query_range__mutmut_9 # type: ignore # mutmut generated
mutants_x__prometheus_query_range__mutmut['x__prometheus_query_range__mutmut_10'] = x__prometheus_query_range__mutmut_10 # type: ignore # mutmut generated
mutants_x__prometheus_query_range__mutmut['x__prometheus_query_range__mutmut_11'] = x__prometheus_query_range__mutmut_11 # type: ignore # mutmut generated
mutants_x__prometheus_query_range__mutmut['x__prometheus_query_range__mutmut_12'] = x__prometheus_query_range__mutmut_12 # type: ignore # mutmut generated
mutants_x__prometheus_query_range__mutmut['x__prometheus_query_range__mutmut_13'] = x__prometheus_query_range__mutmut_13 # type: ignore # mutmut generated
mutants_x__prometheus_query_range__mutmut['x__prometheus_query_range__mutmut_14'] = x__prometheus_query_range__mutmut_14 # type: ignore # mutmut generated
mutants_x__prometheus_query_range__mutmut['x__prometheus_query_range__mutmut_15'] = x__prometheus_query_range__mutmut_15 # type: ignore # mutmut generated
mutants_x__prometheus_query_range__mutmut['x__prometheus_query_range__mutmut_16'] = x__prometheus_query_range__mutmut_16 # type: ignore # mutmut generated
mutants_x__prometheus_query_range__mutmut['x__prometheus_query_range__mutmut_17'] = x__prometheus_query_range__mutmut_17 # type: ignore # mutmut generated
mutants_x__prometheus_query_range__mutmut['x__prometheus_query_range__mutmut_18'] = x__prometheus_query_range__mutmut_18 # type: ignore # mutmut generated
mutants_x__prometheus_query_range__mutmut['x__prometheus_query_range__mutmut_19'] = x__prometheus_query_range__mutmut_19 # type: ignore # mutmut generated
mutants_x__prometheus_query_range__mutmut['x__prometheus_query_range__mutmut_20'] = x__prometheus_query_range__mutmut_20 # type: ignore # mutmut generated
mutants_x__prometheus_query_range__mutmut['x__prometheus_query_range__mutmut_21'] = x__prometheus_query_range__mutmut_21 # type: ignore # mutmut generated
mutants_x__prometheus_query_range__mutmut['x__prometheus_query_range__mutmut_22'] = x__prometheus_query_range__mutmut_22 # type: ignore # mutmut generated
mutants_x__prometheus_query_range__mutmut['x__prometheus_query_range__mutmut_23'] = x__prometheus_query_range__mutmut_23 # type: ignore # mutmut generated
mutants_x__prometheus_query_range__mutmut['x__prometheus_query_range__mutmut_24'] = x__prometheus_query_range__mutmut_24 # type: ignore # mutmut generated
mutants_x__prometheus_query_range__mutmut['x__prometheus_query_range__mutmut_25'] = x__prometheus_query_range__mutmut_25 # type: ignore # mutmut generated
mutants_x__prometheus_query_range__mutmut['x__prometheus_query_range__mutmut_26'] = x__prometheus_query_range__mutmut_26 # type: ignore # mutmut generated
mutants_x_list_jaeger_services__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_list_jaeger_services__mutmut)
def list_jaeger_services() -> list[str]:
    result = _jaeger_get("/api/services")
    data = result.get("data")
    if isinstance(data, list):
        return [str(s) for s in data]
    return []


def x_list_jaeger_services__mutmut_orig() -> list[str]:
    result = _jaeger_get("/api/services")
    data = result.get("data")
    if isinstance(data, list):
        return [str(s) for s in data]
    return []


def x_list_jaeger_services__mutmut_1() -> list[str]:
    result = None
    data = result.get("data")
    if isinstance(data, list):
        return [str(s) for s in data]
    return []


def x_list_jaeger_services__mutmut_2() -> list[str]:
    result = _jaeger_get(None)
    data = result.get("data")
    if isinstance(data, list):
        return [str(s) for s in data]
    return []


def x_list_jaeger_services__mutmut_3() -> list[str]:
    result = _jaeger_get("XX/api/servicesXX")
    data = result.get("data")
    if isinstance(data, list):
        return [str(s) for s in data]
    return []


def x_list_jaeger_services__mutmut_4() -> list[str]:
    result = _jaeger_get("/API/SERVICES")
    data = result.get("data")
    if isinstance(data, list):
        return [str(s) for s in data]
    return []


def x_list_jaeger_services__mutmut_5() -> list[str]:
    result = _jaeger_get("/api/services")
    data = None
    if isinstance(data, list):
        return [str(s) for s in data]
    return []


def x_list_jaeger_services__mutmut_6() -> list[str]:
    result = _jaeger_get("/api/services")
    data = result.get(None)
    if isinstance(data, list):
        return [str(s) for s in data]
    return []


def x_list_jaeger_services__mutmut_7() -> list[str]:
    result = _jaeger_get("/api/services")
    data = result.get("XXdataXX")
    if isinstance(data, list):
        return [str(s) for s in data]
    return []


def x_list_jaeger_services__mutmut_8() -> list[str]:
    result = _jaeger_get("/api/services")
    data = result.get("DATA")
    if isinstance(data, list):
        return [str(s) for s in data]
    return []


def x_list_jaeger_services__mutmut_9() -> list[str]:
    result = _jaeger_get("/api/services")
    data = result.get("data")
    if isinstance(data, list):
        return [str(None) for s in data]
    return []

mutants_x_list_jaeger_services__mutmut['_mutmut_orig'] = x_list_jaeger_services__mutmut_orig # type: ignore # mutmut generated
mutants_x_list_jaeger_services__mutmut['x_list_jaeger_services__mutmut_1'] = x_list_jaeger_services__mutmut_1 # type: ignore # mutmut generated
mutants_x_list_jaeger_services__mutmut['x_list_jaeger_services__mutmut_2'] = x_list_jaeger_services__mutmut_2 # type: ignore # mutmut generated
mutants_x_list_jaeger_services__mutmut['x_list_jaeger_services__mutmut_3'] = x_list_jaeger_services__mutmut_3 # type: ignore # mutmut generated
mutants_x_list_jaeger_services__mutmut['x_list_jaeger_services__mutmut_4'] = x_list_jaeger_services__mutmut_4 # type: ignore # mutmut generated
mutants_x_list_jaeger_services__mutmut['x_list_jaeger_services__mutmut_5'] = x_list_jaeger_services__mutmut_5 # type: ignore # mutmut generated
mutants_x_list_jaeger_services__mutmut['x_list_jaeger_services__mutmut_6'] = x_list_jaeger_services__mutmut_6 # type: ignore # mutmut generated
mutants_x_list_jaeger_services__mutmut['x_list_jaeger_services__mutmut_7'] = x_list_jaeger_services__mutmut_7 # type: ignore # mutmut generated
mutants_x_list_jaeger_services__mutmut['x_list_jaeger_services__mutmut_8'] = x_list_jaeger_services__mutmut_8 # type: ignore # mutmut generated
mutants_x_list_jaeger_services__mutmut['x_list_jaeger_services__mutmut_9'] = x_list_jaeger_services__mutmut_9 # type: ignore # mutmut generated
mutants_x_list_jaeger_operations__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_list_jaeger_operations__mutmut)
def list_jaeger_operations(service: str) -> list[str]:
    result = _jaeger_get(f"/api/services/{service}/operations")
    data = result.get("data")
    if isinstance(data, list):
        return [str(op) if isinstance(op, str) else str(op.get("name", "")) for op in data]
    return []


def x_list_jaeger_operations__mutmut_orig(service: str) -> list[str]:
    result = _jaeger_get(f"/api/services/{service}/operations")
    data = result.get("data")
    if isinstance(data, list):
        return [str(op) if isinstance(op, str) else str(op.get("name", "")) for op in data]
    return []


def x_list_jaeger_operations__mutmut_1(service: str) -> list[str]:
    result = None
    data = result.get("data")
    if isinstance(data, list):
        return [str(op) if isinstance(op, str) else str(op.get("name", "")) for op in data]
    return []


def x_list_jaeger_operations__mutmut_2(service: str) -> list[str]:
    result = _jaeger_get(None)
    data = result.get("data")
    if isinstance(data, list):
        return [str(op) if isinstance(op, str) else str(op.get("name", "")) for op in data]
    return []


def x_list_jaeger_operations__mutmut_3(service: str) -> list[str]:
    result = _jaeger_get(f"/api/services/{service}/operations")
    data = None
    if isinstance(data, list):
        return [str(op) if isinstance(op, str) else str(op.get("name", "")) for op in data]
    return []


def x_list_jaeger_operations__mutmut_4(service: str) -> list[str]:
    result = _jaeger_get(f"/api/services/{service}/operations")
    data = result.get(None)
    if isinstance(data, list):
        return [str(op) if isinstance(op, str) else str(op.get("name", "")) for op in data]
    return []


def x_list_jaeger_operations__mutmut_5(service: str) -> list[str]:
    result = _jaeger_get(f"/api/services/{service}/operations")
    data = result.get("XXdataXX")
    if isinstance(data, list):
        return [str(op) if isinstance(op, str) else str(op.get("name", "")) for op in data]
    return []


def x_list_jaeger_operations__mutmut_6(service: str) -> list[str]:
    result = _jaeger_get(f"/api/services/{service}/operations")
    data = result.get("DATA")
    if isinstance(data, list):
        return [str(op) if isinstance(op, str) else str(op.get("name", "")) for op in data]
    return []


def x_list_jaeger_operations__mutmut_7(service: str) -> list[str]:
    result = _jaeger_get(f"/api/services/{service}/operations")
    data = result.get("data")
    if isinstance(data, list):
        return [str(None) if isinstance(op, str) else str(op.get("name", "")) for op in data]
    return []


def x_list_jaeger_operations__mutmut_8(service: str) -> list[str]:
    result = _jaeger_get(f"/api/services/{service}/operations")
    data = result.get("data")
    if isinstance(data, list):
        return [str(op) if isinstance(op, str) else str(None) for op in data]
    return []


def x_list_jaeger_operations__mutmut_9(service: str) -> list[str]:
    result = _jaeger_get(f"/api/services/{service}/operations")
    data = result.get("data")
    if isinstance(data, list):
        return [str(op) if isinstance(op, str) else str(op.get(None, "")) for op in data]
    return []


def x_list_jaeger_operations__mutmut_10(service: str) -> list[str]:
    result = _jaeger_get(f"/api/services/{service}/operations")
    data = result.get("data")
    if isinstance(data, list):
        return [str(op) if isinstance(op, str) else str(op.get("name", None)) for op in data]
    return []


def x_list_jaeger_operations__mutmut_11(service: str) -> list[str]:
    result = _jaeger_get(f"/api/services/{service}/operations")
    data = result.get("data")
    if isinstance(data, list):
        return [str(op) if isinstance(op, str) else str(op.get("")) for op in data]
    return []


def x_list_jaeger_operations__mutmut_12(service: str) -> list[str]:
    result = _jaeger_get(f"/api/services/{service}/operations")
    data = result.get("data")
    if isinstance(data, list):
        return [str(op) if isinstance(op, str) else str(op.get("name", )) for op in data]
    return []


def x_list_jaeger_operations__mutmut_13(service: str) -> list[str]:
    result = _jaeger_get(f"/api/services/{service}/operations")
    data = result.get("data")
    if isinstance(data, list):
        return [str(op) if isinstance(op, str) else str(op.get("XXnameXX", "")) for op in data]
    return []


def x_list_jaeger_operations__mutmut_14(service: str) -> list[str]:
    result = _jaeger_get(f"/api/services/{service}/operations")
    data = result.get("data")
    if isinstance(data, list):
        return [str(op) if isinstance(op, str) else str(op.get("NAME", "")) for op in data]
    return []


def x_list_jaeger_operations__mutmut_15(service: str) -> list[str]:
    result = _jaeger_get(f"/api/services/{service}/operations")
    data = result.get("data")
    if isinstance(data, list):
        return [str(op) if isinstance(op, str) else str(op.get("name", "XXXX")) for op in data]
    return []

mutants_x_list_jaeger_operations__mutmut['_mutmut_orig'] = x_list_jaeger_operations__mutmut_orig # type: ignore # mutmut generated
mutants_x_list_jaeger_operations__mutmut['x_list_jaeger_operations__mutmut_1'] = x_list_jaeger_operations__mutmut_1 # type: ignore # mutmut generated
mutants_x_list_jaeger_operations__mutmut['x_list_jaeger_operations__mutmut_2'] = x_list_jaeger_operations__mutmut_2 # type: ignore # mutmut generated
mutants_x_list_jaeger_operations__mutmut['x_list_jaeger_operations__mutmut_3'] = x_list_jaeger_operations__mutmut_3 # type: ignore # mutmut generated
mutants_x_list_jaeger_operations__mutmut['x_list_jaeger_operations__mutmut_4'] = x_list_jaeger_operations__mutmut_4 # type: ignore # mutmut generated
mutants_x_list_jaeger_operations__mutmut['x_list_jaeger_operations__mutmut_5'] = x_list_jaeger_operations__mutmut_5 # type: ignore # mutmut generated
mutants_x_list_jaeger_operations__mutmut['x_list_jaeger_operations__mutmut_6'] = x_list_jaeger_operations__mutmut_6 # type: ignore # mutmut generated
mutants_x_list_jaeger_operations__mutmut['x_list_jaeger_operations__mutmut_7'] = x_list_jaeger_operations__mutmut_7 # type: ignore # mutmut generated
mutants_x_list_jaeger_operations__mutmut['x_list_jaeger_operations__mutmut_8'] = x_list_jaeger_operations__mutmut_8 # type: ignore # mutmut generated
mutants_x_list_jaeger_operations__mutmut['x_list_jaeger_operations__mutmut_9'] = x_list_jaeger_operations__mutmut_9 # type: ignore # mutmut generated
mutants_x_list_jaeger_operations__mutmut['x_list_jaeger_operations__mutmut_10'] = x_list_jaeger_operations__mutmut_10 # type: ignore # mutmut generated
mutants_x_list_jaeger_operations__mutmut['x_list_jaeger_operations__mutmut_11'] = x_list_jaeger_operations__mutmut_11 # type: ignore # mutmut generated
mutants_x_list_jaeger_operations__mutmut['x_list_jaeger_operations__mutmut_12'] = x_list_jaeger_operations__mutmut_12 # type: ignore # mutmut generated
mutants_x_list_jaeger_operations__mutmut['x_list_jaeger_operations__mutmut_13'] = x_list_jaeger_operations__mutmut_13 # type: ignore # mutmut generated
mutants_x_list_jaeger_operations__mutmut['x_list_jaeger_operations__mutmut_14'] = x_list_jaeger_operations__mutmut_14 # type: ignore # mutmut generated
mutants_x_list_jaeger_operations__mutmut['x_list_jaeger_operations__mutmut_15'] = x_list_jaeger_operations__mutmut_15 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_search_jaeger_traces__mutmut)
def search_jaeger_traces(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_orig(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_1(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 21,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_2(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = True,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_3(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = None
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_4(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"XXserviceXX": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_5(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"SERVICE": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_6(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "XXlimitXX": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_7(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "LIMIT": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_8(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = None
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_9(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["XXoperationXX"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_10(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["OPERATION"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_11(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = None
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_12(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["XXstartXX"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_13(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["START"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_14(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = None
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_15(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["XXtagsXX"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_16(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["TAGS"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_17(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = 'XX{"error":true}XX'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_18(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"ERROR":TRUE}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_19(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = None

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_20(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["XXminDurationXX"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_21(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minduration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_22(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["MINDURATION"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_23(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = None
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_24(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get(None, params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_25(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", None)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_26(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get(params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_27(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", )
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_28(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("XX/api/tracesXX", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_29(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/API/TRACES", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_30(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = None
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_31(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get(None)
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_32(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("XXdataXX")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_33(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("DATA")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_34(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = None
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_35(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = None
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_36(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get(None, [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_37(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", None)
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_38(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get([])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_39(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", )
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_40(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("XXspansXX", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_41(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("SPANS", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_42(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = None
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_43(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = None
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_44(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 1
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_45(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = None
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_46(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = True
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_47(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = None
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_48(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[1]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_49(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = None
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_50(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(None)
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_51(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get(None, 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_52(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", None))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_53(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get(0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_54(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", ))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_55(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("XXdurationXX", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_56(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("DURATION", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_57(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 1))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_58(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = None
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_59(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get(None, [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_60(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", None)
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_61(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get([])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_62(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", )
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_63(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("XXtagsXX", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_64(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("TAGS", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_65(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) or tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_66(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get(None) == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_67(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("XXkeyXX") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_68(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("KEY") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_69(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") != "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_70(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "XXerrorXX":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_71(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "ERROR":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_72(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = None
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_73(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = False
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_74(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        return
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_75(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = None
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_76(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "XXtraceIDXX": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_77(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceid": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_78(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "TRACEID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_79(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(None),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_80(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get(None, "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_81(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", None)),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_82(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_83(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", )),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_84(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("XXtraceIDXX", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_85(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceid", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_86(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("TRACEID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_87(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "XXXX")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_88(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "XXserviceCountXX": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_89(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "servicecount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_90(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "SERVICECOUNT": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_91(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 2,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_92(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "XXspanCountXX": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_93(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spancount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_94(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "SPANCOUNT": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_95(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "XXdurationXX": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_96(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "DURATION": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_97(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "XXhasErrorsXX": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_98(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "haserrors": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_99(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "HASERRORS": has_errors,
                }
                traces.append(trace)
        return traces
    return []


def x_search_jaeger_traces__mutmut_100(  # noqa: C901, PLR0912, PLR0913
    service: str,
    operation: str | None = None,
    limit: int = 20,
    start_time: str | None = None,
    with_errors: bool = False,
    duration_min: str | None = None,
) -> list[JaegerTraceSummaryDict]:
    params: dict[str, object] = {"service": service, "limit": limit}
    if operation:
        params["operation"] = operation
    if start_time:
        params["start"] = start_time
    if with_errors:
        params["tags"] = '{"error":true}'
    if duration_min:
        params["minDuration"] = duration_min

    result = _jaeger_get("/api/traces", params)
    data = result.get("data")
    if isinstance(data, list):
        traces: list[JaegerTraceSummaryDict] = []
        for t in data:
            if isinstance(t, dict):
                spans = t.get("spans", [])
                span_list = spans if isinstance(spans, list) else []
                first_span_duration = 0
                has_errors = False
                if span_list:
                    first = span_list[0]
                    if isinstance(first, dict):
                        first_span_duration = int(first.get("duration", 0))
                    for s in span_list:
                        if isinstance(s, dict):
                            tags = s.get("tags", [])
                            if isinstance(tags, list):
                                for tag in tags:
                                    if isinstance(tag, dict) and tag.get("key") == "error":
                                        has_errors = True
                                        break
                trace: JaegerTraceSummaryDict = {
                    "traceID": str(t.get("traceID", "")),
                    "serviceCount": 1,
                    "spanCount": len(span_list),
                    "duration": first_span_duration,
                    "hasErrors": has_errors,
                }
                traces.append(None)
        return traces
    return []

mutants_x_search_jaeger_traces__mutmut['_mutmut_orig'] = x_search_jaeger_traces__mutmut_orig # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_1'] = x_search_jaeger_traces__mutmut_1 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_2'] = x_search_jaeger_traces__mutmut_2 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_3'] = x_search_jaeger_traces__mutmut_3 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_4'] = x_search_jaeger_traces__mutmut_4 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_5'] = x_search_jaeger_traces__mutmut_5 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_6'] = x_search_jaeger_traces__mutmut_6 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_7'] = x_search_jaeger_traces__mutmut_7 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_8'] = x_search_jaeger_traces__mutmut_8 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_9'] = x_search_jaeger_traces__mutmut_9 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_10'] = x_search_jaeger_traces__mutmut_10 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_11'] = x_search_jaeger_traces__mutmut_11 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_12'] = x_search_jaeger_traces__mutmut_12 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_13'] = x_search_jaeger_traces__mutmut_13 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_14'] = x_search_jaeger_traces__mutmut_14 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_15'] = x_search_jaeger_traces__mutmut_15 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_16'] = x_search_jaeger_traces__mutmut_16 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_17'] = x_search_jaeger_traces__mutmut_17 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_18'] = x_search_jaeger_traces__mutmut_18 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_19'] = x_search_jaeger_traces__mutmut_19 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_20'] = x_search_jaeger_traces__mutmut_20 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_21'] = x_search_jaeger_traces__mutmut_21 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_22'] = x_search_jaeger_traces__mutmut_22 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_23'] = x_search_jaeger_traces__mutmut_23 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_24'] = x_search_jaeger_traces__mutmut_24 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_25'] = x_search_jaeger_traces__mutmut_25 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_26'] = x_search_jaeger_traces__mutmut_26 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_27'] = x_search_jaeger_traces__mutmut_27 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_28'] = x_search_jaeger_traces__mutmut_28 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_29'] = x_search_jaeger_traces__mutmut_29 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_30'] = x_search_jaeger_traces__mutmut_30 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_31'] = x_search_jaeger_traces__mutmut_31 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_32'] = x_search_jaeger_traces__mutmut_32 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_33'] = x_search_jaeger_traces__mutmut_33 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_34'] = x_search_jaeger_traces__mutmut_34 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_35'] = x_search_jaeger_traces__mutmut_35 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_36'] = x_search_jaeger_traces__mutmut_36 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_37'] = x_search_jaeger_traces__mutmut_37 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_38'] = x_search_jaeger_traces__mutmut_38 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_39'] = x_search_jaeger_traces__mutmut_39 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_40'] = x_search_jaeger_traces__mutmut_40 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_41'] = x_search_jaeger_traces__mutmut_41 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_42'] = x_search_jaeger_traces__mutmut_42 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_43'] = x_search_jaeger_traces__mutmut_43 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_44'] = x_search_jaeger_traces__mutmut_44 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_45'] = x_search_jaeger_traces__mutmut_45 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_46'] = x_search_jaeger_traces__mutmut_46 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_47'] = x_search_jaeger_traces__mutmut_47 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_48'] = x_search_jaeger_traces__mutmut_48 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_49'] = x_search_jaeger_traces__mutmut_49 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_50'] = x_search_jaeger_traces__mutmut_50 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_51'] = x_search_jaeger_traces__mutmut_51 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_52'] = x_search_jaeger_traces__mutmut_52 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_53'] = x_search_jaeger_traces__mutmut_53 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_54'] = x_search_jaeger_traces__mutmut_54 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_55'] = x_search_jaeger_traces__mutmut_55 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_56'] = x_search_jaeger_traces__mutmut_56 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_57'] = x_search_jaeger_traces__mutmut_57 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_58'] = x_search_jaeger_traces__mutmut_58 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_59'] = x_search_jaeger_traces__mutmut_59 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_60'] = x_search_jaeger_traces__mutmut_60 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_61'] = x_search_jaeger_traces__mutmut_61 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_62'] = x_search_jaeger_traces__mutmut_62 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_63'] = x_search_jaeger_traces__mutmut_63 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_64'] = x_search_jaeger_traces__mutmut_64 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_65'] = x_search_jaeger_traces__mutmut_65 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_66'] = x_search_jaeger_traces__mutmut_66 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_67'] = x_search_jaeger_traces__mutmut_67 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_68'] = x_search_jaeger_traces__mutmut_68 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_69'] = x_search_jaeger_traces__mutmut_69 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_70'] = x_search_jaeger_traces__mutmut_70 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_71'] = x_search_jaeger_traces__mutmut_71 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_72'] = x_search_jaeger_traces__mutmut_72 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_73'] = x_search_jaeger_traces__mutmut_73 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_74'] = x_search_jaeger_traces__mutmut_74 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_75'] = x_search_jaeger_traces__mutmut_75 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_76'] = x_search_jaeger_traces__mutmut_76 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_77'] = x_search_jaeger_traces__mutmut_77 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_78'] = x_search_jaeger_traces__mutmut_78 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_79'] = x_search_jaeger_traces__mutmut_79 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_80'] = x_search_jaeger_traces__mutmut_80 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_81'] = x_search_jaeger_traces__mutmut_81 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_82'] = x_search_jaeger_traces__mutmut_82 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_83'] = x_search_jaeger_traces__mutmut_83 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_84'] = x_search_jaeger_traces__mutmut_84 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_85'] = x_search_jaeger_traces__mutmut_85 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_86'] = x_search_jaeger_traces__mutmut_86 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_87'] = x_search_jaeger_traces__mutmut_87 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_88'] = x_search_jaeger_traces__mutmut_88 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_89'] = x_search_jaeger_traces__mutmut_89 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_90'] = x_search_jaeger_traces__mutmut_90 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_91'] = x_search_jaeger_traces__mutmut_91 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_92'] = x_search_jaeger_traces__mutmut_92 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_93'] = x_search_jaeger_traces__mutmut_93 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_94'] = x_search_jaeger_traces__mutmut_94 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_95'] = x_search_jaeger_traces__mutmut_95 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_96'] = x_search_jaeger_traces__mutmut_96 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_97'] = x_search_jaeger_traces__mutmut_97 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_98'] = x_search_jaeger_traces__mutmut_98 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_99'] = x_search_jaeger_traces__mutmut_99 # type: ignore # mutmut generated
mutants_x_search_jaeger_traces__mutmut['x_search_jaeger_traces__mutmut_100'] = x_search_jaeger_traces__mutmut_100 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_jaeger_trace__mutmut)
def get_jaeger_trace(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceID", "")),
                "spans": _parse_spans(first.get("spans", [])),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_orig(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceID", "")),
                "spans": _parse_spans(first.get("spans", [])),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_1(trace_id: str) -> JaegerTraceDict | None:
    result = None
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceID", "")),
                "spans": _parse_spans(first.get("spans", [])),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_2(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(None)
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceID", "")),
                "spans": _parse_spans(first.get("spans", [])),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_3(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = None
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceID", "")),
                "spans": _parse_spans(first.get("spans", [])),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_4(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get(None)
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceID", "")),
                "spans": _parse_spans(first.get("spans", [])),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_5(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("XXdataXX")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceID", "")),
                "spans": _parse_spans(first.get("spans", [])),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_6(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("DATA")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceID", "")),
                "spans": _parse_spans(first.get("spans", [])),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_7(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) or len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceID", "")),
                "spans": _parse_spans(first.get("spans", [])),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_8(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) >= 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceID", "")),
                "spans": _parse_spans(first.get("spans", [])),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_9(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 1:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceID", "")),
                "spans": _parse_spans(first.get("spans", [])),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_10(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = None
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceID", "")),
                "spans": _parse_spans(first.get("spans", [])),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_11(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[1]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceID", "")),
                "spans": _parse_spans(first.get("spans", [])),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_12(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "XXtraceIDXX": str(first.get("traceID", "")),
                "spans": _parse_spans(first.get("spans", [])),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_13(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceid": str(first.get("traceID", "")),
                "spans": _parse_spans(first.get("spans", [])),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_14(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "TRACEID": str(first.get("traceID", "")),
                "spans": _parse_spans(first.get("spans", [])),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_15(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(None),
                "spans": _parse_spans(first.get("spans", [])),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_16(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get(None, "")),
                "spans": _parse_spans(first.get("spans", [])),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_17(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceID", None)),
                "spans": _parse_spans(first.get("spans", [])),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_18(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("")),
                "spans": _parse_spans(first.get("spans", [])),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_19(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceID", )),
                "spans": _parse_spans(first.get("spans", [])),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_20(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("XXtraceIDXX", "")),
                "spans": _parse_spans(first.get("spans", [])),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_21(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceid", "")),
                "spans": _parse_spans(first.get("spans", [])),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_22(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("TRACEID", "")),
                "spans": _parse_spans(first.get("spans", [])),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_23(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceID", "XXXX")),
                "spans": _parse_spans(first.get("spans", [])),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_24(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceID", "")),
                "XXspansXX": _parse_spans(first.get("spans", [])),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_25(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceID", "")),
                "SPANS": _parse_spans(first.get("spans", [])),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_26(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceID", "")),
                "spans": _parse_spans(None),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_27(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceID", "")),
                "spans": _parse_spans(first.get(None, [])),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_28(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceID", "")),
                "spans": _parse_spans(first.get("spans", None)),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_29(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceID", "")),
                "spans": _parse_spans(first.get([])),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_30(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceID", "")),
                "spans": _parse_spans(first.get("spans", )),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_31(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceID", "")),
                "spans": _parse_spans(first.get("XXspansXX", [])),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_32(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceID", "")),
                "spans": _parse_spans(first.get("SPANS", [])),
                "processes": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_33(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceID", "")),
                "spans": _parse_spans(first.get("spans", [])),
                "XXprocessesXX": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_34(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceID", "")),
                "spans": _parse_spans(first.get("spans", [])),
                "PROCESSES": first.get("processes", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_35(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceID", "")),
                "spans": _parse_spans(first.get("spans", [])),
                "processes": first.get(None, {}),
            }
    return None


def x_get_jaeger_trace__mutmut_36(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceID", "")),
                "spans": _parse_spans(first.get("spans", [])),
                "processes": first.get("processes", None),
            }
    return None


def x_get_jaeger_trace__mutmut_37(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceID", "")),
                "spans": _parse_spans(first.get("spans", [])),
                "processes": first.get({}),
            }
    return None


def x_get_jaeger_trace__mutmut_38(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceID", "")),
                "spans": _parse_spans(first.get("spans", [])),
                "processes": first.get("processes", ),
            }
    return None


def x_get_jaeger_trace__mutmut_39(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceID", "")),
                "spans": _parse_spans(first.get("spans", [])),
                "processes": first.get("XXprocessesXX", {}),
            }
    return None


def x_get_jaeger_trace__mutmut_40(trace_id: str) -> JaegerTraceDict | None:
    result = _jaeger_get(f"/api/traces/{trace_id}")
    data = result.get("data")
    if isinstance(data, list) and len(data) > 0:
        first = data[0]
        if isinstance(first, dict):
            return {
                "traceID": str(first.get("traceID", "")),
                "spans": _parse_spans(first.get("spans", [])),
                "processes": first.get("PROCESSES", {}),
            }
    return None

mutants_x_get_jaeger_trace__mutmut['_mutmut_orig'] = x_get_jaeger_trace__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_1'] = x_get_jaeger_trace__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_2'] = x_get_jaeger_trace__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_3'] = x_get_jaeger_trace__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_4'] = x_get_jaeger_trace__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_5'] = x_get_jaeger_trace__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_6'] = x_get_jaeger_trace__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_7'] = x_get_jaeger_trace__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_8'] = x_get_jaeger_trace__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_9'] = x_get_jaeger_trace__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_10'] = x_get_jaeger_trace__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_11'] = x_get_jaeger_trace__mutmut_11 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_12'] = x_get_jaeger_trace__mutmut_12 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_13'] = x_get_jaeger_trace__mutmut_13 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_14'] = x_get_jaeger_trace__mutmut_14 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_15'] = x_get_jaeger_trace__mutmut_15 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_16'] = x_get_jaeger_trace__mutmut_16 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_17'] = x_get_jaeger_trace__mutmut_17 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_18'] = x_get_jaeger_trace__mutmut_18 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_19'] = x_get_jaeger_trace__mutmut_19 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_20'] = x_get_jaeger_trace__mutmut_20 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_21'] = x_get_jaeger_trace__mutmut_21 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_22'] = x_get_jaeger_trace__mutmut_22 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_23'] = x_get_jaeger_trace__mutmut_23 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_24'] = x_get_jaeger_trace__mutmut_24 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_25'] = x_get_jaeger_trace__mutmut_25 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_26'] = x_get_jaeger_trace__mutmut_26 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_27'] = x_get_jaeger_trace__mutmut_27 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_28'] = x_get_jaeger_trace__mutmut_28 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_29'] = x_get_jaeger_trace__mutmut_29 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_30'] = x_get_jaeger_trace__mutmut_30 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_31'] = x_get_jaeger_trace__mutmut_31 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_32'] = x_get_jaeger_trace__mutmut_32 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_33'] = x_get_jaeger_trace__mutmut_33 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_34'] = x_get_jaeger_trace__mutmut_34 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_35'] = x_get_jaeger_trace__mutmut_35 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_36'] = x_get_jaeger_trace__mutmut_36 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_37'] = x_get_jaeger_trace__mutmut_37 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_38'] = x_get_jaeger_trace__mutmut_38 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_39'] = x_get_jaeger_trace__mutmut_39 # type: ignore # mutmut generated
mutants_x_get_jaeger_trace__mutmut['x_get_jaeger_trace__mutmut_40'] = x_get_jaeger_trace__mutmut_40 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_jaeger_dependencies__mutmut)
def get_jaeger_dependencies(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_orig(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_1(end_ts: int, lookback: int = 3600001) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_2(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = None
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_3(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        None,
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_4(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params=None,
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_5(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_6(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_7(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "XX/api/dependenciesXX",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_8(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/API/DEPENDENCIES",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_9(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"XXendTsXX": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_10(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endts": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_11(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"ENDTS": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_12(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "XXlookbackXX": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_13(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "LOOKBACK": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_14(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = None
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_15(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get(None)
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_16(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("XXdataXX")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_17(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("DATA")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_18(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = None
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_19(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    None
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_20(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "XXparentXX": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_21(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "PARENT": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_22(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(None),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_23(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get(None, "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_24(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", None)),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_25(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_26(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", )),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_27(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("XXparentXX", "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_28(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("PARENT", "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_29(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "XXXX")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_30(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "XXchildXX": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_31(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "CHILD": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_32(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(None),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_33(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get(None, "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_34(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", None)),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_35(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_36(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", )),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_37(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("XXchildXX", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_38(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("CHILD", "")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_39(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", "XXXX")),
                        "callCount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_40(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "XXcallCountXX": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_41(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "callcount": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_42(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "CALLCOUNT": int(d.get("callCount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_43(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(None),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_44(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get(None, 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_45(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", None)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_46(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get(0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_47(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", )),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_48(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("XXcallCountXX", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_49(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callcount", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_50(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("CALLCOUNT", 0)),
                    }
                )
        return deps
    return []


def x_get_jaeger_dependencies__mutmut_51(end_ts: int, lookback: int = 3600000) -> list[JaegerDependencyDict]:
    result = _jaeger_get(
        "/api/dependencies",
        params={"endTs": end_ts, "lookback": lookback},
    )
    data = result.get("data")
    if isinstance(data, list):
        deps: list[JaegerDependencyDict] = []
        for d in data:
            if isinstance(d, dict):
                deps.append(
                    {
                        "parent": str(d.get("parent", "")),
                        "child": str(d.get("child", "")),
                        "callCount": int(d.get("callCount", 1)),
                    }
                )
        return deps
    return []

mutants_x_get_jaeger_dependencies__mutmut['_mutmut_orig'] = x_get_jaeger_dependencies__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_1'] = x_get_jaeger_dependencies__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_2'] = x_get_jaeger_dependencies__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_3'] = x_get_jaeger_dependencies__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_4'] = x_get_jaeger_dependencies__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_5'] = x_get_jaeger_dependencies__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_6'] = x_get_jaeger_dependencies__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_7'] = x_get_jaeger_dependencies__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_8'] = x_get_jaeger_dependencies__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_9'] = x_get_jaeger_dependencies__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_10'] = x_get_jaeger_dependencies__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_11'] = x_get_jaeger_dependencies__mutmut_11 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_12'] = x_get_jaeger_dependencies__mutmut_12 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_13'] = x_get_jaeger_dependencies__mutmut_13 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_14'] = x_get_jaeger_dependencies__mutmut_14 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_15'] = x_get_jaeger_dependencies__mutmut_15 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_16'] = x_get_jaeger_dependencies__mutmut_16 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_17'] = x_get_jaeger_dependencies__mutmut_17 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_18'] = x_get_jaeger_dependencies__mutmut_18 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_19'] = x_get_jaeger_dependencies__mutmut_19 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_20'] = x_get_jaeger_dependencies__mutmut_20 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_21'] = x_get_jaeger_dependencies__mutmut_21 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_22'] = x_get_jaeger_dependencies__mutmut_22 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_23'] = x_get_jaeger_dependencies__mutmut_23 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_24'] = x_get_jaeger_dependencies__mutmut_24 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_25'] = x_get_jaeger_dependencies__mutmut_25 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_26'] = x_get_jaeger_dependencies__mutmut_26 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_27'] = x_get_jaeger_dependencies__mutmut_27 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_28'] = x_get_jaeger_dependencies__mutmut_28 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_29'] = x_get_jaeger_dependencies__mutmut_29 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_30'] = x_get_jaeger_dependencies__mutmut_30 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_31'] = x_get_jaeger_dependencies__mutmut_31 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_32'] = x_get_jaeger_dependencies__mutmut_32 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_33'] = x_get_jaeger_dependencies__mutmut_33 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_34'] = x_get_jaeger_dependencies__mutmut_34 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_35'] = x_get_jaeger_dependencies__mutmut_35 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_36'] = x_get_jaeger_dependencies__mutmut_36 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_37'] = x_get_jaeger_dependencies__mutmut_37 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_38'] = x_get_jaeger_dependencies__mutmut_38 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_39'] = x_get_jaeger_dependencies__mutmut_39 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_40'] = x_get_jaeger_dependencies__mutmut_40 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_41'] = x_get_jaeger_dependencies__mutmut_41 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_42'] = x_get_jaeger_dependencies__mutmut_42 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_43'] = x_get_jaeger_dependencies__mutmut_43 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_44'] = x_get_jaeger_dependencies__mutmut_44 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_45'] = x_get_jaeger_dependencies__mutmut_45 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_46'] = x_get_jaeger_dependencies__mutmut_46 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_47'] = x_get_jaeger_dependencies__mutmut_47 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_48'] = x_get_jaeger_dependencies__mutmut_48 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_49'] = x_get_jaeger_dependencies__mutmut_49 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_50'] = x_get_jaeger_dependencies__mutmut_50 # type: ignore # mutmut generated
mutants_x_get_jaeger_dependencies__mutmut['x_get_jaeger_dependencies__mutmut_51'] = x_get_jaeger_dependencies__mutmut_51 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_query_prometheus_instant__mutmut)
def query_prometheus_instant(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_orig(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_1(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = None
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_2(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(None, time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_3(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, None)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_4(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_5(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, )
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_6(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = None
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_7(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get(None, {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_8(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", None)
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_9(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get({})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_10(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", )
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_11(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("XXdataXX", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_12(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("DATA", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_13(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = None
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_14(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get(None, []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_15(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", None) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_16(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get([]) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_17(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", ) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_18(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("XXresultXX", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_19(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("RESULT", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_20(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = None
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_21(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = None
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_22(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get(None, {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_23(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", None)
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_24(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get({})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_25(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", )
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_26(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("XXmetricXX", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_27(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("METRIC", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_28(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = None
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_29(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(None): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_30(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(None) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_31(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    None
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_32(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "XXnameXX": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_33(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "NAME": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_34(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(None),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_35(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get(None, "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_36(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", None)),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_37(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_38(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", )),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_39(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("XX__name__XX", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_40(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__NAME__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_41(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "XXXX")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_42(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "XXvalueXX": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_43(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "VALUE": _parse_prometheus_value(r.get("value")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_44(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(None),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_45(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get(None)),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_46(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("XXvalueXX")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_47(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("VALUE")),
                        "labels": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_48(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "XXlabelsXX": metric_labels,
                    }
                )
        return metrics
    return []


def x_query_prometheus_instant__mutmut_49(query: str, time: str | None = None) -> list[PrometheusMetricDict]:
    result = _prometheus_query(query, time)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        metrics: list[PrometheusMetricDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                metric_labels: dict[str, str] = (
                    {str(k): str(v) for k, v in metric.items()} if isinstance(metric, dict) else {}
                )
                metrics.append(
                    {
                        "name": str(metric.get("__name__", "")),
                        "value": _parse_prometheus_value(r.get("value")),
                        "LABELS": metric_labels,
                    }
                )
        return metrics
    return []

mutants_x_query_prometheus_instant__mutmut['_mutmut_orig'] = x_query_prometheus_instant__mutmut_orig # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_1'] = x_query_prometheus_instant__mutmut_1 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_2'] = x_query_prometheus_instant__mutmut_2 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_3'] = x_query_prometheus_instant__mutmut_3 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_4'] = x_query_prometheus_instant__mutmut_4 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_5'] = x_query_prometheus_instant__mutmut_5 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_6'] = x_query_prometheus_instant__mutmut_6 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_7'] = x_query_prometheus_instant__mutmut_7 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_8'] = x_query_prometheus_instant__mutmut_8 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_9'] = x_query_prometheus_instant__mutmut_9 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_10'] = x_query_prometheus_instant__mutmut_10 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_11'] = x_query_prometheus_instant__mutmut_11 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_12'] = x_query_prometheus_instant__mutmut_12 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_13'] = x_query_prometheus_instant__mutmut_13 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_14'] = x_query_prometheus_instant__mutmut_14 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_15'] = x_query_prometheus_instant__mutmut_15 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_16'] = x_query_prometheus_instant__mutmut_16 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_17'] = x_query_prometheus_instant__mutmut_17 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_18'] = x_query_prometheus_instant__mutmut_18 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_19'] = x_query_prometheus_instant__mutmut_19 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_20'] = x_query_prometheus_instant__mutmut_20 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_21'] = x_query_prometheus_instant__mutmut_21 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_22'] = x_query_prometheus_instant__mutmut_22 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_23'] = x_query_prometheus_instant__mutmut_23 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_24'] = x_query_prometheus_instant__mutmut_24 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_25'] = x_query_prometheus_instant__mutmut_25 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_26'] = x_query_prometheus_instant__mutmut_26 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_27'] = x_query_prometheus_instant__mutmut_27 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_28'] = x_query_prometheus_instant__mutmut_28 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_29'] = x_query_prometheus_instant__mutmut_29 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_30'] = x_query_prometheus_instant__mutmut_30 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_31'] = x_query_prometheus_instant__mutmut_31 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_32'] = x_query_prometheus_instant__mutmut_32 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_33'] = x_query_prometheus_instant__mutmut_33 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_34'] = x_query_prometheus_instant__mutmut_34 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_35'] = x_query_prometheus_instant__mutmut_35 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_36'] = x_query_prometheus_instant__mutmut_36 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_37'] = x_query_prometheus_instant__mutmut_37 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_38'] = x_query_prometheus_instant__mutmut_38 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_39'] = x_query_prometheus_instant__mutmut_39 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_40'] = x_query_prometheus_instant__mutmut_40 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_41'] = x_query_prometheus_instant__mutmut_41 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_42'] = x_query_prometheus_instant__mutmut_42 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_43'] = x_query_prometheus_instant__mutmut_43 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_44'] = x_query_prometheus_instant__mutmut_44 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_45'] = x_query_prometheus_instant__mutmut_45 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_46'] = x_query_prometheus_instant__mutmut_46 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_47'] = x_query_prometheus_instant__mutmut_47 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_48'] = x_query_prometheus_instant__mutmut_48 # type: ignore # mutmut generated
mutants_x_query_prometheus_instant__mutmut['x_query_prometheus_instant__mutmut_49'] = x_query_prometheus_instant__mutmut_49 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_query_prometheus_range__mutmut)
def query_prometheus_range(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_orig(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_1(
    query: str, start: str, end: str, step: str = "XX60sXX"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_2(
    query: str, start: str, end: str, step: str = "60S"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_3(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = None
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_4(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(None, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_5(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, None, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_6(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, None, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_7(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, None)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_8(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_9(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_10(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_11(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, )
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_12(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = None
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_13(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get(None, {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_14(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", None)
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_15(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get({})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_16(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", )
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_17(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("XXdataXX", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_18(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("DATA", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_19(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = None
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_20(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get(None, []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_21(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", None) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_22(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get([]) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_23(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", ) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_24(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("XXresultXX", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_25(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("RESULT", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_26(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = None
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_27(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = None
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_28(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get(None, {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_29(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", None)
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_30(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get({})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_31(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", )
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_32(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("XXmetricXX", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_33(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("METRIC", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_34(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = None
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_35(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get(None, [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_36(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", None)
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_37(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get([])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_38(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", )
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_39(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("XXvaluesXX", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_40(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("VALUES", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_41(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = None
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_42(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) or len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_43(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) != 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_44(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 3:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_45(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append(None)
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_46(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(None), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_47(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[1]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_48(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(None)))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_49(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[2])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_50(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    None
                )
        return out
    return []


def x_query_prometheus_range__mutmut_51(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "XXmetricXX": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_52(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "METRIC": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_53(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(None): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_54(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(None) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "values": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_55(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "XXvaluesXX": values,
                    }
                )
        return out
    return []


def x_query_prometheus_range__mutmut_56(
    query: str, start: str, end: str, step: str = "60s"
) -> list[PrometheusResultDict]:
    result = _prometheus_query_range(query, start, end, step)
    data = result.get("data", {})
    results = data.get("result", []) if isinstance(data, dict) else []
    if isinstance(results, list):
        out: list[PrometheusResultDict] = []
        for r in results:
            if isinstance(r, dict):
                metric = r.get("metric", {})
                values_raw = r.get("values", [])
                values: list[tuple[float, str]] = []
                if isinstance(values_raw, list):
                    for v in values_raw:
                        if isinstance(v, list) and len(v) == 2:  # noqa: PLR2004
                            values.append((float(v[0]), str(v[1])))
                out.append(
                    {
                        "metric": (
                            {str(k): str(v) for k, v in metric.items()}
                            if isinstance(metric, dict)
                            else {}
                        ),
                        "VALUES": values,
                    }
                )
        return out
    return []

mutants_x_query_prometheus_range__mutmut['_mutmut_orig'] = x_query_prometheus_range__mutmut_orig # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_1'] = x_query_prometheus_range__mutmut_1 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_2'] = x_query_prometheus_range__mutmut_2 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_3'] = x_query_prometheus_range__mutmut_3 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_4'] = x_query_prometheus_range__mutmut_4 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_5'] = x_query_prometheus_range__mutmut_5 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_6'] = x_query_prometheus_range__mutmut_6 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_7'] = x_query_prometheus_range__mutmut_7 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_8'] = x_query_prometheus_range__mutmut_8 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_9'] = x_query_prometheus_range__mutmut_9 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_10'] = x_query_prometheus_range__mutmut_10 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_11'] = x_query_prometheus_range__mutmut_11 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_12'] = x_query_prometheus_range__mutmut_12 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_13'] = x_query_prometheus_range__mutmut_13 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_14'] = x_query_prometheus_range__mutmut_14 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_15'] = x_query_prometheus_range__mutmut_15 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_16'] = x_query_prometheus_range__mutmut_16 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_17'] = x_query_prometheus_range__mutmut_17 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_18'] = x_query_prometheus_range__mutmut_18 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_19'] = x_query_prometheus_range__mutmut_19 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_20'] = x_query_prometheus_range__mutmut_20 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_21'] = x_query_prometheus_range__mutmut_21 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_22'] = x_query_prometheus_range__mutmut_22 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_23'] = x_query_prometheus_range__mutmut_23 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_24'] = x_query_prometheus_range__mutmut_24 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_25'] = x_query_prometheus_range__mutmut_25 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_26'] = x_query_prometheus_range__mutmut_26 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_27'] = x_query_prometheus_range__mutmut_27 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_28'] = x_query_prometheus_range__mutmut_28 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_29'] = x_query_prometheus_range__mutmut_29 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_30'] = x_query_prometheus_range__mutmut_30 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_31'] = x_query_prometheus_range__mutmut_31 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_32'] = x_query_prometheus_range__mutmut_32 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_33'] = x_query_prometheus_range__mutmut_33 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_34'] = x_query_prometheus_range__mutmut_34 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_35'] = x_query_prometheus_range__mutmut_35 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_36'] = x_query_prometheus_range__mutmut_36 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_37'] = x_query_prometheus_range__mutmut_37 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_38'] = x_query_prometheus_range__mutmut_38 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_39'] = x_query_prometheus_range__mutmut_39 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_40'] = x_query_prometheus_range__mutmut_40 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_41'] = x_query_prometheus_range__mutmut_41 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_42'] = x_query_prometheus_range__mutmut_42 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_43'] = x_query_prometheus_range__mutmut_43 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_44'] = x_query_prometheus_range__mutmut_44 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_45'] = x_query_prometheus_range__mutmut_45 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_46'] = x_query_prometheus_range__mutmut_46 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_47'] = x_query_prometheus_range__mutmut_47 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_48'] = x_query_prometheus_range__mutmut_48 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_49'] = x_query_prometheus_range__mutmut_49 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_50'] = x_query_prometheus_range__mutmut_50 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_51'] = x_query_prometheus_range__mutmut_51 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_52'] = x_query_prometheus_range__mutmut_52 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_53'] = x_query_prometheus_range__mutmut_53 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_54'] = x_query_prometheus_range__mutmut_54 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_55'] = x_query_prometheus_range__mutmut_55 # type: ignore # mutmut generated
mutants_x_query_prometheus_range__mutmut['x_query_prometheus_range__mutmut_56'] = x_query_prometheus_range__mutmut_56 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse_spans__mutmut)
def _parse_spans(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_orig(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_1(spans_raw: object) -> list[JaegerSpanDict]:
    if isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_2(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = None
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_3(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = None
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_4(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "XXtraceIDXX": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_5(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceid": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_6(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "TRACEID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_7(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(None),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_8(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get(None, "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_9(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", None)),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_10(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_11(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", )),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_12(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("XXtraceIDXX", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_13(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceid", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_14(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("TRACEID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_15(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "XXXX")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_16(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "XXspanIDXX": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_17(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanid": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_18(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "SPANID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_19(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(None),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_20(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get(None, "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_21(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", None)),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_22(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_23(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", )),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_24(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("XXspanIDXX", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_25(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanid", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_26(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("SPANID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_27(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "XXXX")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_28(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "XXoperationNameXX": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_29(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationname": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_30(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "OPERATIONNAME": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_31(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(None),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_32(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get(None, "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_33(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", None)),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_34(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_35(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", )),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_36(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("XXoperationNameXX", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_37(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationname", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_38(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("OPERATIONNAME", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_39(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "XXXX")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_40(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "XXdurationXX": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_41(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "DURATION": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_42(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(None),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_43(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get(None, 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_44(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", None)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_45(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get(0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_46(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", )),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_47(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("XXdurationXX", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_48(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("DURATION", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_49(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 1)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_50(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "XXstartTimeXX": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_51(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "starttime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_52(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "STARTTIME": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_53(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(None),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_54(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get(None, 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_55(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", None)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_56(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get(0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_57(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", )),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_58(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("XXstartTimeXX", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_59(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("starttime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_60(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("STARTTIME", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_61(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 1)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_62(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = None
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_63(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get(None)
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_64(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("XXtagsXX")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_65(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("TAGS")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_66(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = None
            spans.append(span)
    return spans


def x__parse_spans__mutmut_67(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["XXtagsXX"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_68(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["TAGS"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_69(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"XXkeyXX": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_70(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"KEY": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_71(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(None), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_72(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get(None, "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_73(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", None)), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_74(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_75(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", )), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_76(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("XXkeyXX", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_77(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("KEY", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_78(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "XXXX")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_79(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "XXvalueXX": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_80(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "VALUE": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_81(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get(None, "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_82(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", None)}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_83(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_84(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", )}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_85(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("XXvalueXX", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_86(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("VALUE", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_87(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "XXXX")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_88(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"XXkeyXX": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_89(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"KEY": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_90(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "XXXX", "value": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_91(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "XXvalueXX": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_92(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "VALUE": t}
                    )
                    for t in tags
                ]
            spans.append(span)
    return spans


def x__parse_spans__mutmut_93(spans_raw: object) -> list[JaegerSpanDict]:
    if not isinstance(spans_raw, list):
        return []
    spans: list[JaegerSpanDict] = []
    for s in spans_raw:
        if isinstance(s, dict):
            span: JaegerSpanDict = {
                "traceID": str(s.get("traceID", "")),
                "spanID": str(s.get("spanID", "")),
                "operationName": str(s.get("operationName", "")),
                "duration": int(s.get("duration", 0)),
                "startTime": int(s.get("startTime", 0)),
            }
            tags = s.get("tags")
            if isinstance(tags, list):
                span["tags"] = [
                    (
                        {"key": str(t.get("key", "")), "value": t.get("value", "")}
                        if isinstance(t, dict)
                        else {"key": "", "value": t}
                    )
                    for t in tags
                ]
            spans.append(None)
    return spans

mutants_x__parse_spans__mutmut['_mutmut_orig'] = x__parse_spans__mutmut_orig # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_1'] = x__parse_spans__mutmut_1 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_2'] = x__parse_spans__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_3'] = x__parse_spans__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_4'] = x__parse_spans__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_5'] = x__parse_spans__mutmut_5 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_6'] = x__parse_spans__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_7'] = x__parse_spans__mutmut_7 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_8'] = x__parse_spans__mutmut_8 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_9'] = x__parse_spans__mutmut_9 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_10'] = x__parse_spans__mutmut_10 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_11'] = x__parse_spans__mutmut_11 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_12'] = x__parse_spans__mutmut_12 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_13'] = x__parse_spans__mutmut_13 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_14'] = x__parse_spans__mutmut_14 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_15'] = x__parse_spans__mutmut_15 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_16'] = x__parse_spans__mutmut_16 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_17'] = x__parse_spans__mutmut_17 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_18'] = x__parse_spans__mutmut_18 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_19'] = x__parse_spans__mutmut_19 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_20'] = x__parse_spans__mutmut_20 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_21'] = x__parse_spans__mutmut_21 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_22'] = x__parse_spans__mutmut_22 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_23'] = x__parse_spans__mutmut_23 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_24'] = x__parse_spans__mutmut_24 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_25'] = x__parse_spans__mutmut_25 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_26'] = x__parse_spans__mutmut_26 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_27'] = x__parse_spans__mutmut_27 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_28'] = x__parse_spans__mutmut_28 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_29'] = x__parse_spans__mutmut_29 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_30'] = x__parse_spans__mutmut_30 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_31'] = x__parse_spans__mutmut_31 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_32'] = x__parse_spans__mutmut_32 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_33'] = x__parse_spans__mutmut_33 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_34'] = x__parse_spans__mutmut_34 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_35'] = x__parse_spans__mutmut_35 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_36'] = x__parse_spans__mutmut_36 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_37'] = x__parse_spans__mutmut_37 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_38'] = x__parse_spans__mutmut_38 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_39'] = x__parse_spans__mutmut_39 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_40'] = x__parse_spans__mutmut_40 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_41'] = x__parse_spans__mutmut_41 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_42'] = x__parse_spans__mutmut_42 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_43'] = x__parse_spans__mutmut_43 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_44'] = x__parse_spans__mutmut_44 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_45'] = x__parse_spans__mutmut_45 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_46'] = x__parse_spans__mutmut_46 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_47'] = x__parse_spans__mutmut_47 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_48'] = x__parse_spans__mutmut_48 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_49'] = x__parse_spans__mutmut_49 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_50'] = x__parse_spans__mutmut_50 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_51'] = x__parse_spans__mutmut_51 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_52'] = x__parse_spans__mutmut_52 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_53'] = x__parse_spans__mutmut_53 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_54'] = x__parse_spans__mutmut_54 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_55'] = x__parse_spans__mutmut_55 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_56'] = x__parse_spans__mutmut_56 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_57'] = x__parse_spans__mutmut_57 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_58'] = x__parse_spans__mutmut_58 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_59'] = x__parse_spans__mutmut_59 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_60'] = x__parse_spans__mutmut_60 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_61'] = x__parse_spans__mutmut_61 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_62'] = x__parse_spans__mutmut_62 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_63'] = x__parse_spans__mutmut_63 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_64'] = x__parse_spans__mutmut_64 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_65'] = x__parse_spans__mutmut_65 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_66'] = x__parse_spans__mutmut_66 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_67'] = x__parse_spans__mutmut_67 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_68'] = x__parse_spans__mutmut_68 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_69'] = x__parse_spans__mutmut_69 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_70'] = x__parse_spans__mutmut_70 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_71'] = x__parse_spans__mutmut_71 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_72'] = x__parse_spans__mutmut_72 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_73'] = x__parse_spans__mutmut_73 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_74'] = x__parse_spans__mutmut_74 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_75'] = x__parse_spans__mutmut_75 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_76'] = x__parse_spans__mutmut_76 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_77'] = x__parse_spans__mutmut_77 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_78'] = x__parse_spans__mutmut_78 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_79'] = x__parse_spans__mutmut_79 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_80'] = x__parse_spans__mutmut_80 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_81'] = x__parse_spans__mutmut_81 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_82'] = x__parse_spans__mutmut_82 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_83'] = x__parse_spans__mutmut_83 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_84'] = x__parse_spans__mutmut_84 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_85'] = x__parse_spans__mutmut_85 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_86'] = x__parse_spans__mutmut_86 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_87'] = x__parse_spans__mutmut_87 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_88'] = x__parse_spans__mutmut_88 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_89'] = x__parse_spans__mutmut_89 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_90'] = x__parse_spans__mutmut_90 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_91'] = x__parse_spans__mutmut_91 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_92'] = x__parse_spans__mutmut_92 # type: ignore # mutmut generated
mutants_x__parse_spans__mutmut['x__parse_spans__mutmut_93'] = x__parse_spans__mutmut_93 # type: ignore # mutmut generated
mutants_x__parse_prometheus_value__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__parse_prometheus_value__mutmut)
def _parse_prometheus_value(value_raw: object) -> float:
    if isinstance(value_raw, list) and len(value_raw) >= 2:  # noqa: PLR2004
        try:
            return float(value_raw[1])
        except (ValueError, TypeError):
            return 0.0
    return 0.0


def x__parse_prometheus_value__mutmut_orig(value_raw: object) -> float:
    if isinstance(value_raw, list) and len(value_raw) >= 2:  # noqa: PLR2004
        try:
            return float(value_raw[1])
        except (ValueError, TypeError):
            return 0.0
    return 0.0


def x__parse_prometheus_value__mutmut_1(value_raw: object) -> float:
    if isinstance(value_raw, list) or len(value_raw) >= 2:  # noqa: PLR2004
        try:
            return float(value_raw[1])
        except (ValueError, TypeError):
            return 0.0
    return 0.0


def x__parse_prometheus_value__mutmut_2(value_raw: object) -> float:
    if isinstance(value_raw, list) and len(value_raw) > 2:  # noqa: PLR2004
        try:
            return float(value_raw[1])
        except (ValueError, TypeError):
            return 0.0
    return 0.0


def x__parse_prometheus_value__mutmut_3(value_raw: object) -> float:
    if isinstance(value_raw, list) and len(value_raw) >= 3:  # noqa: PLR2004
        try:
            return float(value_raw[1])
        except (ValueError, TypeError):
            return 0.0
    return 0.0


def x__parse_prometheus_value__mutmut_4(value_raw: object) -> float:
    if isinstance(value_raw, list) and len(value_raw) >= 2:  # noqa: PLR2004
        try:
            return float(None)
        except (ValueError, TypeError):
            return 0.0
    return 0.0


def x__parse_prometheus_value__mutmut_5(value_raw: object) -> float:
    if isinstance(value_raw, list) and len(value_raw) >= 2:  # noqa: PLR2004
        try:
            return float(value_raw[2])
        except (ValueError, TypeError):
            return 0.0
    return 0.0


def x__parse_prometheus_value__mutmut_6(value_raw: object) -> float:
    if isinstance(value_raw, list) and len(value_raw) >= 2:  # noqa: PLR2004
        try:
            return float(value_raw[1])
        except (ValueError, TypeError):
            return 1.0
    return 0.0


def x__parse_prometheus_value__mutmut_7(value_raw: object) -> float:
    if isinstance(value_raw, list) and len(value_raw) >= 2:  # noqa: PLR2004
        try:
            return float(value_raw[1])
        except (ValueError, TypeError):
            return 0.0
    return 1.0

mutants_x__parse_prometheus_value__mutmut['_mutmut_orig'] = x__parse_prometheus_value__mutmut_orig # type: ignore # mutmut generated
mutants_x__parse_prometheus_value__mutmut['x__parse_prometheus_value__mutmut_1'] = x__parse_prometheus_value__mutmut_1 # type: ignore # mutmut generated
mutants_x__parse_prometheus_value__mutmut['x__parse_prometheus_value__mutmut_2'] = x__parse_prometheus_value__mutmut_2 # type: ignore # mutmut generated
mutants_x__parse_prometheus_value__mutmut['x__parse_prometheus_value__mutmut_3'] = x__parse_prometheus_value__mutmut_3 # type: ignore # mutmut generated
mutants_x__parse_prometheus_value__mutmut['x__parse_prometheus_value__mutmut_4'] = x__parse_prometheus_value__mutmut_4 # type: ignore # mutmut generated
mutants_x__parse_prometheus_value__mutmut['x__parse_prometheus_value__mutmut_5'] = x__parse_prometheus_value__mutmut_5 # type: ignore # mutmut generated
mutants_x__parse_prometheus_value__mutmut['x__parse_prometheus_value__mutmut_6'] = x__parse_prometheus_value__mutmut_6 # type: ignore # mutmut generated
mutants_x__parse_prometheus_value__mutmut['x__parse_prometheus_value__mutmut_7'] = x__parse_prometheus_value__mutmut_7 # type: ignore # mutmut generated
