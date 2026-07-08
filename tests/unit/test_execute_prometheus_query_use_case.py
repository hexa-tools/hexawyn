from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.execute_prometheus_query.execute_prometheus_query_command import (
    ExecutePrometheusQueryCommand,
)
from hexawyn.application.ports.driving.execute_prometheus_query.execute_prometheus_query_response import (
    ExecutePrometheusQueryResponse,
)
from hexawyn.application.ports.driving.execute_prometheus_query.execute_prometheus_query_service_port import (
    ExecutePrometheusQueryServicePort,
)
from hexawyn.application.use_case.execute_prometheus_query.execute_prometheus_query_use_case import (
    ExecutePrometheusQueryUseCase,
)


class TestExecutePrometheusQueryUseCase:
    def test_execute_delegates_to_service(self) -> None:
        service = MagicMock(spec=ExecutePrometheusQueryServicePort)
        expected = ExecutePrometheusQueryResponse(query="up")
        service.execute.return_value = expected
        use_case = ExecutePrometheusQueryUseCase(service=service)
        command = ExecutePrometheusQueryCommand(promql="up")

        result = use_case.execute(command)

        service.execute.assert_called_once_with(command)
        assert result is expected
