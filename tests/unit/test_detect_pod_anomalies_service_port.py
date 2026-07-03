from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driving.detect_pod_anomalies.detect_pod_anomalies_service_port import (
    DetectPodAnomaliesServicePort,
)


class TestDetectPodAnomaliesServicePort:
    def test_is_abstract(self) -> None:
        assert issubclass(DetectPodAnomaliesServicePort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            DetectPodAnomaliesServicePort()  # type: ignore[abstract]
