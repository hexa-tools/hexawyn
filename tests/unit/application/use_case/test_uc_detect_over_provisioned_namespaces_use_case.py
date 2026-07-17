"""Unit tests for DetectOverProvisionedNamespacesUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.detect_over_provisioned_namespaces.detect_over_provisioned_namespaces_service_port import (
    DetectOverProvisionedNamespacesServicePort,
)
from hexawyn.application.use_case.detect_over_provisioned_namespaces.detect_over_provisioned_namespaces_use_case import (
    DetectOverProvisionedNamespacesUseCase,
)


class TestDetectOverProvisionedNamespacesUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=DetectOverProvisionedNamespacesServicePort)
        use_case = DetectOverProvisionedNamespacesUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.detect_over_provisioned_namespaces.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=DetectOverProvisionedNamespacesServicePort)
        mock_service.detect_over_provisioned_namespaces.side_effect = RuntimeError("test error")
        use_case = DetectOverProvisionedNamespacesUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
