"""Tests for the ListCalicoIpPoolsServicePort inbound port."""

from __future__ import annotations

import pytest
from hexawyn.application.ports.driving.list_calico_ip_pools.list_calico_ip_pools_service_port import (  # noqa: E501
    ListCalicoIpPoolsServicePort,
)


class TestListCalicoIpPoolsServicePort:
    def test_is_abstract(self) -> None:
        with pytest.raises(TypeError):
            ListCalicoIpPoolsServicePort()  # type: ignore[abstract]

    def test_declares_list_pools(self) -> None:
        assert "list_pools" in ListCalicoIpPoolsServicePort.__abstractmethods__
