"""Unit tests for ComputeSecurityPostureUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.compute_security_posture.compute_security_posture_service_port import (
    ComputeSecurityPostureServicePort,
)
from hexawyn.application.use_case.compute_security_posture.compute_security_posture_use_case import (
    ComputeSecurityPostureUseCase,
)


class TestComputeSecurityPostureUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=ComputeSecurityPostureServicePort)
        use_case = ComputeSecurityPostureUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.compute.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=ComputeSecurityPostureServicePort)
        mock_service.compute.side_effect = RuntimeError("test error")
        use_case = ComputeSecurityPostureUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
