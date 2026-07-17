"""Unit tests for RedundantCallsUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.redundant_calls.redundant_calls_service_port import (
    RedundantCallsServicePort,
)
from hexawyn.application.use_case.redundant_calls.redundant_calls_use_case import (
    RedundantCallsUseCase,
)


class TestRedundantCallsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=RedundantCallsServicePort)
        use_case = RedundantCallsUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.detect.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=RedundantCallsServicePort)
        mock_service.detect.side_effect = RuntimeError("test error")
        use_case = RedundantCallsUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
