"""Tests for the ListCalicoNetworkPoliciesServicePort inbound port."""

from __future__ import annotations

import pytest
from hexawyn.application.ports.driving.list_calico_network_policies.list_calico_network_policies_service_port import (  # noqa: E501
    ListCalicoNetworkPoliciesServicePort,
)


class TestListCalicoNetworkPoliciesServicePort:
    def test_is_abstract(self) -> None:
        with pytest.raises(TypeError):
            ListCalicoNetworkPoliciesServicePort()  # type: ignore[abstract]

    def test_declares_list_policies(self) -> None:
        assert "list_policies" in ListCalicoNetworkPoliciesServicePort.__abstractmethods__
