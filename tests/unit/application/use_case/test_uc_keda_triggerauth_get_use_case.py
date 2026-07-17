"""Unit tests for KedaTriggerAuthGetUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.keda_triggerauth_get.keda_triggerauth_get_service_port import (
    KedaTriggerAuthGetServicePort,
)
from hexawyn.application.use_case.keda_triggerauth_get.keda_triggerauth_get_use_case import (
    KedaTriggerAuthGetUseCase,
)


class TestKedaTriggerAuthGetUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=KedaTriggerAuthGetServicePort)
        use_case = KedaTriggerAuthGetUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.get_auth.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=KedaTriggerAuthGetServicePort)
        mock_service.get_auth.side_effect = RuntimeError("test error")
        use_case = KedaTriggerAuthGetUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
