"""Unit tests for DetectZombiesUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.detect_zombies.detect_zombies_service_port import (
    DetectZombiesServicePort,
)
from hexawyn.application.use_case.detect_zombies.detect_zombies_use_case import DetectZombiesUseCase


class TestDetectZombiesUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=DetectZombiesServicePort)
        use_case = DetectZombiesUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.detect_zombies.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=DetectZombiesServicePort)
        mock_service.detect_zombies.side_effect = RuntimeError("test error")
        use_case = DetectZombiesUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
