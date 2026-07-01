from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ServiceNode:
    service_name: str


@dataclass(frozen=True)
class ServiceEdge:
    source: str
    target: str
    call_count: int
    avg_latency_ms: float
    error_rate: float


@dataclass(frozen=True)
class DependencyGraphRequest:
    time_window_minutes: int = 60


@dataclass(frozen=True)
class DependencyGraph:
    nodes: list[ServiceNode]
    edges: list[ServiceEdge]
    time_window_minutes: int

    @staticmethod
    def compute(
        request: DependencyGraphRequest,
        raw_edges: list[dict[str, object]],
    ) -> DependencyGraph:
        merger: dict[str, dict[str, object]] = {}
        for r in raw_edges:
            src = str(r.get("from", ""))
            tgt = str(r.get("to", ""))
            key = f"{src}|{tgt}"
            if key not in merger:
                merger[key] = {
                    "from": src,
                    "to": tgt,
                    "count": 0,
                    "total_ms": 0.0,
                    "total_errors": 0,
                }
            m = merger[key]
            m["count"] = int(str(m["count"])) + int(str(r.get("count", 0)))
            m["total_ms"] = float(str(m["total_ms"])) + float(str(r.get("avg_ms", 0))) * int(
                str(r.get("count", 0))
            )
            m["total_errors"] = float(str(m["total_errors"])) + float(str(r.get("errors", 0)))

        nodes_set: set[str] = set()
        edges: list[ServiceEdge] = []
        for m in merger.values():
            src = str(m["from"])
            tgt = str(m["to"])
            count = int(str(m["count"]))
            total_ms = float(str(m["total_ms"]))
            total_errors = float(str(m["total_errors"]))
            avg_ms = total_ms / count if count > 0 else 0.0
            error_rate = total_errors / count if count > 0 else 0.0
            nodes_set.add(src)
            nodes_set.add(tgt)
            edges.append(
                ServiceEdge(
                    source=src,
                    target=tgt,
                    call_count=count,
                    avg_latency_ms=round(avg_ms, 2),
                    error_rate=round(error_rate, 4),
                )
            )

        nodes = [ServiceNode(service_name=n) for n in sorted(nodes_set)]
        return DependencyGraph(
            nodes=nodes, edges=edges, time_window_minutes=request.time_window_minutes
        )
