"""Unit tests for TraceLogCorrelationUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.trace_log_correlation.trace_log_correlation_service_port import (
    TraceLogCorrelationServicePort,
)
from hexawyn.application.use_case.trace_log_correlation.trace_log_correlation_use_case import (
    TraceLogCorrelationUseCase,
)


class TestTraceLogCorrelationUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=TraceLogCorrelationServicePort)
        use_case = TraceLogCorrelationUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.correlate.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=TraceLogCorrelationServicePort)
        mock_service.correlate.side_effect = RuntimeError("test error")
        use_case = TraceLogCorrelationUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
