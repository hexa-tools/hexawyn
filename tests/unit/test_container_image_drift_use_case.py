from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.container_image_drift.container_image_drift_command import (
    ContainerImageDriftCommand,
)
from hexawyn.application.ports.driving.container_image_drift.container_image_drift_response import (
    ContainerImageDriftResponse,
)
from hexawyn.application.ports.driving.container_image_drift.container_image_drift_service_port import (
    ContainerImageDriftServicePort,
)
from hexawyn.application.use_case.container_image_drift.container_image_drift_use_case import (
    ContainerImageDriftUseCase,
)


class TestContainerImageDriftUseCase:
    def test_execute_delegates_to_service(self) -> None:
        service = MagicMock(spec=ContainerImageDriftServicePort)
        expected = ContainerImageDriftResponse()
        service.detect_image_drift.return_value = expected
        use_case = ContainerImageDriftUseCase(service=service)
        command = ContainerImageDriftCommand(namespace="production")

        result = use_case.execute(command)

        service.detect_image_drift.assert_called_once_with(command)
        assert result is expected
