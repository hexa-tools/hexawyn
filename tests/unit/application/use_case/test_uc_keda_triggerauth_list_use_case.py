"""Unit tests for KedaTriggerAuthListUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.keda_triggerauth_list.keda_triggerauth_list_service_port import (
    KedaTriggerAuthListServicePort,
)
from hexawyn.application.use_case.keda_triggerauth_list.keda_triggerauth_list_use_case import (
    KedaTriggerAuthListUseCase,
)


class TestKedaTriggerAuthListUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=KedaTriggerAuthListServicePort)
        use_case = KedaTriggerAuthListUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.list_auths.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=KedaTriggerAuthListServicePort)
        mock_service.list_auths.side_effect = RuntimeError("test error")
        use_case = KedaTriggerAuthListUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
