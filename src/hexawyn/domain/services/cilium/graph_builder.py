"""Pure Cilium flow-to-graph edge aggregation — no infra imports."""

from __future__ import annotations

from hexawyn.domain.models.cilium import CiliumFlowEntry


def build_graph_edges(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
    """Aggregate flows into dependency-graph edge dicts, deduplicated by pair.

    Each edge carries the observed flow count, the average latency (0 when not
    reported) and the dropped count, so ``DependencyGraph.compute`` can derive
    call counts and error rates from observed traffic only.
    """
    counts: dict[tuple[str, str], int] = {}
    errors: dict[tuple[str, str], int] = {}
    for flow in flows:
        source = flow.source
        target = flow.destination
        if not source or not target:
            continue
        key = (source, target)
        counts[key] = counts.get(key, 0) + 1
        if flow.verdict.lower() == "dropped":
            errors[key] = errors.get(key, 0) + 1
    edges: list[dict[str, object]] = []
    for (source, target), count in sorted(counts.items()):
        edges.append(
            {
                "from": source,
                "to": target,
                "count": count,
                "avg_ms": 0.0,
                "errors": errors.get((source, target), 0),
            }
        )
    return edges
