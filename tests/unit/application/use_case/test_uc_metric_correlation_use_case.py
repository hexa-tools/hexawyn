"""Unit tests for MetricCorrelationUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.metric_correlation.metric_correlation_service_port import (
    MetricCorrelationServicePort,
)
from hexawyn.application.use_case.metric_correlation.metric_correlation_use_case import (
    MetricCorrelationUseCase,
)


class TestMetricCorrelationUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=MetricCorrelationServicePort)
        use_case = MetricCorrelationUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.correlate.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=MetricCorrelationServicePort)
        mock_service.correlate.side_effect = RuntimeError("test error")
        use_case = MetricCorrelationUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
