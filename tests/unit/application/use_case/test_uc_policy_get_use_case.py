"""Unit tests for PolicyGetUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.policy_get.policy_get_service_port import (
    PolicyGetServicePort,
)
from hexawyn.application.use_case.policy_get.policy_get_use_case import PolicyGetUseCase


class TestPolicyGetUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=PolicyGetServicePort)
        use_case = PolicyGetUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.get_policy.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=PolicyGetServicePort)
        mock_service.get_policy.side_effect = RuntimeError("test error")
        use_case = PolicyGetUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
