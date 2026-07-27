from __future__ import annotations

import os
from typing import TypedDict

import httpx

_JAEGER_QUERY_URL = os.environ.get("JAEGER_QUERY_URL", "http://localhost:16686")
_PROMETHEUS_URL = os.environ.get("PROMETHEUS_URL", "http://localhost:9090")
_REQUEST_TIMEOUT = 10.0


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


def list_jaeger_services() -> list[str]:
    result = _jaeger_get("/api/services")
    data = result.get("data")
    if isinstance(data, list):
        return [str(s) for s in data]
    return []


def list_jaeger_operations(service: str) -> list[str]:
    result = _jaeger_get(f"/api/services/{service}/operations")
    data = result.get("data")
    if isinstance(data, list):
        return [str(op) if isinstance(op, str) else str(op.get("name", "")) for op in data]
    return []


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


def _parse_prometheus_value(value_raw: object) -> float:
    if isinstance(value_raw, list) and len(value_raw) >= 2:  # noqa: PLR2004
        try:
            return float(value_raw[1])
        except (ValueError, TypeError):
            return 0.0
    return 0.0
