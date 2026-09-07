from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.observability.trace_log_correlation.command import (
    TraceLogCorrelationCommand,
)
from hexawyn.application.use_case.observability.trace_log_correlation.response import (
    TraceLogCorrelationResponse,
)
from hexawyn.application.use_case.observability.trace_log_correlation.trace_log_correlation_use_case import (  # noqa: E501
    TraceLogCorrelationUseCase,
)


class TestTraceLogCorrelationUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.correlate_trace_logs.return_value = []
        use_case = TraceLogCorrelationUseCase(port=port)
        result = use_case.execute(TraceLogCorrelationCommand(trace_id="abc123"))
        assert isinstance(result, TraceLogCorrelationResponse)

    def test_execute_empty_data(self) -> None:
        port = MagicMock()
        port.correlate_trace_logs.return_value = []
        use_case = TraceLogCorrelationUseCase(port=port)
        result = use_case.execute(TraceLogCorrelationCommand(trace_id="abc123"))
        assert isinstance(result, TraceLogCorrelationResponse)
