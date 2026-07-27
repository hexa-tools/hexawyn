# Auto-generated test for otel_dependency_graph_adapter

from __future__ import annotations


class TestOtelDependencyGraphAdapterUnit:
    def test_returns_list(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_dependency_graph_adapter import (
            OTelDependencyGraphAdapter,
        )
        from hexawyn.domain.models.service_dependency_graph import DependencyGraphRequest

        adapter = OTelDependencyGraphAdapter()
        result = adapter.fetch_edges(DependencyGraphRequest(time_window_minutes=60))
        assert isinstance(result, list)
