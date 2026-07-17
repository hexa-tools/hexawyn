"""Unit tests for RolloutsListUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.rollouts_list.rollouts_list_service_port import (
    RolloutsListServicePort,
)
from hexawyn.application.use_case.rollouts_list.rollouts_list_use_case import RolloutsListUseCase


class TestRolloutsListUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=RolloutsListServicePort)
        use_case = RolloutsListUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.list_rollouts.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=RolloutsListServicePort)
        mock_service.list_rollouts.side_effect = RuntimeError("test error")
        use_case = RolloutsListUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
