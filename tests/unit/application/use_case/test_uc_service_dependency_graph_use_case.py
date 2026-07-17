"""Unit tests for ServiceDependencyGraphUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.service_dependency_graph.service_dependency_graph_service_port import (
    ServiceDependencyGraphServicePort,
)
from hexawyn.application.use_case.service_dependency_graph.service_dependency_graph_use_case import (
    ServiceDependencyGraphUseCase,
)


class TestServiceDependencyGraphUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=ServiceDependencyGraphServicePort)
        use_case = ServiceDependencyGraphUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.build.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=ServiceDependencyGraphServicePort)
        mock_service.build.side_effect = RuntimeError("test error")
        use_case = ServiceDependencyGraphUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
