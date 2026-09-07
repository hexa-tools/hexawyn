from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.observability.service_dependency_graph.command import (
    ServiceDependencyGraphCommand,
)
from hexawyn.application.use_case.observability.service_dependency_graph.response import (
    ServiceDependencyGraphResponse,
)
from hexawyn.application.use_case.observability.service_dependency_graph.service_dependency_graph_use_case import (  # noqa: E501
    UseCaseDependencyGraphUseCase,
)


class TestServiceDependencyGraphUseCase:
    def test_execute_returns_service_dependency_graph_response(self) -> None:
        port = MagicMock()
        port.fetch_edges.return_value = []

        use_case = UseCaseDependencyGraphUseCase(port=port)
        result = use_case.execute(ServiceDependencyGraphCommand())

        assert isinstance(result, ServiceDependencyGraphResponse)

    def test_execute_calls_port_with_request(self) -> None:
        port = MagicMock()
        port.fetch_edges.return_value = []

        use_case = UseCaseDependencyGraphUseCase(port=port)
        use_case.execute(ServiceDependencyGraphCommand(time_window_minutes=30))

        assert port.fetch_edges.call_count == 1
