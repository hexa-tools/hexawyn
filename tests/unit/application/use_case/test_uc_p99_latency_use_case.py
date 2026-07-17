"""Unit tests for P99LatencyUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.p99_latency.p99_latency_service_port import (
    P99LatencyServicePort,
)
from hexawyn.application.use_case.p99_latency.p99_latency_use_case import P99LatencyUseCase


class TestP99LatencyUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=P99LatencyServicePort)
        use_case = P99LatencyUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.compute_p99.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=P99LatencyServicePort)
        mock_service.compute_p99.side_effect = RuntimeError("test error")
        use_case = P99LatencyUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
