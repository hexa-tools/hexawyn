"""Tests for the CalicoConnectivityHealthServicePort inbound port."""

from __future__ import annotations

import pytest
from hexawyn.application.ports.driving.calico_connectivity_health.calico_connectivity_health_service_port import (  # noqa: E501
    CalicoConnectivityHealthServicePort,
)


class TestCalicoConnectivityHealthServicePort:
    def test_is_abstract(self) -> None:
        with pytest.raises(TypeError):
            CalicoConnectivityHealthServicePort()  # type: ignore[abstract]

    def test_declares_health(self) -> None:
        assert "health" in CalicoConnectivityHealthServicePort.__abstractmethods__
