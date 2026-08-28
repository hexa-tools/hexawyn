from __future__ import annotations

from hexawyn.domain.models.cilium import CiliumFlowEntry
from hexawyn.domain.services.cilium.graph_builder import build_graph_edges


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


class TestBuildGraphEdges:
    def test_aggregates_by_pair(self) -> None:
        edges = build_graph_edges(
            [_flow("web-0", "db-0"), _flow("web-0", "db-0"), _flow("web-0", "cache-0")]
        )

        assert len(edges) == 2  # noqa: PLR2004
        db_edge = next(e for e in edges if e["to"] == "db-0")
        assert db_edge["count"] == 2  # noqa: PLR2004
        assert db_edge["errors"] == 0

    def test_counts_dropped_as_errors(self) -> None:
        edges = build_graph_edges(
            [_flow("web-0", "db-0", verdict="DROPPED"), _flow("web-0", "db-0")]
        )

        db_edge = next(e for e in edges if e["to"] == "db-0")
        assert db_edge["count"] == 2  # noqa: PLR2004
        assert db_edge["errors"] == 1  # noqa: PLR2004

    def test_includes_self_loop(self) -> None:
        edges = build_graph_edges([_flow("web-0", "web-0")])

        assert len(edges) == 1  # noqa: PLR2004
        assert edges[0]["from"] == "web-0"
        assert edges[0]["to"] == "web-0"

    def test_skips_incomplete_pairs(self) -> None:
        edges = build_graph_edges([_flow("", "db-0"), _flow("web-0", "")])

        assert edges == []

    def test_empty_flows(self) -> None:
        assert build_graph_edges([]) == []
