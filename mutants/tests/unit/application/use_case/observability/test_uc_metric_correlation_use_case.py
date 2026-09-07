from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.observability.metric_correlation.command import (
    MetricCorrelationCommand,
)
from hexawyn.application.use_case.observability.metric_correlation.metric_correlation_use_case import (  # noqa: E501
    MetricCorrelationUseCase,
)
from hexawyn.application.use_case.observability.metric_correlation.response import (
    MetricCorrelationResponse,
)


class TestMetricCorrelationUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.correlate_metrics.return_value = []
        use_case = MetricCorrelationUseCase(port=port)
        result = use_case.execute(MetricCorrelationCommand(service_name="api"))
        assert isinstance(result, MetricCorrelationResponse)

    def test_execute_empty_data(self) -> None:
        port = MagicMock()
        port.correlate_metrics.return_value = []
        use_case = MetricCorrelationUseCase(port=port)
        result = use_case.execute(MetricCorrelationCommand(service_name="api"))
        assert isinstance(result, MetricCorrelationResponse)
