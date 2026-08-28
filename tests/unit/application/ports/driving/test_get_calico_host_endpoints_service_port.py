"""Tests for the GetCalicoHostEndpointsServicePort inbound port."""

from __future__ import annotations

import pytest
from hexawyn.application.ports.driving.get_calico_host_endpoints.get_calico_host_endpoints_service_port import (  # noqa: E501
    GetCalicoHostEndpointsServicePort,
)


class TestGetCalicoHostEndpointsServicePort:
    def test_is_abstract(self) -> None:
        with pytest.raises(TypeError):
            GetCalicoHostEndpointsServicePort()  # type: ignore[abstract]

    def test_declares_get_endpoints(self) -> None:
        assert "get_endpoints" in GetCalicoHostEndpointsServicePort.__abstractmethods__
