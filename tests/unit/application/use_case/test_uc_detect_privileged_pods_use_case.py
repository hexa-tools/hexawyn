"""Unit tests for DetectPrivilegedPodsUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.detect_privileged_pods.detect_privileged_pods_service_port import (
    DetectPrivilegedPodsServicePort,
)
from hexawyn.application.use_case.detect_privileged_pods.detect_privileged_pods_use_case import (
    DetectPrivilegedPodsUseCase,
)


class TestDetectPrivilegedPodsUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=DetectPrivilegedPodsServicePort)
        use_case = DetectPrivilegedPodsUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.audit_pod_security.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=DetectPrivilegedPodsServicePort)
        mock_service.audit_pod_security.side_effect = RuntimeError("test error")
        use_case = DetectPrivilegedPodsUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
