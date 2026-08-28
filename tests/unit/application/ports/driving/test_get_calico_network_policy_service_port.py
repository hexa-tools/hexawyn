"""Tests for the GetCalicoNetworkPolicyServicePort inbound port."""

from __future__ import annotations

import pytest
from hexawyn.application.ports.driving.get_calico_network_policy.get_calico_network_policy_service_port import (  # noqa: E501
    GetCalicoNetworkPolicyServicePort,
)


class TestGetCalicoNetworkPolicyServicePort:
    def test_is_abstract(self) -> None:
        with pytest.raises(TypeError):
            GetCalicoNetworkPolicyServicePort()  # type: ignore[abstract]

    def test_declares_get_policy(self) -> None:
        assert "get_policy" in GetCalicoNetworkPolicyServicePort.__abstractmethods__
