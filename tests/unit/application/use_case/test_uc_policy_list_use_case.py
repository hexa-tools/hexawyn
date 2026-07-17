"""Unit tests for PolicyListUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.policy_list.policy_list_service_port import (
    PolicyListServicePort,
)
from hexawyn.application.use_case.policy_list.policy_list_use_case import PolicyListUseCase


class TestPolicyListUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=PolicyListServicePort)
        use_case = PolicyListUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.list_policies.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=PolicyListServicePort)
        mock_service.list_policies.side_effect = RuntimeError("test error")
        use_case = PolicyListUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
