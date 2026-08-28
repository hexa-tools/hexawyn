from __future__ import annotations

from unittest.mock import patch

import pytest
from hexawyn.adapters.secondary.cilium.cilium_hubble_adapter import CiliumHubbleAdapter
from hexawyn.domain.errors import AdapterTimeoutError, ClusterUnreachableError
from hexawyn.domain.models.cilium import CiliumFlowQuery


class TestCiliumHubbleAdapter:
    def test_not_installed_when_no_hubble_url(self) -> None:
        with patch(
            "hexawyn.adapters.secondary.cilium.cilium_hubble_adapter.hubble_available",
            return_value=False,
        ):
            result = CiliumHubbleAdapter().get_flows(CiliumFlowQuery())

        assert result.installed is False
        assert result.status == "not_installed"
        assert result.flows == []

    def test_timeout_raises_adapter_timeout(self) -> None:
        with (
            patch(
                "hexawyn.adapters.secondary.cilium.cilium_hubble_adapter.hubble_available",
                return_value=True,
            ),
            patch(
                "hexawyn.adapters.secondary.cilium.cilium_hubble_adapter.fetch_hubble_flows",
                side_effect=TimeoutError("timed out"),
            ),
        ):
            with pytest.raises(AdapterTimeoutError):
                CiliumHubbleAdapter().get_flows(CiliumFlowQuery())

    def test_unreachable_raises_cluster_unreachable(self) -> None:
        with (
            patch(
                "hexawyn.adapters.secondary.cilium.cilium_hubble_adapter.hubble_available",
                return_value=True,
            ),
            patch(
                "hexawyn.adapters.secondary.cilium.cilium_hubble_adapter.fetch_hubble_flows",
                side_effect=RuntimeError("connection refused"),
            ),
        ):
            with pytest.raises(ClusterUnreachableError):
                CiliumHubbleAdapter().get_flows(CiliumFlowQuery())

    def test_returns_flows(self) -> None:
        raw = [
            {
                "time": "2026-08-28T10:00:00Z",
                "verdict": "FORWARDED",
                "direction": "ingress",
                "source": {"namespace": "payments", "pod_name": "web-0"},
                "destination": {"namespace": "payments", "pod_name": "db-0"},
                "l4": {"tcp": {"destination_port": 443}},
            }
        ]
        with (
            patch(
                "hexawyn.adapters.secondary.cilium.cilium_hubble_adapter.hubble_available",
                return_value=True,
            ),
            patch(
                "hexawyn.adapters.secondary.cilium.cilium_hubble_adapter.fetch_hubble_flows",
                return_value=raw,
            ),
        ):
            result = CiliumHubbleAdapter().get_flows(CiliumFlowQuery(namespace="payments"))

        assert result.installed is True
        assert result.status == "present"
        assert result.flows[0].verdict == "FORWARDED"
        assert result.flows[0].destination_port == "443"
