"""Unit tests for SlowestTracesUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.slowest_traces.slowest_traces_service_port import (
    SlowestTracesServicePort,
)
from hexawyn.application.use_case.slowest_traces.slowest_traces_use_case import SlowestTracesUseCase


class TestSlowestTracesUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=SlowestTracesServicePort)
        use_case = SlowestTracesUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.find_slowest.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=SlowestTracesServicePort)
        mock_service.find_slowest.side_effect = RuntimeError("test error")
        use_case = SlowestTracesUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
