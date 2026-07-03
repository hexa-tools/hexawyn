from __future__ import annotations

from hexawyn.application.ports.driven.metrics_query_port import (
    PrometheusInstantSample,
    PrometheusRangeSample,
)
from hexawyn.domain.models.constants import MetricsQueryConstants
from hexawyn.domain.models.metrics_query import (
    PrometheusMetricResult,
    PrometheusQueryResult,
    QueryType,
    UnitHint,
)
from hexawyn.domain.services.metrics_query.unit_formatter import format_metric_value

_cfg = MetricsQueryConstants()


def parse_instant_results(
    raw: list[PrometheusInstantSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, "instant")

    truncated = len(raw) > _cfg.max_results
    items = raw[: _cfg.max_results]
    results = [
        PrometheusMetricResult(
            labels=item["metric"],
            value=item["value"],
            formatted_value=format_metric_value(item["value"], unit_hint),
        )
        for item in items
    ]
    return PrometheusQueryResult(
        query=promql,
        query_type="instant",
        results=results,
        result_count=len(results),
        truncated=truncated,
        summary=_summary(len(results), truncated),
    )


def parse_range_results(
    raw: list[PrometheusRangeSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, "range")

    truncated = len(raw) > _cfg.max_results
    items = raw[: _cfg.max_results]
    results = [
        PrometheusMetricResult(
            labels=item["metric"],
            values=item["values"],
            formatted_value=format_metric_value(item["values"][-1][1], unit_hint)
            if item["values"]
            else "",
        )
        for item in items
    ]
    return PrometheusQueryResult(
        query=promql,
        query_type="range",
        results=results,
        result_count=len(results),
        truncated=truncated,
        summary=_summary(len(results), truncated),
    )


def _no_data_result(promql: str, query_type: QueryType) -> PrometheusQueryResult:
    return PrometheusQueryResult(
        query=promql,
        query_type=query_type,
        no_data=True,
        summary=f"No data found for query '{promql}'",
    )


def _summary(result_count: int, truncated: bool) -> str:
    plural = "" if result_count == 1 else "s"
    summary = f"{result_count} result{plural}"
    if truncated:
        summary += " (truncated — more than the maximum result limit was returned)"
    return summary
