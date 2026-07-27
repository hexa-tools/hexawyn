from __future__ import annotations

from hexawyn.adapters.secondary.gitops.otel_http_client import get_jaeger_dependencies
from hexawyn.application.ports.driven.service_dependency_graph_port import (
    ServiceDependencyGraphPort,
)
from hexawyn.domain.models.service_dependency_graph import DependencyGraphRequest


class OTelDependencyGraphAdapter(ServiceDependencyGraphPort):
    def fetch_edges(self, request: DependencyGraphRequest) -> list[dict[str, object]]:
        import time

        end_ts = int(time.time() * 1_000_000)
        lookback = request.time_window_minutes * 60 * 1_000_000

        deps = get_jaeger_dependencies(end_ts=end_ts, lookback=lookback)
        result: list[dict[str, object]] = []
        for dep in deps:
            result.append(
                {
                    "source": dep["parent"],
                    "target": dep["child"],
                    "call_count": dep["callCount"],
                }
            )
        return result
