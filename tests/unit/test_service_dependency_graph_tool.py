from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.service_dependency_graph_port import (
    ServiceDependencyGraphPort,
)


class TestServiceDependencyGraphTool:
    def test_returns_graph(self) -> None:
        from hexawyn.mcp.tools.service_dependency_graph import (
            service_dependency_graph,
        )

        with patch("hexawyn.mcp.server.build_service_dependency_graph_adapter") as m:
            a = MagicMock(spec=ServiceDependencyGraphPort)
            a.fetch_edges.return_value = [
                {
                    "from": "api-gateway",
                    "to": "auth-service",
                    "count": 12450,
                    "avg_ms": 82.0,
                    "errors": 249,
                },
                {
                    "from": "payment-service",
                    "to": "postgres-db",
                    "count": 24600,
                    "avg_ms": 35.0,
                    "errors": 0,
                },
            ]
            m.return_value = a
            r = service_dependency_graph()
        assert r["error"] is None
        assert len(r["nodes"]) == 4
        assert len(r["edges"]) == 2

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.service_dependency_graph import (
            service_dependency_graph,
        )

        with patch(
            "hexawyn.mcp.server.build_service_dependency_graph_adapter",
            side_effect=RuntimeError("boom"),
        ):
            r = service_dependency_graph()
        assert r["error"] == "boom"
