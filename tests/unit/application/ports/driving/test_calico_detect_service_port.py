"""Tests for the CalicoDetectServicePort inbound port."""

from __future__ import annotations

import pytest
from hexawyn.application.ports.driving.calico_detect.calico_detect_service_port import (
    CalicoDetectServicePort,
)


class TestCalicoDetectServicePort:
    def test_is_abstract(self) -> None:
        with pytest.raises(TypeError):
            CalicoDetectServicePort()  # type: ignore[abstract]

    def test_declares_detect(self) -> None:
        assert "detect" in CalicoDetectServicePort.__abstractmethods__
