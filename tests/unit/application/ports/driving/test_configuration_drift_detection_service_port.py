from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driving.configuration_drift_detection.configuration_drift_detection_service_port import (
    ConfigurationDriftDetectionServicePort,
)


class TestConfigurationDriftDetectionServicePort:
    def test_is_abstract(self) -> None:
        assert issubclass(ConfigurationDriftDetectionServicePort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            ConfigurationDriftDetectionServicePort()  # type: ignore[abstract]
