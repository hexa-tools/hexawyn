from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.cilium.cilium_service_graph.cilium_service_graph_use_case import (
    CiliumServiceGraphUseCase,
)
from hexawyn.application.use_case.cilium.cilium_service_graph.command import (
    CiliumServiceGraphCommand,
)
from hexawyn.application.use_case.cilium.cilium_service_graph.response import (
    CiliumServiceGraphResponse,
)


class TestCiliumServiceGraphUseCase:
    def test_execute_builds_graph(self) -> None:
        port = MagicMock()
        port.fetch_edges.return_value = [
            {"from": "web-0", "to": "db-0", "count": 2, "avg_ms": 0.0, "errors": 0}
        ]

        response = CiliumServiceGraphUseCase(port=port).execute(
            CiliumServiceGraphCommand(time_window_minutes=30)
        )

        assert isinstance(response, CiliumServiceGraphResponse)
        assert response.time_window_minutes == 30  # noqa: PLR2004
        assert "web-0" in response.nodes
        assert response.edges[0]["source"] == "web-0"
        assert response.edges[0]["call_count"] == 2  # noqa: PLR2004

    def test_execute_empty_graph_with_note(self) -> None:
        port = MagicMock()
        port.fetch_edges.return_value = []

        response = CiliumServiceGraphUseCase(port=port).execute(CiliumServiceGraphCommand())

        assert response.nodes == []
        assert response.edges == []
        assert response.note is not None
