"""Tests for the GetCalicoStatusServicePort inbound port."""

from __future__ import annotations

import pytest
from hexawyn.application.ports.driving.get_calico_status.get_calico_status_service_port import (
    GetCalicoStatusServicePort,
)


class TestGetCalicoStatusServicePort:
    def test_is_abstract(self) -> None:
        with pytest.raises(TypeError):
            GetCalicoStatusServicePort()  # type: ignore[abstract]

    def test_declares_get_status(self) -> None:
        assert "get_status" in GetCalicoStatusServicePort.__abstractmethods__
