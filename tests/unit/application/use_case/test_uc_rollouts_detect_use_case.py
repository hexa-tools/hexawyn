"""Unit tests for RolloutsDetectUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.rollouts_detect.rollouts_detect_service_port import (
    RolloutsDetectServicePort,
)
from hexawyn.application.use_case.rollouts_detect.rollouts_detect_use_case import (
    RolloutsDetectUseCase,
)


class TestRolloutsDetectUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=RolloutsDetectServicePort)
        use_case = RolloutsDetectUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.detect.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=RolloutsDetectServicePort)
        mock_service.detect.side_effect = RuntimeError("test error")
        use_case = RolloutsDetectUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
