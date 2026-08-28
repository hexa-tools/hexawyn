from __future__ import annotations

from unittest.mock import patch

import pytest
from hexawyn.adapters.secondary.cilium.cilium_hubble_adapter import CiliumHubbleAdapter
from hexawyn.domain.errors import AdapterTimeoutError, ClusterUnreachableError
from hexawyn.domain.models.cilium import (
    CiliumDenialsQuery,
    CiliumFlowEntry,
    CiliumFlowQuery,
    CiliumFlowsResult,
)


def _dropped_flow(source: str = "web-0", destination: str = "db-0") -> CiliumFlowEntry:
    return CiliumFlowEntry(
        timestamp="t",
        source=source,
        destination=destination,
        source_namespace="payments",
        destination_namespace="payments",
        source_identity="100",
        destination_identity="200",
        verdict="DROPPED",
        drop_reason="Policy denied",
        protocol="tcp",
        destination_port="443",
        l7_protocol=None,
        direction="ingress",
        policy="default/deny-all",
    )


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

    def test_detect_denials_groups_dropped(self) -> None:
        flows_result = CiliumFlowsResult(
            installed=True,
            status="present",
            total_flows=2,
            flows=[_dropped_flow(), _dropped_flow(destination="cache-0")],
            note=None,
        )
        with patch.object(CiliumHubbleAdapter, "get_flows", return_value=flows_result):
            result = CiliumHubbleAdapter().detect_denials(CiliumDenialsQuery())

        assert result.installed is True
        assert result.status == "present"
        assert result.total_denials == 2  # noqa: PLR2004
        assert len(result.groups) == 2  # noqa: PLR2004
        assert result.groups[0].policy == "default/deny-all"

    def test_detect_denials_not_installed(self) -> None:
        flows_result = CiliumFlowsResult(
            installed=False,
            status="not_installed",
            total_flows=0,
            flows=[],
            note=None,
        )
        with patch.object(CiliumHubbleAdapter, "get_flows", return_value=flows_result):
            result = CiliumHubbleAdapter().detect_denials(CiliumDenialsQuery())

        assert result.installed is False
        assert result.status == "not_installed"
        assert result.groups == []

    def test_detect_denials_timeout_raises_adapter_timeout(self) -> None:
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
                CiliumHubbleAdapter().detect_denials(CiliumDenialsQuery())
