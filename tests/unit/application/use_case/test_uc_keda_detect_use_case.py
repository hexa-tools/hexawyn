"""Unit tests for KedaDetectUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.keda_detect.keda_detect_service_port import (
    KedaDetectServicePort,
)
from hexawyn.application.use_case.keda_detect.keda_detect_use_case import KedaDetectUseCase


class TestKedaDetectUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=KedaDetectServicePort)
        use_case = KedaDetectUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.detect.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=KedaDetectServicePort)
        mock_service.detect.side_effect = RuntimeError("test error")
        use_case = KedaDetectUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
