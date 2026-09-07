"""Pure Cilium flow-to-graph edge aggregation — no infra imports."""

from __future__ import annotations

from hexawyn.domain.models.cilium import CiliumFlowEntry


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_graph_edges__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_graph_edges__mutmut)
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


def x_build_graph_edges__mutmut_orig(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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


def x_build_graph_edges__mutmut_1(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
    """Aggregate flows into dependency-graph edge dicts, deduplicated by pair.

    Each edge carries the observed flow count, the average latency (0 when not
    reported) and the dropped count, so ``DependencyGraph.compute`` can derive
    call counts and error rates from observed traffic only.
    """
    counts: dict[tuple[str, str], int] = None
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


def x_build_graph_edges__mutmut_2(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
    """Aggregate flows into dependency-graph edge dicts, deduplicated by pair.

    Each edge carries the observed flow count, the average latency (0 when not
    reported) and the dropped count, so ``DependencyGraph.compute`` can derive
    call counts and error rates from observed traffic only.
    """
    counts: dict[tuple[str, str], int] = {}
    errors: dict[tuple[str, str], int] = None
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


def x_build_graph_edges__mutmut_3(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
    """Aggregate flows into dependency-graph edge dicts, deduplicated by pair.

    Each edge carries the observed flow count, the average latency (0 when not
    reported) and the dropped count, so ``DependencyGraph.compute`` can derive
    call counts and error rates from observed traffic only.
    """
    counts: dict[tuple[str, str], int] = {}
    errors: dict[tuple[str, str], int] = {}
    for flow in flows:
        source = None
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


def x_build_graph_edges__mutmut_4(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
    """Aggregate flows into dependency-graph edge dicts, deduplicated by pair.

    Each edge carries the observed flow count, the average latency (0 when not
    reported) and the dropped count, so ``DependencyGraph.compute`` can derive
    call counts and error rates from observed traffic only.
    """
    counts: dict[tuple[str, str], int] = {}
    errors: dict[tuple[str, str], int] = {}
    for flow in flows:
        source = flow.source
        target = None
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


def x_build_graph_edges__mutmut_5(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
        if not source and not target:
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


def x_build_graph_edges__mutmut_6(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
        if source or not target:
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


def x_build_graph_edges__mutmut_7(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
        if not source or target:
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


def x_build_graph_edges__mutmut_8(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
            break
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


def x_build_graph_edges__mutmut_9(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
        key = None
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


def x_build_graph_edges__mutmut_10(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
        counts[key] = None
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


def x_build_graph_edges__mutmut_11(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
        counts[key] = counts.get(key, 0) - 1
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


def x_build_graph_edges__mutmut_12(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
        counts[key] = counts.get(None, 0) + 1
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


def x_build_graph_edges__mutmut_13(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
        counts[key] = counts.get(key, None) + 1
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


def x_build_graph_edges__mutmut_14(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
        counts[key] = counts.get(0) + 1
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


def x_build_graph_edges__mutmut_15(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
        counts[key] = counts.get(key, ) + 1
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


def x_build_graph_edges__mutmut_16(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
        counts[key] = counts.get(key, 1) + 1
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


def x_build_graph_edges__mutmut_17(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
        counts[key] = counts.get(key, 0) + 2
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


def x_build_graph_edges__mutmut_18(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
        if flow.verdict.upper() == "dropped":
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


def x_build_graph_edges__mutmut_19(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
        if flow.verdict.lower() != "dropped":
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


def x_build_graph_edges__mutmut_20(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
        if flow.verdict.lower() == "XXdroppedXX":
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


def x_build_graph_edges__mutmut_21(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
        if flow.verdict.lower() == "DROPPED":
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


def x_build_graph_edges__mutmut_22(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
            errors[key] = None
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


def x_build_graph_edges__mutmut_23(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
            errors[key] = errors.get(key, 0) - 1
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


def x_build_graph_edges__mutmut_24(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
            errors[key] = errors.get(None, 0) + 1
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


def x_build_graph_edges__mutmut_25(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
            errors[key] = errors.get(key, None) + 1
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


def x_build_graph_edges__mutmut_26(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
            errors[key] = errors.get(0) + 1
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


def x_build_graph_edges__mutmut_27(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
            errors[key] = errors.get(key, ) + 1
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


def x_build_graph_edges__mutmut_28(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
            errors[key] = errors.get(key, 1) + 1
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


def x_build_graph_edges__mutmut_29(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
            errors[key] = errors.get(key, 0) + 2
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


def x_build_graph_edges__mutmut_30(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
    edges: list[dict[str, object]] = None
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


def x_build_graph_edges__mutmut_31(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
    for (source, target), count in sorted(None):
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


def x_build_graph_edges__mutmut_32(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
            None
        )
    return edges


def x_build_graph_edges__mutmut_33(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
                "XXfromXX": source,
                "to": target,
                "count": count,
                "avg_ms": 0.0,
                "errors": errors.get((source, target), 0),
            }
        )
    return edges


def x_build_graph_edges__mutmut_34(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
                "FROM": source,
                "to": target,
                "count": count,
                "avg_ms": 0.0,
                "errors": errors.get((source, target), 0),
            }
        )
    return edges


def x_build_graph_edges__mutmut_35(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
                "XXtoXX": target,
                "count": count,
                "avg_ms": 0.0,
                "errors": errors.get((source, target), 0),
            }
        )
    return edges


def x_build_graph_edges__mutmut_36(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
                "TO": target,
                "count": count,
                "avg_ms": 0.0,
                "errors": errors.get((source, target), 0),
            }
        )
    return edges


def x_build_graph_edges__mutmut_37(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
                "XXcountXX": count,
                "avg_ms": 0.0,
                "errors": errors.get((source, target), 0),
            }
        )
    return edges


def x_build_graph_edges__mutmut_38(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
                "COUNT": count,
                "avg_ms": 0.0,
                "errors": errors.get((source, target), 0),
            }
        )
    return edges


def x_build_graph_edges__mutmut_39(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
                "XXavg_msXX": 0.0,
                "errors": errors.get((source, target), 0),
            }
        )
    return edges


def x_build_graph_edges__mutmut_40(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
                "AVG_MS": 0.0,
                "errors": errors.get((source, target), 0),
            }
        )
    return edges


def x_build_graph_edges__mutmut_41(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
                "avg_ms": 1.0,
                "errors": errors.get((source, target), 0),
            }
        )
    return edges


def x_build_graph_edges__mutmut_42(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
                "XXerrorsXX": errors.get((source, target), 0),
            }
        )
    return edges


def x_build_graph_edges__mutmut_43(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
                "ERRORS": errors.get((source, target), 0),
            }
        )
    return edges


def x_build_graph_edges__mutmut_44(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
                "errors": errors.get(None, 0),
            }
        )
    return edges


def x_build_graph_edges__mutmut_45(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
                "errors": errors.get((source, target), None),
            }
        )
    return edges


def x_build_graph_edges__mutmut_46(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
                "errors": errors.get(0),
            }
        )
    return edges


def x_build_graph_edges__mutmut_47(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
                "errors": errors.get((source, target), ),
            }
        )
    return edges


def x_build_graph_edges__mutmut_48(flows: list[CiliumFlowEntry]) -> list[dict[str, object]]:
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
                "errors": errors.get((source, target), 1),
            }
        )
    return edges

mutants_x_build_graph_edges__mutmut['_mutmut_orig'] = x_build_graph_edges__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_1'] = x_build_graph_edges__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_2'] = x_build_graph_edges__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_3'] = x_build_graph_edges__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_4'] = x_build_graph_edges__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_5'] = x_build_graph_edges__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_6'] = x_build_graph_edges__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_7'] = x_build_graph_edges__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_8'] = x_build_graph_edges__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_9'] = x_build_graph_edges__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_10'] = x_build_graph_edges__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_11'] = x_build_graph_edges__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_12'] = x_build_graph_edges__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_13'] = x_build_graph_edges__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_14'] = x_build_graph_edges__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_15'] = x_build_graph_edges__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_16'] = x_build_graph_edges__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_17'] = x_build_graph_edges__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_18'] = x_build_graph_edges__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_19'] = x_build_graph_edges__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_20'] = x_build_graph_edges__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_21'] = x_build_graph_edges__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_22'] = x_build_graph_edges__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_23'] = x_build_graph_edges__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_24'] = x_build_graph_edges__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_25'] = x_build_graph_edges__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_26'] = x_build_graph_edges__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_27'] = x_build_graph_edges__mutmut_27 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_28'] = x_build_graph_edges__mutmut_28 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_29'] = x_build_graph_edges__mutmut_29 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_30'] = x_build_graph_edges__mutmut_30 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_31'] = x_build_graph_edges__mutmut_31 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_32'] = x_build_graph_edges__mutmut_32 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_33'] = x_build_graph_edges__mutmut_33 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_34'] = x_build_graph_edges__mutmut_34 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_35'] = x_build_graph_edges__mutmut_35 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_36'] = x_build_graph_edges__mutmut_36 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_37'] = x_build_graph_edges__mutmut_37 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_38'] = x_build_graph_edges__mutmut_38 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_39'] = x_build_graph_edges__mutmut_39 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_40'] = x_build_graph_edges__mutmut_40 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_41'] = x_build_graph_edges__mutmut_41 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_42'] = x_build_graph_edges__mutmut_42 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_43'] = x_build_graph_edges__mutmut_43 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_44'] = x_build_graph_edges__mutmut_44 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_45'] = x_build_graph_edges__mutmut_45 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_46'] = x_build_graph_edges__mutmut_46 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_47'] = x_build_graph_edges__mutmut_47 # type: ignore # mutmut generated
mutants_x_build_graph_edges__mutmut['x_build_graph_edges__mutmut_48'] = x_build_graph_edges__mutmut_48 # type: ignore # mutmut generated
