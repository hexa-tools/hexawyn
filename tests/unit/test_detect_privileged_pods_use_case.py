from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.detect_privileged_pods.detect_privileged_pods_command import (
    DetectPrivilegedPodsCommand,
)
from hexawyn.application.ports.driving.detect_privileged_pods.detect_privileged_pods_response import (
    DetectPrivilegedPodsResponse,
)
from hexawyn.application.ports.driving.detect_privileged_pods.detect_privileged_pods_service_port import (
    DetectPrivilegedPodsServicePort,
)
from hexawyn.application.use_case.detect_privileged_pods.detect_privileged_pods_use_case import (
    DetectPrivilegedPodsUseCase,
)


class TestDetectPrivilegedPodsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        service = MagicMock(spec=DetectPrivilegedPodsServicePort)
        expected = DetectPrivilegedPodsResponse()
        service.audit_pod_security.return_value = expected
        use_case = DetectPrivilegedPodsUseCase(service=service)
        command = DetectPrivilegedPodsCommand()

        result = use_case.execute(command)

        service.audit_pod_security.assert_called_once_with(command)
        assert result is expected
