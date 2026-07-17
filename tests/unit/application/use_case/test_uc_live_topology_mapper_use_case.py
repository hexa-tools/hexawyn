"""Unit tests for LiveTopologyMapperUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.live_topology_mapper.live_topology_mapper_service_port import (
    LiveTopologyMapperServicePort,
)
from hexawyn.application.use_case.live_topology_mapper.live_topology_mapper_use_case import (
    LiveTopologyMapperUseCase,
)


class TestLiveTopologyMapperUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=LiveTopologyMapperServicePort)
        use_case = LiveTopologyMapperUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.map_topology.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=LiveTopologyMapperServicePort)
        mock_service.map_topology.side_effect = RuntimeError("test error")
        use_case = LiveTopologyMapperUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
