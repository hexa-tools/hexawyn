from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.live_topology_mapper.live_topology_mapper_command import (
    LiveTopologyMapperCommand,
)
from hexawyn.application.ports.driving.live_topology_mapper.live_topology_mapper_response import (
    LiveTopologyMapperResponse,
)
from hexawyn.application.use_case.live_topology_mapper.live_topology_mapper_use_case import (
    LiveTopologyMapperUseCase,
)


class TestLiveTopologyMapperUseCase:
    def test_execute_delegates_to_service(self) -> None:
        service = MagicMock()
        expected_response = LiveTopologyMapperResponse()
        service.map_topology.return_value = expected_response
        use_case = LiveTopologyMapperUseCase(service=service)
        command = LiveTopologyMapperCommand(namespace="production")

        response = use_case.execute(command)

        service.map_topology.assert_called_once_with(command)
        assert response is expected_response
