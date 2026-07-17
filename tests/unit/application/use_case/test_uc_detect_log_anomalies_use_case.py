"""Unit tests for DetectLogAnomaliesUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.detect_log_anomalies.detect_log_anomalies_service_port import (
    DetectLogAnomaliesServicePort,
)
from hexawyn.application.use_case.detect_log_anomalies.detect_log_anomalies_use_case import (
    DetectLogAnomaliesUseCase,
)


class TestDetectLogAnomaliesUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=DetectLogAnomaliesServicePort)
        use_case = DetectLogAnomaliesUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.detect.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=DetectLogAnomaliesServicePort)
        mock_service.detect.side_effect = RuntimeError("test error")
        use_case = DetectLogAnomaliesUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
