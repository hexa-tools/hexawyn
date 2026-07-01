from __future__ import annotations

from hexawyn.adapters.secondary.gitops.otel_dependency_graph_adapter import (
    OTelDependencyGraphAdapter,
)
from hexawyn.application.ports.driven.service_dependency_graph_port import (
    ServiceDependencyGraphPort,
)
from hexawyn.domain.models.service_dependency_graph import DependencyGraphRequest


class TestOTelDependencyGraphAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(OTelDependencyGraphAdapter(), ServiceDependencyGraphPort)

    def test_fetch_returns_empty(self) -> None:
        r = OTelDependencyGraphAdapter().fetch_edges(DependencyGraphRequest())
        assert r == []
