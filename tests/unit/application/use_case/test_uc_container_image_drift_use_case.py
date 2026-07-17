"""Unit tests for ContainerImageDriftUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.container_image_drift.container_image_drift_service_port import (
    ContainerImageDriftServicePort,
)
from hexawyn.application.use_case.container_image_drift.container_image_drift_use_case import (
    ContainerImageDriftUseCase,
)


class TestContainerImageDriftUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=ContainerImageDriftServicePort)
        use_case = ContainerImageDriftUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.detect_image_drift.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=ContainerImageDriftServicePort)
        mock_service.detect_image_drift.side_effect = RuntimeError("test error")
        use_case = ContainerImageDriftUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
