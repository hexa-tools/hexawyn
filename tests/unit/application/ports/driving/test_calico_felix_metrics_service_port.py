"""Tests for the CalicoFelixMetricsServicePort inbound port."""

from __future__ import annotations

import pytest
from hexawyn.application.ports.driving.calico_felix_metrics.calico_felix_metrics_service_port import (  # noqa: E501
    CalicoFelixMetricsServicePort,
)


class TestCalicoFelixMetricsServicePort:
    def test_is_abstract(self) -> None:
        with pytest.raises(TypeError):
            CalicoFelixMetricsServicePort()  # type: ignore[abstract]

    def test_declares_metrics(self) -> None:
        assert "metrics" in CalicoFelixMetricsServicePort.__abstractmethods__
