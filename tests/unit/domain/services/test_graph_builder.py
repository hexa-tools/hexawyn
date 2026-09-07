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

    def test_incomplete_pair_in_middle_is_skipped_not_breaking(self) -> None:
        edges = build_graph_edges(
            [_flow("web-0", "db-0"), _flow("", "empty-0"), _flow("web-0", "cache-0")]
        )

        assert len(edges) == 2  # noqa: PLR2004
        assert {e["to"] for e in edges} == {"db-0", "cache-0"}

    def test_exact_edges(self) -> None:
        edges = build_graph_edges(
            [
                _flow("web-0", "db-0"),
                _flow("web-0", "db-0"),
                _flow("web-0", "db-0", verdict="DROPPED"),
                _flow("web-0", "cache-0"),
            ]
        )

        assert edges == [
            {
                "from": "web-0",
                "to": "cache-0",
                "count": 1,  # noqa: PLR2004
                "avg_ms": 0.0,
                "errors": 0,
            },
            {
                "from": "web-0",
                "to": "db-0",
                "count": 3,  # noqa: PLR2004
                "avg_ms": 0.0,
                "errors": 1,  # noqa: PLR2004
            },
        ]

    def test_errors_are_per_pair(self) -> None:
        edges = build_graph_edges(
            [
                _flow("a-0", "x-0", verdict="DROPPED"),
                _flow("a-0", "y-0", verdict="DROPPED"),
                _flow("a-0", "x-0"),
            ]
        )

        edges_by_to = {e["to"]: e for e in edges}

        assert edges_by_to["x-0"]["errors"] == 1  # noqa: PLR2004
        assert edges_by_to["y-0"]["errors"] == 1  # noqa: PLR2004

    def test_multiple_dropped_same_pair_increment(self) -> None:
        edges = build_graph_edges(
            [
                _flow("web-0", "db-0", verdict="DROPPED"),
                _flow("web-0", "db-0", verdict="DROPPED"),
                _flow("web-0", "db-0"),
            ]
        )

        assert edges[0]["count"] == 3  # noqa: PLR2004
        assert edges[0]["errors"] == 2  # noqa: PLR2004

    def test_skips_incomplete_pairs(self) -> None:
        edges = build_graph_edges([_flow("", "db-0"), _flow("web-0", "")])

        assert edges == []

    def test_empty_flows(self) -> None:
        assert build_graph_edges([]) == []
