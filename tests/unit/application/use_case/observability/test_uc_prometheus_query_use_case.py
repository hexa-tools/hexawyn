from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.observability.execute_prometheus_query.command import (
    ExecutePrometheusQueryCommand,
)
from hexawyn.application.use_case.observability.execute_prometheus_query.response import (
    ExecutePrometheusQueryResponse,
)
from hexawyn.application.use_case.observability.prometheus_query.prometheus_query_use_case import (  # noqa: E501
    PrometheusQueryUseCase,
)


class TestPrometheusQueryUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.execute_query.return_value = {
            "status": "success",
            "data": {"resultType": "vector", "result": []},
        }

        use_case = PrometheusQueryUseCase(port=port)
        result = use_case.execute(ExecutePrometheusQueryCommand(query_type="instant"))

        assert isinstance(result, ExecutePrometheusQueryResponse)

    def test_execute_range_query(self) -> None:
        port = MagicMock()
        port.range_query.return_value = []

        use_case = PrometheusQueryUseCase(port=port)
        result = use_case.execute(
            ExecutePrometheusQueryCommand(
                promql="up",
                query_type="range",
                start="2024-01-01T00:00:00Z",
                end="2024-01-01T01:00:00Z",
                step="60s",
            )
        )

        assert isinstance(result, ExecutePrometheusQueryResponse)

    def test_execute_with_non_empty_results(self) -> None:
        port = MagicMock()
        port.instant_query.return_value = [
            {"metric": {"job": "api"}, "value": 42.0},
        ]

        use_case = PrometheusQueryUseCase(port=port)
        result = use_case.execute(ExecutePrometheusQueryCommand(promql="up"))

        assert isinstance(result, ExecutePrometheusQueryResponse)
        assert result.result_count == 1
