from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.adapters.secondary.cilium.cilium_hubble_graph_adapter import (
    HubbleDependencyGraphAdapter,
)
from hexawyn.domain.models.cilium import CiliumFlowEntry, CiliumFlowsResult
from hexawyn.domain.models.service_dependency_graph import DependencyGraphRequest


def _flow(source: str, destination: str, verdict: str = "FORWARDED") -> CiliumFlowEntry:
    return CiliumFlowEntry(
        timestamp="t",
        source=source,
        destination=destination,
        source_namespace="payments",
        destination_namespace="payments",
        source_identity="100",
        destination_identity="200",
        verdict=verdict,
        drop_reason=None,
        protocol="tcp",
        destination_port="443",
        l7_protocol="http",
        direction="ingress",
        policy=None,
    )


class TestHubbleDependencyGraphAdapter:
    def test_builds_edges_from_flows(self) -> None:
        hubble_port = MagicMock()
        hubble_port.get_flows.return_value = CiliumFlowsResult(
            installed=True,
            status="present",
            total_flows=2,
            flows=[_flow("web-0", "db-0"), _flow("web-0", "db-0")],
            note=None,
        )

        adapter = HubbleDependencyGraphAdapter(hubble_port)
        edges = adapter.fetch_edges(DependencyGraphRequest(time_window_minutes=30))

        assert len(edges) == 1  # noqa: PLR2004
        assert edges[0]["from"] == "web-0"
        assert edges[0]["to"] == "db-0"
        assert edges[0]["count"] == 2  # noqa: PLR2004

    def test_empty_when_hubble_not_installed(self) -> None:
        hubble_port = MagicMock()
        hubble_port.get_flows.return_value = CiliumFlowsResult(
            installed=False,
            status="not_installed",
            total_flows=0,
            flows=[],
            note=None,
        )

        adapter = HubbleDependencyGraphAdapter(hubble_port)
        edges = adapter.fetch_edges(DependencyGraphRequest())

        assert edges == []

    def test_passes_window_to_hubble_query(self) -> None:
        hubble_port = MagicMock()
        hubble_port.get_flows.return_value = CiliumFlowsResult(
            installed=True, status="present", total_flows=0, flows=[], note=None
        )

        adapter = HubbleDependencyGraphAdapter(hubble_port)
        adapter.fetch_edges(DependencyGraphRequest(time_window_minutes=45))

        args = hubble_port.get_flows.call_args[0]
        query = args[0]
        assert query.window_minutes == 45  # noqa: PLR2004
