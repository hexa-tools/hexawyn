"""Unit tests for RolloutGetUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.rollout_get.rollout_get_service_port import (
    RolloutGetServicePort,
)
from hexawyn.application.use_case.rollout_get.rollout_get_use_case import RolloutGetUseCase


class TestRolloutGetUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=RolloutGetServicePort)
        use_case = RolloutGetUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.get_rollout.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=RolloutGetServicePort)
        mock_service.get_rollout.side_effect = RuntimeError("test error")
        use_case = RolloutGetUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
