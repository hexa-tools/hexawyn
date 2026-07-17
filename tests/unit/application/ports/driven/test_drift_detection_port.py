from __future__ import annotations

from abc import ABC

import pytest
from hexawyn.application.ports.driven.drift_detection_port import DriftDetectionPort


class TestDriftDetectionPort:
    def test_is_abstract(self) -> None:
        assert issubclass(DriftDetectionPort, ABC)

    def test_cannot_instantiate(self) -> None:
        with pytest.raises(TypeError):
            DriftDetectionPort()  # type: ignore[abstract]
