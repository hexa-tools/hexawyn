"""Unit tests for CertsDetectUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.certs_detect.certs_detect_service_port import (
    CertsDetectServicePort,
)
from hexawyn.application.use_case.certs_detect.certs_detect_use_case import CertsDetectUseCase


class TestCertsDetectUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=CertsDetectServicePort)
        use_case = CertsDetectUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.detect.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=CertsDetectServicePort)
        mock_service.detect.side_effect = RuntimeError("test error")
        use_case = CertsDetectUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
