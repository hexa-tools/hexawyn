from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.observability.execute_prometheus_query.command import (
    ExecutePrometheusQueryCommand,
)
from hexawyn.application.use_case.observability.execute_prometheus_query.execute_prometheus_query_use_case import (  # noqa: E501
    ExecutePrometheusQueryUseCase,
)
from hexawyn.application.use_case.observability.execute_prometheus_query.response import (
    ExecutePrometheusQueryResponse,
)


class TestExecutePrometheusQueryUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.execute_query.return_value = {
            "status": "success",
            "data": {"resultType": "vector", "result": []},
        }

        use_case = ExecutePrometheusQueryUseCase(port=port)
        result = use_case.execute(ExecutePrometheusQueryCommand(query_type="instant"))

        assert isinstance(result, ExecutePrometheusQueryResponse)
        assert result.status == "success"
