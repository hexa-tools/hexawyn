from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driving.analyze_pod_logs.analyze_pod_logs_service_port import (
    AnalyzePodLogsServicePort,
)


class TestAnalyzePodLogsServicePort:
    def test_is_abstract(self) -> None:
        assert issubclass(AnalyzePodLogsServicePort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            AnalyzePodLogsServicePort()  # type: ignore[abstract]
