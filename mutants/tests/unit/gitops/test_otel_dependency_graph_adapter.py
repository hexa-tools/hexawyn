from __future__ import annotations

from unittest.mock import patch


class TestOtelDependencyGraphAdapterUnit:
    def test_returns_list(self) -> None:
        from hexawyn.domain.models.service_dependency_graph import DependencyGraphRequest
        from hexawyn.infrastructure.adapters.secondary.gitops.otel_dependency_graph_adapter import (
            OTelDependencyGraphAdapter,
        )

        adapter = OTelDependencyGraphAdapter()
        result = adapter.fetch_edges(DependencyGraphRequest(time_window_minutes=60))
        assert isinstance(result, list)

    def test_edges_populated_with_mocked_deps(self) -> None:
        from hexawyn.domain.models.service_dependency_graph import DependencyGraphRequest
        from hexawyn.infrastructure.adapters.secondary.gitops.otel_dependency_graph_adapter import (
            OTelDependencyGraphAdapter,
        )

        mock_deps = [
            {"parent": "frontend", "child": "backend", "callCount": 42},
            {"parent": "backend", "child": "db", "callCount": 15},
        ]
        with patch(
            "hexawyn.infrastructure.adapters.secondary.gitops.otel_dependency_graph_adapter.get_jaeger_dependencies",
            return_value=mock_deps,
        ):
            adapter = OTelDependencyGraphAdapter()
            result = adapter.fetch_edges(DependencyGraphRequest(time_window_minutes=30))
            assert len(result) == 2  # noqa: PLR2004
            assert result[0]["source"] == "frontend"
            assert result[1]["target"] == "db"
