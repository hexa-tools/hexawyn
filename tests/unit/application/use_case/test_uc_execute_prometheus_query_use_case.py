"""Unit tests for ExecutePrometheusQueryUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.execute_prometheus_query.execute_prometheus_query_service_port import (
    ExecutePrometheusQueryServicePort,
)
from hexawyn.application.use_case.execute_prometheus_query.execute_prometheus_query_use_case import (
    ExecutePrometheusQueryUseCase,
)


class TestExecutePrometheusQueryUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=ExecutePrometheusQueryServicePort)
        use_case = ExecutePrometheusQueryUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.execute.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=ExecutePrometheusQueryServicePort)
        mock_service.execute.side_effect = RuntimeError("test error")
        use_case = ExecutePrometheusQueryUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
