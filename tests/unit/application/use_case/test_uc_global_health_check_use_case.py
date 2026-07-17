"""Unit tests for GlobalHealthCheckUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.global_health_check.global_health_check_service_port import (
    GlobalHealthCheckServicePort,
)
from hexawyn.application.use_case.global_health_check.global_health_check_use_case import (
    GlobalHealthCheckUseCase,
)


class TestGlobalHealthCheckUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=GlobalHealthCheckServicePort)
        use_case = GlobalHealthCheckUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.global_health_check.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=GlobalHealthCheckServicePort)
        mock_service.global_health_check.side_effect = RuntimeError("test error")
        use_case = GlobalHealthCheckUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
