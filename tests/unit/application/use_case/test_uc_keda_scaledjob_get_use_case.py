"""Unit tests for KedaScaledJobGetUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.keda_scaledjob_get.keda_scaledjob_get_service_port import (
    KedaScaledJobGetServicePort,
)
from hexawyn.application.use_case.keda_scaledjob_get.keda_scaledjob_get_use_case import (
    KedaScaledJobGetUseCase,
)


class TestKedaScaledJobGetUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=KedaScaledJobGetServicePort)
        use_case = KedaScaledJobGetUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.get_job.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=KedaScaledJobGetServicePort)
        mock_service.get_job.side_effect = RuntimeError("test error")
        use_case = KedaScaledJobGetUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
