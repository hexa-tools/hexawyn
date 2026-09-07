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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_parse_instant_results__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_parse_instant_results__mutmut)
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


def x_parse_instant_results__mutmut_orig(
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


def x_parse_instant_results__mutmut_1(
    raw: list[PrometheusInstantSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if raw:
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


def x_parse_instant_results__mutmut_2(
    raw: list[PrometheusInstantSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(None, "instant")

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


def x_parse_instant_results__mutmut_3(
    raw: list[PrometheusInstantSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, None)

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


def x_parse_instant_results__mutmut_4(
    raw: list[PrometheusInstantSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result("instant")

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


def x_parse_instant_results__mutmut_5(
    raw: list[PrometheusInstantSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, )

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


def x_parse_instant_results__mutmut_6(
    raw: list[PrometheusInstantSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, "XXinstantXX")

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


def x_parse_instant_results__mutmut_7(
    raw: list[PrometheusInstantSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, "INSTANT")

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


def x_parse_instant_results__mutmut_8(
    raw: list[PrometheusInstantSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, "instant")

    truncated = None
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


def x_parse_instant_results__mutmut_9(
    raw: list[PrometheusInstantSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, "instant")

    truncated = len(raw) >= _cfg.max_results
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


def x_parse_instant_results__mutmut_10(
    raw: list[PrometheusInstantSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, "instant")

    truncated = len(raw) > _cfg.max_results
    items = None
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


def x_parse_instant_results__mutmut_11(
    raw: list[PrometheusInstantSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, "instant")

    truncated = len(raw) > _cfg.max_results
    items = raw[: _cfg.max_results]
    results = None
    return PrometheusQueryResult(
        query=promql,
        query_type="instant",
        results=results,
        result_count=len(results),
        truncated=truncated,
        summary=_summary(len(results), truncated),
    )


def x_parse_instant_results__mutmut_12(
    raw: list[PrometheusInstantSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, "instant")

    truncated = len(raw) > _cfg.max_results
    items = raw[: _cfg.max_results]
    results = [
        PrometheusMetricResult(
            labels=None,
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


def x_parse_instant_results__mutmut_13(
    raw: list[PrometheusInstantSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, "instant")

    truncated = len(raw) > _cfg.max_results
    items = raw[: _cfg.max_results]
    results = [
        PrometheusMetricResult(
            labels=item["metric"],
            value=None,
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


def x_parse_instant_results__mutmut_14(
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
            formatted_value=None,
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


def x_parse_instant_results__mutmut_15(
    raw: list[PrometheusInstantSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, "instant")

    truncated = len(raw) > _cfg.max_results
    items = raw[: _cfg.max_results]
    results = [
        PrometheusMetricResult(
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


def x_parse_instant_results__mutmut_16(
    raw: list[PrometheusInstantSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, "instant")

    truncated = len(raw) > _cfg.max_results
    items = raw[: _cfg.max_results]
    results = [
        PrometheusMetricResult(
            labels=item["metric"],
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


def x_parse_instant_results__mutmut_17(
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


def x_parse_instant_results__mutmut_18(
    raw: list[PrometheusInstantSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, "instant")

    truncated = len(raw) > _cfg.max_results
    items = raw[: _cfg.max_results]
    results = [
        PrometheusMetricResult(
            labels=item["XXmetricXX"],
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


def x_parse_instant_results__mutmut_19(
    raw: list[PrometheusInstantSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, "instant")

    truncated = len(raw) > _cfg.max_results
    items = raw[: _cfg.max_results]
    results = [
        PrometheusMetricResult(
            labels=item["METRIC"],
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


def x_parse_instant_results__mutmut_20(
    raw: list[PrometheusInstantSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, "instant")

    truncated = len(raw) > _cfg.max_results
    items = raw[: _cfg.max_results]
    results = [
        PrometheusMetricResult(
            labels=item["metric"],
            value=item["XXvalueXX"],
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


def x_parse_instant_results__mutmut_21(
    raw: list[PrometheusInstantSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, "instant")

    truncated = len(raw) > _cfg.max_results
    items = raw[: _cfg.max_results]
    results = [
        PrometheusMetricResult(
            labels=item["metric"],
            value=item["VALUE"],
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


def x_parse_instant_results__mutmut_22(
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
            formatted_value=format_metric_value(None, unit_hint),
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


def x_parse_instant_results__mutmut_23(
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
            formatted_value=format_metric_value(item["value"], None),
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


def x_parse_instant_results__mutmut_24(
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
            formatted_value=format_metric_value(unit_hint),
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


def x_parse_instant_results__mutmut_25(
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
            formatted_value=format_metric_value(item["value"], ),
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


def x_parse_instant_results__mutmut_26(
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
            formatted_value=format_metric_value(item["XXvalueXX"], unit_hint),
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


def x_parse_instant_results__mutmut_27(
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
            formatted_value=format_metric_value(item["VALUE"], unit_hint),
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


def x_parse_instant_results__mutmut_28(
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
        query=None,
        query_type="instant",
        results=results,
        result_count=len(results),
        truncated=truncated,
        summary=_summary(len(results), truncated),
    )


def x_parse_instant_results__mutmut_29(
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
        query_type=None,
        results=results,
        result_count=len(results),
        truncated=truncated,
        summary=_summary(len(results), truncated),
    )


def x_parse_instant_results__mutmut_30(
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
        results=None,
        result_count=len(results),
        truncated=truncated,
        summary=_summary(len(results), truncated),
    )


def x_parse_instant_results__mutmut_31(
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
        result_count=None,
        truncated=truncated,
        summary=_summary(len(results), truncated),
    )


def x_parse_instant_results__mutmut_32(
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
        truncated=None,
        summary=_summary(len(results), truncated),
    )


def x_parse_instant_results__mutmut_33(
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
        summary=None,
    )


def x_parse_instant_results__mutmut_34(
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
        query_type="instant",
        results=results,
        result_count=len(results),
        truncated=truncated,
        summary=_summary(len(results), truncated),
    )


def x_parse_instant_results__mutmut_35(
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
        results=results,
        result_count=len(results),
        truncated=truncated,
        summary=_summary(len(results), truncated),
    )


def x_parse_instant_results__mutmut_36(
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
        result_count=len(results),
        truncated=truncated,
        summary=_summary(len(results), truncated),
    )


def x_parse_instant_results__mutmut_37(
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
        truncated=truncated,
        summary=_summary(len(results), truncated),
    )


def x_parse_instant_results__mutmut_38(
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
        summary=_summary(len(results), truncated),
    )


def x_parse_instant_results__mutmut_39(
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
        )


def x_parse_instant_results__mutmut_40(
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
        query_type="XXinstantXX",
        results=results,
        result_count=len(results),
        truncated=truncated,
        summary=_summary(len(results), truncated),
    )


def x_parse_instant_results__mutmut_41(
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
        query_type="INSTANT",
        results=results,
        result_count=len(results),
        truncated=truncated,
        summary=_summary(len(results), truncated),
    )


def x_parse_instant_results__mutmut_42(
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
        summary=_summary(None, truncated),
    )


def x_parse_instant_results__mutmut_43(
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
        summary=_summary(len(results), None),
    )


def x_parse_instant_results__mutmut_44(
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
        summary=_summary(truncated),
    )


def x_parse_instant_results__mutmut_45(
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
        summary=_summary(len(results), ),
    )

mutants_x_parse_instant_results__mutmut['_mutmut_orig'] = x_parse_instant_results__mutmut_orig # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_1'] = x_parse_instant_results__mutmut_1 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_2'] = x_parse_instant_results__mutmut_2 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_3'] = x_parse_instant_results__mutmut_3 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_4'] = x_parse_instant_results__mutmut_4 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_5'] = x_parse_instant_results__mutmut_5 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_6'] = x_parse_instant_results__mutmut_6 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_7'] = x_parse_instant_results__mutmut_7 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_8'] = x_parse_instant_results__mutmut_8 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_9'] = x_parse_instant_results__mutmut_9 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_10'] = x_parse_instant_results__mutmut_10 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_11'] = x_parse_instant_results__mutmut_11 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_12'] = x_parse_instant_results__mutmut_12 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_13'] = x_parse_instant_results__mutmut_13 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_14'] = x_parse_instant_results__mutmut_14 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_15'] = x_parse_instant_results__mutmut_15 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_16'] = x_parse_instant_results__mutmut_16 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_17'] = x_parse_instant_results__mutmut_17 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_18'] = x_parse_instant_results__mutmut_18 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_19'] = x_parse_instant_results__mutmut_19 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_20'] = x_parse_instant_results__mutmut_20 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_21'] = x_parse_instant_results__mutmut_21 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_22'] = x_parse_instant_results__mutmut_22 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_23'] = x_parse_instant_results__mutmut_23 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_24'] = x_parse_instant_results__mutmut_24 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_25'] = x_parse_instant_results__mutmut_25 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_26'] = x_parse_instant_results__mutmut_26 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_27'] = x_parse_instant_results__mutmut_27 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_28'] = x_parse_instant_results__mutmut_28 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_29'] = x_parse_instant_results__mutmut_29 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_30'] = x_parse_instant_results__mutmut_30 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_31'] = x_parse_instant_results__mutmut_31 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_32'] = x_parse_instant_results__mutmut_32 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_33'] = x_parse_instant_results__mutmut_33 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_34'] = x_parse_instant_results__mutmut_34 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_35'] = x_parse_instant_results__mutmut_35 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_36'] = x_parse_instant_results__mutmut_36 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_37'] = x_parse_instant_results__mutmut_37 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_38'] = x_parse_instant_results__mutmut_38 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_39'] = x_parse_instant_results__mutmut_39 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_40'] = x_parse_instant_results__mutmut_40 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_41'] = x_parse_instant_results__mutmut_41 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_42'] = x_parse_instant_results__mutmut_42 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_43'] = x_parse_instant_results__mutmut_43 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_44'] = x_parse_instant_results__mutmut_44 # type: ignore # mutmut generated
mutants_x_parse_instant_results__mutmut['x_parse_instant_results__mutmut_45'] = x_parse_instant_results__mutmut_45 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_parse_range_results__mutmut)
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


def x_parse_range_results__mutmut_orig(
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


def x_parse_range_results__mutmut_1(
    raw: list[PrometheusRangeSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if raw:
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


def x_parse_range_results__mutmut_2(
    raw: list[PrometheusRangeSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(None, "range")

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


def x_parse_range_results__mutmut_3(
    raw: list[PrometheusRangeSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, None)

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


def x_parse_range_results__mutmut_4(
    raw: list[PrometheusRangeSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result("range")

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


def x_parse_range_results__mutmut_5(
    raw: list[PrometheusRangeSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, )

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


def x_parse_range_results__mutmut_6(
    raw: list[PrometheusRangeSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, "XXrangeXX")

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


def x_parse_range_results__mutmut_7(
    raw: list[PrometheusRangeSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, "RANGE")

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


def x_parse_range_results__mutmut_8(
    raw: list[PrometheusRangeSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, "range")

    truncated = None
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


def x_parse_range_results__mutmut_9(
    raw: list[PrometheusRangeSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, "range")

    truncated = len(raw) >= _cfg.max_results
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


def x_parse_range_results__mutmut_10(
    raw: list[PrometheusRangeSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, "range")

    truncated = len(raw) > _cfg.max_results
    items = None
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


def x_parse_range_results__mutmut_11(
    raw: list[PrometheusRangeSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, "range")

    truncated = len(raw) > _cfg.max_results
    items = raw[: _cfg.max_results]
    results = None
    return PrometheusQueryResult(
        query=promql,
        query_type="range",
        results=results,
        result_count=len(results),
        truncated=truncated,
        summary=_summary(len(results), truncated),
    )


def x_parse_range_results__mutmut_12(
    raw: list[PrometheusRangeSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, "range")

    truncated = len(raw) > _cfg.max_results
    items = raw[: _cfg.max_results]
    results = [
        PrometheusMetricResult(
            labels=None,
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


def x_parse_range_results__mutmut_13(
    raw: list[PrometheusRangeSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, "range")

    truncated = len(raw) > _cfg.max_results
    items = raw[: _cfg.max_results]
    results = [
        PrometheusMetricResult(
            labels=item["metric"],
            values=None,
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


def x_parse_range_results__mutmut_14(
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
            formatted_value=None,
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


def x_parse_range_results__mutmut_15(
    raw: list[PrometheusRangeSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, "range")

    truncated = len(raw) > _cfg.max_results
    items = raw[: _cfg.max_results]
    results = [
        PrometheusMetricResult(
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


def x_parse_range_results__mutmut_16(
    raw: list[PrometheusRangeSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, "range")

    truncated = len(raw) > _cfg.max_results
    items = raw[: _cfg.max_results]
    results = [
        PrometheusMetricResult(
            labels=item["metric"],
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


def x_parse_range_results__mutmut_17(
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


def x_parse_range_results__mutmut_18(
    raw: list[PrometheusRangeSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, "range")

    truncated = len(raw) > _cfg.max_results
    items = raw[: _cfg.max_results]
    results = [
        PrometheusMetricResult(
            labels=item["XXmetricXX"],
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


def x_parse_range_results__mutmut_19(
    raw: list[PrometheusRangeSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, "range")

    truncated = len(raw) > _cfg.max_results
    items = raw[: _cfg.max_results]
    results = [
        PrometheusMetricResult(
            labels=item["METRIC"],
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


def x_parse_range_results__mutmut_20(
    raw: list[PrometheusRangeSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, "range")

    truncated = len(raw) > _cfg.max_results
    items = raw[: _cfg.max_results]
    results = [
        PrometheusMetricResult(
            labels=item["metric"],
            values=item["XXvaluesXX"],
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


def x_parse_range_results__mutmut_21(
    raw: list[PrometheusRangeSample], promql: str, unit_hint: UnitHint
) -> PrometheusQueryResult:
    if not raw:
        return _no_data_result(promql, "range")

    truncated = len(raw) > _cfg.max_results
    items = raw[: _cfg.max_results]
    results = [
        PrometheusMetricResult(
            labels=item["metric"],
            values=item["VALUES"],
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


def x_parse_range_results__mutmut_22(
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
            formatted_value=format_metric_value(None, unit_hint)
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


def x_parse_range_results__mutmut_23(
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
            formatted_value=format_metric_value(item["values"][-1][1], None)
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


def x_parse_range_results__mutmut_24(
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
            formatted_value=format_metric_value(unit_hint)
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


def x_parse_range_results__mutmut_25(
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
            formatted_value=format_metric_value(item["values"][-1][1], )
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


def x_parse_range_results__mutmut_26(
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
            formatted_value=format_metric_value(item["XXvaluesXX"][-1][1], unit_hint)
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


def x_parse_range_results__mutmut_27(
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
            formatted_value=format_metric_value(item["VALUES"][-1][1], unit_hint)
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


def x_parse_range_results__mutmut_28(
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
            formatted_value=format_metric_value(item["values"][+1][1], unit_hint)
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


def x_parse_range_results__mutmut_29(
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
            formatted_value=format_metric_value(item["values"][-2][1], unit_hint)
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


def x_parse_range_results__mutmut_30(
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
            formatted_value=format_metric_value(item["values"][-1][2], unit_hint)
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


def x_parse_range_results__mutmut_31(
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
            if item["XXvaluesXX"]
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


def x_parse_range_results__mutmut_32(
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
            if item["VALUES"]
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


def x_parse_range_results__mutmut_33(
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
            else "XXXX",
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


def x_parse_range_results__mutmut_34(
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
        query=None,
        query_type="range",
        results=results,
        result_count=len(results),
        truncated=truncated,
        summary=_summary(len(results), truncated),
    )


def x_parse_range_results__mutmut_35(
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
        query_type=None,
        results=results,
        result_count=len(results),
        truncated=truncated,
        summary=_summary(len(results), truncated),
    )


def x_parse_range_results__mutmut_36(
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
        results=None,
        result_count=len(results),
        truncated=truncated,
        summary=_summary(len(results), truncated),
    )


def x_parse_range_results__mutmut_37(
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
        result_count=None,
        truncated=truncated,
        summary=_summary(len(results), truncated),
    )


def x_parse_range_results__mutmut_38(
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
        truncated=None,
        summary=_summary(len(results), truncated),
    )


def x_parse_range_results__mutmut_39(
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
        summary=None,
    )


def x_parse_range_results__mutmut_40(
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
        query_type="range",
        results=results,
        result_count=len(results),
        truncated=truncated,
        summary=_summary(len(results), truncated),
    )


def x_parse_range_results__mutmut_41(
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
        results=results,
        result_count=len(results),
        truncated=truncated,
        summary=_summary(len(results), truncated),
    )


def x_parse_range_results__mutmut_42(
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
        result_count=len(results),
        truncated=truncated,
        summary=_summary(len(results), truncated),
    )


def x_parse_range_results__mutmut_43(
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
        truncated=truncated,
        summary=_summary(len(results), truncated),
    )


def x_parse_range_results__mutmut_44(
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
        summary=_summary(len(results), truncated),
    )


def x_parse_range_results__mutmut_45(
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
        )


def x_parse_range_results__mutmut_46(
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
        query_type="XXrangeXX",
        results=results,
        result_count=len(results),
        truncated=truncated,
        summary=_summary(len(results), truncated),
    )


def x_parse_range_results__mutmut_47(
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
        query_type="RANGE",
        results=results,
        result_count=len(results),
        truncated=truncated,
        summary=_summary(len(results), truncated),
    )


def x_parse_range_results__mutmut_48(
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
        summary=_summary(None, truncated),
    )


def x_parse_range_results__mutmut_49(
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
        summary=_summary(len(results), None),
    )


def x_parse_range_results__mutmut_50(
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
        summary=_summary(truncated),
    )


def x_parse_range_results__mutmut_51(
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
        summary=_summary(len(results), ),
    )

mutants_x_parse_range_results__mutmut['_mutmut_orig'] = x_parse_range_results__mutmut_orig # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_1'] = x_parse_range_results__mutmut_1 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_2'] = x_parse_range_results__mutmut_2 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_3'] = x_parse_range_results__mutmut_3 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_4'] = x_parse_range_results__mutmut_4 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_5'] = x_parse_range_results__mutmut_5 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_6'] = x_parse_range_results__mutmut_6 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_7'] = x_parse_range_results__mutmut_7 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_8'] = x_parse_range_results__mutmut_8 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_9'] = x_parse_range_results__mutmut_9 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_10'] = x_parse_range_results__mutmut_10 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_11'] = x_parse_range_results__mutmut_11 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_12'] = x_parse_range_results__mutmut_12 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_13'] = x_parse_range_results__mutmut_13 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_14'] = x_parse_range_results__mutmut_14 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_15'] = x_parse_range_results__mutmut_15 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_16'] = x_parse_range_results__mutmut_16 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_17'] = x_parse_range_results__mutmut_17 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_18'] = x_parse_range_results__mutmut_18 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_19'] = x_parse_range_results__mutmut_19 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_20'] = x_parse_range_results__mutmut_20 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_21'] = x_parse_range_results__mutmut_21 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_22'] = x_parse_range_results__mutmut_22 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_23'] = x_parse_range_results__mutmut_23 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_24'] = x_parse_range_results__mutmut_24 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_25'] = x_parse_range_results__mutmut_25 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_26'] = x_parse_range_results__mutmut_26 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_27'] = x_parse_range_results__mutmut_27 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_28'] = x_parse_range_results__mutmut_28 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_29'] = x_parse_range_results__mutmut_29 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_30'] = x_parse_range_results__mutmut_30 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_31'] = x_parse_range_results__mutmut_31 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_32'] = x_parse_range_results__mutmut_32 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_33'] = x_parse_range_results__mutmut_33 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_34'] = x_parse_range_results__mutmut_34 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_35'] = x_parse_range_results__mutmut_35 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_36'] = x_parse_range_results__mutmut_36 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_37'] = x_parse_range_results__mutmut_37 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_38'] = x_parse_range_results__mutmut_38 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_39'] = x_parse_range_results__mutmut_39 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_40'] = x_parse_range_results__mutmut_40 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_41'] = x_parse_range_results__mutmut_41 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_42'] = x_parse_range_results__mutmut_42 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_43'] = x_parse_range_results__mutmut_43 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_44'] = x_parse_range_results__mutmut_44 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_45'] = x_parse_range_results__mutmut_45 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_46'] = x_parse_range_results__mutmut_46 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_47'] = x_parse_range_results__mutmut_47 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_48'] = x_parse_range_results__mutmut_48 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_49'] = x_parse_range_results__mutmut_49 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_50'] = x_parse_range_results__mutmut_50 # type: ignore # mutmut generated
mutants_x_parse_range_results__mutmut['x_parse_range_results__mutmut_51'] = x_parse_range_results__mutmut_51 # type: ignore # mutmut generated
mutants_x__no_data_result__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__no_data_result__mutmut)
def _no_data_result(promql: str, query_type: QueryType) -> PrometheusQueryResult:
    return PrometheusQueryResult(
        query=promql,
        query_type=query_type,
        no_data=True,
        summary=f"No data found for query '{promql}'",
    )


def x__no_data_result__mutmut_orig(promql: str, query_type: QueryType) -> PrometheusQueryResult:
    return PrometheusQueryResult(
        query=promql,
        query_type=query_type,
        no_data=True,
        summary=f"No data found for query '{promql}'",
    )


def x__no_data_result__mutmut_1(promql: str, query_type: QueryType) -> PrometheusQueryResult:
    return PrometheusQueryResult(
        query=None,
        query_type=query_type,
        no_data=True,
        summary=f"No data found for query '{promql}'",
    )


def x__no_data_result__mutmut_2(promql: str, query_type: QueryType) -> PrometheusQueryResult:
    return PrometheusQueryResult(
        query=promql,
        query_type=None,
        no_data=True,
        summary=f"No data found for query '{promql}'",
    )


def x__no_data_result__mutmut_3(promql: str, query_type: QueryType) -> PrometheusQueryResult:
    return PrometheusQueryResult(
        query=promql,
        query_type=query_type,
        no_data=None,
        summary=f"No data found for query '{promql}'",
    )


def x__no_data_result__mutmut_4(promql: str, query_type: QueryType) -> PrometheusQueryResult:
    return PrometheusQueryResult(
        query=promql,
        query_type=query_type,
        no_data=True,
        summary=None,
    )


def x__no_data_result__mutmut_5(promql: str, query_type: QueryType) -> PrometheusQueryResult:
    return PrometheusQueryResult(
        query_type=query_type,
        no_data=True,
        summary=f"No data found for query '{promql}'",
    )


def x__no_data_result__mutmut_6(promql: str, query_type: QueryType) -> PrometheusQueryResult:
    return PrometheusQueryResult(
        query=promql,
        no_data=True,
        summary=f"No data found for query '{promql}'",
    )


def x__no_data_result__mutmut_7(promql: str, query_type: QueryType) -> PrometheusQueryResult:
    return PrometheusQueryResult(
        query=promql,
        query_type=query_type,
        summary=f"No data found for query '{promql}'",
    )


def x__no_data_result__mutmut_8(promql: str, query_type: QueryType) -> PrometheusQueryResult:
    return PrometheusQueryResult(
        query=promql,
        query_type=query_type,
        no_data=True,
        )


def x__no_data_result__mutmut_9(promql: str, query_type: QueryType) -> PrometheusQueryResult:
    return PrometheusQueryResult(
        query=promql,
        query_type=query_type,
        no_data=False,
        summary=f"No data found for query '{promql}'",
    )

mutants_x__no_data_result__mutmut['_mutmut_orig'] = x__no_data_result__mutmut_orig # type: ignore # mutmut generated
mutants_x__no_data_result__mutmut['x__no_data_result__mutmut_1'] = x__no_data_result__mutmut_1 # type: ignore # mutmut generated
mutants_x__no_data_result__mutmut['x__no_data_result__mutmut_2'] = x__no_data_result__mutmut_2 # type: ignore # mutmut generated
mutants_x__no_data_result__mutmut['x__no_data_result__mutmut_3'] = x__no_data_result__mutmut_3 # type: ignore # mutmut generated
mutants_x__no_data_result__mutmut['x__no_data_result__mutmut_4'] = x__no_data_result__mutmut_4 # type: ignore # mutmut generated
mutants_x__no_data_result__mutmut['x__no_data_result__mutmut_5'] = x__no_data_result__mutmut_5 # type: ignore # mutmut generated
mutants_x__no_data_result__mutmut['x__no_data_result__mutmut_6'] = x__no_data_result__mutmut_6 # type: ignore # mutmut generated
mutants_x__no_data_result__mutmut['x__no_data_result__mutmut_7'] = x__no_data_result__mutmut_7 # type: ignore # mutmut generated
mutants_x__no_data_result__mutmut['x__no_data_result__mutmut_8'] = x__no_data_result__mutmut_8 # type: ignore # mutmut generated
mutants_x__no_data_result__mutmut['x__no_data_result__mutmut_9'] = x__no_data_result__mutmut_9 # type: ignore # mutmut generated
mutants_x__summary__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__summary__mutmut)
def _summary(result_count: int, truncated: bool) -> str:
    plural = "" if result_count == 1 else "s"
    summary = f"{result_count} result{plural}"
    if truncated:
        summary += " (truncated — more than the maximum result limit was returned)"
    return summary


def x__summary__mutmut_orig(result_count: int, truncated: bool) -> str:
    plural = "" if result_count == 1 else "s"
    summary = f"{result_count} result{plural}"
    if truncated:
        summary += " (truncated — more than the maximum result limit was returned)"
    return summary


def x__summary__mutmut_1(result_count: int, truncated: bool) -> str:
    plural = None
    summary = f"{result_count} result{plural}"
    if truncated:
        summary += " (truncated — more than the maximum result limit was returned)"
    return summary


def x__summary__mutmut_2(result_count: int, truncated: bool) -> str:
    plural = "XXXX" if result_count == 1 else "s"
    summary = f"{result_count} result{plural}"
    if truncated:
        summary += " (truncated — more than the maximum result limit was returned)"
    return summary


def x__summary__mutmut_3(result_count: int, truncated: bool) -> str:
    plural = "" if result_count != 1 else "s"
    summary = f"{result_count} result{plural}"
    if truncated:
        summary += " (truncated — more than the maximum result limit was returned)"
    return summary


def x__summary__mutmut_4(result_count: int, truncated: bool) -> str:
    plural = "" if result_count == 2 else "s"
    summary = f"{result_count} result{plural}"
    if truncated:
        summary += " (truncated — more than the maximum result limit was returned)"
    return summary


def x__summary__mutmut_5(result_count: int, truncated: bool) -> str:
    plural = "" if result_count == 1 else "XXsXX"
    summary = f"{result_count} result{plural}"
    if truncated:
        summary += " (truncated — more than the maximum result limit was returned)"
    return summary


def x__summary__mutmut_6(result_count: int, truncated: bool) -> str:
    plural = "" if result_count == 1 else "S"
    summary = f"{result_count} result{plural}"
    if truncated:
        summary += " (truncated — more than the maximum result limit was returned)"
    return summary


def x__summary__mutmut_7(result_count: int, truncated: bool) -> str:
    plural = "" if result_count == 1 else "s"
    summary = None
    if truncated:
        summary += " (truncated — more than the maximum result limit was returned)"
    return summary


def x__summary__mutmut_8(result_count: int, truncated: bool) -> str:
    plural = "" if result_count == 1 else "s"
    summary = f"{result_count} result{plural}"
    if truncated:
        summary = " (truncated — more than the maximum result limit was returned)"
    return summary


def x__summary__mutmut_9(result_count: int, truncated: bool) -> str:
    plural = "" if result_count == 1 else "s"
    summary = f"{result_count} result{plural}"
    if truncated:
        summary -= " (truncated — more than the maximum result limit was returned)"
    return summary


def x__summary__mutmut_10(result_count: int, truncated: bool) -> str:
    plural = "" if result_count == 1 else "s"
    summary = f"{result_count} result{plural}"
    if truncated:
        summary += "XX (truncated — more than the maximum result limit was returned)XX"
    return summary


def x__summary__mutmut_11(result_count: int, truncated: bool) -> str:
    plural = "" if result_count == 1 else "s"
    summary = f"{result_count} result{plural}"
    if truncated:
        summary += " (TRUNCATED — MORE THAN THE MAXIMUM RESULT LIMIT WAS RETURNED)"
    return summary

mutants_x__summary__mutmut['_mutmut_orig'] = x__summary__mutmut_orig # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_1'] = x__summary__mutmut_1 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_2'] = x__summary__mutmut_2 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_3'] = x__summary__mutmut_3 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_4'] = x__summary__mutmut_4 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_5'] = x__summary__mutmut_5 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_6'] = x__summary__mutmut_6 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_7'] = x__summary__mutmut_7 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_8'] = x__summary__mutmut_8 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_9'] = x__summary__mutmut_9 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_10'] = x__summary__mutmut_10 # type: ignore # mutmut generated
mutants_x__summary__mutmut['x__summary__mutmut_11'] = x__summary__mutmut_11 # type: ignore # mutmut generated
