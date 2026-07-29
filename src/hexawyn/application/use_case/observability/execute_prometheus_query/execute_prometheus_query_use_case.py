from __future__ import annotations

from hexawyn.application.ports.driven.metrics_query_port import MetricsQueryPort
from hexawyn.application.use_case.observability.execute_prometheus_query.command import (
    ExecutePrometheusQueryCommand,
)
from hexawyn.application.use_case.observability.execute_prometheus_query.response import (
    ExecutePrometheusQueryResponse,
)


class ExecutePrometheusQueryUseCase:
    def __init__(self, port: MetricsQueryPort) -> None:
        self._port = port

    def execute(
        self,
        command: ExecutePrometheusQueryCommand,
    ) -> ExecutePrometheusQueryResponse:
        result = self._port.execute_query(  # type: ignore
            query=command.query_type,
            start=command.start,
            end=command.end,
            step=command.step,
        )
        return ExecutePrometheusQueryResponse(
            status=str(result.get("status", "")),
            result_type=str(result.get("data", {}).get("resultType", "")),
            results=result.get("data", {}).get("result", []),
        )
