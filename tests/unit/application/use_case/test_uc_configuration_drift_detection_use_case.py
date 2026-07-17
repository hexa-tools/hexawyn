"""Unit tests for ConfigurationDriftDetectionUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.configuration_drift_detection.configuration_drift_detection_service_port import (
    ConfigurationDriftDetectionServicePort,
)
from hexawyn.application.use_case.configuration_drift_detection.configuration_drift_detection_use_case import (
    ConfigurationDriftDetectionUseCase,
)


class TestConfigurationDriftDetectionUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=ConfigurationDriftDetectionServicePort)
        use_case = ConfigurationDriftDetectionUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.detect_drift.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=ConfigurationDriftDetectionServicePort)
        mock_service.detect_drift.side_effect = RuntimeError("test error")
        use_case = ConfigurationDriftDetectionUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
