"""Unit tests for RolloutStatusUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.rollout_status.rollout_status_service_port import (
    RolloutStatusServicePort,
)
from hexawyn.application.use_case.rollout_status.rollout_status_use_case import RolloutStatusUseCase


class TestRolloutStatusUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=RolloutStatusServicePort)
        use_case = RolloutStatusUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.get_status.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=RolloutStatusServicePort)
        mock_service.get_status.side_effect = RuntimeError("test error")
        use_case = RolloutStatusUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
