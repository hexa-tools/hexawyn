from __future__ import annotations

from hexawyn.application.ports.driven.metrics_query_port import MetricsQueryPort
from hexawyn.application.ports.driving.execute_prometheus_query.execute_prometheus_query_command import (
    ExecutePrometheusQueryCommand,
)
from hexawyn.application.ports.driving.execute_prometheus_query.execute_prometheus_query_response import (
    ExecutePrometheusQueryResponse,
    MetricResultDict,
)
from hexawyn.application.ports.driving.execute_prometheus_query.execute_prometheus_query_service_port import (
    ExecutePrometheusQueryServicePort,
)
from hexawyn.domain.models.metrics_query import PrometheusMetricResult, PrometheusQueryResult
from hexawyn.domain.services.metrics_query.result_parser import (
    parse_instant_results,
    parse_range_results,
)


class PrometheusQueryService(ExecutePrometheusQueryServicePort):
    def __init__(self, port: MetricsQueryPort) -> None:
        self._port = port

    def execute(self, command: ExecutePrometheusQueryCommand) -> ExecutePrometheusQueryResponse:
        if command.query_type == "range":
            assert command.start is not None, "range query requires start"
            assert command.end is not None, "range query requires end"
            raw_range = self._port.range_query(
                command.promql,
                start=command.start,
                end=command.end,
                step=command.step,
                timeout_seconds=command.timeout_seconds,
            )
            result = parse_range_results(
                raw_range, promql=command.promql, unit_hint=command.unit_hint
            )
        else:
            raw_instant = self._port.instant_query(
                command.promql, timeout_seconds=command.timeout_seconds
            )
            result = parse_instant_results(
                raw_instant, promql=command.promql, unit_hint=command.unit_hint
            )
        return _to_response(result)


def _to_response(result: PrometheusQueryResult) -> ExecutePrometheusQueryResponse:
    return ExecutePrometheusQueryResponse(
        query=result.query,
        query_type=result.query_type,
        results=[_to_result_dict(item) for item in result.results],
        result_count=result.result_count,
        truncated=result.truncated,
        no_data=result.no_data,
        summary=result.summary,
    )


def _to_result_dict(item: PrometheusMetricResult) -> MetricResultDict:
    return MetricResultDict(
        labels=item.labels,
        value=item.value,
        values=item.values,
        formatted_value=item.formatted_value,
    )
