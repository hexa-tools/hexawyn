from __future__ import annotations

from hexawyn.application.ports.driving.live_topology_mapper.live_topology_mapper_command import (
    LiveTopologyMapperCommand,
)
from hexawyn.application.ports.driving.live_topology_mapper.live_topology_mapper_response import (
    LiveTopologyMapperResponse,
)
from hexawyn.application.ports.driving.live_topology_mapper.live_topology_mapper_service_port import (
    LiveTopologyMapperServicePort,
)


class LiveTopologyMapperUseCase:
    def __init__(self, service: LiveTopologyMapperServicePort) -> None:
        self._service = service

    def execute(self, command: LiveTopologyMapperCommand) -> LiveTopologyMapperResponse:
        return self._service.map_topology(command)
