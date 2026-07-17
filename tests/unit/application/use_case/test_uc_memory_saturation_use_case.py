"""Unit tests for MemorySaturationUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.memory_saturation.memory_saturation_service_port import (
    MemorySaturationServicePort,
)
from hexawyn.application.use_case.memory_saturation.memory_saturation_use_case import (
    MemorySaturationUseCase,
)


class TestMemorySaturationUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=MemorySaturationServicePort)
        use_case = MemorySaturationUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.predict.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=MemorySaturationServicePort)
        mock_service.predict.side_effect = RuntimeError("test error")
        use_case = MemorySaturationUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
