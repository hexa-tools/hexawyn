"""Unit tests for DeploymentLatencyUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.deployment_latency.deployment_latency_service_port import (
    DeploymentLatencyServicePort,
)
from hexawyn.application.use_case.deployment_latency.deployment_latency_use_case import (
    DeploymentLatencyUseCase,
)


class TestDeploymentLatencyUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=DeploymentLatencyServicePort)
        use_case = DeploymentLatencyUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.compare.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=DeploymentLatencyServicePort)
        mock_service.compare.side_effect = RuntimeError("test error")
        use_case = DeploymentLatencyUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
