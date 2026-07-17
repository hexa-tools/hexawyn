from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driving.detect_log_anomalies.detect_log_anomalies_service_port import (
    DetectLogAnomaliesServicePort,
)


class TestDetectLogAnomaliesServicePort:
    def test_is_abstract(self) -> None:
        assert issubclass(DetectLogAnomaliesServicePort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            DetectLogAnomaliesServicePort()  # type: ignore[abstract]
