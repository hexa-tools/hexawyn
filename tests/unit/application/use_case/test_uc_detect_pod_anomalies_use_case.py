"""Unit tests for DetectPodAnomaliesUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.detect_pod_anomalies.detect_pod_anomalies_service_port import (
    DetectPodAnomaliesServicePort,
)
from hexawyn.application.use_case.detect_pod_anomalies.detect_pod_anomalies_use_case import (
    DetectPodAnomaliesUseCase,
)


class TestDetectPodAnomaliesUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=DetectPodAnomaliesServicePort)
        use_case = DetectPodAnomaliesUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.detect.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=DetectPodAnomaliesServicePort)
        mock_service.detect.side_effect = RuntimeError("test error")
        use_case = DetectPodAnomaliesUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
