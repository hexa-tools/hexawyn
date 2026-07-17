"""Unit tests for PolicyViolationsListUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.policy_violations_list.policy_violations_list_service_port import (
    PolicyViolationsListServicePort,
)
from hexawyn.application.use_case.policy_violations_list.policy_violations_list_use_case import (
    PolicyViolationsListUseCase,
)


class TestPolicyViolationsListUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=PolicyViolationsListServicePort)
        use_case = PolicyViolationsListUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.list_violations.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=PolicyViolationsListServicePort)
        mock_service.list_violations.side_effect = RuntimeError("test error")
        use_case = PolicyViolationsListUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
